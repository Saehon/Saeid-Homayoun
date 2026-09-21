# Pre-Analysis Protocol — MNSc–FamaFrench–01

**Frozen:** 2026-09-14  
**Project:** ECONOVA-S™ v0.3  
**Scientific classification:** real-data reproducibility / measurement-change study  
**Causal claim:** false  
**Discovery claim:** prohibited at this stage

## 1. Research question

Does the CRSP FIZ → CIZ data-construction transition alter economically or statistically meaningful conclusions drawn from canonical Fama–French factor and portfolio-return data?

## 2. Primary data

Only official Kenneth R. French Data Library historical archive files are admissible for the primary analysis:

- July 2024 Fama/French 5 Factors (2x3) archive;
- July 2025 Fama/French 5 Factors (2x3) archive;
- July 2024 six Size × Book-to-Market portfolio archive;
- July 2025 six Size × Book-to-Market portfolio archive.

Third-party GitHub, Kaggle, package or mirror copies are not primary evidence. They may be used only for independent replication after the official-source analysis.

## 3. Sample rule

The primary sample is the exact intersection of monthly dates present in all four official archive files. No date is retained unless factor and portfolio observations are present in both archive snapshots.

## 4. Variables

Factors: `Mkt-RF`, `SMB`, `HML`, `RMW`, `CMA`, `RF`.

Test assets: six value-weighted Size × Book-to-Market portfolios.

Constructs:

- `DCS_j = mean(abs(X_new,j - X_old,j))`, reported in basis points per month;
- `Conclusion_Reversal = 1` when the same frozen specification changes coefficient/mean sign or crosses the frozen 5% significance threshold across archive snapshots.

## 5. Primary estimands

1. Mean factor-premium difference between archive snapshots.
2. Mean absolute archive difference (DCS).
3. Maximum absolute archive difference.
4. Old/new series correlation.
5. Sign-flip rate.
6. CAPM alpha change.
7. FF3 alpha change.
8. FF5 alpha change.
9. Sign and significance Conclusion Reversals.

## 6. Frozen inference

- Monthly frequency.
- HAC / Newey–West covariance.
- Six lags.
- Two-sided p-values.
- 5% threshold used only as a descriptive stability boundary.
- No specification may be selected because it creates statistical significance.

## 7. Frozen asset-pricing models

- CAPM: `Rp-Rf ~ Mkt-RF`
- FF3: `Rp-Rf ~ Mkt-RF + SMB + HML`
- FF5: `Rp-Rf ~ Mkt-RF + SMB + HML + RMW + CMA`

## 8. Frozen primary tables

1. Variable DNA and source construction.
2. FIZ/CIZ descriptive statistics.
3. Data Construction Sensitivity.
4. CAPM/FF3/FF5 alpha comparison.
5. Conclusion Reversals.
6. Subperiod robustness.

## 9. Frozen subperiods

- full common sample;
- post-July-1963;
- post-1990;
- post-2000;
- post-2009.

These subperiods are robustness checks, not search dimensions.

## 10. Data integrity requirements

Every downloaded source archive must record:

- official source URL;
- archive year;
- dataset family;
- byte size;
- SHA-256 fingerprint.

The Evidence Passport must preserve these records.

## 11. Interpretation rules

Observed old/new differences are first interpreted as **data-construction/revision sensitivity**, not as a causal effect of CIZ alone. The archive comparison can combine effects from the format transition and other revisions between data cuts.

No result may be described as a scientific discovery because it is novel, large, or statistically significant.

## 12. Required falsification / robustness before paper claims

Before a paper-level conclusion is accepted, the study must add:

- replication using Fama/French 3-factor archives;
- additional archived 2×3 portfolio families;
- reduced-rank factor-dimension analysis;
- multiplicity/FDR assessment of conclusion reversals;
- independent code/data replication;
- adversarial scientific review.

## 13. Acceptance gate

A run is technically successful only if:

- unit tests pass;
- all four official archives are retrieved or locally verified;
- exact common dates are established;
- Tables 1–6 are written;
- source hashes are present;
- `evidence_passport.json` is valid;
- `discovery_claim_allowed = false` remains present.

Technical success is not scientific acceptance.

## 14. Change-control rule

Any change to the primary data, sample rule, estimands, model definitions, HAC lag length, significance threshold or primary table definitions after inspecting real results must be documented as a post-analysis amendment rather than silently replacing this protocol.
