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
