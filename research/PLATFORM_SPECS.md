# MOTHWAKE: Platform Technical Specs

**Date checked:** 2026-11-19

## Method and confidence

- Direct reads of support.google.com and other hosts were blocked in this container. Values come from **WebSearch results limited to official domains** (quoted snippets).
- Labels: **OFFICIAL** (official page, via search snippet), **SECONDARY** (third-party), **unverified**.
- Where an official value conflicts with a common "cheat sheet" value, the official value is listed and the other marked unverified.

---

## 1. YouTube

### 1.1 Channel branding

| Asset | Spec | Confidence | Source |
|---|---|---|---|
| Banner, recommended | 2560 x 1440 px (16:9) | OFFICIAL | https://support.google.com/youtube/answer/10456525 |
| Banner, minimum | 2048 x 1152 px, 16:9 | OFFICIAL | same |
| Banner, safe area (text/logos) | **1235 x 338 px at the minimum (2048 x 1152) size**, centred | OFFICIAL | same |
| Banner safe area at 2560 x 1440 | 1546 x 423 px is widely quoted | **unverified** (not found on official page). Scaling 1235x338 by 1.25 gives ~1544 x 423, consistent | n/a |
| Banner, file size | 6 MB or smaller; no borders/shadows/frames added | OFFICIAL | same |
| Profile picture | JPG, GIF, BMP or PNG (no animated GIF); renders at 98 x 98 px; **up to 15 MB** | OFFICIAL | https://support.google.com/youtube/answer/10456525 |
| Profile picture, recommended upload size | 800 x 800 px commonly quoted | **unverified** | n/a |
| Video watermark | Square, at least 150 x 150 px, under 1 MB (PNG/GIF/BMP/JPG) | OFFICIAL | https://support.google.com/youtube/answer/10456525 |
| Branding tips | See also | OFFICIAL | https://support.google.com/youtube/answer/12950272 |

### 1.2 Thumbnails

| Item | Spec | Confidence | Source |
|---|---|---|---|
| Recommended resolution (current help page) | **3840 x 2160** for videos; 2160 x 3840 for Shorts | OFFICIAL | https://support.google.com/youtube/answer/72431 |
| Classic recommendation | 1280 x 720 (16:9), min 640 px wide. Google Ads spec page still lists 1280 x 720 recommended / 1280 x 640 min | OFFICIAL (Google Ads page) | https://support.google.com/google-ads/answer/13547298 |
| Minimum width | 640 px | OFFICIAL | 72431 |
| Max file size | **Desktop: 50 MB** (video, Shorts, podcast). **Mobile: 2 MB** video thumbnails (10 MB podcasts) | OFFICIAL | 72431 |
| Formats | JPG, PNG (GIF also listed on some versions) | OFFICIAL | 72431 |
| Eligibility | Custom thumbnails require a verified channel / intermediate features | General knowledge, **unverified** this session | n/a |

**MOTHWAKE recommendation:** master thumbnails at 3840 x 2160 (16:9), keep files under 2 MB versions available for mobile uploads; design text legible at 1280 x 720 and smaller.

### 1.3 Shorts

| Item | Spec | Confidence | Source |
|---|---|---|---|
| Max length | **Up to 3 minutes** (uploads on/after 2024-10-15) | OFFICIAL | https://support.google.com/youtube/answer/15424877 |
| Aspect ratio | **Square or vertical** (taller than wide). Landscape is always long-form | OFFICIAL | same; https://blog.youtube/news-and-events/tall-updates-coming-to-shorts/ |
| Recommended | 9:16, 1080 x 1920 | Common practice; 9:16 not mandated (square allowed) | n/a |
| Max resolution for Shorts upload | 1080p (per help page snippet) | OFFICIAL (snippet; re-check) | https://support.google.com/youtube/answer/12779649 |
| Music | Most licensed tracks up to 90 s in a Short; some limited to 60 or 30 s | OFFICIAL | 15424877 |
| Keep a vertical video out of Shorts | Use a wider ratio such as 16:9 | OFFICIAL | 15424877 |

### 1.4 Long-form upload encoding (OFFICIAL, https://support.google.com/youtube/answer/1722171)

- Container MP4, moov atom at front (Fast Start), no edit lists.
- Video H.264 High profile, progressive, 4:2:0, VBR; frame rate same as recorded (24/25/30/48/50/60).
- Audio AAC-LC or Opus, 48 kHz (96 kHz also accepted), stereo recommended 384 kbps.
- Max file size / duration (256 GB / 12 h) widely quoted: **unverified** this session.

### 1.5 Loudness

- YouTube does **not** publish an official LUFS target in any page found. The commonly quoted **-14 LUFS integrated, -1 dBTP** is from third-party guides: **unverified**.
- **MOTHWAKE working target (estimate, not a platform spec):** -14 LUFS integrated, true peak at or below -1 dBTP, for all platforms; keep horror dynamics (quiet passages) but avoid dialogue below about -24 LUFS short-term (estimate).

---

## 2. TikTok

