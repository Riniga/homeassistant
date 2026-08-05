# Validation and Testing Standard

The goal is to ensure that configuration changes are syntactically valid, behave as intended, and do not disrupt existing Home Assistant functionality.

Testing should be proportional to the risk and complexity of the change.

## Validation Levels

### 1. Static Review

All changes must be reviewed for:

* Correct YAML indentation and structure
* Correct entity IDs and service/action names
* Consistent naming
* Safe handling of `unknown`, `unavailable`, and missing values
* Unintended changes outside the requested scope
* Exposed credentials or other sensitive information

Static review can be performed on the development computer.

### 2. Home Assistant Configuration Validation

Changes affecting Home Assistant configuration must be validated in the Home Assistant environment.

Use either:

* **Settings → Developer tools → YAML → Check configuration**
* The Home Assistant CLI:

```bash
ha core check
```

A successful configuration check is required before restarting Home Assistant. Home Assistant documents that configuration validation checks YAML syntax and configuration structure.

### 3. Template Validation

Jinja templates must be tested using the Home Assistant template editor when practical:

```text
Developer tools → Template
```

Test:

* Normal expected input
* `unknown`
* `unavailable`
* Missing or empty values
* Relevant boundary values

### 4. Functional Verification

Changes must be verified in the running Home Assistant instance when their behaviour depends on entities, devices, integrations, timing, or state changes.

Functional verification may include:

* Manually running a script
* Manually triggering an automation
* Changing a helper or test entity
* Confirming expected entity states
* Reviewing automation traces
* Reviewing Home Assistant logs
* Confirming that the physical device behaves correctly

Do not perform unsafe tests on physical equipment.

## Test Requirements

| Change                    | Minimum verification                                                              |
| ------------------------- | --------------------------------------------------------------------------------- |
| Documentation only        | Review rendered Markdown                                                          |
| Dashboard change          | Open affected dashboard and verify layout and behaviour                           |
| Simple YAML change        | Static review and configuration validation                                        |
| Template change           | Configuration validation and template editor test                                 |
| Script change             | Configuration validation and manual script execution                              |
| Automation change         | Configuration validation, trigger test, and trace review                          |
| Integration configuration | Configuration validation, runtime verification, and log review                    |
| Bug fix                   | Reproduce the original problem when practical and verify that it no longer occurs |
| Refactoring               | Verify that existing behaviour remains unchanged                                  |

## Automation Testing

When testing an automation:

* Verify each relevant trigger.
* Verify important conditions.
* Verify the expected action.
* Verify that the automation does not run under incorrect conditions.
* Review the automation trace after execution.
* Consider restart, unavailable-device, and repeated-trigger scenarios where relevant.

Testing only the action section is not sufficient when the trigger or conditions have changed.

## Regression Testing

Every bug fix should include a documented verification of the original failure scenario when practical.

Automated regression tests are not required for normal YAML configuration, but the test performed should be noted in the implementation plan or pull request.

## Python

Custom Python code and custom integrations should use automated tests where practical.

* Use `pytest`.
* Keep tests deterministic and isolated.
* Mock Home Assistant services, devices, and external APIs.
* Include regression tests for bug fixes.
* Follow Home Assistant's current testing conventions when developing custom integrations. Home Assistant's developer documentation uses `pytest` for local testing.

## Test Data

* Do not use real credentials in test data.
* Avoid changing production entities solely to create test conditions when helpers or templates can be used instead.
* Restore temporary test values after verification.
* Do not leave test automations, entities, or debug logging enabled unintentionally.

## Before Commit

Before committing a configuration change:

* Review the diff.
* Confirm that only intended files changed.
* Perform all validation possible from the development computer.
* Document any validation that must be completed after deployment.

## Before Restart or Reload

Before reloading configuration or restarting Home Assistant:

* Synchronize the intended files.
* Run the Home Assistant configuration check.
* Review the affected configuration.
* Ensure that rollback is possible.
* Prefer reloading only the affected configuration domain when supported.

## After Deployment

After applying the change:

* Verify the affected functionality.
* Review automation traces when relevant.
* Check Home Assistant logs for new warnings or errors.
* Confirm that unrelated functionality remains operational when the change has wider impact.

A change is not considered verified until all applicable checks have passed.

## Working with AI Assistants

The assistant must:

* State how a change can be validated.
* Distinguish between checks possible on the development computer and checks requiring Home Assistant.
* Never claim that runtime behaviour has been tested unless it was actually tested.
* Avoid inventing test commands or assuming that desktop validation proves Home Assistant compatibility.
* Highlight changes that require physical-device verification.
* Never restart, reload, or operate devices without explicit approval.
