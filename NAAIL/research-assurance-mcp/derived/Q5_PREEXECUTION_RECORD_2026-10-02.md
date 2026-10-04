# Q5 — Microsoft COVID scan pre-execution record

Date: 2026-10-02
State: WAITING_FOR_EXECUTION

## Frozen rule verification
- Path: `derived/covid_rule_v1.json`
- Expected Git blob: `d7760b4909ae84896cae8797fb8536f59d36053c`
- Current PR-B Git blob: `d7760b4909ae84896cae8797fb8536f59d36053c`
- Frozen commit: `a7e999a6880fd8f9b6f9616faad93f4b769904dd`
- File read at frozen commit is byte-identical to the PR-B rule.
- Rule status remains `FROZEN_PREREGISTERED`; no post-result change has been made.

## Secret
- `EDGAR_IDENTITY`: USER-REPORTED added to Repository secrets.
- Secret value is not recorded here.
- Availability to the workflow is not yet CI-EVIDENCE because the dedicated workflow has not executed.

## Dedicated workflow
- Path: `.github/workflows/naail_msft_covid_scan.yml`
- Trigger: `workflow_dispatch` only.
- The workflow verifies the frozen rule blob before executing the scan.
- Q5 is isolated from the P7 regression workflow.

## Execution blocker
The dedicated workflow is not present on the default branch `main` and has never run. GitHub accepts `workflow_dispatch` only when the workflow file exists on the default branch. Therefore no compliant manual run can currently be created from PR B without first registering the workflow on `main`.

No workaround was used:
- regression workflow not re-run;
- no push/pull_request trigger added;
- no local SEC scan substituted;
- no direct write or merge to `main`;
- frozen rule unchanged.

## Gate state
Microsoft COVID remains `PARTIAL`.
POC criteria met: 7 of 10.
POC_COMPLETE = FALSE.
V1_COMPLETE = FALSE.
