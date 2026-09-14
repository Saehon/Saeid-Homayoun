# MNSc–FamaFrench–01

## When Data Construction Changes Asset Pricing: The FIZ–CIZ Transition and the Stability of Fama–French Factors

**ECONOVA-S™ v0.3 real-data study**

This study uses only official Kenneth R. French Data Library historical archives to test whether the CRSP **FIZ → CIZ** data-construction transition changes empirical conclusions drawn from Fama–French factors and benchmark portfolios.

The French Data Library states that Legacy Format (FIZ) files were discontinued after the December 2024 data release and that U.S. research returns use CRSP Flat File Format 2.0 (CIZ) beginning with the January 2025 release. The library provides annual July archive snapshots, including July 2024 (FIZ-era) and July 2025 (CIZ-era) files.

## Research question

> When the underlying return-construction system changes from FIZ to CIZ, how stable are factor premia, portfolio returns, asset-pricing alphas, statistical conclusions, and inferred economic structure?

## Canonical comparison

- **Old snapshot:** July 2024 archive — FIZ-era construction.
- **New snapshot:** July 2025 archive — CIZ-era construction.
- **Common sample:** intersection of dates available in both archive snapshots.
- **Factors:** Mkt-RF, SMB, HML, RMW, CMA, RF.
- **Test assets:** six value-weighted portfolios formed on Size × Book-to-Market (2×3).

## New constructs

### Data Construction Sensitivity (DCS)

For variable `j`:

`DCS_j = mean(|X_new,j - X_old,j|)`

The implementation reports DCS in basis points for monthly returns, together with mean difference, maximum absolute difference, correlation, and sign-flip rate.

### Conclusion Reversal

A result is flagged as a **Conclusion Reversal** when, for the same specification and common sample:

1. the sign changes; or
2. statistical significance at the frozen 5% threshold changes.

The threshold is descriptive and frozen ex ante; ECONOVA-S does **not** optimize models to manufacture significance.

## Models

For each Size × B/M portfolio, monthly excess return is estimated under:

- CAPM: `Rp-Rf ~ Mkt-RF`
- FF3: `Rp-Rf ~ Mkt-RF + SMB + HML`
- FF5: `Rp-Rf ~ Mkt-RF + SMB + HML + RMW + CMA`

Alpha inference uses HAC/Newey-West covariance with six lags. Factor-premium inference also uses HAC standard errors.

## Six-table output

1. **Table 1 — Variable DNA and source construction**
2. **Table 2 — Factor descriptive statistics: FIZ vs CIZ**
3. **Table 3 — Data Construction Sensitivity and correlation**
4. **Table 4 — CAPM/FF3/FF5 alpha comparison**
5. **Table 5 — Significance/sign Conclusion Reversals**
6. **Table 6 — Subperiod robustness of DCS**

The run also writes `evidence_passport.json` and `RUN_SUMMARY.md`.

## Official sources

The code uses the official Kenneth R. French historical archive URL pattern for:

- July 2024 and July 2025 `F-F_Research_Data_5_Factors_2x3_CSV.zip`;
- July 2024 and July 2025 `6_Portfolios_2x3_CSV.zip`.

The source archive bytes are SHA-256 fingerprinted inside the Evidence Passport so later replications can verify that the exact same source files were used.

## Run with live official downloads

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_study.py --old 2024 --new 2025 --output artifacts
```

## Run offline from saved official ZIP archives

For restricted university machines or long-term reproducibility, download the four official ZIP files once from the Kenneth R. French Historical Archives and then run:

```bash
python run_from_local_archives.py \
  --old-ff5 F-F_Research_Data_5_Factors_2x3_2024.zip \
  --new-ff5 F-F_Research_Data_5_Factors_2x3_2025.zip \
  --old-port6 6_Portfolios_2x3_2024.zip \
  --new-port6 6_Portfolios_2x3_2025.zip \
  --output artifacts-local
```

The offline runner calls the same analysis functions as the live runner and records local-file SHA-256 fingerprints in the Evidence Passport. It does not substitute third-party mirrors for the official archives.

## Validation workflow

The GitHub Actions workflow runs both offline unit tests and the live official-archive comparison in the isolated validation pull request. Empirical artifacts are uploaded as a workflow artifact and should be reviewed before any result is treated as canonical.

## Scientific status

This is a **real-data reproducibility and measurement-change study**. A successful run establishes that the archived public data can be compared reproducibly; it does not by itself establish a causal explanation for every observed difference.

`discovery_claim_allowed = false`

The next scientific gates are replication on FF3 and additional archived portfolio families, reduced-rank factor-dimension analysis, multiplicity/FDR analysis, temporal robustness, and independent review.