| Item | Spec | Confidence | Source |
|---|---|---|---|
| In-app length | All creators 3 min; some 5 or 10 min | OFFICIAL (developer/creator docs via search) | https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide |
| Desktop (TikTok Studio) upload | Up to **60 minutes**, 720p or higher, up to 10 GB; landscape or vertical | OFFICIAL (Creator Academy) | https://tiktok.com/creators/creator-portal/en-us/tiktok-content-strategy/creating-videos-longer-than-one-minute |
| API upload | Max 10 min, 4 GB; MP4, WebM, MOV; 360 to 4096 px per side | OFFICIAL | https://developers.tiktok.com/docs/en/content-posting-api-get-started-upload-content |
| Aspect ratio | 9:16 recommended (ads: 9:16, at least 540 x 960) | OFFICIAL (ads docs) | https://ads.tiktok.com/help/article?aid=10002742 |
| Recommended resolution | 1080 x 1920 | Common practice; TikTok says top videos are 720p+ | https://ads.tiktok.com/business/library/7TopCreativeTips.pdf |
| Creator Rewards minimum length | **At least 1 minute** | OFFICIAL | https://www.tiktok.com/legal/page/global/tiktok-creator-rewards-program-eea/en |
| Safe zone | Defined as area not covered by buttons, name, caption, audio; keep text/subtitles/subjects inside. **No official pixel margins published for organic posts**; ad safe zone shrinks with caption length; ad templates downloadable | OFFICIAL definition; pixel values **unverified** | https://www.tiktok.com/creator-academy/article/optimize-video-layout |
| Loudness | No official figure found | **unverified** | n/a |

---

## 3. Instagram Reels

| Item | Spec | Confidence | Source |
|---|---|---|---|
| Length (app) | Clips up to **20 minutes** total; reels over **3 minutes are not recommended to new audiences** | OFFICIAL | https://help.instagram.com/225190788256708 ; https://creators.instagram.com/faq |
| Length (Graph API) | 3 s to 15 min; 300 MB max | OFFICIAL | https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media |
| Aspect ratio | Between 1.91:1 and 9:16; 9:16 recommended to avoid crop | OFFICIAL | https://help.instagram.com/1038071743007909/ |
| Minimum | 30 fps, 720 px | OFFICIAL | same |
| Recommended | 1080 x 1920 | Common practice (Meta cheat sheet) | https://www.facebook.com/fb-answers/social-media-image-sizes-2026/ |
| Cover image | 420 x 654 px (1:1.55) per help page; API recommends 9:16, max 8 MB (conflict) | OFFICIAL (both) | help.instagram.com/1038071743007909 ; Graph API page |
| Safe zone | Meta says keep key messages in the safe zone but gives no pixel margins for organic Reels | pixel values **unverified** | https://www.facebook.com/business/ads/facebook-instagram-reels-ads |
| Loudness | No official figure | **unverified** | n/a |

---

## 4. Facebook Reels and video

| Item | Spec | Confidence | Source |
|---|---|---|---|
| Reels (Reels Publishing API) | MP4, 9:16, 1080 x 1920 recommended, min 540 x 960, 24 to 60 fps, **3 to 90 s**; Reel shared as Page story max 60 s | OFFICIAL | https://developers.facebook.com/documentation/video-api/guides/reels-publishing |
| Reels audio | AAC stereo, 48 kHz, at least 128 kbps | OFFICIAL | same |
| In-app Reels length | Creator guidance: "often 90 seconds or less"; in-app max beyond 90 s **unverified** | OFFICIAL (guidance) | https://creators.facebook.com/blog/how-to-continue-succeeding-with-facebook-on-video |
| Feed video specs | See Meta video requirements chart (max length / file size not captured) | **unverified** values | https://www.facebook.com/business/m/one-sheeters/video-requirements |
| Safe zone | 14% top / 35% bottom is widely quoted; **not found** on Meta pages | **unverified** | n/a |
| Loudness | No official figure | **unverified** | n/a |

---

## 5. MOTHWAKE master deliverable formats (recommendations derived from above)

| Deliverable | Master | Notes |
|---|---|---|
| Long-form episode | 3840 x 2160 or 1920 x 1080, 16:9, H.264 High, AAC-LC 48 kHz 384 kbps, MP4 Fast Start | Landscape keeps it out of Shorts |
| Vertical cut (Shorts / TikTok / Reels / FB Reels) | 1080 x 1920, 9:16, 30 fps (or 24 fps animation conformed), H.264, AAC 48 kHz stereo | 60 to 90 s satisfies TikTok CRP (at least 1 min) and FB Reels API (at most 90 s); under 3 min satisfies Shorts and IG recommendation |
| Vertical safe area (working estimate) | Keep text and faces in the central area, roughly top 15% and bottom 25 to 35% clear, right edge ~15% clear | **Estimate** derived from UI overlays, not an official spec |
| Thumbnail | 3840 x 2160 master, export JPG under 2 MB as well | |
| Banner | 2560 x 1440, all text/logo inside centred 1235 x 338 (at 2048 width) region, scaled; under 6 MB | |
| Profile picture | Square, high-res (e.g., 800 x 800, unverified recommendation), legible at 98 x 98, under 15 MB | |
| Watermark | 150 x 150+ square PNG, under 1 MB | |
| Loudness | -14 LUFS integrated, -1 dBTP (**industry convention, unverified as platform spec**) | |

## 6. Not verified

- YouTube banner safe area at 2560 x 1440 (only the 2048-based value is official).
- YouTube profile picture recommended upload size; long-form max file size/duration.
- Official LUFS targets on any platform.
- Pixel-exact safe zones for TikTok, Instagram Reels, Facebook Reels (organic).
- Facebook in-app Reels maximum length and feed video max file size/length.
