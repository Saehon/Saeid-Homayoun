# P3.1 Competing Hypotheses and Mechanisms

Version: 1.0  
Gate: P3.1 — Generate competing hypotheses and mechanisms  
Construction date: 2026-10-08  
Status: FROZEN CANDIDATE PORTFOLIO — NOT TESTED OR RANKED

## Scope and scientific status

This artifact converts the eight P2.5 handoff families into a balanced portfolio of
positive, rival and null/adverse hypotheses. It is a design artifact, not an empirical
result. Every hypothesis is `CANDIDATE_NOT_TESTED`; no model was run, no package was
executed, no data outcome was inspected, and no hypothesis was ranked.

P3.1 passes only if each family has genuinely competing explanations, an observable
implication, a rejection condition, a negative control, an admissible partition and a
dependency path. Later P3 gates may criticize, falsify and rank the portfolio, but may
not use validation or sealed-test outcomes to generate or improve candidates.

## Common notation and constraints

- **AID:** frozen future AI-disagreement construct; candidate definitions remain
  downstream and cannot be selected here.
- **Consensus:** central tendency of model judgments under one frozen evidence packet.
- **Within-model variance:** repeated-run variation holding model, prompt and evidence
  fixed; it must be separated from cross-model dispersion.
- **Evidence quality:** pre-outcome score for authority, completeness, provenance,
  timeliness and internal consistency.
- **Materiality:** pre-outcome economic significance under a frozen rubric.
- **Admissible partition:** DEVELOPMENT for design and diagnostic estimation;
  VALIDATION only after the relevant specification freeze; SEALED TEST only after
  human approval and never for candidate evolution.
- The RFS integrity-hold record remains `STOP_RELIANCE` and cannot support a positive
  hypothesis, ranking or benchmark claim.

## Portfolio overview

| Family | Positive mechanism | Rival mechanism | Null/adverse mechanism | Primary downstream exposure |
|---|---|---|---|---|
| F1 Incremental information | Cross-model feature diversity | Run/prompt artifact | No incremental information | Information and market outcomes |
| F2 Common error | Low AID reflects clarity | Shared-data/model herding | Consensus is jointly wrong | Calibration and error correlation |
| F3 Market response | Underreaction to ambiguous evidence | Risk compensation | Microstructure/chance | Returns, CAR, volatility |
| F4 Reporting risk | Early inconsistent-reporting signal | Distress/complexity | Auditor/selection artifact | ICFR, restatement, CAM/KAM |
| F5 Evidence quality | Weak evidence exposes useful heterogeneity | Severity/length confounding | Quality score endogeneity | Evidence interactions |
| F6 Human review | Targeted complementarity | Reviewer anchoring/hindsight | Cost exceeds error reduction | Review error, cost and routing |
| F7 Representation | Pair structure improves generalization | Transparent summaries suffice | Complexity overfits | Construct validity and OOS stability |
| F8 Distribution | Aggregate decision benefit | Concentrated subgroup harm | No usable benefit | Group calibration and consequences |

## F1 — Incremental information versus artifact/noise

| ID | Candidate hypothesis and mechanism | Observable implication | Rejection condition | Negative control | Partition / dependencies | State |
|---|---|---|---|---|---|---|
| H1A | **Information diversity.** Holding evidence, rubric and consensus fixed, cross-model dispersion reflects heterogeneous extraction of economically relevant features. | AID improves pre-specified calibration or prediction beyond consensus and evidence quality; signal survives subtraction of within-model variance. | Reject if incremental effect is unstable, economically negligible, or disappears after run-noise adjustment and multiplicity control. | Shuffled model identities and irrelevant-text packets should not produce the same increment. | DEVELOPMENT then frozen VALIDATION/SEALED TEST; P4 chronology benchmark, P5 passport/partitions, P6 repeated runs. | CANDIDATE_NOT_TESTED |
| H1B | **Protocol artifact.** Apparent AID is mainly prompt order, decoding, context-window or provider-version variation rather than economic information. | Within-model and protocol perturbations explain most measured dispersion; packet-level AID is not stable across frozen reruns. | Reject if cross-model variance remains dominant and stable under deterministic settings and protocol controls. | Semantically equivalent prompt permutations and duplicated model endpoints. | DEVELOPMENT diagnostics; P4.4, P5.4, P6.1–P6.4. | CANDIDATE_NOT_TESTED |
| H1N | **No incremental value.** Conditional on consensus, conventional features and evidence quality, AID adds no reliable OOS information. | Consensus-plus-AID does not beat the frozen consensus-only benchmark under calibration, loss and economic-value criteria. | Reject only after pre-specified OOS improvement survives multiple-testing and cost thresholds. | Random pseudo-AID matched on distribution and missingness. | Frozen benchmark; VALIDATION then SEALED TEST; P5.5, P7/P8 freeze. | CANDIDATE_NOT_TESTED |

