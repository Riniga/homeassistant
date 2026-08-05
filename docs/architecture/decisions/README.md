# Architecture Decision Records

This folder records significant, lasting architectural decisions for this repository — the kind that would otherwise get re-debated or silently reversed because nobody remembers why they were made.

Per `docs/standards/documentation.md`, ADRs are reserved for decisions that are genuinely architectural and lasting. Not every change needs one — a folder rename, a naming tweak, or an obvious bug fix does not. Use judgment: if a future contributor (human or AI) would reasonably ask "why is it done this way?", it probably belongs here.

## Format

Each ADR is a single Markdown file:

```text
NNNN-short-title.md
```

* `NNNN` — a zero-padded, sequential four-digit number (`0001`, `0002`, ...). Numbers are never reused, even if a decision is later superseded.
* `short-title` — kebab-case, a few words.

### Template

```markdown
# NNNN. Short title

## Status

Proposed | Accepted | Superseded by [NNNN](NNNN-other-title.md)

## Context

What is the situation that calls for a decision? What forces or constraints are in play?

## Decision

What was decided.

## Consequences

What becomes easier or harder as a result. Include trade-offs honestly, not just benefits.
```

## When to Add One

Add an ADR when a decision:

* Changes the overall repository structure or a core convention.
* Chooses between two or more real alternatives with lasting trade-offs.
* Would be genuinely confusing to reverse-engineer from git history alone.

Do not add one for:

* Routine file additions, renames, or moves that are self-explanatory from their commit message.
* Small, easily reversible choices.
* Anything already fully explained in `docs/architecture/overview.md` or another standards document.

## Status Values

* **Proposed** — under consideration, not yet acted on.
* **Accepted** — the decision is in effect.
* **Superseded by NNNN** — replaced by a later ADR; keep the original file for history, don't delete it.
