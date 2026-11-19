# MOTHWAKE Phase 2: Research Log

**Session date:** 2026-11-19 (UTC). **Researcher:** Claude (subagent).
**Constraints honoured:** no paid connectors used (no Semrush, Supermetrics, Magnific or ElevenLabs calls), nothing published, all files written only under `/home/user/mothwake/research/`. Isolation verifier run at start: 10/10 checks passed.

## 1. Files produced

| File | Contents |
|---|---|
| `COMPETITOR_DATABASE.csv` | 63 channels: 21 small/new, 21 riser, 21 benchmark |
| `TREND_DATABASE.csv` | 42 trend rows: measured, qualitative, or both |
| `MARKET_OPPORTUNITY_REPORT.md`, `CONTENT_GAP_ANALYSIS.md`, `WEEKLY_TREND_REPORT.md` | Synthesis |
| `collectors/yt_public_collector.py` | Re-runnable public-page collector (modes: `channels`, `search`, `topics`) |
| `collectors/build_competitor_csv.py` | Rebuilds the competitor CSV from snapshots plus hand annotations |
| `collectors/handles_2026-11-19*.txt`, `collectors/topic_queries_2026-11-19*.txt` | Inputs for weekly re-runs |
| `raw/yt_channels_2026-11-19{,_b,_c}.json` | Channel snapshots (About, Videos, Popular, Shorts) |
| `raw/yt_channel_search_2026-11-19_{a,b}.json` | YouTube channel-search results (27 queries) |
| `raw/yt_topic_scan_2026-11-19{,_retry,_b}.json` | Topic scans: top-20 videos this month by views (62 query runs) |

**Weekly re-run:**
```
.venv/bin/python research/collectors/yt_public_collector.py channels research/collectors/handles_2026-11-19.txt research/raw/yt_channels_<date>.json
.venv/bin/python research/collectors/yt_public_collector.py topics research/collectors/topic_queries_2026-11-19.txt research/raw/yt_topic_scan_<date>.json
```
Then update `SNAPS` and `AS_OF` in `build_competitor_csv.py` and run it.

## 2. Sources used

### 2.1 Primary (measured), all fetched 2026-11-19 between 17:06 and 17:20 UTC
- **youtube.com channel pages** (`/@handle/about`, `/videos`, `/shorts`, plus the public "Popular" sort continuation via `/youtubei/v1/browse`) for 74 unique handles (63 kept in the database; the rest were off-topic, non-English or mis-guessed handles). Each JSON record carries a `fetched_at` timestamp.
- **youtube.com search results**, channel filter, 27 queries (raw/yt_channel_search_*).
- **youtube.com search results**, video filter "this month", sorted by view count, 62 query runs (raw/yt_topic_scan_*). Six queries returned 0 parsed results on the first run; 3 recovered on retry, and "nosleep story", "two sentence horror" and "reddit horror stories" stayed empty. These are recorded as `unknown`.

### 2.2 Secondary (web search via the WebSearch tool, 2026-11-19). Publication dates as given by the outlet or snippet.

| Topic | Source(s) | Pub. date |
|---|---|---|
| Analog horror scale (500M+ views in a year) | blog.youtube "Signal interrupted, the Analog Horror community..." https://blog.youtube/culture-and-trends/analog-horror-yoodle/ ; Tubefilter https://www.tubefilter.com/2024/10/31/its-an-analog-horror-halloween-on-youtube/ | 2024-10 |
| Theorising and community | Roar News https://roarnews.co.uk/2024/theorising-and-the-rise-of-analogue-horror/ | 2024 |
| Backrooms film box office | Variety AU https://au.variety.com/2026/film/global/backrooms-a24-biggest-movie-domestic-box-office-37270/ ; Fangoria https://www.fangoria.com/backrooms-movie-box-office-opening/ ; tribune.com.pk https://tribune.com.pk/story/2610619/backrooms-becomes-a24s-highest-opening-with-38m-friday-box-office-debut | 2026-05/06; later totals inconsistent ($213M–$400M+), so none are used |
| Iron Lung opening | NBC New York https://www.nbcnewyork.com/entertainment/entertainment-news/markiplier-youtuber-iron-lung-hit/6453897/ ; TheWrap https://www.thewrap.com/creative-content/movies/markiplier-mark-fischbach-iron-lung-interview/ ; Film Stories https://filmstories.co.uk/news/iron-lung-youtuber-auteurs-indie-horror-storms-the-us-box-office/ | 2026-02 |
| Mandela Catalogue film | TheWrap https://www.thewrap.com/creative-content/movies/spielberg-ua-amazon-mgm-nab-youtube-horror-hit-the-mandela-catalogue/ ; Dread Central https://www.dreadcentral.com/box-office/588554/the-mandela-catalogue-movie-sets-june-9-2028-release-date/ | 2026-07 |
| Liminal horror rise | Portside (AV Club reprint) https://portside.org/node/39804/printable/print ; Dread Central top 10 of 2026 https://www.dreadcentral.com/lists/576141/dread-centrals-top-10-horror-movies-of-2026-so-far/ | 2026-06 |
| Inauthentic-content policy | Search Engine Journal https://www.searchenginejournal.com/youtube-monetization-update-spam-not-reaction-channels/550755/ ; PPC Land https://ppc.land/youtube-clarifies-inauthentic-content-policy-changes/ ; Gulf News https://gulfnews.com/technology/youtube-updates-monetisation-policies-ai-and-repetitive-content-ban-begins-july-15-1.500192660 | 2025-07 |
| AI-slop crackdown | Tubefilter https://tubefilter.com/2026/01/29/youtube-ai-slop-channel-crackdown-bans/ ; Tubefilter (policy update) https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/amp/ | 2026-01-29; 2026-07-13 |
| YPP 2027 thresholds | PPC Land https://ppc.land/new-youtube-creators-face-8-000-hour-bar-for-ad-revenue-from-february-2027/ ; Social Media Today https://www.socialmediatoday.com/news/youtube-announces-changes-to-creator-monetization/ ; Hypebot https://www.hypebot.com/hypebot/2026/08/youtube-doubles-watch-hours-for-monetization.html ; Newsshooter https://www.newsshooter.com/2026/08/10/youtube-updates-its-partner-program/ | 2026-08-10/11 |
| Frightgeist 2026 (secondary snippets only) | Search snippets referencing https://blog.google/products-and-platforms/products/search/frightgeist-halloween-trends-2026/ (page blocked) | 2026-10-14 |
| Christmas horror search growth (secondary, unverified) | Haunted Attraction Network https://hauntedattractionnetwork.com/christmas-horror-movies/ ; Dread Central (Comparitech study) https://www.dreadcentral.com/news/419576/ | 2026 / undated |
| Sleep paralysis search claim (unverified) | The Daily Brit https://thedailybrit.co.uk/?p=81222 | date unclear |
| r/nosleep trend (undated) | Daily Dot https://dailydot.com/lifestyle/reddit-r-nosleep-original-horror-stories-nightmares/ | undated |
| ParaHaunt third-party stats (estimate only) | NexLev snippet https://www.nexlev.io/youtube-stats/@parahauntyt (page blocked; values seen only in search summary; not used as fact) | snippet dated 2026-11-15 |
| Snarled / Something Scary history | sponsorradar, findachannel, yidio snippets (third-party; not used for numbers) | various |
| Llama Arts origins | Vietcetera https://vietcetera.com/vn/4-kenh-youtube-cho-tin-do-phim-hoat-hinh-kinh-di ; creatordb snippet | various |

