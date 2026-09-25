# Kaggle × FT50 / ABS4 Research Registry

A bridge from leading accounting/finance research and replication packages to executable Kaggle notebooks, benchmark datasets, reproducible experiments and future multi-agent accounting/auditing research.

> Kaggle resources are upstream references. Verify availability, licenses, revisions, provenance and competition/dataset rules before reuse. Verify the applicable FT50/AJG edition before using a journal-ranking label in a manuscript.

## Platform role

GitHub = code + provenance + replication registry  
Hugging Face = datasets + models + benchmark data  
Kaggle = executable notebooks + experiments + reproduction + benchmark comparison  
Google Drive = papers + drafts + controlled research files

## Research map

| Research stream | Paper / journal anchor | Replication anchor | Kaggle candidate | Proposed experiment |
|---|---|---|---|---|
| Financial-reporting processes | deHaan et al., Management Science | https://github.com/TiesdeKok/mnsc.2023.4670 | SEC Financial Statement Extracts | Reproduce a reporting-process baseline, then add XBRL/agent evidence tests |
| AI and audit firms | Law & Shen, Management Science | Author replication resources | Financial Analysis Agent / enterprise data-quality agent cases | Standardized audit task with evidence-grounded agent outputs |
| Accounting/finance NLP | Huang et al., Contemporary Accounting Research | https://github.com/feng-li/local-information-advantage | financial reasoning / document benchmarks | Compare original NLP pipeline with LLM/agent classification |
| Financial-statement similarity | Brown, Ma & Tucker, Contemporary Accounting Research | https://github.com/guang-ma/fss | SEC Financial Statement Extracts | Original similarity baseline vs embedding/LLM similarity |
| Finance replication | Jensen, Kelly & Pedersen, Journal of Finance | https://github.com/bkelly-lab/ReplicationCrisis ; https://github.com/bkelly-lab/jkp-data | finance datasets/notebooks | Agent-assisted reproduction and falsification |
| ML asset pricing | Gu, Kelly & Xiu, Journal of Finance | open/independent implementations | financial reasoning/ML notebooks | Compare classical ML and foundation-model workflows under identical splits |

## Kaggle candidates

1. SEC Financial Statement Extracts  
https://www.kaggle.com/securities-exchange-commission/financial-statement-extracts

2. ExtractBench  
https://www.kaggle.com/benchmarks/llamaindex-org/extractbench

3. ParseBench  
https://www.kaggle.com/benchmarks/llamaindex-org/parsebench/leaderboard

4. Financial Analysis Agent  
https://www.kaggle.com/competitions/financial-analysis-agent

5. Finance AI Agent case  
https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/finance-ai-agent

6. AI-powered Enterprise Data Quality Auditor  
https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/ai-powered-enterprise-data-quality-auditor

7. Truth Boundary Lab  
https://www.kaggle.com/competitions/kaggle-measuring-agi/writeups/truth-boundary-lab-v4-measuring-evidence-boundary

8. ESG starter  
https://www.kaggle.com/code/alistairking/esg-dataset-starter

9. CHI-Bench  
https://www.kaggle.com/competitions/chi-bench/overview/abstract

## Proposed Kaggle project

FT50-ABS4-Accounting-Audit-Benchmarks

Suggested notebook families:
- 01_SEC_XBRL_Replication
- 02_Audit_ICFR
- 03_CAM_KAM
- 04_Fraud_AAER
- 05_IFRS_Judgment
- 06_ESG_VSME
- 07_Accounting_Assertions
- 08_Multi_Agent_Comparison
- 09_Falsification
- 10_Human_Validation

## Standard benchmark protocol

Same paper + same data/evidence + same task
→ original published/replication baseline
→ reproducible Kaggle notebook
→ Claude / OpenAI / Gemini / Microsoft
→ blind evaluation
→ accounting/audit assertions
→ evidence verification
→ reviewer/falsification
→ human validation
→ accuracy + precision/recall + evidence coverage + calibration + cost + time

## Pilot 001 — Management Science × SEC/XBRL

Anchor: deHaan et al., *How Resilient Are Firms' Financial Reporting Processes?*  
Replication: https://github.com/TiesdeKok/mnsc.2023.4670  
Kaggle data candidate: SEC Financial Statement Extracts.

Pilot objective:
1. Preserve the original replication baseline.
2. Build a Kaggle notebook with deterministic data preparation and logged versions.
3. Add an SEC/XBRL evidence layer.
4. Run identical evidence through alternative agent/model configurations.
5. Evaluate factual consistency, evidence support, false positives/negatives, reproducibility, runtime and cost.
6. Pass conclusions through an independent falsification step.
7. Reserve final research interpretation for human validation.

## Minimum metadata

Paper; journal; DOI; GitHub/official archive; Kaggle dataset/notebook; dataset version; license; code environment; random seed; train/test split; baseline; agent/model/version; prompt/config; metrics; evidence provenance; failures; human-validation status.

_Last curated: 2026-09-25._
