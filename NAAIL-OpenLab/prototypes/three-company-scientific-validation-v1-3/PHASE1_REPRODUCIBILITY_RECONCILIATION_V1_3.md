# NAAIL Prototype V1.3 — Phase 1 Reproducibility Reconciliation

**Date:** 2026-09-17  
**Run family:** `NAAIL-3C-V1.3-2026-09-17`  
**Scope:** V1.2 → V1.3 clean-replay factor discrepancy  
**Reconciliation outcome:** `SUPPORTED_AFTER_CHALLENGE`  
**Maturity:** `RESEARCH_PROTOTYPE`

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Executive finding

The frozen V1.2 factor package is technically reproducible. Re-executing the exact V1.2 contract on the mirrored Google Drive inputs reproduces the 18 primary 31-month CAPM/FF3/FF5 specifications across MSFT, WMT and JPM on both return bases, with only machine/export-rounding differences (maximum absolute difference across compared coefficient, fit, standard-error and p-value fields: **4.84×10⁻⁸**).

The apparent V1.2 → V1.3 mismatch is isolated to the **reference distribution used to convert the same HC3 coefficient/standard-error pairs into p-values**. The frozen V1.2 runner reports HC3 robust-covariance p-values using the asymptotic normal reference distribution. The V1.3 diagnostics numerically match Student-t p-values using residual degrees of freedom. Across all 36 alpha/market-beta p-value comparisons, the maximum absolute V1.3 difference from the corresponding Student-t calculation is **1.75×10⁻¹⁰**, while the maximum difference from the normal-reference p-value is **0.01230**.

This is therefore a reconciled inference-setting difference, not evidence that the factor data, return construction, sample window, regression coefficients or HC3 standard errors changed.

## Frozen replay contract verified

- Companies: Microsoft (`MSFT`), Walmart (`WMT`), JPMorgan Chase (`JPM`).
- Primary window: 2024-01 through 2026-07, 31 monthly observations per company.
- Models: CAPM, FF3 and FF5.
- Return bases: `price` and `dividend_inclusive_approx`.
- V1.2 inference implementation: OLS with `cov_type="HC3"`.
- Market-return construction and WMT split treatment remain unchanged.
- Factor snapshot and company-return inputs are the frozen V1.2 artifacts.

GitHub blob anchors verified before reconciliation:
- V1.2 runner: `1c3d6c0850772c82fd13452d7759dd0bda4ca26b`
- market-return input: `08e7b1d127d925000d54c3cc88ca54d75c5e7e0a`
- FF5 factor snapshot: `ee7c217e266308bb00f206846bcf95bd1db17dd6`
- frozen V1.2 result table: `13f7a0060a0c3f51e2df372671232387d87312fa`
- V1.2 replay output: `93664ee69908ac327bebeb235ca5bb6ce3cfadb5`

## Diagnostic signature

| Company | FF5 price term | Coefficient | HC3 SE | V1.2 normal-reference p | V1.3 / Student-t p | Residual df |
|---|---|---:|---:|---:|---:|---:|
| MSFT | Alpha | -0.003962 | 0.015285 | 0.795483 | 0.797606 | 25 |
| MSFT | Mkt-RF | 1.348806 | 0.341513 | 0.000078 | 0.000564 | 25 |
| WMT | Mkt-RF | 0.717136 | 0.411919 | 0.081690 | 0.093986 | 25 |
| JPM | Mkt-RF | 1.058300 | 0.271080 | 0.000095 | 0.000634 | 25 |

The V1.3 Student-t values are retained as a **small-sample inference sensitivity**. They do not overwrite the frozen V1.2 normal-reference p-values.

## Governance decision

1. Change the clean-replay discrepancy outcome from `REQUEST_MORE_EVIDENCE` to **`SUPPORTED_AFTER_CHALLENGE`**.
2. Preserve both inferential variants and label them explicitly:
   - `HC3_NORMAL_REFERENCE` — frozen V1.2 contract;
   - `HC3_T_REFERENCE_DF_RESID` — V1.3 small-sample sensitivity.
3. Do not reinterpret numerical differences in p-values as data or coefficient replication failures.
4. Preserve sensitivity-dependent findings. In particular, WMT market-beta inference changes around conventional 10% thresholds between the two HC3 reference distributions and also differs under HAC(3); it must remain explicitly sensitivity-dependent.
5. Do not change Step 20 independent replication: `REGISTERED_NOT_EXECUTED` for MSFT, WMT and JPM.
6. Do not promote Phase 2, Phase 3 or Phase 4. Their prepared designs remain governed by their existing statuses.
7. Human Gate restrictions are unchanged. No WMT/JPM Human Gate decision is inferred from this reconciliation.

## Phase 1 boundary after reconciliation

The internal clean-replay subgate is reconciled and the factor falsification diagnostics remain `DERIVED_EXECUTED`. This closes the specific V1.2 → V1.3 technical discrepancy **within the research-prototype scope only**. It is not independent replication, not production validation, and not a Human Gate decision.

Failed, null, contradictory and sensitivity-dependent evidence remains part of the record and must not be filtered from later phases.
