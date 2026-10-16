---
language: en
pipeline_tag: text-generation
base_model: meta-llama/Llama-3.1-8B-Instruct
tags:
- auditing
- accounting
- kam
- cam
- llama
- peft
- work-in-progress
---

# Saeid-Llama-3.1-8B-KAM-V2 (Private research placeholder)

**Research lead/developer:** Dr. Saeid Homayoun, University of Gävle, Sweden  
**Hub owner:** [SADHON](https://huggingface.co/SADHON)  
**STATUS: NOT TRAINED. NO WEIGHTS, ADAPTERS, OR GENERATION METRICS HAVE BEEN PRODUCED.**

Private model-card staging area for an **independent** Llama 3.1 8B-Instruct QLoRA audit-response generation research adapter. This is **not a repackaging** of [MaRyAm1295/Llama-3.1-8B-KAM](https://huggingface.co/MaRyAm1295/Llama-3.1-8B-KAM), which remains separately owned. Code: [GitHub AuditBERT V2 PR #185](https://github.com/Saehon/Saeid-Homayoun/pull/185).

## Release gates
- Obtain authorized research-use rights for the response text pairs in private Google Drive; confirm Meta Llama license and access rules for the base model.
- Prevent train/validation/test company overlap and temporal leakage; block training if validation corpus is unsuitable.
- Fine-tune an independently initialized LoRA adapter on appropriate hosted GPU hardware (not in this staging step).
- Evaluate heldout examples for textual support, fabricated audit procedures, factual faithfulness, human auditor review and *separate* generation metrics such as BERTScore.
- Document checkpoint provenance and hardware, data source rights, label taxonomy, and a strict non-audit-opinion disclaimer before publishing any weights.

Prior collaborative paper: [SSRN 7272139](https://ssrn.com/abstract=7272139). No earlier paper metrics may be represented as independent V2 performance.

This repository is a **private placeholder card**, not a downloadable trained AI model.


## Cross-platform research update — 16 October 2026

The linked independent AuditBERT-USUK project has executed **TF–IDF + LinearSVC topic-classification baselines on real private US CAM and UK-headquartered KAM candidate texts**, obtaining held-out macro-F1 values of **0.778623** and **0.756715** respectively. These scores **do not evaluate this Llama response generator** and **must not be used as generation or neural-model performance claims**. Description-only topic baselines are 0.766761 and 0.717099.

Detailed aggregate evaluation and source hashes: [canonical private Google Drive registry](https://docs.google.com/document/d/1YmktPLQ-be1sIFd-Ghlpvd7r156C2boC3y9eofM8p6k/edit). Reproducibility and future Colab FinBERT training: [GitHub V2 research code](https://github.com/Saehon/Saeid-Homayoun/tree/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2). Public-safe synthetic examples: [existing Kaggle package](https://www.kaggle.com/datasets/sadhon/cam-kam-auditbert-public-demo).

**No LoRA weights, generation training, BERTScore or human-auditor response evaluation have been produced in this repository.** The earlier collaborative models retain their original ownership and attribution.
