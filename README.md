# Home Assistant

Configuration and supporting files for a production Home Assistant installation, managed through this Git repository.

## Overview

* Development happens on a desktop workstation in VS Code.
* The configuration runs live on a Raspberry Pi.
* The two are kept in sync through GitHub using a simple, direct-to-`main` workflow — see `docs/standards/git.md`.

## Where to Start

* `CLAUDE.md` — rules for AI-assisted work on this repository.
* `docs/architecture/overview.md` — current architecture, repository structure, and dependencies.
* `docs/development/setup.md` — one-time setup and the day-to-day sync workflow between the desktop and the Home Assistant Pi.
* `docs/roadmap.md` — current direction of the project.

## Status

This project is in its initial foundation phase: cleaning up repository hygiene and filling in the documentation the AI-assisted workflow depends on, before further feature work begins. See `docs/plans/001-project-foundation.plan.md` and `docs/mvp/001-project-foundation.md`.
