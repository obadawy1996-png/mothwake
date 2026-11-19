# MOTHWAKE Shorts: Reusable Asset Kit

**Status:** Creative Director proposal, 2026-11-19. Not approved. Character sheets and reference images still need owner approval (see `production/CHARACTER_BIBLE.md`, consistency process step 1).
**Scope:** the 30-Short slate in `stories/shorts/SH001-SH030.json`.
**Engine:** Google Flow (Veo 3.1), as the owner specified on 2026-11-19. Every Short is **fully animated**. No still-image slideshows.

## How the kit works with Flow

- Each Flow clip is **one simple action**, 4–8 s, 9:16.
- Each clip uses **at most 3 Ingredients** (reference images). The usual set is 1 character + 1 environment, plus the Tenant or the moth when needed.
- **No text in generated video.** Rule cards, door numbers, fridge letters, fog writing, phone UI, captions and countdowns are all animated motion graphics added in post. The Phone Screen kit (E7) is post-only and never generated in Flow.
- **Model rule.** `lite` for ordinary actions. `fast` for the one key animated moment per Short (two in SH026).
- **Credit cap.** At most 150 credits per Short, including one retry per clip. All 30 Shorts fit: estimated range 80–140, slate total in SLATE.md. These figures are **estimates** from the owner's brief (Lite 10 / Fast 20 per generation). They are not measured.
- Reference images are named `REF-<ID>` in every `flow_clips[].ingredients` list. The same 2–3 images repeat across a Short's clips, which keeps consistency high and set-up time low.

## Recurring environments (8)

Usage counts are across the 30 Shorts, counting each Short once.

