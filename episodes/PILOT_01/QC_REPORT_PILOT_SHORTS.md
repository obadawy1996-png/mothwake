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
