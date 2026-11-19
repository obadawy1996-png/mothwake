#!/usr/bin/env python3
"""MOTHWAKE episode assembler.

  .venv/bin/python scripts/production/assemble.py episodes/EP000/manifest.json

Reads the episode manifest, refuses to run if the brand validator fails, then renders:
  episodes/<id>/master/<id>_master.mp4       clean master (no watermark)
  episodes/<id>/exports/<id>_<platform>.mp4  branded variants listed in manifest["exports"]

Shots are layered stills animated with parallax / push / pan, plus light flicker, dust
and brand-styled burned-in captions (Inter Bold, Bone + Lamp key word). Audio: narration,
sfx and music beds mixed with sidechain ducking, normalised with loudnorm.
"""
from __future__ import annotations

import json
import math
import random
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
FONT = str(ROOT / "brand/fonts/Inter[opsz,wght].ttf")
BONE, LAMP = (231, 226, 216), (241, 221, 176)


def ease(t):
    return t * t * (3 - 2 * t)


def load_font(size):
    f = ImageFont.truetype(FONT, size)
    try:
        f.set_variation_by_axes([32, 700])  # opsz, wght
    except Exception:
        pass
    return f


def layer_frame(layers, W, H, t, move, strength):
    """Composite layered stills for normalised time t (0..1) with a camera move."""
    canvas = Image.new("RGB", (W, H), (9, 10, 13))
    e = ease(t)
    for L in layers:
        im = L["_img"]
        depth = L.get("depth", 0.5)  # 0 far .. 1 near
        scale = 1.08 + 0.04 * depth
        dx = dy = 0.0
        if move == "push":
            scale += strength * e * (0.5 + depth)
        elif move == "pan_left":
            dx = -strength * W * e * (0.3 + depth)
        elif move == "pan_right":
            dx = strength * W * e * (0.3 + depth)
        elif move == "drift":
            dx = math.sin(t * math.pi) * strength * W * (0.2 + depth)
            dy = -strength * H * 0.3 * e
        sw, sh = int(W * scale), int(H * scale)
        r = im.resize((sw, sh), Image.BICUBIC)
        x = int((W - sw) / 2 + dx)
        y = int((H - sh) / 2 + dy)
        canvas.paste(r, (x, y), r if r.mode == "RGBA" else None)
    return canvas


def draw_caption(img, text, key_word, W, H, vertical, y_frac=None):
    if not text:
        return img
    size = 64 if vertical else 46
    font = load_font(size)
    y0 = int(H * (y_frac if y_frac is not None else (0.615 if vertical else 0.80)))
    # soft dark backing gradient (not a box) so captions stay readable over bright art
    band = Image.new("L", (1, 256))
    band.putdata([int(150 * math.sin(math.pi * i / 255) ** 1.5) for i in range(256)])
    bh = int(size * 3.6)
    band = band.resize((W, bh))
    shade = Image.new("RGB", (W, bh), (0, 0, 0))
    img.paste(shade, (0, y0 - int(size * 0.9)), band)
    d = ImageDraw.Draw(img)
    words = text.split()
    lines, cur = [], []
    for w in words:  # max 6 words / line
        cur.append(w)
        if len(cur) == 6:
            lines.append(cur); cur = []
    if cur:
        lines.append(cur)
    y = y0
    for ln in lines[:2]:
        widths = [d.textlength(w + " ", font=font) for w in ln]
        x = (W - sum(widths)) / 2
        for w, wd in zip(ln, widths):
            col = LAMP if key_word and w.strip(".,!?").lower() == key_word.lower() else BONE
            for ox, oy in ((0, 3), (2, 2), (-2, 2)):
                d.text((x + ox, y + oy), w, font=font, fill=(0, 0, 0))
            d.text((x, y), w, font=font, fill=col)
            x += wd
        y += int(size * 1.18)
    return img


