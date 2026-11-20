# QC report: week 2 (Days 8–13), 2026-11-20

| Day | Short | Final master | Length | Loudness / true peak | Verdict |
|---|---|---|---|---|---|
| 8 | SH005 The Last Prescription | `masters/SH005_LastPrescription_master_v2.mp4` | 31.1 s | −14.1 LUFS / −3.0 dBTP | PASS WITH WARNINGS |
| 9 | SH010 Written From In Here | `masters/SH010_WrittenFromInHere_master_v2.mp4` | 24.2 s | −14.3 LUFS / −2.9 dBTP | PASS WITH WARNINGS |
| 10 | SH026 The Kettle in the Glass | `masters/SH026_KettleInTheGlass_master_v2.mp4` | 24.9 s | −14.2 LUFS / −3.0 dBTP | PASS WITH WARNINGS |
| 11 | SH016 The Sixty-Second Light | `masters/SH016_SixtySecondLight_master_v4.mp4` | 32.0 s | −14.3 LUFS / −2.0 dBTP | PASS WITH WARNINGS |
| 12 | SH001 Dryer Six | `masters/SH001_DryerSix_master_v4.mp4` | 30.2 s | −14.2 LUFS / −2.7 dBTP | PASS WITH WARNINGS |
| 13 | SH009 Still Counting | `masters/SH009_StillCounting_master_v2.mp4` | 29.1 s | −14.4 LUFS / −2.5 dBTP | PASS WITH WARNINGS |

**Warnings explained:** "low-threshold cuts" are the lights flickering (SH016), the breath/fog (SH010, SH005) and the push-ins; "frozen" marks are deliberate still shots (the empty pantry, the end cards). No black frames, all 1080×1920, 30 fps.

**Errors found and fixed (new versions, nothing overwritten):**
1. SH016 v2 true peak −0.5 dBFS (switch click transient) → click/buzz/rattle lowered → v4 −2.0 dBTP.
2. SH001 continuity: Ivy's scarf reappeared in the last second of C3 right after she notices it is gone → C3 trimmed to 7.0 s → v4.
3. Flow: the picker truncates long ref titles ("Elderly woman character turnarou…") → helper now matches by prefix and only inside the picker dialog.
4. Flow: one generate click is enough; progress appears 5–10 s later. Two extra clicks on SH005 C1/C2 cost 20 credits (alternate takes kept: C1b has a floating bag, unused; C2b used for the push-in).

**Claude's frame check (contact sheets at 2 s):** on-model Ivy/Dot/Theo; captions above platform UI; the Watcher moth watermark top-left; SH026 opens on the cold kettle (C1 0–3.4 s only, before it steams); SH009 never shows the child and an adult in one frame; the counting line is Ivy's take pitched down ("the counter").
**Still required:** the owner's own watch of each master before posting.

## Spend (measured where shown)
ElevenLabs 1,925 credits (6 takes). Flow 330 credits shown (310 planned + 20 duplicate). SFX all synthesized (0 credits): bell, bus rumble, dryer hum, kettle rumble, key rattle.
