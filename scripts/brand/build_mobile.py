#!/usr/bin/env python3
"""MOTHWAKE mobile-first brand PROPOSALS (Shorts / Reels / TikTok, 1080x1920).

Writes to brand/mobile/ only. Nothing here replaces the approved, locked assets:
these are proposals for owner approval (then add to the lock with brand_validator.py lock).

  - small-size mark ("optical size" cut of the approved Watcher geometry)
  - mobile watermark (top-left, clear of Shorts UI)
  - caption style for phones
  - 3 cover templates (9:16)
  - safe-zone overlay + phone-size readability preview
  - 1.0 s loop-friendly end sting (replaces the 3.2 s outro on Shorts)
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_brand as bb  # noqa: E402
from build_kit import FONT_CSS  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "brand" / "mobile"
C = bb.C
W, H = 1080, 1920
RENDER = ROOT / "scripts/brand/render.js"

# Optical small-size cut: identical silhouette; thicker antennae, larger eyespot cut-outs.
ANT_SMALL = ("M1.6 -23.5 C5.6 -33.5 13 -40.5 23.5 -44 C21.8 -39.6 18.6 -37.4 16 -34.4 "
             "C12 -30 7.6 -25.6 4.2 -21.6 Z")


def mark_small(fg, accent=None):
    eye_o, eye_i = bb.circle(27, -9.5, 8.4), bb.circle(27, -9.5, 3.6)
    fore = f"{bb.FORE} {eye_o} {eye_i}"
    wings = (f'<path fill-rule="evenodd" d="{fore}"/><path d="{bb.HIND}"/>'
             f'<path fill-rule="evenodd" d="{fore}" transform="scale(-1 1)"/>' + bb.mirror(bb.HIND))
    ant = f'<path d="{ANT_SMALL}"/><path d="{ANT_SMALL}" transform="scale(-1 1)"/>'
    pup = ""
    if accent:
        pup = (f'<g fill="{accent}"><path d="{eye_i}"/><path d="{eye_i}" transform="scale(-1 1)"/></g>')
    return f'<g fill="{fg}">{wings}<path d="{bb.BODY}"/><path d="{bb.HEAD}"/>{ant}</g>{pup}'


def svg_mark(size, fg, accent=None, small=True):
    g = mark_small(fg, accent) if small else bb.mark_svg_group("B", fg, accent)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="-50 -50 100 100">'
            f'{g}</svg>')


def page(body, css=""):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONT_CSS}"
            f"html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{C['obsidian']}}}{css}</style></head>"
            f"<body>{body}</body></html>")


def render(html_name, png, w=W, h=H, transparent=False):
    cmd = ["node", str(RENDER), str(OUT / html_name), str(OUT / png), str(w), str(h)]
    if transparent:
        cmd.append("--transparent")
    subprocess.run(cmd, check=True)


# Shorts UI zones (approximate, for planning; confirm against current app UI before final lock)
SAFE = {"top_ui": 0.09, "bottom_ui": 0.22, "right_rail": 0.13, "side_margin": 0.06}

CAPTION_CSS = f"""
.cap{{position:absolute;left:{SAFE['side_margin']*100}%;right:{SAFE['right_rail']*100}%;top:58%;text-align:center;
 font:800 78px/1.08 Inter;letter-spacing:-.01em;color:{C['bone']};
 -webkit-text-stroke:7px #000;paint-order:stroke fill;text-shadow:0 6px 18px rgba(0,0,0,.85)}}
.cap b{{color:{C['lamp']};font-weight:900}}
"""

WM_CSS = (f".wm{{position:absolute;left:{SAFE['side_margin']*100}%;top:{SAFE['top_ui']*100+1.5}%;opacity:.55;"
          "filter:drop-shadow(0 0 4px rgba(0,0,0,.9))}")


def art_placeholder(seed_hue=0):
    return (f'<div style="position:absolute;inset:0;background:'
            f'radial-gradient(ellipse 60% 35% at 50% 40%, rgba(241,221,176,.55), rgba(184,154,104,.12) 45%, transparent 70%),'
            f'linear-gradient({C["charcoal"]},{C["obsidian"]})"></div>'
            f'<div style="position:absolute;left:39%;top:30%;width:22%;height:36%;background:{C["lamp"]};opacity:.85"></div>'
            f'<div style="position:absolute;left:45.5%;top:38%;width:9%;height:28%;background:{C["obsidian"]};border-radius:45% 45% 8% 8%"></div>')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    # 1. marks
    for s in (48, 64, 96, 128, 512):
        (OUT / f"mark_small_{s}.svg").write_text(svg_mark(s, C["gold"], C["lamp"]))
    (OUT / "mark_small_white.svg").write_text(svg_mark(512, "#FFFFFF"))
    # comparison: approved vs small cut at phone sizes
    cmp_html = "".join(
        f'<div style="display:flex;gap:40px;align-items:center;margin:20px 40px">'
        f'<span style="font:600 28px Inter;color:{C["ash"]};width:120px">{s}px</span>'
        f'{svg_mark(s, C["gold"], C["lamp"], small=False)}{svg_mark(s, C["gold"], C["lamp"], small=True)}</div>'
        for s in (32, 48, 64, 96))
    (OUT / "mark_compare.html").write_text(page(
        f'<div style="padding:40px;font:700 34px Inter;color:{C["bone"]}">Approved (left) vs small-size cut (right)</div>{cmp_html}'))
    render("mark_compare.html", "preview_mark_compare.png", 1080, 760)
    # 2. watermark
    (OUT / "watermark_mobile.html").write_text(
        f"<!doctype html><html><head><style>html,body{{margin:0;background:transparent}}</style></head><body>"
        f'<div style="width:120px;height:120px;filter:drop-shadow(0 0 3px rgba(0,0,0,.85))">'
        f'{svg_mark(120, C["gold"])}</div></body></html>')
    render("watermark_mobile.html", "watermark_mobile_120.png", 120, 120, transparent=True)
    # 3. caption + safe zones preview
    safe_overlay = (
        f'<div style="position:absolute;left:0;right:0;top:0;height:{SAFE["top_ui"]*100}%;background:rgba(200,40,40,.28)"></div>'
        f'<div style="position:absolute;left:0;right:0;bottom:0;height:{SAFE["bottom_ui"]*100}%;background:rgba(200,40,40,.28)"></div>'
        f'<div style="position:absolute;right:0;top:{SAFE["top_ui"]*100}%;bottom:{SAFE["bottom_ui"]*100}%;width:{SAFE["right_rail"]*100}%;'
        f'background:rgba(200,40,40,.28)"></div>'
        f'<div style="position:absolute;left:6%;bottom:3%;font:600 30px Inter;color:#fff">platform UI zones (red) — keep text out</div>')
    cap = '<div class="cap">She said the light<br>was <b>already on.</b></div>'
    wm = f'<div class="wm">{svg_mark(64, C["gold"])}</div>'
    (OUT / "caption_safe_preview.html").write_text(page(art_placeholder() + cap + wm + safe_overlay, CAPTION_CSS + WM_CSS))
    render("caption_safe_preview.html", "preview_caption_safe.png")
    (OUT / "caption_clean_preview.html").write_text(page(art_placeholder() + cap + wm, CAPTION_CSS + WM_CSS))
    render("caption_clean_preview.html", "preview_caption_clean.png")
    # 4. cover templates (Shorts/Reels/TikTok covers, 9:16)
    covers = {
        "cover_hook": ('<div class="t">DON\'T<br><b>ANSWER</b></div>',
                       ".t{position:absolute;left:8%;right:15%;top:14%;font:900 150px/0.92 Inter;color:#E7E2D8;"
                       "-webkit-text-stroke:8px #000;paint-order:stroke fill;text-transform:uppercase}.t b{color:#F1DDB0}"),
        "cover_rule": ('<div class="card"><div class="n">RULE 3</div><div class="r">NEVER COUNT THE STAIRS</div></div>',
                       f".card{{position:absolute;left:9%;right:16%;top:16%;padding:40px 36px;background:{C['bone']};"
                       "transform:rotate(-3deg);box-shadow:0 20px 50px #000}"
                       f".n{{font:700 44px Cinzel;letter-spacing:.3em;color:{C['charcoal']}}}"
                       f".r{{font:900 92px/1 Inter;color:{C['obsidian']};margin-top:14px}}"),
        "cover_choice": ('<div class="q">WHICH ONE<br>IS <b>REAL?</b></div><div class="a">A</div><div class="bb">B</div>',
                         ".q{position:absolute;left:8%;right:15%;top:12%;font:900 120px/0.95 Inter;color:#E7E2D8;"
                         "-webkit-text-stroke:8px #000;paint-order:stroke fill}.q b{color:#F1DDB0}"
                         ".a,.bb{position:absolute;top:66%;width:150px;height:150px;border-radius:50%;"
                         f"background:{C['obsidian']};border:6px solid {C['gold']};color:{C['lamp']};"
                         "font:900 96px/138px Inter;text-align:center}.a{left:16%}.bb{left:54%}"),
    }
    for name, (body, css) in covers.items():
        (OUT / f"{name}.html").write_text(page(art_placeholder() + body + f'<div class="wm">{svg_mark(72, C["gold"])}</div>',
                                               css + WM_CSS))
        render(f"{name}.html", f"{name}.png")
    # phone-size readability check (what a viewer sees in the feed ~ 1/3 scale, and grid ~ 1/6)
    imgs = [str(OUT / f) for f in ("cover_hook.png", "cover_rule.png", "cover_choice.png", "preview_caption_clean.png")]
    subprocess.run(["montage", *imgs, "-tile", "4x1", "-geometry", "360x640+8+8", "-background", "#333",
                    str(OUT / "preview_phone_scale.png")], check=True)
    subprocess.run(["montage", *imgs, "-tile", "4x1", "-geometry", "180x320+6+6", "-background", "#333",
                    str(OUT / "preview_grid_scale.png")], check=True)
    # 5. 1.0 s end sting (9:16): moth mark fades in on black with the signature flutter (first 1.0 s)
    (OUT / "end_sting.html").write_text(page(f'<div style="position:absolute;inset:0;display:flex;align-items:center;'
                                             f'justify-content:center">{svg_mark(300, C["gold"], C["lamp"])}</div>'))
    render("end_sting.html", "end_sting_frame.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", "1.0", "-i", str(OUT / "end_sting_frame.png"),
                    "-i", str(ROOT / "brand/sound/mothwake_signature.wav"),
                    "-filter_complex", "[0:v]fade=in:0:9,format=yuv420p[v];[1:a]atrim=0:1.0,afade=t=out:st=0.7:d=0.3[a]",
                    "-map", "[v]", "-map", "[a]", "-r", "30", "-c:v", "libx264", "-crf", "18", "-c:a", "aac",
                    "-shortest", str(OUT / "end_sting_1080x1920.mp4")], check=True)
    print("mobile proposals written to", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