## F2 — Clarity versus correlated common error

| ID | Candidate hypothesis and mechanism | Observable implication | Rejection condition | Negative control | Partition / dependencies | State |
|---|---|---|---|---|---|---|
| H2A | **Genuine clarity.** Low AID indicates that evidence has a clear, consistently recoverable economic meaning. | Low-AID packets show better calibration and lower realized error against independently constructed labels. | Reject if low AID does not improve accuracy/calibration or fails on independent evidence. | Obvious factual packets and deliberately ambiguous matched packets. | DEVELOPMENT labels; independent VALIDATION; P5 evidence labels, P6 outputs. | CANDIDATE_NOT_TESTED |
| H2B | **Model herding.** Low AID reflects shared training data, priors or reasoning shortcuts rather than clarity. | Pairwise errors are positively correlated across model families, especially on shared-source or canonical narratives. | Reject if error correlation vanishes across independent model families and evidence sources. | Synthetic packets with planted but noncanonical corrections. | DEVELOPMENT; model-family registry and provenance required; P6.2, P7.1. | CANDIDATE_NOT_TESTED |
| H2C | **Confident common error.** Low AID and high apparent confidence can identify the most dangerous joint mistakes. | Some low-AID/high-confidence strata have worse externally verified calibration than moderate-AID strata. | Reject if calibration is monotone improving as AID falls after stable stratification and sample-size control. | Counterfactual packets that reverse a familiar fact while preserving style. | DEVELOPMENT discovery only, then frozen stratum test; P5.4, P6, P7.3. | CANDIDATE_NOT_TESTED |

## F3 — Market underreaction versus risk compensation/microstructure

| ID | Candidate hypothesis and mechanism | Observable implication | Rejection condition | Negative control | Partition / dependencies | State |
|---|---|---|---|---|---|---|
| H3A | **Underreaction.** High AID marks disclosures whose implications are incorporated slowly into prices. | Pre-specified post-event drift or delayed CAR varies with AID after consensus, evidence quality and standard controls. | Reject if effects are absent, reverse, confined to tuned windows, or eliminated by transaction costs and multiple-testing control. | Placebo event dates and pre-event pseudo-outcomes. | Frozen event timing; VALIDATION/SEALED TEST; P5.1–P5.2, P6–P8. | CANDIDATE_NOT_TESTED |
| H3B | **Risk compensation.** Any AID-return relation reflects priced uncertainty rather than mispricing. | Higher expected returns coincide with persistent risk/volatility exposures and no abnormal performance after factor/risk adjustment. | Reject if abnormal drift remains under frozen risk models and does not load on pre-specified risk proxies. | Matched non-event windows with similar volatility and liquidity. | DEVELOPMENT model selection before validation; P5.2 and chronology controls. | CANDIDATE_NOT_TESTED |
| H3N | **Microstructure/chance.** Apparent market effects arise from liquidity, bid–ask bounce, news clustering or data mining. | Effects concentrate in illiquid firms, disappear under robust return construction, or fail untouched horizons. | Reject only if results survive liquidity filters, alternate return sources, placebo windows and multiplicity correction. | Randomized timestamps preserving firm/event frequency. | VALIDATION/SEALED TEST after full timing freeze; P4.4, P5.2, P5.5. | CANDIDATE_NOT_TESTED |

## F4 — Reporting-risk signal versus distress/auditor selection

| ID | Candidate hypothesis and mechanism | Observable implication | Rejection condition | Negative control | Partition / dependencies | State |
|---|---|---|---|---|---|---|
| H4A | **Reporting inconsistency precursor.** AID captures conflicting or weak reporting cues before later ICFR, restatement or CAM/KAM outcomes. | Lagged AID adds reporting-outcome discrimination beyond consensus and pre-event controls. | Reject if timing is not prospective, construct validity is weak, or incremental performance fails OOS. | Future-unrelated operational outcomes and post-outcome evidence exclusion. | DEVELOPMENT then frozen OOS; P5.1/P5.3, P6–P8. | CANDIDATE_NOT_TESTED |
| H4B | **Distress/complexity confounding.** AID is a proxy for firm distress, verbosity, complexity or industry conditions. | The relation weakens materially after matched design, firm/time effects and pre-specified distress/complexity controls. | Reject if stable incremental evidence remains across matched and within-firm analyses. | Equally long complex disclosures unrelated to financial reporting controls. | DEVELOPMENT matching specification; P5.2–P5.3. | CANDIDATE_NOT_TESTED |
| H4C | **Auditor/selection mechanism.** Auditor choice, engagement risk or disclosure practices jointly determine AID and later reporting labels. | Effects cluster by auditor/engagement traits and attenuate with auditor or firm fixed effects and selection diagnostics. | Reject if results generalize across auditor strata and survive pre-specified selection sensitivity. | Auditor changes without reporting events and reporting events without auditor changes. | DEVELOPMENT; requires auditor/event mapping in P5.3. | CANDIDATE_NOT_TESTED |

