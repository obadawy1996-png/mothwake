# MOTHWAKE: 30-Shorts strategy (data-based)

**Status:** PLANNED, awaiting owner approval. No new video gets produced until it's approved.
**Platforms:** YouTube Shorts, Instagram Reels, Facebook Reels, TikTok (one master, per-platform packaging).
**Evidence labels:** [M] measured (source in brackets) · [E] estimate · [H] hypothesis to test with pilot data.

## 1. Evidence the plan rests on
| # | Finding | Source |
|---|---|---|
| D1 | Pillar medians (views per recent Short): interactive/scenario **165,530**, micro horror **47,564**, interactive **15,558**, rules & survival **5,173** [M] | `research/shortform/SHORTS_COMPETITORS.csv` (47 channels, 2026-11-19) |
| D2 | Title features vs a 9.2% outlier baseline: family word **21.7%**, question mark **21.1%**, door **18.8%**, explicit choice 14.6%; time words (3AM) **2.0%**, "never/don't" **1.4%** [M] | `research/shortform/raw/title_feature_lift_2026-11-19.json` (476 Shorts) |
| D3 | Shelf medians: "which door would you choose" 381.5K, sleep paralysis animation 301K, two-sentence horror 183.5K, horror rules 30K, night-shift rules 16.5K [M] | `research/shortform/raw/seed_summary_2026-11-19.json` |
| D4 | Fresh shelf (2026-11-20): doors 144K–1.8M; template copies ("knock… 7th floor", "two babysitters 😨", "3 AM") **74–2K** [M] | `research/growth_2026-11-20/SEARCH_SNAPSHOT_2026-11-20.md` |
| D5 | Seasonality: Christmas horror momentum 1.40, peaks around 21 Dec; supply is thin (shelf median 101) [M] | `GOOGLE_TRENDS.csv`, SEARCH_SNAPSHOT |
| D6 | Meta: about 1,900 active "scary stories" video ads, mostly AI auto-posting tools; "comment A or B → Part 2" is an app-ad template [M] | Meta Ad Library 2026-11-20 |
| D7 | Shorts-led channels gain **2.73 subscribers per 1,000 views** vs 12.95 for long-form [M] | `SHORTS_VS_LONGFORM.md` |
| D8 | Autocomplete demand: "rain sounds horror story", "babysitter / neighbor horror story animated", "haunted apartment cheap rent", "horror rules to follow", "christmas horror story animated" [M] | `yt_autocomplete_2026-11-20.json` |
| D9 | Our pilot cost (measured): SH012 = 90 Flow (incl. 1 redo) + 313 ElevenLabs; SH019 = 110 Flow + 532 ElevenLabs [M] | `episodes/PILOT_01/CREDIT_BUDGET.md` |
| D10 | Slate audit: highest text similarity 0.23 (gate warns at 0.30); 30/30 unique twists; **but** the Tenant reveal is in 23/30, Theo in 6, the bedroom in 11, and 4 bus stories [M] | audit run 2026-11-20 (`storydb.similarity`) |

**No platform analytics exist yet** (nothing posted). Every platform-behaviour claim for Instagram, Facebook and TikTok is [H] until our own insights arrive.

## 2. The MOTHWAKE signature (what makes us recognisable and not "mass-produced")
1. **The Comfort Turn** (story rule): every Short corrupts something meant to make you feel safe: rain sounds, a nightlight, your door number, snow angels, a streetlamp. It's one idea with endlessly different objects. *Template channels change names; we change the object and the mechanism.*
2. **Vesper Court** (world): one building, one cast (Ivy, Theo, Dot, Jun, the Watcher moth), recurring places. Viewers return for the place. Continuity can't be mass-copied.
3. **The case-stamp card** (visual, second 0–1): a brand-type card naming the object and the night ("I PAUSED THE RAIN. IT STOPPED." / "RULE 3: NEVER TURN ON THE BIG LIGHT"). Same typography every time; a different line every time.
4. **The hidden Watcher moth** (rewatch game): once per Short; pinned comment "Did you spot the moth?".
5. **Palette and light:** ash-violet dark + one lamp-gold light + gold eye highlights. Gold keyword in every caption.
6. **Sound signature:** designed silence before each reveal + original synthesized SFX (no stock, no music under VO). Brand sonic logo only at the end of long-form.

