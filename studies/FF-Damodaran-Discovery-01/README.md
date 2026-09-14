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
- Damodaran US industry Betas
- Damodaran US industry Cost of Capital / WACC
- Damodaran US industry EVA / ROC / ROE
- Annual archived Damodaran vintages, with year-specific industry classification

Damodaran notes that industry categories can vary over time because underlying raw data sources changed. Therefore this study uses a **year-specific FF49 ↔ Damodaran crosswalk** with explicit confidence and manual-review fields.

## Reproducible pipeline

```text
Official provider URLs
  -> immutable raw downloads
  -> SHA-256 manifest / Data Passport
  -> FF49 monthly-to-year construction
  -> Damodaran vintage panel
  -> year-specific industry mapping suggestions
  -> human-reviewed crosswalk
  -> merged industry-year panel
  -> baseline econometrics
  -> Co-Scientist hypothesis tournament
  -> ERA empirical objects
  -> ResearchEvolve / Computational Discovery
  -> AI-to-AI adversarial review
  -> falsification + replication
  -> Science One-inspired Chain-of-Evidence
  -> Human Gate
```

## Run order

```bash
python src/download_sources.py
python src/build_ff49_annual.py
python src/build_damodaran_panel.py
python src/suggest_crosswalk.py
python src/merge_panel.py
python tests/test_contract.py
```

Install study dependencies with:

```bash
pip install -r requirements-study.txt
```

## Data handling

Raw provider files are intentionally excluded from version control. The downloader records provider URL, retrieval timestamp, local path, size, and SHA-256. Processed files can be regenerated from the raw files and reviewed crosswalk.

## Scientific status

```text
status = IMPLEMENTATION
verified_candidate_discovery = false
human_gate_approved = false
```

This repository must be able to retain null results and classification-artifact findings. No agent is permitted to force a positive result.
