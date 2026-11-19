---
name: horror-trend-intelligence
description: Produce the weekly trend report and update research/TREND_DATABASE.csv. Use every Monday or before choosing topics.
---

# horror-trend-intelligence

Each row: source, date, evidence, confidence, direction, saturation, opportunity, brand_fit, data_type. Split regions US/UK/CA/AU when data allows. Only adapt trends that fit the brand. Write research/WEEKLY_TREND_REPORT.md.

## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
