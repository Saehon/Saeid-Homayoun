# ACK2007 Phase 6 — Verification & Falsification Decision

Decision: **REVISE — NOT ADMITTED TO M1**

## Gate results
1. Compiler artifact integrity — PASS at source-review level.
2. Unit-test and frozen-fixture execution — PASS at engineering level on the latest verified successful ACK workflow before this gate edit; synthetic fixtures are compiler checks only, never empirical performance evidence.
3. Provenance — PARTIAL / RAW CONSTRUCTION BLOCKED.
   - SIZE: BLOCKED_MISSING_YEAR_RULE.
   - RGROWTH: BLOCKED_MISSING_DATA_RULE; canonical window 2002–2004.
   - RZSCORE: raw construction/reference-sample sub-gate open.
4. Estimand — WARNING: mixed ICD existence/discovery/reporting; not a pure latent-MW model.
5. Transportability — NOT TESTED.

## Falsification tests registered
- Missing/unknown/nonfinite input -> reject.
- Frozen-fixture schema drift or duplicate headers -> reject.
- Scaling mismatch -> provenance failure.
- SIZE missing-year rule unresolved -> block raw construction and M1 admission.
- RGROWTH missing-data/ranking eligibility unresolved -> block raw construction and M1 admission.
- RZSCORE raw-construction/reference-sample mismatch -> block raw construction and M1 admission.
- Outcome mismatch -> reject flat ensemble.
- Synthetic fixture -> compiler validation only.

## Admission rule
ACK2007 remains LEMON-SCI-ESM-001 EXECUTABLE-CANDIDATE.
M1 admission requires:
A. observed CI/test execution evidence on the candidate commit;
B. closure of every applicable raw-construction provenance gate, specifically SIZE, RGROWTH, and RZSCORE, OR an explicit preconstructed-input boundary that names each unresolved variable and prevents raw construction;
C. frozen target-dataset compatibility decision;
D. deterministic fixture execution/checksum;
E. human scientific gate.

No single-variable exception can satisfy Gate B. SIZE, RGROWTH, and RZSCORE must each be resolved or explicitly bounded. Current verdict: REVISE.
