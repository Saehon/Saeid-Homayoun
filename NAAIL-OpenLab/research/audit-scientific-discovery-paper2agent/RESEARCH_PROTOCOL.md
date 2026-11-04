# Preregisterable FT50 audit research protocol (DRAFT, not preregistered)
**Working title:** Can Evidence-Governed Scientific AI Agents Improve Fraud-Risk Triage and Risk–CAM Alignment?

## Research questions
RQ1: Does evidence-gated AI reduce unsupported audit-risk recommendations relative to ungated prediction?
RQ2: Does model competition improve genuinely out-of-time fraud-risk discrimination and calibration beyond the original validated benchmark?
RQ3: Is residual risk–CAM misalignment associated with subsequent restatements, ICFR deficiencies, or audit outcomes *after* risk, complexity, industry, auditor and time controls?

## Testable propositions (not empirical results)
H1: Evidence gating reduces unsupported actionable recommendations without changing the underlying predictive score.
H2: AlphaEvolve-inspired, strictly validation-selected models improve external holdout Brier / PR-AUC over precommitted non-evolved baselines, conditional on no data leakage; it may fail.
H3: High pre-audit risk without an associated CAM predicts subsequent adverse outcomes after controls; CAM presence itself is NOT a valid proxy for effective/ineffective audits.

## Units and design
- Pilot unit: synthetic case; target empirical unit: firm-year and account/topic-year.
- Fraud and ICFR material weakness are **distinct labels**; do not conflate.
- Separate pre-report risk features from later CAM disclosure. Use SEC acceptance dates, auditor report dates and first-available news/AAER dates. Avoid hindsight labels in prediction.
- A0 original Bao RUSBoost: implement independently from corrected source, NOT the heuristic synthetic A0 of the software smoke test.
- A1 original published baseline + evidence grounding; A2 + pre-specified multi-agent hypothesis tournament; A3 + bounded program search, independent falsifier and human gate.
- Report PR-AUC, Recall@K, Brier, calibration, unsupported-claim frequency, false positive/negative rates, evidence coverage, decision time/cost and professional judgment accuracy with confidence intervals.
- Candidate selection only on training/validation; held-out test sealed and evaluated once for the preregistered comparison; cluster by firm as appropriate.
- Benchmark expert judgments should be independent of model scoring; separately test human-AI review using randomization if feasible.
- Risk–CAM prediction and subsequent-outcome association require explanatory validity tests; **do not infer causal effects from cross-sectional correlations**.
- Power analysis using pilot effect size and preregistration before final evaluation.

## Publications / novelty boundary
Foundational fraud prediction: Bao et al. (2020), JAR; 2022 correction.
CAM disclosure construct: Burke et al. (2023), TAR.
Audit technology effects: Law and Shen (2025), Management Science.
CAM and ICFR overlap: Dee et al. (2026), JAE.
Research agent architecture: Miao et al. (2026), Nature.
All publication details, source code permissions and extant literature must be checked again at full manuscript stage; this is NOT a systematic review.

## Ethics / rights / interpretation
Use SEC primary filings and public PCAOB evidence, licensed inputs only as authorized, or synthetic demos. Preserve all negative results, data provenance and SHA256 hashes. No private regulator documents. Multi-agent consensus is not validation. Declare external AI services and exact versions only after actual execution.

**Current status:** pilot specification and synthetic runtime; no real accounting evidence tested, no completed Bao replication and no FT50 manuscript results.
