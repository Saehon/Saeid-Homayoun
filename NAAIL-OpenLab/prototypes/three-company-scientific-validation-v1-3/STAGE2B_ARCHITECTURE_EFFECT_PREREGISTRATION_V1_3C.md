# NAAIL OpenLab™ — V1.3C Architecture-Effect Analysis Pre-Registration

**Date frozen:** 2026-09-17  
**Status:** `DESIGN_ONLY`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`  
**Gold_Key opened for scoring:** `NO`

## Research question

Does the **NAAIL governance architecture** improve the quality, grounding, contradiction handling, calibration, auditability and verification efficiency of professional accounting/auditing judgments when the underlying model, task and evidence are held constant?

## Experimental structure

Frozen architecture conditions:

- `A0` — Model + Frozen Evidence
- `A1` — Evidence Passport™
- `A2` — Full NAAIL Verify

Frozen robustness blocks:

- C01 OpenAI `gpt-6-astra`
- C02 Google `gemini-3.8-flash`
- C03 Anthropic `claude-fable-5`

Frozen benchmark:

- 21 tasks;
- 3 companies: MSFT, WMT, JPM;
- 7 professional domains;
- same task/evidence packet within each provider-condition cell;
- planned outputs: `3 providers × 3 conditions × 21 tasks = 189`.

## Primary estimand

For provider `p` and task `t`:

`D_pt = OPQS(A2,p,t) − OPQS(A0,p,t)`

Primary architecture effect:

`Δ_NAAIL = mean(D_pt)` across the 63 provider-task pairs.

## Secondary estimands

1. `Δ_EvidencePassport = mean[OPQS(A1) − OPQS(A0)]`
2. `Δ_VerificationIncrement = mean[OPQS(A2) − OPQS(A1)]`
3. architecture-condition differences in each raw 0–4 rubric dimension;
4. verification minutes, rework minutes, escalation and final verified-output rates;
5. provider/company/domain heterogeneity as robustness evidence only.

## Primary outcome

`Overall Professional Quality Score (OPQS)`, 0–100, from the frozen blinded rubric.

Weights:

- professional correctness: 35%;
- evidence grounding: 20%;
- contradiction handling: 15%;
- calibration/evidence sufficiency: 10%;
- auditability/traceability: 10%;
- professional decision usefulness: 10%.

## Primary practical-effect threshold

A practically meaningful architecture effect requires:

`mean[A2 − A0] ≥ +5.0 OPQS points`.

This threshold is frozen before scoring and will not be changed after observing results.

## Primary inference

The principal analysis preserves provider-task pairing.

1. Compute `D_pt = A2 − A0` for each of the 63 provider-task pairs.
2. Estimate the mean paired difference.
3. Construct a **task-cluster bootstrap 95% confidence interval** by resampling the 21 task IDs with replacement and retaining all provider observations within each sampled task.
4. Use `10,000` bootstrap replications with fixed seed `20260917`.
5. Report the unstandardized mean difference in OPQS points as the primary effect size.

No architecture claim will be based solely on whether the interval excludes zero.

## Secondary inference

- Repeat the paired analysis for A1−A0 and A2−A1.
- Report dimension-level paired mean differences on the original 0–4 scale.
- Report provider-, company- and domain-stratified effects descriptively with uncertainty intervals; do not rank providers.
- As a robustness model, estimate a repeated-observation regression/mixed specification with condition indicators and provider fixed effects, with task-level dependence explicitly accounted for. This model is secondary to the paired estimand.

## Multiple comparisons

The only primary confirmatory contrast is **A2 vs A0 on OPQS**.

A1−A0, A2−A1 and dimension-level analyses are secondary. Their p-values, if reported, will be adjusted within their family using Holm correction. Practical effect sizes and confidence intervals remain primary interpretive evidence.

## Missingness and failure handling

- Provider/API/system failure is preserved as `FAILED_CALL` and is **not imputed** as a professional-quality score.
- Failure rates are reported by condition/provider.
- Model-generated refusal is a substantive response and is scored normally.
- If missing system failures are conditionally imbalanced, complete-case quality estimates must be accompanied by a failure-rate sensitivity discussion.
- No failed, null, contradictory or unfavorable output may be deleted because it weakens the architecture effect.

## Reviewer and blinding plan

- Minimum 2 independent blinded professional reviewers per output.
- Reviewers are masked to provider, architecture condition, other responses and aggregate results.
- Responses receive opaque IDs and randomized review order.
- Adjudication is triggered when OPQS disagreement exceeds 10 points or any dimension differs by at least 2 raw scale points.
- Reliability statistics are calculated before architecture labels are unblinded.

## Promotion decision framework

A2 will not be treated as supported merely because the mean difference is positive or statistically significant.

For `SUPPORTED_AFTER_CHALLENGE`, all of the following are required:

1. mean A2−A0 OPQS improvement ≥ +5.0 points;
2. no material deterioration (>0.20 raw points) in evidence grounding, contradiction handling or calibration;
3. positive mean A2−A0 effect in at least 2 of 3 providers;
4. positive mean A2−A0 effect in at least 2 of 3 companies;
5. no hidden material-error increase;
6. prospective human verification evidence available;
7. reviewer reliability and adjudication results acceptable and disclosed.

Otherwise classify the finding using the controlled vocabulary, including `REVISED_AFTER_CHALLENGE`, `REQUEST_MORE_EVIDENCE`, `REJECTED_BY_FALSIFICATION`, or `BLOCKED` as appropriate.

## CVPO integration

After quality scoring and prospective human review, calculate:

`CVPO = (model/API cost + human verification cost + rework cost) / verified correct professional outputs`

Numeric CVPO remains `NOT_EXECUTED` until real prospective telemetry exists.

## Prohibited post-hoc practices

- changing score weights after observing architecture effects;
- changing the +5 practical threshold after scoring;
- excluding difficult tasks or negative provider/company/domain results without a pre-existing failure rule;
- selecting only the strongest provider as evidence of architecture success;
- promoting a secondary subgroup finding over a null primary contrast;
- treating statistical significance as scientific closure.

## Scientific boundary

This document pre-registers the V1.3C analysis logic. It does not execute any model, score any response, open the Gold_Key, simulate human review, or promote Stage 2C.
