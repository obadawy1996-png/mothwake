#!/usr/bin/env python3
"""Create EP000, an internal pipeline-test episode (NOT for publishing).

Procedural placeholder art (PIL) in layers + synthesised ambience so the full
assemble → brand → QC chain can be tested with zero paid credits.
Story: MW003 "Lost Moth Poster" (captions only; narration slot left for ElevenLabs).
"""
from __future__ import annotations

import json
import math
import random
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/brand"))
EP = ROOT / "episodes/EP000"
ART = EP / "art"
W, H = 1080, 1920
OBS, CHAR, ASH, GOLD, BONE, LAMP = (9, 10, 13), (37, 35, 43), (119, 113, 125), (184, 154, 104), (231, 226, 216), (241, 221, 176)


def font(sz, w=700):
    f = ImageFont.truetype(str(ROOT / "brand/fonts/Inter[opsz,wght].ttf"), sz)
    f.set_variation_by_axes([32, w])
    return f


def grad(top, bottom):
    a = np.linspace(0, 1, H)[:, None, None]
    arr = (np.array(top) * (1 - a) + np.array(bottom) * a).repeat(W, 1)
    return Image.fromarray(arr.astype("uint8"), "RGB").convert("RGBA")


def glow(cx, cy, r, col=LAMP, a=200):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i in range(30, 0, -1):
        d.ellipse([cx - r * i / 30, cy - r * i / 30, cx + r * i / 30, cy + r * i / 30], fill=col + (int(a * (1 - i / 30) ** 2),))
    return im.filter(ImageFilter.GaussianBlur(20))


def moth(size, col=GOLD):
    from build_brand import mark_svg_group  # reuse brand geometry via SVG render
    tmp = ART / f"_moth_{size}.svg"
    tmp.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="-50 -50 100 100">'
                   f'{mark_svg_group("B", "#%02x%02x%02x" % col, None)}</svg>')
    out = tmp.with_suffix(".png")
    subprocess.run(["node", str(ROOT / "scripts/brand/render.js"), str(tmp), str(out), "--transparent"], check=True)
    return Image.open(out).convert("RGBA")


