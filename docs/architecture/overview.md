# Architecture Overview

## Project Overview

This repository holds the configuration for a production Home Assistant installation (version `2026.7.4`) running on a Raspberry Pi. Development happens on a desktop workstation in VS Code; changes are synchronized to the running instance through Git, using a direct-to-`main` workflow described in `docs/development/setup.md` and `docs/standards/git.md`.

The project is in its initial foundation phase (see `docs/roadmap.md`). `docs/claude-prompts/` contains a small workflow (initialize → plan → complete MVP) used to bootstrap AI-assisted, documentation-driven development on top of this configuration — this document, `docs/plans/001-project-foundation.plan.md`, and `docs/mvp/mvp-001-project-foundation.md` are its first output. No application code beyond the Home Assistant configuration and a small number of custom integrations/scripts exists yet.

## Current Workspace Structure

```text
.
├── configuration.yaml       # Main Home Assistant configuration entry point
├── automations.yaml         # All automations (flat file, HA-generated format)
├── scenes.yaml               # All scenes (flat file, HA-generated format)
├── scripts.yaml               # Script definitions (currently empty)
├── blueprints/
│   ├── automation/            # Third-party and built-in automation blueprints
│   ├── script/                 # Script blueprints
│   └── template/                # Template blueprints
├── custom_components/         # Manually installed (non-HACS-managed at runtime) integrations
│   ├── gardena_smart_system/
│   ├── hacs/                    # HACS itself, vendored into the repo
│   ├── midea_ac/
│   ├── midea_dehumidifier_lan/
│   ├── plejd/
│   └── sigen/
├── dashboards/                 # YAML-mode Lovelace dashboards
│   ├── home.yaml
│   ├── climate.yaml
│   ├── tech.yaml
│   ├── security.yaml
│   └── energy.yaml              # Present but currently empty
├── data/                        # Generated export of the HA area/device/entity registries
│   ├── *.csv / *.json
│   └── homeassistant_inventory.md
├── docs/                        # Project documentation (this document lives here)
│   ├── architecture/
│   │   ├── overview.md              # This document
│   │   └── decisions/                # ADR scaffold + 0001 (direct-to-main git workflow)
│   ├── development/               # Setup, tools, and methodology docs
│   ├── plans/                      # Implementation plans (docs/plans/NNN-slug.plan.md)
│   ├── mvp/                         # MVP definitions (docs/mvp/mvp-NNN-slug.md)
│   ├── claude-prompts/               # Prompts for driving AI-assisted work in stages
│   ├── standards/                     # Coding, documentation, git, and testing standards
│   ├── dashboards.md                   # Product-level intent for each dashboard
│   └── roadmap.md                       # Now/Next/Later direction of the project
├── scripts/
│   └── export_inventory.py        # Python script that populates data/
├── www/                            # Static assets served by HA (images, floorplan SVG/CSS)
├── zigbee.db                        # Zigbee2MQTT/ZHA runtime database (gitignored; live, not regenerable — see docs/development/setup.md)
├── .HA_VERSION                       # Tracked; low-churn HA version marker
├── .ha_run.lock                       # Gitignored; runtime PID/timestamp, rewritten every start
├── .claude/settings.json              # Committed Claude Code permissions for this repo
├── CLAUDE.md                          # Governance rules for AI-assisted changes to this repo
└── README.md                           # Repository purpose and pointers
```

