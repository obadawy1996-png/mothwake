---
name: horror-storyboard-generation
description: Turn a script into a shot list/storyboard with layers, camera moves and timing for the assembler.
---

# horror-storyboard-generation

Per shot: duration, framing, layers (bg/far/mid/near/fg/fx with depth), move (push/drift/pan), lighting preset (ENVIRONMENT_BIBLE L1–L5), caption + key word, sfx cues. Output episodes/<id>/storyboard.md and the `shots` array of manifest.json.

## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
