# Claude Code Instructions

## Purpose

This repository contains the configuration and supporting files for a production Home Assistant installation running on a Raspberry Pi.

Development is performed on a desktop computer. Changes are synchronized to the Home Assistant installation through Git.

Claude Code should help maintain and improve the configuration in small, controlled, and reviewable steps. Reliability, clarity, and safe operation take priority over speed or clever solutions.

## Read Before Planning or Implementation

Before creating a plan or modifying files, read the relevant documentation in this order:

1. `README.md` — repository overview and basic workflow.
2. `docs/architecture/overview.md` — current architecture, configuration structure, and dependencies.
3. `docs/architecture/decisions/` — relevant architecture decision records.
4. `docs/development/setup.md` — development and synchronization workflow.
5. `docs/development/tools.md` — required tools and validation options.
6. `docs/standards/coding.md` — coding conventions.
7. `docs/standards/testing.md` — validation and testing requirements.
8. `docs/standards/git.md` — Git conventions.
9. Relevant roadmap, MVP, or implementation plan documents for the requested task.

Read only the documentation relevant to the task. Do not load unrelated files without reason.

If a referenced document does not exist, identify the missing documentation. Do not invent project rules that should be defined elsewhere.

## Repository Structure

The repository contains the complete Home Assistant configuration directory.

Use the actual repository structure as the source of truth. Common areas may include:

| Area                   | Typical location                      |
| ---------------------- | ------------------------------------- |
| Main configuration     | `configuration.yaml`                  |
| Automations            | `automations.yaml` or `automations/`  |
| Scripts                | `scripts.yaml` or `scripts/`          |
| Scenes                 | `scenes.yaml`                         |
| Templates              | `templates.yaml` or `templates/`      |
| Packages               | `packages/`                           |
| Dashboards             | dashboard YAML files or `dashboards/` |
| Themes                 | `themes/`                             |
| Custom integrations    | `custom_components/`                  |
| Documentation          | `docs/`                               |
| Architecture decisions | `docs/architecture/decisions/`        |
| Development workflow   | `docs/development/`                   |
| Implementation plans   | `docs/plans/`                         |
| MVP definitions        | `docs/mvp/`                           |
| Standards              | `docs/standards/`                     |
| Registry data exports  | `data/`                               |

Do not reorganize files or introduce new folders unless the requested change requires it and the change is documented.

## Development Workflow

Follow this flow for non-trivial changes:

```text
Requirement → Plan → Implementation → Validation → Review → Commit → Deployment verification
```

Small, clear, and low-risk changes may be implemented without a separate plan document.

Examples include:

* Correcting documentation
* Fixing a spelling error
* Updating an entity reference
* Making a small dashboard adjustment
* Correcting an obvious YAML error

A plan is normally required when a change:

* Affects several files
* Changes automation behaviour
* Introduces new entities or helpers
* Changes configuration structure
* Adds an integration or dependency
* Requires several implementation steps
* Could affect physical devices or system reliability

## Planning Rules

* Create or update an implementation plan in `docs/plans/` before meaningful multi-step work.
* Use descriptive file names in `kebab-case`.
* Break plans into numbered tasks with clear acceptance criteria.
* Identify which checks can be performed on the desktop and which require Home Assistant.
* Identify any required reload, restart, or physical-device verification.
* Implement one logical task at a time.
* Update the plan as work progresses.
* Mark a task complete only after the applicable validation has passed.
* Do not mark runtime behaviour as verified until it has been tested in Home Assistant.

## Implementation Rules

* Keep changes small and easy to review.
* Modify only files needed for the current task.
* Preserve existing behaviour unless a behaviour change is explicitly requested.
* Prefer native Home Assistant functionality over custom code.
* Prefer simple and explicit YAML and Jinja over compact or clever solutions.
* Reuse existing project patterns before introducing new conventions.
* Do not introduce new integrations, custom components, helpers, or dependencies without explaining why.
* Do not mix unrelated refactoring with the requested change.
* Do not perform broad formatting or cleanup outside the requested scope.
* Do not rename existing entities unless explicitly required.
* Treat entity IDs as stable interfaces used by automations, dashboards, integrations, and external systems.
* Do not leave temporary entities, debug configuration, or test code behind.
* Do not leave `TODO` comments unless they reference an accepted plan item.
* Do not change operational configuration during a documentation-only task.

## Home Assistant Coding Rules

Follow `docs/standards/coding.md`.

Important principles include:

* Use two-space YAML indentation.
* Use `snake_case` for entity IDs, variables, and identifiers.
* Use descriptive and stable names.
* Give automations, scripts, and templates one clear responsibility.
* Avoid unnecessary duplication.
* Keep Jinja templates readable.
* Use intermediate variables for complex templates.
* Handle `unknown`, `unavailable`, `none`, missing attributes, and invalid values safely.
* Avoid deeply nested `choose`, condition, and template structures when a clearer solution is possible.
* Never ignore errors silently.
* Keep comments focused on why a solution exists.
* Preserve the formatting style of existing files unless it conflicts with the coding standard.

## Home Assistant Configuration Safety

This repository controls a live Home Assistant installation and may operate physical devices.

Before changing configuration:

* Identify all affected entities, devices, automations, scripts, dashboards, and templates.
* Search for references before renaming or removing an entity.
* Consider startup behaviour.
* Consider unavailable integrations and devices.
* Consider repeated, delayed, or overlapping automation triggers.
* Consider what happens after a Home Assistant restart.
* Consider safe default behaviour if inputs are missing or invalid.

