# Jev–LLM Probabilistic Decision Intelligence for Accounting and Auditing
**Research proposal | Saeid Homayoun | 15 October 2026**
**Status: proposal only. Jev is not installed; API, license and empirical performance unverified.**

## Aim
Test whether typed probabilistic decision models such as Jev, combined with LLM evidence extraction and independent AI-to-AI verification, improve audit risk discrimination, calibration, traceability and cost-effectiveness relative to standalone LLMs and conventional machine learning.

## Research tracks
| Priority | Existing project | Research application |
|---|---|---|
| 1 | Risk–CAM Alignment | Classify account-level risk, CAM informativeness and independently validated CAM effectiveness |
| 1 | ICFR–SEFD–SEC–TimesFM | Predict future material weaknesses, assess uncertainty and calibration |
| 2 | NAAIL MCP / LEMON-ICFR-US | Evidence provenance, risk gates, abstention, human approval |
| 2 | PCAOB inspection agent | Risk-based inspection triage and evidence review |
| 2 | AI CapEx audit | Misstatement-risk classification |
| 2 | TDABC/tokenized AI management accounting | Token-cost anomalies, routing and cost per correct decision |
| 3 | ESG assurance | Disclosure inconsistency and greenwashing risk |
| 3 | Fama–French / Damodaran | Risk features and scenario probabilities |

## Hypotheses
H1 Hybrid Jev–LLM models improve out-of-sample risk discrimination over standalone LLMs.
H2 Hybrid models improve probability calibration and reduce unsupported confidence.
H3 CAM risk alignment predicts subsequent reporting outcomes beyond CAM presence.
H4 Hybrid models improve prospective ICFR weakness prediction.
H5 Risk-based routing reduces computational cost per validated decision.
H6 Independent verification and abstention reduce unsupported assurance decisions.
H7 Effects vary by industry, accounting domain and firm complexity.
H8 Calibrated risk signals provide incremental predictive information about future reporting outcomes.

## Research design
Unit: firm-year-account domain, linked to CAM observations when applicable.
Data: validated SEC/XBRL/ICFR, CAM/KAM, PCAOB and existing canonical project datasets.
ICFR taxonomy: **effective / ineffective / unknown or unverified**, crossed with industry and control/accounting domain. Do not infer effectiveness solely from missing weakness disclosures.
CAM effectiveness must be independently defined; CAM presence/absence is not a quality or control-effectiveness verdict.
For US revenue reporting use ASC 606; IFRS 15 only where applicable.
Benchmarks: logistic regression, XGBoost, FinBERT, Granite, Claude/GPT, optional Jev and hybrid.
Validation: temporal holdout, leakage prevention, PR-AUC, Brier, ROC-AUC, ECE, recall at fixed review budget, latency, cost per correct decision, bootstrap intervals, industry/domain heterogeneity.
DiD requires a defensible intervention, timing and comparison group; predictive accuracy alone is not causal evidence.

## Architecture
Evidence -> LLM structured extraction -> calibrated probabilistic decision (Jev only if authorized, otherwise baseline) -> independent AI-to-AI evidence/uncertainty checks -> human decision (approve/escalate/abstain).

## Installation plan (NOT YET EXECUTED)
1. Confirm Jev API/SDK availability, terms, licensing, pricing, model identifier and data processing conditions from official vendor.
2. Obtain authorized credentials via secure secrets; never commit tokens or sensitive client evidence.
3. Implement provider-neutral adapter and calibrated logistic/XGBoost fallback.
4. Pilot synthetic/public CAM examples; benchmark against baselines with reproducible splits and seeds.
5. Enable Jev adapter only after API access and response schemas are verified.
6. Record model versions, code hashes, metrics, provenance and human-review decisions.
No local or remote Jev installation is asserted here.

## Project management
Weeks 1–2 feasibility; 3–5 CAM pilot; 6–8 ICFR pilot; 9–10 verification; 11–12 robustness; 13–16 manuscript.
Target research audiences: TAR, JAR, JAE, CAR and AOS. Contribution must be accounting-theoretical, not merely algorithmic.
Reuse canonical Google Drive datasets/workbooks and add worksheets rather than duplicate files; preserve history. This project-specific GitHub proposal does not alter GitHub pauses for unrelated projects.

## Research references
- Bao et al. (2020), *Journal of Accounting Research*. https://doi.org/10.1111/1475-679X.12292
- Dechow et al. (2011), *Contemporary Accounting Research*. https://doi.org/10.1111/j.1911-3846.2010.01041.x
- Gu, Kelly & Xiu (2020), *Review of Financial Studies*. https://doi.org/10.1093/rfs/hhaa009
- Guo et al. (2017), ICML, calibration. https://arxiv.org/abs/1706.04599
- Brier (1950), *Monthly Weather Review*.

