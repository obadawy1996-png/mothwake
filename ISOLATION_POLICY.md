# MOTHWAKE Isolation Policy

**Status:** Implemented and tested (2026-11-19)
**Verifier:** `.venv/bin/python scripts/verify_isolation.py verify`
**Negative tests:** `bash tests/test_isolation.sh`

MOTHWAKE is an independent brand. It shares nothing with Chrono Tales Cinema: no files, configuration, skills, agents, pipelines, environments or assets.

## 1. Boundaries

| Area | Rule |
|---|---|
| Project root | Everything MOTHWAKE lives under `/home/user/mothwake`. |
| Python | Only the project venv `/home/user/mothwake/.venv` is used. No `pip install` into system or user site-packages. |
| Node | If needed later, dependencies go in a `package.json` inside the project, never `npm -g`. |
| Claude skills and agents | Only `mothwake/.claude/skills` and `mothwake/.claude/agents`. Nothing under `~/.claude/skills` or `~/.claude/agents`. |
| Claude settings | Only `mothwake/.claude/settings.json`. It denies edits to `/root/.claude/**` and defines no hooks. |
| Chrono Tales | Never read for reuse, edited, moved, copied, or referenced by MOTHWAKE files. Its assets are not used without your explicit written permission. |
| Account-level plugins | MOTHWAKE never installs, removes or toggles plugins. Plugin settings are yours to change. |
| Paid services | No paid credits are used and nothing is published without your approval, given each time. |

## 2. What the verifier checks

1. The project root is `/home/user/mothwake`.
2. The project venv exists and the verifier is running from it.
3. No symlink inside the project points outside it.
4. Project `.claude/settings.json` defines no hooks.
5. No MOTHWAKE skill or agent exists in user-level Claude config.
6. No project file mentions Chrono Tales. Policy docs, reports and plans are exempt because they describe the boundary.
7. Every protected location has the same SHA-256 fingerprint as in `.isolation/baseline.json`. Protected locations are any Chrono Tales path on this machine plus user-level Claude config.
8. No new Chrono Tales location has appeared since the baseline was recorded.

The verifier only reads files outside the project. It writes only `.isolation/baseline.json`.

## 3. Negative tests (all must pass)

| Injected violation | Expected |
|---|---|
| Altered fingerprint in a copy of the baseline | FAIL |
| A Chrono Tales folder appearing after the baseline | FAIL |
| A symlink from the project to `/etc` | FAIL |
| A project file that references Chrono Tales | FAIL |
| Running with system Python instead of the venv | FAIL |
| Clean project before and after | PASS |

Latest run: 7 passed, 0 failed.

## 4. Current state of this machine (audit 2026-11-19)

- No Chrono Tales files exist in this container. The `chrono-tales-production` plugin was disabled before this session started and is not loaded.
- Plugins still loaded account-wide: `postiz` (social scheduling) and `claude-automation-recommender`. Neither defines hooks that run here. MOTHWAKE will not use `postiz` to publish without your approval.
- If you turn the Chrono Tales plugin back on, its asset-guard hook will fire in MOTHWAKE sessions again. Keep it off for MOTHWAKE work.

## 5. When to re-run

- At the start of every phase and every session.
- Before any render or export (the brand-asset validator will call it).
- After any dependency install.

If any check fails, work stops and the failure is reported to you. A new baseline is recorded only after you have reviewed what changed.

## 6. Persistence warning

This cloud container is temporary. Until the project is pushed to a GitHub repository you own, the work exists only here and will be lost when the container is reclaimed.
