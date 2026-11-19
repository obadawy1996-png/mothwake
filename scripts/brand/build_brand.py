#!/usr/bin/env python3
"""Generate MOTHWAKE logo concepts and the full logo system as SVG.

All marks are hand-built vector geometry (no AI raster art). Text is converted
to outlines from the OFL fonts in brand/fonts, so SVGs render identically
everywhere without font installs.

Usage: .venv/bin/python scripts/brand/build_brand.py
"""
from __future__ import annotations

import json
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[2]
FONTS = ROOT / "brand" / "fonts"
OUT = ROOT / "brand" / "logo"
CONCEPTS = ROOT / "brand" / "concepts"

C = {  # core palette + two proposed refinements (see COLOR_TYPOGRAPHY_GUIDE.md)
    "obsidian": "#090A0D", "charcoal": "#25232B", "ash": "#77717D", "gold": "#B89A68",
    "bone": "#E7E2D8",      # refinement: light-background base
    "lamp": "#F1DDB0",      # refinement: rare highlight for the "light" motif
}

# ---------------------------------------------------------------- text → paths
_font_cache: dict = {}


def font(name: str, wght: int) -> TTFont:
    key = (name, wght)
    if key not in _font_cache:
        f = TTFont(FONTS / name)
        if "fvar" in f:
            f = instantiateVariableFont(f, {"wght": wght}, inplace=False)
        _font_cache[key] = f
    return _font_cache[key]


def text_path(txt: str, fname: str, wght: int, size: float, tracking: float = 0.0):
    """Return (svg_path_d, width, cap_height) for txt at size px, origin at baseline-left."""
    f = font(fname, wght)
    upm = f["head"].unitsPerEm
    s = size / upm
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    hmtx = f["hmtx"]
    pen = SVGPathPen(gs)
    x = 0.0
    for i, ch in enumerate(txt):
        g = cmap.get(ord(ch))
        if g is None:
            continue
        tp = TransformPen(pen, (s, 0, 0, -s, x, 0))
        gs[g].draw(tp)
        x += hmtx[g][0] * s
        if i < len(txt) - 1:
            x += tracking * size
    cap = getattr(f["OS/2"], "sCapHeight", 0.7 * upm) * s
    return pen.getCommands(), x, cap


# ---------------------------------------------------------------- mark geometry
# viewBox -50 -50 100 100, symmetric about x=0. Right half defined, left mirrored.
BODY = ("M0 -12 C3.6 -12 4.6 -6 4.6 2 C4.6 11 3 19 0 24 "
        "C-3 19 -4.6 11 -4.6 2 C-4.6 -6 -3.6 -12 0 -12 Z")
HEAD = "M0 -20 a4.6 4.6 0 1 0 0.001 0 Z"
# Swept, falcate (hook-tipped) forewing: the classic resting-moth delta.
FORE = ("M6.2 -11 C16 -20 33 -25 49 -22 C47.5 -18.5 45.6 -17.6 44.6 -14.6 "
        "C42.6 -6 40 1 37 6 C26 8.4 14 7.4 6.2 4 Z")
# Small rounded hindwing, mostly tucked behind the forewing.
HIND = ("M6.2 6 C16 9 28 10 33 12.5 C33.4 22 24 31 14 29 "
        "C8.6 27.6 6.2 20 6.2 12 Z")
# Feathered (pectinate) antenna as a filled crescent leaf.
ANT = ("M1.8 -23.5 C6 -33 13.5 -40 23 -43 C20.6 -40.2 17 -38.6 14.6 -35.4 "
       "C11 -31 7 -26 3.4 -22 Z")
def circle(cx, cy, r):
    return f"M{cx - r} {cy} a{r} {r} 0 1 0 {2 * r} 0 a{r} {r} 0 1 0 {-2 * r} 0 Z"


def mirror(d: str) -> str:
    return f'<path d="{d}" transform="scale(-1 1)"/>'


def mark_svg_group(concept: str, fg: str, accent: str | None = None) -> str:
    """Return <g> for the mark. Single colour unless accent given (eye pupils)."""
    ant = f'<g fill="{fg}"><path d="{ANT}"/><path d="{ANT}" transform="scale(-1 1)"/></g>'
    if concept == "A":  # Nocturnal moth + the unknown light above it
        wings = f'<path d="{FORE}"/><path d="{HIND}"/>' + mirror(FORE) + mirror(HIND)
        light = f'<path d="{circle(0, -47, 2.8)}"/>'
        return (f'<g fill="{fg}">{wings}<path d="{BODY}"/><path d="{HEAD}"/>{light}</g>{ant}')
    if concept == "B":  # Eye-wing moth: forewing eyespots read as a watching face
        eye_outer, eye_inner = circle(27, -9.5, 7.2), circle(27, -9.5, 3.0)
        fore = f"{FORE} {eye_outer} {eye_inner}"  # evenodd: ring cut out, pupil kept
        wings = (f'<path fill-rule="evenodd" d="{fore}"/><path d="{HIND}"/>'
                 f'<path fill-rule="evenodd" d="{fore}" transform="scale(-1 1)"/>'
                 + mirror(HIND))
        pupils = ""
        if accent:
            pupils = (f'<g fill="{accent}"><path d="{eye_inner}"/>'
                      f'<path d="{eye_inner}" transform="scale(-1 1)"/></g>')
        return f'<g fill="{fg}">{wings}<path d="{BODY}"/><path d="{HEAD}"/></g>{ant}{pupils}'
    if concept == "C":  # Abstract awakening: wing shards around a vertical slit-eye
        wing = "M8 -4 C20 -22 34 -34 46 -40 C42 -24 36 -6 26 8 L8 10 Z"
        eye = "M0 -30 C9 -16 9 16 0 30 C-9 16 -9 -16 0 -30 Z"
        slit = "M0 -18 C3 -8 3 8 0 18 C-3 8 -3 -8 0 -18 Z"
        return (f'<g fill="{fg}"><path d="{wing}"/><path d="{wing}" transform="scale(-1 1)"/>'
                f'<path fill-rule="evenodd" d="{eye} {slit}"/>'
                f'<path d="{circle(0, -42, 3)}"/></g>')
    raise ValueError(concept)


