# NAAIL OpenLab™ — V1.3C Blinded Professional Scoring Rubric

**Date frozen:** 2026-09-17  
**Design status:** `DESIGN_ONLY`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`  
**Gold_Key opened for scoring:** `NO`  
**Architecture:** exactly **Stable Knowledge Core™ + Replaceable Technology Core™**

## Purpose

This rubric evaluates whether the **NAAIL governance architecture** improves professional accounting/auditing judgment when the underlying model, task and frozen evidence are held constant.

The primary comparison is:

`A2 Full NAAIL Verify − A0 Model + Frozen Evidence`

`A1 Evidence Passport™` is retained to decompose the architecture effect.

Provider identity is not the scientific outcome. Providers are robustness blocks.

## Blinding rules

Reviewers must not be shown:

- architecture condition (`A0`, `A1`, `A2`);
- provider/model identity;
- other candidate responses;
- previous reviewer scores;
- aggregate results.

Reviewers may use only:

1. the benchmark task;
2. the frozen evidence supplied to that task;
3. the frozen private Gold_Key / reference rubric after all responses are frozen;
4. the response being scored.

Every scored output receives an opaque review ID.

## Primary quality score — 100 points

Each dimension is first rated on a **0–4 anchored scale**. The weighted composite is then calculated.

| Dimension | Weight | 0 | 1 | 2 | 3 | 4 |
|---|---:|---|---|---|---|---|
| Professional correctness | 35% | materially wrong / unsafe conclusion | major errors | partially correct with important omissions | substantially correct with minor limitations | fully correct within available evidence |
| Evidence grounding | 20% | unsupported / contradicts evidence | weak linkage | mixed grounding | clear evidence linkage | complete, traceable and appropriately bounded grounding |
| Contradiction handling | 15% | ignores/reverses contradiction | notices poorly | partial treatment | correctly identifies and preserves conflict | explicitly resolves what can be resolved and preserves unresolved conflict |
| Calibration / evidence sufficiency | 10% | unjustified certainty | overconfident | mixed calibration | appropriate confidence/qualification | correctly uses `REQUEST_MORE_EVIDENCE` or bounded conclusion when needed |
| Auditability / traceability | 10% | no reconstructable path | largely opaque | partly reconstructable | clear judgment path | reviewer can reproduce evidence→judgment path |
| Professional decision usefulness | 10% | unusable/misleading | weak | usable with substantial revision | professionally useful with minor revision | concise, decision-relevant and professionally usable |

### Composite formula

For dimension score `d ∈ {0,1,2,3,4}`:

`Weighted points = (d / 4) × dimension weight`

`Overall Professional Quality Score (OPQS) = sum(weighted points)`

Range: `0–100`.

## Separate verification-effort measures

These measures are **not included in OPQS** and must be retained separately for CVPO and practical-use evaluation:

- reviewer verification minutes;
- number of corrections required;
- rework minutes;
- final verified output (`TRUE/FALSE`);
- escalation required (`TRUE/FALSE`);
- material error remaining after review (`TRUE/FALSE`).

## Failure and refusal rules

- **API/system failure:** not scored as a professional answer; preserve as `FAILED_CALL`, do not impute a quality score, and report failure frequency separately.
- **Model refusal:** score normally. A refusal may be appropriate if evidence is insufficient and may therefore earn a high calibration/correctness score.
- **Empty/irrelevant answer:** score on the rubric; do not convert it into a system failure unless the provider actually failed.
- **Contradictory evidence:** never reward forced certainty merely because a definitive answer was produced.
- **Null/negative architecture effect:** preserve and report; do not reclassify as implementation noise without documented evidence.

## Reviewer design

- Minimum: **2 independent blinded professional reviewers per output**.
- Reviewer order randomized independently.
- If absolute reviewer disagreement on OPQS is **>10 points**, or any dimension differs by **≥2 scale points**, trigger adjudication by a third reviewer.
- Primary scored value: mean of the two original reviewers when no adjudication is triggered; otherwise the adjudicated consensus value.
- Report inter-rater reliability before architecture labels are unblinded.

Planned reliability outputs:

- ICC for OPQS;
- weighted agreement/kappa by ordinal dimension where feasible;
- adjudication rate.

## Architecture-effect success guardrails

NAAIL architecture is **not** promoted from p-values alone.

The pre-specified practical threshold for the primary comparison is:

`Mean OPQS(A2 − A0) ≥ +5.0 points on the 0–100 scale`

Additional guardrails:

1. mean evidence-grounding score must not decline by more than `0.20` on the raw 0–4 scale;
2. mean contradiction-handling score must not decline by more than `0.20`;
3. mean calibration score must not decline by more than `0.20`;
4. the A2−A0 mean effect must be positive in at least **2 of 3 providers** and at least **2 of 3 companies**;
5. no material increase in unresolved professional errors may be hidden by a higher composite score;
6. human verification evidence is required before any professional-performance promotion claim.

These are promotion guardrails, not a mechanism for declaring a provider winner.

## Anti-overclaim rules

- Fluency ≠ correctness.
- Longer explanation ≠ auditability.
- Lower refusal rate ≠ better calibration.
- Agent agreement ≠ verification.
- Statistical significance ≠ scientific discovery.
- Lower cost ≠ superior professional output if verification quality declines.
- A positive result for one provider/company/domain ≠ general architecture validation.

## Status boundary

This rubric is frozen **before** main output generation and before the Gold_Key is opened for scoring. No V1.3C output has been scored by this document.
