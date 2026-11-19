# MOTHWAKE: Platform Monetization Research

**Date checked:** 2026-11-19 (all entries unless noted)
**Scope:** YouTube, Facebook, Instagram, TikTok. English-language 2D animated horror, AI-assisted production.

## How this was researched (read first)

- Direct page reads (WebFetch/curl) were **blocked** in this container for support.google.com, elevenlabs.io, remotion.dev and most other hosts. Facts below come from **WebSearch results restricted to official domains**, which return quoted snippets of those pages. They were not read in full.
- Confidence labels used:
  - **OFFICIAL**: quoted from an official page (support.google.com, blog.youtube, facebook.com, creators.facebook.com, about.fb.com, help.instagram.com, tiktok.com) in search results.
  - **SECONDARY**: from trade press or third-party guides only.
  - **unverified**: could not be confirmed on an official page.
- Before any decision that costs money or depends on a threshold, open the official URL in a normal browser and re-check it.
- No monetization timeline is promised or implied anywhere in this document. Every threshold is a gate, not a forecast.

---

## 1. YouTube

### 1.1 Five separate stages (do not merge them)

| Stage | What it means | Gate | Source |
|---|---|---|---|
| A. Channel growth | Subscribers, watch hours, Shorts views accumulate | None. Anyone can upload | n/a |
| B. Early YPP access (fan funding) | Can apply to YPP for memberships, Super Chat, Super Stickers, Super Thanks, Shopping. **No ad revenue.** | 500 subs + 3 valid public uploads in last 90 days + (3,000 valid public watch hours in last 12 months **or** 3M valid public Shorts views in last 90 days) | OFFICIAL: https://support.google.com/youtube/answer/72851 ; https://support.google.com/youtube/answer/13429240 ; https://blog.youtube/news-and-events/more-ways-for-creators-to-earn-on-youtube/ |
| C. Ad revenue eligibility (ads + Premium) | Can apply for Watch Page ads, Shorts Feed ads, Premium revenue | **Until 2027-01-31:** 1,000 subs + (4,000 valid public watch hours in 12 months **or** 10M valid public Shorts views in 90 days). **From 2027-02-01 for new applicants:** 1,000 subs + (8,000 qualified watch hours in past 365 days **or** 20M qualified Shorts views in past 90 days) | OFFICIAL: https://support.google.com/youtube/answer/72851 ; https://support.google.com/youtube/answer/12843009 ; https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/ |
| D. Actual revenue | Money accrues only after approval, on eligible (advertiser-friendly, policy-compliant) videos | Human review of the channel; per-video ad suitability; Shorts pool gate from 2027 (below) | OFFICIAL: https://support.google.com/youtube/answer/1311392 |
| E. Payout | Money leaves AdSense for YouTube to your bank | Balance at or above payment threshold (USD 100), tax info, verified payment method, no holds | OFFICIAL: https://support.google.com/adsense/answer/1709871 ; https://support.google.com/youtube/answer/7164703 |

Notes:
- Watch hours and Shorts views **do not combine**. A channel qualifies through one path or the other. (SECONDARY + consistent with OFFICIAL wording "or")
- Meeting a threshold only lets you **apply**. Approval is a review, not automatic. (OFFICIAL, 72851)
- Existing YPP members are **not** affected by the 2027 entry thresholds. (OFFICIAL, 12843009)
- Fan funding thresholds are **not** changed by the 2027 update. (OFFICIAL per search snippet of 12843009; re-check)

### 1.2 The 2027 YPP changes (announced 2026, effective 2027-02-01)

| Change | Detail | Confidence |
|---|---|---|
| New entry thresholds (ads + Premium) | 1,000 subs + 8,000 qualified watch hours / 365 days or 20M qualified Shorts views / 90 days | OFFICIAL (12843009, blog.youtube 2027 post) |
| Shorts Creator Pool monthly gate | To earn Shorts ads and Premium revenue for a given month, channel needs **10M qualified Shorts views in the last 90 days**. Missing it does not remove you from YPP and does not affect long-form earnings | OFFICIAL (12843009, per search snippet) |
| "Active channel" standard | Active if any one: 1,000 qualified watch hours / 365 days, or 1M qualified Shorts views / 90 days, or 2 long-form videos or 5 Shorts uploaded every 90 days. 90-day window to restore status | OFFICIAL (12843009, per search snippet). Consequence of being inactive: unverified |
| Targeted Shorts ads | Ads targeted to 5 or fewer channels pay creators 45% of net revenue from that ad | OFFICIAL (12843009 / blog, per search snippet) |
| Premium Lite | Expanding; creators share a pool of 60% of net Premium Lite subscription revenue | OFFICIAL (12843009 / blog, per search snippet) |
| Terms acceptance | Accept updated terms in YouTube Studio by **2027-01-31** or stop earning from affected features from 2027-02-01 | OFFICIAL (12843009, per search snippet) |
| Announcement date | 2026-08-10 | SECONDARY (newscaststudio.com 2026-08-10, techtimes.com 2026-08-11). Not confirmed on blog itself |