def svg(w, h, body, bg=None, vb=None) -> str:
    vb = vb or f"0 0 {w} {h}"
    bgr = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="{vb}">{bgr}{body}</svg>\n')


def mark_only(concept, size, fg, bg=None, accent=None, pad=0.08):
    s = size * (1 - 2 * pad) / 100
    g = mark_svg_group(concept, fg, accent)
    return svg(size, size, f'<g transform="translate({size / 2} {size / 2 + size * 0.02}) scale({s})">{g}</g>', bg)


def wordmark(size, fg, tracking=0.16):
    d, w, cap = text_path("MOTHWAKE", "Cinzel[wght].ttf", 600, size, tracking)
    return d, w, cap


def tagline(size, fg, tracking=0.32):
    return text_path("SOME THINGS SHOULD STAY ASLEEP.", "Cinzel[wght].ttf", 500, size, tracking)


def lockup_stacked(fg, bg=None, accent=None, concept="B", with_tag=True):
    mark = 420
    d, w, cap = wordmark(150, fg)
    td, tw, tcap = tagline(34, fg)
    W = int(max(w, tw) + 240)
    H = 80 + mark + 70 + cap + (70 + tcap if with_tag else 0) + 90
    s = mark / 100
    y_mark = 80 + mark / 2
    y_word = 80 + mark + 70 + cap
    parts = [f'<g transform="translate({W / 2} {y_mark}) scale({s})">{mark_svg_group(concept, fg, accent)}</g>',
             f'<path fill="{fg}" d="{d}" transform="translate({(W - w) / 2} {y_word})"/>']
    if with_tag:
        parts.append(f'<path fill="{fg}" fill-opacity="0.82" d="{td}" '
                     f'transform="translate({(W - tw) / 2} {y_word + 70 + tcap})"/>')
    return svg(W, int(H), "".join(parts), bg)


def lockup_horizontal(fg, bg=None, accent=None, concept="B"):
    d, w, cap = wordmark(120, fg)
    mark = 210
    gap = 46
    W = int(60 + mark + gap + w + 60)
    H = 300
    s = mark / 100
    parts = [f'<g transform="translate({60 + mark / 2} {H / 2 + 4}) scale({s})">{mark_svg_group(concept, fg, accent)}</g>',
             f'<path fill="{fg}" d="{d}" transform="translate({60 + mark + gap} {H / 2 + cap / 2})"/>']
    return svg(W, H, "".join(parts), bg)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    CONCEPTS.mkdir(parents=True, exist_ok=True)
    manifest = {}

    # --- concept boards (all three, same treatment, for comparison)
    for c in "ABC":
        p = CONCEPTS / f"concept_{c}.svg"
        p.write_text(mark_only(c, 1024, C["gold"], C["obsidian"], accent=C["lamp"] if c == "B" else None))
        manifest[f"concept_{c}"] = str(p.relative_to(ROOT))

    # --- full system for selected concept
    sel = "B"
    files = {
        "mothwake_primary_dark.svg": lockup_stacked(C["gold"], C["obsidian"], C["lamp"], sel),
        "mothwake_primary_light.svg": lockup_stacked(C["obsidian"], C["bone"], None, sel),
        "mothwake_primary_transparent.svg": lockup_stacked(C["gold"], None, C["lamp"], sel),
        "mothwake_secondary_dark.svg": lockup_horizontal(C["gold"], C["obsidian"], C["lamp"], sel),
        "mothwake_secondary_light.svg": lockup_horizontal(C["obsidian"], C["bone"], None, sel),
        "mothwake_secondary_transparent.svg": lockup_horizontal(C["gold"], None, C["lamp"], sel),
        "mothwake_icon_dark.svg": mark_only(sel, 1024, C["gold"], C["obsidian"], C["lamp"]),
        "mothwake_icon_light.svg": mark_only(sel, 1024, C["obsidian"], C["bone"]),
        "mothwake_icon_transparent.svg": mark_only(sel, 1024, C["gold"], None, C["lamp"]),
        "mothwake_mono_black.svg": lockup_stacked("#000000", None, None, sel),
        "mothwake_mono_white.svg": lockup_stacked("#FFFFFF", None, None, sel),
        "mothwake_icon_mono_black.svg": mark_only(sel, 1024, "#000000"),
        "mothwake_icon_mono_white.svg": mark_only(sel, 1024, "#FFFFFF"),
        "mothwake_wordmark_gold.svg": (lambda d=wordmark(150, C["gold"]): svg(int(d[1] + 80), int(d[2] + 80),
                                       f'<path fill="{C["gold"]}" d="{d[0]}" transform="translate(40 {d[2] + 40})"/>'))(),
    }
    for name, content in files.items():
        (OUT / name).write_text(content)
        manifest[name] = f"brand/logo/{name}"
    (ROOT / "brand" / "build_manifest.json").write_text(json.dumps(
        {"selected_concept": sel, "palette": C, "files": manifest}, indent=2))
    print(f"wrote {len(files)} logo files + 3 concepts")


if __name__ == "__main__":
    main()
