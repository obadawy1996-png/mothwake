# MOTHWAKE — Research and Implementation Plan

**Version:** 1.0 (2026-11-19). **Owner approval required before each phase starts.**

Operating model: Claude researches, writes, prepares, generates, organises, assembles and checks. You review and approve. Nothing is published and no paid credits are used without your explicit approval.

Status labels used throughout: **Implemented · Tested · Partially implemented · Planned · Blocked**.

---

## Phase gates

| Phase | Starts when | Critical dependencies |
|---|---|---|
| 2 Research | You approve this plan | B1 repository, B2 network hosts |
| 3 Brand strategy | Phase 2 report reviewed | Research findings |
| 4 Brand kit | You pick a logo concept | Fonts downloaded, licence files stored |
| 5 Story and visual engine | Brand kit approved | ElevenLabs reconnected (B3), Google Flow workflow confirmed |
| 6 Agents and skills | Phase 5 tested | None |
| 7 Editing and QC | Phase 6 tested | Your DaVinci Resolve version, for the import test; OpusClip tools enabled in the session (B6) |
| 8 Analytics and monetization | Phase 7 tested | Channel accounts exist (for live data) |
| 9 30-day strategy | Phases 2–8 complete | None |
| 10 Pilot | Your approval of the first episode plan and its credit budget | Credits approved |

---

## Phase 2 — Market and competitor research

**Method**
1. Build a candidate list of 50 or more English-language channels. Search YouTube for animated horror, analog horror, urban legends, animated mystery and horror Shorts, and take neighbours from "related channels".
2. Select at least 30, deliberately mixing three groups: small or new channels (under 2 years old or under 100k subscribers), fast risers, and a few established benchmarks.
3. For each channel, collect only public data: URL, subscribers, creation date, upload frequency over the last 90 days, the top 10 videos, the recent 10 videos, views-to-subscriber ratio, Shorts vs long-form split, durations, format, visual style, thumbnail pattern, and engagement (likes and comments per view where visible). Every field records its source and date. Unknown values stay `unknown` and are never estimated silently.
4. Fast-growth case studies: launch date, upload count up to the growth inflection, formats, and monetization status **only where publicly verifiable**. Any third-party earnings estimate is labelled as an estimate.
5. Trend intelligence: YouTube search suggestions, Google Trends for the US, UK, Canada and Australia separately, Reddit horror communities (r/nosleep, r/creepypasta, r/LetsNotMeet, r/analoghorror and others, read-only), seasonal curves, and Semrush keyword volume if you approve it.
6. Each trend row records source, date, evidence, confidence (high/medium/low), direction, saturation, opportunity and brand-fit.

**Outputs:** `research/MARKET_OPPORTUNITY_REPORT.md`, `COMPETITOR_DATABASE.csv`, `TREND_DATABASE.csv`, `CONTENT_GAP_ANALYSIS.md`, `WEEKLY_TREND_REPORT.md`, plus `scripts/research/` collectors that can be re-run weekly.

**Also verified in Phase 2, from official sources:** current YouTube Partner Program tiers (early access vs ad revenue sharing, Shorts vs long-form thresholds, payout via AdSense), Facebook Content Monetization eligibility and regional availability, TikTok and Instagram creator programmes, plus pricing, rights and API access for Google Flow, ElevenLabs, OpusClip and Metricool. No figures are stated in this plan until they have been checked.

---

## Phase 3 — Brand strategy and identity

- Positioning, audience personas and tone of voice, drawn from Phase 2 gaps.
- Palette check: test the four core colours for contrast (WCAG) on banner, caption and thumbnail use. Propose at most two accent refinements, for example a pale "lamp light" highlight, and justify each one.
- Typography: Cinzel for the wordmark and titles, Cormorant Garamond for title cards, Inter for captions and UI. Font files and OFL licence texts are stored in `brand/fonts/`.
- Three or more logo concepts as hand-built SVG vectors, not AI raster images:
  A. a nocturnal moth emblem
  B. a moth whose wings carry eye-like markings
  C. an abstract "awakening" mark, such as a closed eye or wing shape opening toward a point of light
  Each concept is tested at 16, 32, 48 and 98 px, in a circular crop, and in monochrome.
