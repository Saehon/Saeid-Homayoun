# CAM/KAM AuditBERT Public Demo

## Professional cross-platform research package

This Kaggle dataset is the public-safe data layer of a broader research architecture connecting **ChatGPT, GitHub, Hugging Face, Kaggle, and Google Drive**.

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
- CAM/KAM classifier: https://huggingface.co/MaRyAm1295/finBERT-KAM
- KAM response generator: https://huggingface.co/MaRyAm1295/Llama-3.1-8B-KAM

### Data included
This public package contains **synthetic CAM/KAM records only**. It is intended for reproducible preprocessing, teaching, testing, and demonstration.

### Data deliberately excluded
- CAM/KAM records drawn from companies' annual reports,
- unpublished collaborator manuscripts,
- private Google Drive source workbooks,
- confidential or restricted research material.

### Governance
GitHub is the canonical reproducibility layer. Kaggle is the discoverable data/notebook layer. Hugging Face is the model layer. Google Drive remains the private manuscript and licensed-data archive.

This dataset does not provide an audit opinion and is not a substitute for professional judgment or applicable auditing standards.


## Research update — AuditBERT-USUK V2, 16 October 2026

**Research software lead: Dr. Saeid Homayoun.** This is the existing public-safe **synthetic data demo**, not the proprietary/private full CAM/KAM corpus and not a real trained FinBERT/Llama model.

Exploratory private-source **TF–IDF + balanced LinearSVC** topic-classification benchmarks have been measured with issuer-disjoint test partitions. US CAM: **36,771** unique eligible matter texts; 5,648 heldout test observations; macro-F1 **0.778623**, accuracy **0.867387**, description-only macro-F1 **0.766761**. UK-headquartered KAM candidate cohort: **33,724** unique eligible matter texts; 5,188 heldout observations; macro-F1 **0.756715**, accuracy **0.820740**, description-only macro-F1 **0.717099**. Initial exploratory results were superseded after removing exact duplicate text clusters with conflicting vendor topic labels.

These aggregate-only benchmark metrics may be distributed for transparent discussion, but **the real source observations, identifiers, vendor-assigned topic rows and original notebooks are not part of this Kaggle dataset**. The UK-headquarters sample must not be labeled a confirmed ISA (UK) KAM corpus. No audit-report-year validation or semantic near-duplicate leakage testing has been completed. Cross-country scores compare different original topic taxonomies and are not comparable as a common-label study.

The same synthetic example CSV and provenance manifest are retained; *auditbert_v2_benchmark_metrics.json* adds only an aggregate research-results manifest, not new raw observations. The source code, verified configuration, and supervised Colab GPU entry point are [in the existing GitHub V2 branch](https://github.com/Saehon/Saeid-Homayoun/tree/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2). Detailed research caveats and source hashes remain in the [existing private Google Drive research registry](https://docs.google.com/document/d/1YmktPLQ-be1sIFd-Ghlpvd7r156C2boC3y9eofM8p6k/edit). The separate [Hugging Face public static demo](https://huggingface.co/spaces/SADHON/dr-saeid-homayoun-auditbert-v2) is keyword-based; its two linked private model repositories do not yet contain trained FinBERT or Llama weights.
