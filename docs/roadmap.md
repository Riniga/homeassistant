# Roadmap — Home Assistant

This roadmap tracks the direction of ongoing work on this Home Assistant configuration repository. It's a living document — update it as priorities shift or firm up, rather than leaving it to go stale.

## Now — Repository Foundation

Establishing a clean, consistent, documented starting point before further feature work begins: stop tracking generated/runtime files, add the documentation `CLAUDE.md` already assumes exists, and align `README.md`/`CLAUDE.md`/`docs/standards/git.md` with how the project actually works today.

Scoped in `docs/plans/001-project-foundation.plan.md` and `docs/mvp/001-project-foundation.md`.

## Next — Complete the Energy Dashboard

`docs/dashboards.md` describes five dashboards, each meant to answer one specific question. Four are built and registered in `configuration.yaml`: Home, Climate, Tech (`dashboards/tech.yaml`), and Security (`dashboards/security.yaml`). The fifth, Energy (`dashboards/energy.yaml` — "What does it cost to run the house?"), is currently an empty file and not registered under `lovelace.dashboards`. Completing and registering it is the next concrete piece of work after this foundation MVP.

## Later — Cleaning & Automation Dashboard

`docs/dashboards.md` describes a sixth dashboard, explicitly called out there as future work: family presence, vacuum, schedules, and automations. No scope or timeline defined yet — this stays a placeholder until it's actually planned.

## Beyond That

Not yet defined. The project is expected to grow to include more applications and shared packages over time, but concrete scope for that is currently unknown and shouldn't be assumed or invented here. Add to this roadmap as real decisions are made, not as speculation.
