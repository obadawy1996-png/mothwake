# Short-Form Pilot Plan: 3 fully animated Shorts

**Status: [APPROVAL NEEDED].** Nothing paid is generated until the owner approves this plan.
**Date:** 2026-11-19 · **Engine:** Google Flow (owner's AI Pro) for all animation · **Voice:** ElevenLabs (owner's paid plan) · **Assembly, captions, brand and QC:** MOTHWAKE pipeline.
**Evidence:** `research/shortform/SHORTS_FORMAT_ANALYSIS.md` §7 (rows cited there), `SHORTS_VS_LONGFORM.md`, `GOOGLE_TRENDS.csv`, `YT_SEED_SHORTS.csv`.

## 1. The three pilots (one per pillar), checked against the data

| # | Short | Pillar | Why this one (data) | Data-informed title (test) | Length |
|---|---|---|---|---|---|
| P1 | **SH012 Rain Sounds** | Micro horror | Sleep/waking wrongness is the #1 micro topic. Sleep paralysis web demand is 14.5× analog horror, the top-Shorts median is about 301K, and related queries are rising (GOOGLE_TRENDS.csv). The highest editorial score in the slate. | *Why Did the Rain Keep Playing After I Paused It?* | 32 s |
| P2 | **SH019 Theo's Nightlight Rules** | Rules | It combines the #1 rules format (an original-world rule about an everyday object) with the #2 (a family-member rule). Shorts with a family word broke out 21.7% of the time, against 9.2% for all Shorts. It avoids the 3AM/DON'T framing, which broke out only 1–2% of the time. | *My Little Brother's Nightlight Has 3 Rules* | 36 s |
| P3 | **SH025 Two Nines, restructured as a two-part vote** | Interactive | The #1 interactive format is a binary dilemma that ends on "comment A or B", with the majority deciding Part 2. The fastest new channels use it (Everdust about 299K on 2.1K subscribers; SimplyPyro 1.59M). Titles with a question mark broke out 21.1% of the time; door titles 18.8%. | *Which Door Is Really Mine?* | Part 1: 30 s, hard stop on the vote |

**P3 change:** the slate version reveals the answer in the same video. The data favours ending on the choice, so **Part 1 ends on "A or B? Comment."** A **Part 2** (about 20 s, around 50 Flow credits, an estimate) is made **only if Part 1 gets enough votes to decide**. It's counted outside the 3-video limit, as a follow-up. **[APPROVAL NEEDED]**

**Seasonal follow-up, if the pilot passes:** the Christmas/winter window is under-supplied (the "christmas horror animation" Shorts median is 101 views) and peaks around 21 December (GOOGLE_TRENDS.csv). Queue **SH002 Nine Snow Angels** and **SH013 The Previous Owners' Advent** to go live by about **14 December**.

## 2. Production format (all three)

- **Fully animated:** every shot is a Google Flow clip (Veo 3.1, 4–8 s, one simple action). No still images.
- **Clips:**
  - P1: 5 clips; P2: 5 clips; P3: 4 clips (from each Short's `flow_clips` field)
  - Model: Lite throughout, Fast for the single key moment
- **Consistency:** 5 reference images are made once and reused as Flow Ingredients (Ivy, Theo, the Tenant, the bedroom, the hallway). The owner approves them before any clip.
- **Opening:** the first frame is the wrong image or the dilemma, and the hook line lands within 1 s. No intro and no logo.
- **Sound:** ElevenLabs narration (Chris for the adult narrator voice or Ivy, plus a child voice to be selected for Theo), brand sounds, room tone, and sound effects designed in post.
- **Text** (rule cards, door numbers, the phone screen, captions) is added in post with brand type. None is generated in video.
- **Mobile brand:** the proposed small mark as the top-left watermark, the mobile caption style, a per-pillar cover, and the 1 s end sting, or a loop ending where the story loops (`brand/mobile/`).

## 3. Cost (estimates; nothing spent yet)

| Item | P1 | P2 | P3 (Part 1) | Total | Notes |
|---|---|---|---|---|---|
| Flow clips, first pass | 60 | 60 | 50 | **170** | Lite 10 / Fast 20 per clip (owner brief) |
| Flow clips, one retry each | +60 | +60 | +50 | **340 max** | Of 1,000 per month. Rule: at most 2 tries per clip. |
| Flow reference stills (5) | — | — | — | **unknown** | Check in Flow whether image generation uses credits |
| ElevenLabs narration | about 250 | about 450 | about 230 | **about 930 credits** | About 1 credit per character, as measured on EP001; one take plus small retakes |
| Other tools | 0 | 0 | 0 | 0 | FFmpeg, brand system and QC are in-house |

## 4. Time estimate (to be measured during the pilot)

| Step | Who | Estimate per Short |
|---|---|---|
| Final script, shot list and Flow paste pack | Claude | about 20 min |
| Reference images (once for all 3) | Owner in Flow | about 45 min in total |
| Generate clips in Flow and download | Owner | about 30–45 min |
| Narration, sound, assembly, captions and QC | Claude | about 20–30 min (rendering included) |
| Review and approval | Owner | about 10 min |

**Target:** at most about 1.5 hours of owner time per Short, falling as the reference library grows. Actual times are logged in each episode's `PRODUCTION_LOG.md`.

## 5. How we judge the pilot (real data only)

**Measured per Short at 48 hours and 7 days** (YouTube Studio, and Instagram/TikTok insights if cross-posted):
- viewed vs swiped away
- average % viewed
- views
- subscribers gained per 1,000 views
- comments per 1,000 views (key for P3)
- shares
- returning viewers

**Decision rules (our own working rules, not industry benchmarks):**

| Result | Action |
|---|---|
| A pilot clearly leads the others on viewed-vs-swiped **and** average % viewed | Its pillar gets more of the next 27 slots |
| P3 gets enough comments for a majority | Make Part 2. Test whether two-part arcs bring returning viewers. |
| Cost or time per Short is well over plan | Simplify. Fewer clips, more reuse, or a cheaper model. |
| None get traction after 7 days | Change **one** variable (hook style, length or narration vs silent), not everything at once |

**Most viewed is not most profitable.** Track subscribers per 1,000 views, and how many Shorts viewers go on to watch long-form once that exists. Shorts revenue alone is small (see the recommendation).

## 6. What is needed from the owner

1. Approve this plan, including the P3 two-part structure. **[APPROVAL NEEDED]**
2. Approve the mobile brand proposals in `brand/mobile/`. **[APPROVAL NEEDED]**
3. Check in Flow whether image generation costs credits, and check the commercial-use terms for your Google account.
4. Create the YouTube channel (and optionally Instagram/TikTok). Their insights become the data source for Meta and TikTok, which can't be reached publicly from here.
5. Choose how I can use your Chrome: a shared Remote Control folder (the app needs an update) or a local Claude session.
