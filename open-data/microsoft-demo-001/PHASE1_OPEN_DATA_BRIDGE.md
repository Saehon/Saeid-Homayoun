# Phase 1 Open Accounting & Finance Data Bridge

## Objective

Build a professional, reproducible, free/open research pipeline in which authoritative accounting and finance data are acquired once, validated once, and then distributed consistently through GitHub, Kaggle, and Hugging Face for notebooks, AI agents, machine learning, teaching, and research.

## Architecture

```text
Authoritative public source
        ↓
SEC EDGAR / XBRL / CompanyFacts
        ↓
Canonical data + provenance
        ↓
Deterministic validation
        ↓
GitHub = source of truth
     ↙                    ↘
Kaggle                  Hugging Face
datasets/notebooks      datasets/agents/ML
     ↘                    ↙
       Reproducible research
```

The key design rule is that Kaggle and Hugging Face are distribution and execution layers. They should not become independently maintained copies of the same dataset.

## Five-Phase Development Roadmap

| Phase | Level | Deliverable |
|---|---|---|
| 1 | Very simple | One company, one verified dataset, one analysis, GitHub-to-Kaggle/Hugging Face bridge |
| 2 | Simple automation | Scheduled/API refresh, schema checks, hashes, automatic dataset versions |
| 3 | Research library | SEC XBRL, CAM, ICFR, ESG, IFRS, governance and finance datasets with notebooks and agents |
| 4 | Agentic research platform | Agents acquire data, test hypotheses, generate tables/figures and preserve evidence lineage |
| 5 | Advanced open infrastructure | Dataset registry, models, agents, benchmarks, APIs, knowledge graphs, replication and governance |

## Phase 1 Reference Company: Microsoft Corporation

**Ticker:** MSFT  
**CIK:** 0000789019  
**Primary evidence source:** U.S. SEC EDGAR  
**Reference filing:** Microsoft FY2026 Form 10-K  
**Accession:** 0001193125-26-323660  
**Unit:** USD millions

### Canonical Accounting Data

| Fiscal year | Revenue | Gross profit | Operating income | Net income |
|---:|---:|---:|---:|---:|
| 2024 | 245,122 | 171,008 | 109,433 | 88,136 |
| 2025 | 281,724 | 193,893 | 128,528 | 101,832 |
| 2026 | 331,839 | 225,465 | 155,237 | 133,749 |

### FY2026 Reproducible Metrics

- Revenue growth: **17.79%**
- Gross margin: **67.94%**
- Operating margin: **46.78%**
- GAAP net margin: **40.31%**

The Phase-1 dataset deliberately uses GAAP statement values and keeps non-GAAP adjustments separate.

## GitHub Canonical Package

Repository: https://github.com/Saehon/Saeid-Homayoun

Canonical directory:

`open-data/microsoft-demo-001/`

Core files:

- `microsoft_financials.csv` — canonical compact dataset
- `fetch_sec.py` — SEC CompanyFacts refresh adapter
- `analysis.py` — accounting calculations
- `validate.py` — deterministic validation
- `provenance.json` — source, accession, XBRL mapping and SHA-256
- `README.md` — dataset card and usage instructions

Validation workflow:

`.github/workflows/microsoft_open_data_phase1.yml`

Current technical result: **PASS**.

## Kaggle Distribution

Kaggle account: **sadhon**

Microsoft notebook:

https://www.kaggle.com/code/sadhon/sec-edgar-microsoft-10-k-simple-example

Microsoft dataset:

https://www.kaggle.com/datasets/sadhon/microsoft-accounting-demo-sec-10k

The GitHub-to-Kaggle workflow is active and authenticated. It stages the canonical GitHub CSV and provenance immediately before publication, reducing manual-copy drift.

Workflow:

`.github/workflows/kaggle-sync.yml`

The Microsoft Kaggle notebook metadata was corrected so its title slug and kernel ID are aligned. The notebook and dataset now synchronize successfully.

## Hugging Face Distribution

Hugging Face account: **SADHON**

Target dataset:

https://huggingface.co/datasets/SADHON/microsoft-accounting-demo

Publish-ready GitHub package:

`huggingface/datasets/microsoft-accounting-demo/`

Workflow:

`.github/workflows/huggingface-microsoft-data-sync.yml`

The Hugging Face workflow is designed to validate the canonical dataset before publication and to create/update `SADHON/microsoft-accounting-demo`.

**Current authorization boundary:** the connected Hugging Face OAuth credential has read access and Jobs access but not repository write access. The GitHub workflow therefore safely skips Hub publication until a GitHub Actions secret named `HF_TOKEN` with Hugging Face write permission is configured.

## Data Provenance and XBRL Alignment

The current schema maps to the following U.S. GAAP concepts:

- Revenue → `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` with documented fallbacks
- Gross profit → `us-gaap:GrossProfit`
- Operating income → `us-gaap:OperatingIncomeLoss`
- Net income → `us-gaap:NetIncomeLoss`

The SEC refresh adapter uses the SEC CompanyFacts API and requires an identifying User-Agent.

## Reproducibility Controls

Phase 1 now includes:

- authoritative-source priority;
- explicit company identifiers;
- fiscal-year controls;
- frozen accounting control totals;
- SHA-256 dataset verification;
- reproducible Python analysis;
- machine-readable provenance;
- GitHub Actions validation;
- Kaggle synchronization;
- Hugging Face publication workflow;
- clear scientific and professional-use boundaries.

## Scientific Boundary

This pipeline demonstrates open accounting-data engineering and reproducible research infrastructure. Technical validation does not constitute an audit opinion, audit assurance, investment advice, causal validation, or professional certification.

## Next Phase

After Hugging Face write authorization is enabled, the same architecture can be scaled without redesigning the core pipeline:

**Microsoft → 10 companies → S&P 100 → large SEC universe → CAM / ICFR / ESG / governance / finance modules.**
