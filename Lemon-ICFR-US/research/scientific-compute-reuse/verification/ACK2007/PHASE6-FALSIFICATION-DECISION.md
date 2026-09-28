# ACK2007 Phase 6 — Verification & Falsification Decision

Decision: **REVISE — NOT ADMITTED TO M1**

## Gate results
1. Compiler artifact integrity — PASS at source-review level.
2. Unit-test and frozen-fixture execution — requires observed CI/test evidence on the candidate commit. Prior successful workflow evidence does not automatically carry forward after gate-architecture changes.
3. Provenance — PARTIAL / RAW CONSTRUCTION BLOCKED.
   - Canonical raw-construction authority: `source-definition-recovery/ACK2007-construction-gates.json`.
   - Fail-closed enforcement: `verification/ACK2007/ack2007_admission_validator.py`.
   - SIZE: BLOCKED_MISSING_YEAR_RULE.
   - RGROWTH: BLOCKED_MISSING_DATA_RULE; canonical definition is decile rank of average sales growth rate, 2002–2004.
   - RZSCORE: BLOCKED_RAW_CONSTRUCTION.
   - Other ACK2007 inputs remain governed by their explicit registry status; absence from the registry is a hard failure.
4. Estimand — WARNING: mixed ICD existence/discovery/reporting; not a pure latent-MW model.
5. Transportability — NOT TESTED.

## Authority boundary
The construction-gate registry is the single machine-readable authority for whether an ACK2007 model input may be constructed from raw data.

The ontology, resolved-variable map, Phase-4 recovery record, and Evidence Passport remain scientific/provenance evidence. They must not be interpreted as independent executable admission logic.

Frozen synthetic fixtures are a separate software-determinism path. They use preconstructed synthetic model inputs and therefore do **not** call the raw-construction validator.

## Falsification tests registered
- Registry must cover the exact ACK2007 model-input set.
- Duplicate registry keys -> reject.
- Unknown requested model input -> reject.
- Any requested raw construction whose status is not VERIFIED -> reject.
- SIZE missing-year rule unresolved -> reject raw construction.
- RGROWTH missing-data/ranking eligibility unresolved -> reject raw construction.
- RZSCORE raw-construction/reference-sample rule unresolved -> reject raw construction.
- Frozen-fixture missing/unknown/nonfinite input -> reject.
- Frozen-fixture schema drift or duplicate headers -> reject.
- Scaling mismatch -> provenance failure.
- Outcome mismatch -> reject flat ensemble.
- Synthetic fixture -> compiler validation only; never empirical performance evidence.

## Admission rule
ACK2007 remains LEMON-SCI-ESM-001 EXECUTABLE-CANDIDATE.

M1 admission requires:
A. observed CI/test execution evidence on the candidate commit;
B. raw-construction requests pass the canonical fail-closed construction-gate validator, OR the target dataset is explicitly treated as preconstructed input and passes a separate provenance/compatibility decision;
C. frozen target-dataset compatibility decision;
D. deterministic compiler/fixture execution and checksum;
E. human scientific gate.

No documentation-only exception can satisfy Gate B. `model.yaml` points to the canonical registry rather than duplicating a hand-maintained unresolved-variable list.

## Current verdict
**REVISE / HOLD.**

Technical compiler execution and raw scientific construction are intentionally separate. Successful fixture execution cannot be used to infer that unresolved raw variables are scientifically constructible.
