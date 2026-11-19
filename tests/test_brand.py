#!/usr/bin/env python3
"""Brand kit tests + ASSET_MANIFEST.md generation (from measured file properties).

Run: .venv/bin/python tests/test_brand.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))


def img(p):
    return Image.open(ROOT / p)


# Logo exports
for f in sorted((ROOT / "brand/logo").glob("*.svg")):
    png = ROOT / "brand/logo/png" / (f.stem + ".png")
    check(f"logo export {f.stem}", png.exists() and png.stat().st_size > 0)
    if "transparent" in f.stem or "mono" in f.stem:
        a = Image.open(png).convert("RGBA").getchannel("A")
        check(f"  transparent bg {f.stem}", a.getextrema()[0] == 0)
    check(f"  svg has no <text> (outlined) {f.stem}", "<text" not in f.read_text())

# Banner dimensions, size, safe-area placement
b = img("brand/kit/youtube_banner_2560x1440.png")
check("banner is 2560x1440", b.size == (2560, 1440), str(b.size))
check("banner file ≤ 6 MB", (ROOT / "brand/kit/youtube_banner_2560x1440.png").stat().st_size <= 6 * 1024 * 1024)
# brightness-based bbox of gold/lamp content must sit inside min safe area 1235x338 centred
rgb = b.convert("RGB")
px = rgb.load()
xs, ys = [], []
for y in range(0, 1440, 2):
    row = []
    for x in range(0, 2560, 2):
        r, g, bb = px[x, y]
        if r > 120 and r - bb > 30:  # gold-ish content (logo/wordmark), not dark bg
            row.append(x)
    if len(row) >= 6:  # ignore isolated 1-3 px dust specks
        xs += row; ys.append(y)
safe = (663, 551, 663 + 1235, 551 + 338)
inside = xs and min(xs) >= safe[0] and max(xs) <= safe[2] and min(ys) >= safe[1] and max(ys) <= safe[3]
check("banner logo/text inside minimum safe area (TV/desktop/mobile)", inside,
      f"content bbox=({min(xs)},{min(ys)})-({max(xs)},{max(ys)}) safe={safe}" if xs else "no content found")

# Profile picture: circle-safe (no content outside inscribed circle's 92%)
p = img("brand/kit/youtube_profile_800.png").convert("RGB")
check("profile is 800x800", p.size == (800, 800))
pp = p.load()
outside = 0
for y in range(0, 800, 4):
    for x in range(0, 800, 4):
        if ((x - 400) ** 2 + (y - 400) ** 2) ** .5 > 368:
            r, g, bb = pp[x, y]
            outside += r > 120 and r - bb > 30
check("profile mark survives circular crop", outside == 0, f"gold px outside circle={outside}")

# Watermark
w = img("brand/kit/watermark_gold.png")
check("watermark 150x150 transparent", w.size == (150, 150) and w.mode == "RGBA")
check("watermark < 1 MB", (ROOT / "brand/kit/watermark_gold.png").stat().st_size < 1024 * 1024)

# Thumbnails
for t in sorted((ROOT / "brand/thumbnails").glob("*.jpg")):
    im = Image.open(t)
    check(f"thumbnail {t.stem} 1280x720 < 2MB", im.size == (1280, 720) and t.stat().st_size < 2 * 1024 * 1024)
r = subprocess.run([sys.executable, str(ROOT / "scripts/brand/thumbnail.py"), "--layout", "light",
                    "--text", "ONE TWO THREE FOUR FIVE", "--out", "/tmp/_t.jpg"], capture_output=True)
check("thumbnail renderer rejects >4 words", r.returncode != 0)


# Audio + outro video
def probe(p):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_name,width,height,sample_rate",
                        "-of", "json", str(ROOT / p)], capture_output=True, text=True).stdout
    return json.loads(o)


def lufs(p):
    o = subprocess.run(["ffmpeg", "-nostats", "-i", str(ROOT / p), "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    line = [l for l in o.splitlines() if l.strip().startswith("I:")][-1]
    return float(line.split()[1])


for s, target in (("mothwake_signature.wav", -18), ("mothwake_outro.wav", -18), ("mothwake_open_sub.wav", -24)):
    v = lufs(f"brand/sound/{s}")
    check(f"sound {s} loudness {v} LUFS within ±1 of {target}", abs(v - target) <= 1)
for v in ("mothwake_outro_1920x1080.mp4", "mothwake_outro_1080x1920.mp4"):
    d = probe(f"brand/video/{v}")
    codecs = {s["codec_name"] for s in d["streams"]}
    check(f"outro {v} h264+aac, ≤ 4 s", {"h264", "aac"} <= codecs and float(d["format"]["duration"]) <= 4)

# Validator
r = subprocess.run([sys.executable, str(ROOT / "scripts/brand_validator.py"), "check"], capture_output=True, text=True)
check("brand validator: all approved assets intact", r.returncode == 0, r.stdout.strip().splitlines()[-1])

# --- ASSET_MANIFEST.md
rows = []
for d in ("brand/logo", "brand/logo/png", "brand/kit", "brand/thumbnails", "brand/sound", "brand/video",
          "brand/fonts", "brand/previews", "brand/concepts"):
    for f in sorted((ROOT / d).glob("*.*")):
        spec = ""
        if f.suffix in (".png", ".jpg"):
            im = Image.open(f)
            spec = f"{im.size[0]}×{im.size[1]} {im.mode}"
        elif f.suffix in (".wav", ".mp4"):
            pr = probe(str(f.relative_to(ROOT)))
            st = pr["streams"][0]
            spec = f"{float(pr['format']['duration']):.2f}s " + (
                f"{st.get('width')}×{st.get('height')}" if st.get("width") else f"{st.get('sample_rate')} Hz")
        rows.append(f"| `{f.relative_to(ROOT)}` | {spec} | {f.stat().st_size / 1024:.0f} KB |")
(ROOT / "brand/ASSET_MANIFEST.md").write_text(
    "# Asset Manifest\n\nGenerated by `tests/test_brand.py` from measured file properties. "
    "Approved hashes are in `brand/APPROVED_ASSETS.lock` (status: provisional until the owner approves).\n\n"
    "| File | Spec | Size |\n|---|---|---|\n" + "\n".join(rows) + "\n")

failed = 0
for n, ok, d in results:
    failed += not ok
    print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d}")
print(f"\n{len(results) - failed}/{len(results)} brand tests passed")
sys.exit(1 if failed else 0)
