---
license: cc-by-4.0
task_categories:
- text-classification
language:
- en
tags:
- auditing
- accounting
- cam
- kam
- auditbert
- finbert
pretty_name: CAM/KAM AuditBERT Public Demo
---

# CAM/KAM AuditBERT Public Demo

## Professional cross-platform research package

This dataset card is the Hugging Face data-layer copy of a research architecture connecting **ChatGPT, GitHub, Hugging Face, Kaggle, and Google Drive**.

### Canonical source
GitHub research package:  
https://github.com/Saehon/Saeid-Homayoun/tree/main/research/cam-kam-auditbert-maryam

Open-data source:  
https://github.com/Saehon/Saeid-Homayoun/tree/main/open-data/cam-kam-auditbert-demo-001

Professional architecture document:  
https://github.com/Saehon/Saeid-Homayoun/blob/main/docs/PROFESSIONAL_AI_RESEARCH_INFRASTRUCTURE_CAM_KAM.md

Cross-platform master integration:  
https://github.com/Saehon/Saeid-Homayoun/blob/main/docs/CAM_KAM_AUDITBERT_CROSS_PLATFORM_MASTER.md

### Verified research models
**CAM/KAM topic classifier**  
https://huggingface.co/MaRyAm1295/finBERT-KAM

Base model: `yiyanghkust/finbert-tone`

**KAM response generator**  
https://huggingface.co/MaRyAm1295/Llama-3.1-8B-KAM

Base model: `meta-llama/Llama-3.1-8B-Instruct`

### Evaluation distinction
Topic-classification and response-generation metrics are separate tasks. The manuscript reports:
- classifier macro F1: 83.20%
- classifier weighted F1: 88.92%
- response-generator BERTScore F1: 83.95%

### Data included
Synthetic CAM/KAM demonstration records only.

### Data excluded
Licensed Audit Analytics observations, unpublished manuscripts, and private Google Drive source workbooks are not redistributed.

### Governance
GitHub is the canonical reproducibility layer. Hugging Face is the model/data layer. Kaggle is the discoverable data/notebook layer. Google Drive remains the private manuscript and licensed-data archive.

This package is for research, teaching, and reproducibility. It does not provide an audit opinion.