## F5 — Evidence-quality moderation versus endogenous scoring

| ID | Candidate hypothesis and mechanism | Observable implication | Rejection condition | Negative control | Partition / dependencies | State |
|---|---|---|---|---|---|---|
| H5A | **Useful quality moderation.** Weak, incomplete or conflicting evidence amplifies informative cross-model heterogeneity. | A frozen evidence-quality × AID interaction predicts correction/resolution beyond main effects. | Reject if interaction is unstable, lacks construct validity or is driven by a single quality component. | Deliberately degraded packets with known omissions and matched clean packets. | Rubric created on DEVELOPMENT without outcomes; P5.4 then frozen test. | CANDIDATE_NOT_TESTED |
| H5B | **Severity/length proxy.** The interaction reflects negativity, materiality, document length or rare topics. | Quality moderation attenuates after matched severity, length, event type and rarity controls. | Reject if it remains stable in equal-length/equal-materiality matched packets. | Neutral long documents and short severe disclosures. | DEVELOPMENT matching only; P5 evidence metadata. | CANDIDATE_NOT_TESTED |
| H5N | **Endogenous quality score.** Reviewer or model judgments of quality encode anticipated outcomes, invalidating the moderation claim. | Scores change when raters see outcome-adjacent information or show poor blind inter-rater reliability. | Reject if blind pre-outcome scoring is reliable, invariant to ordering and predictive only prospectively. | Outcome-label permutations and blinded source-order swaps. | DEVELOPMENT rubric audit; human approval before validation; P5.4. | CANDIDATE_NOT_TESTED |

## F6 — Human complementarity versus reviewer bias/cost

| ID | Candidate hypothesis and mechanism | Observable implication | Rejection condition | Negative control | Partition / dependencies | State |
|---|---|---|---|---|---|---|
| H6A | **Targeted complementarity.** Blind human review adds greatest value for high-AID, high-materiality, low-quality evidence cases. | Pre-specified routing reduces error or loss relative to AI-only and review-all policies at acceptable cost. | Reject if benefit is unstable, below cost threshold or absent under intent-to-review analysis. | Random routing and low-AID routing with equal reviewer capacity. | DEVELOPMENT threshold; frozen VALIDATION; human approval; P5.4, P6–P8. | CANDIDATE_NOT_TESTED |
| H6B | **Anchoring/hindsight.** Reviewers anchor on model outputs or outcome-adjacent facts and amplify rather than correct error. | Blinded independent ratings differ materially from model-visible or outcome-aware ratings; overrides lack prospective validity. | Reject if masked and model-visible reviews show comparable reliability and prospective error reduction. | Sham model rationale and reversed model-order displays. | DEVELOPMENT experiment; reviewer/time logs required. | CANDIDATE_NOT_TESTED |
| H6N | **No net value after cost.** Human review may reduce some errors but not enough to justify delay, inconsistency and labor cost. | Net utility of routed review is no better than frozen AI-only or simple rule-based escalation. | Reject only if benefit remains positive across pre-specified cost and error-severity ranges. | Review-all and simple materiality-only policies. | Frozen decision-utility function before validation; P5/P6. | CANDIDATE_NOT_TESTED |

## F7 — Pair representation versus transparent-baseline sufficiency

| ID | Candidate hypothesis and mechanism | Observable implication | Rejection condition | Negative control | Partition / dependencies | State |
|---|---|---|---|---|---|---|
| H7A | **Relational structure.** Model×model and evidence×model representations capture persistent disagreement structure missed by scalar summaries. | Frozen pair features improve construct stability and OOS performance beyond mean, SD, MAD and sign/rank baselines. | Reject if gains vanish under leave-one-model-family-out tests or fail complexity-adjusted validation. | Permuted pair identities preserving marginal score distributions. | DEVELOPMENT-only representation search; P6 panel, P7 freeze, P8 controls. | CANDIDATE_NOT_TESTED |
| H7B | **Baseline sufficiency.** Transparent dispersion and consensus summaries capture all reproducible signal. | Pair representations fail to improve calibration, stability or economic loss after complexity penalty. | Reject if a pre-frozen pair model delivers reproducible, economically material OOS improvement. | Equivalent-parameter linear expansions and shuffled-pair features. | DEVELOPMENT comparison then frozen validation; P7. | CANDIDATE_NOT_TESTED |
| H7C | **Complexity overfit.** Pair methods exploit development idiosyncrasies and model identity leakage. | Development gains decay sharply in temporal, firm or leave-one-model-out evaluation. | Reject if gains survive untouched validation and sealed tests without candidate recycling. | Random high-dimensional features with matched complexity. | Strict P0.3 firewall; P5.5, P7.4–P7.5, P8. | CANDIDATE_NOT_TESTED |

