# Open-Source Accounting, Finance & Audit Stack

Curated public GitHub resources for accounting, auditing, assurance, financial reporting, finance, fraud/AML, XBRL/SEC research, Microsoft Copilot, and IBM/watsonx experimentation.

## Design rule

This folder **does not vendor or re-publish third-party source code**. It preserves upstream ownership and licences by storing a registry and clone scripts. Always review the upstream licence, security posture, data terms, and current requirements before redistribution or production use.

**Important:** public/open-source code can be free to clone while the intended runtime may require a Microsoft, Azure, IBM Cloud, watsonx, Dynamics 365, M365, GPU, or model/API account.

## Recommended stack

| Provider | Repository | Accounting / audit use | Free asset | Runtime note |
|---|---|---|---|---|
| Microsoft | microsoft/FinanceBenchmark | Finance-agent evaluation; AP/AR, financial Q&A, business briefs | ~300 benchmark questions; synthetic AP/AR data | Public repo; ERP path needs Dynamics/MCP; model calls may need credentials |
| Microsoft | microsoft/finance-advanced-analytics | Corporate-finance analytics, forecasting, ML learning | Code + learning material | Local/open-source content |
| Microsoft | microsoft/dstoolkit-corporate-financial-forecasting | Corporate financial forecasting | Code/templates | Intended for Azure/Synapse workflows |
| Microsoft | microsoft/CopilotStudioSamples | Copilot Studio agent patterns, MCP/A2A, testing | Samples + templates | Copilot Studio/Power Platform may require account/licence |
| Microsoft/PnP | pnp/copilot-pro-dev-samples | Includes Finance Statement Agent for PDF-to-Excel extraction | Community Copilot samples | Some samples require Azure/M365 resources |
| Microsoft | microsoft/qlib | AI/ML quantitative finance, research and backtesting | Code + public-data collectors | Local Python supported; data source terms still apply |
| IBM | IBM/AML-Data | AML research and labelled synthetic financial transactions | Synthetic AML CSV data | Data licence differs from repo licence; see upstream |
| IBM | IBM/AMLSim | Generate synthetic banking transactions and laundering patterns | Simulator + generated data | Local open-source workflow |
| IBM | IBM/TabFormer | Synthetic credit-card transactions + transformer research | Dataset + model code | Research-oriented |
| IBM | IBM/ai-on-z-fraud-detection | Credit-card fraud detection with LSTM/GRU/ONNX | Notebooks + models + linked data | Older dependency stack; use as benchmark/reference |
| IBM | IBM/watsonx-ai-samples | Credit-risk and broader watsonx AI examples | Notebooks + sample code | Running many examples needs watsonx/Cloud Pak credentials |
| IBM | IBM/watsonx-developer-hub | Agent and GenAI patterns for watsonx | Agent/app examples | Runtime usually needs watsonx API/project values |
| IBM | ibm-client-engineering/output-drift-financial-llms | Auditability/replayability of financial LLM agents | Financial-agent benchmark tasks + assurance harness | Strong fit for AI-to-AI assurance research |
| IBM | IBM/ai-agent-for-loan-risk | Agentic loan-risk workflow | PoC code | IBM Cloud/watsonx services required for intended deployment |
| XBRL | Arelle/Arelle | SEC/ESEF/iXBRL validation and extraction | Full XBRL processor | Local, Apache-2.0 upstream |
| SEC | jadchaar/sec-edgar-downloader | Download SEC filings for accounting/audit research | Python package | Local; must comply with SEC fair-access/user-agent rules |
| Audit | westland/auditanalytics | Audit analytics code and example data in R | Code + random_data.csv | Local R workflow |
| Audit research | GitiHubi/deepPaper | Financial audit data-analytics research collection | Paper/project index | Reference-only; follow each linked project's licence |
| Financial NLP | ProsusAI/finBERT | Financial-text sentiment/NLP | Model code + public model access | Older repo dependencies; modern HF model may be easier |
| Financial LLM | AI4Finance-Foundation/FinGPT | Open financial LLM/RAG/benchmark experimentation | Code + HF-linked models/datasets | Local/cloud; some models need GPU or separate model access |

## Best free data for your research

1. **Microsoft FinanceBenchmark synthetic AP/AR** — fictitious customers, vendors and roughly 7,000 AP/AR journal lines, plus finance-agent questions.
2. **IBM AML-Data** — synthetic labelled AML transactions.
3. **IBM AMLSim** — generates configurable synthetic banking/AML networks.
4. **IBM TabFormer** — synthetic credit-card transaction/fraud research data.
5. **SEC EDGAR** — public filings accessed through a compliant downloader.
6. **Microsoft Qlib public-data collectors** — useful for finance/market research; check source data terms.
7. **Westland Audit Analytics example data** — small audit-teaching/research examples.

## Suggested research mapping

- **Accounting / financial reporting:** SEC EDGAR + Arelle + FinBERT/FinGPT.
- **Audit analytics / fraud:** Westland + IBM AMLSim/AML-Data + IBM fraud detection.
- **AI assurance / agent evaluation:** Microsoft FinanceBenchmark + IBM output-drift-financial-llms.
- **Microsoft Copilot research:** FinanceBenchmark + CopilotStudioSamples + PnP Finance Statement Agent.
- **IBM research:** AML-Data + AMLSim + watsonx samples + output-drift assurance harness.
- **Finance / forecasting:** Microsoft finance-advanced-analytics + forecasting toolkit + Qlib.

## Clone locally or in GitHub Codespaces

Linux/macOS:

    bash open-source/accounting-finance-audit/bootstrap.sh core

Windows PowerShell:

    powershell -ExecutionPolicy Bypass -File open-source/accounting-finance-audit/bootstrap.ps1 core

Use `all` instead of `core` to clone the larger optional set.

The scripts only **clone** upstream repositories. They do not automatically execute third-party install scripts, cloud deployments, or model downloads.

## Install lightweight local tools

For the two most directly useful accounting-data utilities:

    python -m pip install -U sec-edgar-downloader arelle-release

For Microsoft Qlib:

    python -m pip install pyqlib

Review package versions and create an isolated virtual environment before research replication.

## Provider integration

**Microsoft / Copilot path**

FinanceBenchmark → Copilot/agent experiment → synthetic AP/AR + public finance questions → independent scoring → Human review.

**IBM path**

AML/financial data → watsonx or local model/agent → replayability/faithfulness tests → evidence trace → independent reviewer → Human review.

**Provider-neutral path**

SEC/XBRL + audit data → local open-source analytics → GPT/Claude/Gemini/Copilot/watsonx as replaceable reasoning layer → falsification → reproducibility → Human Gate™.

## Files

- `repos.yml` — machine-readable registry.
- `bootstrap.sh` — clone script for Linux/macOS/Codespaces.
- `bootstrap.ps1` — clone script for Windows.
- `SECURITY_AND_LICENSE.md` — safe-use and licensing rules.

Last curated: 2026-09-25.

## GitHub + Hugging Face + Kaggle Data Hub

The integrated public-data layer is here:

- [Free Data Hub](data/DATA_HUB.md)
- [Machine-readable data registry](data/data_sources.yml)
- [Cross-platform downloader](data/download_data.py)
- [Python requirements](data/requirements-data.txt)

The data hub keeps large files on their native platforms and downloads them into the Git-ignored `research-data/` directory. It currently covers synthetic audit/journal-entry and AML data, SEC/XBRL and SEC-filing corpora, financial NLP, ESG/sustainability, fraud benchmarks, and GitHub-hosted accounting/finance/audit programs.
