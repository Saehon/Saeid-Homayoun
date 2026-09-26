# Free Data Hub — GitHub + Hugging Face + Kaggle

This hub connects free/public accounting, auditing, finance, fraud/AML, SEC/XBRL and ESG data to the main open-source research stack.

**Principle:** GitHub stores manifests, code, provenance and small samples. Large datasets remain on their native platform and are downloaded on demand.

## Priority datasets

| Platform | Dataset | Research use | Licence / access |
|---|---|---|---|
| Hugging Face | `VynFi/vynfi-audit-p2p` | Synthetic accounting journal entries, audit, SOX, anomalies and fraud | Apache-2.0 |
| Hugging Face | `VynFi/aml-100k` | Synthetic AML transactions and labels | Apache-2.0 |
| Hugging Face | `DenyTranDFW/edgar_xbrl_companyfacts` | SEC/XBRL company facts; US-GAAP/IFRS tags | GPL metadata on Hub; verify source terms |
| Hugging Face | `sfd-anonymous/sfd-v1` | Large SEC filing corpus for long-context financial research | CC-BY-NC-4.0; ~45 GB public snapshot |
| Hugging Face | `lmassaron/FinancialPhraseBank` | Financial sentiment/NLP benchmark | CC-BY-NC-SA-4.0 |
| Hugging Face | `DataNeed/company-reports` | ESG/sustainability/company-report text | CC-BY-SA-4.0; ~2 GB |
| Kaggle | `mlg-ulb/creditcardfraud` | Classic imbalanced fraud benchmark | Open Database / Database Contents |
| Kaggle | `nclunaventures/2024-financial-year-8-core-sec-datasets-for-ml` | 2024 SEC filing index and discovery metadata | CC0 |
| Kaggle | `tunguz/environment-social-and-governance-data` | World Bank ESG indicators | CC BY 4.0 |
| GitHub | `microsoft/FinanceBenchmark` | Finance-agent evaluation + synthetic AP/AR | Public repository; inspect upstream licence |
| GitHub | `IBM/AML-Data` | Synthetic AML transaction data | Public repository; dataset licence differs from code |
| GitHub | `IBM/AMLSim` | Generate synthetic banking/AML data | Public open-source project |
| GitHub | `westland/auditanalytics` | Audit analytics examples + sample data | Public research/teaching repository |

## Priority free programs

- `Arelle/Arelle` — XBRL/iXBRL processing and validation.
- `jadchaar/sec-edgar-downloader` — SEC filing retrieval.
- `microsoft/FinanceBenchmark` — finance-agent benchmark and AP/AR synthetic data.
- `microsoft/CopilotStudioSamples` — Microsoft Copilot agent examples.
- `microsoft/qlib` — quantitative finance ML platform.
- `IBM/AMLSim` — synthetic AML/banking transaction simulator.
- `IBM/watsonx-ai-samples` — watsonx notebooks and credit-risk examples.
- `ibm-client-engineering/output-drift-financial-llms` — financial-agent replayability/auditability harness.
- `ProsusAI/finBERT` — financial NLP.
- `AI4Finance-Foundation/FinGPT` — financial LLM/RAG experiments.

## One-time local setup

Linux/macOS/Codespaces:

    bash open-source/accounting-finance-audit/setup_local.sh

Windows PowerShell:

    powershell -ExecutionPolicy Bypass -File open-source/accounting-finance-audit/setup_local.ps1

This creates a Python virtual environment, installs the downloader libraries, and clones the core GitHub program stack into `external-open-source/`.

## Download data

List registered sources:

    .venv/bin/python open-source/accounting-finance-audit/data/download_data.py --list

On Windows:

    .venv\Scripts\python.exe open-source\accounting-finance-audit\data\download_data.py --list

Download a **small research sample** from a Hugging Face dataset:

    .venv/bin/python open-source/accounting-finance-audit/data/download_data.py --source hf-financialphrasebank --rows 100

Download a larger audit sample:

    .venv/bin/python open-source/accounting-finance-audit/data/download_data.py --source hf-vynfi-audit-p2p --rows 1000

Download a public Kaggle dataset:

    .venv/bin/python open-source/accounting-finance-audit/data/download_data.py --source kaggle-credit-card-fraud

Kaggle may request authentication depending on the current Kaggle API policy/account state. Keep any Kaggle token in environment variables or GitHub secrets; never commit it.

## Research-safe storage

Downloaded content goes under:

    research-data/

That directory is ignored by Git. This avoids accidentally committing multi-GB datasets, proprietary credentials, or data whose licence requires separate attribution.

## Publication / replication rule

For each empirical paper, freeze:

1. source URL / platform identifier;
2. retrieval date;
3. upstream commit or dataset revision where available;
4. licence;
5. checksum of the downloaded snapshot;
6. sample construction code;
7. model/version/prompts;
8. random seed;
9. reviewer/falsification result;
10. human approval.

See `data_sources.yml` for the machine-readable registry.
