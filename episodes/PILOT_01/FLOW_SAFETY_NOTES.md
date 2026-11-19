# PILOT_01 — Flow lessons carried over from Chrono Tales / Omar Studio

**Date:** 2026-11-20. Sources (read only, never edited): `C:\Users\hp\Downloads\ChronoTales_V2\OMAR_STUDIO\knowledge\CHRONO_TALES_FLOW_WORKFLOW.md`, `LESSONS_LEARNED_v2.md`, `MEMORY_NOTE_reference_stills_continuity.md`.

## 1. RISK for SH019 (and SH002): child plus adult
On Chrono Tales, Flow **refused**:
- frames or prompts showing a minor and an adult interacting;
- **child image uploads**.

Refusals were not charged. *(Observed on Chrono Tales; not yet tested on MOTHWAKE.)*

Clips this affects:
| Clip | Problem |
|---|---|
| SH019 C2a | Theo counts on his fingers to Ivy (child and adult together) |
| SH019 C2b | Theo holds Ivy's face (child and adult touching) |
| SH019 C3a | A child's hand stops an adult's wrist |
| REF-THEO | If it is uploaded as an image, it may be refused |

**Plan (the Kuleshov approach from the Omar Studio Handbook §11.7):** shoot the child and the adult in **separate** shots, and let the cut create the relationship:
- C2a becomes "Theo alone, counting on his fingers, looking up off-camera" plus "Ivy alone, listening, looking down off-camera".
- C2b becomes "the nightlight flickers" plus "two small hands rise into frame at the bottom edge" (no adult shown) plus "Ivy's face turned, eyes wide".
- C3a becomes "an adult hand at a switch, alone" plus "a small hand reaching up from below, alone".

**Test first at zero credit cost:** generate REF-THEO *inside* Flow with Nano Banana (images showed **0 credits** on 2026-11-20) and see whether Flow accepts it as an ingredient. Don't rewrite any prompt to sneak past a refusal. If the ingredient is refused, write Theo from his text description only.
This is a proposal: the C2a/C2b/C3a rewrites become prompts only after the owner OKs them.

## 2. Reference images are free; use them heavily
- A Nano Banana 2.1 image at ×1 showed **0 credits** in Flow on 2026-11-20 (measured on screen). The REF image cost is no longer unknown.
- Maling lesson: costumes and props drifted between shots that were generated from text only. **Every clip uses its reference ingredients; never text only.**

## 3. Gate before every generation (adapted from the 9-point gate)
1. The right Flow project is open.
2. Ingredients are attached and checked on screen before typing.
3. The prompt is pasted fresh from CLIP_PROMPTS.md.
4. Settings are read on screen: video, model, 9:16, ×1.
5. The credit cost shown fits the budget.
6. Only then click Create.

## 4. After every generation
- Reload the page before downloading; Chrome blocks repeated downloads from one page.
- Copy the file into `episodes/PILOT_01/flow/`, never move or overwrite it.
- Make a contact sheet and check identity, props, light and any text.
- Run hidden-cut QC: scene detection at above 0.25 **and** at 0.05–0.25.

## 5. Sound and post (Lessons v2)
- Use a 4× oversampled limiter at −2 dBFS before AAC encoding (to avoid true-peak overshoot).
- Owner-requested spot effects go on an un-ducked stem.
- `python -E`, not `-I`, when user-site packages are needed. Use long variable names in PowerShell.

## 6. Model and pricing update seen in Omar Studio notes
Omni 1.2 Flash Frames was 24 credits and Veo 3.1 Lite 10 per clip (Maling, 2026-11-18). Flow also now offers Gemini Omni 1.2 Flash. Check the number Flow shows for each clip.
