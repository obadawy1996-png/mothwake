# Character Bible

## House style (all characters)

- **Proportions:** 6.5 heads tall for adults, 5 for teens, 4 for children. Slightly elongated necks and fingers (the "moth" stylisation) without becoming grotesque.
- **Faces:** large, readable eyes with simple shapes. Expressions are carried by brows and mouth. **Eye highlights are always a warm Lamp tone (#F1DDB0) from the scene's light source.** This is the MOTHWAKE signature.
- **Line:** no outlines on background objects. Characters get a 2–3 px Charcoal (#25232B) rim line at 1080p.
- **Shading:** two-tone cel (base and shadow), plus one soft rim light from the motivated light source.
- **Silhouette test:** every character must be identifiable as a solid black shape.
- **Wardrobe:** muted desaturated base colours, each with one accent colour that is unique per character (used for recognition).
- **Threats and entities:** never fully shown in daylight. They are drawn as silhouettes, partial reveals or wrong proportions, using Ash-Violet and Obsidian, with Lamp-coloured eyes only at the reveal.

## Character sheet template (one per character, in `production/characters/<id>/`)

| Field | Content |
|---|---|
| ID | e.g. `CH-NADIA` |
| Role, age, one-line essence | |
| Silhouette | Front and 3/4 views, solid black |
| Turnaround | Front, 3/4, side, back (reference images) |
| Palette | Base, shadow and accent hex values |
| Expressions | Neutral, curious, uneasy, afraid, terror, relief, blank (see EXPRESSION_LIBRARY) |
| Poses | Standing, walking, turning-to-look, reaching, recoil, sitting (see POSE_LIBRARY) |
| Voice | Voice ID and direction (see SOUND_IDENTITY) |
| Google Flow ingredients | Up to 3 approved reference images. These are the ONLY references used for generation. |
| Approved by / date | |

## Consistency process (2D Character Consistency Supervisor)

1. Design the character sheet first, and get owner approval.
2. Every generated shot is compared with the sheet's silhouette, proportions, palette and accent. Any mismatch means regenerate or repaint.
3. Approved references are hashed into the episode manifest. Unapproved variants never enter the edit.

## Planned recurring element

**The Moth** (from MW003, *Lost Moth Poster*): it may appear in later stories as an easter egg on walls, windows and lamps. This builds universe recognition and gives the audience something to find on rewatch.
