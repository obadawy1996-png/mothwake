#!/usr/bin/env python3
"""MOTHWAKE automated quality control.

  .venv/bin/python scripts/production/qc.py episodes/EP000/manifest.json

Checks every rendered file for the episode and writes episodes/<id>/QC_REPORT.md.
Exit 1 if any blocking check fails. QC never fixes anything silently.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGETS = {"short": (35, 60), "long": (300, 600)}


def probe(p):
    return json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(p)],
                                     capture_output=True, text=True).stdout)


def ff_filter(p, af=None, vf=None):
    cmd = ["ffmpeg", "-nostats", "-i", str(p)]
    if af:
        cmd += ["-af", af]
    if vf:
        cmd += ["-vf", vf]
    cmd += ["-f", "null", "-"]
    return subprocess.run(cmd, capture_output=True, text=True).stderr


def main(mpath):
    mp = Path(mpath).resolve()
    ep = mp.parent
    m = json.loads(mp.read_text())
    rows = []

    def add(name, ok, detail="", blocking=True):
        rows.append((name, ok, detail, blocking))

    r = subprocess.run([sys.executable, str(ROOT / "scripts/brand_validator.py"), "episode", str(mp)],
                       capture_output=True, text=True)
    add("brand assets approved & unchanged", r.returncode == 0, r.stdout.strip().splitlines()[-1])
    led = m.get("licence_ledger", [])
    missing = [x["asset"] for x in led if not x.get("licence") or x.get("licence") == "unknown"]
    add("licence ledger complete", led and not missing, f"{len(led)} entries; unknown: {missing}")
    add("story originality review present", bool(m.get("originality_review")))
    add("human approval recorded (required before publish)", bool(m.get("approvals", {}).get("owner_final")),
        "pending — publishing stays blocked", blocking=False)

    files = sorted((ep / "master").glob("*.mp4")) + sorted((ep / "exports").glob("*.mp4"))
    add("rendered files exist", bool(files), f"{len(files)} files")
    W, H = m["resolution"]
    lo, hi = TARGETS[m["format"]]
    for f in files:
        name = f.relative_to(ep)
        d = probe(f)
        v = next(s for s in d["streams"] if s["codec_type"] == "video")
        a = [s for s in d["streams"] if s["codec_type"] == "audio"]
        dur = float(d["format"]["duration"])
        add(f"{name}: resolution {v['width']}x{v['height']}", (v["width"], v["height"]) == (W, H))
        add(f"{name}: h264 yuv420p + audio", v["codec_name"] == "h264" and v["pix_fmt"] == "yuv420p" and bool(a))
        fps = eval(v["r_frame_rate"])
        add(f"{name}: fps {fps:.2f}", abs(fps - m.get("fps", 30)) < 0.01)
        is_master = "master" in str(name)
        body = dur if is_master else dur  # exports may include outro
        add(f"{name}: duration {dur:.1f}s in target {lo}-{hi}s", lo <= body <= hi + (4 if not is_master else 0),
            blocking=m.get("duration_blocking", True))
        if m["format"] == "short":
            add(f"{name}: under 3 min Shorts limit", dur <= 180)
        e = ff_filter(f, af="ebur128=peak=true")
        I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1])
        tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)
        tpv = float(tp[-1]) if tp else 0.0
        add(f"{name}: loudness {I:.1f} LUFS (target {m.get('loudness_lufs', -14)} ±1.5)",
            abs(I - m.get("loudness_lufs", -14)) <= 1.5)
        add(f"{name}: true peak {tpv:.1f} dBFS ≤ -1.0", tpv <= -1.0)
        bl = ff_filter(f, vf="blackdetect=d=1.0:pix_th=0.06")
        blacks = re.findall(r"black_duration:([\d.]+)", bl)
        add(f"{name}: no black gaps ≥1s", not blacks, f"{blacks}", blocking=False)
        fr = ff_filter(f, vf="freezedetect=n=0.0005:d=4")
        freezes = re.findall(r"freeze_duration: ([\d.]+)", fr)
        add(f"{name}: no frozen stretches ≥4s", not freezes, f"{freezes}", blocking=False)
        add(f"{name}: size < 256 GB (YouTube)", f.stat().st_size < 256 * 1024 ** 3)

    master = [f for f in files if "master" in str(f)]
    add("clean master present (no watermark)", bool(master))
    fails = [r for r in rows if not r[1] and r[3]]
    warns = [r for r in rows if not r[1] and not r[3]]
    lines = [f"# QC Report — {m['id']} {m['title']}", "",
             f"**Result: {'FAIL' if fails else 'PASS'}** — {len(rows) - len(fails) - len(warns)} pass, "
             f"{len(fails)} blocking fail, {len(warns)} warning", "", "| Check | Result | Detail |", "|---|---|---|"]
    for n, ok, dt, b in rows:
        lines.append(f"| {n} | {'PASS' if ok else ('FAIL' if b else 'WARN')} | {dt} |")
    (ep / "QC_REPORT.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main(sys.argv[1])
