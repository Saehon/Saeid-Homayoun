# arXiv × GitHub Research Registry — Accounting, Auditing & Financial Reporting

Purpose: frontier-discovery registry for reproducible AI research. arXiv projects supply frontier methods/benchmarks; FT50/ABS4 literature remains the primary theoretical/positioning anchor.

## High-priority verified seed projects

| Priority | Project | arXiv | Research role | Recommended use |
|---|---|---|---|---|
| 1 | FinVerBench | https://arxiv.org/abs/2605.29586 | Financial-statement verification and calibration; SEC 10-K/XBRL | ICFR/audit error detection, false-positive calibration, construct-valid benchmark |
| 2 | Fin-RATE | https://arxiv.org/abs/2602.07294 | SEC-filing analytics across single-document, cross-entity and longitudinal tasks | CAM/KAM, reporting analytics, retrieval-vs-reasoning error decomposition |
| 3 | FinAuditing | https://arxiv.org/abs/2510.08886 | Taxonomy-structured multi-document auditing; semantic, relational and numerical consistency | XBRL audit assertions, ICFR, evidence-grounded audit agents |
| 4 | Automating Financial Statement Audits with LLMs | https://arxiv.org/abs/2506.17282 | Five-stage automated financial-statement audit benchmark | Error detection, standards mapping, explanation/revision limits |
| 5 | RAGChecker | https://arxiv.org/abs/2408.08067 | Fine-grained RAG evaluation | Evidence/citation layer and retrieval-vs-generation diagnostics |

## Selection rule for the next additions

Only add a project when it has most of:
1. public paper/preprint;
2. public code or reproducible implementation;
3. public/constructible dataset or benchmark;
4. accounting/audit/finance relevance;
5. explicit evaluation metrics;
6. version/provenance information;
7. a clear extension to an FT50/ABS4 research question.

Do not add projects merely because they are popular LLM/agent repositories.

## Research architecture

FT50/ABS4 theory & prior evidence
→ Original replication package
→ SEC/XBRL / PCAOB / CAM-KAM / IFRS / ESG evidence
→ arXiv frontier benchmark
→ GitHub reproducible implementation
→ Hugging Face dataset/model
→ Kaggle executable notebook
→ Same-task multi-model evaluation
→ Independent Reviewer/Falsification
→ Human auditor validation
→ Replication/extension paper

## Core measurement

Accuracy; precision; recall; F1; false-positive rate; false-negative rate; evidence coverage; citation correctness; calibration; retrieval error; reasoning error; entity/time mismatch; reproducibility; runtime; cost.

## FT50-quality design principle

The contribution should not be “we used several LLMs.” The empirical contribution should identify a theoretically meaningful accounting/audit failure mode, preserve a credible baseline, use identical evidence/tasks across systems, separate retrieval from reasoning failures, document negative results, and subject conclusions to independent falsification and human validation.

## Target research modules

- SEC/XBRL financial-reporting verification
- Audit assertions
- ICFR/material weakness
- CAM/KAM
- Fraud/AAER
- IFRS judgment
- ESG/VSME assurance
- Evidence/citation verification
- Cross-provider agent comparison
- Replication/falsification

Curated: 2026-09-25.
