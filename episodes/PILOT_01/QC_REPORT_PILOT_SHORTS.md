# PILOT_01: QC report for assembled Shorts (2026-11-20)

Masters are built with `scripts/production/assemble_flow_short.py` (edit lists in `episodes/PILOT_01/edits/`) and finished with `scripts/production/fix_loudness.py`. Earlier versions are kept; nothing was overwritten.

| Short | File | Length | Automated verdict | Loudness / TP | Human review |
|---|---|---|---|---|---|
| SH012 Rain Sounds | `masters/SH012_RainSounds_master_v3.mp4` | 28.3 s | **PASS WITH WARNINGS** | −14.4 LUFS / −2.3 dBTP | **Pending: owner** |
| SH019 Theo's Nightlight Rules | `masters/SH019_NightlightRules_master_v3.mp4` | 32.6 s | **PASS WITH WARNINGS** | −14.3 LUFS / −2.7 dBTP | **Pending: owner** |

## Version history
- **v1:** first assembly. The captions were too small, and SH019 C2c showed **generated wall-poster text "MOTHWAKE"** (unwanted text).
- **v2:** captions enlarged to 80 px; a punch-in crop (1.45×) on SH019 C2c removes the poster text (verified on a frame at 9.2 s). Automated QC: **NEEDS REVISION**, true peak 0.0 / −0.2 dBFS.
- **v3:** two-pass loudness + oversampled limiter. Picture stream-copied from v2. Automated QC: PASS WITH WARNINGS.

## Warnings explained (automated, to be confirmed by eye)
- "Frozen ≥1 s": SH012 at 0.4 s (Ivy asleep, locked-off camera), 7.6 s and 8.8 s (C2a: **rain freezing on the glass is the story beat**); SH019 at 3.3 s, 8.3 s, 17.5 s (Theo counting, the nightlight, the switch). These are slow, locked-off shots; check they don't read as stalls.
- Low-threshold cut candidates (1 and 3): flicker and light changes inside shots; check continuity.

## Known content issues (NOT fixed; owner decision)
1. **SH012 C5 (key moment):** the tall figure reads as **inside the room** rather than outside the glass. The v2 regeneration was submitted but never generated (no credits charged). Options: regenerate (Veo Fast 20 credits), or keep it (arguably scarier, but it changes the "outside your window" line).
2. **SH019 Theo has no voice yet:** his four rule lines are on-screen **whisper captions** (lamp-yellow italic) with no audio, pending Theo's voice design (ElevenLabs Voice Design, owner approval).
3. SH019 C5: the Tenants show small lamp-light eyes. That's allowed by the Asset Kit ("Lamp eyes only at the reveal").
4. Audio bed = the Flow clips' own generated room tone at −20 dB (−14 dB under SH012 C5). No music or designed SFX yet (tapping, flicker buzz).
5. Watermark: approved `brand/kit/watermark_gold.png`, top-left, 55% opacity. The mobile end sting (a proposal still awaiting approval) is not used; both Shorts end on a loop frame.

## Not produced
SH025 *Which Door Is Really Mine?* Part 1. The narration exists, but its 4 Flow clips (about 40 credits) have not been generated.

## Update: owner asked "Fix C5 and Theo"
- **SH012 C5 fixed:** regenerated on Veo 3.1 Fast (20 credits shown). The figure now stands **outside** the rain-streaked glass, fingers on the window, moth on the sill. New master **`SH012_RainSounds_master_v5.mp4`**: PASS WITH WARNINGS, −14.5 LUFS / −2.5 dBTP. New frozen-frame flags at 20.7 s and 23.2 s are the figure's slow, still tapping shot (confirm by eye). v4 = pre-loudness render (local only).
- **Theo's voice: BLOCKED.** ElevenLabs Voice Design refused the request ("potentially doesn't follow our safety guidelines"), most likely because it designs a child's voice. Not retried and not reworded. The owner must choose an alternative.
- **Theo's lines: owner chose "Ivy speaks his rules".** New ElevenLabs take (Ana-Rita2, eleven_v4, **272 credits measured**; my 150 estimate was low): "Rule one, he said: it stays on / Rule two… / Rule three… / And then he whispered: now they'll look at you." Whisper captions are kept on screen.
- **`SH019_NightlightRules_master_v7.mp4`** (34.5 s): PASS WITH WARNINGS, −14.3 LUFS / −2.3 dBTP. In v5 the whispered rules sat about 6 dB under the narration (ASR missed them), so v6/v7 raise them by 3–6 dB. Measured mean levels: narration −16.7 to −17.5 dB, rules −17.8 / −20.6 / −18.6 dB (whispered and slightly softer on purpose). **Listen check needed on rule two (7.4–11.6 s).**
- **Current masters for owner review:** `SH012_RainSounds_master_v5.mp4` and `SH019_NightlightRules_master_v7.mp4`.

## SH025 Which Door Is Really Mine? Part 1 (2026-11-20, plan approved)
- 4 Flow Lite clips (40 credits shown). Master **`SH025_WhichDoorP1_master_v2.mp4`** (20.6 s): PASS WITH WARNINGS, −14.7 LUFS / −1.3 dBTP.
- Structure: hook card "TWO DOORS SAY 9." on the two doors (with "9" plates added in post) → bike shot (**fair clue: a pale scuff on the right-hand door at handlebar height from about 3 s**) → "Two doors say nine. Only one is mine." → the glowing lock → the hand hesitating as the timer light flickers → **3-2-1 countdown** → "LEFT or RIGHT? COMMENT. MOST VOTES = PART 2". No reveal in Part 1 (owner fix 1).
- SFX (synthesized): a timer tick that speeds the tension, a low drone, the countdown ticks.
- Notes: C2c Ivy's face leans slightly anime (style drift); the scuff is subtle, and Part 2 will replay and zoom it.
- **All 3 pilots now assembled:** SH012 v7, SH019 v9, SH025 P1 v2.
