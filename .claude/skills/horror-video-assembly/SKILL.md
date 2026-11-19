---
name: horror-video-assembly
description: Assemble an episode from its manifest into a clean master and platform exports.
---

# horror-video-assembly

`.venv/bin/python scripts/production/assemble.py episodes/<id>/manifest.json` — refuses to render if the brand validator fails. Long-to-short cut-downs/captions: OpusClip (paid plan, owner approval), then re-run QC. Resolve Free hand-off via FCPXML/OTIO (no scripting in Free).

## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
