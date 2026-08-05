# Plan 001 — Project Foundation

## Goal

Establish a clean, consistent, fully documented starting point for the repository before further feature work begins:

* Stop version-controlling files that are generated/runtime state rather than authored configuration.
* Create the documentation `CLAUDE.md` and the standards already assume exists (`docs/development/*`, `docs/architecture/decisions/`).
* Bring `CLAUDE.md` and `README.md` in line with the repository as it exists today (after the `docs` → `data` rename and the addition of `docs/architecture/overview.md`).
* Produce a real first-pass roadmap and the first MVP definition so subsequent work has a clear, agreed entry point.

This plan is documentation and repository-hygiene work. No Home Assistant configuration, automation, entity, or physical-device behaviour is changed.

## Assumptions

* "Unrelated files" means tracked files that are either (a) generated/runtime state written by Home Assistant or an integration, or (b) not tied to the project's documented purpose. Concrete candidates are listed below; final confirmation on each is the user's call before anything is untracked.
* Untracking a file (`git rm --cached`) removes it from future version control but leaves the working copy on disk — it is not the same as deleting it.
* README will be rewritten in English per `docs/standards/documentation.md` ("All project documentation is written in English"); the existing Swedish operational steps are relocated, not discarded.
* Three items flagged in `docs/architecture/overview.md` as configuration-level risks — camera credentials in `configuration.yaml`, the empty/unregistered `dashboards/energy.yaml`, and the `themes:` include with no `themes/` directory — are **out of scope** for this plan. They change operational configuration, and `CLAUDE.md` explicitly says not to do that during a documentation-only task.
* Naming: this plan uses sequential numbering (`001-...`) as requested, and the paired MVP file mirrors the same number for traceability, rather than the `mvp-XXX-slug.md` shorthand used as an example in `docs/claude-prompts/2-create-plan-prompt.md`.
* **Git workflow — decided:** this is a solo project (you + Claude Code, no other collaborators), so the project adopts the simple workflow already described in `README.md` — commit and push directly to `main`/`master`. `docs/standards/git.md`'s mandatory branch + pull-request model is replaced, not just relocated. The AI-assistant safety rule ("never commit, push, or reload without explicit approval") stays — that is about safety, not branching.

## Proposed File Changes

### Remove from version control (keep on disk, add/adjust `.gitignore`)

| Path | Why it's confirmed for removal |
| --- | --- |
| `.cache/` (34 tracked integration brand icons) | Already matched by the existing `.cache/` ignore rule — these were tracked before that rule applied. Only needs `git rm -r --cached`. |
| `.ha_run.lock` | Live process PID + start timestamp, rewritten on every HA start. Pure runtime churn, and its `ha_version` field only duplicates `.HA_VERSION` — redundant info we're keeping only in one place. |
| `home-assistant.log.fault` | 0-byte log marker file. Falls outside the existing `*.log` ignore rule only because of the `.fault` suffix. |
| `zigbee.db` | Binary Zigbee network/device-pairing database, same category as the already-ignored `home-assistant_v2.db*`. Confirmed: not needed for this project. |

### Keep as-is (reviewed, not proposed for change)

* `environment.yml` — developer Python environment definition (conda, `python=3.13`, `pytest`); relevant and current.
* `data/*` — inventory exports; already correctly scoped by the prior rename.
* `.HA_VERSION` — kept tracked. Unlike `.ha_run.lock`, this is a low-churn, single-line record of the HA version the config was last known to run against, useful to check at a glance. It becomes the one place that version lives (see `.ha_run.lock` above).

### Add (new documentation)

* `docs/development/setup.md` — desktop ↔ GitHub ↔ Raspberry Pi sync workflow (moved out of README) and the `environment.yml` setup steps.
* `docs/development/tools.md` — required tools: VS Code, Git, SSH, Home Assistant CLI (`ha core check`, `ha core restart`), conda/pytest.
* `docs/development/methodology.md` — the `Requirement → Plan → Implementation → Validation → Review → Commit` flow from `CLAUDE.md`, linking to `docs/claude-prompts/`.
* `docs/architecture/decisions/` — short `README.md` explaining ADR numbering/format; add a first ADR only if a real decision is identified during implementation (candidate: the `docs` → `data` rename).
* `docs/mvp/mvp-001-project-foundation.md` — first MVP definition, scoping this cleanup/documentation effort with acceptance criteria matching the phases below.

### Update (existing files)

* `docs/roadmap.md` — replace placeholder headings with real first-pass content.
* `README.md` — rewrite in English; keep to project purpose and pointers (`CLAUDE.md`, `docs/architecture/overview.md`, `docs/development/setup.md`); remove the relocated operational steps.
* `CLAUDE.md` — update the repository-structure table (e.g. add `data/`), verify the "Read Before Planning" file list now resolves, and simplify the "Git Workflow" summary to match the direct-to-`main` decision (drop the branch-only rule; keep the explicit-approval-before-push/commit rule).
* `docs/standards/git.md` — replace the mandatory branch + pull-request workflow with the simple direct-to-`main` workflow already described in `README.md`. Keep the rules that aren't about branching: commit message style, what must never be committed, explicit-approval-before-push/commit when working with an AI assistant.
* `.gitignore` — add entries for the runtime files confirmed for removal above.
* `docs/architecture/overview.md` — revisit after the above changes land, since it currently documents several of the gaps this plan closes.

