# EP001 — Flow credit budget

**All numbers here are estimates**, prepared 2026-11-19 before any generation. Nothing has been spent.
Price inputs come from the owner brief (not checked by Claude against Google's pages):
Google AI Pro = **1,000 credits / month**; Veo 3.1 **Lite = 10**, **Fast = 20** credits per 8 s generation.
Still-image cost in Flow = **unknown** (not in the brief, not checked).

> Spending credits needs the owner's explicit go-ahead. The owner generates; Claude never does.

## 1. Clips (estimate)
| Item | Count | Credits each | Credits |
|---|---|---|---|
| Fast clips, first take (C01, C04, C08, C09) | 4 | 20 | 80 |
| Lite clips, first take (C02, C03, C05, C06, C07, C10, C11, C12) | 8 | 10 | 80 |
| **First takes** | 12 | | **160** |
| One retry for every clip (same model) | 12 | 10 / 20 | 160 |
| **Clips incl. one retry each** | 24 generations | | **320** |

## 2. Reference stills (cost unknown)
| Item | Count | Assumed attempts each (estimate) | Generations |
|---|---|---|---|
| Step 1a required stills | 18 | 3 | 54 |
| Step 1b optional stills | 4 | 3 | 12 |
| **Total still generations** | 22 | | **66** |

Credits for stills = 66 × (Flow's per-image cost). Check that cost in the Flow UI before the first still.

## 3. Total vs the monthly allowance
| Scenario | Stills | Clips + 1 retry | Total | Left of 1,000 | Share used |
|---|---|---|---|---|---|
| A. Stills cost 0 credits | 0 | 320 | **320** | 680 | 32 % |
| B. Hypothetical: stills cost 5 each* | 330 | 320 | 650 | 350 | 65 % |
| C. Hypothetical: stills cost 10 each* (as much as a Lite clip) | 660 | 320 | 980 | 20 | 98 % |
| C'. As C, but required stills only (skip Step 1b) | 540 | 320 | 860 | 140 | 86 % |

\* B and C are **what-if scenarios, not Flow prices.** They show why the still price must be known before starting. If stills cost credits, the cheaper path is for the owner to paint or edit the stills by hand and upload them as ingredients (0 Flow credits).

**Headline estimate: 320 credits for clips including one retry each, plus an unknown amount for stills.**

## 4. Rules to stay inside budget
1. **Check the balance** in Flow before starting and write it in the generation log (measured, with date).
2. **One output per prompt.** Multiple outputs multiply the cost (confirm in the UI).
3. **Max two generations per clip** (first take + one retry). After that, use the parallax-still fallback in `CLIP_PROMPTS.md`.
4. **Soft cap for EP001: 400 credits.** At 400, stop and ask the owner before spending more.
5. Generate a cheap test first: **C03 (Lite, 10)** checks that the style frame and prefix give the MOTHWAKE look before any Fast clip is tried.
6. Possible savings: C02 (fog) and C03 (tower blink) are easy to do as parallax stills. Doing them as stills from the start saves 20 credits (40 with retries).

## 5. Unknowns to confirm (owner)
| Question | Status |
|---|---|
| Credit cost of a still image in Flow | Unknown |
| Do unused credits roll over to the next month? | Unknown |
| Do other Google AI tools on the same account draw from the same 1,000 credits? | Unknown |
| Does a failed or blocked generation still cost credits? | Unknown |
| Do Lite/Fast cost the same with Ingredients as without? | Unknown (brief gives one price per model) |
