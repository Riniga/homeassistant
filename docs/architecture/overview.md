# Architecture Overview

## Project Overview

This repository holds the configuration for a production Home Assistant installation (version `2026.7.4`) running on a Raspberry Pi. Development happens on a desktop workstation in VS Code; changes are synchronized to the running instance through Git (`git pull` / `git push`), as described in [README.md](../../README.md).

The project is in its initial state. `docs/claude-prompts/` contains a small workflow (initialize → plan → complete MVP) intended to bootstrap AI-assisted, documentation-driven development on top of this configuration. No application code beyond the Home Assistant configuration and a small number of custom integrations/scripts exists yet.

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
│   ├── claude-prompts/           # Prompts for driving AI-assisted work in stages
│   ├── standards/                 # Coding, documentation, git, and testing standards
│   ├── dashboards.md               # Product-level intent for each dashboard
│   └── roadmap.md                   # Placeholder, not yet filled in
├── scripts/
│   └── export_inventory.py        # Python script that populates data/
├── www/                            # Static assets served by HA (images, floorplan SVG/CSS)
├── zigbee.db                        # Zigbee2MQTT/ZHA runtime database
├── .HA_VERSION / .ha_run.lock        # Runtime state files written by Home Assistant
├── CLAUDE.md                          # Governance rules for AI-assisted changes to this repo
└── README.md                           # Repository purpose and sync/operational workflow
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
| AI governance | `CLAUDE.md`, `docs/standards/*.md`, `docs/claude-prompts/*.md` | Rules and prompts constraining how AI-assisted changes are planned, implemented, and validated |

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

**Standalone tooling:** `scripts/export_inventory.py` depends on `websockets` and `python-dotenv` (`load_dotenv`), reading `HA_URL` and `HA_TOKEN` from a local `.env` file (present but git-ignored). There is no `requirements.txt` or `pyproject.toml` pinning these dependencies — they are currently assumed to be installed ad hoc in the developer's environment. **This is a gap**: the exact required package versions for this script are currently unknown/undeclared.

## Build and Development Process

There is no build step — Home Assistant consumes the YAML/Python files directly.

Documented workflow (from `README.md`, in Swedish):

1. Edit configuration on the desktop via VS Code; the repo is cloned locally.
2. Home Assistant's own working copy on the Raspberry Pi is kept in sync with GitHub via `git pull` / `git push` from HA's own "Terminal & SSH" add-on.
3. Day-to-day HA-side changes (made through the UI, e.g. new automations/scenes) are committed and pushed from the HA terminal: `git add . && git commit -m "message" && git push origin master`.
4. Changes made on the desktop are pulled onto HA with `git pull origin master`.
5. After configuration changes, `ha core check` is used to validate, followed by `ha core restart` if needed.

`docs/standards/git.md` additionally defines a branch-based workflow (feature branches, PRs against `main`) for AI-assisted changes, which is stricter than the direct-to-`master`/`main` push flow described in the README. **These two workflows are not yet reconciled** — see Open Questions.

`scripts/export_inventory.py` is run manually (not on a schedule or via CI) to regenerate the `data/` exports from the live HA websocket API.

There is no CI/CD pipeline, linter configuration, or automated formatting tool present in the repository.

## Architectural Observations

