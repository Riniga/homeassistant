# Git Workflow

The goal is to keep every change small, traceable, and safe to deploy.

## Working on `main`

This is a solo project (you + Claude Code, no other collaborators) — commit and push directly to `main`. There is no mandatory feature-branch or pull-request process.

* `main` always represents the current Home Assistant configuration, on both the desktop and the live Raspberry Pi.
* Keep each change focused on one purpose, even without a branch to enforce it.
* See `docs/development/setup.md` for how changes actually move between the desktop and the Home Assistant Pi.

## Commits

* Commit after each completed and verified task, or plan phase.
* Keep commits focused on a single logical change.
* Do not commit unfinished or unverified configuration.
* Validate the affected configuration before committing.
* Update related documentation as part of the same commit whenever appropriate.

## Commit Messages

Write commit messages in English using a short imperative sentence.

Examples:

```text
Add ventilation automation

Improve presence detection

Fix template sensor calculation

Refactor dashboard layout

Update coding standard
```

Avoid vague messages such as:

```text
fix

updates

misc

wip
```

## Push Rules

* Do not commit or push without explicit approval when working with an AI assistant.
* Never force-push without explicit agreement.

## Removing a File From Version Control

Untracking a file (`git rm --cached`) only affects the desktop's index — the working copy stays in place there. On any other machine, pulling that same commit deletes the file from disk for real.

* For generated/regenerable files (cache, lock, log files) this is harmless.
* For a live, non-regenerable file (a database, credential file, or similar), follow the backup-first rollout in `docs/development/setup.md` before pushing the change: back up the file independently, pull, then restore it from the backup. This is not optional — see the `zigbee.db` incident logged in `docs/plans/001-project-foundation.plan.md` for what happens if it's skipped.

## Validation Before Commit

Before committing, verify that:

* Configuration is syntactically valid.
* YAML formatting is consistent.
* Templates are valid.
* Modified automations behave as expected.
* No unintended entity renames have been introduced.
* Related documentation has been updated.

## What Must Never Be Committed

Never commit:

* Passwords
* API keys
* Access tokens
* Private certificates
* Backup archives
* Sensitive personal data
* Temporary or generated files

Respect the project's `.gitignore` file.

## Working with AI Assistants

The assistant must:

* Follow the approved implementation plan.
* Complete one task at a time.
* Keep changes as small as practical.
* Explain significant refactoring before performing it.
* Never commit or push without explicit approval.
* Preserve existing behaviour unless the task explicitly requires a change.

## Daily Workflow

```bash
git status
git pull origin main
```

Implement and validate a small, complete change.

```bash
git add <files>
git commit -m "Add descriptive commit message"
git push origin main
```

## Scope of Changes

The assistant should modify only the files required to complete the current task.

Avoid unrelated formatting changes, file reorganizations, or broad refactoring unless explicitly requested.
