# OPEN REPAIR QUEUE — NAAIL Research Assurance MCP

Last verified: 2026-10-04T14:32:00+02:00  
Scope in this revision: Q5 Microsoft COVID only

## Q5-PROTOCOL-VALIDITY-001

- Classification: SCIENTIFIC_VALIDITY / WAITING_FOR_INDEPENDENT_REVIEW
- State: OPEN
- Persistent same-blocker fail count: 0
- Retry suppression: do not execute or dispatch while open
- Evidence:
  - Claude decision: `Q5_PROTOCOL_DECISION = REJECT_V1_PREREGISTRATION`
  - Claude decision: `CREATE_VERSIONED_V2_WITH_UNOBSERVED_HOLDOUT = NO` for the POC
  - Claude decision: `GPT_MAY_PROCEED_WITH_R3 = NO`
  - v1 rule blob: `d7760b4909ae84896cae8797fb8536f59d36053c`
  - v1-R protocol blob: `4851cbac193eb222f7bccd6c02c46e396b91f003`
  - v1-R scanner blob: `ffb3f6401fa45491aec400ee92147f1a8d84a5b6`
  - prior-exposure guard CI: run `37201762703`, job `111434733660`, SUCCESS
- Affected dependencies: Q5 result; Microsoft combined POC proof; Q7 final determination; POC freeze.
- Exact future repair action:
  1. Obtain independent Claude decisions for the v1-R protocol, scanner and prior-exposure control.
  2. Require explicit authorized protocol/scanner blobs.
  3. Proceed only if Claude explicitly returns `GPT_MAY_PROCEED_WITH_V1R_REDERIVATION = YES`.
  4. Keep any result at `HUMAN_REVIEW` or `FLAGGED` until independent snippet review.

## Q5-MAIN-WORKFLOW-REJECTED-V1-001

- Classification: GOVERNANCE_CRITICAL / EXECUTION_PATH_MISMATCH
- State: OPEN
- Persistent same-blocker fail count: 0
- Retry suppression: do not invoke the current main-branch workflow
- Evidence:
  - PR #104 merged the manual workflow on 2026-10-04.
  - Main workflow blob: `82db9f718e48a1e1946026a7fa83c47eb7d559f7`.
  - The workflow still runs `derived/msft_covid_scan.py`, the rejected v1 path.
  - The Q5 registry marks `NAAIL-MSFT-COVID-RULE-V1` as `REJECTED_V1_PREREGISTRATION`, `active_for_execution=false`, and `prior_exposure=true`.
- Affected dependencies: safe Q5 dispatch; provenance; scientific-validity gate.
- Exact future repair action:
  1. Do not dispatch the current main workflow.
  2. After independent v1-R approval, amend the existing Q5 PR #103 workflow so it verifies the authorized v1-R protocol/scanner blobs and the registry execution state before running.
  3. If v1-R is rejected, preserve the historical workflow as non-executable or replace it only through explicit human-approved governance.
  4. Never treat the PR #104 merge itself as authorization to execute.

## Two-failure rule status

No blocker reached two new failed attempts in this packet. The queue entries above were created from new evidence and are not PASS states. Known dependent outputs remain quarantined.
