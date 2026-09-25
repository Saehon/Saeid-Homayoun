# Hugging Face × FT50 / ABS4 Research Registry

A bridge between leading accounting/finance research, open replication packages, and Hugging Face datasets/benchmarks for reproducible AI-enabled accounting and auditing research.

> Hugging Face resources are upstream references. Verify licenses, revisions, provenance and research-use constraints before experiments or redistribution. Journal-list classifications should be checked against the FT50/AJG edition used in a manuscript.

## Research map

| Research stream | Paper / journal anchor | GitHub / replication anchor | Hugging Face candidates | Replication / extension task |
|---|---|---|---|---|
| Financial-reporting processes | deHaan et al., Management Science | https://github.com/TiesdeKok/mnsc.2023.4670 | TheFinAI/Herculean; TheFinAI/FinSM | Reproduce/extend reporting-process evidence with XBRL consistency and agent evaluation |
| AI and audit firms | Law & Shen, Management Science | Author replication resources | OumarDicko/Audit_Management_QA; TheFinAI/Herculean | Test audit-domain agents on standardized evidence and audit judgments |
| Accounting/finance NLP | Huang et al., Contemporary Accounting Research | https://github.com/feng-li/local-information-advantage | nlpaueb/finer-139 | Compare traditional NLP with LLM/agent extraction and classification |
| Financial-statement similarity | Brown, Ma & Tucker, Contemporary Accounting Research | https://github.com/guang-ma/fss | SEC/XBRL corpora and knowledge-graph resources | Extend similarity measures using embeddings/LLMs while retaining original benchmark |
| Bayesian accounting methods | Breuer & Schütt, Review of Accounting Studies | https://github.com/hschuett/AccForUncertaintyCode | Accounting/financial evaluation datasets | Compare probabilistic uncertainty with LLM confidence/calibration |
| Finance replication | Jensen, Kelly & Pedersen, Journal of Finance | https://github.com/bkelly-lab/ReplicationCrisis ; https://github.com/bkelly-lab/jkp-data | Finance benchmarks/models | Agent-assisted replication and falsification across published factors |
| ML asset pricing | Gu, Kelly & Xiu, Journal of Finance | Independent/open implementations | Finance reasoning/evaluation datasets | Compare classical ML pipeline with foundation-model reasoning under identical splits |

## Hugging Face benchmark candidates

- https://huggingface.co/datasets/TheFinAI/Herculean — audit/XBRL consistency assertions
- https://huggingface.co/datasets/TheFinAI/FinSM — financial semantic, relational and numerical consistency
- https://huggingface.co/datasets/FinWorkBench/Finch — accounting/finance workflow benchmark
- https://huggingface.co/datasets/nlpaueb/finer-139 — financial entity/XBRL-oriented tagging
- https://huggingface.co/datasets/ArchCoder/Reckon — financial reconciliation
- https://huggingface.co/datasets/Entendre/Crypto-Accounting-Bench — accounting evidence/scoring benchmark
- https://huggingface.co/datasets/SakanaAI/EDINET-Bench — financial/accounting evaluation
- https://huggingface.co/datasets/Tomas08119993/finmmeval-cfa-cpa — professional finance/accounting evaluation
- https://huggingface.co/datasets/OumarDicko/Audit_Management_QA — audit-management QA
- https://huggingface.co/datasets/jonathanschmoll/eu-taxonomy-dataset — EU sustainability/taxonomy research
- https://huggingface.co/datasets/exo-is/VSME-artificial-report — VSME reporting experiments

## Proposed Hugging Face repository

SADHON/FT50-ABS4-Accounting-Audit-Benchmarks

Suggested structure:
- SEC-XBRL
- Audit-ICFR
- CAM-KAM
- Fraud-AAER
- IFRS
- ESG
- Accounting-Assertions
- Replication-Benchmarks

## Standard experiment

Same paper + same evidence + same task
→ Original replication baseline
→ Claude / OpenAI / Gemini / Microsoft
→ Hugging Face dataset/benchmark
→ Blind evaluation
→ Reviewer / Falsification
→ Human validation
→ Accuracy + Precision/Recall + Evidence Coverage + Calibration + Cost + Time

## Minimum metadata

Paper; journal; DOI; original data; replication code; HF dataset/model; revision; license; task definition; train/test split; baseline; metrics; agent/model version; prompt/config; evidence provenance; result; failure cases; human-validation status.

_Last curated: 2026-09-25._
