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

## Tier A — directly useful industry sources

| Organization | Resource | Category | Why it belongs | Upstream |
|---|---|---|---|---|
| Goldman Sachs | GS Quant | Finance / Markets / Risk | Open-source Python quantitative-finance toolkit | https://github.com/goldmansachs/gs-quant |
| Goldman Sachs | Open Source | Finance / Data | Official organization; also points to FINOS contributions including Legend | https://github.com/goldmansachs |
| JPMorgan Chase | Open Source | Finance / Research / Data | Official open-source organization; includes GTAR research code and finance technology projects | https://github.com/jpmorganchase |
| J.P. Morgan Payments | Embedded Finance examples | Payments / Finance | Open-source examples for payment and banking API research | https://github.com/jpmorgan-payments |
| McKinsey / QuantumBlack | Kedro | Reproducible Research / Data Engineering | Modular reproducible research/data pipelines; Apache-2.0 | https://github.com/kedro-org/kedro |
| McKinsey | Agents at Scale ARK | Agentic AI infrastructure | Provider-agnostic agentic operations; evaluate before production use | https://github.com/mckinsey/agents-at-scale-ark |
| BCG X | ARTKIT | AI Evaluation | Prompt-based GenAI testing/evaluation; Apache-2.0 | https://github.com/BCG-X-Official/artkit |
| BCG X | FACET | Explainable AI | Explainability layer useful for audit/finance ML validation | https://github.com/BCG-X-Official/facet |
| BlackRock | Open Source | Finance / Risk / Research workflows | Official financial-technology open-source organization | https://github.com/blackrock |
| Bloomberg | Open Source | Financial Technology / Data Infrastructure | Verified Bloomberg organization; finance-industry infrastructure | https://github.com/bloomberg |

## Tier A — directly useful university/research sources

| Institution | Resource | Category | Research use | Upstream |
|---|---|---|---|---|
| Stanford CRFM | HELM | AI / LLM Evaluation | Reproducible model evaluation; candidate backbone for Accounting/Audit/Finance benchmarks | https://github.com/stanford-crfm/helm |
| Yale NLP | FinanceMath | Finance / AI Evaluation | Financial reasoning dataset and executable expert solutions; useful benchmark candidate | https://github.com/yale-nlp/FinanceMath |
| Columbia University FinTech Lab | OpenSource Risk Engine | Finance / Risk | Research-oriented open-source risk analytics for financial institutions/regulators/academia | https://fintech.datascience.columbia.edu/download |
| MIT DCI | Open-source organization | Finance / Transaction Infrastructure | Digital-finance and transaction-system research reference | https://github.com/mit-dci |
| Oxford Sustainable Finance Group | Research hub | ESG / Sustainable Finance | Sustainable finance, climate/environment analytics, ML/data science and spatial finance | https://sustainablefinance.ox.ac.uk/research/ |
| Cambridge Sustainable Computing Lab | Green Algorithms ecosystem | ESG / Sustainability | Carbon/resource measurement and sustainability methodology | https://github.com/Cambridge-Sustainable-Computing-Lab |

## Watchlist — institution name alone is not enough

Harvard, Wharton/UPenn, Chicago, Berkeley, NYU, Princeton and other leading institutions remain on the discovery watchlist. Add a project only when a specific official repository/dataset/model passes the admission gate. This prevents prestige-based inclusion of unrelated or unofficial code.

## Hugging Face / Kaggle candidate layer

Do not mirror third-party code or data merely because it is public. Prefer links/metadata unless redistribution is explicitly permitted. Candidate subjects:
- SEC / EDGAR / XBRL and 10-K/10-Q
- CAM / KAM and audit reports
- ICFR / material weaknesses / controls
- fraud / enforcement / restatements
- financial sentiment / FinBERT-style models
- finance reasoning benchmarks
- ESG / sustainability disclosures
- economic and financial time series

## Cross-platform architecture

GitHub = canonical provenance/catalog/code hub  
Hugging Face = eligible models + datasets + model/dataset cards  
Kaggle = eligible datasets + notebooks + benchmark tasks

Every cross-platform item should record: upstream owner, canonical URL, license, retrieval/version date, category, intended research use, redistribution status, and citation.

## Admission gate

An external resource enters the operational stack only if:
- source/ownership is verified;
- license permits intended use;
- free/open status or access restrictions are disclosed;
- relationship to the taxonomy is concrete;
- provenance/citation is retained;
- third-party material is clearly distinguished from original Saeid Homayoun research;
- no existing research asset is overwritten.

Last curated: 2026-09-26.
