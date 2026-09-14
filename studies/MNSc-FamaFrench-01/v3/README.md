# MNSc–FamaFrench–01 V3 — Management Science Study

**Scientific status:** pre-discovery / real-data execution and validation  
**Evidence class:** associational measurement-stability research  
**Discovery claim:** `false`

## Core question

How sensitive are factor realizations, portfolio returns, asset-pricing alphas, statistical conclusions, and inferred factor structure when the same historical calendar is evaluated using the official July-2024 FIZ-era versus July-2025 CIZ-era Fama–French archive snapshots?

## Attribution firewall

The documented FIZ→CIZ transition is the focal institutional/data-construction change, but the two archive vintages can also differ because of ordinary revisions, corrections, reclassifications, or other archive maintenance. Therefore:

> **The primary estimand is archive / construction-regime sensitivity, not the pure causal treatment effect of CIZ.**

See [`protocol/ATTRIBUTION_FIREWALL.md`](protocol/ATTRIBUTION_FIREWALL.md).

## Data hierarchy

1. **Primary:** official Kenneth R. French historical archive snapshots, July 2024 (FIZ-era) and July 2025 (CIZ-era).
2. **Complementary benchmark:** official Aswath Damodaran / NYU Stern industry data.
3. **GitHub:** execution, version control, reproducibility, protocol governance, and auditable artifacts.

The Damodaran layer is a complementary industry benchmark. It does **not** validate or identify the FIZ→CIZ transition. The legacy output filename containing `external_validation` is retained only for package compatibility.

## Frozen discovery protocol

The v3 study now carries a study-specific ECONOVA-S scientific-discovery package:

```text
protocol/01_RESEARCH_GOAL.md
protocol/02_LITERATURE_GROUNDING.md
protocol/03_HYPOTHESIS_TOURNAMENT.json
protocol/04_CAUSAL_DAG.md
protocol/05_VARIABLE_DNA.csv
protocol/06_EMPIRICAL_MANIFEST.json
protocol/07_DISCOVERY_SEARCH.json
protocol/08_LATENT_STRUCTURE.md
protocol/09_REPLICATION_REPORT.md
protocol/10_RED_TEAM_REPORT.md
protocol/11_FALSIFICATION_REPORT.md
protocol/12_CHAIN_OF_EVIDENCE.json
protocol/13_COE_AUDIT.json
protocol/14_EVIDENCE_PASSPORT.json
protocol/15_HUMAN_GATE.md
```

`study_manifest.json` is validated against the repository-wide ECONOVA-S discovery schema before the real-data build starts.

## Co-Scientist-style hypothesis tournament

The frozen tournament prioritizes:

- H1 — measurement sensitivity across official vintages;
- H2 — sensitivity of CAPM/FF3/FF5 conclusions;
- H3 — reduced-rank factor-dimension stability (extension);
- H4 — heterogeneous sensitivity across series/subperiods;
- H5 — reliability after multiplicity control;
- H0-Attribution — the primary two-vintage comparison does not identify the pure causal effect of FIZ→CIZ.

No hypothesis is selected because it later produces a desirable p-value.

## Five-table executable design

- **Table 1** — Descriptive statistics and Data Construction Sensitivity (DCS)
- **Table 2** — Pearson/Spearman correlation structure of revisions
- **Table 3** — CAPM/FF3/FF5 alpha regressions, Newey–West/HAC(6)
- **Table 4** — Damodaran complementary industry benchmark, HC3 (**not FIZ→CIZ validation**)
- **Table 5** — HAC-lag sensitivity, FDR, and frozen subperiod DCS

A sixth publication-grade replication/benchmark table is reserved for the independent replication/placebo extension rather than being fabricated before those analyses are executed.

## Falsification path

The frozen falsification plan includes same-archive identity checks, FIZ-era and CIZ-era adjacent-vintage placebo comparisons, HAC(3/6/12), BH-FDR, subperiod stability, additional test assets, parser/scale checks, and latent-structure stress tests.

## Run

```bash
pip install -r studies/MNSc-FamaFrench-01/v3/requirements.txt
pip install jsonschema
python discovery/validate_study_manifest.py studies/MNSc-FamaFrench-01/v3/study_manifest.json
python studies/MNSc-FamaFrench-01/v3/build_v3.py --output studies/MNSc-FamaFrench-01/v3/artifact
```

Then independently reproduce the applicable outputs using Stata `stata/00_master.do` against the generated clean data.

## Promotion rule

No successful model run, low p-value, model agreement, or AI consensus is sufficient for scientific discovery. Promotion requires provenance, replication/OOS, falsification, adversarial review, Chain-of-Evidence, CoE Audit, economic interpretation, and explicit Human Gate approval.

`agent_consensus != scientific_truth`

`discovery_claim_allowed = false`
