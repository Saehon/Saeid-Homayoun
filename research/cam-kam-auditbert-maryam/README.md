# CAM/KAM AuditBERT — Public Reproducibility Package

## Research project
**AuditBERT: Revolutionizing KAM Disclosures with LLMs**

Collaboration associated with Saeid Homayoun, Zabihollah Rezaee, Maryam Khosravian, Salma Boumediene, and Salem L. Boumediene.

This repository folder is a reproducibility layer for CAM/KAM AuditBERT. The research data originate from **companies' annual reports**, including SEC EDGAR filings where applicable, and are maintained in a standardized research dataset format. Unpublished manuscripts and source datasets are maintained in the project archive.

## Latest validation status (12 October 2026)

See [**October 12 validation update**](VALIDATION_UPDATE_2026-10-12.md) and [**source-of-data clarification**](PROVENANCE_RECONCILIATION_2026-10-12.md). The research owner confirms **companies' annual reports** as the original source, including SEC EDGAR filings where applicable. No additional source-origin test is requested. Remaining research tasks concern KAM truncation, report-year construction, the 49-class discrepancy and exposed access-token remediation. **No new regression result or pipeline PASS is claimed.**

## Cross-platform integration
Master integration record:  
https://github.com/Saehon/Saeid-Homayoun/blob/main/docs/CAM_KAM_AUDITBERT_CROSS_PLATFORM_MASTER.md

Hugging Face dataset mirror:  
https://huggingface.co/datasets/SADHON/cam-kam-auditbert-public-demo

Kaggle benchmark dataset:  
https://www.kaggle.com/datasets/sadhon/cam-kam-auditbert-public-demo

## Research objective
The project studies AI-assisted analysis of **Key Audit Matters (KAMs)** and **Critical Audit Matters (CAMs)**, including:
- accounting-topic classification,
- identification of audit-risk themes,
- assessment of KAM/CAM disclosure specificity,
- support for entity-specific audit-report drafting,
- benchmarking of domain-specific language models.

## Architecture
```
Private/raw KAM + CAM sources
        ↓
schema checks + report-year mapping
        ↓
TITLE + DESCRIPTION text construction
        ↓
topic encoding
        ↓
FinBERT / AuditBERT training or inference
        ↓
evaluation: precision / recall / F1
        ↓
human review and regulatory interpretation
```

## Public files
- `synthetic_cam_kam_sample.csv` — synthetic demonstration records only.
- `prepare_cam_kam_data.py` — validates and prepares a private CAM/KAM dataset locally.
- `requirements.txt` — minimal Python dependencies.
- `DATA_SCHEMA.md` — research-variable schema.
- `SOURCE_MANIFEST.md` — provenance map without exposing private Drive identifiers.
- `README_HUGGINGFACE.md` — Hugging Face-ready dataset card.
- `dataset-metadata.json` — Kaggle-ready metadata.

## Private source assets located
The project sources include a U.S. CAM workbook and UK KAM workbooks in the researcher's private Google Drive, plus the revised AuditBERT/KAM manuscript supplied by Maryam Khosravian via Gmail.

Original annual-report data remain in the project archive. No new record-by-record source-origin audit is needed for this update. Any publication of the original text/data remains a separate release decision; sanitize exposed access tokens first.

## Manuscript data notes
The revised manuscript describes a large CAM/KAM research corpus spanning U.S. and European public companies and an AuditBERT/FinBERT/LLaMA workflow. Before publication, sample-count and topic-count statements should be reconciled across the abstract and methodology.

## Quick start
```bash
pip install -r requirements.txt
python prepare_cam_kam_data.py --input synthetic_cam_kam_sample.csv --output prepared_demo
```

For a private real-data run, point `--input` to an authorized local export of the CAM/KAM data.

## Research integrity
This package is for reproducibility, research and teaching. It does not provide an audit opinion and should not be used as a substitute for professional judgment or applicable auditing standards.
