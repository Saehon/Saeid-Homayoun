# LEMON-SCI Executable Scientific Model #1 — ACK2007

Status: **ENGINEERING-EXECUTABLE / SCIENTIFIC-HOLD / NOT M1-LOCKED**

This artifact is an engineering compiler for the current ACK2007 regression pin. It performs no fitting, tuning, calibration, threshold selection, test-set optimization, or scientific coefficient verification.

## Single sources of truth
- Numerical coefficient/intercept engineering pin: `coefficient-contract.json`
- Raw-construction gate status: `../../source-definition-recovery/ACK2007-construction-gates.json`
- Scientific/provenance decisions: append-only Drive Conflict/Resolution records plus repository verification notes

The coefficient contract remains:
- `role = regression_pin_only`
- `coefficient_verification = PENDING_PRIMARY_TABLE`
- `coefficient_origin = UNKNOWN_ORIGIN`

This README intentionally does not duplicate numerical coefficients or the intercept.

## Prediction boundary
While scientific raw-construction gates remain unresolved, the public compiler prediction API fails closed unless the caller explicitly selects `PRECONSTRUCTED_SYNTHETIC_COMPILER_TEST` mode.

That mode exists only for committed synthetic compiler/schema fixtures. It is not a production/raw-data admission path and is not empirical evidence.

## Scientific boundary
Passing unit tests proves compiler arithmetic, interface invariants, fail-closed behavior and deterministic fixture execution only. It does **not** establish primary-paper replication, transportability, calibration, scientific validity, or predictive performance.

All 14 raw predictors currently remain non-VERIFIED in the construction registry. No complete raw ACK2007 prediction is scientifically admitted.

## Remaining gate
Published-primary evidence is required to resolve coefficient origin and the unresolved construction rules, including SIZE, RGROWTH, %LOSS and RZSCORE. No raw construction, M1 lock, or scientific status upgrade is allowed before those gates close with append-only evidence and human approval.
