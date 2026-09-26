# IFRS-CPJ Management Science Study

## Purpose

This study operationalizes the **Computational Professional Judgment (CPJ)** research program for a Management Science-style experiment.

### Main hypothesis

> **H1 — Independent AI Challenge Hypothesis.** In judgment-intensive IFRS tasks, an accounting decision produced through an independent AI challenger, evidence verification, deterministic recalculation, and a human professional gate will have a lower material-error rate and higher evidence-grounded decision quality than a decision produced by a single AI or by an AI that reviews its own answer.

### Core moderator

> **H2.** The benefit of independent AI challenge increases as IFRS judgment complexity, ambiguity, and estimation uncertainty increase.

## Experimental arms

| Arm | Architecture | Role |
|---|---|---|
| T0 | Human only | Human baseline |
| T1 | Single AI | AI baseline |
| T2 | Human + AI | Conventional human-AI collaboration |
| T3 | AI + self-review | Tests self-review |
| T4 | AI + blind independent challenger | Tests independence |
| T5 | Generator + challenger + evidence + deterministic calculator | Structured verification |
| T6 | T5 + human professional gate | Full CPJ architecture |

## Data strategy

Primary IFRS case construction should use European ESEF filings, ESMA enforcement/educational materials, and IFRS 20-F issuers. Kaggle datasets are supplementary and should not be treated as the main IFRS benchmark.

## Repository layout

- `SOURCE_REGISTRY.md` — human-readable upstream and dataset registry.
- `source_registry.json` — machine-readable registry.
- `FORK_AND_LICENSE_PLAN.md` — fork/reuse boundaries and clean-room policy.

## Planned case benchmark

Target first benchmark: **300 cases**.

- ~100 authoritative/regulatory cases
- ~150 real-company IFRS filing cases
- ~50 adversarial/perturbed cases

Each case should contain source provenance, IFRS standard, facts, evidence, complexity, gold-standard conclusion, expert coding, treatment assignment, and outcome measures.

## Reproducibility principle

Do not treat upstream repositories as proprietary Mirendal code. Preserve source attribution and licenses. Where licensing or product-boundary questions exist, reproduce the methodology through independent clean-room adapters and maintain provenance records.
