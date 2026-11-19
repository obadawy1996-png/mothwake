# Logo Usage Guide

## Concepts explored

Previews are in `brand/previews/concept_A.png`, `concept_B.png` and `concept_C.png`.

| Concept | Idea | Strengths | Weaknesses |
|---|---|---|---|
| A — Nocturnal Moth | A resting moth with a point of light above it | Clear silhouette and a direct "drawn to the light" story | Without the light dot it could be any moth or nature brand |
| **B — The Watcher (APPROVED 2026-11-19)** | A moth whose forewing eyespots read as a face looking back | Distinctive and slightly unsettling, with a double read that matches the tagline. Holds at 32 px. | At 16 px the eyespots merge, though the silhouette still reads |
| C — Awakening | Abstract wing shards around a vertical slit-eye, with a light above | Minimal and modern | Less ownable, reads as generic "eye" iconography, weaker as a profile icon |

**Why B:** it is the only concept that says *horror* and *moth* at once without gore or clip-art, and it stays recognisable inside a circular crop.

> **Approved by the owner on 2026-11-19.** Any future change needs a new approval, then `scripts/brand_validator.py lock`.

## Construction

- The mark is drawn on a 100 × 100 grid, mirror-symmetric about the vertical axis.
- Parts: falcate (hook-tipped) forewings, tucked hindwings, a 9.2-unit-wide body, a head and feathered crescent antennae.
- The eyespots are rings cut out of the wing, with a solid pupil (radius 7.2 outer, 3.0 inner).
- The pupils may take the Lamp highlight (#F1DDB0) in full-colour use only. In single-colour versions they are the wing colour.

## Variants (`brand/logo/`)

| File | Use |
|---|---|
| `mothwake_primary_{dark,light,transparent}.svg/.png` | Stacked: mark, wordmark and tagline. Channel art and about pages. |
| `mothwake_secondary_{dark,light,transparent}` | Horizontal: mark and wordmark. Headers and narrow spaces. |
| `mothwake_icon_{dark,light,transparent}` | Mark only. Avatars, favicons and stickers. |
| `mothwake_mono_{black,white}`, `mothwake_icon_mono_{black,white}` | Single-colour reproduction |
| `mothwake_wordmark_gold` | Wordmark only, with text as outlines |

All SVG text is converted to outlines, so no fonts are needed to open them.

## Rules

- **Clear space:** at least the height of the moth's head times 2 (about 9% of the mark's width) on every side.
- **Minimum size:** the mark is 24 px on screen (eyespots readable from 32 px). The stacked lockup is 180 px wide, and the tagline is dropped below 320 px wide.
- **Backgrounds:** gold on Obsidian or Charcoal, Obsidian on Bone, or white mono on busy footage with the soft shadow watermark.

**Never:**
- stretch the mark or change its proportions
- recolour it outside the palette
- add bevels, metallic gradients, glows, outlines, or drips or other gore
- rotate it
- put it on clashing mid-tones without the shadow
- rebuild it by hand instead of using the master files
