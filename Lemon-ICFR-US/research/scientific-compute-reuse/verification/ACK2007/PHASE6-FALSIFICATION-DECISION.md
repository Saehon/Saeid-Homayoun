# ACK2007 Phase 6 — Verification & Falsification Decision

Decision: **REVISE — NOT ADMITTED TO M1**

## Gate results

1. Compiler artifact integrity — PASS at source-review level.
   - Explicit intercept and 14 coefficients.
   - Deterministic sigmoid.
   - Strict required/unknown/nonfinite input validation.
   - No fitting/tuning code.

2. Unit-test specification — PASS at test-design level.
   - Tests cover coefficient count/intercept, zero vector, single coefficient, missing/unknown/nonfinite input, sigmoid bounds.
   - IMPORTANT: test files existing is not evidence they executed.

3. GitHub CI execution evidence — FAIL / NO EVIDENCE.
   - Query of workflow runs for commit ec53a6496ce8d92d9cb20303a7a5c2854b193aff returned no workflow runs.
   - Combined commit statuses also returned no statuses.
   - Therefore CI MUST NOT be described as passing.

4. Frozen synthetic fixture — CREATED.
   - ZERO: arithmetic/intercept check only.
   - AUDITOR_RESIGN_ONLY: single-coefficient check.
   - SCHEMA_VALID: deterministic synthetic vector.
   - These fixtures are not firms and produce no empirical evidence.

5. Provenance — PARTIAL PASS.
   - Published coefficient vector/intercept and author-continuity operational definitions are recorded.
   - RZSCORE raw construction/reference-sample sub-gate remains open.

6. Estimand falsification — WARNING.
   - ACK2007 mixes exposure to ICD existence with discovery/reporting incentives.
   - It must not be relabeled as a pure latent-MW model.

7. Transportability — NOT TESTED.
   - No frozen compatible external firm-year dataset has been executed.
   - No calibration, PR-AUC, Brier, temporal stability or regime-shift result exists yet.

## Falsification tests registered
- Missing variable -> must reject.
- Unknown variable -> must reject.
- NaN/infinite -> must reject.
- Scaling mismatch -> provenance failure.
- RZSCORE raw-construction mismatch -> block raw pipeline.
- Post-SOX/regime transport -> empirical test required.
- Outcome mismatch -> reject flat ensemble.
- Synthetic fixture -> compiler validation only, never performance evidence.

## Admission rule
ACK2007 remains LEMON-SCI-ESM-001 EXECUTABLE-CANDIDATE.
M1 admission requires:
A. observed CI/test execution evidence;
B. provenance closure or explicit preconstructed-RZSCORE boundary;
C. frozen target-dataset compatibility decision;
D. deterministic fixture execution/checksum;
E. human scientific gate.

Current verdict: REVISE.
