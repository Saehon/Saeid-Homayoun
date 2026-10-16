---
language: en
pipeline_tag: text-classification
base_model: yiyanghkust/finbert-tone
tags:
- auditing
- accounting
- kam
- cam
- finbert
- work-in-progress
---

# Saeid-FinBERT-KAM-V2 (Private research placeholder)

**Research lead/developer:** Dr. Saeid Homayoun, University of Gävle, Sweden  
**Hub owner:** [SADHON](https://huggingface.co/SADHON)  
**STATUS: NOT TRAINED. NO WEIGHTS. NO F1 OR PRECISION RESULTS CLAIMED.**

This is a *private staging/model-card repository* for a planned independent FinBERT topic-classification extension; it is not an inference-ready model yet. The source code is maintained in the [AuditBERT V2 research branch](https://github.com/Saehon/Saeid-Homayoun/pull/185).

## Proposed methodology
- Base checkpoint: \`yiyanghkust/finbert-tone\`, with underlying license, revision and citation verified before weights redistribution.
- Dataset: authorized private Drive CAM/KAM corpus; reconcile topic taxonomy and clean source IDs; **no raw observations uploaded here**.
- Design: company-disjoint / year-forward holdouts, stratified diagnostics, leakage audit, and out-of-sample calibration analysis.
- Benchmarks: TF–IDF / LinearSVC, unadapted FinBERT, independent new fine-tuned FinBERT; original [MaRyAm1295/finBERT-KAM](https://huggingface.co/MaRyAm1295/finBERT-KAM) only as an attributed permitted reference.
- Results: **pending a genuine, reproducible GPU training and independent validation run**.

## Research integrity
The earlier collaborative [SSRN 7272139 study](https://ssrn.com/abstract=7272139) and its reported scores are not the V2 results; retain the historical authorship. Label quality, data redistribution permission, and human-validation governance are mandatory release gates.

This repository deliberately contains **no trained weights, no proprietary data, no checkpoints and no original collaborative source notebooks** until review and authorizations have been completed.


## Verified external CPU baselines — 16 October 2026 (NOT this model)

These are **real private-data TF–IDF + LinearSVC** benchmarks calculated by the AuditBERT-USUK research extension. They are **not FinBERT training results** and the contents of this private Hugging Face model repository are **still README/model card only; no trained checkpoint or predictions are available here**.

| Real-data exploratory benchmark | US CAM | UK-headquarters KAM proxy |
|---|---:|---:|
| Original source corpus | 45,924 | 86,122 Europe-wide, of which 35,886 UK HQ candidates |
| Unique eligible texts after filtering, de-duplication and conflicting-label exclusions | 36,771 | 33,724 |
| Issuer-disjoint training / validation / test | 25,774 / 5,349 / 5,648 | 23,576 / 4,960 / 5,188 |
| Test macro-F1, title + description | **0.778623** | **0.756715** |
| Test accuracy, title + description | 0.867387 | 0.820740 |
| Test macro-F1, description only | 0.766761 | 0.717099 |

**Key qualifications:** UK is presently a headquarters-code proxy, not a verified UK-audit-report/ISA (UK) cohort. US and UK topic labels and class supports differ, so their F1 scores are not comparable as a country ranking. No original audit-report-year variable has been verified in the large source files; semantic near-duplicate contamination, original reporting regime, human label quality, data rights and model-release conditions remain open. The original vendor-format full texts and previous notebooks have **not** been uploaded here.

**Reproducible code and approved-source Colab notebook:** [AuditBERT V2 GitHub research branch](https://github.com/Saehon/Saeid-Homayoun/tree/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2) · [Google Drive canonical research registry](https://docs.google.com/document/d/1YmktPLQ-be1sIFd-Ghlpvd7r156C2boC3y9eofM8p6k/edit) · [Kaggle public synthetic demonstration](https://www.kaggle.com/datasets/sadhon/cam-kam-auditbert-public-demo).

**Neural training status:** Not started. This model repository does not contain a trained FinBERT or any externally evaluated FinBERT score.
