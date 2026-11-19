---
name: ffmpeg-media-processing
description: Encode, trim, loudness-normalise, reframe and inspect media with FFmpeg.
---

# ffmpeg-media-processing

Delivery: H.264 yuv420p, AAC 192k, 30 fps, -14 LUFS / TP ≤ -1 (convention — platforms don't document a target). Measure with `ebur128`; detect black/freeze with `blackdetect`/`freezedetect`. Never overwrite masters.

## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
