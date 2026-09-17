# Prototype V1.3 — Reproducibility Discrepancy Status

**Date:** 2026-09-17  
**Status:** `SUPPORTED_AFTER_CHALLENGE`  
**Scope:** technical clean replay of the frozen V1.2 factor package

## Finding

The original clean-replay warning is preserved in the audit trail, but the cause has now been reconciled. Re-executing the exact frozen V1.2 contract on the mirrored inputs reproduces all 18 primary 31-month CAPM/FF3/FF5 specifications across MSFT, WMT and JPM on both return bases. Coefficients, HC3 standard errors and fit statistics agree up to machine/export rounding.

The apparent V1.2 → V1.3 difference is confined to robust-covariance **p-value reference distributions**:

- frozen V1.2: HC3 covariance with asymptotic-normal reference p-values;
- V1.3 diagnostics: the same coefficient/HC3-SE pairs with Student-t reference p-values using residual degrees of freedom.

Across the 36 alpha/market-beta comparisons, V1.3 p-values match the Student-t calculation to a maximum absolute difference of 1.75×10⁻¹⁰. The exact V1.2 replay differs from the frozen Drive result table by at most 4.84×10⁻⁸ across compared numerical fields, consistent with export/rounding precision.

## Scientific interpretation

This is an inference-setting difference, not a failure to reproduce the factor inputs, return construction, sample window, regression coefficients or HC3 standard errors. Both p-value variants are retained rather than silently overwriting the frozen result.

## Governance response

- reconciliation outcome: `SUPPORTED_AFTER_CHALLENGE`;
- preserve the original `REQUEST_MORE_EVIDENCE` event as historical failed/discrepant evidence;
- label V1.2 as `HC3_NORMAL_REFERENCE` and the V1.3 small-sample sensitivity as `HC3_T_REFERENCE_DF_RESID`;
- retain HAC(3), Cook's-distance and leave-one-month-out diagnostics as separate robustness evidence;
- keep WMT market-beta inference explicitly sensitivity-dependent;
- Step 20 independent replication remains `REGISTERED_NOT_EXECUTED` for all three companies;
- no Human Gate, production, Phase 2, Phase 3 or Phase 4 promotion follows from this reconciliation.

See `PHASE1_REPRODUCIBILITY_RECONCILIATION_V1_3.md` for the full audit record.
