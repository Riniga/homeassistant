# Complete an MVP

Use this prompt when all implementation phases for an MVP are completed and the work should be prepared for a final commit.

## Prompt

    Complete the MVP and prepare it for a final commit.

    Read:

    * `docs/development/methodology.md`
    * `docs/development/tools.md`
    * `docs/standards/coding.md`
    * `docs/standards/testing.md`
    * `docs/standards/git.md`
    * `docs/standards/documentation.md`
    * `docs/architecture/overview.md`
    * the relevant MVP document in `docs/mvp/`
    * the relevant implementation plan in `docs/plans/`

    Review the full change set.

    Check that:

    * the MVP goal is fulfilled
    * all acceptance criteria are met
    * the implementation plan is completed and updated, with each phase's status recorded
    * desktop-level checks have passed (see `docs/standards/testing.md`)
    * any Home Assistant-level validation (`ha core check`, template testing, functional verification) has been clearly identified, and completed where practical
    * code follows the coding standard
    * the solution is simple and understandable
    * no unnecessary complexity has been introduced
    * no unrelated changes are included, and no operational Home Assistant configuration was touched unless the MVP explicitly required it
    * documentation is updated, with no information duplicated across documents
    * `docs/architecture/overview.md` is updated if the implemented structure changed
    * ADRs are added under `docs/architecture/decisions/` for significant architectural decisions — not for routine or self-explanatory changes
    * README is updated if needed
    * no secrets, temporary files, or generated artifacts are committed

    If anything is missing, fix it.

    After fixing, run the relevant validation again.

    Never claim that Home Assistant configuration has been validated, or that an automation or device behaviour works, unless it was actually tested — static inspection alone is not enough.

    When everything is ready, provide:

    1. Summary of completed work
    2. Validation performed, and any validation still required from the user (Home Assistant checks, physical-device verification)
    3. Documentation updated
    4. Remaining risks or open questions
    5. Suggested commit message(s)

    This project uses a direct-to-`main` workflow (see `docs/standards/git.md`) — no feature branches or pull requests. Do not commit or push without explicit approval.
