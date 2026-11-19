#!/usr/bin/env python3
"""MOTHWAKE story database, scoring model and similarity checker.

  storydb.py init                      create stories/stories.db
  storydb.py import stories/concepts   load/refresh every *.json concept
  storydb.py list                      ranked table (priority score)
  storydb.py similar <id>              similarity of one story vs all others
  storydb.py check <file.json>         similarity gate for a NEW concept before import
  storydb.py hooks <id>                show hooks + duplicate-opening check across DB

Scores are a prioritisation aid, not a prediction of views. See stories/SCORING_MODEL.md.
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "stories" / "stories.db"

REQUIRED = ["id", "title", "category", "format", "concept", "hooks", "characters", "setting", "conflict",
            "escalation", "reveal", "ending", "emotional_objective", "visual_requirements",
            "production_effort", "twist_type", "originality_review", "scores"]
CRITERIA = {  # name: (weight, higher_is_better)
    "topic_demand": (1.5, True), "audience_curiosity": (1.5, True), "hook_strength": (2.0, True),
    "emotional_impact": (1.0, True), "story_clarity": (1.0, True), "suspense": (1.0, True),
    "retention_potential": (1.5, True), "rewatch_potential": (1.0, True), "shareability": (1.0, True),
    "production_complexity": (1.0, False), "originality": (1.5, True), "brand_suitability": (1.5, True),
}
SIM_WARN, SIM_BLOCK = 0.30, 0.45


def conn():
    DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB)
    c.execute("""CREATE TABLE IF NOT EXISTS stories(
        id TEXT PRIMARY KEY, title TEXT, category TEXT, format TEXT, twist_type TEXT,
        status TEXT DEFAULT 'concept', priority REAL, data TEXT)""")
    return c


def priority(scores: dict) -> float:
    """Weighted mean on a 0-100 scale. Complexity is inverted (simpler = higher)."""
    tot = wsum = 0.0
    for k, (w, up) in CRITERIA.items():
        v = float(scores[k])
        if not 1 <= v <= 5:
            raise ValueError(f"{k}={v} must be 1-5")
        v = v if up else 6 - v
        tot += w * (v - 1) / 4
        wsum += w
    return round(100 * tot / wsum, 1)


def validate(d: dict) -> list[str]:
    errs = [f"missing field: {k}" for k in REQUIRED if k not in d]
    if "scores" in d:
        errs += [f"missing score: {k}" for k in CRITERIA if k not in d["scores"]]
    if len(d.get("hooks", [])) < 5:
        errs.append("need ≥5 hook alternatives")
    return errs


def shingles(text: str, n=3) -> set:
    w = re.findall(r"[a-z']+", text.lower())
    stop = {"the", "a", "an", "and", "of", "to", "in", "is", "it", "her", "his", "their", "that", "she", "he",
            "they", "on", "at", "for", "with", "was", "but", "as", "by", "from", "into", "who", "what", "has"}
    w = [x for x in w if x not in stop]
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))} | set(w)


def text_of(d):
    return " ".join(str(d.get(k, "")) for k in ("concept", "setting", "conflict", "escalation", "reveal", "ending"))


def similarity(a: dict, b: dict) -> float:
    sa, sb = shingles(text_of(a)), shingles(text_of(b))
    jac = len(sa & sb) / max(1, len(sa | sb))
    twist = 0.25 if a.get("twist_type") == b.get("twist_type") else 0.0
    setting = 0.10 if a.get("setting_type") and a.get("setting_type") == b.get("setting_type") else 0.0
    return round(min(1.0, jac * 2.2 + twist + setting), 3)


def all_stories(c):
    return {r[0]: json.loads(r[1]) for r in c.execute("SELECT id, data FROM stories")}


def cmd_import(folder):
    c = conn()
    n = 0
    for f in sorted(Path(folder).glob("*.json")):
        d = json.loads(f.read_text())
        errs = validate(d)
        if errs:
            print(f"[SKIP] {f.name}: {'; '.join(errs)}")
            continue
        c.execute("INSERT OR REPLACE INTO stories VALUES(?,?,?,?,?,?,?,?)",
                  (d["id"], d["title"], d["category"], d["format"], d["twist_type"],
                   d.get("status", "concept"), priority(d["scores"]), json.dumps(d)))
        n += 1
    c.commit()
    print(f"imported {n} stories → {DB.relative_to(ROOT)}")


def cmd_list():
    c = conn()
    print(f"{'id':8} {'prio':>5}  {'format':9} {'category':24} {'twist':20} title")
    for r in c.execute("SELECT id, priority, format, category, twist_type, title FROM stories ORDER BY priority DESC"):
        print(f"{r[0]:8} {r[1]:5.1f}  {r[2]:9} {r[3][:24]:24} {r[4][:20]:20} {r[5]}")


def report(d, others):
    rows = sorted(((similarity(d, o), oid) for oid, o in others.items() if oid != d["id"]), reverse=True)
    worst = rows[0][0] if rows else 0
    for s, oid in rows[:5]:
        flag = "BLOCK" if s >= SIM_BLOCK else "WARN" if s >= SIM_WARN else "ok"
        print(f"  {s:.3f} {flag:5} vs {oid} ({others[oid]['title']})")
    return worst


def cmd_similar(sid):
    st = all_stories(conn())
    print(f"similarity for {sid} — {st[sid]['title']}")
    report(st[sid], st)


def cmd_check(path):
    d = json.loads(Path(path).read_text())
    errs = validate(d)
    for e in errs:
        print("[FAIL]", e)
    worst = report(d, all_stories(conn()))
    if worst >= SIM_BLOCK:
        print(f"[FAIL] too similar to an existing story ({worst:.2f} ≥ {SIM_BLOCK})")
    sys.exit(1 if errs or worst >= SIM_BLOCK else 0)


def opening(h):
    return " ".join(re.findall(r"[a-z']+", h.lower())[:3])


def cmd_hooks(sid):
    st = all_stories(conn())
    seen = {}
    for oid, o in st.items():
        for h in o["hooks"]:
            seen.setdefault(opening(h["line"]), []).append(oid)
    for h in st[sid]["hooks"]:
        dup = [x for x in seen[opening(h["line"])] if x != sid]
        print(f"- [{h['structure']}] {h['line']}" + (f"   ⚠ same opening as {dup}" if dup else ""))
        print(f"    first visual: {h['first_visual']}")


if __name__ == "__main__":
    a = sys.argv[1:] or ["list"]
    {"init": lambda: (conn(), print("ok")), "import": lambda: cmd_import(a[1] if len(a) > 1 else ROOT / "stories/concepts"),
     "list": cmd_list, "similar": lambda: cmd_similar(a[1]), "check": lambda: cmd_check(a[1]),
     "hooks": lambda: cmd_hooks(a[1])}[a[0]]()
