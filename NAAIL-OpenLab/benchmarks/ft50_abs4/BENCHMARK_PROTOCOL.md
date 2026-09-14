# NAAIL Scientific Replication Arena™ — Benchmark Protocol

## Objective
Evaluate published FT50 / AJG 4* research workflows against NAAIL OpenLab™ standards without treating publication status as proof that a method is universally valid.

## Stage 0 — Rights, provenance, and source freeze
- verify repository owner and publication linkage;
- inspect code/data licenses;
- identify restricted, confidential, WRDS, CRSP, Compustat, Audit Analytics, IBES, or other licensed inputs;
- record the exact Git commit SHA before execution;
- record software versions and environment lockfiles;
- do not copy or redistribute data/code beyond applicable rights.

## Stage 1 — Original-result replication
Attempt to reproduce the paper's reported tables, figures, coefficients, diagnostics, and logs using the authors' documented workflow.

Minimum outputs:
- expected vs reproduced statistic;
- absolute and relative difference;
- pass/fail tolerance;
- missing input/dependency report;
- runtime and environment metadata.

## Stage 2 — Independent reproduction
Reimplement the empirical logic independently where feasible. The objective is to distinguish scientific reproducibility from dependence on a specific codebase.

## Stage 3 — Specification robustness
Where substantively appropriate, test:
- alternative control sets;
- alternative fixed effects;
- clustering choices;
- winsorization/outlier rules;
- alternative variable construction;
- sample restrictions;
- alternative functional forms;
- alternative estimators.

Never select a preferred model solely because it yields a lower p-value.

## Stage 4 — Causal verification
For causal claims, where appropriate run:
- placebo outcomes/treatments;
- pre-trend checks;
- alternative event-study estimators;
- staggered-treatment diagnostics;
- sensitivity analysis;
- negative controls;
- falsification tests;
- synthetic or doubly robust alternatives where justified.

Prediction quality must not be interpreted as causal validity.

## Stage 5 — ML / AI verification
For predictive or AI studies, where appropriate run:
- leakage audit;
- train/validation/test separation;
- temporal holdout;
- industry/entity holdout;
- baseline comparison;
- calibration;
- distribution shift;
- seed sensitivity;
- feature-ablation tests;
- model-family comparison;
- cost/latency reporting.

## Stage 6 — Adversarial Critic–Defender review
A Critic attempts to invalidate the result; a Defender may respond only with evidence, code, diagnostics, or theory. Unsupported rhetorical defense is not accepted.

## Stage 7 — Cross-dataset / Digital Twin validation
When rights permit, test the method on a second dataset. Where ground truth is unavailable, use a controlled NAAIL Digital Twin scenario to evaluate false positives, false negatives, identification failure, leakage, and inference stability.

## Stage 8 — NAAIL benchmark metrics
Each run should report, where applicable:
- Replication Fidelity;
- Reproducibility;
- Specification Stability;
- Causal Robustness;
- Temporal/OOS Stability;
- Cross-Dataset Generalization;
- Falsification Survival;
- Evidence Traceability;
- Data/License Compliance;
- runtime/cost;
- human override and reason.

For audit/accounting applications also report the NAAIL professional metrics:
- RPA — Risk–Procedure Alignment;
- AA — Assertion Alignment;
- EG — Evidence Grounding;
- PS — Professional Skepticism;
- DS — Documentation Sufficiency;
- DIST — Decision/Inference Stability.

## Stage 9 — Chain-of-Evidence
Preserve:
Question → Theory → Literature → Repository/Commit → Data Rights → Data → Transformations → Model → Identification → Result → Robustness → Falsification → Replication → Interpretation → Human Decision.

## Stage 10 — Human Gate
No benchmark result is labeled "validated", "reproduced", or "scientifically supported" without explicit human review. Failures are retained as evidence and must not be silently deleted.

## Release classes
- **GREEN** — reproduced and survives required critical tests;
- **AMBER** — partially reproduced or important caveats remain;
- **RED** — material replication, identification, leakage, provenance, or rights failure;
- **BLOCKED** — required data/software/rights unavailable; no scientific conclusion drawn.
