# EP001 — Flow export checklist (owner)

For the owner, who generates in Flow in their own browser. Claude does not log in, generate or download.

## Before you start (once per session)
- [ ] Owner has approved spending credits for this session (how many: ____).
- [ ] Flow balance checked and written in the log: ____ credits on ____ (date). This is a measured number.
- [ ] Correct Google account (the one you intend to use for MOTHWAKE). Write its label in the log, e.g. `owner-ai-pro` — **not** the email address.
- [ ] Style prefix version in use: v1 (`STYLE_PROMPT.md`).

## 1. Download
- Download the **original** file from Flow (highest quality offered; MP4 for clips, PNG for stills). Do not screen-record. Do not re-encode.
- Download every take you keep, and also note rejected takes in the log (they cost credits too).

## 2. File names and folders
| Type | Path |
|---|---|
| Clips | `episodes/EP001/art/flow/<shot>_<take>.mp4` |
| Reference stills | `episodes/EP001/art/flow/refs/<REF-ID>_v<n>.png` |
| Approved character refs (copy) | `production/characters/<CH-ID>/refs/<REF-ID>_v<n>.png` |

- `<shot>` = the clip ID from `CLIP_PROMPTS.md`: `C01` … `C12`.
- `<take>` = `t01`, `t02` … (two digits, in the order generated).
- Examples: `episodes/EP001/art/flow/C04_t01.mp4`, `episodes/EP001/art/flow/C04_t02.mp4`, `episodes/EP001/art/flow/refs/REF-CH-INES-TURN_v2.png`.
- Upper case IDs, no spaces, no dates in names (dates go in the log).

## 3. Log every generation
Add one row per generation to `episodes/EP001/flow/generation_log.csv` (template provided). Columns:

| Column | Example | Notes |
|---|---|---|
| date | 2026-11-20 | Day generated |
| account | owner-ai-pro | Label only, never the email |
| item | C04 / REF-STYLE-01 | Clip or reference ID |
| take | t01 | |
| model | veo-3.1-fast | or veo-3.1-lite, or the image model Flow shows |
| mode | ingredients | ingredients / text / image |
| ingredients | REF-CH-INES-TURN_v2;REF-CH-INES-HANDS_v1;REF-BG-DINER-INT_v1 | Exact files used |
| style_version | v1 | |
| credits | 20 | **As shown by Flow** (measured). If not shown, write `unknown` |
| balance_after | 860 | As shown by Flow |
| file | episodes/EP001/art/flow/C04_t01.mp4 | Empty if not downloaded |
| sha256 | | `sha256sum <file>` |
| status | kept / rejected | |
| reason | text on apron | Why rejected, or what is good |
| approved_by | owner | For refs and kept clips |

## 4. What goes into the manifest
`episodes/EP001/manifest.json` **does not exist yet** (checked 2026-11-19). When it is created, each kept Flow asset needs an entry like this (field names are a proposal for the Video Assembly step):

```json
{
  "id": "C04_t01",
  "file": "episodes/EP001/art/flow/C04_t01.mp4",
  "source": "google-flow",
  "model": "veo-3.1-fast",
  "mode": "ingredients",
  "ingredients": ["REF-CH-INES-TURN_v2", "REF-CH-INES-HANDS_v1", "REF-BG-DINER-INT_v1"],
  "style_prompt_version": "v1",
  "credits": 20,
  "date": "2026-11-20",
  "account": "owner-ai-pro",
  "sha256": "<hash>",
  "synthid": true,
  "approved_by": "owner",
  "approved_date": "2026-11-20"
}
```
Approved reference stills are recorded the same way (Character Bible: approved references are hashed into the manifest).

## 5. Before anything is published
- [ ] **SynthID:** Flow/Veo outputs carry an invisible SynthID watermark identifying them as AI-generated. Do not try to remove it. Follow each platform's AI-content disclosure rules (e.g. YouTube's altered/synthetic content setting) when uploading.
- [ ] **Commercial-use terms are unverified.** As of 2026-11-19 nobody on this project has checked whether Google's terms for Flow on your plan allow commercial use (monetised YouTube, ads, merch). **Confirm the current terms for your own Google account and plan before publishing anything that contains Flow output**, and note the date and the page you checked in `docs/` or the manifest.
- [ ] No generated text, logos or real brands slipped into a kept frame (scrub through every kept clip).
- [ ] Every kept asset has a log row and a hash.

## 6. Hand-off
When the kept clips and refs are in place and logged, tell the Director; the Video Assembly Agent picks them up from `episodes/EP001/art/flow/` and the manifest.