def poster(lines, sub, w=560, h=760):
    p = Image.new("RGBA", (w, h), BONE + (255,))
    d = ImageDraw.Draw(p)
    d.text((w / 2, 70), "LOST MOTH", font=font(78, 850), fill=OBS, anchor="mm")
    m = moth(300, (60, 56, 64))
    p.paste(m, ((w - 300) // 2, 130), m)
    y = 470
    for ln in lines:
        d.text((w / 2, y), ln, font=font(34, 600), fill=OBS, anchor="mm"); y += 50
    d.text((w / 2, h - 70), sub, font=font(30, 800), fill=(120, 30, 30), anchor="mm")
    return p.rotate(random.Random(len(sub)).uniform(-3, 3), expand=True, resample=Image.BICUBIC)


def pole_scene(lines, sub, name):
    bg = grad(OBS, CHAR)
    bg.alpha_composite(glow(W // 2, 300, 700, LAMP, 120))
    far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(far)
    for x in range(-50, W, 180):
        hh = random.randint(300, 600); d.rectangle([x, H - 500 - hh, x + 150, H - 500], fill=(20, 20, 26, 255))
    mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
    d.rectangle([W // 2 - 70, 0, W // 2 + 70, H], fill=(52, 44, 40, 255))
    p = poster(lines, sub)
    mid.alpha_composite(p, ((W - p.width) // 2, 560))
    for n, im in (("bg", bg), ("far", far), ("mid", mid)):
        im.save(ART / f"{name}_{n}.png")
    return [{"src": f"art/{name}_bg.png", "depth": 0.0}, {"src": f"art/{name}_far.png", "depth": 0.3},
            {"src": f"art/{name}_mid.png", "depth": 0.8}]


def window_scene():
    bg = grad((14, 16, 24), OBS)
    room = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(room)
    d.rectangle([180, 380, 900, 1240], fill=(30, 34, 46, 255)); d.rectangle([180, 380, 900, 1240], outline=CHAR, width=26)
    d.line([540, 380, 540, 1240], fill=CHAR, width=18); d.line([180, 810, 900, 810], fill=CHAR, width=18)
    m = moth(360, GOLD)
    fg = Image.new("RGBA", (W, H), (0, 0, 0, 0)); fg.alpha_composite(glow(540, 820, 360, LAMP, 90)); fg.alpha_composite(m, (360, 640))
    girl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(girl)
    d.ellipse([430, 1380, 650, 1600], fill=OBS + (255,)); d.rectangle([380, 1560, 700, H], fill=OBS + (255,))
    for n, im in (("bg", bg), ("room", room), ("moth", fg), ("girl", girl)):
        im.save(ART / f"win_{n}.png")
    return [{"src": "art/win_bg.png", "depth": 0}, {"src": "art/win_room.png", "depth": 0.3},
            {"src": "art/win_moth.png", "depth": 0.55}, {"src": "art/win_girl.png", "depth": 1.0}]


def ambience(path, dur=48):
    sr = 48000
    n = sr * dur
    rng = np.random.default_rng(3)
    x = rng.standard_normal(n)
    b = np.convolve(x, np.ones(400) / 400, mode="same")  # low rumble/room tone
    hum = 0.02 * np.sin(2 * np.pi * 60 * np.arange(n) / sr)
    s = (b * 0.6 + hum)
    s = np.stack([s, s], 1) / np.abs(s).max() * 0.5
    import wave
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((s * 32767).astype("<i2").tobytes())


def main():
    random.seed(11)
    ART.mkdir(parents=True, exist_ok=True)
    (EP / "audio").mkdir(exist_ok=True)
    s1 = pole_scene(["Small. Grey wings.", "Two spots like eyes."], "LAST SEEN: LAUNDROMAT", "p1")
    s2 = pole_scene(["Answers to nothing.", "Do not tell it your name."], "LAST SEEN: ELM ST", "p2")
    s3 = pole_scene(["It was here today.", "So were you."], "LAST SEEN: YOUR WINDOW", "p3")
    s4 = window_scene()
    s5 = pole_scene(["Thank you for", "your help, Iris."], "FOUND.", "p4")
    ambience(EP / "audio/ambience.wav")
    sel = __import__("json").loads((ROOT / "brand/APPROVED_ASSETS.lock").read_text())["roles"]
    manifest = {
        "id": "EP000", "title": "Lost Moth Poster (pipeline test)", "story_id": "MW003", "format": "short",
        "status": "internal-test — DO NOT PUBLISH", "resolution": [W, H], "fps": 30, "loudness_lufs": -14,
        "brand_assets": sel,
        "originality_review": "MW003 originality review in stories/concepts/MW003.json",
        "licence_ledger": [
            {"asset": "art/*.png", "licence": "original — procedurally generated by MOTHWAKE scripts"},
            {"asset": "audio/ambience.wav", "licence": "original — synthesised"},
            {"asset": "brand/sound/*", "licence": "original — synthesised (brand)"},
            {"asset": "brand/fonts/*", "licence": "SIL OFL 1.1"}],
        "approvals": {"concept": None, "script": None, "owner_final": None},
        "shots": [
            {"layers": s1, "duration": 8, "move": "push", "strength": 0.05, "fade_in": 0.3,
             "caption": {"text": "Someone is putting up posters for a lost moth.", "key": "moth", "y": 0.78, "from": 0.2}},
            {"layers": s2, "duration": 8, "move": "drift", "strength": 0.03,
             "caption": {"text": "The next day, the poster had changed.", "key": "changed", "y": 0.78}},
            {"layers": s3, "duration": 9, "move": "push", "strength": 0.07, "flicker": True,
             "caption": {"text": "It knew where I had been.", "key": "knew", "y": 0.78}},
            {"layers": s4, "duration": 9, "move": "push", "strength": 0.05,
             "caption": {"text": "Then I found the moth. At my window.", "key": "window", "y": 0.70}},
            {"layers": s5, "duration": 7, "move": "push", "strength": 0.09, "hide_watermark": True,
             "caption": {"text": "I never told it my name.", "key": "name", "y": 0.78, "from": 1.5}},
        ],
        "audio": {
            "narration": [],
            "sfx": [{"src": "brand/sound/mothwake_open_sub.wav", "at": 0.0, "gain_db": 0},
                    {"src": "brand/sound/mothwake_signature.wav", "at": 33.5, "gain_db": -2}],
            "music": [{"src": "audio/ambience.wav", "at": 0, "gain_db": -6}]},
        "exports": [{"platform": "youtube_shorts", "watermark": True},
                    {"platform": "tiktok", "watermark": False},
                    {"platform": "instagram_reels", "watermark": False}],
    }
    (EP / "manifest.json").write_text(json.dumps(manifest, indent=2))
    for f in ART.glob("_moth_*"):
        f.unlink()
    print("EP000 ready:", EP.relative_to(ROOT))


if __name__ == "__main__":
    main()
