# Microsoft FY2026 Fama–French Validation — Reproducibility Package Status

**Date:** 2026-09-16  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Golden Anchor:** Microsoft Corporation  
**Execution status:** `REGISTERED_NOT_EXECUTED` — runner and workflow published; coefficient outputs not yet verified  
**Production approval:** NO

## What is now implemented

The Microsoft V1 Finance module now contains a reproducible bounded Fama–French validation package:

- `microsoft_fama_french_fy2026_input.csv` — frozen MSFT month-end IEX closes from June 2025 through June 2026;
- `code/msft_fama_french_fy2026.py` — downloads the official Kenneth R. French U.S. monthly five-factor archive, validates coverage, computes 12 FY2026 MSFT monthly price returns, merges factors, and estimates CAPM, FF3, and FF5;
- `.github/workflows/microsoft_poc_v1_fama_french.yml` — GitHub Actions execution/publishing workflow;
- planned generated outputs: `microsoft_fama_french_fy2026_merged.csv`, `microsoft_fama_french_results.csv`, `microsoft_fama_french_provenance.json`, and `MICROSOFT_FAMA_FRENCH_FY2026.md`.

## Frozen MSFT market input

The input file contains 13 monthly IEX closes so 12 monthly FY2026 close-to-close returns can be calculated:

| Month | IEX close (USD) |
|---|---:|
| 2025-06 | 497.45 |
| 2025-07 | 533.93 |
| 2025-08 | 506.74 |
| 2025-09 | 518.12 |
| 2025-10 | 517.815 |
| 2025-11 | 491.995 |
| 2025-12 | 483.695 |
| 2026-01 | 430.05 |
| 2026-02 | 392.80 |
| 2026-03 | 370.13 |
| 2026-04 | 407.765 |
| 2026-05 | 449.44 |
| 2026-06 | 372.92 |

These are market-price observations from the connected Alpaca IEX feed. They are **price data, not dividend-adjusted total returns**.

## Factor source and model contract

Canonical factor source: Kenneth R. French Data Library, U.S. Fama/French 5 Factors (2x3), monthly.

The official Data Library currently reports monthly five-factor coverage through July 2026, so the required July 2025–June 2026 factor window exists at the source.

The runner estimates:

1. CAPM: MSFT excess price return on `Mkt-RF`;
2. FF3: `Mkt-RF + SMB + HML`;
3. FF5: `Mkt-RF + SMB + HML + RMW + CMA`.

The dependent variable is MSFT monthly close-to-close price return minus the French `RF` series. Coefficient uncertainty uses HC3 heteroskedasticity-robust standard errors.

## Deliberate inference boundary

Only 12 FY2026 monthly observations are available. A five-factor model plus intercept therefore has very low residual degrees of freedom. The FY2026 regression is a **bounded exploratory reproducibility test**, not a stable long-run risk model, causal model, valuation model, forecast, or investment recommendation.

A later robustness pass should use a longer window and a total-return MSFT series including dividends.

## Current execution evidence

The input, runner and GitHub Actions workflow are published on `main`. At the time of this status record, GitHub's workflow-run list does **not** show a completed run of the new Fama–French workflow, and the generated regression-result artifacts are not present in the repository.

Therefore no alpha, beta, factor loading, p-value or R² is claimed yet. The Fama–French gate remains `REGISTERED_NOT_EXECUTED` until the generated outputs and completed execution are verified.

## Publication commits

- `51f3f3ced00aacd78d817637159e2d1830790758` — freeze MSFT FY2026 monthly IEX closes;
- `934401e91997e1d5959b3095ebbb7b7f0087a51c` — add reproducible CAPM/FF3/FF5 runner;
- `72b4281e9268cb3b046f8681559ea5600957ecec` — add GitHub Actions execution/publishing workflow.

## Next acceptance gate

Change the factor-regression status to executed only after all of the following are verified:

- completed workflow or independently reproduced execution;
- official French factor archive successfully retrieved with provenance/hash;
- 12 matched FY2026 monthly observations;
- generated CAPM/FF3/FF5 coefficient table;
- generated provenance JSON and merged dataset;
- results interpreted with the 12-observation and price-return limitations;
- independent/alternative-source sensitivity retained as an open falsification item.

Until then, Microsoft V1 remains `RESEARCH_PROTOTYPE` and the broader scientific success gate remains open.
