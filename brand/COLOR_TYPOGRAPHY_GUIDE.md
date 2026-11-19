# Colour and Typography Guide

## Palette

| Name | Hex | Role |
|---|---|---|
| Obsidian Black | #090A0D | Primary background, the night |
| Charcoal | #25232B | Secondary surfaces and gradients |
| Ash Violet | #77717D | Supporting text, tagline on dark, mist |
| Old Gold | #B89A68 | The mark, wordmark and accents (the moth) |
| **Bone** *(proposed refinement)* | #E7E2D8 | Light-background base, caption text |
| **Lamp** *(proposed refinement)* | #F1DDB0 | Rare highlight: the unknown light, eyespot pupils, the hot word in a thumbnail |

**Why the two refinements:** the core palette has no light tone. Without one, light-background logos, captions and readable thumbnail text are impossible. Lamp is used sparingly, like the light in the metaphor.

### Contrast (WCAG 2.x)

Ratios were computed with the WCAG relative-luminance formula.

| Pair | Ratio | Rating |
|---|---|---|
| Old Gold on Obsidian | 7.4 : 1 | AAA |
| Bone on Obsidian | 15.3 : 1 | AAA |
| Lamp on Obsidian | 14.8 : 1 | AAA |
| Ash Violet on Obsidian | 4.2 : 1 | AA for large text only. Tagline only, never body copy. |
| Obsidian on Bone | 15.3 : 1 | AAA |
| Old Gold on Bone | 2.1 : 1 | **Fails**. Never use gold on light backgrounds; use Obsidian. |

## Typography

All three families are **SIL Open Font License 1.1**: free for commercial use, embedding and video. The licence texts are in `brand/fonts/licenses/`, downloaded from the google/fonts repository on 2026-11-19.

| Family | Use | Weights |
|---|---|---|
| Cinzel | Wordmark, tagline, small-caps labels ("A MOTHWAKE STORY", "RULE 3") | 500–600, tracked +16% to +42% |
| Cormorant Garamond | Episode title cards, long-form chapter cards | Italic 500 |
| Inter | Captions, thumbnail text, UI and descriptions | 700–800 |

Rules:
- Cinzel is always uppercase and tracked. Never use it for long sentences.
- Captions are Inter Bold, Bone, with the key word in Lamp and a black shadow. There is no box.
- Thumbnails use Inter ExtraBold, at most 4 words.
