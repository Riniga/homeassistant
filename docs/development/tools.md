# Development Tools

## Desktop

* **VS Code** — primary editor.
* **Git** — version control.
* **PuTTY** — SSH client used to connect to the Home Assistant Pi's terminal (port `22222`, `root` login; see `docs/development/setup.md`) and, separately, to the GitHub remote.
* **Conda** (or a compatible environment manager) — Python environment for `scripts/export_inventory.py` and its tests, defined in `environment.yml` (Python 3.13, `pytest`).

## Home Assistant (Raspberry Pi)

* **Terminal & SSH add-on** — provides SSH access to the Pi on port `22222`. Its in-browser terminal is not used (unreliable in practice); access is via PuTTY instead.
* **Home Assistant CLI (`ha`):**
  * `ha core check` — validates configuration. Run before every restart.
  * `ha core restart` — restarts Home Assistant core. Only after a successful `ha core check`, and only with explicit approval when working with an AI assistant (see `CLAUDE.md`).

## Validation Options

* **YAML / templates** — static review, plus Home Assistant's own `Developer tools → YAML → Check configuration` or `ha core check`. See `docs/standards/testing.md` for the full validation levels.
* **Python** — `pytest`, run from the conda `ha` environment.

There is currently no CI pipeline or linter configured for this repository (tracked as an open item in `docs/architecture/overview.md`).
