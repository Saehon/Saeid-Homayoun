# P0.1 — Frozen Research Question and JFE Contribution

Version: 1.0  
Freeze date: 2026-10-04  
Gate: P0.1  
Status: PASS (design freeze only; no empirical result or novelty finding is claimed)

## Primary research question

> When independently executed, versioned large language models receive the same time-stamped financial evidence, does cross-model disagreement contain incremental, out-of-sample information about prespecified future financial outcomes beyond the mean model judgment, evidence quality, and conventional predictors?

## Unit of analysis and timing

- Unit: firm-information-event-model judgment.
- Information set: an identical evidence packet available as of event time `t`.
- Treatment-like construct: cross-model disagreement measured only from actual logged model outputs.
- Comparison: mean AI judgment (`AIConsensus`) plus conventional predictors and fixed effects appropriate to the outcome.
- Outcomes: realized strictly after the evidence cutoff. The primary outcome and horizon will be preregistered before sealed-test access; market, information, reporting, audit, and enforcement outcomes remain separate families.

## Primary estimand

The primary quantity is the incremental predictive contribution of disagreement:

`Y_i,t+1 = alpha + beta1 AIConsensus_it + beta2 AID_it + gamma X_it + FE + error_it`

The core test concerns `beta2` and the out-of-sample change in prespecified scoring metrics when `AID` is added to a benchmark containing `AIConsensus`, evidence quality, and conventional controls. This is initially a predictive design. Causal language is prohibited unless a later identification design independently supports it.

## Proposed JFE contribution

1. **Controlled information-processing disagreement.** The design holds the evidence packet fixed while varying the model, separating disagreement in information processing from disagreement caused by different information sets.
2. **Financial-information construct.** It develops AI Disagreement (AID) as a preregistered family of dispersion and pair-topology measures, evaluated incrementally to AI consensus rather than as a standalone model score.
3. **Chronology and evidence governance.** It couples the construct to evidence passports, model/version logs, temporal firewalls, raw-output preservation, falsification, and human escalation.
4. **Economic validation.** It tests whether AID improves genuine held-out prediction and decision utility for financial-market and reporting-risk outcomes, with outcome families and multiplicity handled explicitly.

These are proposed contributions. Originality relative to the complete literature is not declared PASS until P2.1–P2.5 are completed.

## Falsifiable null and success boundary

- Null: conditional on consensus and benchmarks, AID adds no reproducible held-out information or economic utility.
- A null or adverse result is scientifically valid and must not be relabeled as engineering failure.
- Statistical significance alone is insufficient; calibration, held-out predictive increment, economic magnitude, and robustness must be reported.
- AID cannot be selected, mutated, or tuned using validation or sealed-test outcomes.

## Scientific boundaries

- The Microsoft FY2026 POC is a transparent workflow demonstration, not evidence for the main claim.
- Illustrative risk scores are not model runs, audit opinions, or investment recommendations.
- GPT, Claude, Gemini, Llama, or Chrono outputs count only when actually executed and logged with model/version/protocol metadata.
- “AlphaFold-inspired,” “AlphaEvolve-inspired,” “Co-Scientist,” and “100-CEO board” denote design principles or structured review roles; they are not claims that those systems or 100 independent agents were run.
- Restricted/proprietary inputs stay outside public GitHub; public records use hashes, schemas, acquisition instructions, or synthetic substitutes.
- Human approval remains required for governance decisions and any merge to protected `main`.

## Change control

Changes to the frozen question require a versioned amendment containing rationale, affected hypotheses/gates, whether any development/validation/test outcomes were seen, and human approval. The prior version remains preserved. No change may be motivated by sealed-test performance.

## Gate decision

P0.1 is PASS because the question, estimand, proposed contribution, falsifiable null, timing rule, and scientific boundaries are explicit and versioned. This PASS certifies the research-design freeze only; it does not certify novelty, data availability, model execution, hypothesis support, or JFE suitability.