## Vendor/video references (claims require verification)
https://youtu.be/YGgNBcIgI4s
https://typesafe.ai/
https://typesafe.ai/blog/introducing-system-one-models-and-jev


## Open-source Jev-family variants: research integration (2026-10-15)
These are **independent third-party projects, not official Jev releases**. Their claims and licenses must be verified before redistribution or production use. We link upstream sources rather than copying their model weights or code, preserving attribution and avoiding redundant files.

| Variant | Upstream | Accounting adaptation | Verification gate |
|---|---|---|---|
| OpenJev-RLCD | https://github.com/ZimmyGao/openjev-rlcd | CAM/ICFR confidence calibration, selective prediction, Brier and coverage evaluation | Reproduce published calibration pipeline; benchmark with held-out accounting labels |
| openJev-verdict-2.0 | https://github.com/Heman10x-NGU/openJev-verdict-2.0 | Typed CAM relevance, account-domain and ICFR risk decisions | Check weights, license, label semantics, benchmark leakage, and calibration |
| OpenJevX | https://github.com/muthuishere/openjevx | Optional local service for NAAIL/LEMON risk gates and AI-to-AI checks | Install separately; confirm local endpoint schema, authentication and inference |
| Calibrated logistic/XGBoost | Train from validated project data | Transparent baseline for all tracks | Chronological splits and independent test data |

### Executable comparison harness
`benchmark.py` is a dependency-free evaluator, **not a Jev installation or a pretrained classifier**. Obtain independently scored held-out probabilities from each model and supply a CSV with columns:
`variant,industry,domain,icfr_status,label,p_event`.
Here `label` is the *observed future event* (0/1/blank), `p_event` its predicted probability, and `icfr_status` is effective/ineffective/unknown. Do not substitute ICFR status for the observed outcome or label CAM effectiveness by CAM presence. Keep firm/year identifiers in canonical datasets for split validation.

```bash
python research/jev-ai-audit/benchmark.py --variants
python research/jev-ai-audit/benchmark.py --input /path/to/heldout_predictions.csv
```

The evaluator returns grouped Brier, precision and recall by model × industry × accounting domain, excluding unknown *outcome* labels without imputing them as negatives. Results are descriptive and must not be interpreted as published validation, statistical significance, or Jev performance. For rare outcomes, extend the analysis with PR-AUC, confidence intervals and cost-sensitive utility before submitting a manuscript.

**Implementation stages:** CAM first (revenue/ASC 606, inventory, goodwill); ICFR second (effective/ineffective/unknown stratification); NAAIL/PCAOB third (human approval and abstention). Only public/synthetic data until privacy approval. No model weights, external package, API token, GPU training or live service has been installed by this PR.


## FT50-SUPPORTED COMMON RISK ENGINE — 2026-10-16

**Status:** Implemented feature/provenance checks and synthetic tests, NOT an estimated DEARS risk score, validated Jev model, completed replication, or publication result. Maintainer attribution: **Dr. Saeid Homayoun**.

**Code:** `common_risk_engine.py` creates *point-in-time* accounting features using explicit metadata (`firm_id, fiscal_year, industry, domain, accounting_standard, cutoff_date, evidence_available_date, icfr_status`). It returns eight candidates: accrual intensity, receivables/sales gap, inventory/sales gap, goodwill/assets, leverage, revenue growth, log segment count, and loss indicator. Missing denominators return `None`, not zero; a source availability date after cutoff raises an error; future outcomes are not treated as features. `cam_smoke_test.py` includes synthetic feature/leakage tests. Data custodians must audit each raw field's publication date; a single row-level maximum availability date alone is not sufficient proof of point-in-time correctness. Coefficients, calibration, data imputation, sample selection, and any JEV API adapter must be separately fitted and validated, NEVER imputed from journal articles.

**Common taxonomy:** effective / ineffective / unknown ICFR × industry × accounting domain; US-GAAP revenue → ASC 606, IFRS revenue → IFRS 15. CAM selection, CAM effectiveness, ICFR status, and PCAOB findings must be assessed separately and independently. CAM or PCAOB findings are never used as contemporaneous ex-ante risk features. PCAOB public inspection observations generally support auditor/firm level rather than invented issuer-specific links.

### Verified publications and replication sources (authoritative links)

