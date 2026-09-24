# SEC 10-Company Accounting Panel — Phase 2

Phase 2 scales the Microsoft proof-of-concept into a reproducible multi-company accounting pipeline.

## Companies

MSFT, AAPL, GOOGL, AMZN, NVDA, META, JPM, WMT, XOM, TSLA.

## Architecture

```text
SEC CompanyFacts
      ↓
10-company registry
      ↓
annual 10-K fact selection
      ↓
normalized accounting panel
      ↓
validation + SHA-256 + provenance
      ↓
GitHub canonical dataset
   ↙                   ↘
Kaggle               Hugging Face
   ↘                   ↙
 deterministic free accounting agent
```

## Outputs

- `sec_10_company_panel.csv` — 10 companies × 3 annual periods.
- `phase2_summary.csv` — one latest-period summary row per company.
- `sec_refresh_manifest.json` — extraction provenance and XBRL concept selection.
- `companies.json` — explicit ticker/CIK registry.
- `fetch_sec_panel.py` — SEC CompanyFacts collector.
- `validate.py` — reproducibility and control checks.
- `analysis.py` — latest-period accounting calculations.
- `agent.py` — free deterministic accounting agent.

## Accounting fields

The normalized panel attempts to extract:

- revenue
- gross profit
- operating income
- net income
- total assets
- total liabilities
- stockholders' equity

Amounts are USD millions. Blank fields are preserved when a standardized U.S.-GAAP concept is not available or is not economically meaningful for a company. This is especially important for cross-industry comparisons such as financial institutions.

## Fact-selection logic

The collector:

1. calls the official SEC CompanyFacts endpoint for each CIK;
2. keeps Form 10-K / FY observations;
3. identifies duration facts with approximately annual periods (300–430 days);
4. selects the latest filed fact for each fiscal-year end;
5. uses explicit concept-priority lists;
6. preserves accession numbers, filing dates and selected concepts in the manifest;
7. pauses between calls to remain comfortably below the SEC fair-access ceiling.

## Validation

The validator requires:

- exactly 10 registered companies;
- exactly 3 annual periods per company;
- 30 unique company-period rows;
- non-missing net income and assets;
- high revenue coverage;
- deterministic Microsoft FY2024–FY2026 control totals inherited from Phase 1;
- SHA-256 equality between the CSV and provenance manifest.

## Free accounting agent

No paid API or LLM is needed.

```bash
python open-data/sec-10-company-phase2/agent.py profile MSFT
python open-data/sec-10-company-phase2/agent.py compare MSFT AAPL
python open-data/sec-10-company-phase2/agent.py quality
```

The agent reports only deterministic calculations from the validated canonical CSV and cites the SEC CompanyFacts source URL in its output.

## Automation

The GitHub Actions workflow `.github/workflows/sec_10_company_phase2.yml`:

- refreshes all 10 companies from SEC;
- validates the panel;
- builds the summary;
- tests the free accounting agent;
- publishes/versions the Kaggle dataset when `KAGGLE_API_TOKEN` is configured;
- publishes/versions the Hugging Face dataset when `HF_TOKEN` is configured;
- commits refreshed canonical outputs back to GitHub;
- runs weekly and supports manual execution.

## Distribution targets

- GitHub canonical source: `Saehon/Saeid-Homayoun/open-data/sec-10-company-phase2/`
- Kaggle dataset: `sadhon/sec-10-company-accounting-panel`
- Hugging Face dataset: `SADHON/sec-10-company-accounting-panel`

GitHub remains the source of truth. Kaggle and Hugging Face are distribution/execution layers.

## Scientific boundary

This package is research and educational infrastructure. Automated extraction and validation do not constitute an audit, assurance engagement, investment recommendation, valuation opinion, or certification of issuer-reported information.
