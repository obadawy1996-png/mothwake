# Thumbnail System

Preview: `brand/previews/thumbnail_system.png`. Renderer: `scripts/brand/thumbnail.py`. Output is 1280 × 720 JPG, under 2 MB (enforced).

## Layouts

| Layout | When | Composition |
|---|---|---|
| **watcher** | A threat or presence | Subject on the right 60%, 1–2 word stack on the left, the last word in Lamp |
| **light** | A mystery object or place | Subject centred in a pool of light, heavy vignette, optional single word at the top |
| **split** | Wrongness or comparison ("which one is real?") | Desaturated "normal" on the left, the wrong version on the right, gold hairline divider |
| **rule** | Rules-based or instruction stories | A tilted Bone note card with "RULE N" and a short rule beside the subject |

```bash
.venv/bin/python scripts/brand/thumbnail.py --layout watcher --art episodes/EP001/art/thumb.png --text "DON'T|ANSWER" --out episodes/EP001/thumb_A.jpg
```

## Rules

1. One focal subject, readable as a silhouette at 160 px wide.
2. At most 4 words. The renderer refuses more. The text must not repeat the title.
3. Every thumbnail has one visible mystery: a hidden face, a wrong detail, or light where none should be.
4. Brand signature: the gold Watcher mark, 54 px, bottom-right. It is never the focus.
5. Palette: dark field, warm light, and Lamp for the single hot word. No red arrows, circles or fake screenshots.
6. No gore. No misleading imagery the video doesn't show.
7. Make at least 2 variants (A/B) per long-form video using YouTube's built-in thumbnail test where available.

## Checklist before approval

- [ ] Readable at 160 × 90 px (mobile feed)
- [ ] Clear in both dark and light YouTube themes
- [ ] Art is original or licensed, and recorded in the episode manifest
- [ ] Title and thumbnail together make a question, not a duplicate
