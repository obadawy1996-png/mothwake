# First Pilot Episode Plan — EP001 "The Quiet Hour" (MW012)

**Status:** Planned, awaiting your approval of the concept and the credit budget.
**Format:** long-form, target 10–12 min, 16:9. Companion Short: a 45 s trailer, 9:16.
**Why this one:** it scores in the top tier, establishes the recurring world (Wrenfield), fits the "isolation / quiet town" trend (Glendale Archives median about 742K, measured 2026-11-19), and uses the brand's sound identity as a story device (silence).

## Story beats (target timing)

| Time | Beat |
|---|---|
| 0:00–0:20 | **Cold open (hook):** the diner clock hits 1:00 and every customer stops mid-sentence. A spoon is held in the air. Cal's voice: "In this town, nobody speaks between one and two in the morning." |
| 0:20–0:45 | Title card "A MOTHWAKE STORY · The Quiet Hour" with the signature sound |
| 0:45–3:30 | **Act I:** Cal arrives to make a podcast episode. Ines communicates with notes. Rule shown: a sign at the town line. Clue 1: the radio tower's light blinks during the hour. |
| 3:30–7:30 | **Act II:** Cal talks during the hour. Something outside repeats his sentence, badly, then better each night. Clue 2: old town tapes where the 'echo' learns words. Ines's note: "Every visitor taught it a little." |
| 7:30–10:00 | **Act III:** reveal that the silence keeps the thing from finishing its language, and it is nearly fluent. Cal tries to leave without speaking. |
| 10:00–11:00 | **Ending:** his podcast uploads by itself. The narrator sounds like Cal. Cal isn't in the room. Final frame: the Moth on the diner window (easter egg). Outro clip, then the end screen. |

## Hooks (5 alternatives in the story database; A/B the first line)

The lead line is "In this town, nobody speaks between 1 and 2 a.m. Not even in an emergency."

## Production plan

| Step | Owner (agent) | Output | Paid? |
|---|---|---|---|
| Script and timing | Storywriter | `episodes/EP001/script.md` | No |
| Storyboard (about 70 shots) | Storyboard Designer | `storyboard.md`, manifest shots | No |
| Character sheets: Cal, Ines, "the Echo" (silhouette only) | Character Consistency Supervisor | `production/characters/` | No |
| Backgrounds: diner, main street, radio tower, town sign (layered) | Visual Production | `production/backgrounds/` | Flow image gens if used (approval) |
| Hero animation: about 12 clips (spoon freeze, window breath, tower blink) | Visual Production → you generate in Flow | `art/flow/` | ≈ 240 Fast or 120 Lite credits (estimate) |
| Narration: Cal (narrator), Ines (none; notes), the Echo (processed Cal voice) | Voice & Sound | `audio/` | ElevenLabs ≈ 20k credits incl. retakes (estimate) |
| SFX: diner room tone, clock, wind | Voice & Sound | synthesised or licensed | Mostly free |
| Assembly, master and exports | Video Assembly | `master/`, `exports/` | No |
| QC | Quality Control | `QC_REPORT.md` | No |
| Thumbnails A/B (watcher, light) + title | Packaging | `package/` | No |
| Trailer Short cut (FFmpeg pipeline) | Video Assembly | 45 s 9:16 | No |
| **Your final approval** | You | `approvals.owner_final` | — |

## Title options (plain-sentence style, which research shows performs for new-wave channels)

1. Nobody in This Town Speaks Between 1 and 2 AM
2. I Broke My Town's Only Rule: Don't Talk During the Quiet Hour
3. Something in Wrenfield Is Learning to Talk

## Success criteria (cohort-based, real data only)

- Average view duration and % viewed against the channel's long-form cohort once n ≥ 3. Before then, use the absolute retention curve shape: no cliff after the cold open.
- CTR by thumbnail variant (YouTube test).
- Subscribers per 1k views, and returning viewers after week 2.
