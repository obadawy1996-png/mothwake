---
name: horror-quality-control
description: Run automated QC on rendered episodes and block anything failing.
---

# horror-quality-control

`.venv/bin/python scripts/production/qc.py episodes/<id>/manifest.json` → QC_REPORT.md. Blocking: brand assets, licence ledger, resolution/codec/fps, duration target, loudness, true peak. Human approval is always required before publishing.

## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
