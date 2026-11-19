---
name: 2d-character-consistency
description: Enforce character consistency across generated and drawn shots. Use before any character art enters an episode.
---

# 2d-character-consistency

Compare each shot with production/CHARACTER_BIBLE.md sheet: silhouette, proportions, palette, accent colour, Lamp eye highlight. Reject mismatches. Record approved reference hashes in the manifest. Only approved references (max 3 per Flow clip) may be used as ingredients.

## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
