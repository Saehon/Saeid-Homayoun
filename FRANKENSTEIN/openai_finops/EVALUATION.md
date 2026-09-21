# OpenAI Finance & Operations Audit Profile — Evaluation Framework

The system should be evaluated as an audit decision-support capability, not only as an LLM application.

## Core evaluation dimensions

| Dimension | Question | Example metric |
|---|---|---|
| Detection quality | Does the deterministic layer find known seeded exceptions? | Recall / precision by rule |
| False-positive control | How often are legitimate transactions flagged? | False-positive rate |
| Evidence completeness | Are material claims linked to valid finding IDs? | % claims with validated evidence |
| Evidence hallucination | Does any agent invent unsupported finding IDs? | Unsupported-reference rate |
| Calibration | Does confidence correspond to observed correctness? | Brier score / calibration curve |
| Abstention quality | Does a specialist say insufficient evidence when its domain data is absent? | Appropriate-abstention rate |
| Challenge yield | Does independent challenge remove or narrow unsupported claims? | % challenged claims revised |
| Cross-domain consistency | Do specialists contradict each other without surfacing the conflict? | Unresolved contradiction rate |
| Reproducibility | Do identical data/configurations produce identical deterministic findings? | Deterministic match rate |
| Provenance | Can the exact input population be verified? | SHA-256 match |
| Human override | How often does the reviewer modify/reject AI conclusions? | Override rate by domain |
| Remediation usefulness | Do recommended actions address the evidenced risk? | Human-rated action relevance |
| Efficiency | What does a complete review cost in time/tokens? | Cost and latency per audit run |

## Minimum promotion gates

A future version should not be promoted beyond research prototype status unless:

1. deterministic rules have unit and regression tests;
2. seeded-positive and seeded-negative evaluation populations exist;
3. unsupported evidence-reference rate is effectively zero after governance enforcement;
4. specialists demonstrate appropriate abstention on missing-domain evidence;
5. independent challenge is evaluated on deliberately overclaimed cases;
6. model/version/configuration and input provenance are captured;
7. security and privacy review is completed;
8. a qualified professional signs off on intended use and decision rights.

## Red-team scenarios

Evaluation sets should include:

- duplicate payments with benign explanations;
- legitimate weekend or out-of-hours processing;
- authorized high-value payments;
- split transactions near approval thresholds;
- reversals and credit notes;
- missing/dirty timestamps;
- incomplete cost-center coding;
- conflicting evidence between ERP workflow and transaction exports;
- model-generated unsupported evidence IDs;
- specialist overreach into domains lacking data;
- attempts to turn risk indicators into allegations of fraud.

## Human-review dataset

For research, maintain a labeled review table with:

- run ID;
- finding ID;
- specialist domain;
- AI conclusion;
- reviewer decision;
- reviewer rationale;
- evidence sufficiency;
- final severity;
- action taken;
- later validation result.

This creates a basis for calibration, error analysis, learning from overrides, and publication-quality evaluation.


## NAAIL / FRANKENSTEIN promotion boundary

Passing software tests establishes implementation quality only. Promotion to VALIDATED or EMPIRICAL_RESULT requires the broader FRANKENSTEIN/NAAIL evidence, reproducibility, adversarial review and Human Approval Gate requirements.