* **Flat, HA-generated configuration files.** `automations.yaml` and `scenes.yaml` follow Home Assistant's UI-editor format (auto-generated numeric IDs, inline `alias`/`description`), rather than hand-authored, well-named YAML. This is consistent with a workflow where changes originate in the HA UI and are synced to Git, rather than authored directly in the repository.
* **`scripts.yaml` is empty.** No native HA scripts are currently defined; any automation logic beyond triggers/conditions/actions currently lives inline in automations.
* **Credentials embedded directly in `configuration.yaml`.** The `camera:` block contains RTSP URLs with plaintext credentials embedded in the connection string, rather than using `!secret` references into `secrets.yaml` (which does not exist in this repository). This conflicts with `docs/standards/git.md` and `CLAUDE.md`'s secrets-handling rules and is a notable risk.
* **`themes:` include with no `themes/` directory.** `configuration.yaml` includes `!include_dir_merge_named themes`, but no `themes/` directory exists in the repository. Home Assistant may tolerate a missing directory here, but this is currently unverified.
* **Dual sync workflow.** Configuration can be changed from two directions — the HA UI (synced back to Git from the device itself) and the desktop repository (synced to HA via Git) — which means conflicting edits are possible if both sides are used without careful ordering.
* **`custom_components/hacs` is vendored into version control**, including its full compiled frontend bundle (`hacs_frontend/`), rather than being installed/managed purely at runtime. This substantially increases repository size and is unusual compared to a typical HACS-managed setup where HACS installs itself once and updates itself outside of Git.
* **AI-assisted development governance is already defined** (`CLAUDE.md`, `docs/standards/*`) even though the supporting documents it references (`docs/development/setup.md`, `docs/development/tools.md`, `docs/development/methodology.md`, `docs/mvp/`, `docs/plans/`) do not exist yet. This document (`docs/architecture/overview.md`) is the first of those referenced documents to be created.
* **No automated tests exist** for the one piece of custom Python (`scripts/export_inventory.py`), despite `docs/standards/testing.md` recommending `pytest` for custom Python code.

## Planned Evolution of the Workspace

Per the instruction under which this document was created, this is stated to be "the initial version of the project," with additional applications and shared packages expected to be added over time. Beyond that, concrete planned evolution is currently only partially documented:

* `docs/roadmap.md` exists but is a placeholder (contains only section headings, no content).
* `docs/dashboards.md` describes the intended purpose of each dashboard, including one not yet built: **Dashboard 6 – Cleaning & Automation** (family presence, vacuum, schedules, automations), described as a "future dashboard."
* The `docs/claude-prompts/` workflow (`1-initialize-the-project.md` → `2-create-plan-prompt.md` → `3-complete-mvp.md`) implies future work will be organized around `docs/mvp/*.md` MVP definitions and `docs/plans/*.plan.md` implementation plans, neither of which exist yet.

Beyond these signals, specific future applications, shared packages, or structural changes are **currently unknown** and should not be assumed.

## Open Questions or Areas Not Yet Implemented

* `docs/development/setup.md`, `docs/development/tools.md`, and `docs/development/methodology.md` are referenced by `CLAUDE.md` and `docs/claude-prompts/2-create-plan-prompt.md` but do not exist.
* `docs/architecture/decisions/` (ADR directory) is referenced by `CLAUDE.md` but does not exist.
* `docs/plans/` and `docs/mvp/` are referenced by the Claude prompt workflow but do not exist.
* `docs/roadmap.md` has no actual content yet ("Övergripande mål" section is a placeholder).
* The relationship between the README's direct-push workflow and `docs/standards/git.md`'s branch/PR-based workflow has not been reconciled — it is unclear which applies when, or whether the README is expected to be updated to match the newer standard.
* Whether a missing `themes/` directory causes a Home Assistant startup error is unverified.
* Whether `dashboards/energy.yaml` (currently empty, 0 lines) but referenced conceptually in `docs/dashboards.md` as "Dashboard 3 – Energi" is planned, in-progress, or abandoned is unknown — it is not currently registered under `lovelace.dashboards` in `configuration.yaml` at all.
* No dependency manifest exists for `scripts/export_inventory.py`; the exact required versions of `websockets` and `python-dotenv` are unknown.
* No testing strategy, CI pipeline, or linting configuration currently exists for either the Python script or the YAML configuration, beyond the manual validation steps described in `docs/standards/testing.md`.
* Camera credentials in `configuration.yaml` should likely move to `secrets.yaml`, but this is a configuration change and is intentionally **not** performed as part of this documentation-only task.
