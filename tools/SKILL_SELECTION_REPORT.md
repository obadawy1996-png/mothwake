# Skills inventory and selection (Phase 1)

## Existing MOTHWAKE skills (project-scoped, `repo/.claude/skills/`, 19)
2d-character-consistency · 2d-environment-design · elevenlabs-audio-production · ffmpeg-media-processing · google-flow-production · horror-market-research · horror-quality-control · horror-scriptwriting · horror-story-development · horror-storyboard-generation · horror-trend-intelligence · horror-video-assembly · mothwake-brand-development · mothwake-logo-and-visual-identity · thumbnail-and-title-optimization · viral-hook-analysis · youtube-analytics · youtube-monetization-analysis (+ .gitkeep)

## Existing agents (`repo/.claude/agents/`, 14) vs the 19 the brief asks for
Exist: creative-director, storywriter, storyboard-designer, character-consistency-supervisor, visual-production-agent, voice-and-sound-agent, video-assembly-agent, quality-control-agent, thumbnail-and-packaging-agent, trend-research-agent, competitor-intelligence-agent, viral-content-analyst, youtube-analytics-agent, revenue-and-monetization-analyst.
**Missing from the brief's list:** Keyword Research, Content Opportunity, Hook Optimization, Subtitle, Brand Integration, Publishing. **Proposal:** fold Keyword + Content Opportunity into trend-research; Hook into storywriter; Subtitle + Brand Integration into video-assembly; add only **publishing-agent** (a genuinely new responsibility). That avoids duplicate agents, as the brief asks.

## External skill sources
| Source | Licence | Action |
|---|---|---|
| Melvynx/video-agent-skills | MIT | Review; copy only non-overlapping skills, with the MIT notice, under new names (never overwrite) |
| anthropics/claude-plugins-official → plugin-dev | Apache-2.0 | Use when building new MOTHWAKE skills |
| remotion-dev/skills | **no licence** | Reference only; do not copy |
| obra/superpowers | MIT | Not needed for media work now |
| Chrono Tales / Omar Studio skills (39) | owner's own | **Read-only reference**; adapt the ideas into MOTHWAKE files, never copy into or modify CT |
