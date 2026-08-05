# MVP 1 — Project Foundation

## Purpose

Establish a clean, consistent, fully documented starting point for this repository before further feature work begins, so that future work — human or AI-assisted — has accurate documentation, no stray generated files under version control, and an agreed lightweight process to follow.

## Scope

This MVP covers exactly the work defined in `docs/plans/001-project-foundation.plan.md`:

* Stop tracking generated/runtime files that don't belong in version control.
* Add the development documentation `CLAUDE.md` already assumes exists.
* Scaffold architecture decision records.
* Produce a real first-pass roadmap and this MVP definition.
* Align `README.md`, `CLAUDE.md`, and `docs/standards/git.md` with the current state of the repository and the direct-to-`main` workflow decision.

No Home Assistant configuration, automation, entity, or physical-device behaviour changes are in scope.

## Acceptance Criteria

- [x] Phase 1 — `.cache/`, `.ha_run.lock`, `home-assistant.log.fault`, and `zigbee.db` are untracked and gitignored; `.HA_VERSION` remains tracked. Rolled out to the live Home Assistant Pi (see the incident log in the plan for how the rollout itself was handled safely).
- [x] Phase 2 — `docs/development/setup.md`, `tools.md`, and `methodology.md` exist with real content.
- [x] Phase 3 — `docs/architecture/decisions/` exists with format, numbering, and when-to-use guidance.
- [x] Phase 4 — `docs/roadmap.md` has real first-pass content; this MVP document exists.
- [x] Phase 5 — `README.md` is rewritten in English with sync steps moved to `docs/development/setup.md`; `CLAUDE.md` and `docs/standards/git.md` reflect the current documentation tree and the direct-to-`main` workflow.
- [x] Phase 6 — `docs/architecture/overview.md` is re-reviewed and updated to reflect everything above; nothing in the finished documentation set contradicts anything else.

## Status

Complete. All phases implemented, validated, and committed — see `docs/plans/001-project-foundation.plan.md` for the phase-by-phase record.

## Out of Scope

Explicitly deferred, per the plan's assumptions — these are configuration-level changes, not documentation/hygiene, and stay tracked as open items in `docs/architecture/overview.md` for a future MVP:

* Moving camera credentials out of `configuration.yaml` into `secrets.yaml`.
* Building and registering `dashboards/energy.yaml`.
* Resolving the missing `themes/` directory referenced by `configuration.yaml`.
