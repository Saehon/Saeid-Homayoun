# MNSc FIZ-CIZ Management Science Study V3

This directory is the executable real-data layer for the Management Science submission-development package.

## Core question
Does a documented change in the underlying CRSP/Fama-French return-construction system alter empirical asset-pricing measurements and conclusions when the research design and historical calendar are held fixed?

## Data hierarchy
1. **Primary:** official Kenneth R. French historical archive snapshots, July 2024 (FIZ-era) and July 2025 (CIZ-era).
2. **External validation:** official Aswath Damodaran / NYU Stern January-2026 industry data.
3. **GitHub:** execution, version control, and reproducibility channel. Public mirrors may be recorded for provenance checks but never replace an available authoritative primary source.

## Five-table design
- Table 1 — Descriptive statistics and Data Construction Sensitivity (DCS)
- Table 2 — Pearson/Spearman correlation structure of revisions
- Table 3 — CAPM/FF3/FF5 alpha regressions, Newey-West/HAC(6)
- Table 4 — Damodaran industry external-validation regressions, HC3
- Table 5 — HAC-lag sensitivity, FDR, and subperiod DCS

Run with Python in CI or locally, then independently reproduce using Stata `00_master.do`.