| ID | Ref image | Environment | Description | Lighting (Env. Bible) | Palette accent | Mobile readability | Used in |
|---|---|---|---|---|---|---|---|
| E1 | REF-E1-HALLWAY | **Vesper Court Hallway** | Third-floor corridor of an old block: doors 7–12, Ivy is flat 9, Dot is flat 8. Glowing 60-second push-button timer. A numberless door at the far end. Redressed as the inside hall of Ivy's flat for SH029. | L4 + warm timer-light pools | Timer button in Lamp #F1DDB0 | Doors are the vertical subject, so they fill a 9:16 frame naturally. Keep the corridor end in the top third. | 4 |
| E2 | REF-E2-KITCHEN | **Night Kitchen** (Ivy's flat) | Fridge with magnets, black window over the sink (reflections), kettle, pantry cupboard, amber radio on the sill, one table lamp. | L4, fridge light, lamp | Amber radio and kettle glow #B89A68 | The window reflection must sit in the centre third, or SH026 is unreadable on a phone. | 7 |
| E3 | REF-E3-BEDROOM | **Small Bedroom** | One room, three dressings: Theo's room (moth nightlight, small bed, crayon drawings), Ivy's room (mirror, nightstand), Jun's room (posters, desk). Same window and wardrobe positions. | L4, L2 phone glow | Moth nightlight Lamp #F1DDB0 | Bed low in frame, window high, so a vertical stack leaves room for captions. | 11 |
| E4 | REF-E4-BUS | **Night Bus No. 9** | Single-deck bus: back seat, fogged windows, red STOP buttons, cab window, mirror. Exterior: rain shelter on the Fenwick Road route. | L3 Sodium Street | STOP button red, muted (#8E3B32) | Shoot down the aisle (a vertical vanishing point). Fog writing must be at least 12% of frame height. | 5 |
| E5 | REF-E5-LAUNDROMAT | **Suds & Spin Laundromat** | 24-hour launderette: a dryer row with round portholes, plastic chairs, folding table, a small CCTV monitor. | Warm buzzing tubes (Lamp, dimmed) | Porthole rims Old Gold | The portholes are strong circles that read at thumbnail size. Use them as the frame-1 motif. | 3 |
| E6 | REF-E6-WINTERLANE | **Winter Lane** | Snowy residential street outside Vesper Court: streetlamp WL-14, footpath, garden, building front, Dot's upstairs window. This is the seasonal hero. A no-snow variant can follow after winter. | L1 / L3, snow FX | Streetlamp cone Lamp | Keep the streetlamp on the left third so the cone runs down the frame. Snow particles must not hide faces. | 6 |
| E7 | (post only) | **Phone Screen kit** | Fictional generic UI: lock screen, camera, notifications, parcel app, sleep-sounds app, council form. No real brands. Built as motion graphics, never in Flow. | L2 Screen Glow | Cool white-blue (the only cool key) | Inter 700, at least 48 px at 1080×1920. Keep within 80% safe width. | 6 |
| E8 | REF-E8-PHARMACY | **Night Pharmacy Hatch** | Late-night pharmacy: thick glass hatch with slot and bell, steel counter, glowing back shelves, stockroom door, front door. | Shelf glow + L4 | Green cross sign, desaturated (#5D7A63) | The glass hatch is a natural frame-in-frame. Keep faces behind the glass. | 3 |

## Recurring characters (6)

All characters follow the house style: two-tone cel, a Charcoal rim line, and Lamp-tone eye highlights (in SH022 the highlight itself is a story beat). Each character has one unique accent colour for instant recognition on small screens.

| ID | Ref image | Character | One-line essence | Silhouette hook | Accent | Mobile readability | Used in |
|---|---|---|---|---|---|---|---|
| CH-IVY | REF-IVY | **Ivy Marr**, 27 | A night-shift pharmacy assistant who can't sleep. Curious to a fault: she is the moth. | Long rust scarf, low bun | Rust #A4553A | The scarf reads even in silhouette. Keep the face at least 15% of frame height in close-ups. | 27 |
| CH-THEO | REF-THEO | **Theo Marr**, 7 | Ivy's nephew, who lives with her. He knows the rules before the adults do. | Oversized pyjamas, cowlick | Mustard-yellow #D8B54A (socks, raincoat) | The yellow socks are the identifier (SH009 frame 1). | 8 |
| CH-DOT | REF-DOT | **Dot Ferris**, 78 | Flat 8. Kind, folk-wise, and secretly the building's keeper. | Round shoulders, hearing aid | Teal cardigan #4E7F7A | The cardigan is a plot device (SH005, where the Tenant wears it). | 2 |
| CH-JUN | REF-JUN | **Jun Sato**, 15 | The upstairs teen who lives through his phone. Our tech-horror lead. | Hood up, phone glow on his face | Lime hoodie cords #9DBA5A | The cords identify him in cropped shots (SH011). | 3 |
| CH-TENANT | REF-TENANT | **The Tenant** (entity) | A too-tall, thin, Ash-Violet presence that plays every threat: closet thing, driver's double, the shape under the lamp. It is never fully shown in light. | Head always slightly above the door frame | Ash Violet #77717D, Lamp eyes only at the reveal | It must stay a silhouette at thumbnail size. Never give it a mouth in close-up (low gore). | 23 |
| CH-MOTH | REF-MOTH | **The Watcher Moth** (easter egg) | The brand emblem (concept B) as an in-world motif, placed once in every Short. It is the hero in SH006, SH024 and SH030. | Eye-marked forewings | Old Gold #B89A68 | It must read at 40 px. In 11 Shorts it is a post-composited 6-frame flutter sprite rather than a Flow ingredient. | 30 |

**Extras:** background passengers, customers and the bus driver are faceless or cropped (hands, eyes in a mirror). They need no character sheet and use the environment reference only.

## Universe threads (rewatch and comment value)

- **Fenwick Road** runs through SH017 and SH027. **Flat 8 / Dot** runs through SH005, SH024 and SH030. **Dryer portholes** link SH001 and SH028. **The lamp-eye highlight** links SH022 and the house style.
- No episode depends on another. Every Short is complete on its own.

## Production notes and open dependencies

1. **Reference images (13: 6 characters + 7 environments)** must be designed and approved before any Flow generation. This is a critical dependency. It needs owner approval and is not started.
2. The Environment Bible's "limited motion / parallax" recipes are superseded for Shorts by the owner's fully-animated Flow decision. `production/ENVIRONMENT_BIBLE.md` is owned by another agent; a change has been raised, not made.
3. Text, UI and captions are all post work. Estimated motion-graphics effort is low to medium per Short (unknown until a pilot is timed).
4. Credit figures are estimates only. A pilot should measure the real retry rate before the cap is trusted.
