#!/usr/bin/env python3
"""MOTHWAKE thumbnail renderer (1280x720, JPG < 2 MB).

  .venv/bin/python scripts/brand/thumbnail.py --layout watcher --art art.png \
      --text "DON'T|ANSWER" --out episodes/EP001/thumb_A.jpg

Layouts (see brand/THUMBNAIL_SYSTEM.md):
  watcher  subject right 60%, 1-2 word stack left, eyespot signature
  light    subject centred in a pool of light, optional single word top
  split    two panels: normal | wrong, gold hairline divider
  rule     "RULE 3"-style card + subject; for rules/instructions stories
If --art is omitted a procedural placeholder scene is used (template preview only).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_brand import C  # noqa: E402
from build_kit import FONT_CSS, mark  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
W, H = 1280, 720

PLACEHOLDER = f"""<svg viewBox="420 0 760 720" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">
<defs><radialGradient id="g" cx="62%" cy="45%" r="45%"><stop offset="0" stop-color="{C['lamp']}" stop-opacity=".85"/>
<stop offset=".35" stop-color="{C['gold']}" stop-opacity=".35"/><stop offset="1" stop-color="{C['obsidian']}" stop-opacity="0"/></radialGradient></defs>
<rect width="1280" height="720" fill="{C['charcoal']}"/><rect width="1280" height="720" fill="url(#g)"/>
<rect x="690" y="150" width="210" height="430" fill="{C['lamp']}" opacity=".9"/>
<path d="M795 250 q22 0 24 30 q2 26 -10 40 l26 70 l-8 190 h-64 l-8-190 l26-70 q-12-14-10-40 q2-30 24-30z" fill="{C['obsidian']}"/>
<rect y="580" width="1280" height="140" fill="{C['obsidian']}"/></svg>"""

LAYOUT_CSS = f"""
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{C['obsidian']}}}
.art{{position:absolute;inset:0;background-size:cover;background-position:center}}
.art svg{{position:absolute;inset:0}}
.vig{{position:absolute;inset:0;box-shadow:inset 0 0 180px 40px rgba(0,0,0,.8)}}
.sig{{position:absolute;right:26px;bottom:20px;opacity:.9;filter:drop-shadow(0 0 4px #000)}}
.big{{font:800 118px/0.92 Inter;letter-spacing:-.02em;color:{C['bone']};text-transform:uppercase;
     text-shadow:0 6px 0 #000,0 0 30px rgba(0,0,0,.9)}}
.big .hot{{color:{C['lamp']}}}
"""

LAYOUTS = {
    "watcher": (".art{left:28%}.shade{position:absolute;inset:0;background:linear-gradient(90deg,"
                f"{C['obsidian']} 30%,rgba(9,10,13,.6) 46%,transparent 62%)}}"
                ".txt{position:absolute;left:58px;top:50%;transform:translateY(-50%)}",
                '<div class="shade"></div><div class="txt big">{text}</div>'),
    "light": (".shade{position:absolute;inset:0;background:radial-gradient(ellipse 42% 60% at 50% 55%,"
              "transparent 40%,rgba(9,10,13,.92) 100%)}"
              ".txt{position:absolute;top:34px;left:0;right:0;text-align:center;font-size:84px}",
              '<div class="shade"></div><div class="txt big">{text}</div>'),
    "split": (".art{left:50%}.left{position:absolute;left:0;top:0;width:50%;height:100%;background-size:cover;"
              "background-position:center;filter:saturate(.5) brightness(1.1)}"
              f".div{{position:absolute;left:calc(50% - 2px);top:0;width:4px;height:100%;background:{C['gold']}}}"
              ".txt{position:absolute;left:0;right:0;bottom:46px;text-align:center;font-size:76px}",
              '<div class="left" style="{left_style}">{left_svg}</div><div class="div"></div>'
              '<div class="txt big">{text}</div>'),
    "rule": (".art{left:36%}.shade{position:absolute;inset:0;background:linear-gradient(90deg,"
             f"{C['obsidian']} 36%,transparent 52%)}}"
             f".card{{position:absolute;left:54px;top:50%;transform:translateY(-50%) rotate(-3deg);width:360px;"
             f"padding:34px 30px;background:{C['bone']};box-shadow:0 18px 40px #000}}"
             f".card .n{{font:700 30px Cinzel;letter-spacing:.3em;color:{C['charcoal']}}}"
             f".card .r{{font:800 50px/1.02 Inter;color:{C['obsidian']};margin-top:14px;text-transform:uppercase}}",
             '<div class="shade"></div><div class="card"><div class="n">{rule_no}</div><div class="r">{text}</div></div>'),
}


def render(layout: str, text: str, out: Path, art: Path | None = None, rule_no: str = "RULE 3",
           left_art: Path | None = None) -> Path:
    css, tpl = LAYOUTS[layout]
    words = [w for w in text.split("|") if w]
    if len(" ".join(words).split()) > 4:
        raise SystemExit("thumbnail text rule: max 4 words")
    html_text = "<br>".join(f'<span class="{"hot" if i == len(words) - 1 else ""}">{w}</span>'
                            for i, w in enumerate(words))
    if art:
        art_html = f'<div class="art" style="background-image:url(\'{art.resolve().as_uri()}\')"></div>'
        left_style = f"background-image:url('{(left_art or art).resolve().as_uri()}')"
        left_svg = ""
    else:
        art_html = f'<div class="art">{PLACEHOLDER}</div>'
        left_style, left_svg = "", PLACEHOLDER.replace(C["lamp"], C["ash"])
    body = (art_html + tpl.format(text=html_text, rule_no=rule_no, left_style=left_style, left_svg=left_svg)
            + '<div class="vig"></div>' + f'<div class="sig">{mark(54)}</div>')
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONT_CSS}{LAYOUT_CSS}{css}"
            f"</style></head><body>{body}</body></html>")
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        h = Path(td) / "t.html"
        png = Path(td) / "t.png"
        h.write_text(html)
        subprocess.run(["node", str(ROOT / "scripts/brand/render.js"), str(h), str(png), str(W), str(H)], check=True)
        if out.suffix.lower() in (".jpg", ".jpeg"):
            subprocess.run(["convert", str(png), "-quality", "90", "-strip", str(out)], check=True)
        else:
            png.replace(out)
    if out.stat().st_size > 2 * 1024 * 1024:
        raise SystemExit(f"{out} exceeds 2 MB")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--layout", choices=LAYOUTS, required=True)
    ap.add_argument("--text", default="")
    ap.add_argument("--art", type=Path)
    ap.add_argument("--left-art", type=Path)
    ap.add_argument("--rule-no", default="RULE 3")
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    print(render(a.layout, a.text, a.out, a.art, a.rule_no, a.left_art))
