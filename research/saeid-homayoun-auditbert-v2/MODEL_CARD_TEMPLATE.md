---
language: en
tags:
- accounting
- audit
- cam
- kam
- finbert
- text-classification
pipeline_tag: text-classification
base_model: yiyanghkust/finbert-tone
---

# Saeid-FinBERT-KAM-V2 — Model Card Template (NOT TRAINED)

**Planned repository:** `SADHON/saeid-finbert-kam-v2`  
**Independent implementation / research lead:** Dr. Saeid Homayoun, University of Gävle, Sweden  
**Status:** PROPOSED — this file describes the publication standard. **No model has been uploaded or fine-tuned and no test result has been established.**

## Task
Classification of CAM/KAM disclosures into reproducibly specified accounting-topic labels.

## Base checkpoint / attribution
The independently fine-tuned checkpoint will begin from `yiyanghkust/finbert-tone`, a third-party FinBERT checkpoint; verify applicable redistribution conditions when publishing. Prior comparison checkpoints (not owned by this account):
- https://huggingface.co/MaRyAm1295/finBERT-KAM
- https://huggingface.co/MaRyAm1295/Llama-3.1-8B-KAM

## Dataset governance
Use only data for which the project has authorized research/compute rights. Public model weights require separate confirmation of training-data/model licensing and privacy restrictions. Never upload private Google Drive files, individual identifiers, raw licensed datasets, or authentication tokens as training artifacts.

**Actual dataset inventory:** [TO BE COMPLETED AFTER VERIFIED RUN].  
**Topic taxonomy:** [TO BE RECONCILED — previous paper differs between 48 and 49 labels].  
**Rows/companies/years:** [TO BE MEASURED, NOT COPIED FROM EARLIER PAPER].

## Training and evaluation (after real run)
Record Git commit, base model revision, package versions, private input SHA256, annotation provenance, deduplication policy, split seed, group IDs/time cutoff, epochs, learning rate, batch size and class support.

| Quantity | Value |
|---|---|
| Train / validation / test counts | PENDING |
| Macro F1, held-out | PENDING |
| Weighted F1, held-out | PENDING |
| Micro F1, held-out | PENDING |
| Per-topic precision/recall/F1/support | PENDING |
| Group-disjoint / forward-time leakage audit | PENDING |
| Model limitations and dataset license | PENDING |

Do not upload this placeholder card as if a trained model exists.

## Usage and limitations
Research only; not an audit opinion, assurance conclusion or independently verified audit procedure. Rare labels, distribution shift between UK KAM and US CAM, issuer-specific boilerplate, and truncation beyond the model context can degrade validity. Human review is required.

## Research reference and contribution separation
- Homayoun, S., Rezaee, N., Rezaee, Z., & Khosravian, M. (2026). *AI-Enabled Key Audit Matter Disclosures: A Hybrid LLM Approach to Enhancing Audit Report Transparency*. SSRN. https://doi.org/10.2139/ssrn.7272139
- Huang, A. H., Wang, H., & Yang, Y. (2023). FinBERT: A large language model for extracting information from financial text. *Contemporary Accounting Research*. https://doi.org/10.1111/1911-3846.12832
- V2 software research extension: authored independently under Saeid Homayoun. Any separate research paper requires a substantive independent contribution and correct coauthorship determination.

**Important:** The prior paper's generator BERTScore F1 (83.95%) and classifier macro F1 (83.20%) are historical values; neither is a new V2 result.
