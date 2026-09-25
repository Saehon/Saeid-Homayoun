# arXiv × GitHub Research Registry — Accounting, Auditing & Financial Reporting

Purpose: frontier-discovery registry for reproducible AI research. arXiv projects supply frontier methods/benchmarks; FT50/ABS4 literature remains the primary theoretical/positioning anchor.

## Ten-project research shortlist

| # | Project | arXiv | Accounting/audit role | FT50/ABS4-style extension |
|---|---|---|---|---|
| 1 | FinVerBench | https://arxiv.org/abs/2605.29586 | SEC 10-K/XBRL financial-statement verification and calibration | ICFR/audit error detection; study false-positive costs and calibrated professional judgment |
| 2 | Fin-RATE | https://arxiv.org/abs/2602.07294 | SEC filing analytics: single-document, cross-entity and longitudinal | CAM/KAM and reporting analytics; decompose retrieval, reasoning, entity and temporal failures |
| 3 | FinAuditing | https://arxiv.org/abs/2510.08886 | Taxonomy-aligned multi-document auditing; semantic, relational and numerical consistency | Map benchmark failures to audit assertions and ICFR risks |
| 4 | Automating Financial Statement Audits with LLMs | https://arxiv.org/abs/2506.17282 | Five-stage automated financial-statement audit evaluation | Compare error detection, standards mapping, explanation and revision against human audit judgments |
| 5 | AuditFraudBench | https://arxiv.org/abs/2606.08345 | Enforcement-grounded fraud benchmark using filings, restatements, MD&A and SEC AAER evidence | Fraud/AAER study of misleading narratives, manipulation patterns and auditor-relevant evidence integration |
| 6 | Company-Isolated Financial Statement Fraud Detection | https://arxiv.org/abs/2607.19259 | Robust FSFD with company-isolated generalization and combined structured/textual evidence | Replace random-split performance with out-of-company/out-of-time audit-risk validation |
| 7 | ESGenius | https://arxiv.org/abs/2506.01646 | ESG/sustainability QA benchmark grounded in authoritative frameworks and documents | ESG assurance: compare zero-shot vs evidence-grounded RAG and traceability |
| 8 | ESGBench | https://arxiv.org/abs/2511.16438 | Explainable ESG QA from corporate sustainability reports with supporting evidence | Test disclosure-quality, evidence traceability and assurance-ready explanations |
| 9 | ESG-Bench | https://arxiv.org/abs/2603.13154 | Long-context ESG reports and hallucination mitigation | Sustainability assurance: factual-support/hallucination tests under long disclosures |
| 10 | RAGChecker | https://arxiv.org/abs/2408.08067 | Fine-grained RAG evaluation framework | Evidence/citation gate across every accounting/audit agent; distinguish retrieval and generation failures |

## Replication design

For every project, create one reproducible research card containing:
- paper/version/DOI or arXiv ID;
- official code repository when verified;
- dataset/benchmark and exact revision;
- license and redistribution constraints;
- original metric and baseline;
- accounting/audit construct;
- SEC/XBRL/PCAOB/AAER/IFRS/ESG evidence mapping;
- fixed train/validation/test or time/company split;
- model/provider/version and prompt/configuration;
- accuracy, precision, recall, F1, FPR/FNR and calibration;
- evidence coverage and citation correctness;
- runtime and cost;
- negative/failure cases;
- independent Reviewer/Falsification result;
- human validation status.

## Research architecture

FT50/ABS4 theory & prior evidence
→ Original replication package
→ SEC/XBRL / PCAOB / CAM-KAM / AAER / IFRS / ESG evidence
→ arXiv frontier benchmark
→ GitHub reproducible implementation
→ Hugging Face dataset/model
→ Kaggle executable notebook
→ Same-task multi-model evaluation
→ Independent Reviewer/Falsification
→ Human auditor validation
→ Replication/extension paper

## Quality gate

A project enters the executable benchmark only after its code/data availability, license, version, provenance and benchmark construction are verified. A paper appearing on arXiv is not treated as FT50/ABS4 evidence by itself.

## Core measurement

Accuracy; precision; recall; F1; false-positive rate; false-negative rate; evidence coverage; citation correctness; calibration; retrieval error; reasoning error; entity/time mismatch; out-of-company generalization; out-of-time generalization; reproducibility; runtime; cost.

## Research priorities

1. Audit/ICFR: FinVerBench + FinAuditing.
2. Fraud/AAER: AuditFraudBench + company-isolated FSFD.
3. SEC/CAM-KAM: Fin-RATE.
4. ESG assurance: ESGenius + ESGBench + ESG-Bench.
5. Evidence/falsification: RAGChecker as the common evaluation gate.

Curated: 2026-09-25.
