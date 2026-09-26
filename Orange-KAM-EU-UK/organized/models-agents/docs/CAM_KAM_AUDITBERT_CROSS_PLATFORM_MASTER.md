# CAM/KAM AuditBERT — Cross-Platform Master Integration

## Canonical project
**Research project:** AuditBERT: Revolutionizing KAM Disclosures with LLMs

**Canonical GitHub package:**  
https://github.com/Saehon/Saeid-Homayoun/tree/main/research/cam-kam-auditbert-maryam

**Canonical open-data demonstration:**  
https://github.com/Saehon/Saeid-Homayoun/tree/main/open-data/cam-kam-auditbert-demo-001

## Platform architecture

| Platform | Role | Canonical location |
|---|---|---|
| GitHub | Code, reproducibility, provenance, validation, manifests and synchronization | https://github.com/Saehon/Saeid-Homayoun |
| Hugging Face | Controlled CAM/KAM synthetic dataset mirror and model/data discovery | https://huggingface.co/datasets/SADHON/cam-kam-auditbert-public-demo |
| Kaggle | Controlled benchmark dataset/notebook mirror | https://www.kaggle.com/datasets/sadhon/cam-kam-auditbert-public-demo |
| Google Drive | Private manuscript, licensed/raw data archive and cross-platform master record | Managed in the researcher's connected Google Drive |

## Verified research models

### CAM/KAM topic classifier
https://huggingface.co/MaRyAm1295/finBERT-KAM

- Task: text classification
- Architecture: BERT / AutoModelForSequenceClassification
- Parameters: approximately 109.8M
- Base model: yiyanghkust/finbert-tone
- Research role: classify CAM/KAM disclosures into accounting-topic categories.

### KAM response generator
https://huggingface.co/MaRyAm1295/Llama-3.1-8B-KAM

- Task: text generation
- Architecture: Llama / AutoModelForCausalLM
- Parameters: approximately 8.17B
- Base model: meta-llama/Llama-3.1-8B-Instruct
- Research role: generate context-aware responses to audit matters.

## Evaluation mapping

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

Do not interchange classifier F1 metrics with response-generation BERTScore metrics.

## Research pipeline

Private/raw CAM + KAM sources  
→ schema validation + provenance checks  
→ TITLE + DESCRIPTION construction  
→ topic encoding  
→ FinBERT / AuditBERT training or inference  
→ precision / recall / F1 evaluation  
→ human review and regulatory interpretation

## Public/private boundary

### Public-safe assets
- synthetic CAM/KAM demonstration data
- schema and provenance documentation
- preparation/validation code
- model registry and dependency links
- reproducibility metadata
- benchmark/notebook scaffolding

### Private / restricted assets
- licensed Audit Analytics observations
- private CAM/KAM workbooks
- unpublished manuscript material unless separately authorized
- any source whose redistribution rights are not established

## Governance

1. GitHub is the canonical reproducibility source.
2. Hugging Face and Kaggle are mirrors/discovery layers, not independent authorities.
3. Google Drive remains the controlled archive for manuscript and licensed/raw research assets.
4. Model ownership is attributed to the external Hugging Face account MaRyAm1295; this package links to those models as research dependencies and does not claim their weights.
5. Human review remains required for interpretation of audit-matter classifications and generated responses.

## Cross-platform synchronization

GitHub workflows:
- .github/workflows/validate_cam_kam_auditbert.yml
- .github/workflows/huggingface-cam-kam-auditbert-sync.yml
- .github/workflows/kaggle-cam-kam-auditbert-sync.yml

## Current verified integration status

- **GitHub:** master registry, Hugging Face manifest, Kaggle manifest, and cross-platform links are committed.
- **Hugging Face:** synchronization completed successfully; dataset updated on 25 Sep 2026 and remains private/controlled. The workflow now stages the cross-platform integration manifest.
- **Kaggle:** dedicated CAM/KAM publication completed successfully; a new dataset version was created and `INTEGRATION_MANIFEST.md` uploaded. Existing workflow configuration keeps controlled/private publication mode.
- **Google Drive:** a native Google Doc master record stores the platform links, model registry, metrics, data boundary, governance, and synchronization status.

An unrelated general Kaggle multi-dataset synchronization job can still fail because another AWS registry dataset has an invalid title length; this does not block the dedicated CAM/KAM Kaggle publication.

## Next benchmark artifact

Recommended notebook:
`CAM-KAM-AuditBERT-Benchmark.ipynb`

Target flow:
synthetic CAM/KAM → finBERT-KAM → topic predictions → precision/recall/F1 → confusion matrix → error analysis → human-review table.

---
Research and teaching use only. This package does not provide an audit opinion and is not a substitute for professional judgment or applicable auditing standards.
