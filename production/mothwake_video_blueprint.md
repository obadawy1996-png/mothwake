# MOTHWAKE video production blueprint (15 stages)

Paid tools allowed: **Google Flow, ElevenLabs** only. Status per stage: what exists today in this repo.

| # | Stage | Input | Output | Quality criteria | Tools (free unless marked) | Status |
|---|---|---|---|---|---|---|
| 1 | Topic research | Pillar, season | Research card (topic, keyword, country, source, interest, trend, evidence, gap, date, confidence) | Every number labelled measured/estimated/unknown; EXPERIMENTAL if thin | Repo collectors, Google Trends (web), Semrush connector, YouTube search | IMPLEMENTED (collectors) |
| 2 | Demand and competition check | Research card | Go / Experimental / Drop | ≥2 independent signals for "trending" | `research/*.csv`, competitor DB | IMPLEMENTED |
| 3 | Story concept | Research card | Concept JSON (premise, hook ×5, conflict, twist, ending) | Passes the similarity gate; distinct from the 30-slate | `stories/`, `scripts/story/storydb.py` | IMPLEMENTED |
| 4 | Hook development | Concept | 5 hooks, choose 1 | Wrong image in frame 1; ≤12 words; no 3AM/DON'T | Hook DB in stories.db | IMPLEMENTED |
| 5 | Script | Concept + frame device | Script with timings | ≤45 s Shorts; present tense; captions readable | Story framework doc | PARTIAL |
| 6 | Storyboard | Script | Shot list (one action per clip) | 9:16; ≤3 ingredients per clip; no on-screen text generated | PILOT_01 format | TESTED (PILOT_01) |
| 7 | Character and environment design | Bibles | Approved Flow refs | Owner approval; refs never text-only | Flow Nano Banana (**0 credits**) | TESTED |
| 8 | Visual generation | Shot list + refs | Flow clips | Gate: model/cost/9:16/×1/ingredients checked before Generate; ≤2 tries per clip | **Google Flow (paid)**: Lite 10 / Fast 20 / Omni 24 | TESTED (SH012, SH019) |
| 9 | Voiceover | Script | VO stems | Voice approved; eleven_v4; 1 take, then targeted retakes | **ElevenLabs (paid)** | TESTED (Ivy VO) |
| 10 | Sound design | Script | SFX, room tone, brand sounds | No unlicensed music; −16 LUFS; limiter before AAC | Brand sounds (repo), ElevenLabs SFX (paid), Freesound CC0 only (licence register) | PARTIAL |
| 11 | Editing and assembly | Clips, VO, SFX, type cards | Master 1080×1920 | Hook ≤1 s; captions in the safe area; loop ending | FFmpeg 9, `scripts/production/assemble.py` (Linux-tested, Windows pending) | PARTIAL |
| 12 | QC | Master | QC report: PASS / PASS WITH WARNINGS / NEEDS REVISION / FAILED | Black and frozen frames, clipping, A/V sync, aspect, text, hidden cuts (scene detection at 2 thresholds), **human frame review** | `scripts/production/qc.py`; PySceneDetect + OpenCV (to install in a venv, pending approval) | PARTIAL |
| 13 | Thumbnail and metadata | Master | Cover, titles per platform, hashtags | ≤4 words; no misleading claims | `scripts/brand/thumbnail.py`, Canva connector | IMPLEMENTED |
| 14 | Publishing prep | Approved package | Per-platform packages + manual instructions | Owner approval per post; no auto-publish | YouTube Studio (browser, TESTED for branding); Metricool (needs FB/IG linked) | PARTIAL |
| 15 | Performance analysis | Exports at 48 h / 7 d | Weekly learning report | Real data only; no single-outlier decisions | `analytics/dashboard.html`, `scripts/analytics/analytics.py` | IMPLEMENTED (empty until data) |