Low-quality sources seen and **not** relied on: dyerbolical.com trend pieces, blogspot "Shorts trends 2026" pages, an alibaba.com product-insights page, and AI-tool marketing pages.

## 3. Blocked or unavailable

| Resource | What happened | Impact |
|---|---|---|
| reddit.com (curl and WebFetch) | Blocked by network policy / "unable to fetch" | No subreddit volume or top-post data. Reddit is covered only by search snippets. |
| Third-party Reddit mirrors | Attempt **denied by the permission classifier**; not pursued further | Same as above |
| trends.google.com (curl and WebFetch) | DNS not allowed | No per-country (US/UK/CA/AU) Trends data |
| socialblade.com, playboard.co | Blocked | No historical subscriber curves, so no growth-inflection analysis |
| support.google.com (YouTube Help) | DNS not allowed | Policy and YPP figures come from press only, not verified at source |
| blog.google, nexlev.io (WebFetch) | DNS not allowed | Frightgeist and NexLev seen only as snippets |
| suggestqueries.google.com / YouTube autocomplete | Blocked | **No YouTube search-suggestion data.** Search-result scans used as a proxy. |
| i.ytimg.com (thumbnails) | Blocked | Thumbnail patterns unknown; title patterns used instead |
| youtube.com/watch pages | Redirect to www.google.com, which is blocked | No likes, comments, exact publish dates or per-video engagement |
| googleapis.com YouTube Data API v3 | 403 (no key) | No official stats, retention or engagement |
| Semrush, Supermetrics (connectors) | Not used, per instruction (paid) | No keyword volumes |

## 4. Connections that would improve the data (in order of value)

1. **YouTube Data API v3 key** (free quota) for exact subscriber counts, per-video views, likes, comments and publish dates. Also allow `www.googleapis.com` in the network policy.
2. **Network access to trends.google.com** for US/UK/CA/AU seasonal curves (winter and Christmas horror, sleep paralysis, liminal).
3. **Network access to reddit.com** (read-only JSON) for theme frequency in r/nosleep, r/creepypasta, r/LetsNotMeet, r/analoghorror and r/shortscarystories.
4. **socialblade.com** for growth curves and case-study inflection points.
5. **suggestqueries.google.com** for YouTube autocomplete (search-suggestion trends).
6. **i.ytimg.com** to view thumbnails for thumbnail-pattern analysis.
7. **support.google.com** to verify YPP and policy text at source before Phase 8.
8. Optional, only with your approval: Semrush keyword volumes (paid credits).

## 5. Method notes and caveats
- `views_to_subs_signal` = median views of the last 10 long-form videos ÷ subscribers. For dormant channels this measures catalogue strength, because old videos have had years to collect views.
- `upload_frequency` counts long-form uploads with a relative date of 90 days or less among the most recent 15 parsed. "15+" means all 15 were within the window. YouTube's relative dates are approximate ("3mo ago").
- The "Popular" sort did not return for some channels. Those rows show the best of the 15 most recent videos and are labelled as such.
- The Dark Somnium's recent-video metadata parsed wrongly (collaboration rows), so its recent views are `unknown`.
- The handle `@TheRuleFiles` was guessed. It is not verified to be the uploader seen in the topic scan.
- Topic scans are single snapshots with no geo control, so "direction" relies on external evidence or is `unknown`.
- Non-English channels seen in searches (Hindi, Bengali, French, Indonesian-run) are used only as market-structure evidence. The database keeps English-titled channels only.
