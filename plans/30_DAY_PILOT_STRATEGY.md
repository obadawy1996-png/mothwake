# 30-Day Pilot Strategy

**Status:** Plan changes APPROVED by owner 2026-11-19 (see `DECISIONS.md`). The start date depends on your approvals and paid-plan decisions (see section 6). Nothing is published without your approval.
**Calendar:** `plans/CONTENT_CALENDAR.csv`, with separate rows per platform.

## 1. Proposed changes to the original brief (your decision)

| Brief said | Research shows | Proposal |
|---|---|---|
| ~30 Shorts | Templated, high-volume AI uploads trigger YouTube's channel-wide "inauthentic content" enforcement. Generic compilations get 0.01–0.17 views per subscriber. | **14 Shorts.** Each is a distinct story or a trailer cut from a long-form story. |
| Long-form 5–10 min | Breakout new-wave channels run about 8–14 min with one clear premise | **8–14 min**, 4 stories |
| Shorts-led growth | From 2027-02-01, Shorts revenue needs 10M Shorts views per 90 days and ad revenue for new channels needs 8,000 hours or 20M Shorts views | **Long-form drives watch hours; Shorts drive discovery** |

## 2. Slate (from the story database; scores are editorial)

| Week | Long-form (8–14 min) | Shorts (35–60 s) |
|---|---|---|
| 1 | **The Quiet Hour** (MW012): establishes the Wrenfield world | Lost Moth Poster (MW003) · Smile Check (MW010) · Quiet Hour trailer · Voicemail From Tomorrow (MW004) |
| 2 | **Winter original:** "The Lamp Census" (from the trend report; to be written). Must be live before 1 Dec if the launch allows. | Extra Floor (MW002) · Night Inventory (MW005) · Lamp Census trailer |
| 3 | **Sleep Study** (MW006) | Babysitter's Third Rule (MW008) · Last Bus to Halden (MW011) · Sleep Study trailer · Mile Marker 0 (MW007) |
| 4 | **Signal Lake** (MW009) | Signal Lake trailer · 2 Shorts chosen from week 1–3 learnings |

MW001 *Porch Light Rule* is held back: research found an existing 2026 video with an overlapping premise, so it needs a rework.

## 3. Controlled experiments (one variable at a time)

| Test | Variable | Held constant | Read-out |
|---|---|---|---|
| E1 (weeks 1–2) | Hook structure: "mysterious rule" vs "impossible situation" | Length (45–55 s), art style, voice | Viewed vs swiped away, average % viewed |
| E2 (weeks 2–3) | Short type: self-contained story vs long-form trailer | Hook type (E1 winner) | Subscribers per 1k views, clicks to related video |
| E3 (long-form) | Thumbnail layout: watcher vs light (YouTube's built-in A/B test) | Title | CTR, average view duration |
| E4 (weeks 3–4) | Long-form length: about 9 min vs about 13 min | Category (psychological) | Average view duration, watch hours, retention curve |

Each comparison is made within its cohort (same format and duration band) using `scripts/analytics/analytics.py cohorts`. No single outlier decides anything.

## 4. Platform plan (one clean master, separate packaging and calendars)

| Platform | What goes there | Cadence | Notes |
|---|---|---|---|
| YouTube | All long-form plus all Shorts | Long-form weekly (Fri), Shorts about every 2 days | Main platform for watch hours. End screens point to related stories. |
| TikTok | The 14 Shorts. Long-form cut into 1–3 min parts | Daily slots, staggered 1 day after YouTube | Creator Rewards pays only on videos of 1 minute or more, is region-limited, and needs 10k followers. Treat it as discovery for now. |
| Instagram Reels | The 14 Shorts | About 4 per week | No platform watermarks. Cover frame from the thumbnail system. |
| Facebook | Shorts as Reels plus long-form as native video | About 3 per week | Content Monetization is invite-only. Express interest through the Professional Dashboard once eligible. |

## 5. Weekly operating rhythm

- **Mon:** trend re-scan (`research/collectors/`) and the weekly trend report.
- **Tue–Wed:** script, storyboard, art.
- **Thu:** voice, assembly, QC, and your review and approval.
- **Fri:** you publish the long-form. Shorts follow the calendar.
- **Sun:** performance review, then the learning log.

## 6. What must be in place before Day 1

1. Your approval of the logo (concept B), the brand kit and this plan.
2. Channels created by you (handles verified by you).
3. Paid plans approved: ElevenLabs Starter or Creator, and Google AI Pro (Flow). OpusClip Starter is optional.
4. A GitHub repository for the project.
5. Analytics access: YouTube Studio exports at minimum.

## 7. Day-30 deliverable

A performance-based recommendation covering:
- what to continue, stop, improve and scale
- which audience segments respond
- whether to refine the direction

Every point must be backed by real cohort data.
