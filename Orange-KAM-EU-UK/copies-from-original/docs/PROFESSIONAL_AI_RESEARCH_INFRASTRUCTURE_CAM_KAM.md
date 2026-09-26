# Professional AI Research Infrastructure

## ChatGPT × GitHub × Hugging Face × Kaggle × Google Drive
### CAM/KAM AuditBERT Professional Research Case

This document defines the canonical cross-platform research architecture for accounting, auditing, finance, and sustainability AI projects.

## Operating model

| Layer | Main role | Canonical content |
|---|---|---|
| ChatGPT | Research and agent orchestration | literature reasoning, coding assistance, analytical design, experiment planning, model comparison, manuscript development |
| GitHub | Canonical code and reproducibility layer | Python/R code, notebooks, documentation, GitHub Actions, provenance, validation, replication packages |
| Hugging Face | AI model and dataset layer | models, model cards, datasets, embeddings, inference assets, Spaces |
| Kaggle | Data and executable notebook layer | discoverable datasets, notebooks, teaching examples, benchmark demos |
| Google Drive | Private research and manuscript layer | manuscripts, licensed datasets, collaborator files, private source data, research registries |

**Professional principle:** create once, validate once, and publish from GitHub rather than manually maintaining independent copies.

## Canonical workflow

```text
Private evidence / source data
        ↓
Google Drive private archive
        ↓
controlled preparation
        ↓
GitHub canonical package
        ↓
automated validation
        ↓
approved public-safe release
        ├── Kaggle datasets + notebooks
        └── Hugging Face models + datasets
        ↓
ChatGPT-assisted research analysis and manuscript development
```

## Microsoft FinBERT demonstration

GitHub:
https://github.com/Saehon/Financial-Sentiment-Analysis-and-Classification-Deep-Learning-Models/tree/main/cases/microsoft_finbert_case

Hugging Face profile:
https://huggingface.co/SADHON

FinBERT model:
https://huggingface.co/ProsusAI/finbert

Planned Hugging Face dataset:
https://huggingface.co/datasets/SADHON/microsoft-finbert-sentiment-case

Planned Kaggle dataset:
https://www.kaggle.com/datasets/sadhon/microsoft-finbert-sentiment-case

The Microsoft example is a connectivity and reproducibility demonstration using synthetic text. It is not financial, accounting, audit, or investment evidence.

## CAM/KAM AuditBERT research case

**Project:** AuditBERT: Revolutionizing KAM Disclosures with LLMs

The revised manuscript identifies Saeid Homayoun, Zabihollah Rezaee, Maryam Khosravian, Salma Boumediene, and Salem L. Boumediene as authors/collaborators.

Canonical GitHub package:
https://github.com/Saehon/Saeid-Homayoun/tree/main/research/cam-kam-auditbert-maryam

Canonical public-safe open-data package:
https://github.com/Saehon/Saeid-Homayoun/tree/main/open-data/cam-kam-auditbert-demo-001

Professional Google Drive master copy:
https://docs.google.com/document/d/1XaRSI9oTUNZbxOW4ZCsgdHb1Qn4a_T223_oDhymyoM8/edit

Published Hugging Face dataset:
https://huggingface.co/datasets/SADHON/cam-kam-auditbert-public-demo

Published Kaggle dataset:
https://www.kaggle.com/datasets/sadhon/cam-kam-auditbert-public-demo

## Verified Hugging Face research models

### CAM/KAM topic classifier
https://huggingface.co/MaRyAm1295/finBERT-KAM

- Base model: `yiyanghkust/finbert-tone`
- Architecture: BERT / sequence classification
- Research role: classify CAM/KAM disclosures into accounting-topic categories

### KAM response generator
https://huggingface.co/MaRyAm1295/Llama-3.1-8B-KAM

- Base model: `meta-llama/Llama-3.1-8B-Instruct`
- Architecture: LLaMA / causal language model
- Research role: generate context-aware responses to audit matters

