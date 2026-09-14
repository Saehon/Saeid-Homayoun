# FF–Damodaran Discovery 01

## ECONOVA-S™ verified public-data benchmark

This study is the first executable benchmark for the ECONOVA-S™ Research Co-Scientist.

### Research question

**Does combining Fama–French market information with Damodaran industry fundamentals produce incremental out-of-sample information about future industry returns relative to Fama–French information alone?**

The design deliberately separates scientific discovery from significance hunting. A candidate finding is not a discovery unless it survives literature validation, construct validation, mapping review, temporal/out-of-sample testing, falsification, replication, adversarial AI-to-AI review, Chain-of-Evidence, DAG governance, and Human Gate approval.

## Authoritative data

Primary market data come from the Kenneth R. French Data Library. Primary fundamental/valuation data come from Aswath Damodaran / NYU Stern. GitHub mirrors are not treated as authoritative sources.

Core inputs:

- Fama/French 5 Factors (monthly)
- Momentum factor (monthly)
- 49 Industry Portfolios (monthly)
- rolling 60-month FF5+Momentum exposures estimated separately for each FF49 industry
- Damodaran US industry Betas
- Damodaran US industry Cost of Capital / WACC
- Damodaran US industry EVA / ROC / ROE
- annual archived Damodaran vintages, with year-specific industry classification

Damodaran notes that industry categories can vary over time because underlying raw data sources changed. Therefore this study uses a **year-specific FF49 ↔ Damodaran crosswalk** with explicit confidence, weights, and manual-review fields.

## Reproducible pipeline

```text
Official provider URLs
  -> immutable raw downloads
  -> SHA-256 manifest / Data Passport
  -> FF49 monthly-to-year construction
  -> rolling industry-specific FF5+Momentum exposures
  -> Damodaran vintage panel
  -> year-specific industry mapping suggestions
  -> human-reviewed many-to-many crosswalk
  -> merged industry-year panel
  -> publication-style Tables 1-5
  -> Co-Scientist hypothesis tournament
  -> ERA empirical objects
  -> ResearchEvolve / Computational Discovery
  -> AI-to-AI adversarial review
  -> falsification + replication
  -> Science One-inspired Chain-of-Evidence
  -> Human Gate
```

## Easiest execution: GitHub Actions

No local Python setup is required for the first preparation stage.

1. Open the repository **Actions** tab.
2. Select **FF-Damodaran Prepare Crosswalk**.
3. Choose **Run workflow**.
4. When it finishes, download the artifact `ff-damodaran-crosswalk-review`.
5. Review `candidate_crosswalk.csv`. Copy only defensible mappings into `crosswalk/reviewed_crosswalk.csv`, set `approved=true`, assign weights, and ensure weights sum to 1 within each year × FF49 industry.
6. Commit the reviewed crosswalk.
7. In Actions, run **FF-Damodaran Full Baseline**.
8. Download `ff-damodaran-baseline-results`, which contains Tables 1–5 and the evidence/Data Passport files.

The workflow intentionally stops if no human-approved crosswalk exists.

## Local run order

```bash
pip install -r requirements-study.txt
python src/download_sources.py
python src/build_ff49_annual.py
python src/build_factor_exposures.py
python src/build_damodaran_panel.py
python src/suggest_crosswalk.py
```

At this point review `crosswalk/candidate_crosswalk.csv`. Copy only economically defensible mappings into `crosswalk/reviewed_crosswalk.csv`, set `approved=true`, and make mapping weights sum to 1 for every year × FF49 industry. Then run:

```bash
python src/merge_panel.py
python src/baseline_tables.py
python src/make_data_passport.py
python tests/test_contract.py
```

## Baseline outputs

The baseline creates:

1. `table1_variable_definitions.csv`
2. `table2_descriptive_statistics.csv`
3. `table3_correlations.csv`
4. `table4_main_regressions.csv`
5. `table5_temporal_oos_and_data_value.csv`

Table 5 directly evaluates the ECONOVA-S **Data Economic Value™** question by comparing factor-exposure-only, fundamentals-only, and combined models in expanding-window temporal prediction. P-values are reported descriptively in Table 4 but are never an optimization or evolutionary fitness target.

## Timing rule

Predictors are dated year `t`. The strict forecasting outcome is FF49 industry return in `t+1`. Rolling factor exposures use up to 60 monthly observations ending in year `t` and require at least 36 observations.

## Data handling

Raw provider files are intentionally excluded from version control. The downloader records provider URL, retrieval timestamp, local path, size, and SHA-256. Processed files can be regenerated from raw files and the reviewed crosswalk.

## Scientific status

```text
status = IMPLEMENTATION
verified_candidate_discovery = false
human_gate_approved = false
```

This repository must retain null results, failed specifications, and classification-artifact findings. No agent is permitted to force a positive result.
