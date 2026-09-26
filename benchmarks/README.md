# Accounting, Audit & Finance Benchmark Layer

A provider-neutral evaluation layer for research and education. It does not copy third-party benchmark data or code. External frameworks are referenced upstream and must be used under their own licenses.

## Benchmark families

| Benchmark | Core task | Example outputs | Primary metrics |
|---|---|---|---|
| CAM/KAM | detect, classify and track audit matters | topic, entry, exit, persistence, evidence | Precision, Recall, F1, PR-AUC, evidence coverage |
| ICFR | identify and classify control weaknesses | weakness class, severity, evidence, horizon | PR-AUC, Brier, Recall@K, calibration |
| Financial Reasoning | solve evidence-grounded finance/accounting problems | answer, calculation, cited evidence | exact match, numeric tolerance, evidence accuracy |

## Evaluation architecture

Input evidence -> Candidate model/agent -> Deterministic checks -> Independent reviewer/challenge -> Metrics -> Human approval.

### External reference frameworks
- Stanford HELM: https://github.com/stanford-crfm/helm
- BCG X ARTKIT: https://github.com/BCG-X-Official/artkit
- Yale FinanceMath: https://github.com/yale-nlp/FinanceMath

These are references/adapters, not vendored dependencies.

## Research principles
- fixed train/dev/test boundaries where applicable
- no test-set leakage
- provenance and license metadata for every dataset
- model/version/prompt reproducibility
- report false positives and false negatives
- calibration alongside discrimination
- evidence traceability
- human judgment retained for professional conclusions
