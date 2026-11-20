# Phase 2: tool install and test (2026-11-20, owner approved "Approve Phase 2")

**Environment:** `repo/.venv` (Python 3.12.10, MOTHWAKE only, git-ignored). Global Python and Chrono Tales untouched. Lock file: `requirements-lock-windows.txt` (33 packages).
**Installed:** requirements.txt (6 pinned) + faster-whisper 1.2.1 + scenedetect 0.7.3 + opencv-python-headless 5.1.0 (numpy 2.5.5).
**Downloaded on first use:** faster-whisper "tiny" model from Hugging Face (`~/.cache/huggingface`, shared user cache; it holds model files only).

**New tool:** `scripts/production/qc_clip_check.py`. It reports resolution and aspect, scene cuts at 2 thresholds (hidden-cut candidates), black frames, frozen frames, loudness and true peak, and optional speech timing, then gives a verdict. It never edits media.

| Test file | Verdict | Findings | Status |
|---|---|---|---|
| episodes/EP000/exports/EP000_youtube_shorts.mp4 (1080×1920, 41 s) | PASS WITH WARNINGS | 4 frozen ≥1 s stretches (EP000 was built from still layers), 6 low-threshold cut candidates, −14.3 LUFS, TP −1.4 dBFS, no speech (captions-only build) | TESTED |
| episodes/EP001_sample/MOTHWAKE_QuietHour_sample.mp4 (1920×1080, 106 s) | NEEDS REVISION | not 9:16; TP −0.8 dBFS (clipping risk); a black segment at 79.5–80.4 s; frozen at 16.4 and 78.4 s; 19 cut candidates; 26 speech segments transcribed in about 3 min on CPU | TESTED |

**Known limits:**
- whisper "tiny" mishears names ("Wrenfield" became "our end field"). Use `--whisper base` for caption timing and fix names from the script.
- PyAV in faster-whisper had an API mismatch, worked around by decoding with our FFmpeg.
- Automated QC never replaces the human frame review.
