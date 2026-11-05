# NOMOS AI V6 — Phase 1 Data Validation Report
**Date:** 5 November 2026 | **Project:** NOMOS V6 Financial Decision Intelligence
**Scope:** source retrieval, historical revision audit, eight-signal panel, Tidy specification/cost join, chronology unit tests. **No V6 investment policy was fitted.**

## Executive outcome
**Conditional / research use only.** Structural data integrity PASSED; formal historical publication-time provenance FAILED/NOT ESTABLISHED. This does not authorize prospective backtesting or investment-return claims.

## Panels and quality gates
| Item | Observed result |
|---|---|
| OpenAP revised + French FF5 | 60/60 monthly rows, 2021-01-01 to 2025-12-01 |
| Eight predeclared OpenAP signals | 8 signals; missing rates: [0.0] |
| French 5 factors + RF | all six columns; {'Mkt-RF': 0.0, 'SMB': 0.0, 'HML': 0.0, 'RMW': 0.0, 'CMA': 0.0, 'RF': 0.0} |
| Duplicate or absent monthly keys | 0 duplicates, 0 missing months |
| Lagged predictors | prior month only, first month lag obtained from 2020 history; max missing rate 0.0000 |
| Tidy specification-level returns/costs | 8 series, 48 common monthly rows, 2021–2024 |
| Structural quality gate | **PASS** |
| Publication-time vintage gate | **FAIL_NOT_ESTABLISHED** |
| Tidy construction equivalence | **NOT_ESTABLISHED** |
| Eligible for prospective asset-pricing test | **False** |

## Historical release revision risk
The March 2021 OpenAP vintage covers 1926-01-01 to 2020-12-01; the 2026 release covers 1926-01-01 to 2025-12-01.
The historical overlap has 1,140 calendar months, but coverage by factor varies. The following mean absolute revisions are in monthly percentage points, computed only when both vintage values exist:

| Signal | Vintage-paired observations | Mean abs revision (percentage points) |
|---|---:|---:|
| Accruals | 822 | 1.030 |
| AssetGrowth | 822 | 0.197 |
| BM | 714 | 2.641 |
| Mom12m | 1128 | 0.287 |
| GP | 834 | 0.121 |
| Investment | 810 | 0.189 |
| EP | 840 | 0.135 |
| STreversal | 1139 | 0.316 |

## Separate benchmark: Tidy Finance portfolios
These are **not the same portfolio construction** as the OpenAP original-paper long–short returns. Tidy estimated trading costs are therefore auxiliary measurements **and must not be mechanically subtracted from OpenAP returns**.

| Signal | Tidy specification ID | Months | Correlation with OpenAP | Mean abs return difference (pp) |
|---|---:|---:|---:|---:|
| Accruals | 3087638 | 48 | 0.090 | 2.395 |
| AssetGrowth | 3145238 | 48 | 0.501 | 3.519 |
| BM | 3185558 | 48 | 0.712 | 3.763 |
| Mom12m | 3680918 | 48 | 0.451 | 7.124 |
| GP | 3496598 | 48 | 0.441 | 4.448 |
| Investment | 3623318 | 48 | 0.714 | 2.341 |
| EP | 3438998 | 48 | 0.723 | 2.961 |
| STreversal | 4033430 | 48 | 0.271 | 6.374 |

Tidy cost columns are retained in original dataset units. No re-scaling into dollars or net investment profits has been claimed. Grid choices were selected deterministically using metadata only and were not chosen using test returns.

## Strict statistical and economic restrictions
1. OpenAP 2026.10 is a **retrospectively published release**. A lag of one month prevents a coding-level look-ahead but does **not** establish publication-time availability of all original signals or revisions. Historical versions 2022.04, 2023.08, 2024.10, 2025.10 can be checked next, but annual vintages still cannot certify every decision date.
2. The eight factor names were pre-selected, not selected by performance. Future tests need investment universe, formation lag, release dates, trading/borrow fees, delisting treatment, microcaps and appropriate dynamic exposure constraints.
3. Tidy alternative portfolio construction must be matched by weights, signs, universes and lags before a fair counterfactual comparison.
4. Kenneth French factors were used only as series joined on calendar month; vintage file is current on download, not necessarily the archived factor data known in each historical month.
5. No measured cost per GPT/Claude inference, alpha estimate, Sharpe improvement, economic effect or V6 theorem exists in Phase 1.

## Verified immutable sources
| Evidence source | Revision and source SHA-256 |
|---|---|
| OpenAP_2026 | `fc01df25d4383153cb3ae9e0dd730cc34b6d15a5207abeff09f34beda45bca58` |
| OpenAP_2021 | `8ad8f59d390ee95e100d5b79e47e3faf99feeb4918d0480f88013ccf2c5e1793` |
| French_FF5 | `17d7a575e71d6764a70ddec3f8d887756c0eebf3a60f64d6ba95d2adde3fed26` |
OpenAP 2026 revision `dd1054254c4501776432caa6d7ce5ecd9586f6a9`; OpenAP 2021 revision `2ef566a3a35fc075ceaf5f6fd01b58d39b25e1b6`;
Tidy returns/costs revision `31887641d9df6aeeeb901c985edf3fe370dc59f7`; Tidy grid revision `54da7bfaef55bdf566849be56e9f1d5826798ea`.

## Supporting literature and code
- Chen & Zimmermann (2022), *Critical Finance Review*, **Open Source Cross-Sectional Asset Pricing**, doi:10.1561/104.00000112; source https://github.com/OpenSourceAP/CrossSection
- Fama & French (2015), *Journal of Financial Economics*, **A Five-Factor Asset Pricing Model**, doi:10.1016/j.jfineco.2014.10.010.
- Gu, Kelly & Xiu (2020), *Review of Financial Studies*, **Empirical Asset Pricing via Machine Learning**, doi:10.1093/rfs/hhaa009.
- McLean & Pontiff (2016), *Journal of Finance*, **Does Academic Research Destroy Stock Return Predictability?**, doi:10.1111/jofi.12365.
- Bertsimas & Kallus (2020), *Management Science*, **From Predictive to Prescriptive Analytics**, doi:10.1287/mnsc.2018.3253.
- Frey, Scheuch, Voigt & Weiss (2026), **A Transparent Financial Risk Factor Library**, *working paper*; https://huggingface.co/datasets/tidy-finance/factor-library.

## Next research gate
Construct historical decision-month availability using official dated OpenAP releases; exclude unavailable or backfilled signals; reconcile Tidy sign/lag/weighting and actual implementation costs; only then freeze the V6 economic hypothesis and start a new held-out policy test.
