# B5 Claude Review Package — Human Ground-Truth Protocol

Date: 2026-10-05  
PR: [#123](https://github.com/Saehon/Saeid-Homayoun/pull/123)  
Validated commit: `ee893f02430576a7cc3e7ce3c125449b407c8f02`  
Base: `main` at `d48faf52bd27a6796063f10b73657eb1d9cf384b`  
Status requested from Claude: independent review of a **DRAFT protocol only**.

## Review boundary

No item was selected, authored, retrieved, released, coded, adjudicated, or scored. No system output or scientific claim was produced. The operator has seen the detector and disclosed Benchmark V2 examples and is excluded from holdout authorship, coding, adjudication, case selection, and ground-truth decisions.

Execution is blocked until all three conditions are recorded: human POC approval, Claude approval of the B5 protocol, and a pre-data freeze with the required fingerprints.

## Files and fingerprints

| File | Git blob | SHA-256 |
| --- | --- | --- |
| `v1-preparation/b5/human_ground_truth_protocol_v1.json` | `4304cd857454c681bf8a94c296bf11121858e4e1` | `55e9a80d5a01a53d9dc524ea948ca934de8323a7f57cedbf3a81aed131058a6` |
| `v1-preparation/b5/human_ground_truth_preregistration_template_v1.json` | `85aa486489bc2b4a8e4adc9e66791dd38cb8fd05` | `c8da134aa5abbacb50ff4b90e50e1fee910b160293fd2d2888068d30eddd02c8` |
| `v1-preparation/b5/HUMAN_GROUND_TRUTH_PROTOCOL_V1.md` | `d0bb03a9bc54d5840f4f881696c868514a1f0150` | `acb820ac2fc07f2dd584b5d1d7911c8f4970df863d9885355cea27604bef18ee` |
| `tests/test_b5_human_ground_truth_protocol.py` | `021e153fef2c23ad4cb7e5cf37a650786a0628ba` | `79d10ca2d579e55884dc524ea948ca934de8323a7f57cedbf3a81aed131058a6` |
| `.github/workflows/naail_v1_b5_human_ground_truth_protocol.yml` | `6d795f74d9a4142004de746694ad7210ce84e1dc` | `2b7195d58855b6638098645c9f05e385d66724325a89491784d5d50bb8bd19a3` |
| `derived/OPEN_REPAIR_QUEUE.md` | `e5c37c7b0e141db0d6924839c0108bfbd77917ee` | `69837176d30726ef1168fdb2dc0d5f6d23ef139d97dd4780d7708efe74952441` |

## Preregistered decisions for review

1. Two independent coders label each eligible scored item under blinding.
2. Objective fields remain separate from judgment-dependent fields.
3. Unweighted Cohen's kappa is computed before adjudication for eligible `error_present` and `error_category` labels.
4. The minimum threshold is `kappa >= 0.70`.
5. Undefined kappa is reported as `UNDEFINED` and does not meet the threshold.
6. A below-threshold affected ground truth remains `PRELIMINARY` and `HUMAN_REVIEW` and cannot support confirmatory system claims.
7. Raw coder labels are immutable before reliability computation; a separate adjudicator records every resolution or leaves it `HUMAN_REVIEW`.
8. Missing labels and exclusions remain in the manifest with reasons; no silent exclusion is permitted.
9. A material protocol or codebook change requires a new version and new pre-data fingerprints.
10. One agreement calculation and one adjudication release are permitted for each frozen label set and protocol version.

## Governance amendment recorded

The human direction that hourly runs continue by fail-forward and that V1 preparation may proceed while POC items wait on human or Claude is recorded verbatim in the protocol narrative. It does not upgrade any gate. `POC_COMPLETE` and `V1_COMPLETE` remain false.

## Validation evidence

- Local `py_compile`: exit 0.
- Local deterministic invariant guard: exit 0, `B5 human ground-truth protocol invariants: PASS`.
- The unavailable local optional `pytest` dependency was recorded as `NAAIL-B5-LOCAL-PYTEST-001`, attempt 1 of 2, and repaired with a materially different dependency-free harness.
- Single authoritative GitHub Actions run: [37256377004](https://github.com/Saehon/Saeid-Homayoun/actions/runs/37256377004), attempt 1, `success`.
- Job: `111594244234`, `b5-protocol-guard`.
- The CI-triggering files were not changed after this run; this review package is outside the workflow path filter.

## Questions for Claude

1. Is the separation of objective and judgment-dependent labels sufficient for the intended V1 evidence claim?
2. Is the pre-adjudication unweighted kappa rule and `0.70` minimum defensible as frozen, including the undefined-kappa rule?
3. Are the blinding, missingness, deviation, and adjudication controls sufficient to prevent system-output leakage and silent exclusion?
4. Does the prior-exposure declaration adequately exclude the operator from scientific ground-truth creation?

Until Claude and the human act, B5 remains a draft preparation artifact and authorizes no execution.
