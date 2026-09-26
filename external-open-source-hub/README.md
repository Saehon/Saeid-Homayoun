# Curated External Open-Source Research & Industry Hub

Purpose: a provenance-first catalog of external resources relevant to accounting, auditing, assurance, ICFR, CAM/KAM, finance, risk, ESG/sustainability, and AI evaluation.

> Reference layer only. External projects are not represented as authored or endorsed by this repository. Verify each upstream license and data-access condition before reuse.

## Taxonomy

1. Accounting & Financial Reporting
2. Audit & Assurance
3. ICFR / Internal Control / Fraud & Forensics
4. CAM / KAM / Audit-Matter Analytics
5. Finance / Markets / Risk
6. ESG / Sustainability
7. AI / NLP / LLM Evaluation
8. Data Engineering / Reproducible Research

## Industry sources

| Organization | Resource | Primary category | Access note | Upstream |
|---|---|---|---|---|
| Goldman Sachs | GS Quant | Finance / Markets / Risk | Open-source Python toolkit; some Goldman APIs require institutional credentials | https://github.com/goldmansachs/gs-quant |
| Goldman Sachs | Open-source organization | Finance / Data Infrastructure | Includes GS Quant and projects contributed to open-source foundations | https://github.com/goldmansachs |
| McKinsey / QuantumBlack | Kedro ecosystem | Data Engineering / Reproducible Research | Use as research/data pipeline infrastructure; not an auditing product | https://github.com/kedro-org/kedro |
| BlackRock | Public GitHub organization | Finance / Risk / Data | Review individual repository licenses before reuse | https://github.com/blackrock |
| Bloomberg | Public GitHub organization | Financial technology / Data | Review individual repository relevance and license before reuse | https://github.com/bloomberg |

## University / research sources

| Institution | Resource | Primary category | Research use in this repository | Upstream |
|---|---|---|---|---|
| Stanford CRFM | HELM | AI / LLM Evaluation | Reproducible evaluation framework for future accounting/audit/finance benchmarks | https://github.com/stanford-crfm/helm |
| MIT DCI | Open-source organization | Finance / Transaction Infrastructure | Reference for digital-finance and transaction-system research | https://github.com/mit-dci |
| University of Cambridge Sustainable Computing Lab | Green Algorithms ecosystem | ESG / Sustainability | Carbon/resource measurement and sustainability methodology | https://github.com/Cambridge-Sustainable-Computing-Lab |

## Model and dataset layer

Hugging Face and Kaggle resources should be added only after checking provenance, license, dataset documentation, and relevance. Preferred subjects:
- SEC / EDGAR / XBRL
- 10-K / 10-Q / annual reports
- CAM / KAM / audit reports
- ICFR / material weaknesses / controls
- financial sentiment and FinBERT-style models
- ESG / sustainability disclosures
- fraud / enforcement / restatement data
- finance and economic time series

## Integration policy

GitHub is the canonical catalog and provenance hub. Hugging Face is intended for eligible models/datasets and model cards; Kaggle is intended for eligible datasets/notebooks/benchmarks. Cross-platform copies must retain upstream attribution, license information, source URL, version/date, and a clear statement distinguishing external material from Saeid Homayoun's original research.

## Admission gate

An external resource enters the operational stack only if:
- source/ownership can be verified;
- license permits the intended use;
- it is free/open for the intended educational or research workflow, or any access restriction is clearly disclosed;
- it has a concrete relationship to the taxonomy above;
- provenance and citation are retained;
- it does not overwrite existing research assets.

Last curated: 2026-09-26.