For changes affecting locks, alarms, heating, ventilation, power, doors, safety-related equipment, or unattended physical operation:

* Use conservative behaviour.
* Clearly identify risks and assumptions.
* Require explicit user review before deployment.
* Include a rollback approach.
* Do not activate or operate physical devices without explicit approval.

## Protected and Generated Files

Do not manually modify Home Assistant-managed files unless explicitly requested and the consequences are understood.

This normally includes:

* `.storage/`
* Database files
* Log files
* Backup archives
* Generated files
* Runtime state
* Integration-managed configuration

Do not assume that every file in the repository should be version controlled.

Respect `.gitignore` and the documented repository policy.

## Secrets and Sensitive Information

* Never expose, print, log, or commit secrets.
* Store supported credentials in `secrets.yaml` and reference them with `!secret`.
* Never commit real passwords, tokens, API keys, certificates, webhook IDs, or private connection details.
* Do not replace secret references with literal values.
* Do not include sensitive values in examples, plans, commit messages, or documentation.
* Review diffs for accidentally exposed credentials.
* Treat location data, camera configuration, alarm details, device identifiers, and household presence information as potentially sensitive.

## Documentation Rules

Follow `docs/standards/documentation.md`.

Summary:

* Write documentation in English.
* Use English `kebab-case` file and folder names.
* Keep documentation concise, practical, and current.
* Document why something exists, what it does, and important assumptions or constraints.
* Avoid duplicating information across documents.
* Update documentation in the same change as the implementation it describes.
* Record significant and lasting architectural decisions as ADRs.
* Do not create documentation for implementation details already obvious from the configuration.

## Validation and Testing Rules

Follow `docs/standards/testing.md`.

Claude must distinguish between:

1. Checks that can be performed on the desktop.
2. Checks that require the Home Assistant environment.
3. Checks that require real entities or physical devices.

Before proposing a commit:

* Review the complete diff.
* Check YAML structure and indentation.
* Verify entity IDs and action or service names against existing project usage.
* Review Jinja templates for invalid and unavailable values.
* Check that no unrelated files changed.
* Identify the exact Home Assistant validation still required.

When applicable, instruct the user to perform:

* Home Assistant configuration validation
* Template validation
* Automation or script execution
* Automation trace review
* Log review
* Dashboard verification
* Physical-device verification

Never claim that configuration has passed Home Assistant validation unless that validation was actually performed.

Never claim that an automation or device behaviour works based only on static inspection.

## Reload and Restart Rules

* Prefer reloading only the affected configuration domain when supported.
* Do not recommend a full restart when a targeted reload is sufficient.
* Validate configuration before recommending a restart.
* Explain what must be reloaded or restarted for the change to take effect.
* Warn when a restart may temporarily affect availability.
* Never execute a reload, restart, or device action without explicit approval.

## Git Workflow

Follow `docs/standards/git.md`.

Summary:

* Work directly on `main` — this is a solo project, no mandatory branches or pull requests.
* Keep each change focused on one purpose.
* Use clear, descriptive commit messages.
* Review the diff before suggesting a commit.
* Commit only completed and appropriately validated work.
* Never commit secrets, generated runtime files, databases, logs, or backups.
* Never commit, push, rebase, or force-push without explicit approval.
* When a change stops tracking a live, non-regenerable file, follow the backup-first rollout in `docs/development/setup.md` before pushing.
* Do not discard or overwrite existing user changes.
* Do not use destructive Git commands without explicit approval.

## Working With Existing Changes

Before modifying files:

* Run or request `git status`.
* Identify modified, staged, and untracked files.
* Assume existing uncommitted changes belong to the user.
* Do not overwrite, revert, reformat, or remove unrelated changes.
* Keep the requested changes separate whenever practical.
* Ask before modifying a file containing substantial unrelated user changes.

## Architecture Rules

* Preserve the documented architecture unless a change is explicitly required.
* Follow existing include, package, dashboard, automation, and naming patterns.
* Do not move configuration between files merely to match personal preference.
* Avoid unnecessary abstractions.
* Do not introduce a new structural convention when an existing convention already solves the problem.
* Document significant structural or architectural changes.
* Update the architecture overview when the implemented structure changes.

## AI Collaboration Rules

* Be explicit about assumptions and uncertainty.
* Do not invent entity IDs, device IDs, service names, paths, integrations, or project rules.
* Search the repository before concluding that something does not exist.
* Prefer existing entities and helpers over creating new ones.
* Explain important trade-offs briefly.
* Present risky or broad changes before applying them.
* Keep changes incremental and reviewable.
* Do not rewrite large configuration areas unless explicitly required.
* Do not silently improve unrelated code.
* Do not claim that an action has been performed unless it has actually been performed.
* When information is missing, state what is missing and make the safest reasonable assumption only when necessary.
* Keep generated plans, documentation, and configuration consistent with repository standards.

## Definition of Done

A task is complete when:

* The requested change has been implemented.
* Only relevant files were modified.
* The implementation follows project standards.
* Documentation has been updated when required.
* All desktop-level checks have passed.
* Required Home Assistant validation has been clearly identified or completed.
* Runtime or physical-device testing has been completed when applicable.
* No sensitive data has been introduced.
* The diff has been reviewed.
* The relevant implementation plan has been updated.
* The work is ready for user approval before commit, push, merge, reload, restart, or deployment.
