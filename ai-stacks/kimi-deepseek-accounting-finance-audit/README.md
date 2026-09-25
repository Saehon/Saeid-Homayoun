# Kimi + DeepSeek Open Stack for Accounting, Finance & Auditing

Purpose: a reproducible, license-aware registry and starter environment for using open Kimi and DeepSeek models with accounting, auditing, assurance, financial reporting, SEC/XBRL, fraud, and finance research.

This folder deliberately does **not** copy hundreds of gigabytes of model weights or duplicate third-party repositories. It keeps the canonical upstream links, licenses, install instructions, and optional download scripts. This preserves provenance and keeps the main research repository lightweight.

## What is installed here

- README.md — architecture, recommended components, and links.
- catalog.csv — machine-readable catalog of models, code, and datasets.
- requirements.txt — free Python packages for Hugging Face, Kaggle, RAG, and financial-data workflows.
- download_assets.py — optional downloader for selected open datasets and smaller model checkpoints.
- setup.ps1 — Windows setup.
- setup.sh — Linux/macOS setup.

## Cross-platform control links

- GitHub canonical source: https://github.com/Saehon/Saeid-Homayoun/tree/main/ai-stacks/kimi-deepseek-accounting-finance-audit
- Hugging Face mirror: https://huggingface.co/datasets/SADHON/kimi-deepseek-accounting-finance-audit
- Kaggle mirror: https://www.kaggle.com/datasets/sadhon/kimi-deepseek-accounting-finance-audit
- Google Drive control folder: https://drive.google.com/drive/folders/1oEZR1FI4fsJzkN4O5aHEWMZi4fXacqNW
- Google Drive master integration record: https://docs.google.com/document/d/1Ts1DpE608E5DpOTX5ihfculpkNNUwGwl1v2p3rnkNK8/edit

**Control logic:** GitHub is the executable source of truth; Hugging Face and Kaggle are synchronized public mirrors; Google Drive is the controlled research/documentation record.

## Recommended research stack

### 1. DeepSeek reasoning layer

**Default local/research choice:** deepseek-ai/DeepSeek-R1-Distill-Qwen-7B on Hugging Face.

Why: MIT-licensed, materially smaller than the 671B/685B frontier DeepSeek releases, and suitable for controlled accounting calculations, financial QA, RAG evaluation, audit reasoning experiments, and reviewer/challenge-agent prototypes.

**Frontier references:** DeepSeek-R1, DeepSeek-V3, and DeepSeek-V3.2. These are kept as upstream references because their full weights require substantial compute and storage.

### 2. Kimi multimodal / long-document layer

**Practical research choice:** moonshotai/Kimi-VL-A3B-Instruct or moonshotai/Kimi-Linear-48B-A3B-Instruct.

Why: Kimi-VL is useful for multimodal work such as financial tables, document pages, receipts, invoices, screenshots, and evidence inspection. Kimi Linear is designed for very long context.

**Frontier references:** Kimi K2, Kimi K2.5, and Kimi K3. Full frontier checkpoints are not automatically downloaded.

### 3. Accounting and audit application layer

Recommended open repositories:

| Repository | Area | License / status | Suggested use |
|---|---|---|---|
| williamjxj/agentic-langgraph-accounting | Accounting audit, invoices, RAG, LangGraph, DeepSeek | MIT | Prototype accounting-auditor agents |
| hananedupouy/LLMs-in-Finance | Finance agents, RAG, multimodal finance | MIT | Teaching, experiments, agent architecture |
| ikarib/FinEvalKit | Audit-ready evaluation, financial RAG, XBRL, OCR, provenance | MIT | Falsification, model-risk and evaluation layer |
| Arelle/Arelle | XBRL platform | Apache-2.0 | SEC/XBRL and financial-reporting validation |
| OpenBB-finance/OpenBB | Open finance data platform | AGPL-3.0 | Finance data integration and AI-agent back end |
| kai-tran-cs/FinRAG | SEC 10-K RAG | MIT | Financial-document QA baseline |
| cv-lee/FinanceRAG | Finance-specific RAG benchmark system | Check upstream license before redistribution | Research comparison / benchmark reference |
| AI4Finance-Foundation/FinGPT | Open-source financial LLM / RAG / sentiment | MIT | Finance-domain LLM baseline and training ideas |
| AI4Finance-Foundation/FinRL | Financial reinforcement learning | MIT | Finance research benchmark / agent environments |
| ProsusAI/finBERT | Financial sentiment NLP | Apache-2.0 | Lightweight financial NLP baseline |
| czyssrs/FinQA | Original FinQA dataset + code | MIT | Canonical financial numerical-reasoning benchmark |
| dgunning/edgartools | SEC EDGAR + XBRL Python toolkit | MIT | Primary-source filings, XBRL and financial statements |
| jadchaar/sec-edgar-downloader | SEC filing downloader | MIT | Reproducible SEC filing acquisition |

## Official model sources

### Moonshot AI / Kimi