## F8 — Aggregate benefit versus distributional harm/null

| ID | Candidate hypothesis and mechanism | Observable implication | Rejection condition | Negative control | Partition / dependencies | State |
|---|---|---|---|---|---|---|
| H8A | **Broad decision benefit.** AID-aware decisions improve calibration or loss across pre-specified firm/event groups without material subgroup harm. | Aggregate and group-specific metrics improve with uncertainty bounds and minimum-cell safeguards. | Reject if improvement is absent, driven by one group, or accompanied by material pre-defined harm. | Group-label permutations and consensus-only policy. | Group definitions frozen on DEVELOPMENT; P5 schemas, later OOS. | CANDIDATE_NOT_TESTED |
| H8B | **Concentrated harm.** Aggregate gains mask worse errors or review burdens for small firms, sparse-coverage events or specific industries. | Some pre-specified groups show materially worse calibration, false-positive rates or routing costs despite aggregate gains. | Reject if hierarchical estimates exclude material harm across all pre-specified groups. | Random groups matched on size and base rate. | DEVELOPMENT diagnostics; multiplicity/hierarchical plan frozen before validation. | CANDIDATE_NOT_TESTED |
| H8N | **No usable benefit.** Heterogeneous and unstable group effects make the construct unsuitable for operational or external claims. | Signs/magnitudes vary across time, event types or model panels and fail transport tests. | Reject only after stable multi-period, multi-group OOS benefit under a frozen decision rule. | Temporal-block and leave-industry-out placebo transport tests. | VALIDATION/SEALED TEST after complete freezes; P5–P8. | CANDIDATE_NOT_TESTED |

## Dependency and exposure controls

| Control | Requirement |
|---|---|
| Chronology | No hypothesis may be tested without immutable evidence timestamps, model/version identity and leakage probes. |
| Construct validity | Predictive performance alone cannot validate AID; convergent, discriminant, calibration and stability evidence are required. |
| Repeated runs | Cross-model dispersion must be decomposed from within-model run variance. |
| Outcome timing | Every outcome must occur after the frozen evidence packet and judgment timestamp. |
| Baselines | Consensus-only, transparent dispersion, conventional-feature and relevant literature baselines must be frozen before evaluation. |
| Multiple testing | Families, horizons, metrics and subgroups require a pre-specified multiplicity policy. |
| Economic value | Statistical significance cannot substitute for calibration, cost or decision-value thresholds. |
| Sealed-test firewall | No candidate generation, threshold tuning, ranking or mutation may use sealed outcomes. |
| Integrity hold | LIT-RFS-002 remains adverse metadata under STOP_RELIANCE and cannot serve as positive evidence. |
| Human approval | Sealed access, material claim changes and external scientific claims remain human-controlled. |

## P3.2 critic handoff

The critic must attack all 24 candidates symmetrically across theory coherence,
identification, construct validity, measurement, chronology, selection, power,
multiplicity, transportability and reproducibility. It must not reward positive-sign
hypotheses by default and must preserve plausible nulls. P3.2 may recommend merge,
revision, quarantine or rejection, but no empirical rank is admissible at that gate.

## Structural falsification audit

| Check | Result |
|---|---|
| P2.5 handoff families represented | PASS — 8/8 |
| Positive, rival and null/adverse candidates present | PASS — 8 balanced triads |
| Candidate hypotheses uniquely identified | PASS — 24 |
| Rejection condition recorded | PASS — 24/24 |
| Negative control recorded | PASS — 24/24 |
| Partition and dependency path recorded | PASS — 24/24 |
| Candidate promoted to supported/ranked | PASS — none |
| Validation or sealed outcome used | PASS — none |
| Model/package/data execution claimed | PASS — none |
| Causal, novelty or publication-readiness claim made | PASS — none |

## Gate conclusion

P3.1 is PASS for generating and freezing a balanced, falsifiable candidate portfolio:
eight families, eight positive–rival–null/adverse triads and 24 untested hypotheses.
The PASS is for hypothesis-design completeness only. It does not establish construct
validity, empirical support, ranking, novelty, causality or decision value.

Next gate: P3.2 — conduct symmetric critic review of theory, identification and
measurement weaknesses before any hypothesis ranking or empirical testing.
