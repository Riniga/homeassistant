# Create an Implementation Plan

## Prompt

Create an implementation plan for:

```text
docs/mvp/mvp-003-visuell-design.md
```

Before creating the plan, read:

* `docs/development/methodology.md`
* `docs/architecture/overview.md`
* `docs/standards/coding.md`
* `docs/standards/testing.md`
* `docs/standards/git.md`
* `docs/standards/documentation.md`

### Requirements

* Important, this plan needs to be able to consider, use of correct AI model as some of the tasks is to create a very appealing visual design for the site.
* Create a complete but simple implementation plan.
* Break the work into small TODOs.
* Group TODOs into logical phases.
* Suggest a commit message for each phase.
* Keep each TODO small enough to implement and verify independently.
* Identify files likely to change.
* Do **not** write implementation code.

### Output

Save the plan as:

```text
docs/plans/003-visuell-design.plan.md
```

(the plan number matches the MVP's number — `docs/mvp/mvp-003-visuell-design.md` → `docs/plans/003-visuell-design.plan.md` — per `docs/development/methodology.md`)

Use this structure:

1. Goal
2. Assumptions
3. Proposed file changes
4. Implementation phases with TODOs
5. Risks / Open questions

---

## Workflow

1. Create or select an MVP.
2. Create the implementation plan.
3. Review and adjust the plan.
4. Implement one phase at a time.
5. Commit after each completed phase, directly to `main` (see `docs/standards/git.md` — no feature branches or pull requests).
6. Run tests and update documentation.
7. Once all phases are done, use `docs/claude-prompts/3-complete-mvp.md` to prepare the final commit.
