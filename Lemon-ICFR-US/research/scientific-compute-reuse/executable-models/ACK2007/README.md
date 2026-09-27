# LEMON-SCI Executable Scientific Model #1 — ACK2007

Status: **EXECUTABLE-CANDIDATE; NOT M1-LOCKED**

This artifact compiles the recovered ACK2007 logit specification into deterministic Python. It performs no fitting, tuning, calibration, threshold selection, or test-set optimization.

Equation:
`z = -3.752 + Σ beta_k x_k`
`p = 1/(1+exp(-z))`

The 14 coefficients are stored explicitly in `ack2007.py`. Input validation rejects missing, unknown, nonnumeric, and nonfinite fields.

## Scientific boundary
Passing unit tests proves compiler arithmetic and interface invariants only. It does **not** establish replication, transportability, calibration, or predictive performance.

## Remaining gate
RZSCORE is accepted as a preconstructed model input (decile rank of the relevant Altman z-score). A raw-data pipeline must not claim full reproduction until its exact raw construction and ranking reference sample are provenance-locked.

Next: run tests in CI, create provenance checksum, then execute on a frozen compatible dataset only after the scientific gate approves it.
