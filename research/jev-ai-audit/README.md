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
