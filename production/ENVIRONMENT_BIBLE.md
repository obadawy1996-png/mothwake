# Environment, Lighting and Background Bible

## Environment principles

- **The mundane made wrong.** Houses, buses, elevators, diners and phones. Familiar places with one wrong detail are scarier than castles.
- **One motivated warm light per scene** (lamp, porch light, phone screen or streetlight) against cool Ash-Violet darkness. The viewer, like the moth, is drawn to it.
- **Layered for parallax:** every background is built in 4–6 layers (sky, far, mid, near, foreground silhouette, light FX) so the camera can move without new art.
- **Detail budget:** high detail at the focal point only, with soft and simplified edges.

## Lighting library

| Preset | Use | Key | Fill/shadow | Notes |
|---|---|---|---|---|
| L1 Porch Lamp | Exteriors at night | #F1DDB0 cone from above | #25232B | Floating dust specks |
| L2 Screen Glow | Phones, TVs | Cool white-blue on the face from below | #090A0D | Only cool key allowed |
| L3 Sodium Street | Roads, buses | #B89A68 amber | #3A3546 | Rain streaks |
| L4 Moonless Interior | Houses at 3 a.m. | Ash-Violet ambient | Obsidian | Eyes catch the Lamp highlight |
| L5 Reveal | The final beat | Warm key suddenly from a *wrong* direction | Hard shadows | Used once per story |

## Background library (built once, reused with variation)

`production/backgrounds/<id>/` holds the layered PSD/PNG and a JSON describing the layers.

Starter set, matching the first slate:
- suburban street at night (MW001, MW008)
- apartment corridor and elevator (MW002)
- small-town poles and laundromat (MW003)
- kitchen, front door and peephole (MW004, MW008)
- closed store floor (MW005)
- empty highway loop (MW007)
- bus interior (MW011)
- diner (MW012)

Each background gets at least 3 dressing variants (props and signage swapped), so reuse never looks identical.

## Pose, expression and animation reference libraries

- `production/library/poses/`: reusable pose drawings per character body type (see CHARACTER_BIBLE).
- `production/library/expressions/`: 7 core expressions, front and 3/4 views.
- `production/library/animation/`: approved motion recipes:
  - **Parallax drift:** 6–10 s camera move, at most 4% scale
  - **Slow push-in:** for dread beats
  - **Breathing loop:** a 2% chest scale over 3 s
  - **Blink:** 4 frames at 24 fps
  - **Head turn:** 3 drawings plus a smear
  - **Flicker:** irregular light opacity
  - **Rain overlay**
  - **Dust specks**
  - **Moth flutter:** a 6-frame loop

**Limited but intentional motion:** the camera and lights move constantly while characters move economically. Full motion is saved for the scare beat.

### Added 2026-11-19 (EP001 storyboard need)

| Preset | Use | Key | Fill/shadow | Notes |
|---|---|---|---|---|
| L6 Overcast Day | Daytime exteriors and interiors (EP001 town by day, library, porch) | Soft, flat Bone-grey sky light (#E7E2D8 at low saturation) | Charcoal #25232B, shadows lifted, no hard sun | The town looks friendly but drained of colour. Keep Lamp only on practical lights. |
