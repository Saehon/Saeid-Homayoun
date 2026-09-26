---
license: other
tags:
- accounting
- finance
- sec
- edgar
- xbrl
- reproducibility
- financial-statements
configs:
- config_name: panel
  data_files:
  - split: train
    path: "sec_10_company_panel.csv"
  default: true
- config_name: summary
  data_files:
  - split: train
    path: "phase2_summary.csv"
---

# SEC 10-Company Accounting Panel

A reproducible annual accounting dataset sourced from the official U.S. SEC CompanyFacts API.

## Coverage

MSFT, AAPL, GOOGL, AMZN, NVDA, META, JPM, WMT, XOM and TSLA.

The current verified snapshot contains the latest three annual 10-K comparative periods used for each company and normalizes reported USD values to millions. Live CompanyFacts refresh code is maintained in the canonical GitHub repository.

## Dataset Viewer

This repository exposes two separate Hugging Face configurations so files with different schemas are not incorrectly merged:

- `panel` — company-year accounting observations from `sec_10_company_panel.csv`
- `summary` — latest-period analytical metrics from `phase2_summary.csv`

This structure follows Hugging Face's recommended multiple-configuration pattern for independent files.

## Files

- `sec_10_company_panel.csv`
- `phase2_summary.csv`
- `sec_refresh_manifest.json`
- `README.md`

## Canonical source

GitHub is the source of truth:

https://github.com/Saehon/Saeid-Homayoun/tree/main/open-data/sec-10-company-phase2

The GitHub workflow validates the dataset before every Hugging Face upload.

## Research identity

Saeid Homayoun — Accounting & Auditing Scholar integrating AI into accounting, auditing, assurance, finance and sustainability research.

- GitHub: https://github.com/Saehon/Saeid-Homayoun
- Hugging Face: https://huggingface.co/SADHON
- Kaggle: https://www.kaggle.com/sadhon
- ORCID: https://orcid.org/0000-0002-2536-0446

## Method boundary

Cross-industry standardized XBRL concepts are not perfectly uniform. Missing values are retained rather than silently imputed. The provenance manifest records the concept selected for every company-period-field combination.

This is research/educational infrastructure and not audit assurance or investment advice.
