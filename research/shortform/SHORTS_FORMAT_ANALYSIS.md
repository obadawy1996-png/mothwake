# MOTHWAKE: Short-form format analysis (20–45 s animated micro horror)

**Checked:** 2026-11-19 (UTC). **Scope:** English animated horror Shorts in the three pilot pillars: Micro Horror Stories (50%), Horror Rules & Survival (30%) and Interactive Choices (20%).
**Data files (all in `research/shortform/`):** `SHORTS_COMPETITORS.csv` (47 rows: 43 core, 4 flagged contrast or adjacent), `GOOGLE_TRENDS.csv` (320 rows), `YT_AUTOCOMPLETE.csv` (328 rows), `YT_SEED_SHORTS.csv` (240 rows). Raw snapshots are in `raw/` and collectors in `collectors/`.

> **How to read the numbers**
> - **Measured** means a figure read from a public YouTube or Google Trends page today. "RSS" values are **exact** view and like counts from YouTube's public channel feed. It covers each channel's last 15 uploads. "Rounded" values are YouTube's own display rounding ("1.4M").
> - **Google Trends** values are relative, not volumes. To compare terms across groups, I divide each term by the term "analog horror" (which sits in every group). The result is written as *×anchor*.
> - **Not measured:** retention, swipe-away rate, CTR, traffic sources and revenue. These need a channel's own YouTube Studio.
> - **Not watched:** no video was played (thumbnails and playback were not available), so visual style, narration and sound come from titles, descriptions and About text only. Claims about "what works" are **inference**.
> - Nothing here promises results.

---

## 1. Key measured signals