def render_video(m, ep_dir, out, watermark):
    W, H = m["resolution"]
    fps = m.get("fps", 30)
    vertical = H > W
    rnd = random.Random(m["id"])
    wm = None
    if watermark:
        wm = Image.open(ROOT / m["brand_assets"]["watermark"]).convert("RGBA")
        hgt = int(H * (0.042 if vertical else 0.068))
        wm = wm.resize((hgt, hgt), Image.LANCZOS)
        a = wm.getchannel("A").point(lambda v: int(v * 0.58))
        wm.putalpha(a)
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                           "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                           "-crf", "18", "-pix_fmt", "yuv420p", str(out)], stdin=subprocess.PIPE)
    for shot in m["shots"]:
        for L in shot["layers"]:
            L["_img"] = Image.open(ep_dir / L["src"]).convert("RGBA")
        n = int(shot["duration"] * fps)
        for i in range(n):
            t = i / max(1, n - 1)
            f = layer_frame(shot["layers"], W, H, t, shot.get("move", "drift"), shot.get("strength", 0.04))
            if shot.get("flicker"):
                k = 0.82 + 0.18 * (rnd.random() > 0.12)
                f = Image.eval(f, lambda v, k=k: int(v * k))
            if shot.get("fade_in") and i < fps * shot["fade_in"]:
                k = i / (fps * shot["fade_in"])
                f = Image.eval(f, lambda v, k=k: int(v * k))
            cap = shot.get("caption")
            if cap and (cap.get("from", 0) * fps <= i < cap.get("to", shot["duration"]) * fps):
                f = draw_caption(f, cap["text"], cap.get("key"), W, H, vertical, cap.get("y"))
            if wm is not None and not shot.get("hide_watermark"):
                mx = int(W * 0.04)
                f.paste(wm, (W - wm.width - mx, H - wm.height - mx - (int(H * 0.12) if vertical else 0)), wm)
            ff.stdin.write(f.tobytes())
    ff.stdin.close()
    if ff.wait():
        raise SystemExit("ffmpeg video encode failed")


def render_audio(m, ep_dir, out, total):
    a = m["audio"]
    inputs, filters, mixes = [], [], []
    idx = 0
    for kind in ("narration", "sfx", "music"):
        for clip in a.get(kind, []):
            inputs += ["-i", str((ep_dir / clip["src"]) if not clip["src"].startswith("brand/") else ROOT / clip["src"])]
            gain = clip.get("gain_db", 0 if kind != "music" else -16)
            filters.append(f"[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={gain}dB,"
                           f"adelay={int(clip.get('at', 0) * 1000)}|{int(clip.get('at', 0) * 1000)}[{kind}{idx}]")
            mixes.append((kind, f"[{kind}{idx}]"))
            idx += 1
    if not mixes:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-t", str(total), "-i",
                        "anullsrc=r=48000:cl=stereo", str(out)], check=True)
        return
    nar = [x for k, x in mixes if k == "narration"]
    other = [x for k, x in mixes if k != "narration"]
    chain = ";".join(filters)
    if nar and other:
        chain += (f";{''.join(nar)}amix=inputs={len(nar)}:normalize=0,asplit=2[nar][key]"
                  f";{''.join(other)}amix=inputs={len(other)}:normalize=0[bed]"
                  ";[bed][key]sidechaincompress=threshold=0.05:ratio=6:attack=20:release=400[duck]"
                  ";[nar][duck]amix=inputs=2:normalize=0[mix]")
    else:
        allx = nar + other
        chain += f";{''.join(allx)}amix=inputs={len(allx)}:normalize=0[mix]"
    lufs = m.get("loudness_lufs", -14)
    chain += f";[mix]apad,atrim=0:{total},loudnorm=I={lufs}:TP=-1.5:LRA=11[out]"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", chain, "-map", "[out]",
                    "-ar", "48000", "-c:a", "pcm_s16le", str(out)], check=True)


def mux(video, audio, out, outro=None):
    if outro:
        tmp = out.with_suffix(".body.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-i", str(audio), "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "192k", "-shortest", str(tmp)], check=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp), "-i", str(outro), "-filter_complex",
                        "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]", "-map", "[v]", "-map", "[a]",
                        "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                        str(out)], check=True)
        tmp.unlink()
    else:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-i", str(audio), "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)], check=True)


def main(manifest_path):
    mp = Path(manifest_path).resolve()
    ep = mp.parent
    m = json.loads(mp.read_text())
    r = subprocess.run([sys.executable, str(ROOT / "scripts/brand_validator.py"), "episode", str(mp)])
    if r.returncode:
        raise SystemExit("BLOCKED: brand validation failed — not rendering")
    total = sum(s["duration"] for s in m["shots"])
    (ep / "master").mkdir(exist_ok=True)
    (ep / "exports").mkdir(exist_ok=True)
    work = ep / "render"
    work.mkdir(exist_ok=True)
    audio = work / "mix.wav"
    render_audio(m, ep, audio, total)
    clean = work / "clean.mp4"
    render_video(m, ep, clean, watermark=False)
    master = ep / "master" / f"{m['id']}_master.mp4"
    mux(clean, audio, master)
    print("master:", master.relative_to(ROOT))
    for x in m.get("exports", []):
        if x.get("watermark", True):
            v = work / f"wm_{x['platform']}.mp4"
            render_video(m, ep, v, watermark=True)
        else:
            v = clean  # identical picture to the master: reuse, don't re-render
        outro = ROOT / m["brand_assets"][x["outro"]] if x.get("outro") else None
        out = ep / "exports" / f"{m['id']}_{x['platform']}.mp4"
        mux(v, audio, out, outro)
        print("export:", out.relative_to(ROOT))


if __name__ == "__main__":
    main(sys.argv[1])