| Study / journal | DOI | Replication access | Role / integrity gate |
|---|---|---|---|
| Bao, Ke, Li, Yu & Zhang (2020), **JAR**, accounting fraud ML | https://doi.org/10.1111/1475-679X.12292 | **Author data and MATLAB code:** https://github.com/JarFraud/FraudDetection | Corrected RUSBoost; must incorporate 2022 erratum https://doi.org/10.1111/1475-679X.12454 |
| deHaan, de Kok, Matsumoto & Rodriguez-Vazquez (2023), **Management Science**, resilience | https://doi.org/10.1287/mnsc.2023.4670 | **Author Python/SAS/Stata:** https://github.com/TiesdeKok/mnsc.2023.4670 | Raw licensed source data not included; reporting-process risk validation |
| Gassen & Veenman (2026), **JAE**, robust inference | https://doi.org/10.1016/j.jacceco.2026.101895 | **Author R/Stata code:** https://github.com/dveenman/robust | Robust regression / high-dimensional FE; some WRDS inputs required; inferential module only |
| Breuer & Schütt (2023), **RAST**, Bayesian accruals | https://doi.org/10.1007/s11142-021-09654-0 | **Author sample code/data:** https://github.com/hschuett/AccForUncertaintyCode | Measurement uncertainty; not a calibrated risk score by itself |
| Dechow, Ge, Larson & Sloan (2011), **CAR**, F-score | https://doi.org/10.1111/j.1911-3846.2010.01041.x | Published method; **original-author executable code not confirmed** | Conventional misstatement-risk benchmark; independently implement and validate |
| Burke, Hoitash, Hoitash & Xiao (2023), **TAR**, CAM | https://doi.org/10.2308/TAR-2021-0013 | Published methods; **public analysis code not confirmed** | CAM selection / expected-unexpected topics; prevent construct duplication |
| Dee, Luo, Wang & Zhang (2026), **JAE**, CAM–ICFR | https://doi.org/10.1016/j.jacceco.2025.101834 | Published methods; **public analysis code not confirmed** | Account-level CAM/ICFR mechanism; incremental novelty required |
| Hassan, Hollander, van Lent & Tahoun (2019), **QJE**, firm political risk | https://doi.org/10.1093/qje/qjz021 | **Authors' risk data:** https://www.firmlevelrisk.com/download | Textual risk design/TF–IDF; different risk construct, not an accounting risk model |
| PCAOB firm inspection data (regulator, **NOT FT50 paper**) | https://pcaobus.org/oversight/inspections/firm-inspection-reports | Official public Part I.A/B CSV/XML/JSON | Auditor-level deficiency design with inspection-selection and publication-timing safeguards |

**Three FT50 paper pathways:** (A) ex-ante risk × CAM selection/alignment → future outcomes; (B) risk × ICFR taxonomy → future material weaknesses; (C) auditor-level aggregated risk × PCAOB published inspection outcomes (subject to identification and coverage checks). Predictive lift must be established out of sample, and causal claims require separately defensible identification.

**Research reproducibility protocol:** Freeze definitions and source checksums before modeling; train/validate/test strictly by public-availability dates, prevent shared-firm leakage, benchmark logistic regression / Dechow F-score / corrected Bao ML / FinBERT / JEV only if genuine accessible outputs exist, report PR-AUC + Brier + reliability + Recall@K + bootstrap CI, and retain all adverse/null results. Link third-party repositories rather than redistributing weights or licensed data. Upload no confidential Drive data to public GitHub or Hugging Face. Canonical empirical registry: existing Google Sheet `03_EMPIRICAL_RESULTS_Risk_CAM_DARWIN_V2`, new tab `FT50_RISK_REPLICATION`.

## JAR Risk–CAM Manuscript and Replication Package — 2026-10-16

[Publication package and synthetic validation source](./jar-risk-cam/README.md) includes the exact previously archived synthetic starter ZIP, six unit tests, validation script, synthetic data, and the publication timetable and reference links.

- **Private canonical Drive folder:** https://drive.google.com/drive/folders/1rX5r3VIS5x4prq0hlFFNIrH6OTACyuvB
- **Word manuscript (Drive only; unpublished):** https://docs.google.com/document/d/1ARsLl2pDqf1wmtwo8GWO2vxr5UKMxegc/edit
- **Google Drive ZIP:** https://drive.google.com/file/d/1qGtbIOubT4X6NOxbybTI-F-whWIRETWX/view
- **Publication plan:** https://docs.google.com/document/d/1CT6pp2160s51kgY1k2vF31jCGaS_DM22hUvMnslLf18/edit

The GitHub repo is **public**. No private raw CAM dataset, restricted external data, or unpublished full-text manuscript has been copied into the public repository. The synthetic validation is NOT empirical evidence, and neither actual Jev inference nor FT50 model replication is claimed.
