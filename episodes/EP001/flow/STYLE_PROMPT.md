# EP001 — Locked style prompt (MOTHWAKE 2D look)

**Status:** draft v1, 2026-11-19. Locked once the owner approves the first style frame (`REF-STYLE-01`). After locking, do not edit the wording: change it only as a new version (v2) and note which clips used which version.

## How to use
Every Flow prompt (stills in `REFERENCE_IMAGES.md` and clips in `CLIP_PROMPTS.md`) is built as:

```
[STYLE PREFIX]  +  [SHOT TEXT]  +  [AVOID LINE]
```

Paste the prefix and the avoid line **exactly**, character for character. Only the shot text changes.

## STYLE PREFIX (v1) — copy exactly

```
MOTHWAKE style. Dark 2D hand-drawn animation, flat cel shading with only two tones per surface (base and shadow) and one soft warm rim light from the single light source in the scene. Strictly limited palette: near-black obsidian, charcoal, muted ash violet, dull old gold, bone white, and one warm lamp-yellow light. Cool ash-violet darkness surrounds one warm pool of light. Painted flat backgrounds with no outlines and soft simplified edges away from the focal point; characters drawn with a thin dark charcoal line. Small warm lamp-coloured highlights in every eye. Quiet, still, atmospheric night. Restrained motion, slow camera. 16:9 cinematic frame.
```

## AVOID LINE (v1) — copy exactly, at the end of every prompt

```
Avoid: photorealism, 3D render, CGI, glossy plastic look, anime, chibi, bright or saturated colours, neon, multiple coloured light sources, heavy lens flare, blood, gore, wounds, corpses, monsters with faces, teeth or claws, text, letters, numbers, words, captions, subtitles, signage lettering, logos, brand names, watermarks, readable screens, extra fingers, distorted hands, people speaking or moving their lips, camera shake, fast cuts.
```

## Audio line (clips only) — add before the avoid line
Veo 3.1 generates audio. MOTHWAKE sound is designed in post (the Echo's voice is never generated), so ask for near-silence and plan to mute or replace it.

```
Audio: quiet room tone only, no speech, no voices, no music.
```

## Why it is worded this way
| Choice | Reason |
|---|---|
| Colour **names**, not hex codes | Text-to-video models read colour words better than hex. Hex strings can also appear as stray on-screen text (a risk, not a measured result). The hex values stay in the bibles and are checked in QC. |
| "only two tones per surface" + "one soft warm rim light" | Matches the Character Bible shading rule (two-tone cel + one rim from the motivated light). |
| "one warm pool of light" | Environment Bible: one motivated warm light per scene. |
| Lamp highlights in eyes | The MOTHWAKE signature (Character Bible). |
| No text at all | Signs, notepad pages, the caller ID, clock digits and tape labels are **added in post** with brand type. Generated text is usually garbled and can produce real brand names. |
| No lip movement | The town is silent; Ines never speaks; the Echo's voice is post-only. |
| No gore, no monster face | Brand pillar "dread over gore"; the Echo is never shown (see `production/characters/CH-ECHO/sheet.md`). |

## Negative list (full, for QC review of every take)
Reject or repaint a take that shows any of these:
- Photorealistic texture, 3D shading, subsurface skin, specular gloss, depth-of-field bokeh that looks like a real lens.
- Colours outside the palette: saturated reds (except the small Signal Red indicator lights on the tower, the recorder and the booth mic), cyan, bright green, pink, neon.
- More than one warm light source in a scene (except where a clip says so).
- Any readable or pseudo-readable text, logos, real phone UI, real car badges, real radio brands.
- Faces, eyes, teeth, mouths or a full body on the Echo.
- Blood, injury, dead bodies.
- Character drift: wrong accent colour, missing silhouette marker (Cal's headphones, Ines's pencil bun and notepad).
- Extra or fused fingers; hands that change shape between frames.
- Lips moving on any character.
- Style flicker (frames switching between flat and shaded looks).

## Flow settings to keep fixed (all clips)
| Setting | Value |
|---|---|
| Aspect ratio | 16:9 |
| Clip length | 8 s (Flow default for these models, per owner brief) |
| Outputs per prompt | **1** (each extra output costs credits; confirm in the Flow UI before generating) |
| Mode | Ingredients to Video (up to 3 reference images; Veo 3.1 Lite or Fast only) |
| Style prefix version | v1 (record it in the generation log) |

Note: whether Flow has a separate negative-prompt field is **unknown** (not checked). If it has one, put the avoid line there; if not, keep it at the end of the prompt.