These repositories are owned by the Hugging Face account `MaRyAm1295`. This repository links to them as research dependencies and does not claim ownership of model weights.

## Evaluation metrics: keep tasks separate

| Component | Metric | Reported value |
|---|---|---:|
| Topic classifier | Macro precision | 85.15% |
| Topic classifier | Macro recall | 82.08% |
| Topic classifier | Macro F1 | 83.20% |
| Topic classifier | Weighted precision | 88.98% |
| Topic classifier | Weighted recall | 89.03% |
| Topic classifier | Weighted F1 | 88.92% |
| Response generator | BERTScore precision | 84.19% |
| Response generator | BERTScore recall | 83.75% |
| Response generator | BERTScore F1 | 83.95% |

The 83.95% value is a response-generation **BERTScore F1**, not the topic-classification F1.

## Data governance

Private Google Drive assets include the U.S. CAM and UK KAM source workbooks and the revised AuditBERT manuscript.

Public GitHub, Kaggle, and Hugging Face demonstration assets should contain:
- synthetic data,
- SEC/EDGAR-derived material where redistribution is permitted,
- schemas,
- provenance,
- validation code,
- model cards,
- replication scripts.

Do **not** publicly redistribute Audit Analytics-derived observations unless the applicable license explicitly permits it.

For public U.S. replication, preserve issuer, accession number, filing form, filing date, section, extraction method, and source URL.

## Manuscript QA controls

Before final submission, reconcile:
- 48 accounting topics in the abstract versus 49 in the methodology;
- 65,535 raw entries versus 65,192 cleaned observations;
- the response-generation sample of 60,270 fine-tuning observations plus 1,231 out-of-sample observations;
- classifier F1 measures versus response-generation BERTScore measures;
- consistent naming of AuditBERT classifier, generator, and integrated framework.

See:
`research/cam-kam-auditbert-maryam/MANUSCRIPT_QA.md`

## Validation and synchronization

The CAM/KAM GitHub reproducibility workflow has passed:

https://github.com/Saehon/Saeid-Homayoun/actions/runs/35989916956

Kaggle synchronization is authenticated through GitHub Actions and uses `KAGGLE_API_TOKEN`.

Hugging Face publication is authenticated through GitHub Actions with `HF_TOKEN`. The professional CAM/KAM dataset was successfully published as a private dataset under the `SADHON` account.

Successful Hugging Face publication run:
https://github.com/Saehon/Saeid-Homayoun/actions/runs/35993093786

## Recommended professional structure

### GitHub
- Accounting AI
- Audit / CAM-KAM
- ICFR and Internal Controls
- ESG and Sustainability
- Reproducibility and Open Data

### Hugging Face
- Models: AuditBERT, FinBERT adaptations, accounting classifiers, audit generators
- Datasets: redistribution-safe CAM/KAM, synthetic audit data, SEC-derived public data, approved ESG data
- Spaces: interactive accounting and auditing demonstrations

### Kaggle
- Public-safe datasets
- Executable notebooks
- Teaching demonstrations
- Benchmark datasets with provenance

### Google Drive
- Private source data
- Collaborator manuscripts
- Licensed commercial data
- Working papers
- Research governance and QA records

## Current verified status

- GitHub connection: active.
- Google Drive connection: active.
- Hugging Face ChatGPT connection: active as `SADHON`.
- Hugging Face CAM/KAM dataset: **published and verified, private**.
- Kaggle CAM/KAM dataset: **published through GitHub Actions, private**.
- CAM/KAM GitHub reproducibility validation: passed.
- Verified research models: `MaRyAm1295/finBERT-KAM` and `MaRyAm1295/Llama-3.1-8B-KAM`.
- Private CAM/KAM research data: retained in Google Drive.
- Public release boundary: synthetic or redistribution-safe data only unless licensing explicitly permits broader publication.

This architecture is the professional template for future accounting, auditing, CAM/KAM, ICFR, ESG, and financial-AI projects.
