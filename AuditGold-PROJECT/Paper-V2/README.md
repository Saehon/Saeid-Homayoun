# AuditGold-PROJECT — Manuscript V2 and Research Replication Map

**Created:** 17 November 2026  
**Target:** *Journal of Management Information Systems* (FT50), Agentic Organizations special issue.  
**Status:** working paper draft, not submitted, no experimental runs or expert-certified gold answers.

## Contents

- `manuscript/AuditGold_JMIS_Manuscript_V2.docx` — formatted 12-page research manuscript draft.
- `manuscript/AuditGold_JMIS_Manuscript_V2.md` — public, editable Markdown source.
- `sources/FT50_AJG4_Replication_Evidence_Matrix.csv` — 17 independently differentiated research and primary-source entries, with venue, code/data evidence, limitations and publication links.
- `replication/score_agentic_runs.py` — standalone standard-library scoring utility for **future human-adjudicated experimental traces**, with 95% Wilson intervals and guardrails.
- `replication/validate_source_matrix.py` — metadata validation for the reproducibility registry (not replication of third-party papers).
- `replication/synthetic_smoke_only.csv` — fabricated *unit-test fixture*, intentionally **not** scientific data or an experiment.
- `quality/DEMO_Smoke_Results_NOT_EMPIRICAL.json` — smoke-test output (not scientific results).

## Verified sources with computational material

- Bao et al. (2020, JAR): [author code and final data](https://github.com/JarFraud/FraudDetection); fraud is AAER-proxy rather than universal truth; read erratum.
- Law & Shen (2025, Management Science): [author-listed complete publisher replication archive](https://kelvinlaw.me/data); not downloaded or run in this study.
- Nguyen & Nguyen (2026, ISR): [R analysis code and processed data](https://github.com/mikenguyen13/p-hacking-publication-bias-information-systems); a methods-transparency analogue, not audit engagement data.
- Blankespoor et al. (2026, JAR): [GenScore data](https://github.com/ed-dehaan/GenScore) under CC BY 4.0; no verified complete open commercial AI-detection pipeline.
- Ciconte et al. (2026, RoAS): [prompts, Jupyter notebooks and generated research artifacts](https://github.com/AIPoweredAccountingScholarship/Base); a falsification case, not audit labels.

External evaluation controls: [FinQA](https://github.com/czyssrs/FinQA), [TAT-QA](https://github.com/NExTplusplus/TAT-QA), and [FinanceBench](https://github.com/patronus-ai/financebench) (FinanceBench openly released sample n=150, CC BY-NC). Do not publish data acquired under incompatible licenses.

## Reproducibility quick-start

```bash
python replication/validate_source_matrix.py sources/FT50_AJG4_Replication_Evidence_Matrix.csv
python replication/score_agentic_runs.py replication/synthetic_smoke_only.csv
```

The scoring script **does not run or score an AI model**, and its supplied fixture contains invented test rows to confirm parsing, input validation and arithmetic. To generate publishable evidence, independently adjudicated trace-level results and real model outputs must replace this fixture. Log family-level sample sizes and code/model versions, treat related template variants as clustered observations, and preregister the statistical comparisons.

## Release governance

This package contains **no private CAM/ICFR gold-answer keys** and no private or proprietary third-party data. GitHub publication is requested by the author as a publicly visible **working manuscript**; it does not imply JMIS submission or acceptance. Reconfirm journal preprint/AI-use policy before formal submission and freeze external source hashes before claiming archival replication. No automatic synchronization exists between Drive and GitHub.