## 3. Anti-repetition rules (to stay clear of YouTube's "inauthentic / repetitive content" policy)
| Rule | Limit across 30 | Why |
|---|---|---|
| Unique premise, main event, twist type, ending | 30/30 unique (twist types already unique, D10) | Policy + brief |
| Text similarity gate (`storydb check`) | every pair < 0.30 (now max 0.23) | D10 |
| Tenant (tall figure) as the reveal | **≤ 10** (now 23 → **re-script 13 threats**: mimic voice, missing time, self/reflection, absence, objects, the building itself) | Same monster = a template feel |
| Theo stories | ≤ 5 (drop SH023) | D10 |
| Any one environment | ≤ 6 (bedroom now 11 → move 5) | D10 |
| Bus stories | ≤ 3 (drop SH017) | D10 |
| Two Shorts in a row | never the same pillar **and** environment | viewer fatigue |
| Hook opening word | not repeated within 3 consecutive Shorts | D10 ("Theo…" ×6) |
| Run time | varied 20–45 s, not one fixed length | brief; D-research S10 inconclusive → test |
| Clips | never reused across Shorts (refs yes, clips no) | policy |
| Scripts | human-directed, written per story; no auto-generated batch scripts | D6 (the auto-tool flood) |

## 4. Portfolio (rebalanced from the 15/9/6 slate using D1–D3)
Brief hypothesis 10/6/5/5/4 → **data-adjusted 10 / 5 / 5 / 5 / 5**: rules down (weakest median, D1), interactive up (strongest, D1/D3/D4).
| Pillar | # | Stories |
|---|---|---|
| Micro Horror | 10 | SH012 Rain Sounds · SH015 Streetlamp · SH005 Last Prescription · SH004 Fridge Letters · SH008 Footprints Ahead · SH002 Nine Snow Angels · SH013 Previous Owners' Advent · SH009 Still Counting · SH007 Pell Moves Out · SH011 Handed to Resident |
| Paranormal Encounters | 5 | SH010 Written From In Here · SH001 Dryer Six · SH018 Whiteout Broadcast · SH014 Request Stop · SH006 Floater |
| Psychological Twists | 5 | SH003 Hold Still · SH026 Kettle in the Glass · SH029 Which Theo? · SH020 Night Safety · **NEW-P1** (to write; must pass the gate) |
| Rules & Survival | 5 | SH019 Nightlight Rules · SH022 How to Survive Sleep Paralysis · SH016 Sixty-Second Light · SH024 When a Moth Lands · SH021 Rule Four |
| Interactive | 5 | SH025 Which Door P1 · SH025 P2 (by vote) · SH028 Pause at Seven Seconds · SH030 Three Moths · SH027 Your Stop Is Closed |
Dropped: SH017 (4th bus story), SH023 (6th Theo story, weakest pillar, child-and-adult contract scenes are a Flow refusal risk).