- Magnific (free daily allowance) is used only for mood references, never as final logo art.

**Decision for you:** choose the final logo concept.

## Phase 4 — Brand kit

- Logo set: primary, secondary, icon, monochrome, light and dark versions, as SVG sources and transparent PNG exports.
- YouTube profile picture (800×800, safe in a circular crop) and banner (2560×1440). Text stays inside the 1546×423 safe area. Previews are made for TV, desktop and mobile crops, and the file stays under YouTube's size limit (both checked against current YouTube Help).
- Watermark: a simplified moth at 150×150 or larger, with automatic contrast variants for light and dark scenes.
- Thumbnail system: four or more layouts as editable SVG/Figma templates plus a Python/Pillow renderer, with documented rules.
- Channel copy: description, short bio, extended About section, trailer script, brand introduction, and bios for TikTok, Instagram and Facebook. No username is claimed as available unless you have checked it.
- Sound identity: a short moth-wing flutter and low-tone signature, an outro sting, sound guidelines and narration direction. Sources are licence-clean only (ElevenLabs SFX with your approval, or self-made).
- All eight guide documents in `brand/` (listed in the master brief), with previews and export specifications.
- `scripts/brand_validator.py` hashes the approved assets into `brand/APPROVED_ASSETS.lock` and fails any render that uses a missing, changed or unapproved asset. It never replaces an asset automatically.

## Phase 5 — Story engine and visual production system

- Story database (SQLite inside the project) holding every field listed in the brief, including an originality review.
- Story similarity checker: TF-IDF and embedding-free n-gram overlap across premise, twist and setting, plus a "twist taxonomy" tag that stops predictable repeats.
- Viral Content Intelligence scoring: 12 criteria scored 1–5, with documented weights. It is **a prioritisation aid, not a prediction**. Weights are recalibrated from real data after the pilot.
- Hook generator: at least 5 hooks per story, built from varied structures, with duplicate-opening detection.
- Bibles: characters (proportion sheets, palettes, turnarounds), environments, poses, expressions, lighting and backgrounds, plus an animation reference library.
- Google Flow workflow: reference-image packs and prompt templates for character consistency and image-to-video, with a manual export checklist. It is documented as manual because there is no API.
- ElevenLabs workflow: narrator and character voice specs, SFX lists and credit estimates per episode.

## Phase 6 — Agents and skills

The 14 agents are created in `.claude/agents/`. Each has a role, inputs, outputs, files owned and a hand-off contract (JSON manifest fields). The 18 skills are created in `.claude/skills/`. A duplicate check runs before each one is created, and existing skills are never overwritten.

| Pipeline step | Agent | Main skills |
|---|---|---|
| 1 Trend discovery | Trend Research, Competitor Intelligence | horror-trend-intelligence, horror-market-research |
| 2–4 Scoring, selection, hooks | Viral Content Analyst, Creative Director | viral-hook-analysis, horror-story-development |
| 5 Script | Storywriter | horror-scriptwriting |
| 6 Storyboard | Storyboard Designer | horror-storyboard-generation |
| 7–8 Characters, environments, visuals | Character Consistency Supervisor, Visual Production | 2d-character-consistency, 2d-environment-design, google-flow-production |
| 9 Voice and sound | Voice and Sound | elevenlabs-audio-production |
| 10–11 Assembly and branding | Video Assembly | horror-video-assembly, ffmpeg-media-processing, mothwake-brand-development, plus OpusClip for Shorts cut-downs and captions |
| 12 QC | Quality Control | horror-quality-control |
| 13 Packaging | Thumbnail and Packaging | thumbnail-and-title-optimization, mothwake-logo-and-visual-identity |
| 14–15 Approval and publish prep | You, and the Creative Director | — |
| 16–17 Analysis and learning | YouTube Analytics, Revenue and Monetization | youtube-analytics, youtube-monetization-analysis |

