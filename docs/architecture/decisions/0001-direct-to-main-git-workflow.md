# 0001. Direct-to-main git workflow

## Status

Accepted

## Context

`docs/standards/git.md` originally defined a mandatory feature-branch and pull-request workflow (branch prefixes, PR review, "never work directly on `main`"). At the same time, `README.md` documented a simpler reality already in use: commit and push directly to `main`/`master`, including from the Home Assistant terminal itself for day-to-day UI-driven changes.

This repository has exactly one contributor (the owner) plus Claude Code — no team to coordinate with, no concurrent branches, no review handoff between people. A mandatory branch/PR process adds process overhead (branch naming, PR creation, merge step) without the coordination benefit it exists to provide, and it actively contradicted how the project was already being used.

## Decision

Adopt a single, direct-to-`main` git workflow for the whole repository: commit and push straight to `main`, no feature branches, no pull requests. `docs/standards/git.md` and `CLAUDE.md` were rewritten to match (`docs/plans/001-project-foundation.plan.md`, Phase 5), rather than leaving the branch/PR model in place alongside a README that contradicted it.

The existing AI-assistant safety rule is unaffected: commits and pushes still require explicit approval each time — that rule is about safety, not about branching.

## Consequences

* Simpler day-to-day workflow, matching how the project already operated in practice on the Home Assistant side.
* No branch-based isolation between in-progress and stable work — `main` can contain incomplete multi-phase work between commits (mitigated by keeping each commit small and phase-scoped, per `docs/development/methodology.md`).
* If a second contributor is ever added, this decision should be revisited — the trade-off assumes a solo maintainer.
