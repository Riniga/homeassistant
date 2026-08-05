# Git Workflow

The goal is to keep every change small, traceable, reviewable, and safe to deploy.

## Branches

* Always work on a branch. Never work directly on `main`.
* `main` always represents the latest stable Home Assistant configuration.
* Use short, descriptive branch names based on the work being performed.

Recommended prefixes:

```text
feature/<short-name>
fix/<short-name>
docs/<short-name>
refactor/<short-name>
chore/<short-name>
```

Examples:

```text
feature/energy-dashboard
feature/presence-detection
fix/ventilation-automation
docs/update-coding-standard
chore/update-hacs-integration
```

## Commits

* Commit after each completed and verified task.
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

## Pull Requests

* Create pull requests against `main`.
* Keep pull requests focused on a single purpose.
* Describe what changed and why.
* Include documentation updates when the change affects behaviour, configuration, or workflow.
* Verify that the configuration has been validated before merging.

## Push and Merge Rules

* Do not push or merge without explicit approval when working with an AI assistant.
* Never force-push shared branches unless explicitly agreed.
* Prefer many small pull requests over large mixed changes.

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
* Never commit, push, merge, or delete branches without explicit approval.
* Preserve existing behaviour unless the task explicitly requires a change.

## Recommended Daily Workflow

```bash
git status
git switch main
git pull
git switch -c feature/<short-name>
```

Implement and validate a small, complete change.

```bash
git add <files>
git commit -m "Add descriptive commit message"
git push -u origin feature/<short-name>
```

Create a pull request against `main` when the change is complete and verified.

## Scope of Changes

The assistant should modify only the files required to complete the current task.

Avoid unrelated formatting changes, file reorganizations, or broad refactoring unless explicitly requested.