**Interactive twist vs the app template (D6):** every vote Short plants a **fair clue in the first second** and rewards rewatching (SH025's bike scrape). Generic app votes have no clue.

## 5. 30-day calendar (Day 1 = first approved publish date; proposed Mon 2026-11-24)
| Day | Short | Pillar | Env | Data reason |
|---|---|---|---|---|
| 1 | SH012 Rain Sounds | Micro | bedroom | "rain sounds horror" searched (D8); sleep theme |
| 2 | SH025 Which Door P1 | Interactive | hallway | doors 144K–1.8M (D3, D4) |
| 3 | SH019 Nightlight Rules | Rules | bedroom | family word 21.7% (D2) |
| 4 | SH003 Hold Still | Psych | bedroom/phone | phone-camera everyday object |
| 5 | SH015 Streetlamp | Micro | street | — |
| 6 | SH022 Sleep Paralysis | Rules | bedroom | sleep paralysis 301K (D3) |
| 7 | SH028 Pause at 7 Seconds | Interactive | laundromat | rewatch mechanic |
| — | **48 h / 7 d review of Days 1–3 → adjust weeks 2–4** | | | |
| 8 | SH025 P2 (if votes decide) | Interactive | hallway | |
| 9 | SH005 Last Prescription | Micro | pharmacy | |
| 10 | SH010 Written From In Here | Paranormal | bus | |
| 11 | SH026 Kettle in the Glass | Psych | kitchen | |
| 12 | SH016 Sixty-Second Light | Rules | hallway | |
| 13 | SH001 Dryer Six | Paranormal | laundromat | |
| 14 | SH004 Fridge Letters | Micro | kitchen | |
| 15 | SH008 Footprints Ahead | Micro | winter lane | **winter block starts** (D5) |
| 16 | SH002 Nine Snow Angels | Micro | winter lane | winter |
| 17 | SH018 Whiteout Broadcast | Paranormal | kitchen | winter |
| 18 | SH013 Previous Owners' Advent | Micro | kitchen | Christmas, live before 14 Dec (D5) |
| 19 | SH030 Three Moths | Interactive | winter lane | moth game |
| 20 | SH014 Request Stop | Paranormal | bus | |
| 21 | SH009 Still Counting | Micro | kitchen | |
| 22 | SH029 Which Theo? | Psych | flat | |
| 23 | SH024 When a Moth Lands | Rules | kitchen | |
| 24 | SH006 Floater | Paranormal | street | |
| 25 | SH007 Pell Moves Out | Micro | bedroom | |
| 26 | SH011 Handed to Resident | Micro | bedroom | |
| 27 | SH020 Night Safety | Psych | phone | |
| 28 | SH027 Your Stop Is Closed | Interactive | bus | |
| 29 | NEW-P1 | Psych | tbd | |
| 30 | SH021 Rule Four | Rules | pharmacy | |
(The environment column is provisional: SH-files reassigned during the Tenant/bedroom re-script must keep any one environment ≤ 6.)

## 6. Packaging per Short (rules from D2/D4/D8)
- **Title:** a question or reversal; a family/home/door word where it is true to the story; ≤ 60 characters. Never "TRUE", "3AM", "DON'T", "Nth floor", emoji spam.
- **Cover:** one central figure or object + 2–4 words in Cinzel + one lamp-gold hotspot + the small moth mark.
- **YouTube:** title + 3 hashtags (`#horror #animatedhorror` + topic). Description: hook question / "A MOTHWAKE original fiction story" / moth game line. Pinned comment: the moth question or the A/B question.
- **Instagram Reels:** caption = hook question + "Comment what you'd do"; 5–8 hashtags; cover chosen in-app.
- **Facebook Reels:** the same caption, shorter; 3–5 hashtags.
- **TikTok:** a ≤100-char caption + 3–5 hashtags; captions kept in the raised safe zone (we render at marginV 780).
- One clean master per Short; **no other platform's watermark** on any upload.

## 7. Measuring and deciding (real data only)
At 48 h and 7 d per platform: views, viewed vs swiped (YT), average % viewed, shares, comments/1K views, follows/1K views. Rules (from the pilot plan):
- The pillar that leads on retention **and** shares gets +2 slots in weeks 3–4.
- An interactive Short with enough votes gets Part 2 within 72 h.
- If nothing gets traction by day 7, change ONE variable (hook card style, length, or VO vs silent).
- Never re-plan off a single outlier.

## 8. Capacity and budget (measured costs, D9)
| Resource | Need for 27 more Shorts | Available | Gap / decision |
|---|---|---|---|
| Flow (Veo Lite 10 / Fast 20) | at 5 clips/Short (4 Lite + 1 Fast = 60): **~1,620**; at pilot size (~100): ~2,700 [E] | Flow monthly 1,000 (resets 23 Nov) + AI pool above the Chrono Tales floor (~2,070 − 1,366 ≈ 700) ≈ **1,700** [M/E] | **Use the 5-clip budget rule** to fit, or spread over two Flow months, or the owner adds credits |
| ElevenLabs | ~340/Short measured avg → **~9,200** [E] | Plan balance **unknown** (usage tool lacks permission) | Owner to check the plan |
| Owner time | ~1–1.5 h/Short [E] | — | Batch 7 Shorts per week |
