#!/usr/bin/env python3
"""System tests: agent/skill interfaces, story engine gates, analytics. Run with the project venv."""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable
res = []


def check(n, ok, d=""):
    res.append((n, bool(ok), d))


# Agents ↔ skills interfaces
skills = {p.parent.name for p in (ROOT / ".claude/skills").glob("*/SKILL.md")}
agents = {p.stem: p.read_text() for p in (ROOT / ".claude/agents").glob("*.md")}
check("18 skills present", len(skills) == 18, str(len(skills)))
check("14 agents present", len(agents) == 14, str(len(agents)))
for name, txt in agents.items():
    used = re.search(r"\*\*Skills to load:\*\* (.+?) \(", txt).group(1).split(", ")
    check(f"agent {name}: all skills exist", set(used) <= skills, str(set(used) - skills))
    check(f"agent {name}: has hand-off + owned outputs", "**Hand-off:**" in txt and "**Owns" in txt)
for s in skills:
    t = (ROOT / ".claude/skills" / s / "SKILL.md").read_text()
    check(f"skill {s}: frontmatter name matches", f"name: {s}\n" in t)
# every agent hand-off target maps to an existing agent or the owner
targets = set(re.findall(r"hand to \*\*(.+?)\*\*", "".join(agents.values())))
names = {n.replace("-", " ").lower() for n in agents}
bad = [t for t in targets if not t.lower().startswith("owner") and t.lower() not in names]
check("all hand-off targets resolve", not bad, str(bad))

# Story engine
r = subprocess.run([PY, ROOT / "scripts/story/storydb.py", "import", ROOT / "stories/concepts"], capture_output=True, text=True)
check("story import: all concepts valid", "SKIP" not in r.stdout, r.stdout.strip())
with tempfile.TemporaryDirectory() as td:
    d = json.loads((ROOT / "stories/concepts/MW003.json").read_text())
    d["id"] = "TMP1"
    Path(td, "dup.json").write_text(json.dumps(d))
    r = subprocess.run([PY, ROOT / "scripts/story/storydb.py", "check", Path(td, "dup.json")], capture_output=True, text=True)
    check("similarity gate blocks near-duplicate", r.returncode == 1)
    d2 = dict(d, hooks=d["hooks"][:2], id="TMP2")
    Path(td, "few.json").write_text(json.dumps(d2))
    r = subprocess.run([PY, ROOT / "scripts/story/storydb.py", "check", Path(td, "few.json")], capture_output=True, text=True)
    check("hook gate blocks <5 hooks", r.returncode == 1)
    # Analytics with explicit fake fixture into temp db
    db = Path(td, "t.db")
    subprocess.run([PY, ROOT / "scripts/analytics/analytics.py", "ingest", "youtube",
                    ROOT / "tests/fixtures/FAKE_youtube_export_TEST_ONLY.csv", "--db", db], check=True, capture_output=True)
    out = subprocess.run([PY, ROOT / "scripts/analytics/analytics.py", "cohorts", "--db", db], capture_output=True, text=True).stdout
    check("analytics cohorts split short vs long", "'short'" in out and "'long'" in out, out.strip())
    subprocess.run([PY, ROOT / "scripts/analytics/analytics.py", "dashboard", "--db", db, "--out", Path(td, "d.html")], check=True,
                   capture_output=True)
    check("dashboard renders data rows", "TEST short A" in Path(td, "d.html").read_text())
check("live dashboard shows no fabricated data", "No platform data has been ingested yet" in
      (ROOT / "analytics/dashboard.html").read_text())

f = 0
for n, ok, d in res:
    f += not ok
    print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d if not ok else ''}")
print(f"\n{len(res) - f}/{len(res)} system tests passed")
sys.exit(1 if f else 0)
