# NAAIL hourly run — Q5 protocol-validity verification

- Start: 2026-10-04T14:28:38+02:00
- End: 2026-10-04T14:30:56+02:00
- Scope: Q5 Microsoft COVID only
- Canonical working-branch HEAD read: `580f6d9f6f3c48f5db2511b0e4a5b052968ad64d`
- Q5 PR branch HEAD before: `13e6b215547fea789f68b6174933ee782911caaf`
- Q5 PR branch HEAD after repair-queue record: `2149b667c2de4656145f2f605da1f0d131bc3996`
- Lock: expired; owner `interactive-session-q5-pr-consolidation`; expiry `2026-10-02T15:06:00+02:00`

## Live-state reconstruction

- PR #101: OPEN; no mutation in this packet.
- PR #103: OPEN; one PR retained for Q5 scope.
- PR #104: MERGED at one-file infrastructure scope.
- R3/Q5 workflow dispatch: NOT PERFORMED.
- Q6: unchanged, WAITING_FOR_USER.
- Canonical ledger: POC 7/10 Met + 3 Partial; V1 0/10 Met.
- POC_COMPLETE = FALSE.
- V1_COMPLETE = FALSE.

## Independent-review decision applied

- `Q5_PROTOCOL_DECISION = REJECT_V1_PREREGISTRATION`
- `CREATE_VERSIONED_V2_WITH_UNOBSERVED_HOLDOUT = NO` for the POC
- `GPT_MAY_PROCEED_WITH_R3 = NO`

The v1-R package was inspected without SEC retrieval. Verified fingerprints:

- v1 historical rule: `d7760b4909ae84896cae8797fb8536f59d36053c`
- v1-R protocol: `4851cbac193eb222f7bccd6c02c46e396b91f003`
- v1-R scanner: `ffb3f6401fa45491aec400ee92147f1a8d84a5b6`
- prior-exposure guard workflow: run `37201762703`, job `111434733660`, SUCCESS
- guard steps: protocol JSON PASS; scanner py_compile PASS; prior-exposure guard PASS

This is static/governance evidence only. It is not COVID-result evidence and does not change a scientific gate.

## New governance-critical finding

Main now contains manual workflow blob `82db9f718e48a1e1946026a7fa83c47eb7d559f7`. It still invokes the rejected historical `msft_covid_scan.py`, while the Q5 registry marks v1 `REJECTED_V1_PREREGISTRATION`, `active_for_execution=false`, and `prior_exposure=true`.

Therefore the current main workflow must not be dispatched.

## Repair queue

Created and read back `hourly-build/OPEN_REPAIR_QUEUE.md` with:

1. `Q5-PROTOCOL-VALIDITY-001`
2. `Q5-MAIN-WORKFLOW-REJECTED-V1-001`

Queue blob after timestamp correction: `cb1feaf0c1af9f29fa976c2904c510909b855f75`.

Persistent same-blocker fail count: 0 for both new-evidence blockers. No two-failure suppression was triggered in this packet.

## Next executable action

Wait for Claude to return separate v1-R protocol/scanner/prior-exposure-control decisions and explicit authorized blobs. Proceed only if `GPT_MAY_PROCEED_WITH_V1R_REDERIVATION = YES`. Until then, do not dispatch the current main workflow.

## Dual save

- GitHub: pending readback of this record.
- Google Drive Hourly Build Master Log: pending append/readback.
