#!/usr/bin/env python3
"""MOTHWAKE isolation verifier.

Usage:
  .venv/bin/python scripts/verify_isolation.py baseline   # record fingerprints of protected areas
  .venv/bin/python scripts/verify_isolation.py verify     # check isolation; exit 1 on any failure

Protected areas are things MOTHWAKE must never change: any Chrono Tales
location found on this machine, and user-level Claude config. The verifier
only reads them; it never writes outside the MOTHWAKE project.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
BASELINE = Path(os.environ.get("MOTHWAKE_BASELINE", PROJECT / ".isolation" / "baseline.json"))
SEARCH_ROOTS = [Path(p) for p in os.environ.get(
    "MOTHWAKE_SEARCH_ROOTS", "/home:/root:/opt:/srv:/workspace").split(":")]
SKIP_DIRS = {".cache", ".npm", ".cargo", ".rustup", ".gradle", "node_modules",
             ".venv", "site-packages", ".git", ".bun", ".nix-defexpr", ".local"}
# User-level config MOTHWAKE must not modify (fingerprinted when present).
USER_CONFIG = [Path("/root/.claude/settings.json"), Path("/root/.claude/CLAUDE.md"),
               Path("/root/.claude/skills"), Path("/root/.claude/agents")]
# Docs allowed to mention Chrono Tales by name (they describe the policy).
CHRONO_MENTION_ALLOW = {"ISOLATION_POLICY.md", "README.md", "CLAUDE.md",
                        "verify_isolation.py", "test_isolation.sh"}
CHRONO_MENTION_ALLOW_DIRS = {"reports", "plans", ".isolation"}


def sha_tree(p: Path) -> dict:
    """Return {relpath: sha256} for a file or directory (symlinks not followed)."""
    out = {}
    if p.is_file():
        out["."] = hashlib.sha256(p.read_bytes()).hexdigest()
        return out
    for root, dirs, files in os.walk(p, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d != ".in_use")
        for f in sorted(files):
            fp = Path(root) / f
            if fp.is_symlink():
                out[str(fp.relative_to(p))] = "symlink->" + os.readlink(fp)
            else:
                try:
                    out[str(fp.relative_to(p))] = hashlib.sha256(fp.read_bytes()).hexdigest()
                except OSError as e:
                    out[str(fp.relative_to(p))] = f"unreadable:{e.errno}"
    return out


def find_chrono() -> list[Path]:
    hits = []
    for r in SEARCH_ROOTS:
        if not r.exists():
            continue
        for root, dirs, files in os.walk(r, followlinks=False):
            rp = Path(root)
            if rp == PROJECT or PROJECT in rp.parents:
                dirs[:] = []
                continue
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in list(dirs) + files:
                low = name.lower().replace("-", "").replace("_", "").replace(" ", "")
                if "chronotales" in low or "chronotale" in low:
                    hits.append(rp / name)
                    if name in dirs:
                        dirs.remove(name)
    return sorted(hits)


def protected_targets() -> list[Path]:
    return find_chrono() + [p for p in USER_CONFIG if p.exists()]


def cmd_baseline() -> int:
    data = {"created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "project": str(PROJECT), "targets": {}}
    for t in protected_targets():
        data["targets"][str(t)] = sha_tree(t)
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    BASELINE.write_text(json.dumps(data, indent=2, sort_keys=True))
    print(f"baseline written: {BASELINE} ({len(data['targets'])} protected targets)")
    for t in data["targets"]:
        print("  -", t)
    return 0


def cmd_verify() -> int:
    results: list[tuple[str, bool, str]] = []
    add = lambda name, ok, detail="": results.append((name, bool(ok), detail))

    # 1. project location and venv
    add("project root is /home/user/mothwake", PROJECT == Path("/home/user/mothwake"), str(PROJECT))
    venv = PROJECT / ".venv"
    py = Path(sys.prefix).resolve()
    add("project venv exists inside project", (venv / "bin" / "python").exists())
    add("verifier runs from project venv", py == venv.resolve(), f"running_prefix={py}")

    # 2. no symlink inside project escapes it
    escapes = []
    for root, dirs, files in os.walk(PROJECT, followlinks=False):
        if ".venv" in Path(root).parts:
            dirs[:] = []
            continue
        for n in dirs + files:
            p = Path(root) / n
            if p.is_symlink():
                tgt = (p.parent / os.readlink(p)).resolve()
                if PROJECT not in tgt.parents and tgt != PROJECT:
                    escapes.append(f"{p} -> {tgt}")
    add("no symlinks escape the project", not escapes, "; ".join(escapes))

    # 3. project Claude config is self-contained (no hooks, no outside paths)
    settings = PROJECT / ".claude" / "settings.json"
    hooks_ok, detail = True, ""
    if settings.exists():
        try:
            s = json.loads(settings.read_text())
            if s.get("hooks"):
                hooks_ok, detail = False, "project settings define hooks (review required)"
        except json.JSONDecodeError as e:
            hooks_ok, detail = False, f"invalid JSON: {e}"
    add("project .claude/settings.json has no hooks", hooks_ok, detail)

    # 4. MOTHWAKE skills/agents live only in the project
    leaked = []
    for d in (Path("/root/.claude/skills"), Path("/root/.claude/agents")):
        if d.exists():
            leaked += [str(x) for x in d.iterdir() if "mothwake" in x.name.lower()
                       or x.name in MOTHWAKE_SKILL_NAMES]
    add("no MOTHWAKE skills/agents in user-level config", not leaked, "; ".join(leaked))

    # 5. project files do not reference Chrono Tales paths/assets
    refs = []
    for root, dirs, files in os.walk(PROJECT):
        rp = Path(root)
        dirs[:] = [d for d in dirs if d not in {".venv", ".git", "__pycache__"}]
        if set(rp.relative_to(PROJECT).parts) & CHRONO_MENTION_ALLOW_DIRS:
            continue
        for f in files:
            if f in CHRONO_MENTION_ALLOW:
                continue
            fp = rp / f
            try:
                txt = fp.read_text(errors="ignore").lower()
            except OSError:
                continue
            if "chrono tales" in txt or "chrono-tales" in txt or "chrono_tales" in txt:
                refs.append(str(fp.relative_to(PROJECT)))
    add("no project file references Chrono Tales", not refs, "; ".join(refs))

    # 6. protected areas unchanged since baseline
    if not BASELINE.exists():
        add("baseline present", False, f"missing {BASELINE}; run 'baseline' first")
    else:
        base = json.loads(BASELINE.read_text())
        add("baseline present", True, base.get("created", ""))
        for t, fp in base["targets"].items():
            p = Path(t)
            cur = sha_tree(p) if p.exists() else None
            add(f"protected unchanged: {t}", cur == fp,
                "missing now" if cur is None else ("" if cur == fp else "fingerprint differs"))
        new = [str(t) for t in find_chrono() if str(t) not in base["targets"]]
        add("no new unbaselined Chrono Tales locations", not new,
            "re-run baseline after review: " + "; ".join(new))

    width = max(len(r[0]) for r in results)
    failed = 0
    for name, ok, detail in results:
        failed += not ok
        print(f"[{'PASS' if ok else 'FAIL'}] {name.ljust(width)}  {detail}")
    print(f"\n{len(results) - failed}/{len(results)} checks passed")
    return 1 if failed else 0


MOTHWAKE_SKILL_NAMES = {
    "mothwake-brand-development", "mothwake-logo-and-visual-identity", "horror-market-research",
    "horror-trend-intelligence", "viral-hook-analysis", "horror-story-development",
    "horror-scriptwriting", "horror-storyboard-generation", "2d-character-consistency",
    "2d-environment-design", "google-flow-production", "elevenlabs-audio-production",
    "horror-video-assembly", "ffmpeg-media-processing", "thumbnail-and-title-optimization",
    "horror-quality-control", "youtube-analytics", "youtube-monetization-analysis",
}

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "verify"
    sys.exit({"baseline": cmd_baseline, "verify": cmd_verify}.get(cmd, lambda: (print(__doc__), 2)[1])())
