# MOTHWAKE: Content Gap Analysis

**As of:** 2026-11-19. Evidence IDs refer to rows in `TREND_DATABASE.csv` and `COMPETITOR_DATABASE.csv`.
**Method:** A gap means **measured low or poor-quality supply** next to **evidence of demand** (a high median nearby, a successful adjacent channel, or press). Confidence reflects how strongly demand is evidenced. Supply alone does not prove demand.

**Measured** means a YouTube public search with the "uploaded this month" filter, sorted by views (top 20), or a channel page. Both were captured on 2026-11-19.

---

## Underserved subjects

| # | Gap | Supply evidence (measured) | Demand evidence | Fit (1–5) | Confidence |
|---|---|---|---|---|---|
| G1 | **English, premium-feeling 2D psychological horror shorts (8–14 min)** | Hindi and Bengali channels lead "animated horror story" and "psychological horror animation". English legacy 2D anthologies are fading (SNARLED recent median ~4.3K on 2.27M subs). Llama Arts has not posted long-form in ~1 year. | Thriller Teller: "WRONG TURN" 10M, recent median ~178K. Animated Horror Flicks ratio 0.40. Surkee ratio 1.10. | 5 | **Medium-high** |
| G2 | **Isolation and emptiness horror in animation** (most current examples are found footage) | Glendale and Kane Pixels are live-action or 3D found footage, not 2D story animation. | Glendale long-form median ~742K (joined 2025-03). Crowmudgeon "The Loneliest World in Analog Horror" 2.2M. | 5 | **Medium-high** |
| G3 | **Original winter and holiday horror (December)** | "christmas horror story" median 8.7K; "analog horror christmas" 201; "winter folklore horror" 263; "krampus story" 484 (results polluted by a game). | Mr. Nightmare "Cold Night" 724K and "Home Alone" 794K (≤8 days). Merrily's "GRYLA, Icelandic Christmas" episode. Press (secondary, unverified): Christmas-horror movie searches in December are more than double 2016. | 5 | **Medium** (December demand not measured yet) |
| G4 | **Serious sleep and waking horror** (sleep paralysis, insomnia, hypnagogia) | "sleep paralysis story" median 24.9K; "insomnia horror" median ~1K; parody, ASMR and romance mixed in. | Film Reflections "The Horror of Not Being Able to Sleep" 805K. "horror stories to fall asleep to" median 222K. Ties directly to the tagline. | 5 | **Medium-low** |
| G5 | **Original animated mysteries with fair-play clues** | "unsolved mystery animated" median ~1.1K (cartoon-lore explainers, not original mysteries). | "missing persons mystery" median 176K. Analysis channels (Nexpo 4.01M, Crowmudgeon) show appetite for decoding. | 4 | **Medium-low** |
| G6 | **The moth and light motif** | "moth horror" median ~1.9K; only a few moth-themed videos (one 52K rules video; a Silent Hill 2026 film clip, 122K). | Indirect only: atmospheric, insect and creature folklore does well (Just a Rock in Space). | 5 | **Low** (demand unproven; this is a brand asset rather than a search gap) |
| G7 | **Coastal, maritime and British-Isles folk horror** | "lighthouse keeper horror" median ~3.4K; British folk horror series under 5K. | "deep sea horror" median 288K (17/20 over 100K). Flannan Isles mystery video 62K. | 4 | **Low-medium** |
| G8 | **Fictional Appalachian and mountain-hollow mysteries (animated)** | Current hits are narration or investigations, not animation. | "appalachian horror stories" median 250K; "Crole Clan" 1.54M. | 4 | **Medium** |
| G9 | **Calm long-form "stories to stay asleep to" built from your own episodes** | "snowed in horror story" median 5K; long sleep-story formats are rare in English animation. | "horror stories to fall asleep to" median 222K. | 4 | **Medium-low** |

## Underserved formats

| Format | Evidence | Confidence |
|---|---|---|
| **Seasons with a light overarching arc** (standalone episodes linked by recurring symbols) | GREYLOCK: 121K subs from 12 tapes. White Stag: 38.2K from 5 videos. Glendale serial logs. All measured. | Medium |
| **Shorts as teasers cut from original episodes** | Shorts medians: ParaHaunt ~689K, Stretch ~333K, Liminal Static ~253K. SCP Shorts ~4× long-form. | Medium |
| **Analog devices inside 2D animation** (tapes, broadcasts, voicemails as in-world clues) | Analog horror median 775K. "emergency broadcast horror" has low supply (median ~6K). | Medium-low |
| **Lore depth that analysis channels can cover** | soda girl (ratio 2.40), Crowmudgeon (1.56) and Nexpo (0.56) build big audiences analysing other people's series. | Medium |

## Not gaps (avoid or deprioritise)

| Area | Why | Evidence |
|---|---|---|
| "N TRUE horror stories ANIMATED" compilations | Saturated; new entrants get little reach. | Views/subs 0.01–0.17 for GRD, SSS, Lele Hill, Urban Legends Animated, DarkAce |
| Skinwalker and wendigo | Saturated (skinwalker median 621K is led by pranks and non-fiction), plus cultural-appropriation risk | TREND rows "Skinwalker", "Wendigo" |
| Japanese urban-legend retellings | Covered by many channels | Merrily, Nightmare Tales, Bixu, MrUnnerving, Snarled |
| Backrooms, SCP, Trevor Henderson creatures, famous children's IP | Not our IP. Rights and originality risk. | ParaHaunt, Kris Archives, Stretch, XBackroom |
| Generic "rules" channel identity | Flooded long tail of tiny channels | Channel search: 11 of 20 channels ≤133 subs, plus 3 with no count shown |
| Game-trend horror (The Classrooms, Roblox mimic) | Streamer-dominated, not narrative | "the classrooms game" median 1.85M (streams) |

## Next checks to raise confidence
1. **December check:** repeat the winter and Christmas scans weekly (`research/collectors/topic_queries_*.txt`) to see whether demand rises with supply.
2. **Google Trends** (US/UK/CA/AU) for "sleep paralysis", "christmas horror", "liminal space", "analog horror", once trends.google.com is reachable.
3. **Reddit** top-of-month in r/nosleep, r/LetsNotMeet and r/analoghorror for theme frequency (read-only, no story adaptation), once reddit.com is reachable.
4. **Retention and engagement** benchmarks via the YouTube Data API (likes and comments per view) for the riser cohort.
