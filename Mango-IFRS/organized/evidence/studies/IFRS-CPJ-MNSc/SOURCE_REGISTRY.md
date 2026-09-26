# Source Registry — IFRS-CPJ / Management Science

## Verified GitHub upstreams

| Upstream | Purpose | Verified license | Integration policy |
|---|---|---|---|
| [ESMA ESEF Toolkit](https://github.com/European-Securities-Markets-Authority/esef_toolkit) | Retrieve and extract ESEF XBRL filings from European listed firms | EUPL-1.2 | Fork/reference permitted under license; preserve notices; keep as data-ingestion adapter |
| [TRR266 ESEF Website](https://github.com/trr266/esef-website) | Academic ESEF research data access and parsing | MIT | Suitable for research pipeline and reproducibility patterns |
| [Arelle](https://github.com/Arelle/Arelle) | XBRL/iXBRL parsing and validation for ESEF/SEC | Apache-2.0 | Use as external dependency; retain Apache notices |
| [Open-ESEF](https://github.com/reeyarn/openesef) | Python ESEF/XBRL processing | GPL-3.0 | Keep isolated from proprietary core; do not copy GPL code into closed-source Mirendal modules |
| [sec-edgar-downloader](https://github.com/jadchaar/sec-edgar-downloader) | Download SEC EDGAR filings, including IFRS 20-F issuers | MIT | Use as external dependency or fork; retain MIT notice |
| [TRR266 treat](https://github.com/trr266/treat) | Reproducible empirical accounting-research template | MIT | Recommended reproducibility structure for the Management Science package |

## Kaggle supplementary resources

Kaggle resources are **external data/notebook references**, not vendored code or datasets. Check the current dataset license/terms on Kaggle before downloading or redistributing.

| Kaggle resource | Role in CPJ project | IFRS relevance |
|---|---|---|
| [SEC Financial Statement Extracts](https://www.kaggle.com/securities-exchange-commission/financial-statement-extracts) | Deterministic accounting calculations and US-GAAP comparison sample | Supplementary |
| [SEC Edgar Annual Financial Filings 2021](https://www.kaggle.com/datasets/pranjalverma08/sec-edgar-annual-financial-filings-2021) | Filing-text extraction prototype | Supplementary |
| [2023–2024 SEC Data: 8 Core Filings](https://www.kaggle.com/datasets/nclunaventures/2023-2024-sec-data-8-core-filings-for-ml-and-quant/data) | Filing discovery/metadata pipeline | Supplementary |
| [SEC Filings 1994–2020](https://www.kaggle.com/finnhub/sec-filings) | Historical filing discovery/robustness | Supplementary |
| [Financial Reports Fraud Detection Data](https://www.kaggle.com/datasets/ziya07/financial-reports-fraud-detection-data) | Adversarial/fraud extension | Indirect |
| [AntiFraud Centre Dataset](https://www.kaggle.com/datasets/monamzubair/antifraud-centre-dataset/versions/1) | Fraud/anomaly stress testing | Indirect |
| [Extracting 10-K Reports via SEC EDGAR](https://www.kaggle.com/code/purvasingh/extracting-financial-10-k-reports-via-sec-edgar-db) | Notebook pattern for retrieval | Supplementary |

## Preferred data pipeline

1. ESMA ESEF Toolkit / filings.xbrl.org for European IFRS filings.
2. Arelle for XBRL validation and deterministic extraction.
3. TRR266 ESEF for academic replication and data-engineering benchmarks.
4. sec-edgar-downloader for IFRS 20-F issuers and US comparison samples.
5. Open-ESEF only in a clearly isolated GPL-compatible research environment.
6. Kaggle only for supplementary comparison, stress testing, and notebooks.

## Case schema

Recommended fields:

`case_id, source_type, source_url, industry, country, ifrs_standard, topic, case_facts, evidence_documents, management_treatment, judgment_complexity, ambiguity_score, materiality, gold_answer, gold_rationale, expert_1, expert_2, adjudicated_answer, treatment, agent_answer, material_error, evidence_completeness, unsupported_claims, calculation_accuracy, confidence, human_override, decision_time, token_cost, final_quality_score`.
