# Viral Content Intelligence — Scoring Model

**This is a prioritisation tool, not a prediction.** No formula predicts virality. The score ranks *which story to make next* from editorial judgement plus evidence, and its weights are recalibrated from real performance after the pilot.

Implementation: `scripts/story/storydb.py`. Each criterion is scored 1–5.

| # | Criterion | Weight | What a 5 looks like | Evidence source |
|---|---|---|---|---|
| 1 | Topic demand | 1.5 | Rising or evergreen interest in the theme | `research/TREND_DATABASE.csv` |
| 2 | Audience curiosity | 1.5 | The premise raises a question you need answered | Editorial, plus comment themes on comparable videos |
| 3 | Hook strength | 2.0 | Best hook + first visual creates a question in under 1.5 s | Hook review (5+ alternatives) |
| 4 | Emotional impact | 1.0 | Clear target feeling (dread, grief, paranoia) delivered | Script read |
| 5 | Story clarity | 1.0 | Understandable on one watch without the narration | Storyboard read |
| 6 | Suspense | 1.0 | Escalation with no flat beats | Beat sheet |
| 7 | Retention potential | 1.5 | A new piece of information every 3–6 s; reveal held to the end | Beat timing |
| 8 | Rewatch potential | 1.0 | The ending recontextualises earlier shots | Twist type |
| 9 | Shareability | 1.0 | "You have to see the ending", a debate, or a relatable fear | Editorial |
| 10 | Production complexity | 1.0 (inverted) | 1 = reuses library assets; 5 = many new characters or sets | Asset list |
| 11 | Originality | 1.5 | No resemblance to known stories (similarity < 0.30) | Similarity checker plus manual review |
| 12 | Brand suitability | 1.5 | Moth or light motif, low gore, psychological | Brand guidelines |

**Priority** = weighted mean rescaled to 0–100. Complexity is inverted, so simpler stories score higher.

## Gates (independent of score)

- Similarity ≥ 0.45 to any story in the database: **blocked**. 0.30–0.45: rework the twist or setting.
- Fewer than 5 hooks: **blocked**.
- An originality review is required. Any resemblance to a known creator's story means it is rewritten or dropped.
- Real-world claims ("true story", real victims or places in tragedies): **blocked**.

## Calibration (after each 2-week cycle)

1. For each published video, compare the pre-launch score with cohort-normalised results: Shorts are compared with Shorts of similar length, long-form with long-form.
2. Where a criterion consistently over- or under-predicts, adjust its weight by at most ±0.25 per cycle. Log every change in `analytics/LEARNING_LOG.md`.
3. Never fit weights to a single outlier.

## Initial status

The 12 concepts in `stories/concepts/` are scored by editorial judgement made **before** the trend data. `topic_demand` is to be updated from the research results.
