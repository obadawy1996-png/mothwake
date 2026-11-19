#!/usr/bin/env python3
"""Create MOTHWAKE project skills (.claude/skills/<name>/SKILL.md) and agents (.claude/agents/<name>.md).

Never overwrites: an existing file is reported and skipped. Everything stays inside the project.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SK = ROOT / ".claude/skills"
AG = ROOT / ".claude/agents"

COMMON = """
## Always
- Run `.venv/bin/python scripts/verify_isolation.py verify` first; stop on failure.
- Never spend paid credits, publish, or change accounts without the owner's explicit approval.
- Never fabricate data. Label numbers measured (source+date) / estimate / unknown.
- Stories are original fiction; never copy another creator's scripts, characters, scenes or style.
"""

SKILLS = {
 "mothwake-brand-development": ("Apply and evolve the MOTHWAKE brand: positioning, voice, palette, typography, brand pillars. Use when writing brand copy or judging if content is on-brand.",
   "Read brand/BRAND_GUIDELINES.md, COLOR_TYPOGRAPHY_GUIDE.md, CHANNEL_COPY.md.\n1. Check copy against voice rules (quiet, precise, no exclamation marks, no fake 'true story').\n2. Check visuals against palette/contrast table.\n3. Brand changes = proposal + owner approval + `scripts/brand_validator.py lock`."),
 "mothwake-logo-and-visual-identity": ("Generate or export MOTHWAKE logos, banner, profile, watermark, end cards from the master geometry. Use for any logo/kit asset work.",
   "Rebuild: `.venv/bin/python scripts/brand/build_brand.py` then `scripts/brand/build_kit.py`; test with `tests/test_brand.py`.\nNever hand-edit exported files; change geometry in build_brand.py only. Respect LOGO_USAGE_GUIDE.md misuse list."),
 "horror-market-research": ("Research competitor horror/mystery channels with public data only. Use to refresh research/COMPETITOR_DATABASE.csv.",
   "Run `research/collectors/yt_public_collector.py` then `build_competitor_csv.py`. Every metric needs source + as-of date; unknown stays `unknown`. Never present third-party earnings estimates as income. Compare channels by tier (small/new, riser, benchmark)."),
 "horror-trend-intelligence": ("Produce the weekly trend report and update research/TREND_DATABASE.csv. Use every Monday or before choosing topics.",
   "Each row: source, date, evidence, confidence, direction, saturation, opportunity, brand_fit, data_type. Split regions US/UK/CA/AU when data allows. Only adapt trends that fit the brand. Write research/WEEKLY_TREND_REPORT.md."),
 "viral-hook-analysis": ("Write and evaluate hooks and score story concepts with the 12-criterion model. Use before a concept is approved.",
   "Write ≥5 hooks using varied structures (impossible situation, disturbing discovery, mysterious rule, unexpected visitor, strange message, dangerous decision, question with visual answer). Check duplicates: `scripts/story/storydb.py hooks <id>`. Score per stories/SCORING_MODEL.md — a prioritisation aid, never a prediction."),
 "horror-story-development": ("Develop original story concepts into full story-database entries. Use when creating or revising concepts.",
   "Fill every field (concept, hook, characters, setting, conflict, escalation, reveal, ending, emotional objective, visual requirements, effort, twist_type, originality review). Gate with `scripts/story/storydb.py check <file>`; similarity ≥0.45 is blocked. Import with `storydb.py import`."),
 "horror-scriptwriting": ("Write Shorts (35–60 s) and long-form (8–14 min) scripts from approved concepts.",
   "Shorts: hook line + first visual in ≤1.5 s, new information every 3–6 s, payoff in final 5 s, loop-friendly last line, ~150–165 wpm.\nLong-form: cold open ≤60 s, title card, 3 acts, set-up/payoff for the twist, no padding. Save to episodes/<id>/script.md with timing column. No real-world claims."),
 "horror-storyboard-generation": ("Turn a script into a shot list/storyboard with layers, camera moves and timing for the assembler.",
   "Per shot: duration, framing, layers (bg/far/mid/near/fg/fx with depth), move (push/drift/pan), lighting preset (ENVIRONMENT_BIBLE L1–L5), caption + key word, sfx cues. Output episodes/<id>/storyboard.md and the `shots` array of manifest.json."),
 "2d-character-consistency": ("Enforce character consistency across generated and drawn shots. Use before any character art enters an episode.",
   "Compare each shot with production/CHARACTER_BIBLE.md sheet: silhouette, proportions, palette, accent colour, Lamp eye highlight. Reject mismatches. Record approved reference hashes in the manifest. Only approved references (max 3 per Flow clip) may be used as ingredients."),
 "2d-environment-design": ("Design layered, reusable backgrounds and lighting per the Environment Bible.",
   "Build 4–6 parallax layers; one motivated warm light; ≥3 dressing variants per background; store in production/backgrounds/<id>/ with layer JSON."),
 "google-flow-production": ("Prepare manual Google Flow generations (no API): ingredient packs, prompts, export checklist.",
   "Flow has no public API — Claude prepares prompts + up to 3 reference ingredients per clip; the owner generates in the browser and drops exports into episodes/<id>/art/flow/. Record model, credits used, date in the manifest. Verify commercial-use terms on the owner's plan before publishing (unverified as of 2026-11-19). Outputs carry SynthID."),
 "elevenlabs-audio-production": ("Plan and produce narration, character voices and SFX with ElevenLabs — only on an approved commercial plan.",
   "Estimate credits first; get approval; free plan is non-commercial. Voice IDs come from the account, logged in the manifest. Deliver WAV to episodes/<id>/audio/. Follow brand/SOUND_IDENTITY.md narration direction."),
 "horror-video-assembly": ("Assemble an episode from its manifest into a clean master and platform exports.",
   "`.venv/bin/python scripts/production/assemble.py episodes/<id>/manifest.json` — refuses to render if the brand validator fails. Long-to-short cut-downs/captions: OpusClip (paid plan, owner approval), then re-run QC. Resolve Free hand-off via FCPXML/OTIO (no scripting in Free)."),
 "ffmpeg-media-processing": ("Encode, trim, loudness-normalise, reframe and inspect media with FFmpeg.",
   "Delivery: H.264 yuv420p, AAC 192k, 30 fps, -14 LUFS / TP ≤ -1 (convention — platforms don't document a target). Measure with `ebur128`; detect black/freeze with `blackdetect`/`freezedetect`. Never overwrite masters."),
 "thumbnail-and-title-optimization": ("Create thumbnails and titles that make a question, per the thumbnail system.",
   "`scripts/brand/thumbnail.py --layout watcher|light|split|rule`. ≤4 words; title + thumbnail together form a question; plain-sentence titles perform for new-wave channels (research). Make A/B variants for long-form. No misleading imagery."),
 "horror-quality-control": ("Run automated QC on rendered episodes and block anything failing.",
   "`.venv/bin/python scripts/production/qc.py episodes/<id>/manifest.json` → QC_REPORT.md. Blocking: brand assets, licence ledger, resolution/codec/fps, duration target, loudness, true peak. Human approval is always required before publishing."),
 "youtube-analytics": ("Ingest real performance data and analyse it against cohorts. Use after each publishing cycle.",
   "Only real data: YouTube Studio CSV exports or authorised API/connectors. Load with `scripts/analytics/ingest.py`; build dashboard `scripts/analytics/dashboard.py`. Compare within format/duration cohorts; never against one outlier. Log learnings in analytics/LEARNING_LOG.md."),
 "youtube-monetization-analysis": ("Track monetization eligibility and revenue across platforms; distinguish growth, early access, ad eligibility, revenue, payout.",
   "Use research/PLATFORM_MONETIZATION.md (re-verify figures before decisions). Note the 2027-02-01 YPP change for new channels. Never promise timelines; revenue only from real reports."),
}

AGENTS = {
 "trend-research-agent": ("Finds rising/evergreen/seasonal horror topics weekly", ["horror-trend-intelligence"], "research/TREND_DATABASE.csv, WEEKLY_TREND_REPORT.md", "Creative Director"),
 "competitor-intelligence-agent": ("Maintains the competitor database from public data", ["horror-market-research"], "research/COMPETITOR_DATABASE.csv, MARKET_OPPORTUNITY_REPORT.md", "Viral Content Analyst"),
 "viral-content-analyst": ("Scores concepts and hooks; flags saturation and policy risk", ["viral-hook-analysis"], "scores in stories/concepts/*.json", "Creative Director"),
 "creative-director": ("Selects concepts, guards brand and originality, approves internal stages before owner review", ["mothwake-brand-development", "horror-story-development"], "stories/ status, episodes/<id>/manifest.json approvals.concept (proposal only)", "Storywriter"),
 "storywriter": ("Writes scripts from approved concepts", ["horror-scriptwriting"], "episodes/<id>/script.md", "Storyboard Designer"),
 "storyboard-designer": ("Builds shot lists and manifest shots", ["horror-storyboard-generation"], "episodes/<id>/storyboard.md, manifest shots", "Character Consistency Supervisor"),
 "character-consistency-supervisor": ("Approves character/environment references and rejects drift", ["2d-character-consistency", "2d-environment-design"], "production/characters, production/backgrounds", "Visual Production Agent"),
 "visual-production-agent": ("Prepares Flow ingredient packs/prompts and layered art", ["google-flow-production", "2d-environment-design"], "episodes/<id>/art/", "Video Assembly Agent"),
 "voice-and-sound-agent": ("Narration, voices, SFX, music licensing ledger", ["elevenlabs-audio-production"], "episodes/<id>/audio/, licence_ledger", "Video Assembly Agent"),
 "video-assembly-agent": ("Renders master and platform exports", ["horror-video-assembly", "ffmpeg-media-processing", "mothwake-logo-and-visual-identity"], "episodes/<id>/master, exports", "Quality Control Agent"),
 "quality-control-agent": ("Runs QC and blocks failures", ["horror-quality-control"], "episodes/<id>/QC_REPORT.md", "Thumbnail and Packaging Agent"),
 "thumbnail-and-packaging-agent": ("Thumbnails, titles, descriptions, platform captions", ["thumbnail-and-title-optimization"], "episodes/<id>/package/", "Owner (approval)"),
 "youtube-analytics-agent": ("Ingests real data, cohort analysis, learning log", ["youtube-analytics"], "analytics/", "Creative Director"),
 "revenue-and-monetization-analyst": ("Eligibility tracking and revenue strategy", ["youtube-monetization-analysis"], "analytics/MONETIZATION_TRACKER.md", "Owner"),
}


def write(p: Path, text: str, created: list, skipped: list):
    if p.exists():
        skipped.append(str(p.relative_to(ROOT)))
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    created.append(str(p.relative_to(ROOT)))


def main():
    created, skipped = [], []
    for name, (desc, body) in SKILLS.items():
        write(SK / name / "SKILL.md", f"---\nname: {name}\ndescription: {desc}\n---\n\n# {name}\n\n{body}\n{COMMON}",
              created, skipped)
    for name, (role, skills, owns, handoff) in AGENTS.items():
        text = (f"---\nname: {name}\ndescription: MOTHWAKE {role.lower()}. Use for this step of the MOTHWAKE pipeline.\n---\n\n"
                f"You are the MOTHWAKE {name.replace('-', ' ').title()}.\n\n**Role:** {role}.\n\n"
                f"**Skills to load:** {', '.join(skills)} (in .claude/skills/).\n\n**Owns (writes only):** {owns}.\n\n"
                f"**Input:** the episode manifest (`episodes/<id>/manifest.json`) and outputs of the previous step.\n\n"
                f"**Hand-off:** update `manifest.json` → `pipeline.<step>.status = done`, list output files, notes, then hand to **{handoff}**.\n"
                f"Never edit files owned by another agent; raise issues in `manifest.json` → `issues`.\n{COMMON}")
        write(AG / f"{name}.md", text, created, skipped)
    print(f"created {len(created)}; skipped existing {len(skipped)}: {skipped}")


if __name__ == "__main__":
    main()
