# EP001 — The Quiet Hour · Storyboard v1 (draft)

**Source:** `episodes/EP001/script.md` (v3) + `episodes/EP001/vo.json` · **Format:** long-form 16:9, 1920×1080 · **Owner of this file:** Storyboard Designer · **Date:** 2026-11-19 · **Status:** draft, not reviewed

Companion file: `episodes/EP001/shots_draft.json` (the `shots` array for `scripts/production/assemble.py`). No media was generated and no paid service was used.

## Timing summary (all **estimates**)

| Item | Value | Basis |
|---|---|---|
| Narration words | 1,089 | **measured**: `scripts/production/script_stats.py`, 2026-11-19 |
| Narration, recorded | 394.2 s (6.57 min) | **measured**: ffprobe on the 15 files in `episodes/EP001/audio/processed/`, 2026-11-19 (≈ 166 wpm incl. pauses) |
| Narration, planning estimate | 487 s | estimate at 145 wpm + 0.8 s/beat; superseded by the measured files |
| Visual-only pads, silences, cards | 107 s | estimate: per-shot pads below |
| **Picture total (shots)** | **501.0 s ≈ 8:21** | sum of shot durations (estimate built on measured VO) |
| + brand outro | 3.2 s | brand/video/mothwake_outro_1920x1080.mp4 (exports.outro) |
| + end screen | 10–20 s | YouTube end-screen element, see issues |
| Shots | 98 | |
| Hero clips (Google Flow, manual) | 12 unique, used in 21 shots | budget ≤ 12 |
| Unique backgrounds | 10 (+ title card, black) | budget ≤ 10 |

| Section | Script range | Estimated length |
|---|---|---|
| Cold open | 0:00–0:30 | 23.0 s (starts ≈ 0:00) |
| Title | 0:30–0:36 | 3.0 s (starts ≈ 0:23) |
| Act I | 0:36–3:50 | 134.0 s (starts ≈ 0:26) |
| Act II | 3:50–7:30 | 156.0 s (starts ≈ 2:40) |
| Act II · second night | (inside Act II) | 49.5 s (starts ≈ 5:16) |
| Act III | 7:30–10:00 | 113.0 s (starts ≈ 6:05) |
| Ending | 10:00–10:50 | 22.5 s (starts ≈ 7:58) |

## Conventions

- **Framing:** WS wide · MS medium · CU close-up · ECU extreme close-up · insert (prop/hand detail).
- **Layers:** `kind@depth`, depth 0 = farthest (static), 1 = nearest (moves most). Files are `art/<bg_id>_<layer>.png` placeholders; a variant letter in the id (e.g. `BG01C_mid`) means a re-dressed layer on a shared plate (`BG01_bg`).
- **Move:** `push` / `drift` / `pan_left` / `pan_right` / `static`; strength is the assembler value (0.02 = barely, 0.06 = strong dread push). Keep to the Environment Bible recipe: ≤ 4% scale on drifts.
- **Lighting:** Environment Bible presets L1–L5. `DAY*` = daylight scene; the bible has **no daylight preset** (see issues). L5 Reveal is used **once**: S096.
- **Captions:** long-form lower third (y = 0.80), Inter SemiBold 46 px, Bone with key word in Lamp, ≤ 12 words, text taken from the narration. No caption on visual-only shots; on-screen notepad text is art, not caption.
- **Watermark:** hidden on title card and the whole ending (S092 onward).
- **Hero clip:** a manual Google Flow generation (no API, owner runs it). Everything else is a layered parallax still (free).

## Background inventory (10 unique)

| ID | Background | Lighting | Dressing variants | Notes | Shots |
|---|---|---|---|---|---|
| BG01 | Lantern diner interior (wide) | L1 (pendant lamps; L4 for the dark street beyond the glass) | A night busy (cold open, 2:00 exhale) · B late night, sparse, 12:5x · C quiet hour, frozen customers · D emptying, money on tables, half-eaten food · E morning, flat daylight, chairs up | booth, counter, stools, jukebox, wall clock, pendant lamps, window wall (right) | 25 |
| BG02 | Counter insert plate (generic close-up counter top) | L1 / L3 per dressing | A diner counter (coffee cup, recorder, radio behind) · B motel office desk (taped bell, laminated card, key) · C gas-station till (hand-lettered sign, change tray, tube-light flicker) | one counter-top plate re-dressed for three locations; all inserts and hand shots | 14 |
| BG03 | Diner window + hill and radio tower | L4 outside / L1 reflection | A night, tower red light (cold open, Act I) · B night 2, breath fog layer · C tower exterior, faded flashback (spring) · D tower exterior, night (Act III held silence) | window frame fg, glass reflection fx, hill + tower far layer shared by all four | 5 |
| BG04 | Highway and Wrenfield town line | L3 | A highway in rain (arrival) · B car cabin overlay (dashboard, wipers) · C town-line sign in headlights · D town line 12:55 a.m., departing tail lights | sign layer 'POP. 412' + hand-painted board shared by C and D | 6 |
| BG05 | Motel room | L4 + L2 (laptop / phone) | A night 1, cheap lamp, laptop, headphones · B night 3, every light on, notes on bed · C bedside close (clock, phone on bed) · S screen-insert plates (waveform, dashboard, phone UI) | screen plates are flat L2 graphics laid over a blurred room bg | 15 |
| BG06 | Wrenfield main street | L1 (diner glow) / L3 (street, forecourt) / DAY* | A night, everything dark except the Lantern · B day, bright, townsfolk, bike · C gas-station forecourt end, one flickering tube light · D morning, Cal's hatchback at the kerb | the gas station is the far end of main street: same far/bg, new mid | 8 |
| BG07 | Town library | DAY* (window light) / L1 desk lamp in booth | A wide reading room · B cassette drawer (labels 1974/1981/1996/2009) · C listening booth with deck | — | 10 |
| BG08 | Porch on Fenner Street | DAY* (late afternoon) | A wide porch, old woman shelling peas · B close, pea pod and hands | — | 4 |
| BG09 | Radio booth (flashback, faded colour) | L1 desaturated + red on-air light | A man at the desk (silhouette) · B empty chair, mic light on · C mic close, tower through frosted window | flashback grade: lifted, desaturated, grain fx layer | 3 |
| BG10 | Ines's flat above the diner | L4 + radio-dial glow; L5 once (door, ending) | A wide, dark, small radio · B door to hallway · C window behind Ines (moth) | — | 6 |

