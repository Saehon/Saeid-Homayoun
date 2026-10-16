---
language: en
pipeline_tag: text-classification
base_model: yiyanghkust/finbert-tone
tags:
- auditing
- accounting
- us-cam
- finbert
- darwin-auditbert
- work-in-progress
---

# DARWIN–AuditBERT — US CAM FinBERT V2 (Private Model Card Only)

**Research lead:** Dr. Saeid Homayoun, University of Gävle, Sweden.  
**Hub namespace:** `SADHON`.  
**STATUS: MODEL NOT TRAINED. NO WEIGHTS AND NO FINBERT RESULT.**

This is a dedicated **private** placeholder for the independently trained US Critical Audit Matters (CAM) topic classifier, deliberately separate from the existing UK-headquarters KAM candidate repository `SADHON/saeid-finbert-kam-v2`. The model will be initialized from the appropriately licensed/revision-controlled `yiyanghkust/finbert-tone` only when private source-use and token-remediation gates pass.

The verified reference CPU baseline is **TF-IDF + balanced LinearSVC**, not this untrained neural model: real US CAM data, 45,924 source matters, 36,771 unique cleaned title+description texts and 5,648 issuer-disjoint heldout examples. Baseline macro-F1 **0.778623**, accuracy **0.867387**, description-only macro-F1 **0.766761**, all provisional pending semantic leakage/human label validation. Do not infer FinBERT performance or general model validity from these scores.

**Training process:** [DARWIN–AuditBERT GitHub master research plan](https://github.com/Saehon/Saeid-Homayoun/blob/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2/README.md), [Colab with Gemini-in-Colab master prompt](https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2/AuditBERT_USUK_Drive_Colab.ipynb).

**Release rules:** Keep actual private CAM.csv, KAM.csv, per-matter vendor metadata and historical credential-bearing notebooks in the existing owner-controlled Drive archive. Only model artifacts with source rights and independent test evidence may be considered for *separately approved* private upload; no automatic weights transfer from Colab. The [guarded release script](https://github.com/Saehon/Saeid-Homayoun/blob/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2/publish_private_checkpoint.py) defaults to local read-only checks, refuses a nonprivate Hub destination, and requires explicit attestation.

**Scientific limitations:** Source audit year is not encoded in raw `CAM.csv`. A separate `OPINION_DATES.csv` alignment is available in the original Phase 1 Drive archive for a distinct *candidate* chronological holdout with verified reports only. Text-based title/description topic mapping is not proof of CAM effectiveness, audit quality, or ICFR weakness. Preserve previous collaborative SSRN 7272139 paper authorship and externally owned model weights.

**Platform status:** PRIVATE MODEL-CARD STAGING ONLY. Neither Hugging Face, Kaggle nor GitHub stores this project's original confidential CAM text.
