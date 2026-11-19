# MOTHWAKE — Project Handover

**Date:** 2026-11-19 · **Project:** `/home/user/mothwake` · **Isolation:** verified, 10/10 checks plus 7/7 negative tests
**Idea score:** 66/100 (`reports/PROJECT_IDEA_SCORECARD.md`, including the path to 100)

Labels: **Implemented** · **Tested** · **Partially implemented** · **Planned** · **Blocked**. "Tested" means an automated test ran and passed in this container.

| # | Deliverable | Status | Where / evidence |
|---|---|---|---|
| 1 | Independent MOTHWAKE project | Implemented, Tested | Own venv, `.claude/`, `CLAUDE.md` |
| 2 | Verified isolation report | Implemented, Tested | `ISOLATION_POLICY.md`, `reports/PHASE_1_REPORT.md` |
| 3 | Market research report | Implemented | `research/MARKET_OPPORTUNITY_REPORT.md`, `CONTENT_GAP_ANALYSIS.md`. Reddit and Google Trends were blocked, so they are qualitative only. |
| 4 | Competitor database | Implemented | `research/COMPETITOR_DATABASE.csv`: 63 channels, 62 with measured subscribers. Likes and comments unknown (blocked). |
| 5 | Trend intelligence system | Implemented, Partially | `TREND_DATABASE.csv` (42 rows), `WEEKLY_TREND_REPORT.md`, re-runnable `research/collectors/`. Per-country Trends data is **Blocked** by network policy. |
| 6 | Complete Brand Kit | Implemented, Tested | `brand/` with 8 guides, 53/53 brand tests. **The logo choice (B) is provisional until you approve it.** |
| 7 | Logo files and source files | Implemented, Tested | `brand/logo/` (14 SVG with outlined text, 14 PNG), generator `scripts/brand/build_brand.py` |
| 8 | YouTube profile picture | Implemented, Tested | `brand/kit/youtube_profile_800.png` (circle-crop test) |
| 9 | YouTube banner | Implemented, Tested | `brand/kit/youtube_banner_2560x1440.png`; content inside the strictest safe area; guide overlay in `brand/previews/` |
| 10 | Video watermark | Implemented, Tested | `brand/kit/watermark_{gold,white}.png` (150×150 transparent) |
| 11 | Channel description and About | Implemented | `brand/CHANNEL_COPY.md` (handles **not** checked for availability) |
| 12 | Thumbnail templates | Implemented, Tested | `scripts/brand/thumbnail.py` (4 layouts, enforces 4 words or fewer and under 2 MB), `brand/THUMBNAIL_SYSTEM.md` |
| 13 | Video branding templates | Implemented, Tested | Outro clips 16:9 and 9:16, title card, caption style, end cards, sound identity (loudness tested) |
| 14 | Character Bible | Implemented (framework) | `production/CHARACTER_BIBLE.md`. Per-character sheets are **Planned** for the pilot. |
| 15 | Environment Bible | Implemented (framework) | `production/ENVIRONMENT_BIBLE.md` (lighting, background, pose, expression and animation libraries) |
| 16 | Story Bible | Implemented, Tested | `stories/stories.db` (12 original concepts, 5+ hooks each), `SCORING_MODEL.md`, similarity and hook gates |
| 17 | Production pipeline | Implemented, Tested | `scripts/production/assemble.py`: brand gate, layered parallax, captions, ducked mix, master and exports. EP000 test render: see QC row. |
| 18 | Claude Code skills | Implemented, Tested | 18 in `.claude/skills/`, created without overwriting anything |
| 19 | Specialized agents | Implemented, Tested | 14 in `.claude/agents/`; interfaces tested (55/55 system tests) |
| 20 | Quality-control system | Implemented, Tested | `scripts/production/qc.py`, `scripts/brand_validator.py` (catches tampering) |
| 21 | Analytics dashboard | Implemented, Tested | `analytics/dashboard.html` (empty, "no data", until real exports arrive); cohort analysis |
| 22 | Monetization strategy | Implemented | `research/PLATFORM_MONETIZATION.md` (2027-02-01 YPP change), scorecard, 30-day strategy |
| 23 | 30-day content calendar | Implemented | `plans/CONTENT_CALENDAR.csv` (68 rows across 4 platforms), `plans/30_DAY_PILOT_STRATEGY.md` |
| 24 | First pilot episode plan | Implemented (plan) | `plans/PILOT_EPISODE_PLAN.md`, EP001 *The Quiet Hour* |
| 25 | Production cost analysis | Implemented | `plans/PRODUCTION_COST_ANALYSIS.md` (lean stack about USD 42/month) |
| 26 | This handover | Implemented | |

## Still blocked or waiting on you

| # | Item | What to do |
|---|---|---|
| 1 | **No GitHub repository** (critical: the container is temporary) | Create an empty repository and tell me its name |
| 2 | **Approvals:** logo concept B, brand kit, plan changes (14 Shorts, 8–14 min long-form) | Reply "approve" or give changes |
| 3 | **ElevenLabs connector** needs reconnecting | claude.ai/customize/connectors → ElevenLabs → reconnect |
| 4 | **OpusClip tools** aren't loaded in sessions | Same page → AI Producer by OpusClip → allow its tools, then start a new session |
| 5 | **Paid plans** (commercial rights) | Approve ElevenLabs Creator and Google AI Pro; OpusClip Starter optional |
| 6 | **Network access** for research: trends.google.com, reddit.com, socialblade.com, support.google.com, suggestqueries.google.com, i.ytimg.com | Approve an environment network change when I request it |
| 7 | **YouTube Data API key** (optional; improves competitor data) | Create a key; I'll request it through the secure credential form |
| 8 | **Channels and handles** | Create them yourself; MOTHWAKE never claims availability |

## Not done (honestly)

- No published content and no paid generations.
- No real narration: EP000 is captions-only with synthesised audio.
- No per-character art sheets yet.
- MW001 is on hold because research found an overlapping premise.
- **Known limits of the pipeline:**
  - Rendering is slow: about 5 min per 40 s of 1080×1920 on this container, so a 12-min long-form would take hours. Plan: pre-scaled layers or FFmpeg-native zoompan.
  - Automated QC checks technical specs but can't judge visual readability. The first EP000 render had captions over the poster text; I caught it by viewing frames and fixed it. A human frame review stays mandatory.
- Every price and policy figure must be re-checked in a browser before you act on it. The research couldn't open official pages in full, only search extracts.
