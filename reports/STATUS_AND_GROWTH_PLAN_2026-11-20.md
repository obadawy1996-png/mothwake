# MOTHWAKE: status report and growth plan (2026-11-20)

Evidence: `research/growth_2026-11-20/` (fresh YouTube + Meta snapshot today), `research/shortform/` (476 Shorts / 47 channels, 2026-11-19), and the competitor studies (`research/competitor_*.md`). Numbers are **measured public counts** unless marked as an estimate. No private analytics exist yet (nothing published).

---
## 1. What we have done

| Area | Done | Status |
|---|---|---|
| Brand | Logo B, colours, fonts, banner, profile picture, watermark, outro, sound identity, channel copy | IMPLEMENTED (approved) |
| YouTube channel | @THEMOTHWAKE: banner, profile picture and description published | DONE (live) |
| Research | Long-form market (63 channels) · Shorts study (47 ch / 476 Shorts / Trends / autocomplete) · niche score 74/100 · tavieenfilm / Money Decoded / Paper Billions study · fresh YouTube + Meta snapshot | DONE |
| Strategy | Short-form first (hybrid), "original horror + real fear science" direction, storytelling framework, 15-stage blueprint | PROPOSED (direction) |
| Studio 3.0 | Phase 1 audit (isolation OK, 25 repos), Phase 2 (venv + faster-whisper / PySceneDetect / OpenCV) | DONE |
| Tools built | QC checker, Flow-clip assembler, two-pass loudness fix, Flow automation helpers | TESTED |
| Pilot production | 9 refs approved · 17 Flow clips (SH012 ×7, SH019 ×10) · Ivy VO ×4 takes · 2 masters | DONE |
| Masters | **SH012 Rain Sounds v5** (28.3 s) · **SH019 Nightlight Rules v7** (34.5 s), both PASS WITH WARNINGS | Owner said "not bad" |
| Spend | Flow: about 160–220 AI credits (button vs balance gap logged) · ElevenLabs 1,012 · image gens 185 | Logged in CREDIT_BUDGET.md |

## 2. What remains

| # | Task | Blocker / owner |
|---|---|---|
| 1 | Apply the **improvements in §4** to SH012 and SH019 (v6/v8) | Your go-ahead (mostly free: re-edit + SFX) |
| 2 | SH025 *Which Door* Part 1: 4 Flow clips (~40 credits) + assembly | Your go-ahead |
| 3 | Covers (thumbnails) + titles + descriptions + hashtags per platform | Can do now (free) |
| 4 | Publish the 3 pilots (YouTube, then FB/IG/TikTok) | **Your approval per post**; FB/IG need linking (Metricool) or manual upload; TikTok account? |
| 5 | Mobile brand proposals (small mark, end sting) | Your approval |
| 6 | Measure at 48 h / 7 d → decide the next 27 | After publishing |
| 7 | Winter/Christmas Shorts live by **about 14 Dec** (SH002 Nine Snow Angels, SH013) | Scripts exist; production after the pilot |
| 8 | Studio 3.0 next phases (Windows CLAUDE.md, KinoCut test, publishing queue) | Your approval |

---
## 3. What the market says today (key findings)

1. **Evergreen winners are craft-heavy and simple:** Crawl Space Clown 10M, "Not my dad" 9.6M, Two Sentence Horror 7.1M, "I Heard It Too" 4.9M. Each has one character, one wrong detail, and one twist.
2. **Template saturation is real.** New uploads that copy a formula ("knocking at my window… I live on the 7th floor", "two babysitters, only one is real 😨", "at 3 AM") sit at **74–2K views**.
3. **Meta is being flooded by automation:** about 1,900 active "scary stories" video ads, mostly AI faceless-video tools promising auto-posting. The "rules + comment A or B" format is now literally an app ad (Norveko). **Generic AI horror is becoming invisible; recognisable craft is the moat.**
4. **Open lanes with demand:**
   - "rain sounds horror" (people search it; nobody makes the rain *itself* the horror). **This is SH012.**
   - "which door would you choose": 144K–1.8M. **This is SH025**, but it needs a twist beyond the template.
   - Sleep paralysis (one 1.9M breakout, then weak supply).
   - Babysitter, neighbour and apartment stories ("haunted apartment cheap rent" appears in autocomplete). **These suit Vesper Court.**
   - Christmas and winter: low supply now, peaking about 21 Dec.

---
## 4. Recommendations to improve OUR videos (concrete, by priority)

### 4.1 Fix the first second (biggest lever)
- **SH012** opens on Ivy calmly asleep. A calm image in a swipe feed is a lost viewer. **New open:** start on C3 (the only wet window on a dry building) or C2a (raindrops frozen mid-air) with the hook line already on screen, then cut back to Ivy. The research rule: "the first frame is already wrong".
- **SH019** opens on the nightlight with *very faint* shadows. **Brighten/contrast the shadow layer** so the tall shadows read at phone size in frame 1, or open on C4 (the crowd) for 0.5 s as a flash-forward, then "Theo has three rules…".
- Add a **1-second text hook card** in brand type on frame 1 ("I paused the rain. It stopped." / "Rule 3: never turn on the big light.").

