# Sound Identity

All brand sounds are **synthesised from scratch** by `scripts/brand/build_sound.py` (noise, sine and FM). No samples are used, so there is no third-party licence. Files are 48 kHz, 24-bit WAV, normalised with ffmpeg `loudnorm`.

| File | Length | Loudness (measured) | Use |
|---|---|---|---|
| `brand/sound/mothwake_signature.wav` | 1.65 s | −18.0 LUFS, peak −6.4 dBFS | Wing flutter, then a low A (55 Hz) swell with a fifth, then a faint "lamp" ping. Long-form title card only. |
| `brand/sound/mothwake_open_sub.wav` | 0.90 s | −24.0 LUFS | Optional sub-bass breath under a cold open. Felt more than heard. |
| `brand/sound/mothwake_outro.wav` | 3.20 s | −17.3 LUFS, peak −4.3 dBFS | The flutter flies off left to right, a ping, and a low tone settles. Used in the outro clips. |

## Sound design guidelines

- Silence is an instrument. Leave 0.5–1.5 s gaps before reveals.
- Hierarchy: dialogue or narration above key SFX, above ambience, above score. Score ducks 6–9 dB under narration.
- Recurring motifs: the moth flutter means something is noticing you; a high single ping means the "light", the moment of realisation. Use them inside stories sparingly so they stay meaningful.
- Ambiences are room tone, wind, refrigerator hum and distant traffic. Specific and mundane is scarier than generic "horror drones".
- No jump-scare stingers louder than the narration peak +3 dB. No ear-rape spikes.
- Music only from licensed sources, recorded per asset in the episode licence ledger. No copyrighted tracks.
- Target delivery (to be confirmed in `research/PLATFORM_SPECS.md`): about −14 LUFS integrated, true peak −1 dBTP for platforms; keep the master stems at −23 LUFS.

## Narration direction

- **Voice:** an intimate storyteller, mid-low register, close-mic, unhurried but never slow. A friend telling you something they shouldn't.
- **Pace:** about 150–165 wpm in Shorts and 135–150 wpm in long-form. Slow down before a reveal and land the last line flat, without a theatrical whisper.
- **Avoid:** "movie trailer" voice, over-acting, horror-host clichés, laughing.
- **Character voices:** distinct, small cast, consistent per character (recorded in the Character Bible).
- **AI voices:** ElevenLabs voices only on a plan whose terms allow commercial use, with the voice ID logged in the manifest and AI-voice disclosure followed where the platform requires it.
