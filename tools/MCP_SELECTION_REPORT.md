# MCP selection report (Phase 1, recommendations only, nothing installed)

| Need | Already have (TESTED/connected) | Candidate | Recommendation |
|---|---|---|---|
| Trend research | Repo collectors (`gtrends_collector.py`, YouTube collectors), Semrush and Supermetrics connectors, web search | google-trends-mcp (MIT, 2★) | **Test in an isolated venv** against our collector; adopt only if it adds rising/regional queries reliably |
| Reddit audience research | — | reddit-mcp (MIT, 13★, can post/vote) | **Defer.** Needs a Reddit app plus API-terms review; read-only research can use public pages manually |
| Browser research | Built-in browser pane (TESTED) | playwright-mcp (Apache-2.0) | Optional, for unattended collection only |
| Video editing | FFmpeg + repo `assemble.py` / `qc.py` | **KinoCut** (Apache-2.0, 272★, v2.0.1) | **Test first** (one MCP only). Skip mcp-video, rushcut (AGPL), video-editor-mcp |
| Publishing queue | YouTube Studio (browser), Metricool connector | **pendpost** (MIT, v2.14.0) | Test in Phase 9, per platform, approval-gated |
| Social posting | Metricool (needs FB/IG linked) | social-media-mcp (1★) | Skip |
| Filesystem/git | Native Claude Code tools | modelcontextprotocol/servers | Skip |

Install location for any MCP: **project scope** (`repo/.mcp.json`), never user/global scope, so Chrono Tales is unaffected.