### 4.2 Sound = feeling (currently the weakest part)
- Right now the bed is only the clips' own room tone. Add designed sound:
  - SH012: a **rain loop that becomes knuckle tapping in the same rhythm** (the story's twist in audio), plus a hard cut to silence on "Pause. Nothing."
  - SH019: **nightlight hum → flicker buzz → dead silence when the big light clicks on**, then one breath when the heads turn.
- Sources: ElevenLabs SFX (paid, approved; small cost) or Freesound **CC0 only**, logged in `assets/ASSET_LICENSE_REGISTER.csv`. **No music** under the narration for Shorts: silence is scarier and avoids licensing issues.
- Leave **0.4–0.8 s of silence before each reveal**. The silence does the work.

### 4.3 Captions
- Keep them big and centred. **Highlight one key word per line in Lamp gold** (e.g. "Only **MY** window was wet"). This helps people watching on mute (most feeds autoplay muted).
- Pull captions out of the lower third where the platform UI covers them on TikTok and Reels (keep them at about 55–70% height).

### 4.4 Endings and rewatch
- Both end well (a loop or a whisper). Make the **loop literal**: SH012's last tapping sound = the first second's rain; SH019's last frame = the first frame's nightlight (already planned; verify on a phone).
- **"Find the moth" easter egg:** the Watcher moth appears once in every Short. Pin a comment: "Did you spot the moth?" That gives viewers a reason to rewatch and to comment, and it's unique to MOTHWAKE.

### 4.5 Titles (keywords that are searched, without the saturated crutches)
| Short | Recommended title (A) | Alternative (B) | Why |
|---|---|---|---|
| SH012 | **I Paused My Rain Sounds. The Rain Outside Stopped.** | Why Did My Rain Sounds Know I Was Awake? | "rain sounds" is searched; reversal; no "3AM/knock" |
| SH019 | **My Little Brother's Nightlight Has 3 Rules** | Never Turn On the Big Light | Family word (21.7% outlier rate) + number |
| SH025 | **Which Door Is Really Mine?** | Two Doors Say 9. Only One Is Mine. | Door + question (18.8% / 21.1%) |
Avoid "TRUE" (they're fiction), "3AM", "DON'T", "7th floor", and emoji spam.

### 4.6 Covers (thumbnails for Shorts and Reels)
Pattern from the winners: **one central figure or object, close; 2–4 word punch line; one hot accent**.
- SH012 cover: the wet window with the tall silhouette's fingers + "IT WAS LIVE" (Old Gold on Obsidian).
- SH019 cover: the crowd of silhouettes facing the moth lamp + "RULE 3".
- SH025 cover: two identical "9" doors, one peephole glowing + "ONLY ONE IS MINE".
- MOTHWAKE's palette is muted, so **give each cover one Lamp-gold hotspot** for contrast. Keep the small moth mark in the corner for brand recall.

### 4.7 Hashtags and descriptions
- YouTube: 3 tags at most: `#horror #animatedhorror #scarystories` plus one topic tag (`#sleepparalysis`, `#horrorrules`, `#whichdoor`). The description opens with the story's question line, then "A MOTHWAKE original fiction story."
- Instagram/Facebook: the caption = the hook question + a "Comment what you'd do 👇" style prompt; 5–8 hashtags.
- TikTok: a short caption, a question, 3–5 hashtags. Native text on the cover.

---
## 5. Being unique (the MOTHWAKE moat)

1. **A recurring world, not one-offs:** Vesper Court (one building, one cast: Ivy, Theo, Dot, Jun, the Tenant, the Watcher moth). Viewers come back for *the place*. Template channels can't copy continuity.
2. **A signature mechanic:** "the comfort object turns": rain sounds, the nightlight, the door number, the snow angels. Every story corrupts something meant to make you feel safe. That's the emotional hook (violated safety), and it's ownable.
3. **A visible craft signal:** consistent hand-drawn style, lamp-gold eye highlights, the moth easter egg, designed sound. Put "A MOTHWAKE story" in every description. *Do not* hide the craft behind generic AI looks.
4. **Interactive, but earned:** keep A/B votes for **one series** (Which Door), with a fair clue planted in the first second (beats the app templates, which have no fair-play clue).
5. **Fear Science long-form (later):** "the story is fiction, the effect is real" Investigations, every 3–4 weeks, to build watch hours.

## 6. Emotions to aim for (per Short)
| Beat | Feeling | Tool |
|---|---|---|
| Frame 1 | Unease ("that's wrong") | A wrong image + calm caption |
| Middle | Recognition ("I do that too": rain sounds, nightlights, door numbers) | Everyday objects, second-person/first-person VO |
| Turn | Dread | Silence, then a single sound |
| End | Gut punch + curiosity | A visual twist, a loop, a CTA question |

## 7. Next steps (ranked by impact ÷ effort)
1. **Re-edit SH012/SH019 with §4.1–4.4** (new first second, SFX, highlighted captions). Low cost: SFX only.
2. **Make the 3 covers + titles + per-platform text** (free).
3. **Produce SH025 Part 1** with a stronger fair-clue twist (~40 Flow credits).
4. **Publish the 3 pilots** across YouTube, then FB/IG (link Metricool or upload manually) and TikTok, on your approval.
5. Measure at 48 h / 7 d; double down on the winner; start the winter Shorts for 14 Dec.
