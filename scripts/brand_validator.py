#!/usr/bin/env python3
"""MOTHWAKE brand asset validator.

  lock      record SHA-256 of every approved asset in brand/APPROVED_ASSETS.lock
            (run only after the owner approves a brand change)
  check     verify every approved asset exists and is unchanged
  episode   check an episode manifest only references approved, unchanged assets:
            .venv/bin/python scripts/brand_validator.py episode episodes/EP001/manifest.json

Exit code 1 on any problem. Never modifies or replaces assets.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "brand" / "APPROVED_ASSETS.lock"
APPROVED_DIRS = ["brand/logo", "brand/kit", "brand/fonts", "brand/sound", "brand/video"]
ROLES = {  # role → path every episode must use for that role
    "logo_primary": "brand/logo/mothwake_primary_transparent.svg",
    "watermark": "brand/kit/watermark_gold.png",
    "watermark_light_scenes": "brand/kit/watermark_white.png",
    "font_display": "brand/fonts/Cinzel[wght].ttf",
    "font_title": "brand/fonts/CormorantGaramond[wght].ttf",
    "font_caption": "brand/fonts/Inter[opsz,wght].ttf",
    "sound_signature": "brand/sound/mothwake_signature.wav",
    "sound_outro": "brand/sound/mothwake_outro.wav",
    "outro_16x9": "brand/video/mothwake_outro_1920x1080.mp4",
    "outro_9x16": "brand/video/mothwake_outro_1080x1920.mp4",
}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def lock():
    files = {}
    for d in APPROVED_DIRS:
        for p in sorted((ROOT / d).rglob("*")):
            if p.is_file() and not p.name.startswith("."):
                files[str(p.relative_to(ROOT))] = sha(p)
    LOCK.write_text(json.dumps({"locked": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                "status": "APPROVED by owner 2026-11-19 (logo concept B)",
                                "roles": ROLES, "files": files}, indent=2))
    print(f"locked {len(files)} assets → {LOCK.relative_to(ROOT)}")
    return 0


def load():
    if not LOCK.exists():
        print("FAIL no APPROVED_ASSETS.lock — run 'lock' after approval")
        sys.exit(1)
    return json.loads(LOCK.read_text())


def check() -> int:
    data, bad = load(), 0
    for rel, h in data["files"].items():
        p = ROOT / rel
        if not p.exists():
            print(f"[FAIL] missing   {rel}"); bad += 1
        elif sha(p) != h:
            print(f"[FAIL] modified  {rel} (not the approved version)"); bad += 1
    for role, rel in data["roles"].items():
        if rel not in data["files"]:
            print(f"[FAIL] role {role} points to unapproved {rel}"); bad += 1
    print(f"{len(data['files']) - bad}/{len(data['files'])} approved assets OK")
    return 1 if bad else 0


def episode(manifest: str) -> int:
    data, bad = load(), 0
    m = json.loads(Path(manifest).read_text())
    used = m.get("brand_assets", {})
    for role in data["roles"]:
        if role not in used:
            print(f"[WARN] role {role} not declared in manifest")
    for role, rel in used.items():
        if rel != data["roles"].get(role):
            print(f"[FAIL] {role}: uses {rel}, approved is {data['roles'].get(role)}"); bad += 1
        elif not (ROOT / rel).exists() or sha(ROOT / rel) != data["files"].get(rel):
            print(f"[FAIL] {role}: {rel} missing or modified"); bad += 1
    print("episode brand check:", "PASS" if not bad else f"FAIL ({bad})")
    return 1 if bad else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "lock":
        sys.exit(lock())
    if cmd == "check":
        sys.exit(check())
    if cmd == "episode":
        sys.exit(episode(sys.argv[2]))
    print(__doc__); sys.exit(2)
