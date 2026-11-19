# MOTHWAKE — Brand Guidelines

**Status:** Implemented and tested. The logo concept is a **provisional selection pending owner approval** (see LOGO_USAGE_GUIDE.md).

## Brand core

| | |
|---|---|
| Name | MOTHWAKE |
| Tagline | SOME THINGS SHOULD STAY ASLEEP. |
| Category | Independent 2D animated horror and mystery entertainment |
| Promise | Original stories that pull you toward the light, then show you what was waiting there. |
| Personality | Dark · mysterious · psychological · atmospheric · distinctive · memorable · artistic · unsettling without gore |
| Visual metaphor | A nocturnal moth drawn to an unknown light. Curiosity is the hook, and danger is the payoff. |

## The idea behind the mark

The selected emblem (concept B, "The Watcher") is a resting moth whose forewings carry eye markings. Read quickly it is a moth. Look again and it is a face looking back at you. That double read is the brand: things are not what they first appear to be.

## Brand pillars

1. **Curiosity first.** Every story opens on a question the viewer needs answered.
2. **Dread over gore.** Fear comes from implication, sound, silhouette and wrongness.
3. **Earned endings.** Twists must be set up. No cheap "it was a dream".
4. **A recognisable world.** One consistent animation language, palette and sound.
5. **Story before brand.** Branding never delays or interrupts the story.

## Voice and tone

- Quiet, precise and confident. Second person is allowed sparingly ("You've heard it too.").
- Short sentences. No exclamation marks in brand copy. No clickbait that the video doesn't pay off.
- Never claim fiction is real. Stories are presented as stories ("A MOTHWAKE STORY").

## Core files

| Guide | Covers |
|---|---|
| LOGO_USAGE_GUIDE.md | Concepts, the selected mark, variants, clear space, minimum sizes, misuse |
| COLOR_TYPOGRAPHY_GUIDE.md | Palette, contrast and type system |
| VIDEO_BRANDING_GUIDE.md | Openings, watermark, captions, title cards and endings |
| THUMBNAIL_SYSTEM.md | Layouts, rules and the renderer |
| CHANNEL_COPY.md | Descriptions, bios and trailer script |
| SOUND_IDENTITY.md | Signature, outro, sound design and narration direction |
| ASSET_MANIFEST.md | Every file, its size and specification |

## Rebuilding the kit

```bash
.venv/bin/python scripts/brand/build_brand.py
```

```bash
.venv/bin/python scripts/brand/build_kit.py
```

```bash
.venv/bin/python scripts/brand/build_sound.py
```

```bash
.venv/bin/python scripts/brand_validator.py check
```

Approved assets are hashed in `brand/APPROVED_ASSETS.lock`. Any change must be approved and then re-locked with `brand_validator.py lock`.
