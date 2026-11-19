---
name: horror-market-research
description: Research competitor horror/mystery channels with public data only. Use to refresh research/COMPETITOR_DATABASE.csv.
---

# horror-market-research

Run `research/collectors/yt_public_collector.py` then `build_competitor_csv.py`. Every metric needs source + as-of date; unknown stays `unknown`. Never present third-party earnings estimates as income. Compare channels by tier (small/new, riser, benchmark).

## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