Each episode gets `episodes/<id>/manifest.json`, which records its step status, approvals, asset hashes and licences.

## Phase 7 — Automated editing and QC

- FFmpeg assembly: layered stills with parallax and camera moves, captions burned in using brand styles, audio ducking, and loudness normalised to −14 LUFS integrated (to be verified against current platform guidance).
- Exports: a clean master with no watermark, plus platform variants for YouTube Shorts, long-form, TikTok, Instagram Reels and Facebook (9:16 / 16:9, specific safe zones).
- DaVinci Resolve hand-off: FCPXML or EDL plus stems, tested against your installed version.
- Automated QC: brand validator, resolution and frame rate, loudness, black or frozen frames, caption safe area, duration targets (Shorts 35–60 s, long-form 5–10 min), licence ledger complete, and no unapproved assets.
- **Update 2026-11-19: OpusClip paid plan declined.** The free plan is non-commercial and watermarked, so OpusClip is **not used for published content**. Shorts cut-downs, captions and reframing use the FFmpeg pipeline. Original note follows for reference:
- ~~AI Producer by OpusClip is the chosen tool~~ for cutting Shorts from long-form stories, AI captions, reframing to 9:16, and platform-ready variants. The FFmpeg pipeline remains the fallback and produces the clean master.
  - Before first use: verify its plan, credit costs, commercial rights to outputs, export formats and caption styling. Captions must use MOTHWAKE fonts and colours, or be restyled.
  - Every OpusClip export goes through the brand validator and QC before approval.
  - OpusClip credits are only spent with your approval. Its scheduling and publishing features are never used without your explicit approval.

## Phase 8 — Analytics and monetization framework

- Dashboard (HTML artifact plus CSV/SQLite) showing the Shorts, long-form and brand KPIs from the brief, and a cross-platform comparison.
- Data sources: YouTube Studio exports or the YouTube Analytics API (once authorised), Supermetrics, and Metricool. Data is never invented. Empty panels say "no data yet".
- Comparison by cohort, meaning the same format and duration band, so no video is judged against a single outlier.
- Monetization model separating channel growth, early YPP access, ad-revenue eligibility, actual revenue and payout requirements, for each platform.

## Phase 9 — 30-day content strategy

- Targets, not quotas: about 30 Shorts, about 4 long-form stories, weekly trend reports and weekly performance reviews.
- Controlled experiments that change one variable per batch (hook type, category, length, visual approach, thumbnail concept).
- Separate calendars for YouTube, TikTok, Instagram and Facebook.
- Production cost analysis per Short and per long-form episode (credits, hours and tools), based on verified prices.

## Phase 10 — Pilot

- First pilot episode plan delivered for your approval, with its credit budget.
- One internal test render through the full pipeline. **It is not published.**
- The full test matrix from the brief is run, and the results go into `reports/`.
- `FINAL_PROJECT_HANDOVER.md` lists all 26 deliverables with honest status labels.

---

## Cost and credit policy

- Free first: FFmpeg, Python, Playwright, OFL fonts, and Magnific's free daily allowance.
- Every paid action (ElevenLabs characters, Semrush units, any Flow plan, OpusClip) is costed in advance and run only after you approve it.
- No tool purchases are recommended unless the research shows a clear gap.

## Risks

| Risk | Mitigation |
|---|---|
| "Reused or repetitive content" policies on YouTube, Facebook and TikTok | Original stories, the similarity checker, a distinct value per video, and no templated mass uploads |
| AI character inconsistency | Reference packs, a consistency supervisor, and layer-based animation from approved stills |
| Licensing gaps | A licence ledger per asset, and the brand validator blocks renders with unknown licences |
| Container loss | Push to GitHub after every phase |
| Over-relying on scores | Scores are labelled as heuristics and recalibrated on real data |