- GitHub organization: https://github.com/MoonshotAI
- Kimi K3: https://github.com/MoonshotAI/Kimi-K3
- Kimi K2.5: https://github.com/MoonshotAI/Kimi-K2.5
- Kimi K2: https://github.com/MoonshotAI/Kimi-K2
- Hugging Face Kimi K2.5: https://huggingface.co/moonshotai/Kimi-K2.5
- Hugging Face Kimi VL A3B Instruct: https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct
- Hugging Face Kimi Linear 48B A3B Instruct: https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct

### DeepSeek

- GitHub organization: https://github.com/deepseek-ai
- DeepSeek R1: https://github.com/deepseek-ai/DeepSeek-R1
- DeepSeek V3: https://github.com/deepseek-ai/DeepSeek-V3
- Hugging Face DeepSeek V3.2: https://huggingface.co/deepseek-ai/DeepSeek-V3.2
- Hugging Face DeepSeek R1 Distill Qwen 7B: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B

## Free/open datasets

### Hugging Face

| Dataset | Research use | License |
|---|---|---|
| bevaya/FinQA | Numerical reasoning over financial reports and tables | MIT |
| ibm-research/finqa | Canonical FinQA distribution | CC BY 4.0 |
| PatronusAI/financebench | Financial open-book QA benchmark | CC BY-NC 4.0 |
| takala/financial_phrasebank | Financial-news sentiment | CC BY-NC-SA 3.0 |

Links:
- https://huggingface.co/datasets/bevaya/FinQA
- https://huggingface.co/datasets/ibm-research/finqa
- https://huggingface.co/datasets/PatronusAI/financebench
- https://huggingface.co/datasets/takala/financial_phrasebank

### Kaggle

| Dataset | Research use | License |
|---|---|---|
| mlg-ulb/creditcardfraud | Rare-event fraud detection, PR-AUC, anomaly detection | Open Database License / database contents terms shown by Kaggle |
| ealaxi/paysim1 | Synthetic transaction fraud | CC BY-SA 4.0 |
| nclunaventures/2024-financial-year-8-core-sec-datasets-for-ml | SEC filing index / discovery | Verify current Kaggle data-card terms before redistribution |

Links:
- https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- https://www.kaggle.com/datasets/ealaxi/paysim1
- https://www.kaggle.com/datasets/nclunaventures/2024-financial-year-8-core-sec-datasets-for-ml

## Direct public financial-reporting infrastructure

- SEC EDGAR: https://www.sec.gov/edgar
- SEC XBRL / Company Facts can be used as primary-source evidence.
- Arelle provides an open-source XBRL validation and processing layer.
- EdgarTools provides a MIT-licensed Python interface for SEC filings, XBRL financial statements, 10-K/10-Q/8-K and related evidence.
- sec-edgar-downloader provides a small MIT-licensed downloader for reproducible SEC filing acquisition.
- FinGPT, FinBERT and FinQA provide useful finance-domain baselines that can be paired with Kimi/DeepSeek rather than treated as competing closed stacks.

For research, prefer primary SEC/XBRL evidence where possible and use Kaggle/Hugging Face copies as benchmark or convenience layers.

## Installation

### Windows PowerShell

~~~powershell
cd ai-stacks/kimi-deepseek-accounting-finance-audit
powershell -ExecutionPolicy Bypass -File .\setup.ps1
~~~

### Linux / macOS

~~~bash
cd ai-stacks/kimi-deepseek-accounting-finance-audit
bash setup.sh
~~~

### Download only the lightweight datasets

~~~bash
python download_assets.py --datasets
~~~

### Add the two practical model checkpoints

This can require many gigabytes of storage and suitable hardware.

~~~bash
python download_assets.py --datasets --deepseek-7b --kimi-vl
~~~

### Add Kaggle datasets

Public Kaggle downloads may require Kaggle authentication in your environment.

~~~bash
python download_assets.py --kaggle
~~~

## Suggested accounting/audit architecture

Financial evidence / SEC / XBRL / invoices / policies
→ deterministic preprocessing and accounting rules
→ retrieval and provenance
→ DeepSeek reasoning agent
→ Kimi multimodal / long-context review
→ independent evaluator / falsification layer
→ human approval

For high-stakes audit or financial-reporting work, do not treat an LLM output as audit evidence by itself. Preserve source documents, calculation traces, model/version information, and human review.

## License discipline

Every upstream asset retains its own license. Do not relicense third-party code or data under this repository's license. Before publishing derivative datasets or commercial applications, re-check the upstream license and data-card terms. Non-commercial licenses such as CC BY-NC and CC BY-NC-SA are appropriate for research/education but may restrict commercial use.

## Research priority

For accounting and auditing research, start with:

1. FinQA for numerical financial reasoning.
2. FinanceBench for evidence-grounded financial QA.
3. SEC/XBRL + Arelle for primary-source financial reporting.
4. DeepSeek R1 Distill 7B as a manageable reasoning baseline.
5. Kimi-VL A3B for visual-document and table review.
6. FinEvalKit for independent evaluation, provenance, and falsification.
7. Agentic LangGraph Accounting for invoice/accounting workflow prototypes.
