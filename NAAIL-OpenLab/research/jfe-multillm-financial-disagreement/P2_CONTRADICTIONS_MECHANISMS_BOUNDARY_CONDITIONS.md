# P2.4 Contradictions, Unresolved Mechanisms and Boundary Conditions

Version: 1.0  
Gate: P2.4 — Map contradictions, unresolved mechanisms and boundary conditions  
Construction date: 2026-10-08  
Status: FROZEN ANALYTICAL MAP — NO EMPIRICAL ADJUDICATION

## Scope and acceptance rule

This register interrogates the P2.1 verified literature, P2.2 replication-resource
inventory and P2.3 literature–evidence–construct graph. It distinguishes:

- **contradiction:** two claims, methods or evidence states that cannot be treated as
  interchangeable without an explicit reconciliation test;
- **unresolved mechanism:** a plausible channel not yet identified or rejected by
  this project;
- **boundary condition:** a context in which a relation may change sign, magnitude,
  interpretation or admissibility;
- **integrity constraint:** adverse evidence that limits reliance independent of
  whether a theoretical mechanism is plausible.

P2.4 passes only if each tension is traceable to existing graph nodes, has a stated
non-resolution, identifies a future falsification/adjudication test, and propagates
scientific limitations. A mapped contradiction is not evidence that either side is
true, and a proposed test is not an executed result.

## Contradiction register

| ID | Tension | Anchoring nodes | Why unresolved | Required adjudication / rejection test | Current disposition |
|---|---|---|---|---|---|
| CTR-01 | Predictive accuracy versus construct validity | LIT-JFE-002; LIT-RFS-001; LIT-RFS-003; CON-AID-SD; TST-CONSTRUCT-VALIDITY | A model may predict an outcome while measuring a different latent object; the seed studies do not validate multi-model disagreement. | Compare convergent, discriminant, calibration and human-coded validity before outcome prediction; reject the construct if it lacks stable semantic meaning. | OPEN |
| CTR-02 | Single-model signal versus multi-model disagreement | LIT-JFE-002; CON-AI-CONSENSUS; CON-AID-SD; CON-AID-PAIR | Single-model news predictability does not establish incremental information in cross-model dispersion. | Estimate frozen consensus-only versus consensus-plus-AID models OOS; require incremental calibration/economic evidence, not in-sample fit. | OPEN |
| CTR-03 | Historical model output versus current-model regeneration | LIT-MS-001; RES-MS-001-COMPANION; DAT-LLM-API-VERSION; CON-MODEL-DRIFT | Provider/model changes can make current outputs non-equivalent to historical outputs. | Pin model/version/date/settings; perform frozen reruns; classify exact versus procedural reproduction. | OPEN |
| CTR-04 | Open package versus full reproducibility | RES-JFE-002-V2; RES-JF-001-SYNTH; RES-RFS-003-SHORT; GOV-LICENSE-GATE | Public code may still depend on licensed data, paid APIs, short samples or unavailable historical versions. | File manifest, checksum, entitlement, environment and input audit before execution; synthetic/sample results cannot stand in for full estimates. | OPEN |
| CTR-05 | Aggregate performance versus distributional consequence | LIT-JF-001; MEC-ACCURACY-FAIRNESS; CON-DISTRIBUTIONAL-RISK | Higher average accuracy may coexist with unequal errors or welfare effects. | Pre-specify subgroup error/calibration/consequence tests and multiple-testing control; reject aggregate-benefit claims if harms are material. | OPEN |
| CTR-06 | Statistical prediction versus causal/economic mechanism | LIT-RFS-001; LIT-MS-002; MEC-NONLINEARITY; MEC-ECONOMIC-OBJECTIVE | Flexible models can predict without identifying why information maps to prices or reporting outcomes. | Separate predictive estimand from causal claims; use temporal ordering, negative controls and explicit identification assumptions. | OPEN |
| CTR-07 | Representation sophistication versus transparent benchmark | LIT-MS-002; MET-DEEP-ASSET-PRICING; CON-AID-PAIR | Complex representations may improve fit but raise fragility and interpretation costs. | Compare against mean, SD, MAD, sign/rank and linear baselines with complexity penalties on development data only. | OPEN |
| CTR-08 | Stable evidence packet versus evidence-quality heterogeneity | CON-EVIDENCE-QUALITY; MEC-INFO-PROCESSING; CON-MATERIALITY | Holding nominal evidence constant does not guarantee equal completeness, authority, ambiguity or materiality across events. | Score provenance/completeness/timeliness under a frozen rubric and test interactions without selecting evidence using outcomes. | OPEN |
| CTR-09 | Human review as safeguard versus human review as bias source | CON-HUMAN-OVERRIDE; MET-HUMAN-MACHINE; MEC-ACCURACY-FAIRNESS | Human intervention can correct machine errors but can also add anchoring, inconsistency or outcome-informed hindsight. | Blind, independently logged review with inter-rater reliability and override audit; compare pre/post-review errors on admissible data. | OPEN |
| CTR-10 | Textual/embedding validity versus transfer across tasks | LIT-RFS-003; LIT-MS-001; MEC-LANGUAGE-PERCEPTION | A validated sector-sentiment or textual task does not automatically validate firm-level risk judgments. | Task-specific labels, discriminant tests and error analysis; reject transfer if construct meaning or calibration changes materially. | OPEN |
| CTR-11 | Apparent chronology versus latent training leakage | LIT-JFE-002; CON-CHRONOLOGY-RISK; TST-CHRONOLOGY | Time-stamped prompts do not prove that a model lacked future information in training or retrieval. | Cutoff probes, future-information canaries, post-cutoff subsamples and chronology-safe comparators; quarantine contaminated tasks. | OPEN |
| CTR-12 | Reported benchmark versus unresolved integrity notice | LIT-RFS-002; RES-RFS-002-HOLD; ANM-RFS-002-EOC | A published result under active journal investigation cannot be treated as uncontested evidence. | Journal resolution or separately authorized independent audit; until then retain adverse node and STOP_RELIANCE. | QUARANTINED |