Shared overlay assets (not backgrounds): `BG04B_fg_cabin` (car cabin, used on highway, main street night and day), `BG01_fg_pad` (Ines's notepad, blank, text composited), `BG03_far_tower` (hill + tower, also seen through the radio-booth window), `BG01_clock_*` (diner clock faces 12:59 / 1:00), `BG04_fx_rain`, `BG06_fx_dust`, `BG09_fx_grain`.

Every location is built once in 4–6 layers per the Environment Bible; three locations (diner counter, motel office, gas-station till) share one counter-top plate (BG02), and the gas station is the far end of main street (BG06C). Each background has ≥ 3 dressing variants except BG07–BG10 (2–3; they appear in one sequence each).

## Hero clips (12, Google Flow, manual)

| Hero | Moment | Shots | Why it earns motion |
|---|---|---|---|
| H01 | Coffee keeps pouring over the rim at 1:00 while everything else freezes | S003 | the hook image; the one thing still moving at 1:00 |
| H02 | Radio-tower red light: one slow blink (one clip, re-used at the end of Act I and in the Act III held silence) | S005, S029, S091 | the recurring 'something is awake' signal; one clip, three uses |
| H03 | Ines turns her notepad to camera (blank page; text composited in post, re-used for COFFEE?/HABIT./NOT A WORD.) | S019, S020, S028 | Ines's only voice; one clip, three pages |
| H04 | Ines tears the page off, folds it, pockets it | S021 | establishes that words are dangerous objects |
| H05 | Gas attendant counts change very slowly, smile frozen | S016 | first human wrongness in town |
| H06 | Every head in the diner turns toward Cal (the episode's first full-motion scare beat) | S062 | first full-motion scare beat (bible: full motion saved for the scare) |
| H07 | Breath fog blooms on the outside of the window, then fades | S064 | the Echo's first physical trace |
| H08 | Phone buzzes on the bed (caller ID HOME), rings out, voicemail plays itself | S075, S076 | the Echo reaches into Cal's own life |
| H09 | Notepad pages torn off one by one and handed over (blank pages; four texts composited) | S080, S081, S082, S083 | Ines finally 'speaks'; the rule explained |
| H10 | Tail lights shrink into the dark past the town-line sign | S090 | Cal's escape, emotionally false relief |
| H11 | Radio dial glows; Ines's hand reaches for it and stops | S093, S095 | the twist lands on the radio |
| H12 | A moth lands on the window behind Ines, lit by the radio dial | S097 | brand easter egg and final frame |

Each hero clip must also exist as a layered still fallback (the layers listed per shot), so the episode renders end-to-end before any Flow clip exists. Character references for Flow must come only from approved character sheets (CHARACTER_BIBLE: ≤ 3 ingredients each). Notepad, sign and screen **text is never generated**: generate blank surfaces and composite text in post.

## Shot list


### Cold open

| Shot | Dur (s) | Framing | BG | Description | Layers (kind@depth) | Move | Light | VO | SFX | Caption key | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S001 | 2.0 | ECU | BG01A | Diner wall clock, second hand ticking 12:59:58 to 12:59:59. Warm Lamp light swings in. | BG01_bg bg@0.0, BG01_clock_1259 mid@0.6, BG01_fx_lamps fx@0.8 | push 0.03 | L1 | — (visual only) | brand open_sub at 0.0 (-24 LUFS, under); clock tick x2; diner murmur | — | parallax still |
| S002 | 2.5 | WS | BG01A | Booth and counter: coffee steam, waitress mid-pour, two truckers mid-laugh. | BG01_bg bg@0.0, BG01_far far@0.25, BG01A_mid mid@0.55, BG01_fx_lamps fx@0.7, BG01A_near_truckers near@0.85, BG01_fx_steam fx@0.9 | drift 0.02 | L1 | — (visual only) | laugh, cups, jukebox low, pour | — | parallax still |
| S003 | 6.0 | CU | BG02A | 1:00. Every sound stops. Only the coffee keeps running over the rim onto the counter. | BG02_bg bg@0.0, BG02A_mid_cup mid@0.6, BG02A_near_pot near@0.9 | push 0.04 | L1 | L001 | HARD CUT of all diner sound at the clock landing; only pour + clock remain | **speaks** — “In Wrenfield, nobody speaks between one and two in the morning.” | **HERO H01** |
| S004 | 6.0 | MS | BG01C | Frozen faces: truckers' mouths shut mid-laugh, waitress perfectly still. Coffee drips off the counter. | BG01_bg bg@0.0, BG01_far far@0.25, BG01C_mid mid@0.55, BG01C_near_truckers near@0.85 | push 0.04 | L1 | L002 | fridge hum, drip on lino, clock | **help** — “Not to answer a phone. Not to call for help.” | parallax still |
| S005 | 6.5 | WS | BG03A | Through the window: the radio tower on the hill blinks its red light once, slowly. | BG03_bg bg@0.0, BG03_far_tower far@0.2, BG03A_mid_glass mid@0.6, BG03_fg_frame fg@1.0 | push 0.03 | L4 | L003 | low wind outside the glass; no sting | **listened** — “I went there to find out why. I should have just listened.” | **HERO H02** |

### Title

| Shot | Dur (s) | Framing | BG | Description | Layers (kind@depth) | Move | Light | VO | SFX | Caption key | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S006 | 3.0 | card | TITLE | Title card from brand/templates/title_card_template.html: A MOTHWAKE STORY / The Quiet Hour. | TITLE_card bg@0.0 | static | n/a | — (visual only) | brand signature (1.65 s) at card start, -2 dB | — | parallax still · no watermark |

### Act I

| Shot | Dur (s) | Framing | BG | Description | Layers (kind@depth) | Move | Light | VO | SFX | Caption key | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S007 | 7.0 | WS | BG04A | Highway at night in rain. Cal's hatchback with a dented door. | BG04_bg bg@0.0, BG04A_far far@0.3, BG04A_mid_car mid@0.6, BG04_fx_rain fx@0.95 | pan_left 0.03 | L3 | L004 (~40%) | rain on tarmac, tyre hiss | **podcast** — “I make a podcast about small towns with strange habits.” | parallax still |
| S008 | 5.5 | MS | BG04B | Inside the car: Cal driving, dashboard glow, wipers, sodium light sliding over him. | BG04A_far bg@0.0, BG04B_mid_cal mid@0.6, BG04B_fg_cabin fg@1.0, BG04_fx_rain fx@0.9 | drift 0.02 | L3 | L004 (~35%) | wipers, rain on roof, indicator off | **grudge** — “A festival nobody remembers starting. A grudge between two families.” | parallax still |
| S009 | 4.5 | CU | BG04B | Cal in profile, half-smile, eyes on the road. | BG04A_far bg@0.0, BG04B_near_cal_cu near@0.8, BG04B_fg_cabin fg@1.0 | push 0.03 | L3 | L004 (~25%) | rain, engine | **bad** — “People liked them because nothing bad ever happened at the end.” | parallax still |
| S010 | 2.0 | WS | BG04C | Town-line sign in the headlights: WRENFIELD. POP. 412. | BG04_bg bg@0.0, BG04C_far far@0.3, BG04_mid_sign mid@0.6, BG04_fx_rain fx@0.95 | push 0.04 | L3 | — (visual only) | engine slows, rain | — | parallax still |
| S011 | 5.0 | insert | BG04C | Hand-painted board below the sign: VISITORS — PLEASE LEARN TO BE QUIET. | BG04_bg bg@0.0, BG04_near_board near@0.7, BG04_fx_rain fx@0.95 | push 0.05 | L3 | L005 | rain; a single wiper pass | **sign** — “Wrenfield's habit was already on the sign. That's rare.” | parallax still |
| S012 | 5.5 | MS | BG02B | Motel office desk. Bell with tape over the clapper. The older owner slides a key across. | BG02_bg bg@0.0, BG02B_mid_desk mid@0.5, BG02B_near_owner near@0.8 | drift 0.02 | L1 | L006 (~50%) | desk-lamp buzz, key on wood | **explain** — “The motel owner didn't explain it.” | parallax still |
| S013 | 6.0 | insert | BG02B | His finger taps a laminated card twice: QUIET HOUR 1–2 A.M. THANK YOU FOR YOUR COOPERATION. | BG02_bg bg@0.0, BG02B_mid_card mid@0.6, BG02B_near_finger near@0.9 | push 0.04 | L1 | L006 (~50%) | two taps on laminate (sync to 'tapped the card twice') | **talked** — “It was nine in the evening. He could have talked.” | parallax still |
| S014 | 7.0 | WS | BG06C | Gas-station forecourt at the end of main street under one flickering tube light. | BG06_bg bg@0.0, BG06_far far@0.3, BG06C_mid_forecourt mid@0.6, BG06C_fx_tube fx@0.8 | pan_right 0.03 · flicker | L3 | L007 (~50%) | tube-light buzz and tick, pump hum | **relaxed** — “The kid at the gas station was more relaxed about it.” | parallax still |
| S015 | 7.5 | MS | BG02C | The attendant (twenties) at the till. Sign above: WE CLOSE OUR MOUTHS AT ONE. THANK YOU. | BG02_bg bg@0.0, BG02C_mid_till mid@0.5, BG02C_near_attendant near@0.8 | drift 0.02 · flicker | L3 | L007 (~50%) | tube buzz | **didn't** — “Then I asked what happened to people who didn't.” | parallax still |
| S016 | 10.5 | CU | BG02C | His smile stays exactly where it is. He counts out Cal's change very slowly. | BG02_bg bg@0.0, BG02C_mid_tray mid@0.6, BG02C_near_hands near@0.9 | push 0.05 · flicker | L3 | L008 | coins, one by one, too slow; tube buzz | **long** — “You're not staying long, are you?” | **HERO H05** |
| S017 | 5.5 | WS | BG06A | Main street at night: everything shut except one diner, its windows the only warm light. | BG06_bg bg@0.0, BG06_far far@0.3, BG06A_mid_lantern mid@0.6, BG06_fx_dust fx@0.9 | push 0.03 | L1 | L009 (~55%) | distant dog, wind, neon hum | **Lantern** — “The only place open after midnight was a diner called the Lantern.” | parallax still |
| S018 | 5.0 | MS | BG01B | Ines behind the counter: fifties, steady eyes, notepad on a string around her neck. | BG01_bg bg@0.0, BG01_far far@0.25, BG01B_mid mid@0.55, BG01B_near_ines near@0.85 | push 0.03 | L1 | L009 (~45%) | jukebox, cutlery | **Ever** — “She didn't speak at all. Not just during the hour. Ever.” | parallax still |
| S019 | 4.5 | CU | BG01B | Ines writes and turns the pad to camera: COFFEE? | BG01_bg bg@0.0, BG01B_near_ines_cu near@0.7, BG01_fg_pad fg@1.0 | static | L1 | L010 (~60%) | pencil scratch, pad flip | **pad** — “She wrote everything on a little pad she wore around her neck.” | **HERO H03** |
| S020 | 4.5 | insert | BG01B | Notepad: HABIT. | BG01_bg bg@0.0, BG01_fg_pad fg@1.0 | push 0.03 | L1 | L010 (~40%) | pencil scratch | **word** — “When I asked why the town went silent, she wrote one word.” | **HERO H03** |
| S021 | 11.5 | CU | BG02A | Her hands tear the page off, fold it in half, put it in her apron pocket. | BG02_bg bg@0.0, BG02A_mid_counter mid@0.5, BG02A_near_hands near@0.9 | static | L1 | L011 | paper tear, fold | **lying** — “Like it was something that shouldn't be left lying around.” | **HERO H04** |
| S022 | 4.0 | insert | BG02A | Cal's recorder on the counter, red light on; green level bar jumping with the jukebox. | BG02_bg bg@0.0, BG02A_mid_recorder mid@0.6, BG02A_fx_led fx@0.8 | push 0.04 | L1 | L012 | jukebox through the recorder (slightly compressed) | **hear** — “I stayed until one. I wanted to hear it for myself.” | parallax still |
| S023 | 3.5 | MS | BG01B | 12:57. A man stops his story halfway and nods; a trucker pays in exact change. | BG01_bg bg@0.0, BG01_far far@0.25, BG01B_mid mid@0.55, BG01B_near_customers near@0.85 | drift 0.02 | L1 | L013 (~50%) | coins on counter, chatter thinning | **ready** — “You could feel the whole room getting ready.” | parallax still |
| S024 | 4.0 | CU | BG01B | Two customers say goodbye to each other. Neither stands up. | BG01_bg bg@0.0, BG01B_near_goodbye near@0.8, BG01_fx_lamps fx@0.9 | push 0.03 | L1 | L013 (~50%) | murmur fading | **goodbye** — “People said goodbye to each other at two minutes to one.” | parallax still |
| S025 | 2.0 | ECU | BG01B | Clock: 1:00. | BG01_bg bg@0.0, BG01_clock_0100 mid@0.6, BG01_fx_lamps fx@0.8 | push 0.05 | L1 | — (visual only) | jukebox cuts with the second hand; clock tick, fridge hum only | — | parallax still |
| S026 | 4.5 | insert | BG02A | Recorder level drops to almost nothing. | BG02_bg bg@0.0, BG02A_mid_recorder mid@0.6, BG02A_fx_led_low fx@0.8 | push 0.04 | L1 | L014 (~45%) | fridge hum, forty people breathing | **quiet** — “How loud a room full of people being quiet is.” | parallax still |
| S027 | 5.0 | WS | BG01C | The whole diner holding still. Breathing loops only (2% chest scale). | BG01_bg bg@0.0, BG01_far far@0.25, BG01C_mid mid@0.55, BG01C_near near@0.85 | push 0.03 | L1 | L014 (~55%) | breath, fridge, clock | **effort** — “It isn't calm. It's effort. Everybody holding something in.” | parallax still |
| S028 | 3.5 | CU | BG01C | Ines looks at Cal, writes slowly, turns the pad: NOT A WORD. PLEASE. | BG01_bg bg@0.0, BG01C_near_ines_cu near@0.7, BG01_fg_pad fg@1.0 | static | L1 | — (visual only) | pencil only | — | **HERO H03** |
| S029 | 4.0 | WS | BG03A | Through the window the tower light blinks. Then again. Steady, like breathing. | BG03_bg bg@0.0, BG03_far_tower far@0.2, BG03A_mid_glass mid@0.6, BG03_fg_frame fg@1.0 | push 0.02 | L4 | — (visual only) | wind; no music | — | **HERO H02** |
| S030 | 6.5 | WS | BG01A | 2:00. Everyone exhales at once; the room goes back to normal. | BG01_bg bg@0.0, BG01_far far@0.25, BG01A_mid mid@0.55, BG01_fx_lamps fx@0.7, BG01A_near_truckers near@0.85 | drift 0.02 | L1 | L015 (~55%) | collective exhale, chatter and jukebox return together | **exhaled** — “At two o'clock, everyone exhaled at once.” | parallax still |
| S031 | 5.5 | MS | BG01A | Cal at the counter, recorder in hand, not saying a word. | BG01_bg bg@0.0, BG01A_mid mid@0.55, BG01A_near_cal near@0.85 | push 0.03 | L1 | L015 (~45%) | room tone | **word** — “I didn't say a word that first night.” | parallax still |

### Act II

| Shot | Dur (s) | Framing | BG | Description | Layers (kind@depth) | Move | Light | VO | SFX | Caption key | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S032 | 5.0 | WS | BG05A | Motel room: cheap lamp, laptop, Cal in headphones playing back the night. | BG05_bg bg@0.0, BG05A_mid mid@0.5, BG05A_near_cal near@0.8, BG05_fx_screen fx@0.9 | push 0.03 | L4 | L016 (~50%) | motel AC rattle; headphone bleed of diner chatter | **recording** — “Back at the motel I went through the recording.” | parallax still |
| S033 | 4.5 | insert | BG05S | Laptop screen: busy waveform, then flat at 1:00. | BG05_bg_blur bg@0.0, BG05S_mid_waveform_flat mid@0.6 | pan_left 0.04 | L2 | L016 (~50%) | playback: chatter, cups, jukebox, then nothing | **nothing** — “One o'clock: nothing. Just the fridge and forty people breathing.” | parallax still |
| S034 | 4.0 | ECU | BG05S | Flat line. At 1:37, a tiny blip. | BG05_bg_blur bg@0.0, BG05S_mid_waveform_blip mid@0.6 | push 0.06 | L2 | L017 | fridge hum (playback) | **small** — “Except at one thirty-seven. Something very small.” | parallax still |
| S035 | 6.5 | CU | BG05A | Cal's face in screen light as he boosts the gain. | BG05_bg bg@0.0, BG05A_near_cal_cu near@0.8, BG05_fx_screen fx@0.9 | push 0.05 | L2 | L018 | 1.0 s silence first; then a breath and a mouth shape (ECHO processing) | **…ffee…** — “…ffee…” | parallax still |
| S036 | 7.5 | MS | BG05A | Cal very still, staring at the screen. | BG05_bg bg@0.0, BG05A_mid mid@0.5, BG05A_near_cal near@0.8 | static | L2 | L019 | AC rattle | **coffee** — “It sounded like someone practising the word coffee.” | parallax still |
| S037 | 5.0 | WS | BG06B | Day. Main street bright and friendly; people talk, laugh, wave; a kid rings a bike bell. | BG06_bg_day bg@0.0, BG06_far far@0.3, BG06B_mid mid@0.6, BG06B_near_kid near@0.9 | pan_right 0.03 | DAY* | L020 (~50%) | bike bell, birds, overlapping chatter (loud contrast) | **friendliest** — “In daylight, Wrenfield was the friendliest town I've ever been to.” | parallax still |
| S038 | 5.5 | MS | BG06B | Townsfolk talking a little too much, a little too fast. | BG06_bg_day bg@0.0, BG06B_mid mid@0.5, BG06B_near_townsfolk near@0.85 | drift 0.02 | DAY* | L020 (~50%) | chatter | **system** — “As if they were getting it all out of their system.” | parallax still |
| S039 | 5.0 | WS | BG07A | Town library reading room, dust in window light. | BG07_bg bg@0.0, BG07A_mid mid@0.5, BG07_fx_dust fx@0.9 | push 0.03 | DAY* | L021 (~45%) | clock, page turn | **tapes** — “The library kept tapes. Interviews with visitors.” | parallax still |
| S040 | 6.0 | insert | BG07B | A drawer of cassette tapes labelled by year: 1974, 1981, 1996, 2009. | BG07_bg bg@0.0, BG07B_mid_drawer mid@0.6 | pan_left 0.03 | DAY* | L021 (~55%) | drawer slide, cassettes clack | **stranger** — “A stranger who'd come to ask about the quiet hour.” | parallax still |
| S041 | 6.0 | MS | BG07C | Listening booth. Tape 1974 in the deck. A nervous man laughing on tape. | BG07_bg bg@0.0, BG07C_mid_booth mid@0.5, BG07C_near_cal near@0.85 | push 0.03 | L1 | L022 | tape hiss, deck clunk | **Hello** — “So what happens if I talk? Hello? Hello?” | parallax still |
| S042 | 5.0 | CU | BG07C | Cassette reels turning in the deck. | BG07_bg bg@0.0, BG07C_mid_deck mid@0.7 | push 0.04 | L1 | L023 (~50%) | tape hiss | **talked** — “Each tape ended the same way. The visitor talked during the hour.” | parallax still |
| S043 | 5.5 | MS | BG07C | Cal listening, headphones pressed to his ears. | BG07_bg bg@0.0, BG07C_mid_booth mid@0.5, BG07C_near_cal near@0.85 | drift 0.02 | L1 | L023 (~50%) | tape hiss | **silence** — “Afterwards, the historian went outside and recorded the silence.” | parallax still |
| S044 | 3.0 | insert | BG07C | Tape label 1981 in the deck. Wind on the tape. | BG07_bg bg@0.0, BG07C_mid_tape1981 mid@0.7 | push 0.04 | L1 | L024 | outdoor wind on tape, then the voice | **…hello…** — “…hello…” | parallax still |
| S045 | 3.5 | insert | BG07C | Tape label 1996. | BG07_bg bg@0.0, BG07C_mid_tape1996 mid@0.7 | push 0.04 | L1 | L025 | tape hiss, wind | **happens** — “…what happens if I…” | parallax still |
| S046 | 4.0 | insert | BG07C | Tape label 2009. Clearer, nearly a sentence. | BG07_bg bg@0.0, BG07C_mid_tape2009 mid@0.7 | push 0.05 | L1 | L026 | less hiss each year | **anybody…** — “…is anybody… out there…” | parallax still |
| S047 | 6.0 | CU | BG07C | Cal takes the headphones off slowly. | BG07_bg bg@0.0, BG07C_near_cal_cu near@0.8 | push 0.04 | L1 | L027 (~50%) | room tone | **keeping** — “It wasn't just repeating them. It was keeping them.” | parallax still |
| S048 | 6.0 | WS | BG07B | The drawer of tapes, rows of years. | BG07_bg bg@0.0, BG07B_mid_drawer mid@0.6, BG07_fx_dust fx@0.9 | push 0.04 | DAY* | L027 (~50%) | low room tone | **teaching** — “Fifty years of tourists, teaching it one sentence at a time.” | parallax still |
| S049 | 6.5 | WS | BG08A | Afternoon porch on Fenner Street. An old woman shelling peas eyes Cal's recorder. | BG08_bg bg@0.0, BG08A_mid_porch mid@0.5, BG08A_near_woman near@0.8 | drift 0.02 | DAY* | L028 (~50%) | peas into a bowl, screen door, wind chime | **record** — “I tried to get someone to say it on the record.” | parallax still |
| S050 | 7.0 | MS | BG08A | Cal clicks the recorder off and shows her. She leans in close. | BG08_bg bg@0.0, BG08A_mid_porch mid@0.5, BG08A_near_both near@0.85 | push 0.03 | DAY* | L028 (~50%) | recorder click | **recorder** — “As long as I turned off the recorder first.” | parallax still |
| S051 | 5.5 | CU | BG08A | Her face, close, lowering her voice. | BG08_bg bg@0.0, BG08A_near_woman_cu near@0.8 | push 0.03 | DAY* | L029 (~35%) | wind chime fades | **radio** — “The town still had a night-time radio show.” | parallax still |
| S052 | 6.0 | WS | BG09A | Flashback (faded colour): tiny radio booth, a man reading the news (silhouette). | BG09_bg bg@0.0, BG09A_mid_man mid@0.6, BG09_fx_grain fx@1.0 | drift 0.02 | L1 | L029 (~40%) | old AM hiss, faint weather report bed (original, no voice) | **news** — “Requests, weather, a man reading the news.” | parallax still |
| S053 | 4.5 | MS | BG09B | Flashback: the chair empty, microphone ON light still lit. | BG09_bg bg@0.0, BG09B_mid_empty mid@0.6, BG09B_fx_onair fx@0.8, BG09_fx_grain fx@1.0 | push 0.04 · flicker | L1 | L029 (~25%) | AM hiss continues | **home** — “The station kept broadcasting after the man went home.” | parallax still |
| S054 | 7.0 | CU | BG09C | Flashback: mic close; through the frosted window the tower light blinks. | BG09_bg bg@0.0, BG03_far_tower far@0.2, BG09C_mid_mic mid@0.7, BG09_fx_grain fx@1.0 | push 0.04 · flicker | L1 | L030 (~45%) | hiss with fragments of syllables (no words) | **talking** — “Nobody was in the booth. But something kept talking.” | parallax still |
| S055 | 9.0 | WS | BG03C | Flashback: the tower on the hill in spring; the transmitter hut gutted. | BG03C_bg_spring bg@0.0, BG03_far_tower far@0.3, BG09_fx_grain fx@1.0 | push 0.03 | DAY* | L030 (~55%) | birds, wind; AM hiss cuts out | **transmitter** — “They tore the transmitter out in the spring. The tower's still there.” | parallax still |
| S056 | 9.0 | CU | BG08B | Back on the porch: she splits a pea pod with her thumbnail. | BG08_bg bg@0.0, BG08B_near_hands near@0.8 | static | DAY* | L031 | pod snap (crisp, close) | **always** — “Honey, it's always been out there.” | parallax still |
| S057 | 6.5 | MS | BG06A | Cal in his parked car on main street, recorder in his lap, lit by the dashboard. | BG06_bg bg@0.0, BG06A_mid_lantern mid@0.4, BG04B_mid_cal_parked near@0.8, BG04B_fg_cabin fg@1.0 | drift 0.02 | L3 | L032 (~50%) | engine ticking as it cools | **left** — “I should have left then. But I'm a podcaster.” | parallax still |
| S058 | 7.0 | CU | BG06A | Cal's face, decided. | BG06_bg bg@0.0, BG04B_near_cal_cu near@0.8, BG04B_fg_cabin fg@1.0 | push 0.04 | L3 | L032 (~50%) | engine tick | **story** — “I had the best story of my life sitting in a drawer.” | parallax still |

### Act II · second night

| Shot | Dur (s) | Framing | BG | Description | Layers (kind@depth) | Move | Light | VO | SFX | Caption key | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S059 | 4.0 | MS | BG01B | 12:58. Ines sees Cal's recorder and shakes her head: a small, frightened no. | BG01_bg bg@0.0, BG01_far far@0.25, BG01B_mid mid@0.55, BG01B_near_ines_no near@0.85 | push 0.03 | L1 | L033 | chatter thinning, clock | **talked** — “The second night, I talked.” | parallax still |
| S060 | 1.5 | ECU | BG01C | Clock: 1:00 (re-use). | BG01_bg bg@0.0, BG01_clock_0100 mid@0.6, BG01_fx_lamps fx@0.8 | push 0.05 | L1 | — (visual only) | all sound cuts; fridge, clock | — | parallax still |
| S061 | 5.0 | CU | BG02A | Cal leans close to his recorder and speaks. | BG02_bg bg@0.0, BG02A_mid_recorder mid@0.6, BG02A_near_cal_cu near@0.9 | push 0.05 | L1 | L034 | Cal's voice dry and close, no reverb (it must feel too loud) | **something** — “It's one o'clock in Wrenfield, and I'm going to say something.” | parallax still |
| S062 | 2.5 | WS | BG01C | Every head in the diner turns. Nobody speaks. | BG01_bg bg@0.0, BG01_far far@0.25, BG01C_mid_turn mid@0.55, BG01C_near_turn near@0.85 | static | L1 | — (visual only) | chairs creak in unison; nothing else | — | **HERO H06** |
| S063 | 2.0 | MS | BG01C | A woman covers her child's ears. | BG01_bg bg@0.0, BG01C_near_mother near@0.8 | push 0.03 | L1 | — (visual only) | fridge hum | — | parallax still |
| S064 | 7.0 | CU | BG03B | Outside the glass, a faint fog of breath appears, as if someone stands very close. | BG03_bg bg@0.0, BG03_far_tower far@0.2, BG03A_mid_glass mid@0.6, BG03B_fx_fog fx@0.8, BG03_fg_frame fg@1.0 | push 0.04 | L4 | L035 | 1.0 s total silence, then ECHO (Cal, flat, late, through glass) | **one** — “…it's one o'clock… in…” | **HERO H07** |
| S065 | 3.5 | CU | BG01C | Cal frozen. Behind him, the fog on the glass slowly fades. | BG01_bg bg@0.0, BG03B_fx_fog far@0.3, BG01C_near_cal_cu near@0.85 | push 0.03 | L1 | L036 (~45%) | his breathing | **voice** — “It used my voice. Not well.” | parallax still |
| S066 | 5.0 | insert | BG01C | Ines writes, hands shaking, doesn't turn the pad. She closes her eyes. | BG01_bg bg@0.0, BG01C_near_ines_eyes near@0.7, BG01_fg_pad fg@1.0 | static | L1 | L036 (~55%) | pencil shaking | **coat** — “Like someone wearing a coat that doesn't fit yet.” | parallax still |
| S067 | 7.5 | WS | BG01D | 2:00. Money left on tables, food unfinished; people leave without a word. | BG01_bg bg@0.0, BG01_far far@0.25, BG01D_mid mid@0.55, BG01D_near_leaving near@0.85 | drift 0.02 | L1 | L037 (~40%) | coats, door bell, nobody talks | **left** — “At two o'clock, nobody said goodbye. They just left.” | parallax still |
| S068 | 4.5 | MS | BG01D | Ines locks the door behind the last of them. | BG01_bg bg@0.0, BG01D_mid mid@0.55, BG01D_near_ines_door near@0.85 | push 0.03 | L1 | L037 (~25%) | lock turning | **locked** — “Ines locked the door behind the last of them.” | parallax still |
| S069 | 7.0 | MS | BG01D | She points: at Cal, at the door, at the road out of town. | BG01_bg bg@0.0, BG01D_mid mid@0.55, BG01D_near_ines_point near@0.85 | static | L1 | L037 (~35%) | fridge hum | **clearest** — “It was the clearest sentence anyone said to me in Wrenfield.” | parallax still |

### Act III

| Shot | Dur (s) | Framing | BG | Description | Layers (kind@depth) | Move | Light | VO | SFX | Caption key | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S070 | 8.5 | WS | BG05B | Night three. Every light on. Notes, dates, a hand-drawn timeline all over the bed. Cal hasn't slept. | BG05_bg bg@0.0, BG05B_mid_notes mid@0.5, BG05B_near_cal near@0.85 | push 0.03 | L1 | L038 | AC rattle, lamp buzz | **light** — “I stayed in my room with every light on.” | parallax still |
| S071 | 2.0 | insert | BG05C | Bedside clock: 1:12. | BG05C_bg_bedside bg@0.0, BG05C_mid_clock mid@0.6 | push 0.04 | L1 | — (visual only) | clock flip | — | parallax still |
| S072 | 7.0 | MS | BG05B | Cal turns toward the wall. Through it, faint and conversational, his own voice. | BG05_bg bg@0.0, BG05B_mid_wall mid@0.5, BG05B_near_cal_turn near@0.85 | push 0.05 | L1 | L039 | ECHO muffled through drywall (low-pass) | **podcast** — “…I make a podcast about small towns… with strange habits…” | parallax still |
| S073 | 6.0 | CU | BG05B | Cal's face: recognition. | BG05_bg bg@0.0, BG05B_near_cal_cu near@0.85 | push 0.04 | L1 | L040 (~50%) | room tone | **intro** — “That was my intro. Word for word.” | parallax still |
| S074 | 5.5 | MS | BG05B | Cal on the bed among the notes, hugging his knees. | BG05_bg bg@0.0, BG05B_mid_notes mid@0.5, BG05B_near_cal near@0.85 | drift 0.02 | L1 | L040 (~50%) | room tone | **myself** — “In the car. In the motel. Every time I talked to myself.” | parallax still |
| S075 | 4.0 | insert | BG05C | 1:24. Phone buzzes on the bed. Caller ID: HOME. It rings out. | BG05C_bg_bedside bg@0.0, BG05C_mid_phone_home mid@0.6, BG05_fx_screen fx@0.8 | push 0.04 | L2 | — (visual only) | vibration on the mattress x3, then stop | — | **HERO H08** |
| S076 | 6.0 | insert | BG05C | A voicemail notification. He doesn't touch it. It plays on speaker by itself. | BG05C_bg_bedside bg@0.0, BG05C_mid_phone_vm mid@0.6, BG05_fx_screen fx@0.8 | push 0.05 | L2 | L041 | phone-speaker EQ on ECHO (almost natural) | **town** — “Pick up. I want to tell you about the town.” | **HERO H08** |
| S077 | 9.5 | CU | BG05B | Cal staring at the phone. | BG05_bg bg@0.0, BG05B_near_cal_cu near@0.85, BG05_fx_screen fx@0.9 | push 0.03 | L2 | L042 | room tone | **home** — “The only person who calls me from home is me.” | parallax still |
| S078 | 8.0 | insert | BG05S | Laptop: podcast dashboard. A draft he never made: WRENFIELD — Part 1. Length 41 minutes. | BG05_bg_blur bg@0.0, BG05S_mid_dashboard mid@0.6 | push 0.05 | L2 | L043 | laptop fan; trackpad click | **talking** — “The one place where a voice can go on talking.” | parallax still |
| S079 | 1.5 | WS | BG01E | Morning at the Lantern. Ines writes fast, for the first time. | BG01_bg_day bg@0.0, BG01_far far@0.25, BG01E_mid mid@0.55, BG01E_near_ines near@0.85 | push 0.03 | DAY* | — (visual only) | pencil racing, coffee machine | — | parallax still |
| S080 | 3.0 | insert | BG02A | Notepad page torn off and handed to Cal: IT CAN'T FINISH IF WE DON'T TEACH IT. | BG02_bg_day bg@0.0, BG02A_mid_counter mid@0.5, BG01_fg_pad fg@1.0 | push 0.02 | DAY* | — (visual only) | page tear; page slides across the counter | — | **HERO H09** |
| S081 | 2.5 | insert | BG02A | Notepad page torn off and handed to Cal: EVERY VISITOR GAVE IT WORDS. | BG02_bg_day bg@0.0, BG02A_mid_counter mid@0.5, BG01_fg_pad fg@1.0 | push 0.02 | DAY* | — (visual only) | page tear; page slides across the counter | — | **HERO H09** |
| S082 | 2.5 | insert | BG02A | Notepad page torn off and handed to Cal: YOU GAVE IT MORE THAN ANYONE. | BG02_bg_day bg@0.0, BG02A_mid_counter mid@0.5, BG01_fg_pad fg@1.0 | push 0.02 | DAY* | — (visual only) | page tear; page slides across the counter | — | **HERO H09** |
| S083 | 3.0 | insert | BG02A | Notepad page torn off and handed to Cal: IT ONLY NEEDS THE LAST ONES. | BG02_bg_day bg@0.0, BG02A_mid_counter mid@0.5, BG01_fg_pad fg@1.0 | push 0.02 | DAY* | — (visual only) | page tear; page slides across the counter | — | **HERO H09** |
| S084 | 6.0 | MS | BG01E | Ines looks at the radio behind the counter. | BG01_bg_day bg@0.0, BG01E_mid mid@0.55, BG01E_near_ines_look near@0.85 | push 0.03 | DAY* | L044 (~50%) | room tone drops out | **finishes** — “I asked her what happens when it finishes.” | parallax still |
| S085 | 6.5 | CU | BG02A | The old radio behind the counter, dial dark. | BG02_bg_day bg@0.0, BG02A_mid_radio mid@0.7 | push 0.05 | DAY* | L044 (~50%) | faint electrical hum from the radio (no signal) | **door** — “The way you look at a door you're not allowed to open.” | parallax still |
| S086 | 9.0 | WS | BG01E | Cal and Ines small in the wide frame, the radio between them. | BG01_bg_day bg@0.0, BG01_far far@0.25, BG01E_mid mid@0.55, BG01E_near_both near@0.85 | drift 0.02 | DAY* | L045 | room tone | **wall** — “The silence was never a superstition. It was a wall.” | parallax still |
| S087 | 5.0 | MS | BG06D | At his car: Cal puts the recorder in the glovebox and locks it. | BG06_bg_day bg@0.0, BG06D_mid_car mid@0.5, BG04B_fg_cabin fg@1.0 | push 0.03 | DAY* | L046 (~35%) | glovebox click, key | **leave** — “So I decided to leave without saying another word.” | parallax still |
| S088 | 5.5 | insert | BG05S | Laptop: he deletes the draft. 'Are you sure?' He clicks yes. | BG05_bg_blur bg@0.0, BG05S_mid_delete mid@0.6 | static | L2 | L046 (~35%) | trackpad click | **deleted** — “I deleted the episode. I'd make something else.” | parallax still |
| S089 | 4.5 | CU | BG06D | Cal behind the wheel, jaw set. | BG06_bg_day bg@0.0, BG04B_near_cal_cu near@0.8, BG04B_fg_cabin fg@1.0 | push 0.03 | DAY* | L046 (~30%) | engine starts | **nothing** — “Something where nothing bad happens at the end.” | parallax still |
| S090 | 3.5 | WS | BG04D | The town line at 12:55 a.m. The sign. The car's tail lights shrink into the dark. | BG04_bg bg@0.0, BG04D_far far@0.3, BG04_mid_sign mid@0.6, BG04D_fx_taillights fx@0.8 | static | L3 | — (visual only) | engine recedes to nothing | — | **HERO H10** |
| S091 | 4.0 | WS | BG03D | Held silence, four seconds. On the hill, the tower light blinks. | BG03D_bg_night bg@0.0, BG03_far_tower far@0.3 | static | L4 | — (visual only) | NOTHING. True digital silence for 4.0 s (QC: confirm intentional) | — | **HERO H02** |

### Ending

| Shot | Dur (s) | Framing | BG | Description | Layers (kind@depth) | Move | Light | VO | SFX | Caption key | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S092 | 2.0 | WS | BG10A | Ines's flat above the diner, 1:30 a.m. She sits in the dark beside a small radio. | BG10_bg bg@0.0, BG10A_mid mid@0.5, BG10A_near_ines near@0.85 | push 0.02 | L4 | — (visual only) | radio crackle builds | — | parallax still · no watermark |
| S093 | 5.5 | CU | BG10A | The radio dial glows. A podcast intro: Cal's voice, fluent, perfect. | BG10_bg bg@0.0, BG10A_mid_radio mid@0.7, BG10_fx_dial fx@0.9 | push 0.04 | L4 | L047 (~45%) | ECHO as Cal: full-range, warm, NO processing (it has learned) | **podcast** — “I make a podcast about small towns with strange habits.” | **HERO H11** · no watermark |
| S094 | 2.5 | MS | BG10A | Ines listening, her face lit only by the dial; Lamp highlight in her eyes. | BG10_bg bg@0.0, BG10A_near_ines_lit near@0.85, BG10_fx_dial fx@0.9 | push 0.03 | L4 | L047 (~25%) | radio | **here** — “This week: a town called Wrenfield. I'm here now.” | parallax still · no watermark |
| S095 | 4.0 | CU | BG10A | Ines reaches for the dial. Her hand stops. | BG10_bg bg@0.0, BG10A_mid_radio mid@0.7, BG10A_near_hand near@0.9, BG10_fx_dial fx@0.95 | static | L4 | L047 (~30%) | radio; the same voice, very faintly, from the hallway (offset 0.3 s) | **talk** — “And I'm going to talk for as long as you'll let me.” | **HERO H11** · no watermark |
| S096 | 3.0 | MS | BG10B | Hold on the door. Warm light under it, from the hallway: the wrong direction. | BG10_bg bg@0.0, BG10B_mid_door mid@0.6, BG10B_fx_underdoor fx@0.8 | push 0.03 | L5 | — (visual only) | hallway voice continues, unintelligible | — | parallax still · no watermark |
| S097 | 4.0 | CU | BG10C | A moth lands on the window behind her, lit by the radio dial. | BG10C_bg_window bg@0.0, BG10C_mid_glass mid@0.5, BG10C_near_moth near@0.8, BG10_fx_dial fx@0.9 | push 0.03 | L4 | — (visual only) | a single soft wing flutter (motif: something is noticing you) | — | **HERO H12** · no watermark |
| S098 | 1.5 | black | - | Cut to black. Then brand outro (exports.outro) and the YouTube end screen. | BLACK bg@0.0 | static | n/a | — (visual only) | voice cuts with the picture | — | parallax still · no watermark |

## Issues and script notes (for Storywriter / Creative Director; this file does not change the script)

1. **Hook timing vs Video Branding Guide.** The guide wants the hook line within 1.5 s. The script opens on a clock and a busy diner before the 1:00 cut, so L001 starts at ≈ 4.5 s + 1.5 s pad (≈ 6 s). Storyboard compresses the pre-roll to 4.5 s; going lower kills the 'sound stops' gag. Decide: accept ≈ 6 s, or put a 1-line hook caption/ECHO whisper over S001.
2. **Title card length.** Script reserves 0:30–0:36 (6 s); the branding guide caps title cards at 2–3 s. Storyboard uses 3.0 s.
3. **Runtime is short of the ~9.5 min target.** The recorded narration measures 394 s (≈ 166 wpm incl. pauses; the plan assumed 145 wpm ≈ 487 s). With every visual beat in the script the picture is ≈ 8:21 (+3.2 s outro + end screen ≈ 8:40–8:50 delivered). Reaching 9:30 would need ≈ 69 s more: options are (a) re-time the processed VO with small inter-sentence gaps (free, ffmpeg, Voice and Sound agent), (b) longer visual holds in the quiet-hour sequences (risk: drag), (c) a script addition (Storywriter). Padding was **not** added here. The script's section timecodes (Act I to 3:50, Ending at 10:00) are also optimistic: Act I now ends ≈ 2:40.
4. **Shot timing inside long narration files is estimated.** N02_act1 (112.5 s) and N03_act2 (123.9 s) are single files; shot cuts were placed by word share. Before assembly, re-time cuts to real line onsets (e.g. silence detection on the processed WAVs).
5. **Act II is the longest stretch (≈ 3.4 min incl. the second night; 156 s before the second night) and is mostly exposition** (library tapes + porch + radio flashback with no threat on screen). Retention risk in the 3:30–5:15 window. Option: trim L029/L030 (radio backstory) by a sentence each, or move one tape (1996) out.
6. **'I want that on the record' (L015) is unclear in a cut.** It reads as a podcast aside; fine, but it is the only line that addresses an audience inside the story before the twist. Keep it consistent with the ending reveal (good set-up) — just confirm it is intentional.
7. **Act III notepad scene has no narration for ≈ 12.5 s** (four pages, S080–S083). Pages must be readable (≈ 2.5–3 s each); this is deliberate, but it is the longest visual-only stretch after the cold open. Confirm it is wanted, or let NARR read one page.
8. **Geography gap:** 'the radio behind the counter' (L044) is first seen in Act III. It should be planted earlier: storyboard dresses it into BG02A from Act I (S022/S026 background) so the ending pays off.
9. **Ines's flat (Ending)** has no set-up line; the audience must infer 'above the diner'. Suggest an establishing exterior beat (re-use BG06A with a lit upstairs window) if a 2–3 s shot can be afforded.
10. **The tower light is never explained in Act I** (blinks in S005/S029) and the radio-station backstory lands in Act II. Good mystery set-up; no change, noted for QC so the blinks are not removed as 'decoration'.
11. **Held 4 s silence (S091) and the 1:00 hard cuts** are true silence. QC tools that flag dropouts must whitelist these timestamps.
12. **Day scenes have no Environment Bible lighting preset** (main street day, library, porch, diner morning; marked DAY*). Environment Bible owner should add one (suggest: overcast Bone key, Ash-Violet shadow, lowered saturation) so the town is 'friendly but wrong'.
13. **Assembler gaps (scripts/production/assemble.py):** (a) no video layers, so hero clips cannot be placed yet; each hero shot carries a still-layer fallback. (b) `static` is not a named move; it works because unknown moves fall through to no motion. (c) Caption key matching strips only `.,!?`, so keys next to '…' or apostrophes must be written exactly (e.g. key `…ffee…`). (d) The YouTube end screen (10–20 s) must follow the outro; the assembler appends the outro last, so the end-screen plate needs a separate step.
14. **No `episodes/EP001/manifest.json` exists yet**, so the shots could not be written into the manifest or `pipeline.storyboard.status` set; they are in `shots_draft.json` for the owner of the manifest to merge.
15. **Character sheets for Cal, Ines, the motel owner, the attendant and the old woman do not exist yet** (CHARACTER_BIBLE requires approved sheets before any Flow generation). Hero clips H03–H06, H08, H09, H11 are blocked on them.
16. **Originality:** storyboard keeps the radio station to three short flashback shots (S052–S054) and no DJ character, as the script notes require (distance from *Pontypool*).
