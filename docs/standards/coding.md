# Coding Standard

Correctness is mandatory. Clarity, structure, and maintainability take priority over speed and cleverness.

## Language and Style

* Write clean, readable YAML.
* Keep Jinja templates simple and easy to understand.
* Use Python only when YAML or native Home Assistant functionality cannot reasonably solve the problem.
* Prefer explicit solutions over compact or clever implementations.
* Follow the formatting conventions of the language being used.

## Naming

| Entity             | Convention                       |
| ------------------ | -------------------------------- |
| Files              | `kebab-case.yaml`                |
| Entity IDs         | `snake_case`                     |
| Variables          | `snake_case`                     |
| Constants          | `UPPER_SNAKE_CASE`               |
| Scripts            | Verb + object (`turn_on_fan`)    |
| Automations        | Human-readable descriptive names |
| Template variables | `snake_case`                     |

## Core Principles

* Single Responsibility: one automation, script, sensor, or template should have one clear purpose.
* Keep logic small and focused.
* Prefer simple, readable solutions over clever implementations.
* Eliminate duplication only when it is real and recurring.
* Do not introduce abstractions before they are needed.
* Optimize for maintainability rather than minimizing line count.

## YAML

* Use consistent indentation (2 spaces).
* Group related configuration together.
* Keep files organized and easy to scan.
* Avoid deeply nested structures whenever possible.
* Prefer readability over compact formatting.

## Jinja Templates

* Keep expressions easy to read.
* Use local variables for complex calculations.
* Avoid nested conditional expressions where possible.
* Handle `unknown`, `unavailable`, and `None` safely.
* Avoid repeating identical template logic.

## Python

* Follow PEP 8.
* Keep functions short and focused.
* Prefer descriptive names over abbreviations.
* Use type hints where appropriate.
* Avoid unnecessary classes or abstractions.
* Use standard library functionality before introducing dependencies.

## Imports

* Import standard library modules first.
* Then third-party libraries.
* Finally local modules.
* Remove unused imports.

## Error Handling

* Never ignore exceptions silently.
* Validate assumptions before using entity states or input values.
* Fail safely when unexpected data is encountered.
* Log unexpected errors with sufficient context.

## Comments

* Write comments to explain **why**, not **what**.
* Keep comments accurate and up to date.
* Remove obsolete comments.
* Do not leave `TODO` comments without a corresponding plan item.

## Code Organization

* Keep related logic together.
* Avoid duplicated code across automations, scripts, or templates.
* Prefer reusable helpers over copy-paste.
* Break large files or functions into smaller logical units when readability improves.

## Dependencies

* Prefer built-in functionality before introducing additional dependencies.
* Remove unused dependencies.
* Document any significant external dependency before introducing it.
