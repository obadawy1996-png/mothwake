# Phase 1 Report — Workspace Audit and Project Isolation

**Date:** 2026-11-19
**Phase status:** Complete, with blockers listed in section 6 that must be cleared before Phase 2.

## 1. Workspace audit

| Item | Finding |
|---|---|
| Working directory | `/home/user` was empty at session start. |
| Chrono Tales files | None in this container. Search covered `/home`, `/root`, `/opt`, `/srv` and `/workspace`. |
| Chrono Tales plugin | Disabled by you before this session and not loaded. The earlier hook conflict is resolved. |
| Other account plugins | `postiz` (social scheduling CLI) and `claude-automation-recommender`. Neither defines hooks in this session. |
| User-level Claude config | No `settings.json` or `CLAUDE.md`. `~/.claude/skills` holds only built-in items. It is fingerprinted. |
| Git | No repository. The project has a local `git init`, but there is no remote yet (see blocker B1). |
| Container | Temporary cloud container with 60 GB free. Anything not pushed to GitHub will be lost. |

## 2. Isolated project — Implemented and tested

- Created `/home/user/mothwake` with its own venv, `.claude/` (skills, agents, settings), `CLAUDE.md`, `.gitignore`, and folders for brand, research, stories, episodes, analytics, config, tools, docs, tests, reports and plans.
- `ISOLATION_POLICY.md` defines the boundaries.
- `scripts/verify_isolation.py` passes 10 of 10 checks.
- `tests/test_isolation.sh` passes 7 of 7. Every injected violation is detected.

## 3. Local tool inventory (verified in this container)

| Tool | Status | Notes |
|---|---|---|
| Python 3.13.18 + venv | Available | numpy 2.5.3, pandas 3.0.5, Pillow 12.3.0 and reportlab 5.0.1 are on the system Python. They will be installed into the project venv when needed. |
| FFmpeg / ffprobe 6.1.1 | Available | Main encode and assembly engine. |
| ImageMagick 6.9.12 | Available | Raster exports. |
| Node 22.23.5 / npm 10.9.9 | Available | Remotion is possible later and would be installed project-local. |
| Playwright + Chromium | Available | Renders SVG to PNG precisely, so it can stand in for Inkscape or rsvg. |
| Inter font | Installed system-wide | SIL OFL 1.1. |
| Cinzel, Cormorant Garamond | Licence verified (SIL OFL 1.1, from the google/fonts repository) | Files will be downloaded into `brand/fonts/` in Phase 3. |
| Inkscape, rsvg-convert, sox, sqlite3 CLI | Not installed | Not required. Python's built-in `sqlite3` module covers the databases. |
| DaVinci Resolve Free | Not available here | It is a desktop app, so it runs on your computer. Resolve Free has no external Python scripting, so the planned hand-off is FCPXML/EDL timeline import plus FFmpeg-rendered stems. This will be checked against your installed version in Phase 7. |
| Audacity | Not available here | Optional. FFmpeg filters cover loudness normalisation. |

## 4. Connected services (read-only checks, no credits used)

| Service | Status | What it means for MOTHWAKE |
|---|---|---|
| ElevenLabs | Connected, but the usage check failed with "requires additional permissions" | **Blocker B3.** Reconnect it in connector settings so plan, credits and commercial-licence tier can be checked. |
| Magnific | Connected. Free plan, 0 credits, 20 free image generations per day | Usable for concept exploration within the free daily allowance. Commercial terms for free-plan outputs must be checked in Phase 3. |
| Figma | Connected | Good fit for editable logo, banner and thumbnail templates. |
| AI Producer by OpusClip | Connected, but its tools aren't loaded in this session | Candidate for clipping long-form into Shorts and for captions. Its features, pricing and rights will be evaluated in Phase 6 or 7. |
| Metricool | Connected, not loaded in this session | Candidate for cross-platform scheduling and analytics. Nothing will be published without your approval. |
| Supermetrics | Connected | Candidate source for YouTube, Facebook, Instagram and TikTok analytics once those channels exist. |
| Semrush | Connected | Keyword and search-demand research for Phase 2. API units may be charged per report, and costs are shown before use. |
| Notion, Gmail, HubSpot, Intuit, Viberate, AiChatForWebsite | Connected, not needed | Not used. |
| Google Flow | No connector and no API | Manual workflow in your browser. Claude prepares prompts and reference sheets, you generate, and assets are dropped into the episode folder. |

## 5. Network access (current environment policy)

| Host | Result |
|---|---|
| youtube.com, raw.githubusercontent.com | Reachable |
| googleapis.com (YouTube Data API) | Reachable. It needs an API key, which you would provide through the secure credential form. |
| reddit.com, trends.google.com, socialblade.com, fonts.google.com, support.google.com | **Blocked by the environment's network policy** (proxy: "no rule allows this host") |

## 6. Blockers and decisions needed before Phase 2

| # | Blocker | Severity | What clears it |
|---|---|---|---|
| B1 | No GitHub repository, so the work will be lost when the container is reclaimed | Critical | Create an empty repository (for example `mothwake`) and tell me its name. I'll push to it. |
| B2 | Research hosts are blocked (Reddit, Google Trends, Social Blade, YouTube Help) | Critical for Phase 2 | Approve adding these hosts to this environment, or to a new MOTHWAKE-only environment. I'll send the request when Phase 2 starts. |
| B3 | ElevenLabs connector lacks permissions | Needed by Phase 5 | Reconnect ElevenLabs in connector settings. |
| B4 | No YouTube Data API key | Optional, but improves competitor data | Create a free YouTube Data API v3 key in Google Cloud and enter it in the secure credential form when asked. |
| B5 | Semrush report costs | Decision | Approve a Semrush budget, or tell me to skip Semrush. |

## 7. Deliverable status after Phase 1

| # | Deliverable | Status |
|---|---|---|
| 1 | Independent MOTHWAKE project | Implemented, tested |
| 2 | Verified isolation report | Implemented, tested (this report and `ISOLATION_POLICY.md`) |
| 3–26 | All other deliverables | Planned. See `plans/RESEARCH_AND_IMPLEMENTATION_PLAN.md`. |