## Unresolved mechanism register

| ID | Candidate mechanism | Observable implication if operative | Rival explanation | Falsification design | Status |
|---|---|---|---|---|---|
| MEC-U01 | Information-processing heterogeneity: models extract different relevant features from identical evidence | AID predicts later information resolution conditional on consensus and evidence quality | Random sampling/decoding noise | Repeated deterministic/stochastic runs; subtract within-model variance from cross-model variation | CANDIDATE |
| MEC-U02 | Semantic ambiguity: evidence admits multiple economically plausible interpretations | AID rises with independently coded ambiguity and falls after clarifying disclosures | Prompt underspecification | Frozen prompt variants plus blind ambiguity labels; reject if prompt wording fully explains AID | CANDIDATE |
| MEC-U03 | Knowledge/capability heterogeneity across model families | Persistent pair-specific disagreement aligned with documented capability/domain differences | Version drift or context-window differences | Version-logged pair matrix, leave-one-model-out tests and capability-matched controls | CANDIDATE |
| MEC-U04 | Evidence-quality channel | Weak provenance/completeness increases disagreement and subsequent correction risk | Negative-event severity or length | Match/control materiality, length and event type; test pre-specified evidence-quality interactions | CANDIDATE |
| MEC-U05 | Complexity/materiality channel | AID is more informative for complex and economically material events | Mechanical verbosity or rare-topic effects | Control length/rarity; compare equally long low-complexity evidence; pre-freeze materiality rubric | CANDIDATE |
| MEC-U06 | Market underreaction | High AID identifies evidence whose implications are incorporated slowly | Risk compensation, microstructure or data mining | CAR/drift windows, factor controls, placebo dates, transaction-cost/economic-value checks | CANDIDATE |
| MEC-U07 | Reporting-risk precursor | AID detects internally inconsistent or weak reporting before later ICFR/restatement/CAM outcomes | Industry distress or auditor selection | Firm/time FE, lag discipline, negative-control outcomes and reporting-specific error analysis | CANDIDATE |
| MEC-U08 | Model-herding/common-data channel | Low disagreement can coexist with common error when models share training data or priors | Genuine clarity/consensus | Independent evidence benchmark and correlated-error analysis; do not equate low AID with correctness | CANDIDATE |
| MEC-U09 | Confidence-miscalibration channel | Disagreement weighted by calibrated confidence outperforms raw dispersion | Confidence verbosity/style | External calibration and reliability curves; reject self-reported confidence if uncalibrated | CANDIDATE |
| MEC-U10 | Human-complementarity channel | Review adds greatest value for high-AID/high-materiality cases | Selective escalation or reviewer hindsight | Frozen routing threshold, blinded review and intent-to-review evaluation | CANDIDATE |
| MEC-U11 | Distributional error channel | Aggregate gains mask concentrated errors across firm/event groups | Small subgroup noise | Minimum cell sizes, hierarchical shrinkage and pre-specified heterogeneity tests | CANDIDATE |
| MEC-U12 | Nonlinear representation channel | Pair/evidence representations improve stable OOS performance beyond transparent summaries | Overfit complexity | Development-only search, complexity penalties, validation freeze and sealed OOS comparison | CANDIDATE |

No candidate mechanism is promoted to SUPPORTED. Mechanism ranking belongs to P3 and
empirical adjudication belongs to later gated work.

## Boundary-condition map

