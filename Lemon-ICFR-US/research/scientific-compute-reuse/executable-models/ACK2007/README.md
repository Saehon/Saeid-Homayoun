# LEMON-SCI Executable Scientific Model #1 — ACK2007

Status: **ENGINEERING-EXECUTABLE / SCIENTIFIC-HOLD / NOT M1-LOCKED**

This artifact preserves and tests the current ACK2007 regression pin. It performs no fitting, tuning, calibration, threshold selection, test-set optimization, or scientific coefficient verification.

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
While ACK2007 remains on scientific hold, the public `predict()` and `linear_predictor()` APIs are disabled for all callers. There is no caller-selectable synthetic mode.

Frozen synthetic regression-pin arithmetic is isolated in:
`verification/ACK2007/run_fixtures.py`

That runner:
- consumes only the committed frozen fixture schema;
- validates the complete preconstructed input vector;
- uses the immutable coefficient mapping loaded from the coefficient contract;
- writes deterministic input/output checksums;
- is an engineering/compiler test only.

A raw-data caller cannot obtain a prediction by passing a mode string. Raw construction remains governed by the canonical construction-gate registry and fail-closed admission validator.

## Runtime immutability
The runtime `COEFFICIENTS` mapping is immutable. Mutating the exported runtime vector cannot bypass contract validation or the semantic-digest regression pin.

## Scientific boundary
Passing unit tests proves contract/schema invariants, fail-closed behavior and deterministic frozen-fixture execution only. It does **not** establish primary-paper replication, transportability, calibration, scientific validity, or predictive performance.

All 14 raw predictors currently remain non-VERIFIED in the construction registry. No complete raw ACK2007 prediction is scientifically admitted.

## Remaining gate
Published-primary evidence is required to resolve coefficient origin and unresolved construction rules, including SIZE, RGROWTH, %LOSS and RZSCORE. No raw construction, M1 lock, or scientific status upgrade is allowed before those gates close with append-only evidence and human approval.
