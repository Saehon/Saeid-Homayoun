# B2 Claude Review Package — Duplicate Case Correction

Date: 2026-10-05  
Status requested: independent review of an additive historical correction.

PR: [#128](https://github.com/Saehon/Saeid-Homayoun/pull/128)  
Validated commit: `95f0207441ef358df17357d02bc3ee36d81fc42f`  
Base: `main` at `d48faf52bd27a6796063f10b73657eb1d9cf384b`

## Scope and boundary

This package records that RUN 021 mislabeled canonical Case 001 as Case 002 and RUN 022 continued work on that same duplicated selection. The valid additional V1 case count contributed by those runs is zero. Historical records are immutable and remain unchanged; the replacement Case 002 remains unassigned for later human selection.

No candidate search, data retrieval, case selection, replication, detector change, or scientific claim is included.

## Evidence anchors

| Evidence | Git blob |
| --- | --- |
| RUN 021 | `9bd1330bcaf3ad66fd2ae38dbd1e37ddf1b5982d` |
| RUN 022 | `52e1db3cb1282eabd21273c442cfe6c56046aa9a` |
| Prior additive correction | `4650da0587356f1c07c075eebea3f43833edbf86` |
| Independent-review handoff | `56079783f78fd934fd946fb88d8189d02c68b413` |

## Proposed-file fingerprints

| File | Git blob | SHA-256 |
| --- | --- | --- |
| `duplicate_case_002_correction_v1.json` | `3b821c02ace59f391c08692cfdc29a15c9f9bc8e` | `7eb9f887d1ddb6561a129338e39aefffac39b0542f1d0ea89819b25f7b4bef60` |
| `DUPLICATE_CASE_002_CORRECTION_2026-10-05.md` | `ef6658f89a3f2d13fe2263adbc9cdd59bcb5a3f5` | `eaaa49706e2003b26ee60e2c2731e343200137f6b7763911362c028cabbc3619` |
| `test_b2_duplicate_case_correction.py` | `c6b8695d5448e4c2af0d3ff66d7e51aa13e075dd` | `1b7ccbc180b4179e3de672369396b7730cb28d07dc4f0357fe8e8997212c61d1` |
| `naail_v1_b2_duplicate_case_correction.yml` | `8f85a278a28dd3c86e95932ffe8959444cd8956e` | `466e8cb98dd3a9a1bdccb6c6256bc7cd01a3117a0a0f3bd2f7afa6ef975cbf4b` |

## Local validation

- Python compile: exit 0.
- Additive-correction invariant suite: exit 0, `B2 duplicate-case correction invariants: PASS`.

## Authoritative CI evidence

- Single authorized run: [37284788607](https://github.com/Saehon/Saeid-Homayoun/actions/runs/37284788607), run number 1, `success`.
- Job: `111680989301`, `b2-duplicate-case-correction-guard`, `success`.
- Validated commit: `95f0207441ef358df17357d02bc3ee36d81fc42f`.
- Successful steps: compile correction guard; validate additive-correction invariants.

## One-run control

The guard workflow listens only to the pull request `opened` event. It excludes `synchronize`, `reopened`, `push`, and `workflow_dispatch`, so this review-package finalization cannot repeat the test. No rerun is authorized to select a result.

## Review questions

1. Does the correction accurately preserve RUN 021/022 while removing them from valid V1 case counts?
2. Are the evidence anchors sufficient and correctly bounded?
3. Is the unassigned Case 002 boundary clear enough to prevent implicit case selection?

`POC_COMPLETE = FALSE`; `V1_COMPLETE = FALSE`.
