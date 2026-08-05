# Development Methodology

This repository follows the workflow defined in `CLAUDE.md`:

```text
Requirement → Plan → Implementation → Validation → Review → Commit → Deployment verification
```

## When a Plan Is Required

Small, low-risk changes — a typo fix, a small dashboard tweak, an obvious YAML correction — can be implemented directly. A plan is needed first when a change touches several files, changes automation behaviour, introduces new entities or helpers, changes configuration structure, or could affect physical devices or system reliability.

## Plans

* Live in `docs/plans/`, named `NNN-slug.plan.md`.
* The plan number matches the number of the MVP it implements (e.g. MVP `003-slug.md` → plan `003-slug.plan.md`), so the pairing is obvious from the filenames alone.
* Structure: Goal, Assumptions, Proposed file changes, Implementation phases with TODOs (each phase with a suggested commit message), Risks / Open questions.
* Broken into phases. Each phase is implemented, validated, and — per the direct-to-`main` git workflow in `docs/standards/git.md` — committed before moving to the next.
* `docs/claude-prompts/2-create-plan-prompt.md` describes the prompt used to generate one.

## MVPs

* Live in `docs/mvp/`, named `NNN-slug.md`.
* Scope one unit of delivery: purpose, contents, acceptance criteria.
* `docs/claude-prompts/3-complete-mvp.md` describes the checklist used once an MVP's phases are all done and it's ready to be considered complete.

## Roadmap

`docs/roadmap.md` holds the longer-term direction this work is building toward. Plans and MVPs should trace back to something in it, or explicitly extend it.

## AI-Assisted Work

Governed by `CLAUDE.md`. In particular: implement one phase or task at a time, keep changes small and reviewable, never commit, push, reload, or restart without explicit approval each time, and update the plan as work progresses rather than leaving it stale.
