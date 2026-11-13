# B6 Pilot Comparison Protocol V1

Status: **FROZEN BEFORE DATA; DRAFT PENDING CLAUDE AND HUMAN REVIEW**.

This protocol defines a later single pilot comparison of the frozen NAAIL system, blinded human evaluation coders, and a deterministic always-no-error baseline. It contains no benchmark probes, case candidates, evaluation data, ground-truth labels, predictions, scores, or scientific claims.

## Design

The same frozen item identifiers and hidden ground truth are used for all arms. Results are reported separately for the independently authored sealed Benchmark V3 holdout and for predefined assessment units from real Cases 001–003. The two strata are never pooled into one headline result.

The simple baseline always predicts `NO_ERROR` and an empty taxonomy set. It has no parameters and cannot use corpus statistics, labels, detector outputs, or post-unseal choices.

Human evaluation coders must be blinded to ground truth and system outputs. Their unadjudicated outputs are scored separately. The adjudicated ground truth is not treated as a comparison arm. Any overlap between evaluation coding and ground-truth coding or adjudication must be disclosed and prevents an independence claim.

## Frozen metrics

For every arm and stratum, report raw `TP`, `FP`, `FN`, `TN`, and `N`, then precision, recall, and F1. The frozen zero-denominator value is `0.0`. Taxonomy-label micro and macro metrics, exact-set matches, abstentions, missing outputs, and item-level disagreements are secondary outputs. Pairwise deltas, exact McNemar tests, and a paired item bootstrap are descriptive pilot evidence, not automatic gates.

## One authoritative run

All versions, inputs, ground truth, instructions, code, environment, exposure declarations, and approvals must be hashed in a pre-run manifest. After arm outputs are sealed, the scoring entry point may be invoked exactly once. Success cannot be rerun, and failure cannot be replaced. Any later repair requires a prospectively frozen new protocol version plus Claude and human authorization, while the original failed run remains preserved.

## Execution boundary

Execution remains prohibited until human POC approval; Claude approval of B4, B5, and B6; an approved frozen B5 ground-truth process; independently authored sealed B4 holdout inputs; human-selected and frozen real cases; and a complete pre-run manifest.

Benchmark V2 remains development evidence and its limitation—8 of 9 realistic evasion probes missed—must remain visible.

`POC_COMPLETE = FALSE`; `V1_COMPLETE = FALSE`.
