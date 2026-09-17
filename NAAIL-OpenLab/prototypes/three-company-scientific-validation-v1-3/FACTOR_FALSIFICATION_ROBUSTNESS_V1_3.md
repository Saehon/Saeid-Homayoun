# NAAIL Prototype V1.3 — Factor-Model Falsification & Robustness

**Date:** 2026-09-17  
**Status:** `DERIVED_EXECUTED`  
**Base window:** 31 monthly observations, 2024-01 through 2026-07  
**Models:** CAPM, FF3, FF5  
**Primary robustness additions:** HC3 vs HAC(3), Cook's distance, leave-one-month-out coefficient stability.

## FF5 price-return diagnostics

| Company | R² | Alpha | HC3 alpha p | Market beta | HC3 beta p | HAC(3) beta p | Most influential month | Max Cook D |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| MSFT | 0.674 | -0.0040 | 0.798 | 1.349 | 0.0006 | 0.0000 | 2026-07 | 1.567 |
| WMT | 0.228 | 0.0150 | 0.321 | 0.717 | 0.0940 | 0.0254 | 2026-07 | 0.517 |
| JPM | 0.414 | 0.0075 | 0.513 | 1.058 | 0.0006 | 0.0003 | 2026-06 | 0.397 |

## Interpretation
- None of the three FF5 monthly alphas is statistically significant at 5% under HC3.
- MSFT and JPM market betas remain strongly significant under both HC3 and HAC(3).
- WMT's market-beta inference is specification-sensitive: HC3 p≈0.094, while HAC(3) p≈0.025. NAAIL therefore treats the WMT beta inference as **sensitivity-dependent**, not as a single unqualified finding.
- The most influential FF5 observation is 2026-07 for MSFT, 2026-07 for WMT, and 2026-06 for JPM.
- Leave-one-month-out market-beta signs remain positive for all three firms. Alpha signs also remain stable, but this does not make the alphas statistically significant.

## Boundary
These are robustness diagnostics for a short IEX-based monthly sample. They are not causal estimates and do not replace a longer-window consolidated-feed/CRSP replication.
