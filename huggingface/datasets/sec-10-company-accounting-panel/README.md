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
---

# SEC 10-Company Accounting Panel

A reproducible annual accounting dataset sourced from the official U.S. SEC CompanyFacts API.

## Coverage

MSFT, AAPL, GOOGL, AMZN, NVDA, META, JPM, WMT, XOM and TSLA.

Each refresh selects the latest three annual 10-K periods available for each company and normalizes reported USD values to millions.

## Files

- `sec_10_company_panel.csv`
- `phase2_summary.csv`
- `sec_refresh_manifest.json`
- `README.md`

## Canonical source

GitHub is the source of truth:

https://github.com/Saehon/Saeid-Homayoun/tree/main/open-data/sec-10-company-phase2

The GitHub workflow validates the dataset before every Hugging Face upload.

## Method boundary

Cross-industry standardized XBRL concepts are not perfectly uniform. Missing values are retained rather than silently imputed. The provenance manifest records the concept selected for every company-period-field combination.

This is research/educational infrastructure and not audit assurance or investment advice.
