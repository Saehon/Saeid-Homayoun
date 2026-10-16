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