**Implication for MOTHWAKE:** a new channel will almost certainly face the 2027 bar (8,000 hours or 20M Shorts views). A Shorts-only strategy is weak for ad revenue: even after joining, Shorts pool earnings need 10M qualified Shorts views every rolling 90 days. Long-form watch time is the more durable route to ad revenue. This is an interpretation, not a forecast.

### 1.3 Shorts revenue sharing model (OFFICIAL, https://support.google.com/youtube/answer/12504220, checked 2026-11-19)

1. Ad revenue from ads shown between Shorts in the Shorts Feed is pooled monthly (Creator Pool).
2. Part of the pool covers music licensing. Shorts using music send part of their share to licensing. More tracks, larger licensing share.
3. Remaining pool is allocated to monetizing creators by their share of eligible Shorts views (by country).
4. Creator keeps **45%** of their allocated revenue, whether or not music was used.
5. Views that are not "engaged" or that come from inauthentic sources are excluded (detail: unverified).
6. From 2027-02-01, monthly 10M / 90 days gate applies (see 1.2).

Long-form ads: creator share widely reported as 55% (OFFICIAL per blog snippet on Premium distribution "55% for long-form and 45% for Shorts"; the long-form ad share itself was not re-quoted from the YPP terms in this session, so treat 55% for long-form ads as **unverified this session**).

### 1.4 YouTube Premium revenue

| Item | Detail | Source / confidence |
|---|---|---|
| How it works | Premium members' subscription revenue is distributed to creators by how much members watch your content | OFFICIAL: https://support.google.com/youtube/answer/7060016 ; https://support.google.com/youtube/answer/6306276 |
| Eligibility | Part of the ads + Premium tier (stage C). Requires accepting the relevant module | OFFICIAL (72851, 12843009) |
| Pool sizes | Search summary of the 2027 blog post said 30% of net revenue for Premium and 60% for Premium Lite form the creator pools, then creators keep 55% long-form / 45% Shorts of allocation | 60% Premium Lite: OFFICIAL. **30% Premium figure: unverified** (appeared only in an AI search summary) |
| Shorts Premium revenue from 2027 | Subject to the same 10M / 90 days monthly gate | OFFICIAL (12843009) |

### 1.5 Memberships and Super Thanks

| Feature | Requirements | Source |
|---|---|---|
| Channel memberships | In YPP (fan funding tier is enough), creator 18+, lives in an available country, accepted Commerce Product Module, channel not set as Made for Kids and no significant number of MFK videos; music claims can make videos ineligible | OFFICIAL: https://support.google.com/youtube/answer/7636690 ; https://support.google.com/youtube/answer/13195878 |
| Super Thanks | Same baseline. Not available on age-restricted, unlisted, private, MFK, copyright-claimed videos, videos with Giving fundraisers, live/Premiere while live, comments off | OFFICIAL: https://support.google.com/youtube/answer/10879035 ; https://support.google.com/youtube/answer/10878910 |
| Commerce Product Module | Fan funding creators must accept updated module by 2027-01-31 to keep access | OFFICIAL (12843009 per search snippet) |

**Horror-specific risk:** heavily graphic videos may be age-restricted. Age-restricted videos lose Super Thanks and typically have limited ads (ad suitability detail: see YouTube advertiser-friendly guidelines; not re-checked this session, **unverified**). Plan content to stay below age-restriction thresholds: atmosphere and dread over gore.

### 1.6 Payout (AdSense for YouTube)