Directories referenced by `configuration.yaml` but **not present** in the repository: `themes/` (see [Open Questions](#open-questions-or-areas-not-yet-implemented)).

## Major Components

| Component | Location | Purpose |
| --- | --- | --- |
| Core configuration | `configuration.yaml` | Zone/location, HTTP/proxy settings, TTS, camera, frontend themes include, automation/script/scene includes, Lovelace dashboard registration |
| Automations | `automations.yaml` | Home Assistant UI-managed automation definitions (flat list, HA-generated IDs) |
| Scenes | `scenes.yaml` | HA UI-managed scene definitions |
| Scripts | `scripts.yaml` | Currently empty; no scripts defined through HA's native script domain |
| Blueprints | `blueprints/` | Reusable automation/script/template logic sourced from the community (motion lighting, TRADFRI remotes, zone notifications, confirmable notifications, inverted binary sensor) |
| Custom integrations | `custom_components/` | Six vendored integrations: HACS (the integration/dependency manager itself), Gardena Smart System, Midea AC, Midea Dehumidifier (LAN), Plejd BLE, Sigenergy ESS |
| Dashboards | `dashboards/` + `lovelace.dashboards` in `configuration.yaml` | Four active YAML-mode dashboards (Home, Climate, Tech, Security) plus one empty placeholder (Energy) |
| Inventory export tool | `scripts/export_inventory.py` | Standalone Python script (outside the HA process) that connects to HA's websocket API and exports the area/device/entity registries into `data/` |
| Static assets | `www/` | Floorplan SVG/CSS and photos used by dashboards |
| AI governance | `CLAUDE.md`, `.claude/settings.json`, `docs/standards/*.md`, `docs/development/*.md`, `docs/architecture/decisions/`, `docs/plans/*.md`, `docs/mvp/*.md`, `docs/claude-prompts/*.md` | Rules, tool permissions, and prompts constraining how AI-assisted changes are planned, implemented, and validated |

## Existing Dependencies

**Runtime (Home Assistant core):** version `2026.7.4` (from `.HA_VERSION`). The Python environment/dependency manifest for HA core itself is not part of this repository (no `requirements.txt` at the repo root for HA core).

**Custom integration dependencies** (from each `manifest.json`):

| Integration | Version | Key requirements |
| --- | --- | --- |
| `gardena_smart_system` | 3.1.3 | `aiohttp>=3.7.0`, `websockets>=10.0` |
| `hacs` | 2.0.5 | Bundled frontend assets; depends on HA's `http`, `websocket_api`, `frontend`, `persistent_notification`, `lovelace`, `repairs` |
| `midea_ac` | 2026.7.2 | `msmart-ng==2026.7.0`, `pyyaml` |
| `midea_dehumidifier_lan` | 0.9.7 | `midea-beautiful-air==0.10.7` |
| `plejd` | (see manifest) | Depends on HA's `bluetooth_adapters`; uses Bluetooth service UUID matching |
| `sigen` | (see manifest) | Depends on HA's `modbus`, `integration`, `recorder`; DHCP-based discovery |

**Standalone tooling:** `scripts/export_inventory.py` depends on `websockets` and `python-dotenv` (`load_dotenv`), reading `HA_URL` and `HA_TOKEN` from a local `.env` file (present but git-ignored). These are now pinned in `environment.yml` (`websockets>=17,<18`, `python-dotenv>=1,<2`, alongside `pytest>=8,<9`) rather than installed ad hoc.

## Build and Development Process

There is no build step — Home Assistant consumes the YAML/Python files directly.

Documented workflow (`docs/development/setup.md`, `docs/standards/git.md`):

1. Edit configuration on the desktop via VS Code; the repo is cloned locally.
2. Home Assistant's own working copy on the Raspberry Pi is kept in sync with GitHub via `git pull` / `git push` from HA's own "Terminal & SSH" add-on.
3. Day-to-day HA-side changes (made through the UI, e.g. new automations/scenes) are committed and pushed directly to `main` from the HA terminal.
4. Changes made on the desktop are pulled onto HA the same way.
5. After configuration changes, `ha core check` is used to validate, followed by `ha core restart` if needed.
6. For a commit that stops tracking a live, non-regenerable file (not a cache/log/lock file), a backup-first rollout is required — see `docs/development/setup.md`. This was learned the hard way: rolling out the Phase 1 cleanup in `docs/plans/001-project-foundation.plan.md` deleted `zigbee.db` from the live Pi before this procedure existed.

This repository uses a single, direct-to-`main` workflow — no feature branches or pull requests (a deliberate simplification for a solo project, decided during `docs/plans/001-project-foundation.plan.md`).

`scripts/export_inventory.py` is run manually (not on a schedule or via CI) to regenerate the `data/` exports from the live HA websocket API.

There is no CI/CD pipeline, linter configuration, or automated formatting tool present in the repository.

## Architectural Observations

* **Flat, HA-generated configuration files.** `automations.yaml` and `scenes.yaml` follow Home Assistant's UI-editor format (auto-generated numeric IDs, inline `alias`/`description`), rather than hand-authored, well-named YAML. This is consistent with a workflow where changes originate in the HA UI and are synced to Git, rather than authored directly in the repository.
* **`scripts.yaml` is empty.** No native HA scripts are currently defined; any automation logic beyond triggers/conditions/actions currently lives inline in automations.
* **Credentials embedded directly in `configuration.yaml`.** The `camera:` block contains RTSP URLs with plaintext credentials embedded in the connection string, rather than using `!secret` references into `secrets.yaml` (which does not exist in this repository). This conflicts with `docs/standards/git.md` and `CLAUDE.md`'s secrets-handling rules and is a notable risk.
* **`themes:` include with no `themes/` directory.** `configuration.yaml` includes `!include_dir_merge_named themes`, but no `themes/` directory exists in the repository. Home Assistant may tolerate a missing directory here, but this is currently unverified.
* **Dual sync workflow.** Configuration can be changed from two directions — the HA UI (synced back to Git from the device itself) and the desktop repository (synced to HA via Git) — which means conflicting edits are possible if both sides are used without careful ordering.
* **`custom_components/hacs` is vendored into version control**, including its full compiled frontend bundle (`hacs_frontend/`), rather than being installed/managed purely at runtime. This substantially increases repository size and is unusual compared to a typical HACS-managed setup where HACS installs itself once and updates itself outside of Git.
* **AI-assisted development governance is fully scaffolded.** `CLAUDE.md` and `docs/standards/*` reference `docs/development/setup.md`, `docs/development/tools.md`, `docs/development/methodology.md`, `docs/architecture/decisions/`, `docs/plans/`, and `docs/mvp/` — all of these now exist with real content (created via `docs/plans/001-project-foundation.plan.md`), so `CLAUDE.md`'s "Read Before Planning" list now fully resolves.
* **No automated tests exist** for the one piece of custom Python (`scripts/export_inventory.py`), despite `docs/standards/testing.md` recommending `pytest` for custom Python code.

## Planned Evolution of the Workspace

Per the instruction under which this document was created, this is stated to be "the initial version of the project," with additional applications and shared packages expected to be added over time. See `docs/roadmap.md` for the current Now/Next/Later direction — not repeated here to avoid two documents drifting out of sync (per `docs/standards/documentation.md`'s single-source-of-truth rule).

Future work is organized around `docs/mvp/*.md` MVP definitions and `docs/plans/*.plan.md` implementation plans, following the `docs/claude-prompts/` workflow (`1-initialize-the-project.md` → `2-create-plan-prompt.md` → `3-complete-mvp.md`).

## Open Questions or Areas Not Yet Implemented

* Whether a missing `themes/` directory causes a Home Assistant startup error is unverified.
* No testing strategy, CI pipeline, or linting configuration currently exists for either the Python script or the YAML configuration, beyond the manual validation steps described in `docs/standards/testing.md`.
* Camera credentials in `configuration.yaml` should likely move to `secrets.yaml`, but this is a configuration change and is intentionally **not** performed as part of this documentation-only task.
