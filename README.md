# MOTHWAKE
*Some things should stay asleep.*

Independent 2D animated horror and mystery brand. **Start with `FINAL_PROJECT_HANDOVER.md`.**

| Area | Where |
|---|---|
| Isolation | `ISOLATION_POLICY.md`, `scripts/verify_isolation.py` |
| Research | `research/` (market, competitors, trends, platform monetization, tool stack, specs) |
| Brand kit | `brand/` (guides, logos, kit, thumbnails, sound, video) |
| Stories | `stories/` (database, scoring model, concepts) |
| Production | `production/` (bibles), `scripts/production/` (assemble, QC), `episodes/` |
| Agents & skills | `.claude/agents/`, `.claude/skills/` |
| Analytics | `scripts/analytics/analytics.py`, `analytics/dashboard.html` |
| Plans | `plans/` (plan, 30-day strategy, calendar, costs, pilot episode) |
| Reports | `reports/` (Phase 1, idea scorecard) |

Run all tests:
```bash
.venv/bin/python scripts/verify_isolation.py verify && bash tests/test_isolation.sh && .venv/bin/python tests/test_brand.py && .venv/bin/python tests/test_system.py
```
