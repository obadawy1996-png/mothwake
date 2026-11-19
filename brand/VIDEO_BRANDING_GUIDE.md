# Video Branding Guide

The story always comes first. The brand is the atmosphere around it, not an interruption.

## Opening

- **No logo intro.** Frame 1 is the strongest story image and the hook line within the first 1.5 s.
- **Optional:** `brand/sound/mothwake_open_sub.wav`, a 0.9 s sub-bass breath at −24 LUFS mixed *under* the first shot.
- **Long-form only:** the signature sound (`mothwake_signature.wav`, 1.65 s) may play over the title card after the cold open (roughly 20–60 s in).

## During the video

| Element | Rule |
|---|---|
| Watermark | `brand/kit/watermark_gold.png`, or `watermark_white.png` on bright scenes. Bottom-right, 4% margin, 55–60% opacity, 64–80 px tall at 1080p. Hide it during title cards, the ending, and any shot where it covers story-critical detail. For the YouTube channel watermark (Studio → Customization → Branding), upload the same 150 × 150 PNG. |
| Captions (Shorts) | Inter Bold 64 px at 1080 × 1920, Bone with the key word in Lamp, black shadow, centred at y ≈ 1180. That keeps them clear of the platform UI at the top and bottom (zones to be confirmed against `research/PLATFORM_SPECS.md`). At most 2 lines and 6 words per line. Preview: `brand/previews/caption_style_shorts.png`. |
| Captions (long-form) | Inter SemiBold 46 px at 1080p, lower third, same colours. |
| Title cards | `brand/templates/title_card_template.html`: "A MOTHWAKE STORY" in Cinzel, then the title in Cormorant Italic. 2–3 s maximum. |
| Grade | Lifted blacks toward Charcoal. Warm practical lights (Lamp or Gold) against cool Ash-Violet shadows. No teal-orange presets. |

## Ending

- **Shorts:** end on the story's final beat. At most 1.0 s of the moth mark fading in on the last frame (optional). No end screen. A loop-friendly last line is encouraged.
- **Long-form:** use `brand/video/mothwake_outro_1920x1080.mp4` (3.2 s, flutter sting and moth mark), then a 10–20 s end screen with 2 related stories and a subscribe element (YouTube end-screen editor).
- A spoken subscribe reminder is used only when it fits the story's voice. Never mid-story.

## Exports

- **Clean master:** no watermark and no platform UI, kept permanently in `episodes/<id>/master/`.
- **Platform variants:** the watermark is burned in only where it adds value. TikTok, Instagram and Facebook exports never carry another platform's watermark.

## Automated checks

`scripts/brand_validator.py episode episodes/<id>/manifest.json` must pass before rendering. A missing, modified or unapproved asset blocks the render.
