# NAAIL Prototype V1.3 — Factor-Model Falsification & Robustness

**Date:** 2026-09-17  
**Status:** `DERIVED_EXECUTED`  
**Base window:** 31 monthly observations, 2024-01 through 2026-07  
**Models:** CAPM, FF3, FF5  
**Primary robustness additions:** HC3 vs HAC(3), Cook's distance, leave-one-month-out coefficient stability.

## Inference-label reconciliation

The frozen V1.2 factor runner used HC3 robust covariance with asymptotic-normal reference p-values. The V1.3 HC3 p-values below use a Student-t reference distribution with residual degrees of freedom as a small-sample sensitivity. The coefficient estimates, HC3 standard errors and R² values reproduce the V1.2 31-month specifications; the reference-distribution choice explains the p-value difference. Both variants are preserved.

## FF5 price-return diagnostics

| Company | R² | Alpha | HC3-t alpha p | Market beta | HC3-t beta p | HAC(3) beta p | Most influential month | Max Cook D |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| MSFT | 0.674 | -0.0040 | 0.798 | 1.349 | 0.0006 | 0.0000 | 2026-07 | 1.567 |
| WMT | 0.228 | 0.0150 | 0.321 | 0.717 | 0.0940 | 0.0254 | 2026-07 | 0.517 |
| JPM | 0.414 | 0.0075 | 0.513 | 1.058 | 0.0006 | 0.0003 | 2026-06 | 0.397 |

For the same FF5 price coefficients/HC3 standard errors, the frozen V1.2 normal-reference p-values include MSFT alpha 0.7955, MSFT market beta 0.000078, WMT market beta 0.0817 and JPM market beta 0.000095. These remain the canonical V1.2 values and are not overwritten.

## Interpretation

- None of the three FF5 monthly alphas is statistically significant at 5% under either retained HC3 reference distribution.
- MSFT and JPM market betas remain strongly significant under HC3 and HAC(3).
- WMT's market-beta inference is specification-sensitive: HC3-normal p≈0.0817, HC3-t p≈0.0940, and HAC(3) p≈0.0254. NAAIL therefore treats the WMT beta inference as **sensitivity-dependent**, not as a single unqualified finding.
- The most influential FF5 observation is 2026-07 for MSFT, 2026-07 for WMT, and 2026-06 for JPM.
- Leave-one-month-out market-beta signs remain positive for all three firms. Alpha signs also remain stable, but this does not make the alphas statistically significant.

## Reproducibility status

The clean-replay discrepancy is reconciled as `SUPPORTED_AFTER_CHALLENGE`. This does not equal independent replication: Step 20 remains `REGISTERED_NOT_EXECUTED` for all three companies.

## Boundary

These are robustness diagnostics for a short IEX-based monthly sample. They are not causal estimates and do not replace a longer-window consolidated-feed/CRSP replication, Human Gate review, or independent reviewer/environment replication.