| # | Signal | Value | Source row |
|---|---|---|---|
| S1 | Search interest, YouTube, US, 12 months (×anchor "analog horror" = 1.0) | backrooms 4.07 · skinwalker 0.455 · horror shorts 0.213 · horror animation 0.097 · sleep paralysis 0.079 · liminal space 0.075 · pick a door 0.065 · christmas horror 0.048 · mimic horror 0.021 · two sentence horror 0.015 · **horror rules 0.010** · winter horror 0.005 · would you rather horror ≈0 · creepypasta animation ≈0 · scary story animation ≈0 · survival scenario ≈0 | `GOOGLE_TRENDS.csv` (geo=US, property=youtube, timeframe=today 12-m) |
| S2 | Christmas horror seasonality, YouTube US | Weekly index ~2 from Jan to Oct 2026. Peaked at **27** in the week of 2025-12-21. Now 4 → 5 → 6 (Nov 2026, still rising) | `raw/gtrends_multiline_2026-11-19.json` (group 2, US, youtube, 12-m) |
| S3 | Momentum (last 4 weeks ÷ prior 4), YouTube US | skinwalker 1.25 (last 3 weeks 43, 42, 44 vs 24–34 earlier) · christmas horror 1.40 · horror shorts 1.14 (GB 1.27, CA 1.50, AU 1.32) · backrooms 0.84 · analog horror 0.85 | `GOOGLE_TRENDS.csv` |
| S4 | Rising related queries, YouTube US | sleep paralysis: "how to date a sleep paralysis demon" (Breakout), "sleep paralysis demon game" (+500%). backrooms: "captain clark backrooms" (Breakout), "backrooms trailer 2026" (Breakout). two sentence horror: "worst two sentence horror stories" (Breakout). analog horror: "the cat in the hat analog horror" (Breakout). horror rules: "campus rules horror", "the rules thai horror" (both Breakout). | `GOOGLE_TRENDS.csv` column `rising_related_US_12m` |
| S5 | Shorts shelf, top-10 median views by seed (relevance order, any upload date, rounded) | backrooms animation 1.19M · which door would you choose scary 381.5K · horror shorts animated 362K · sleep paralysis animation 301K · pick a door horror 220K · liminal space horror 196K · two sentence horror animated 183.5K · would you survive horror 83K · analog horror 78.5K · creepypasta animation 56.5K · scary rules shorts 55K · skinwalker animation 40.5K · what would you do horror 30.5K · horror rules 30K · night shift rules 16.5K · mimic horror animation 15.5K · winter horror story 8.9K · if your mom says goodnight twice 6.5K · would you rather horror 2.3K · knocking at night 1.4K · micro horror 648 · christmas horror animation 101 | `raw/seed_summary_2026-11-19.json`, `YT_SEED_SHORTS.csv` |
| S6 | Autocomplete confirms domestic-rules demand | "if your mom" → "says goodnight twice", "calls you at 3am (don't answer)", "smiles at your doorbell". "horror rules" → "shorts", "to survive", "job", **"ai drama", "ai"**. "which door would you" → "choose backrooms / scary / horror / liminal spaces". | `YT_AUTOCOMPLETE.csv` |
| S7 | Title-feature outlier rate (share of Shorts at ≥3× their own channel's median; baseline **9.2%**, n=476 Shorts, 39 channels) | family member 21.7% (n=23) · question mark 21.1% (n=76) · door 18.8% (n=69) · emoji 17.6% · survival word 14.8% · explicit choice 14.6% (n=89) · ellipsis 10.9% · "Part N" 9.1% · rule word 7.1% · conditional "If..." 6.4% · **time words (3AM/midnight) 2.0%** (n=50) · **"never/don't" 1.4%** (n=74) · analog-horror tag 0% | `raw/title_feature_lift_2026-11-19.json` |
| S8 | Median lift per title feature | ~1.0 for every feature | same file. Titles alone do not move the typical Short; they only change how often outliers happen. |
| S9 | Duration across 34 core channels with a measured Short length | median **57.5 s**, range 12–132 s. Only 13 of 34 are ≤45 s. | `SHORTS_COMPETITORS.csv` `typical_duration_s` |
| S10 | Duration vs lift | n=64 Shorts. ≤20 s: 33% outliers (n=6). 21–45 s: 8% (n=13). 46–60 s: 17%. 61–90 s: 15%. 91 s+: 20%. **Inconclusive** (sample too small). | computed 2026-11-19 from RSS + detail pages |
| S11 | Subscribers per 1,000 lifetime views | Shorts-led channels (≥80% Shorts in RSS): median **2.73** (n=28 core channels; 2.63 with n=39 incl. off-niche). Long-form-led risers from the earlier research: median **12.95** (n=10) | `raw/yt_channels_rss_2026-11-19.json`. `../raw/yt_channels_2026-11-19*.json` |

---

## 2. What works, by pillar

### 2.1 Micro Horror Stories (50% of pilot)

| Element | Evidence (measured) | Inference for MOTHWAKE |
|---|---|---|
| **Hook (first second)** | Biggest outliers open on a calm caption over a wrong image: LIGHTS ARE OFF "I think it's safe to swim here" **55,906,277** views (RSS), 15 s, published 2025-05-16. UnwholesomePenguin "Not my dad" 9.5M (rounded), ~18–22 s, hand-drawn. Family-member titles have a 21.7% outlier rate (S7). | Open on the *finished wrong image*, not on a set-up. The first frame should already be uncanny. A plain, calm caption beats shouting. |
| **Duration** | Pure-twist micro horror runs shortest: LIGHTS ARE OFF 15 s, UnwholesomePenguin median 22.5 s, ParaHaunt median 32 s (n=4), Darkbox 54.5 s. | 20–35 s suits single-reveal micro stories. |
| **Visual complexity** | Top performers are either high-craft 3D (LIGHTS ARE OFF, which states "No AI was used") or one-artist hand-drawn (UnwholesomePenguin, "all made by me"). **Not watched**, from About/descriptions only. | One strong illustrated frame with limited animation is a credible budget. Craft shows in the reveal frame. |
| **Narration** | Unknown for most (not viewed). Darkbox Silent Horror is silent by design (2.01M subs, motion comic). | Test silent + caption against narrated. Silent versions also travel across languages. |
| **Endings / loop** | Two-sentence twist format: rising query "worst two sentence horror stories" (Breakout, S4), shelf median 183.5K (S5). | End on the twist frame, cut hard, and make the last frame lead back into the first (loop). |
| **Topics with signal** | Sleep paralysis: web interest 14.5×anchor US, YouTube 0.079×. Shelf median 301K. Patrick Foxy sleep-paralysis Short **520,590** views, 16 s, published 2026-11-06 (`YT_SEED_SHORTS.csv`). Winter/Christmas: S2 seasonality, and the "christmas horror animation" shelf median is only 101, so supply is thin. Hollow Hours "My Grandma Had ONE Rule About the Wendigo Every Winter…" **34,449**, 20 s, 2026-11-09. | Sleep and waking horror is MOTHWAKE's core theme and has measured demand. Christmas originals have a clear window (post by early to mid December, peak in the week of Dec 21). |

### 2.2 Horror Rules & Survival (30%)

| Element | Evidence (measured) | Inference |
|---|---|---|
| **Search vs feed** | "horror rules" is only 0.010×anchor on YouTube search (S1). Yet rules channels reach six figures: Secret Zone RSS median **74,455** (154K subs, 15 Shorts 2026-10-31..11-18). INSTITUTE 19 median **37,375** (6.76K subs). Liminal Lands median 189,175. | Rules Shorts are found through the **feed**, not search. Write titles for curiosity in the feed, not for keywords. |
| **Hook** | Strongest titles are an "If [ordinary domestic event]…" premise: Secret Zone "If your dog ever starts barking at your mom…" 657K (rounded); Lullorin long-form "If Your Mom Ever Says Goodnight to You Twice… LOCK YOUR DOOR" 3.3M (earlier research). The conditional "If…" alone does **not** raise outlier odds (6.4% vs 9.2% baseline, S7). | Novelty comes from the *premise* (an everyday thing made wrong), not the "If…" template. |
| **Weak crutches** | "3AM/midnight" titles: 2.0% outlier rate (n=50). "Never/Don't" titles: 1.4% (n=74). 3 AM Rules (joined 2026-11-03) RSS median **1,539**. The "if you hear knocking at night" shelf median is 1.4K. | Avoid the 3AM and "DON'T" crutches. They are saturated. |
| **Saturation (measured)** | Lullorin's title has been copied at least **4 times within 3 weeks**: Hushorin 8,394 (2026-11-03), Apexvids 4,480 (11-08), The Fourth Knock 1,091 (11-10), IN THIS WORLD 17,115 (11-13) (`YT_SEED_SHORTS.csv`, seed "if your mom says goodnight twice"). Job/night-shift rules: RULES OF FEAR median 5,173. Night Shift Tales stopped after 13 uploads. Horror Bytes posts at volume (431 videos) with an RSS median of **35**. | Copying a viral rules template underperforms. Night-shift job rules are the most crowded sub-format. |
| **Duration** | Rules Shorts run long: RULES OF FEAR 126 s, Last Instructions 121 s, Liminal Lands 61.5 s, Secret Zone 65 s, INSTITUTE 19 40 s. | 3–5 rules will not fit in 45 s. Use **one rule + one consequence** per Short, and a numbered series ("Rule 4 of the Wake"). |
| **World-building** | INSTITUTE 19 numbers its objects ("Object 19-004. Medical block. Rule 1.") inside an original fictional institute. Secret Zone frames posts as "Recovered tapes. Survival protocols." | A recurring in-world source (a MOTHWAKE rulebook or broadcast) builds series identity without copying titles. |

### 2.3 Interactive Choices (20%)

| Element | Evidence (measured) | Inference |
|---|---|---|
| **Hook** | Ticking binary dilemma in the title: Everdust "The roof is lifting… hide in the bathtub or drive away?" **298,823** and "One Mom is in the closet, one is at the door… which Mom do you trust?" **297,566** (both 2026-11-17, channel joined 2026-10-05, 2.13K subs). WhatWouldYouDo "Open the door... or trust the vents?" **143,026** (2026-11-13, channel joined 2026-11-13). Question-mark titles 21.1% outliers; explicit-choice titles 14.6% (S7). | State the choice in the title *and* in the first frame. Use a concrete stake, not "what would you do?". |
| **Serialisation** | TRZ_FTB (joined 2026-09-30) RSS median **104,786**, all "Part N" with a choice. SimplyPyro (joined 2026-11-11) "They Laughed at My Bunker… Now They Want In" **1,586,444** (published 2026-11-13) and "Bunker Part 3". You Decide Stories: "Comment your choice, and the majority decides the next part". Its 12 s Short reached **27,627** on a 195-sub channel. | The comment vote is the engine: it gives people a reason to comment *and* to come back. "Part N" alone does not raise outlier odds (9.1%). The vote has to matter. |
| **Pick-a-door** | Grim Tales "Pick A Door 4" **289,585** (2026-01-19, 2.17K subs). Liminal Static "Pick a Path" **1,410,086** (2026-02-08). But Internet Nightmares, a pick-a-door channel with 57.4K subs, had an RSS median of only **1,767** in Oct 2026, and Liminal Static stopped on 2026-03-08. Google's top related queries for "pick a door" are lock-picking (S4), so search intent is ambiguous. | Pick-a-door peaked in early 2026 and shows fatigue. Use it sparingly, with an original world. |
| **Weak** | "would you rather horror": shelf median 2.3K, Trends ≈0. "survival scenario horror animation": shelf median 178. | Skip these as framings. |
| **Duration** | Interactive Shorts run 60–120 s (Everdust 80 s, WhatWouldYouDo 117 s, unfixed 99.5 s, Liminal Static 94.5 s). The fastest is You Decide Stories at 12 s. | A 30–45 s choice Short is shorter than the field. That is untested, so measure completion rate. |
| **Comment bait** | Comment counts: Liminal Static 666 on 393,187 views; UnwholesomePenguin 15,738 on 9.6M. Nightline Horror uses "Subscribe if you Won". | Ask a real question with two defensible answers. Avoid "subscribe if…" bait. It is low-trust, and it may conflict with YouTube's spam and engagement rules (not verified this session). |

---

## 3. Saturation by pillar (measured indicators)

| Pillar | Indicators | Verdict |
|---|---|---|
| Micro Horror (generic "scary story animation") | Trends ≈0×anchor. The generic animated-horror space is led by Hindi/Bengali channels (earlier research). Darkbox 2.01M subs, RSS median 26,581. | **Crowded** generically. **Open** for sleep/waking, winter originals and silent visual twists. |
| Rules & Survival | Copycats of the Lullorin title at 1K–17K. 3AM and "DON'T" crutches below baseline. Night-shift sub-genre: many channels under 10K median. Autocomplete shows "horror rules ai". | **High saturation** in templates. Original-world rules (INSTITUTE 19, Secret Zone) still perform. |
| Interactive | Channels joined Sep–Nov 2026 already at 100K+ medians (TRZ_FTB, WhatWouldYouDo, Everdust, SimplyPyro). Pick-a-door is declining (Internet Nightmares, Liminal Static). | **Growing fast** and early. It will fill within months (inference). |

---

## 4. Policy risk (inauthentic / mass-produced content)

| Risk | Evidence | Status |
|---|---|---|
| YouTube "inauthentic content" monetization rule (renamed from "repetitious", 2025-07-15). It targets mass-produced or templated uploads and is enforced at **channel level**. | Earlier research (`../PLATFORM_MONETIZATION.md`, `../MARKET_OPPORTUNITY_REPORT.md`). A July 2026 update was reported by Tubefilter (2026-07-13) and Android Headlines: monetization removed from repetitive AI-generated videos, "distressing or emotionally manipulative" clips, and synthetic personas on sensitive topics. | **Reported, from search snippets.** tubefilter.com was blocked for direct reading this session. |
| Scale of the AI-slop problem in Shorts | Neal Mohan's January 2026 letter is reported to have said 1 in 5 Shorts recommended to new users was low-quality, mass-produced AI content (web search summary, figures vary by outlet). Reported terminations of 16 channels (35M subs combined). | **Reported, approximate.** |
| Template signals seen in this dataset | VONNshorts puts "In This Town, If…" on every title and states "I make AI short videos" (RSS median 17,809). Dark_Liminal repeats "Which door did you pick?" word for word. Horror Bytes has 431 videos with a median of 35. | These are the patterns the policy describes. Avoid them. |
| Reused content | Disturbia Files and The Face of Horror repost TikTok clips "with credit" (descriptions). Couple of horrorz adapts Reddit users' two-sentence stories. ParaHaunt animates other creators' creatures. | Original stories only (CLAUDE.md rule). |
| Real tragedies as "choices" | Everdust dramatizes the 2011 Joplin tornado as a "FICTION" choice game. | Sensitivity risk. Do not use real disasters. |

**MOTHWAKE safeguards for 30 Shorts:** every Short gets a unique premise, a unique title structure (no single template on more than about 1 in 5 titles), its own art and its own edit. Space uploads rather than batch-dumping them. Disclose AI assistance as YouTube requires. Keep a per-Short rights log.

---

## 5. What not to copy

1. Exact viral title templates: "If your mom ever says goodnight twice…", "Which door did you pick?", "In This Town, if…".
2. Third-party IP: Backrooms entities, SCP, Doctor Nowhere and Trevor Henderson creatures, FNAF, Poppy Playtime, the "Cat in the Hat" analog-horror wave (Breakout in S4).
3. Reddit or TikTok adaptations and reposts.
4. Real disasters or crimes as choice games.
5. Skinwalker and wendigo: they are rising (S3), but culturally sensitive. The earlier research already advised avoiding them.
6. "3AM" and "DON'T" as default hooks (S7).

---

## 6. Meta (Facebook / Instagram) data: what was and was not accessible

| Attempt (2026-11-19) | Result |
|---|---|
| `curl` instagram.com/explore/tags/horrorshorts, instagram.com/reels, facebook.com/reel, facebook.com/hashtag/horrorstories, threads.net search, facebook.com/ads/library, tiktok.com/tag/horrorrules | **All blocked** at this session's network proxy (`CONNECT tunnel failed, response 403`). No Meta or TikTok data was obtained. |
| Meta Ad Library | Covers ads, not organic Reels. It is not a demand signal for this question, and it was also blocked. |

**What would give real Meta data (none used; all need owner action):**
- **Own-account Insights** (Instagram Professional or Facebook Page, in Meta Business Suite): free and native, once MOTHWAKE accounts exist. These are the only reliable reach and retention numbers for Reels.
- **Metricool or Supermetrics connectors:** available in this workspace, but they are paid or credit-bearing. **Not called**, per instructions. They read only connected own accounts, after the owner approves.
- **Instagram Graph API hashtag search:** needs a Business account plus a Meta app with review. From Meta's developer docs as I remember them, it is capped at 30 unique hashtags per 7 days. **Not re-checked this session.**
- **Meta Content Library / API:** public-content research access through Meta's Research Tools Manager, vetted by ICPSR (Univ. of Michigan), with review in about 4–6 weeks (Meta and SOMAR pages via web search, 2026-11-19). It is meant for qualifying research. A commercial brand is unlikely to be eligible (my inference).
- **Monetization context (secondary, unverified):** guides report Facebook Content Monetization needs 5,000 followers plus 60,000 minutes in 60 days, and that Reels under 90 s do not count toward in-stream ad minutes (socialbee, fluxnote via search). TikTok Creator Rewards needs videos of **at least 1 minute** (`../PLATFORM_MONETIZATION.md`), so 20–45 s cuts earn nothing there.

---

## 7. Data-driven topic & format ranking for the 30-Short pilot

Scoring is ordinal and transparent. Each topic gets **+** or **–** on four measured signals:
- **D:** search demand (S1, S4).
- **P:** proven Shorts views (S5 and the measured examples).
- **M:** momentum (S2, S3).
- **Sat:** saturation (sections 2–3).

"Fit" is MOTHWAKE brand fit (judgement). The ranking orders *what to test first*. It is not a forecast.

### 7.1 Micro Horror Stories (15 Shorts)

| Rank | Topic / hook | D | P | M | Sat | Fit | Evidence (row) | Pilot slots |
|---|---|---|---|---|---|---|---|---|
| 1 | **Sleep / waking wrongness** (sleep paralysis, the bed, the night light). Open on the wrong image. | + (web 14.5×, YT 0.079×) | + (shelf 301K; Patrick Foxy 520,590, 2026-11-06) | + (rising "sleep paralysis demon" +70%, game +500%) | medium | core | GOOGLE_TRENDS.csv sleep paralysis rows. YT_SEED_SHORTS.csv seed "sleep paralysis animation" | 5 |
| 2 | **Winter / Christmas originals** (original creature, no Santa IP) | + seasonal (peak 27 vs ~2 baseline) | + (LIGHTS ARE OFF santa Short 228M rounded; Hollow Hours winter rule 34,449, 2026-11-09) | + (christmas horror 1.40, ramping) | **low** (shelf median 101) | strong | GOOGLE_TRENDS.csv christmas horror. SHORTS_COMPETITORS.csv LIGHTS ARE OFF | 4, all live by about 2026-12-14 |
| 3 | **Family / imposter micro twist** ("that isn't Mom"), told as a 2-sentence story | – (mimic 0.021×) | + (family-word outlier rate 21.7%; You Decide Stories 27,627 on 195 subs) | n/a | medium | strong | title_feature_lift. YT_SEED_SHORTS.csv | 3 |
| 4 | **Silent visual twist** (no narration, one caption) | n/a | + (LIGHTS ARE OFF 55.9M, 15 s; Darkbox format) | n/a | medium | good | SHORTS_COMPETITORS.csv | 2 (also a test of narration vs silent) |
| 5 | **Liminal aesthetic, no Backrooms IP** | + (backrooms 4.07×, but driven by IP and film) | + (shelf 1.19M backrooms, 196K liminal) | – (backrooms 0.84) | high + IP | medium | GOOGLE_TRENDS.csv backrooms rising "captain clark" | 1 |
| – | Skinwalker / wendigo | + | + | + (1.25) | high | **avoid** (cultural) | GOOGLE_TRENDS.csv skinwalker | 0 |

### 7.2 Horror Rules & Survival (9 Shorts)

| Rank | Format | Evidence (row) | Pilot slots |
|---|---|---|---|
| 1 | **Original-world protocol rule**: one rule, one consequence, numbered inside a MOTHWAKE source (a broadcast or rulebook). Premise is an everyday domestic object made wrong. | Secret Zone median 74,455. INSTITUTE 19 median 37,375. Liminal Lands median 189,175 (SHORTS_COMPETITORS.csv). Autocomplete domestic variants (YT_AUTOCOMPLETE.csv "if your mom"). | 5 |
| 2 | **Family-member rule** with an original twist (not "goodnight twice") | Family outlier rate 21.7%. The Lullorin title is proven but already copied 4× at 1K–17K (YT_SEED_SHORTS.csv). | 3 |
| 3 | **Survival scenario as first-person conflict** ("They laughed at my bunker…") | SimplyPyro 1,586,444 (RSS 2026-11-13). Survival-word outlier rate 14.8%. | 1 |
| – | Night-shift job rules, 3AM rules, "DON'T" hooks | RULES OF FEAR median 5,173; 3 AM Rules 1,539; Horror Bytes 35; time-word outlier rate 2.0% | 0 |

### 7.3 Interactive Choices (6 Shorts)

| Rank | Format | Evidence (row) | Pilot slots |
|---|---|---|---|
| 1 | **Ticking binary dilemma + "comment A or B"**, where the majority decides the next part (2 arcs × 2 parts, with the payoff in Part 2) | Everdust 298,823 / 297,566. WhatWouldYouDo 143,026. TRZ_FTB median 104,786. Question-mark outlier rate 21.1%. You Decide Stories' majority-vote mechanic. | 4 |
| 2 | **Pick-a-door in the MOTHWAKE world** (two lit doors, moth motif) | Grim Tales 289,585. Liminal Static 1.41M. Fatigue signals (Internet Nightmares 1,767). | 2 |
| – | "Would you rather horror", "survival scenario" framing | Shelf medians 2.3K and 178. Trends ≈0. | 0 |

### 7.4 Format defaults for the pilot (from the signals above)

| Parameter | Default | Basis |
|---|---|---|
| Length | Micro 20–35 s. Rules 30–45 s. Interactive 35–45 s. | S9/S10: the field runs longer (median 57.5 s). Shorter is untested, so log completion rate per Short. |
| First frame | The wrong image or the dilemma, already on screen at 0 s | Outliers listed in §2 |
| Title | Calm, specific, one premise. A question mark for choices. No 3AM/DON'T crutch. No single template on more than ~20% of titles. | S7, §4 |
| Ending | Micro: twist frame that loops. Rules: consequence plus rule number. Interactive: hard stop on the choice and the vote prompt. | §2 |
| Series identity | "Rule N of the Wake" numbering plus two-part choice arcs | INSTITUTE 19, TRZ_FTB, You Decide Stories |
| Measurement | Studio: viewed vs swiped away, average % viewed, subs per Short, comments per 1K views | Not measurable from public data |

---

## 8. Limits
- One snapshot (2026-11-19). Search results are not geo-controlled. The Shorts shelf is relevance-ordered and mixes upload years.
- YouTube served full Short pages for only part of the requests, then returned its bot-check page. I stopped collecting rather than work around it. As a result, durations exist for 34 of 43 core channels, and exact views on seed Shorts for 88 of 240.
- Title-feature analysis covers 476 Shorts and 39 channels. It shows correlation, not causation. Channels with different audiences are pooled.
- "Not viewed" columns (visuals, narration, sound) need a human pass. The owner should watch the top 2 Shorts of 10 core channels before scripting.
