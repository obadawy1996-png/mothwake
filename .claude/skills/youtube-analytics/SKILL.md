---
name: youtube-analytics
description: Ingest real performance data and analyse it against cohorts. Use after each publishing cycle.
---

# youtube-analytics

Only real data: YouTube Studio CSV exports or authorised API/connectors. Load with `scripts/analytics/ingest.py`; build dashboard `scripts/analytics/dashboard.py`. Compare within format/duration cohorts; never against one outlier. Log learnings in analytics/LEARNING_LOG.md.

## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
