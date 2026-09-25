# Databricks × FT50/ABS4 Research Registry — Accounting, Auditing & Finance

Purpose: use Databricks as the reproducible data, experiment, evaluation and governance layer connecting FT50/ABS4 replication research with SEC/XBRL, PCAOB, CAM/KAM, AAER, IFRS and ESG evidence.

## Platform role

GitHub = code + architecture + provenance  
Hugging Face = datasets + models  
Kaggle = executable notebooks + public benchmarks  
arXiv = frontier research discovery  
Google Drive = papers + controlled research documents  
Databricks = data engineering + scalable compute + ML/GenAI experiment tracking + lineage/governance

## Core open-source components

1. MLflow — https://github.com/mlflow/mlflow
   - Experiment tracking, traces, evaluation, prompt/model lineage and reproducibility.
   - Research use: log identical accounting/audit tasks across models and retain metrics, traces, configuration and failures.

2. Delta Lake — https://github.com/delta-io/delta
   - Open-source Lakehouse storage framework.
   - Research use: versioned SEC/XBRL, CAM/KAM, AAER, ICFR and ESG research tables with reproducible transformations.

3. MLflow Agent Evaluation skills — https://github.com/mlflow/skills
   - Evaluation workflows based on datasets, scorers and tracing.
   - Research use: common evaluation harness for cross-provider accounting/audit agents.

## Research modules

### 01 SEC/XBRL
SEC filings → raw/bronze → normalized/silver → research/gold tables → replication baseline → agent experiment → MLflow evaluation → falsification → human validation.

Primary outcomes: factual accuracy, numerical consistency, entity/time consistency, evidence coverage, citation correctness and reproducibility.

### 02 Audit / ICFR
CompanyFacts + controls/material-weakness labels + audit evidence → risk model/agent → assertion-level tests → Reviewer/Falsification → human audit validation.

Primary outcomes: PR-AUC, Brier/calibration, recall at review capacity, FPR/FNR, evidence sufficiency and false-alarm cost.

### 03 CAM/KAM
CAM/KAM corpus → deterministic preprocessing → topic/account/assertion mapping → persistence/entry/exit measures → LLM/agent classification → human-coded validation.

Primary outcomes: precision/recall/F1, agreement with human coding, temporal stability, evidence traceability and reproducibility.

### 04 Fraud / AAER
SEC filings + restatements + AAER evidence → structured/text features → fraud-risk models/agents → out-of-company/out-of-time validation → falsification.

Primary outcomes: generalization, class-imbalance-aware metrics, calibration, false-negative risk and explainable evidence.

### 05 IFRS Judgment
IFRS cases + disclosed accounting policies + structured facts → judgment task → multi-model comparison → evidence/standards verification → human expert gate.

Primary outcomes: judgment consistency, evidence support, standards grounding, uncertainty calibration and failure taxonomy.

### 06 ESG / VSME Assurance
Sustainability reports + structured ESG data + VSME/ESRS mappings → disclosure extraction → assurance tests → evidence/citation verification.

Primary outcomes: completeness, disclosure quality, hallucination/factual-support rate, traceability and assurance-ready explanations.

## FT50/ABS4 replication layer

Original FT50/ABS4 paper
→ reproduce published baseline
→ preserve original sample/construction
→ build a versioned Databricks research table
→ add agentic/AI extension without altering the baseline
→ run identical tasks across OpenAI / Anthropic / Gemini / Microsoft configurations
→ log runs/traces/metrics in MLflow
→ independent Reviewer/Falsification
→ human validation
→ report successful AND failed replications/extensions.

Initial anchors already maintained in the project registry include:
- deHaan, de Kok, Matsumoto & Rodriguez-Vazquez — Management Science — financial-reporting processes.
- Law & Shen — Management Science — AI and audit firms.
- Huang, Li, Li & Lin — Contemporary Accounting Research — local information advantage.
- Brown, Ma & Tucker — Contemporary Accounting Research — financial-statement similarity.
- Breuer & Schütt — Review of Accounting Studies — Bayesian accounting methods.
- Jensen, Kelly & Pedersen — Journal of Finance — replication in finance.
- Gu, Kelly & Xiu — Journal of Finance — machine learning in asset pricing.

Verify the applicable FT50/AJG edition and official replication package before using ranking labels in a manuscript.

## Standard Databricks experiment card

Every experiment should record:
- paper / research question;
- dataset name + immutable version;
- source/provenance;
- transformation/code commit;
- train/validation/test or company/time split;
- agent/model/provider/version;
- prompt/configuration;
- baseline;
- accuracy / precision / recall / F1;
- PR-AUC / ROC-AUC where appropriate;
- calibration/Brier where appropriate;
- FPR/FNR;
- evidence coverage;
- citation correctness;
- latency and cost;
- trace/run ID;
- failure cases;
- Reviewer/Falsification result;
- human-validation status.

## Quality gate

Do not treat Databricks as the scientific contribution. The contribution must remain an accounting/auditing/finance question with a credible construct, baseline and identification/evaluation design. Databricks provides reproducibility, scale, lineage and experimental control.

A result is paper-ready only when:
Data provenance PASS
→ Baseline replication PASS
→ Split/leakage checks PASS
→ Cross-model identical-task check PASS
→ Evidence verification PASS
→ Falsification PASS
→ Human validation PASS.

## Proposed repository structure

external-agent-ecosystems/databricks/
  README.md
  01-sec-xbrl/
  02-audit-icfr/
  03-cam-kam/
  04-fraud-aaer/
  05-ifrs/
  06-esg-vsme/
  07-agent-evaluation/
  08-falsification/
  09-human-validation/
  10-ft50-replications/

Curated: 2026-09-25.