## Implementation Phases

### Phase 1 — Untrack unrelated files

1. Add `.gitignore` entries for `.cache/` (already covered, kept for clarity), `.ha_run.lock`, `home-assistant.log.fault`, and `zigbee.db`.
2. `git rm -r --cached .cache .ha_run.lock home-assistant.log.fault zigbee.db`.
3. Verify `git status` / diff is limited to these removals and nothing else, and that `.HA_VERSION` remains tracked.

**Suggested commit message:** `Stop tracking generated and runtime state files`

**Status: done.** Committed as `phase 1 of our plan 1` (`e654fb1`) and pushed to `origin/main`.

**Incident during rollout (2026-08-05):** pulling this commit onto the live Home Assistant Raspberry Pi deleted `zigbee.db` from disk, since `git pull` applies a tracked→removed file as an actual working-tree deletion, not just an index change (unlike `git rm --cached` on the desktop, which only untracks while leaving the file in place). This is different from `.cache/*`, `.ha_run.lock`, and `home-assistant.log.fault`, which are all safely regenerated by Home Assistant and needed no recovery.

Recovered by: `git reflog` → `git reset --hard <pre-pull commit>` on the HA machine to restore the file, then re-syncing safely: back up `zigbee.db` (an HA Backup, plus a copy into the already-gitignored `backups/` folder) *before* pulling, let the pull delete the tracked copy, then restore it from the backup copy — after which it stays in place permanently since it now matches `.gitignore`.

**Lesson for future work:** before ever pushing a change that removes a *live, non-regenerable* file from git tracking (a database, credential file, or similar — not a cache/log/lock file), the rollout to any machine where that file is live must be: back up the file independently → pull/apply → restore from backup. This should be captured in `docs/development/setup.md` (Phase 2) as part of the sync workflow.

### Phase 2 — Development documentation

1. Create `docs/development/setup.md`.
2. Create `docs/development/tools.md`.
3. Create `docs/development/methodology.md`.

**Suggested commit message:** `Add development workflow and tooling documentation`

**Status: done.** All three files created with real content (not placeholders): `setup.md` includes the safe-rollout procedure from the Phase 1 incident above; `tools.md` covers desktop and Pi tooling plus current validation options; `methodology.md` documents the plan/MVP/roadmap structure and AI-assisted work rules. Not yet committed.

### Phase 3 — Architecture decision records scaffold

1. Create `docs/architecture/decisions/README.md` explaining ADR format and numbering.
2. Decide whether the `docs` → `data` rename warrants a first ADR; add it if so.

**Suggested commit message:** `Add architecture decision record scaffold`

### Phase 4 — Roadmap and first MVP

1. Replace placeholder content in `docs/roadmap.md` with a real first-pass roadmap (near-term: this foundation work; mid-term: completing the dashboards described in `docs/dashboards.md`; further out: explicitly marked unknown rather than invented).
2. Create `docs/mvp/mvp-001-project-foundation.md`, scoping this plan's work as MVP 1 with acceptance criteria mirroring phases 1–5.

**Suggested commit message:** `Add initial roadmap and MVP 1 definition`

### Phase 5 — README, CLAUDE.md, and git standard alignment

1. Rewrite `README.md` in English: project purpose, pointer to `CLAUDE.md`, pointer to `docs/architecture/overview.md`, pointer to `docs/development/setup.md` for environment/sync instructions.
2. Update `CLAUDE.md`'s repository-structure table, file references, and "Git Workflow" summary against the now-complete `docs/` tree and the direct-to-`main` decision.
3. Rewrite `docs/standards/git.md` to describe the direct-to-`main` workflow instead of the branch + PR model, keeping commit-message conventions and the never-commit/push-without-approval rule.

**Suggested commit message:** `Align README, CLAUDE.md, and git standard with the direct-to-main workflow`

### Phase 6 — Final review

1. Re-read `docs/architecture/overview.md` and update anything phases 1–5 changed (removed files, new doc tree, resolved open questions).
2. Confirm no operational Home Assistant configuration was touched.
3. Review the full diff against `docs/standards/git.md` and `docs/standards/documentation.md`.

**Suggested commit message:** `Update architecture overview after repository foundation work`

## Decisions Made

* **`zigbee.db`** — confirmed: not needed for this project, safe to untrack (Phase 1).
* **`.HA_VERSION` vs `.ha_run.lock`** — keep `.HA_VERSION` tracked (single-line, low-churn, useful version reference); untrack `.ha_run.lock` (pure runtime churn, and its version field would otherwise duplicate `.HA_VERSION`).
* **Git workflow** — direct-to-`main`, no mandatory branch/PR. Solo project (you + Claude Code); simplicity preferred over process overhead. `docs/standards/git.md` and `CLAUDE.md` are updated to match in Phase 5, rather than left contradicting `README.md`.
* **Scaffold vs. real content** — confirmed: real minimal content everywhere, not empty placeholders.
* **Standing rule for this project:** avoid redundant information across documents — each fact should live in exactly one place and be referenced, not repeated. Applies to all phases below, not just the `.HA_VERSION`/`.ha_run.lock` decision above.

## Risks / Open Questions

* **ADR for the `docs` → `data` rename** — `docs/standards/documentation.md` reserves ADRs for "significant architectural decisions." Whether a folder rename clears that bar is a judgment call; default plan is to add one only if the user agrees it's worth recording during Phase 3.
