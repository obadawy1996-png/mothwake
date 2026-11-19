#!/usr/bin/env python3
"""Build MOTHWAKE platform assets from the approved logo geometry.

Writes HTML sources to brand/templates/ and renders PNGs into brand/kit/ via
scripts/brand/render.js (Playwright). Every asset reuses mark_svg_group() so
geometry and proportions never drift.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_brand import C, mark_svg_group, tagline, wordmark  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TPL = ROOT / "brand" / "templates"
KIT = ROOT / "brand" / "kit"
FONTS = (ROOT / "brand" / "fonts").as_uri()
SEL = json.loads((ROOT / "brand" / "build_manifest.json").read_text())["selected_concept"]

FONT_CSS = f"""
@font-face{{font-family:Cinzel;src:url('{FONTS}/Cinzel[wght].ttf');font-weight:400 900}}
@font-face{{font-family:Cormorant;src:url('{FONTS}/CormorantGaramond[wght].ttf');font-weight:300 700}}
@font-face{{font-family:Cormorant;font-style:italic;src:url('{FONTS}/CormorantGaramond-Italic[wght].ttf');font-weight:300 700}}
@font-face{{font-family:Inter;src:url('{FONTS}/Inter[opsz,wght].ttf');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
"""


def mark(size, fg=C["gold"], accent=C["lamp"], extra=""):
    return (f'<svg width="{size}" height="{size}" viewBox="-50 -50 100 100" {extra}>'
            f'{mark_svg_group(SEL, fg, accent)}</svg>')


def word(size, fg=C["gold"], tag=False):
    d, w, cap = (tagline if tag else wordmark)(size, fg)
    return (f'<svg width="{w:.0f}" height="{cap * 1.02:.0f}" viewBox="0 {-cap:.1f} {w:.1f} {cap * 1.02:.1f}">'
            f'<path fill="{fg}" d="{d}"/></svg>')


def page(w, h, body, css=""):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONT_CSS}"
            f"html,body{{width:{w}px;height:{h}px;overflow:hidden;background:transparent}}{css}</style></head>"
            f"<body>{body}</body></html>")


ATMOS = f"""
.atmos{{position:absolute;inset:0;background:
 radial-gradient(ellipse 38% 55% at 50% 46%, rgba(241,221,176,.16), rgba(184,154,104,.05) 45%, transparent 70%),
 radial-gradient(ellipse 120% 90% at 50% 120%, rgba(119,113,125,.20), transparent 60%),
 linear-gradient({C['obsidian']}, {C['charcoal']});}}
.vig{{position:absolute;inset:0;box-shadow:inset 0 0 260px 80px rgba(0,0,0,.85)}}
.dust i{{position:absolute;border-radius:50%;background:{C['lamp']};}}
"""


def dust(n, w, h, seed=7, cx=0.5, cy=0.46, spread=0.35):
    import random
    r = random.Random(seed)
    out = []
    for _ in range(n):
        x = r.gauss(cx, spread / 1.6) * w
        y = r.gauss(cy, spread / 1.6) * h
        s = r.choice([1, 1, 2, 2, 3])
        out.append(f'<i style="left:{x:.0f}px;top:{y:.0f}px;width:{s}px;height:{s}px;opacity:{r.uniform(.15, .6):.2f}"></i>')
    return '<div class="dust">' + "".join(out) + "</div>"


def build():
    TPL.mkdir(parents=True, exist_ok=True)
    KIT.mkdir(parents=True, exist_ok=True)
    jobs = []  # (html_name, png_name, w, h, transparent)

    # ---- YouTube banner 2560x1440; content inside 1235x338 minimum-safe (all devices)
    W, H = 2560, 1440
    body = (f'<div class="atmos"></div>{dust(160, W, H)}<div class="vig"></div>'
            f'<div class="safe">{mark(170)}<div class="wm">{word(118)}</div>'
            f'<div class="tag">{word(30, C["ash"], tag=True)}</div></div>')
    css = ATMOS + (".safe{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);"
                   "display:flex;align-items:center;gap:44px}"
                   ".wm{display:flex;flex-direction:column}.tag{position:absolute;left:214px;top:178px}")
    # Overlay guide (separate file) for desktop/mobile/TV crop checks.
    (TPL / "yt_banner.html").write_text(page(W, H, body, css))
    jobs.append(("yt_banner.html", "youtube_banner_2560x1440.png", W, H, False))
    guide = body + ('<div style="position:absolute;left:663px;top:551px;width:1235px;height:338px;'
                    'outline:3px dashed #e33"></div>'  # min safe (all devices)
                    '<div style="position:absolute;left:0;top:508px;width:2560px;height:423px;'
                    'outline:3px dashed #3ae"></div>'  # desktop max
                    '<div style="position:absolute;left:507px;top:508px;width:1546px;height:423px;'
                    'outline:3px dashed #ea3"></div>')  # tablet/text-and-logo safe
    (TPL / "yt_banner_safe_guide.html").write_text(page(W, H, guide, css))
    jobs.append(("yt_banner_safe_guide.html", "../previews/youtube_banner_safe_guide.png", W, H, False))

    # ---- Profile pictures (circle-safe: mark within 70% diameter)
    for name, s in (("youtube_profile_800.png", 800), ("social_profile_1080.png", 1080)):
        body = (f'<div class="atmos"></div><div class="c">{mark(int(s * .66))}</div>')
        css = ATMOS.replace("260px 80px", f"{s * .12:.0f}px {s * .03:.0f}px") + \
            ".c{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding-top:2%}"
        (TPL / f"profile_{s}.html").write_text(page(s, s, body, css))
        jobs.append((f"profile_{s}.html", name, s, s, False))

    # ---- Watermark: simplified single-colour mark + soft shadow so it reads on light and dark
    for name, fg, acc in (("watermark_gold.png", C["gold"], None), ("watermark_white.png", "#FFFFFF", None)):
        body = f'<div class="w">{mark(132, fg, acc)}</div>'
        css = (".w{width:150px;height:150px;display:flex;align-items:center;justify-content:center;"
               "filter:drop-shadow(0 0 3px rgba(0,0,0,.75))}")
        (TPL / name.replace(".png", ".html")).write_text(page(150, 150, body, css))
        jobs.append((name.replace(".png", ".html"), name, 150, 150, True))

    # ---- Social banners (dimensions marked unverified until PLATFORM_SPECS confirms)
    for name, w, h in (("facebook_cover_1640x624.png", 1640, 624),):
        body = (f'<div class="atmos"></div>{dust(70, w, h)}<div class="vig"></div>'
                f'<div class="safe">{mark(150)}<div>{word(84)}<div style="margin-top:22px">'
                f'{word(22, C["ash"], tag=True)}</div></div></div>')
        css = ATMOS.replace("260px 80px", "140px 40px") + (
            ".safe{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:34px}")
        (TPL / "facebook_cover.html").write_text(page(w, h, body, css))
        jobs.append(("facebook_cover.html", name, w, h, False))

    # ---- Video branding: end card (16:9 and 9:16), title card, caption style sample
    for name, w, h, ms, ws in (("end_card_1920x1080.png", 1920, 1080, 220, 96),
                               ("end_card_1080x1920.png", 1080, 1920, 260, 74)):
        body = (f'<div class="atmos"></div>{dust(90, w, h)}<div class="vig"></div>'
                f'<div class="c">{mark(ms)}<div style="margin-top:46px">{word(ws)}</div>'
                f'<div style="margin-top:26px">{word(ws * .26, C["ash"], tag=True)}</div></div>')
        css = ATMOS + ".c{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}"
        (TPL / name.replace(".png", ".html")).write_text(page(w, h, body, css))
        jobs.append((name.replace(".png", ".html"), name, w, h, False))

    body = (f'<div class="atmos"></div><div class="vig"></div><div class="c">'
            f'<div class="ep">A MOTHWAKE STORY</div><div class="t">The Lamp on Hollow Street</div>'
            f'<div class="rule"></div></div>')
    css = ATMOS + (".c{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}"
                   f".ep{{font:600 26px Cinzel;letter-spacing:.42em;color:{C['ash']}}}"
                   f".t{{font:italic 500 112px Cormorant;color:{C['bone']};margin-top:22px}}"
                   f".rule{{width:120px;height:2px;background:{C['gold']};margin-top:34px}}")
    (TPL / "title_card_template.html").write_text(page(1920, 1080, body, css))
    jobs.append(("title_card_template.html", "title_card_sample_1920x1080.png", 1920, 1080, False))

    body = ('<div class="bg"></div><div class="cap">She said the light<br><b>was already on.</b></div>')
    css = (f".bg{{position:absolute;inset:0;background:linear-gradient(160deg,#3a3e46,#121318 60%,#5b5246)}}"
           ".cap{position:absolute;left:0;right:0;top:1180px;text-align:center;font:700 64px/1.18 Inter;"
           f"color:{C['bone']};text-shadow:0 3px 0 #000,0 0 18px rgba(0,0,0,.9)}}"
           f".cap b{{color:{C['lamp']}}}")
    (TPL / "caption_style_shorts.html").write_text(page(1080, 1920, body, css))
    jobs.append(("caption_style_shorts.html", "../previews/caption_style_shorts.png", 1080, 1920, False))

    for html, png, w, h, t in jobs:
        out = (KIT / png).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        cmd = ["node", str(ROOT / "scripts/brand/render.js"), str(TPL / html), str(out), str(w), str(h)]
        if t:
            cmd.append("--transparent")
        subprocess.run(cmd, check=True)
        print("rendered", out.relative_to(ROOT))


if __name__ == "__main__":
    build()
