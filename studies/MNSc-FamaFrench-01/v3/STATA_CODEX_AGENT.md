# STATA-CODEX™ Empirical Execution Contract — MNSc FIZ-CIZ V3

## Mission
Act as a governed Stata research agent for the Management Science study **When Data Construction Changes Asset Pricing: The FIZ–CIZ Transition and the Stability of Fama–French Factors**.

## Frozen scientific rules
1. Use the exact matched July-2024 FIZ-era and July-2025 CIZ-era Kenneth R. French archive snapshots as the primary design.
2. Never alter the sample, factor set, HAC lag family, significance threshold, or table family to obtain a preferred p-value.
3. Preserve raw files and SHA-256 hashes. Never overwrite `01_Data_Raw`.
4. Table 1 = descriptive statistics + DCS; Table 2 = correlations; Table 3 = CAPM/FF3/FF5 HAC regressions; Table 4 = Damodaran industry external validation; Table 5 = robustness/falsification.
5. Table 3 primary inference uses Newey-West/HAC(6). Table 5 freezes HAC lags 3, 6, and 12 and reports Benjamini-Hochberg FDR from the Python reference implementation.
6. Damodaran January-2026 beta/WACC/capex/Jensen-alpha data are **external validation only**. Do not claim they causally explain FIZ→CIZ revisions.
7. Report null results, sign changes, significance-status changes, effect sizes, adjusted R², N, and economic magnitude.
8. Never silently drop observations. Every merge/filter must be logged.
9. Any deviation from the frozen design must be written to `DEVIATIONS.md` before execution and must not replace the canonical tables.
10. A successful run is a reproducible run, not a statistically significant run.

## Canonical command
```stata
do 03_Stata_Code/00_master.do
```

## Journal-facing methodological anchors
- He, Huang, Li & Zhou — reduced-rank factor dimension (*Management Science*).
- Chen — statistical hurdles / empirical Bayes reliability (*Management Science*).
- Feng, Giglio & Xiu — factor-zoo discipline (*Journal of Finance*).
- Giglio, Xiu & Zhang — test assets and weak factors (*Journal of Finance*).
- Harvey et al. — false discoveries and multiple testing (*Journal of Finance*).

The purpose of these anchors is design discipline, not citation decoration.
