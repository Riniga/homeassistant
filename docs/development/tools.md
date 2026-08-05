# Development Tools

## Desktop

* **VS Code** — primary editor.
* **Git** — version control.
* **SSH** — used to connect to the Home Assistant remote (see `docs/development/setup.md`).
* **Conda** (or a compatible environment manager) — Python environment for `scripts/export_inventory.py` and its tests, defined in `environment.yml` (Python 3.13, `pytest`).

## Home Assistant (Raspberry Pi)

* **Terminal & SSH add-on** — provides an in-browser terminal and SSH access to the Pi.
* **Home Assistant CLI (`ha`):**
  * `ha core check` — validates configuration. Run before every restart.
  * `ha core restart` — restarts Home Assistant core. Only after a successful `ha core check`, and only with explicit approval when working with an AI assistant (see `CLAUDE.md`).

## Validation Options

* **YAML / templates** — static review, plus Home Assistant's own `Developer tools → YAML → Check configuration` or `ha core check`. See `docs/standards/testing.md` for the full validation levels.
* **Python** — `pytest`, run from the conda `ha` environment.

There is currently no CI pipeline or linter configured for this repository (tracked as an open item in `docs/architecture/overview.md`).
