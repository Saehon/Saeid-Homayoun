# AWS Free/Open Data Registry — Accounting, Auditing, Finance & ESG

This registry connects free/open AWS-hosted or AWS-delivered data to NAAIL OpenLab™ / FRANKENSTEIN™ research in accounting, auditing, assurance, finance, economics, ICFR, IFRS and ESG.

## Design principle

Do not copy a dataset merely because access is free. This repository records provenance, access conditions and research use first. Raw vendor-delivered files are mirrored only when the applicable licence or terms explicitly permit redistribution.

The machine-readable registry is free-data-registry.csv.

## Priority sources

| Domain | Dataset | Why it matters |
|---|---|---|
| Accounting / Audit / Finance | SEC EDGAR Filings SAMPLE | XBRL and filings for financial-reporting NLP, audit analytics and CAM/KAM research |
| Accounting / Audit / Finance | EDGAR 10-K filings | annual-report disclosure, audit-risk, fraud and filing research |
| Finance / Economics | World Bank GDP | macroeconomic stress and cross-country controls |
| Finance / Economics | World Bank CPI | inflation, earnings pressure and valuation controls |
| Finance / Economics | World Bank unemployment | going-concern, impairment and credit-risk context |
| ESG / Carbon Accounting | Open CEDA | Scope 3 GHG measurement and supply-chain carbon accounting |
| ESG / Carbon / Energy | Climate TRACE MBERs | emissions-rate analysis aligned to project-level carbon accounting |
| ESG / Climate | Global Carbon Budget | global carbon-emissions/sinks context |
| ESG / Climate Risk | NASA NEX | physical climate-risk scenario analysis |

## Cross-platform use

```text
AWS Open Data / AWS Data Exchange
            ↓
   Provenance + licence gate
            ↓
GitHub canonical registry
       ↙           ↘
Hugging Face      Kaggle
dataset card      dataset/notebooks
       \           /
        NAAIL / FRANKENSTEIN
              ↓
 Accounting · Audit · Finance · ESG Agents
              ↓
 Reviewer / Falsification
              ↓
 Human Gate™
```

## Public mirror targets

- GitHub: https://github.com/Saehon/Saeid-Homayoun/tree/main/aws
- Hugging Face target: https://huggingface.co/datasets/SADHON/aws-free-accounting-audit-finance-registry
- Kaggle target: https://www.kaggle.com/datasets/sadhon/aws-free-accounting-audit-finance-registry

These public mirrors contain the registry metadata, not automatically the underlying vendor datasets.

## Research applications

- SEC/XBRL → financial statement analysis, audit assertions, CAM/KAM, ICFR and fraud.
- World Bank macro data → earnings-management pressure, economic-stress controls, impairment and going-concern research.
- Open CEDA / Climate TRACE / Global Carbon Budget / NASA NEX → carbon accounting, Scope 3, climate risk, ESG disclosure and assurance.

_Last curated: 25 September 2026._
