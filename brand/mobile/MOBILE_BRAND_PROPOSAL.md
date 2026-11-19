# Mobile-First Brand Proposal (Shorts, Reels and TikTok)

**Status: PROPOSED, awaiting owner approval.** Nothing here replaces the approved, locked assets. On approval, run `scripts/brand_validator.py lock` to add these to the approved set.
Generator: `scripts/brand/build_mobile.py`. Previews are in this folder.

| Element | Proposal | Why |
|---|---|---|
| **Small-size mark** (`mark_small_*.svg`) | Same Watcher silhouette, with thicker antennae and eyespots enlarged by about 15%. Use at 96 px or below. | At 32–48 px the approved mark's eyespots fill in. This cut keeps the "eyes" readable (`preview_mark_compare.png`). Geometry and proportions are otherwise unchanged. |
| **Watermark** (`watermark_mobile_120.png`) | Small-size mark at 64 px on 1080×1920, **top-left**: 6% from the side, about 10.5% from the top, 55% opacity, dark halo. | The bottom-right corner is covered by the Shorts, Reels and TikTok button rail and the caption area. Top-left sits just under the status and search bar and stays visible. |
| **Captions** | Inter ExtraBold 78 px, Bone with **one Lamp key word**, 7 px black stroke and shadow. At most 2 lines and about 4–5 words per line. Centred at about 58% height, inside the margins (6% left, 13% right rail). | Readable at phone size; stays clear of the platform UI (`preview_caption_safe.png`, red = keep out). |
| **Covers** (`cover_hook`, `cover_rule`, `cover_choice`) | One cover per pillar. 2–4 words, top third, the key word in Lamp, one subject in the centre in a pool of light. | Pillar recognition in the grid (`preview_grid_scale.png`). Text stays readable at about 180 px wide. |
| **Opening** | No intro, no logo. Frame 1 is the hook image, and the hook line lands within 1 second. | The swipe decision happens in the first second. |
| **Ending** (`end_sting_1080x1920.mp4`) | 1.0 s: the moth mark fades in on black with the start of the signature flutter. Optional, and dropped when the story's last frame loops back to the first. | Replaces the 3.2 s outro on Shorts, keeping endings fast and loop-friendly. |
| **Animation style for phones** | Fewer, bigger shapes. One subject per frame. Faces at least 25% of frame height for reaction shots. Strong silhouettes, high value contrast. Limited motion, with one key animated moment per Short. | Small screens lose fine detail. This also keeps production fast. |

**Safe zones** are approximate, taken from typical app layouts, not from official pixel specs (research found none for organic Shorts, Reels or TikTok). Confirm them on a real phone before locking.