| Item | Detail | Source |
|---|---|---|
| Account | YouTube earnings go to a separate "AdSense for YouTube" payments account, with its own threshold | OFFICIAL: https://support.google.com/youtube/answer/11602441 |
| Threshold | USD 100 (local equivalents vary) | OFFICIAL: https://support.google.com/adsense/answer/1709871 |
| Timeline | Previous month's finalized earnings posted between the 7th and 12th; payment issued 21st to 26th if balance above threshold and no holds | OFFICIAL: https://support.google.com/youtube/answer/7164703 |
| Requirements | Tax info (incl. US tax info for all creators), verified identity/address (PIN), payment method | OFFICIAL: https://support.google.com/adsense/answer/1709858 ; https://support.google.com/youtube/troubleshooter/1094206 |
| Tax withholding | US withholding may apply to US-viewer earnings depending on tax forms/treaty | OFFICIAL mention; rates **unverified** this session |

### 1.7 Inauthentic, reused, mass-produced content (critical for AI-assisted animation)

OFFICIAL: https://support.google.com/youtube/answer/1311392 (YouTube channel monetization policies), checked 2026-11-19.

- On **2025-07-15**, YouTube renamed "repetitious content" to **"inauthentic content"** and clarified it covers content that is **repetitive or mass-produced**. YouTube states this was always ineligible for monetization.
- Falls under it: AI-generated content made from generic or unoriginal templates, giving the impression of mass production, without the creator's original insights.
- Spam-policy example: channels using the same background music and repetitive AI-generated imagery across many videos, each reading an AI-generated script (https://support.google.com/youtube/answer/2801973).
- Unsatisfying-content example: videos stitching together unrelated or inconsistent AI clips to surprise or shock, without a clear narrative arc.
- Allowed example given by YouTube: using AI to visualize an **original character and narrative**; using AI to edit scripts or generate unique backgrounds that support a unique narrative.
- AI voiceover does not by itself make a channel ineligible, provided monetization policies are met (OFFICIAL community FAQ: https://support.google.com/youtube/community-guide/271248162).
- **Reused content** policy (compilations, clips with little narrative) unchanged in 2025.
- Policy applies at channel level: one review of the whole channel. A pattern of templated videos can sink the application even if individual videos are fine.

**MOTHWAKE guardrails (recommendations):**
1. Every episode is an original story with its own plot arc, recurring original characters, and a human-written script and edit.
2. Vary structure, music, pacing and visuals between episodes. No "same template, new text" output.
3. Keep evidence of human creative work per episode (script drafts, storyboards, edit project files) in `episodes/<id>/`.
4. Do not publish batches of near-identical Shorts. Shorts should be cut with intent, not auto-dumped.
5. Avoid stitched, inconsistent AI clips. Character consistency is a policy issue, not just aesthetics.

### 1.8 AI disclosure (altered or synthetic content)

OFFICIAL: https://support.google.com/youtube/answer/14328491 (now titled "Disclosing use of GenAI content"); https://blog.youtube/news-and-events/disclosing-ai-generated-content/ ; https://support.google.com/youtube/blog/424874071 ; checked 2026-11-19.

- **Must disclose:** realistic content that a viewer could mistake for real: making a real person appear to say/do something, altering footage of real events/places, generating a realistic scene that did not occur; also some realistic synthetic music cases.
- **Exempt:** clearly unrealistic or animated content (YouTube's examples: unicorn in a fantastical world), colour/lighting filters, special effects, production assistance (scripts, captions, upscaling), cloning **your own** voice for voiceover.
- **Labels:** photorealistic AI gets a prominent label (below player for long-form, overlay on Shorts). Unrealistic/animated or slightly altered content: disclosure shown in expanded description.
- **Auto-labelling:** YouTube may apply a label if its systems detect significant photorealistic AI, or if C2PA metadata shows fully generative content, or content made with YouTube's own AI tools. Some labels are permanent.
- Labels alone do **not** affect recommendations or monetization eligibility (OFFICIAL per search snippet).
- Note: Google Flow outputs carry SynthID; whether YouTube reads SynthID to auto-label is **unverified**.

**MOTHWAKE stance (recommendation):** 2D stylised animation is likely exempt, but horror often uses photoreal textures, fake "found footage" or fake news clips. If any shot could be mistaken for real footage, tick the disclosure. When in doubt, disclose. Never depict real people or real events as AI-generated "reality".

---

## 2. Facebook

| Stage | Detail | Source / confidence |
|---|---|---|
| Growth | Facebook Page or professional-mode profile; Reels and long video | n/a |
| Program | **Facebook Content Monetization** (consolidated in-stream ads, Reels ads and performance bonus) | OFFICIAL: https://creators.facebook.com/tools/facebook-content-monetization ; https://creators.facebook.com/introducing-facebook-content-monetization |
| Access | **Invite-only.** Creators can express interest via Professional Dashboard > Monetization (interest form). Older Meta page said open enrollment was "planned"; not confirmed as happened | OFFICIAL (creators.facebook.com) + SECONDARY. Open enrollment: **unverified** |
| Eligibility baseline | Public content surface (Page, professional-mode profile, etc.); reside in an eligible country; linked payout entity in eligible country; comply with Partner Monetization Policies and Content Monetization Policies; 18+ (age detail unverified for this program) | OFFICIAL: https://www.facebook.com/business/help/169845596919485 ; https://www.facebook.com/business/help/1348682518563619 |
| Numeric follower/view thresholds | **No public numeric threshold found** | unverified |
| Countries | No official public country list located. Third-party aggregators claim ~70 countries as of 2026-10-08 and disagree with each other | SECONDARY only; **unverified**. Check Professional Dashboard |
| Creator Fast Track | Launched 2026-03-18. Official page: reside in US, Canada, UK or Australia; linked Instagram/TikTok/YouTube account with at least 20,000 followers and 30,000 video views in last 60 days; FB account 30+ days old; no FB reel in past 6 months; post 15 eligible reels/month on 10 separate days; guaranteed monthly pay for 3 months, then possible move to Content Monetization at Meta's discretion. Brazil added Nov 2026 per press | OFFICIAL: https://creators.facebook.com/creator-fast-track ; https://about.fb.com/news/2026/03/creator-fast-track-grow-your-audience-earn-money-on-facebook/ ; Brazil: SECONDARY |
| Breakthrough bonus | US-only, 18+, Instagram professional account + Facebook Page; leads to Content Monetization invite | OFFICIAL: https://creators.facebook.com/breakthrough-bonus |
| Originality rules | March 2026: re-uploads and low-value edits (borders, captions, speed changes) of others' content are unoriginal; repeat offenders deprioritised, made non-recommendable and demonetised. Content must be created by you or substantially involve you | OFFICIAL: https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/ ; https://creators.facebook.com/blog/combating-unoriginal-content |
| AI labelling | "AI info" label when detected or self-disclosed. Disclosure **required** for organic photorealistic video or realistic audio that was digitally created or altered; penalties possible | OFFICIAL: https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/ ; https://about.fb.com/news/2026/02/meta-prepares-for-2026-us-midterms/ |
| Revenue / payout | Payout thresholds and schedule for Content Monetization | **unverified** this session |

**Note on cross-posting:** reposting your *own* YouTube/TikTok originals to Facebook is allowed under Fast Track if not already on your Facebook Page (OFFICIAL Fast Track page per search). Meta's duplicate detection reduces distribution of copies of *the same video posted multiple times on Facebook*.

---

## 3. Instagram

Instagram has **no general ad revenue share for Reels** comparable to YPP (no official page found describing one; treat as **unverified absence**).

| Tool | Detail | Source / confidence |
|---|---|---|
| Gifts | Professional account, 18+, 500+ followers, eligible country, Gifts Creator Terms, payout account; USD 0.01 per star | OFFICIAL: https://help.instagram.com/738469380549477 (page may be old) |
| Subscriptions | Exists; thresholds not found this session | OFFICIAL page exists: https://help.instagram.com/427415519366046 ; thresholds **unverified** |
| Bonuses | Invite-only; rewards reel/photo performance | OFFICIAL: https://creators.instagram.com/bonuses ; eligibility **unverified** |
| Partner Monetization Policies | Eligible country, authentic established presence, no fake engagement | OFFICIAL: https://www.facebook.com/help/instagram/512371932629820 |
| Payouts | Payout account required; without one, up to USD 500 per tool / 1,500 across 3 tools can accrue; unclaimed earnings can be forfeited after 6 months; most tools pay around 21st for previous month | OFFICIAL: https://help.instagram.com/217939383051653/ |
| Branded content / partnerships | Main realistic revenue route | General knowledge, not re-verified (**unverified**) |
| AI labels | Same Meta "AI info" system as Facebook | OFFICIAL (about.fb.com links above) |

---

## 4. TikTok: Creator Rewards Program

| Item | Detail | Source / confidence |
|---|---|---|
| Account thresholds | 18+, personal (not business) account, **10,000 authentic followers**, **100,000 authentic video views in last 30 days**, account in good standing. Japan/Korea terms: 50,000 followers | OFFICIAL: https://www.tiktok.com/legal/page/global/creator-rewards-program-us/en ; https://www.tiktok.com/legal/page/global/tiktok-creator-rewards-program-jp-kr/en |
| Regions | US, UK, Germany, Japan, South Korea, France, Mexico, Brazil (list may change) | OFFICIAL: https://www.tiktok.com/creator-academy/article/creator-rewards-program |
| Qualifying video | **At least 1 minute long**, at least 1,000 qualified views; not Duets/Stitches, Photo Mode, ads/sponsored | OFFICIAL: https://www.tiktok.com/legal/page/global/tiktok-creator-rewards-program-eea/en |
| Originality | Program rewards original, high-quality content (newsroom). Whether AI-generated content is specifically ineligible: **not found; unverified** | OFFICIAL: https://newsroom.tiktok.com/introducing-the-new-creator-rewards-program?lang=en |
| Payout | Monthly around the 15th once at least USD 50; onboarding incl. tax info | Per search summary of official terms; treat as **verify before relying** |
| AI labelling | Must label AI-generated or significantly edited content showing **realistic** scenes or people; unlabeled may be removed/restricted/labeled. Auto "AI-generated" label for TikTok AI effects or C2PA Content Credentials. Label does not reduce distribution if guidelines met | OFFICIAL: https://www.tiktok.com/community-guidelines/en/integrity-authenticity ; https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content |

**Owner's country matters:** if the owner does not reside in a listed CRP country, TikTok CRP is unavailable regardless of audience. Owner residence is not stated in the brief: **unknown**.

---

## 5. Revenue strategy recommendations (audience first)

These are recommendations, not forecasts. No timeline is implied.

1. **Build for YouTube long-form first.** It is the only platform here with a published, open (non-invite) route to ad revenue. From 2027-02-01 the bar for new channels is 8,000 hours or 20M Shorts views. Long-form episodes (8 to 20 min animated stories) accumulate watch hours; Shorts are discovery, not income.
2. **Treat Shorts, Reels and TikTok as funnels** to the long-form episode, each cut deliberately (hook, standalone payoff, pointer to full episode). TikTok CRP needs videos at least 1 minute long, so 60 to 90 second cuts suit both TikTok CRP and Facebook Reels (90 s API cap).
3. **Plan for fan funding before ads.** The 500-subscriber tier (memberships, Super Thanks) is the earliest YouTube revenue gate and is unchanged in 2027. Requires 3 uploads per 90 days, so keep a steady cadence.
4. **Originality is the main risk.** YouTube "inauthentic content", Meta originality rules and TikTok originality all penalise templated, mass-produced AI output. Invest in recurring original characters, a recognisable visual identity and human-written scripts. Keep production evidence per episode.
5. **Disclose realistic AI.** Stylised 2D is likely exempt on YouTube, but fake found-footage or photoreal shots need disclosure on YouTube, Meta and TikTok.
6. **Keep content below age-restriction level.** Age-restricted videos lose Super Thanks and ad reach. Dread, sound and implication over gore.
7. **Facebook:** apply via the Professional Dashboard interest form; consider Creator Fast Track only after building 20,000+ followers on another platform (and only if resident in an eligible country).
8. **Measure honestly.** Track qualified watch hours and qualified Shorts views in YouTube Studio; never extrapolate earnings.
9. **Accept terms on time.** Any account in YPP by January 2027 must accept the updated terms by 2027-01-31.

## 6. Not verified (open items)

- YouTube long-form ad revenue share percentage (55%) not re-quoted from YPP terms this session.
- Premium creator pool "30% of net revenue": appeared only in an AI search summary.
- Consequences of falling below the YouTube "active channel" standard.
- Facebook Content Monetization: official country list, numeric thresholds, payout threshold, current invite/open status.
- Instagram Subscriptions and Bonuses thresholds; whether any Reels revenue share exists.
- TikTok: whether AI-generated content is excluded from Creator Rewards; exact payout minimum per region.
- Owner's country of residence (determines TikTok CRP, Facebook, Fast Track eligibility).
