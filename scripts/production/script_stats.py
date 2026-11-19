#!/usr/bin/env python3
"""Measure spoken lines in a MOTHWAKE script and export them for voice production.

  script_stats.py episodes/EP001/script.md            word/char counts + runtime estimate
  script_stats.py episodes/EP001/script.md --vo OUT   also write vo.json (one entry per line)

Speaker tag = bold label at line start, e.g. **NARR:** / **CAL:** / **ECHO:** / **VISITOR 1974 (on tape):**
Parenthetical directions like (beat) or (whispered) are stripped from the spoken text; (beat)
becomes a pause marker. Counts are measurements of the text, not of recorded audio.
"""
import json
import re
import sys
from pathlib import Path

LINE = re.compile(r"^\*\*([A-Z][A-Z0-9 ]*?)(?: \(([^)]*)\))?:\*\*\s*(.*)$", re.M)


def parse(path):
    body = Path(path).read_text().split("## Notes for review")[0]
    out = []
    for m in LINE.finditer(body):
        who, note, txt = m.group(1).strip(), m.group(2), m.group(3)
        direction = " ".join(re.findall(r"^\(([^)]*)\)", txt.strip()))
        pauses = txt.count("(beat)")
        spoken = re.sub(r"\([^)]*\)", " ", txt)
        spoken = re.sub(r"\*", "", spoken)
        spoken = re.sub(r"\s+", " ", spoken).strip()
        if spoken:
            out.append({"speaker": who, "note": note, "direction": direction, "text": spoken, "beats": pauses})
    return out


def main():
    p = sys.argv[1]
    lines = parse(p)
    words = sum(len(l["text"].split()) for l in lines)
    chars = sum(len(l["text"]) for l in lines)
    beats = sum(l["beats"] for l in lines)
    by = {}
    for l in lines:
        by.setdefault(l["speaker"], [0, 0])
        by[l["speaker"]][0] += len(l["text"].split())
        by[l["speaker"]][1] += len(l["text"])
    print(f"{len(lines)} spoken lines · {words} words · {chars} characters · {beats} beats")
    for s, (w, c) in by.items():
        print(f"  {s:14} {w:5} words {c:6} chars")
    for wpm in (135, 145):
        print(f"  speech at {wpm} wpm: {words / wpm:.1f} min (+ beats {beats * 0.8 / 60:.1f} min)")
    if "--vo" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--vo") + 1])
        out.write_text(json.dumps({"source": p, "lines": [dict(id=f"L{i + 1:03d}", **l) for i, l in enumerate(lines)]},
                                  indent=2, ensure_ascii=False))
        print("wrote", out)


if __name__ == "__main__":
    main()
