---
name: google-flow-production
description: Prepare manual Google Flow generations (no API): ingredient packs, prompts, export checklist.
---

# google-flow-production

Flow has no public API — Claude prepares prompts + up to 3 reference ingredients per clip; the owner generates in the browser and drops exports into episodes/<id>/art/flow/. Record model, credits used, date in the manifest. Verify commercial-use terms on the owner's plan before publishing (unverified as of 2026-11-19). Outputs carry SynthID.

## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
