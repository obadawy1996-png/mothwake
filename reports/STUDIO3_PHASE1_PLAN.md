# STUDIO 3.0: Phase 1 summary and ranked implementation plan

Date 2026-11-20. See `STUDIO3_PHASE1_WORKSPACE_AUDIT.md` (workspace, isolation, available tools) and `tools/*` (repo audit, MCP, skills, licences).

## Recommended free stack (minimum practical set)
FFmpeg (installed) · Python venv with faster-whisper, PySceneDetect, opencv-python-headless · KinoCut (if the test beats `assemble.py`) · SQLite (already: `stories.db`, `analytics/data.db`) · YouTube Studio / official APIs + human approval · Windows Task Scheduler instead of n8n/Postiz for now · Krita (optional, manual retouch) · **No** Blender/OpenToonz/Synfig/Glaxnimate/Resolve now: Flow clips + FFmpeg compositing cover the 2D need, and Resolve is too heavy for 7.7 GB RAM with no GPU.

## Free vs paid
Paid and approved: Google Flow, ElevenLabs. **Everything else in the stack is free.** Hidden-cost watch: Postiz/n8n need an always-on machine (the laptop or a paid server: not free), Semrush/Supermetrics connector usage may be plan-limited, and Meta/TikTok publishing needs app reviews (free, slow).

## Ranked implementation plan (impact ÷ effort)
| Rank | Step | Impact | Effort | Needs approval |
|---|---|---|---|---|
| 1 | Finish the 3-Short pilot (assemble SH012/SH019, SH025 P1 clips) and **publish manually** | ★★★★★ real data | M | publishing |
| 2 | Create `repo/.venv` + install faster-whisper, PySceneDetect, OpenCV; port `assemble.py`/`qc.py` to Windows | ★★★★ | M | **yes (dependencies)** |
| 3 | Make `CLAUDE.md` / `verify_isolation.py` Windows-aware | ★★★ | S | yes (hard-rules file) |
| 4 | Link FB + IG in Metricool; YouTube already branded | ★★★★ | S (owner) | owner action |
| 5 | Test KinoCut in isolation vs our pipeline | ★★ | M | yes |
| 6 | Add "Fear Science" + countdown/rewind devices to the story engine; re-score the 30-slate | ★★★ | M | yes (creative) |
| 7 | Keyword DB + weekly trend report refresh (Google Trends via collector; Reddit manual) | ★★★ | M | no |
| 8 | pendpost test for an approval queue | ★★ | M | yes |
| 9 | Official API integrations (YouTube upload, Meta, TikTok) after verifying the audit/review rules | ★★★ | L | yes + owner accounts |
| 10 | Postiz/n8n only if an always-on host exists | ★ | L | yes |

## Research strategy
Same evidence rules as the existing research (`RESEARCH_LOG.md`): each topic gets a record (keyword, country, source, interest, trend, competitor and discussion evidence, gap, date, confidence); EXPERIMENTAL when thin; refreshed weekly. Add the competitor craft studies (this phase's tavieenfilm/Money Decoded work) as a "mechanics library", never as a copy source.

## 30-video campaign method
Start from the existing 30-Short slate (`stories/shorts/SLATE.md`) and the brief's portfolio hypothesis (10 micro / 6 rules / 5 paranormal / 5 psychological / 4 interactive). Re-balance only with pilot data. Every video passes the similarity gate + originality review; 20 distinct production-package items per video; nothing is scheduled before owner approval.

## Risks and open questions
1. **Shared Google AI credit pool with Chrono Tales** (floor 1,366). Balance now about 2,090 (to re-check).
2. Flow sign-in keeps dropping in the browser pane, and the account index changes (u/0 ↔ u/1).
3. Meta/TikTok API publishing likely starts private-only until review (to verify).
4. YouTube "inauthentic/mass-produced content" policy: keep volume humane and originality visible.
5. Should MOTHWAKE_STUDIO stay as the `repo` folder (recommended) or be renamed?
6. Commercial-use terms of Google Flow output on the owner's plan: the owner should confirm.
