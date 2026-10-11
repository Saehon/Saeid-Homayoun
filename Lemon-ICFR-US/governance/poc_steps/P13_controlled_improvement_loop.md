# P13 — Controlled improvement loop

## What was done

Executed the committed `tools/improvement_gate.py` twice against explicitly labelled `SYNTHETIC_TEST_ONLY` fixtures: once with a deliberately worse candidate and once with the baseline compared with itself. The worse candidate was rejected for increasing false negatives and failing the required recall margin. The baseline self-comparison was rejected because it was not an improvement. Repository and P11-registry searches found no provenance-verified real frozen development-benchmark metrics record compatible with the gate schema, so no empirical improvement run or promotion was claimed.

## Files changed

- `organized/poc/improvement_gate/P13_SYNTHETIC_BASELINE.json`
- `organized/poc/improvement_gate/P13_SYNTHETIC_WORSE_CANDIDATE.json`
- `organized/poc/improvement_gate/P13_RESULTS.json`
- `governance/OPEN_REPAIR_QUEUE.md`
- `governance/poc_steps/P13_controlled_improvement_loop.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-11_R202610110404-P13.md`

## POC demonstration (command + REAL output excerpt)

`python tools/improvement_gate.py ...P13_SYNTHETIC_BASELINE.json ...P13_SYNTHETIC_WORSE_CANDIDATE.json --frozen-sha SYNTHETIC_P13_FROZEN_V1` → `REJECT`; `candidate increases false negatives`; `no improvement ≥ 0.01 on recall`. Baseline versus itself → `REJECT`; `no improvement ≥ 0.01 on recall`. Baseline SHA-256: `09804b18a5bebbbc03b0a13c4dbc75471f8e2f5046f93e473baf5e5b0377075d`; worse-candidate SHA-256: `9defb52bb8120c9c4cbb692a02c285a1e41099c05acb68d494da186a9b28fef1`.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting authoritative SHA: `d4f8e11a74b4aada8c5ceeb2a9c6217bbe2fd6f4`.
- POC unittest suite, including `test_improvement_gate`: `18 tests`, 0 failed, 0 errors, 0 skipped.
- Full exact-test harness over the unchanged assurance, POC and orchestrator tests: `84 tests, 33 subtests`; 0 failed, 0 errors, 0 skipped.
- Direct pytest was unavailable in this runtime (`No module named pytest`); the repository's exact test functions were executed with Python `unittest` plus `FunctionTestCase` for the nine pytest-style orchestrator functions. No test was changed or weakened.

## Problems found (ORQ ids, or "none")

`ORQ-018` opened: the real frozen development-benchmark outputs needed for an empirical baseline/candidate comparison are absent. The synthetic execution verifies only gate mechanics and cannot support an improvement claim.

## Decisions made without review (list every one)

Used the numerical synthetic fixtures already encoded in the committed P13 unit test, labelled every artifact `SYNTHETIC_TEST_ONLY`, and applied the implementation map's required `PARTIAL` status because no real compatible frozen benchmark was available. Did not accept a candidate, promote to production, or describe the synthetic outcome as scientific evidence.

## Phase status: PARTIAL

The required guard behaviours are demonstrated, but the real benchmark-gated improvement comparison was not executable. The output remains quarantined from empirical and production claims and P13 moves forward under the program's fail-forward rule.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY; SYNTHETIC_TEST_ONLY. ACK2007 remains SCIENTIFIC_HOLD. No scientific PASS, empirical improvement, production promotion, independent review, human approval, or merge is claimed.
