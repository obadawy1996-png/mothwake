# MOTHWAKE STUDIO 3.0: Phase 1 workspace and isolation audit

**Date:** 2026-11-20 · **Machine:** the owner's Windows 11 laptop · **Method:** read-only inspection. Nothing was installed, changed or deleted.
**Labels:** IMPLEMENTED · TESTED · PARTIALLY IMPLEMENTED · PLANNED · BLOCKED

## 1. Workspace assessment
| Item | Finding | Source |
|---|---|---|
| Hardware | 7.7 GB RAM; C: has 36.9 GB free; no GPU (Chrono Tales notes say i3, 2 cores) | measured / CT notes |
| Python | 3.12.10, global install. **MOTHWAKE has no venv yet**; `requirements.txt` lists 6 packages | measured |
| Node.js | v26.13.0, npm 11.20.0, global | measured |
| FFmpeg / ffprobe | 9.0.2 (gyan full build), user-scope WinGet. Read-only use is shared safely | measured |
| Git | 2.56 at `C:\Program Files\Git\cmd\git.exe`, signed in to GitHub through Git Credential Manager. Pushes to `obadawy1996-png/mothwake` work | TESTED 2026-11-20 |
| Not installed | Docker, uv, pipx, MediaInfo, Blender, Krita | measured |
| MOTHWAKE project | `C:\DocumentsMOTHWAKE\repo` (git repo, 25+ commits). It acts as **MOTHWAKE_STUDIO/** (see §4) | measured |
| Chrono Tales | `C:\Users\hp\Downloads\ChronoTales_V2` (+ `OMAR_STUDIO\`), its own `CLAUDE.md` and `.claude\` | measured, read only |

## 2. Isolation verification (Chrono Tales protection)
| Check | Result | Status |
|---|---|---|
| Separate directories | MOTHWAKE lives under `C:\DocumentsMOTHWAKE`; Chrono Tales lives under `Downloads\ChronoTales_V2`. Neither is inside the other | PASS |
| Separate Claude project config | MOTHWAKE: `repo\CLAUDE.md` + `repo\.claude\{agents,skills,settings.json}`. Chrono Tales: its own `CLAUDE.md` + `.claude\`. Both are project-scoped | PASS |
| Chrono Tales plugin | `chrono-tales-omar-studio` is enabled only in **Chrono Tales' project** `.claude\settings.json`. It does not load in MOTHWAKE | PASS |
| Global skills, agents, plugins | No `~\.claude\skills` or `~\.claude\agents`; `installed_plugins.json` is empty. Nothing global to collide with | PASS |
| Global `~\.claude\settings.json` | Holds auto-mode notes naming Chrono Tales as the trusted repo. **MOTHWAKE will not edit it.** | PASS (left untouched) |
| Writes into Chrono Tales this session | None. Its lessons were *read* and adapted into MOTHWAKE files (`episodes/PILOT_01/FLOW_SAFETY_NOTES.md`) | PASS |
| Separate memory | MOTHWAKE memory: `~\.claude\projects\C--DocumentsMOTHWAKE\memory\`. Chrono Tales has its own folder | PASS |
| Python environment | Shared **global** Python only. No MOTHWAKE venv yet. Must create `repo\.venv` before installing anything | PLANNED |
| Node packages | Nothing installed for MOTHWAKE. Any future Node tool goes in `repo\node_modules` (local), never `-g` | PLANNED |

### Shared resources that cannot be fully isolated (risks)
| Shared thing | Why it matters | Control |
|---|---|---|
| **Google AI credits (2,150 now)** | One pool for Flow across both projects. Chrono Tales notes set a **floor of 1,366** | Read the balance before and after every batch; stop above the floor |
| ElevenLabs account | Chrono Tales spent credits on the same account | Show estimates before each run (done for Ivy VO: 740) |
| Claude.ai connectors (Canva, ElevenLabs, Notion, Metricool…) | Account-level, visible to both projects | Name MOTHWAKE assets with a `MOTHWAKE` prefix (Flow projects, ElevenLabs flows) |
| Built-in browser profile | Google sign-ins are shared (u/0 Everora Studio, u/1 omar badawy) | Always use Flow at `/u/1/` |
| Global Python and Node | An accidental global `pip install` would touch Chrono Tales tooling | venv only; never `npm -g` |

### Fixes MOTHWAKE needs (its own files only)
1. `repo\CLAUDE.md` and `scripts\verify_isolation.py` were written for the Linux cloud box (`/home/user/mothwake`, `.venv/bin/python`), so the isolation verifier cannot pass on this laptop. **PLANNED:** add a Windows path mode. Doing it now would change the hard-rules file, so it needs the owner's OK.
2. Create `repo\.venv` and install `requirements.txt`. **PLANNED** (major-dependency approval).

**Verdict: safe isolation is achievable and is already in place for config, skills, agents, plugins and memory. The remaining shared pieces (credits, accounts, global runtimes) are controlled by the rules above. No reason to stop.**

## 3. Tools available right now
| Category | Available | Status |
|---|---|---|
| Animation (paid, approved) | Google Flow through the built-in browser (Veo 3.1 Lite 10 / Fast 20 / Omni 1.2 Flash 24; Nano Banana images 0) | TESTED |
| Voice (paid, approved) | ElevenLabs connector (TTS, voice design, SFX, music) | TESTED (Ivy VO) |
| Design | Canva, Figma, Magnific connectors; local brand generators (`scripts/brand/`) | Connected |
| Research | Semrush, Supermetrics connectors; repo collectors (`research/**/collectors`); web search | Connected / IMPLEMENTED |
| Publishing | YouTube Studio in the browser (TESTED: banner, picture, description); Metricool connector (0 networks linked) | PARTIAL |
| Assembly / QC | FFmpeg 9; repo `scripts/production/{assemble,qc}.py` | IMPLEMENTED (Linux-tested; Windows untested) |

## 4. Folder mapping (STUDIO 3.0 layout vs the existing repo)
The brief asks for `MOTHWAKE_STUDIO/`. The existing repo already holds most of it. **Recommendation: keep `C:\DocumentsMOTHWAKE\repo` as MOTHWAKE_STUDIO** (renaming would break the git remote path and memory) and add the missing folders only when they get real content:
| Brief folder | Exists in repo | Action |
|---|---|---|
| research/, brand/, episodes/, analytics/, tests/, reports→documentation/ | yes | keep |
| story_engine/ | `stories/` + `scripts/story/` | keep the names (renaming = churn) |
| characters/, environments/ | `production/CHARACTER_BIBLE.md`, `ENVIRONMENT_BIBLE.md`, `production/characters/` | keep |
| agents/, skills/ | `.claude/agents` (14), `.claude/skills` (19) | keep (that's where Claude Code loads them) |
| tools/ | new: this audit | added |
| assets/, publishing/, quality_control/, logs/, mcp/, automation/, templates/, config/ | partly (`brand/templates`, `config/`) | create when first used (the brief says no empty abstractions) |