| Family | Boundary states | Risk to interpretation | Required control |
|---|---|---|---|
| Time/chronology | Pre-cutoff; near-cutoff; post-cutoff; retrieved/current evidence | Future-information contamination or non-comparable model knowledge | Evidence timestamp, model cutoff/version, retrieval log, chronology probe |
| Model identity | Frontier proprietary; open-weight; finance-tuned; chronology-safe comparator | Shared training data, unequal capabilities, unavailable historical versions | Immutable model registry, family tags, leave-one-family-out analysis |
| Run protocol | Deterministic versus sampled; context window; prompt order; tool/retrieval use | AID may be run noise or protocol artifact | Frozen settings, repetitions, raw-output preservation |
| Evidence quality | Primary/secondary; complete/partial; verified/unverified; conflicting sources | Disagreement may measure input defects rather than economic uncertainty | Evidence Passport and frozen quality rubric |
| Event type | 10-K/10-Q; earnings/news; CAM/KAM; ICFR; enforcement | Construct semantics and outcome horizons differ | Event-specific prompts, labels, timing and separate validity checks |
| Outcome family | Returns/CAR/volatility; forecast error; reporting failure; enforcement | One outcome cannot validate all proposed meanings of AID | Family-specific estimands, metrics and multiplicity control |
| Firm context | Size; industry; complexity; loss/distress; coverage; AI intensity | Base rates, disclosure style and data availability vary | Stratified diagnostics, FE/controls, pre-specified heterogeneity |
| Market regime | Normal; crisis; high volatility; major technology shock | Model and market behavior may shift jointly | Time FE, regime indicators, temporal OOS and stability tests |
| Language/jurisdiction | English versus multilingual; US versus other regimes | Corpus, rules, disclosure and model capability differ | Initial US/English scope; explicit external-validation gate |
| Licensing/access | Public; restricted; synthetic; short sample; unknown license | Executability and reproducibility differ from scientific validity | Entitlement/license audit; no redistribution of restricted inputs |
| Human review | Blind versus outcome-aware; single versus multiple reviewer | Hindsight, anchoring and false consensus | Blind protocol, reviewer identity/time, inter-rater and override logs |
| Integrity status | Clean record; correction; concern; retraction/withdrawal | Reliance can become inadmissible after publication | Continuous notice register; quarantine propagation; claim re-audit |

## Cross-paper non-equivalence rules

1. **Prediction ≠ measurement validity.** Return, earnings or credit prediction cannot
   alone validate AI Disagreement.
2. **Code access ≠ data access.** A public repository does not remove upstream data,
   API, model or redistribution restrictions.
3. **Current execution ≠ historical replication.** A new provider model may permit
   procedural reconstruction but not exact reproduction.
4. **Low disagreement ≠ truth.** Shared training data or correlated errors can produce
   consensus that is jointly wrong.
5. **High disagreement ≠ risk.** It may reflect ambiguity, run noise, prompt defects,
   capability gaps or relevant uncertainty; mechanisms require separation.
6. **Model confidence ≠ calibrated probability.** Self-reported confidence requires
   external calibration.
7. **Human override ≠ ground truth.** Review must be blind, logged and evaluated.
8. **Association ≠ causality.** The baseline project is predictive unless later
   identification supports a bounded causal estimand.
9. **Journal publication ≠ uncontested evidence.** Corrections and integrity notices
   remain active graph dependencies.
10. **Engineering success ≠ scientific PASS.** Code execution cannot substitute for
    construct validity, chronology, OOS evidence or human approval.

## P3 design implications

The P3 tournament must generate genuinely competing hypotheses rather than variations
of a preferred positive result. At minimum it must include:

- information-value versus artifact/noise hypotheses;
- high-AID risk versus low-AID common-error hypotheses;
- market-underreaction versus risk-compensation/null explanations;
- reporting-risk signal versus distress/auditor-selection explanations;
- human-complementarity versus human-bias explanations;
- nonlinear-representation benefit versus transparent-baseline sufficiency;
- aggregate benefit versus distributional-harm/null hypotheses.

Every hypothesis must specify a rejection region, negative control, admissible data
partition and dependency path. P3 may rank candidates but cannot use validation or
sealed outcomes.

## Falsification and structural audit

| Check | Result |
|---|---|
| Contradictions trace to P2.1–P2.3 nodes | PASS — 12/12 |
| Unresolved mechanisms include observable implication, rival and falsification design | PASS — 12/12 |
| Boundary families include required control | PASS — 12/12 |
| Integrity hold remains explicit and quarantined | PASS — CTR-12 / ANM-RFS-002-EOC |
| Positive-only hypothesis framing permitted | PASS — prohibited |
| Low disagreement treated as correctness | PASS — prohibited |
| Public code treated as full reproducibility | PASS — prohibited |
| Historical/current model outputs treated as equivalent | PASS — prohibited |
| Planned adjudication test represented as executed | PASS — none |
| Model/package execution or empirical result claimed | PASS — none |
| Causal, novelty or publication-readiness claim made | PASS — none |

## Gate conclusion

P2.4 is PASS for a controlled analytical map containing 12 contradictions, 12
unresolved mechanisms, 12 boundary-condition families, ten cross-paper
non-equivalence rules and explicit P3 adversarial-design requirements. The active RFS
integrity notice remains quarantined and no contradiction is falsely resolved.

This PASS is literature/graph analysis only. It does not establish which mechanism is
true, whether AID is valid or useful, whether any benchmark reproduces, or whether
any empirical hypothesis will be supported. P2.5 is the next admissible gate: freeze
the literature matrix and novelty map with these limitations and dependency edges.
