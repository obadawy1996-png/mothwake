# MOTHWAKE — project instructions

Independent 2D animated horror and mystery brand. Tagline: "SOME THINGS SHOULD STAY ASLEEP."

## Hard rules
- Read `ISOLATION_POLICY.md`. Run `.venv/bin/python scripts/verify_isolation.py verify` at the start of each session. Stop if any check fails.
- Never touch files outside `/home/user/mothwake`. Never install into global Python or Node.
- No paid credits, no publishing, and no account or plugin changes without the owner's explicit approval each time.
- All stories are original fiction. Never copy another creator's scripts, characters, narration, scenes or visual identity.
- Never fabricate metrics. Label every number as measured (with source and date), estimated, or unknown.
- Brand colours: Obsidian Black #090A0D, Charcoal #25232B, Ash Violet #77717D, Old Gold #B89A68.
- Fonts: Cinzel and Cormorant Garamond (both SIL OFL 1.1, verified), Inter (SIL OFL 1.1).

## Layout
- `brand/` brand kit and guides
- `research/` market, competitor and trend data
- `stories/` story database
- `episodes/<id>/` one folder and manifest per episode
- `analytics/` dashboards and data
- `scripts/` tools
- `.claude/skills/`, `.claude/agents/` project-only skills and agents
- `reports/` phase reports
- `plans/` research and implementation plan

## Workflow
Work phase by phase as set out in `plans/RESEARCH_AND_IMPLEMENTATION_PLAN.md`. Report after each phase. Don't start the next phase while a critical dependency is unresolved.
