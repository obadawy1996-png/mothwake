# GitHub repository audit (STUDIO 3.0, Phase 1)

**Date:** 2026-11-20. **Method:** GitHub REST API (repo metadata and latest release) plus the raw LICENSE file where GitHub showed no standard licence. Raw data: `tools/audit_raw/` (`github_api_summary.tsv` and one JSON per repo).
**Not done yet (Phase 2):** reading each repo's source and dependency tree, and isolated test installs. "Capabilities" below come from each repo's own description; they are **not tested claims**.

| # | Repo | Licence (verified) | Stars | Last push | Latest release | Verdict | Why |
|---|---|---|---|---|---|---|---|
| 1 | lhitches/google-trends-mcp | MIT | 2 | 2026-09-12 | none | **TEST in isolation** | Fits the need, but tiny and unproven. Google Trends has no official API, so it relies on unofficial endpoints (rate limits and breakage likely). Our own `gtrends_collector.py` already does this |
| 2 | wrxck/reddit-mcp | MIT | 13 | 2026-03-29 | none | **DEFER** | Needs a Reddit OAuth app. Reddit's Data API terms restrict commercial use; it can post and vote, so read-only scope is needed. Inactive since March |
| 3 | microsoft/playwright-mcp | Apache-2.0 | 39.9k | 2026-11-18 | v0.0.86 | **OPTIONAL** | Solid and official. The built-in browser pane already covers interactive research, so add it only for unattended scraping |
| 4 | modelcontextprotocol/servers | MIT→Apache-2.0 (transition; docs CC-BY-4.0) | 92k | 2026-11-19 | v2.5.0 | **SKIP** | Filesystem and git are already native in Claude Code |
| 5 | KyaniteLabs/kinocut | Apache-2.0 | 272 | 2026-11-19 | v2.0.1 | **TOP CANDIDATE: test** | Active, "guardrailed" FFmpeg editing MCP. Must test against our own `assemble.py` on Windows |
| 6 | rhkiswani/mcp-video | Apache-2.0 | 2 | 2026-05-10 | none | SKIP | Overlaps with KinoCut; tiny adoption |
| 7 | RFingAdam/rushcut | **AGPL-3.0** | 1 | 2026-11-20 | none | SKIP | AGPL plus no adoption |
| 8 | PlbKin190/video-editor-mcp | Apache-2.0 | 0 | 2026-09-25 | none | SKIP | Duplicate; no adoption |
| 9 | jessestay/social-media-mcp | MIT | 1 | 2026-05-16 | none | SKIP | Unproven; we use official APIs and human approval instead |
| 10 | pendpost/pendpost | MIT | 28 | 2026-11-18 | v2.14.0 | **CANDIDATE (Phase 9)** | Local-first draft→approve→publish queue that matches the brief. Platform support must be tested one platform at a time |
| 11 | anthropics/claude-plugins-official | Apache-2.0 | 47.8k | 2026-11-20 | — | USE selectively | Source of `plugin-dev`. Install only individual plugins, project-scoped |
| 12 | Melvynx/video-agent-skills | MIT | 186 | 2026-11-06 | — | **REVIEW, then cherry-pick** | Short-form scripting and editing skills (Markdown). Copy only useful ones into `.claude/skills` with the MIT notice |
| 13 | iamaanahmad/agents-video-editing-skills | MIT | 1 | 2026-11-11 | — | SKIP | No adoption; overlaps with #12 |
| 14 | remotion-dev/skills | **No licence file** | 7.6k | 2026-11-18 | — | READ ONLY | No licence means no permission to copy; use it as reference only |
| 15 | obra/superpowers | MIT | 322k | 2026-11-03 | v7.0.2 | OPTIONAL | A software-dev methodology, not media production. Low value for MOTHWAKE now |
| 16 | gitroomhq/postiz-app | **AGPL-3.0** | 42k | 2026-11-20 | v2.26.0 | **DEFER** | Self-hosting needs Docker, Postgres and Redis, which is heavy for 7.7 GB RAM and no Docker. The laptop would have to stay on |
| 17 | n8n-io/n8n | **Sustainable Use License** (fair-code; `.ee` files need an enterprise licence) | 211k | 2026-11-20 | 2.48.7 | **DEFER** | Free for internal self-hosted use. Chrono Tales notes found n8n needs Node ≤24 (we have 26). Use Windows Task Scheduler for now |
| 18 | activepieces/activepieces | MIT core + separate EE licence | 25.6k | 2026-11-20 | 0.93.0 | SKIP | Overlaps with n8n; also Docker |
| 19 | LateWiz (website, not on GitHub) | not checked | — | — | — | **UNVERIFIED** | Not inspected this phase |
| 20 | SYSTRAN/faster-whisper | MIT | 26.9k | 2026-11-12 | v1.2.1 | **INSTALL (venv)** | Caption timing and VO sync; CPU int8 works on this laptop |
| 21 | ggml-org/whisper.cpp | MIT | 55k | 2026-11-20 | v1.9.5 | Fallback | Only if faster-whisper is too slow on 2 cores |
| 22 | Breakthrough/PySceneDetect | BSD-3 | 5.6k | 2026-11-20 | v0.7.3 | **INSTALL (venv)** | QC: hidden cuts, repeated shots (the Omar Studio lesson) |
| 23 | opencv/opencv | Apache-2.0 | 91.7k | 2026-11-20 | 5.1.0 | **INSTALL (venv, opencv-python-headless)** | Black and frozen frame checks; PySceneDetect needs it |
| 24 | MediaArea/MediaInfo | BSD-2 | 2.1k | 2026-11-19 | v26.10 | SKIP for now | ffprobe already covers stream checks |
| 25 | remotion-dev/remotion | **Remotion License** (free for individuals and small companies, commercial OK; company licence above a size threshold) | 74.5k | 2026-11-20 | v4.0.545 | DEFER | Our pipeline is Python and FFmpeg; Remotion adds a heavy Node and Chromium render stack |
| 26 | Zulko/moviepy | MIT | 15.2k | 2026-08-26 | v2.2.1 | SKIP | FFmpeg directly is faster and already in use |

**Security notes for anything installed later:** read `package.json` / `pyproject` and install scripts before running; venv or local `node_modules` only; MCPs with write or publish powers (Reddit posting, social posting) get read-only or human-approval modes; API keys go in environment variables, never in the repo.
