# ACK2007 Phase 6 — Verification & Falsification Decision

Decision: **REVISE / SCIENTIFIC-HOLD / NOT M1-LOCKED**

## Live-safe authority repairs
- Canonical raw-construction authority: `source-definition-recovery/ACK2007-construction-gates.json`.
- R-005 is enforced: FOREIGN_SALES, AUDITOR, INST_CON and LITIGATION are SECONDARY_SOURCE, not VERIFIED.
- C1/R-002: RGROWTH remains PROVENANCE_CONFLICT; neither 2001–2003 nor 2002–2004 is executable.
- C2/R-003: SIZE remains PROVENANCE_CONFLICT; neither log nor level/average is executable.
- C3/R-004: %LOSS remains BLOCKED_MISSING_YEAR_RULE.
- O3/R-007: RZSCORE remains BLOCKED_RAW_CONSTRUCTION; Altman version must not be inferred.
- Numerical coefficients/intercept live only in `executable-models/ACK2007/coefficient-contract.json` as a regression pin with PENDING_PRIMARY_TABLE / UNKNOWN_ORIGIN.

## Falsification protections
- Exact 14-predictor identity/order and unique names.
- Semantic digest pin for any coefficient/intercept change or sign flip.
- Missing/extra/renamed/duplicate predictor contract rejection.
- Intercept deletion/duplicate-key rejection.
- End-to-end raw execution stops before any constructor for unresolved or secondary-only variables.
- Scale/unit/log-vs-level/window/missing-year/denominator/ranking-direction claims cannot bypass fail-closed gates.
- Registry schema/identity/default-policy drift rejects.
- Frozen fixture remains unmodified and runs twice into independent clean output directories.
- Fixture checksum mutation rejects.
- Constructor/predict exceptions propagate; no silent swallowing.

## Historical evidence
GitHub Actions run #34 failure remains historical falsification evidence and must not be deleted or reinterpreted as a pass.

## Admission rule
Green CI is engineering evidence only. ACK2007 scientific admission still requires published-primary evidence plus repository/adversarial pass and human approval.

No PDF-independent repair in this phase upgrades scientific status.
