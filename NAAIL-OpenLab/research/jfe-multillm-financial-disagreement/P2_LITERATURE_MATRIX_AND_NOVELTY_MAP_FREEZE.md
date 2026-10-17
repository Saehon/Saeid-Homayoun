# P2.5 Literature Matrix and Candidate-Novelty Map Freeze

Version: 1.0.0  
Gate: P2.5 — Freeze literature matrix and novelty map  
Freeze date: 2026-10-08  
Status: FROZEN P2 SEED SYNTHESIS — CANDIDATE NOVELTY ONLY

## Scope and acceptance rule

This artifact reconciles and freezes the bounded eight-record P2 seed set. It does
not claim an exhaustive systematic review, global prior-art clearance, verified
novelty, empirical support or publication readiness. Novelty below means a candidate
contribution not represented in the verified seed set and requiring broader search,
adversarial critique, replication and empirical falsification.

The freeze passes only if all eight P2.1 records appear once; P2.2 resource states,
P2.3 graph relations and P2.4 contradictions reconcile; every candidate novelty names
its closest anchors and a kill criterion; and the RFS integrity hold remains visible.

## Frozen source manifest

| Controlled source | Version | Git blob SHA | Frozen role |
|---|---:|---|---|
| P2_VERIFIED_AI_FINANCE_LITERATURE_REGISTER.md | 1.0 | 200ff5b3009b4fa669e16ba2cb017b175bdab171 | Verified identities, uses and claim boundaries |
| P2_OFFICIAL_REPLICATION_AND_PUBLIC_DATA_INVENTORY.md | 1.0 | fe774dffc6abb8f5cfd823d3b27c1daf9103797d | Resource, license, data and integrity dispositions |
| P2_LITERATURE_EVIDENCE_CONSTRUCT_GRAPH.md | 1.0 | cd4527695fdcaf592d5967e4a5a9a25250fde94e | Literature/resource/method/construct/test graph |
| P2_CONTRADICTIONS_MECHANISMS_BOUNDARY_CONDITIONS.md | 1.0 | b5d6e1a56a3ab0cd4c39a1186bc6cf35c85dbceb | Contradictions, rivals, boundaries and rejection logic |

Semantic changes require P0.4 change control, impact analysis and a new freeze version.
Adding a newly discovered article is not a silent row edit.

## Frozen literature matrix

| ID | Verified object | Core method/evidence | Resource state | Closest project relation | Material boundary | P3/P4 disposition |
|---|---|---|---|---|---|---|
| LIT-JFE-001 | Babina et al. (2024), firm AI investment, growth and innovation | Firm-level AI measures and panel evidence | PUBLIC_PACKAGE; Mendeley V2; CC BY 4.0 | Adoption/real-effects context | Firm AI adoption is not LLM judgment or model disagreement | Theory/boundary input; audit package before optional benchmark |
| LIT-JFE-002 | Lopez-Lira & Tang (2026), ChatGPT news interpretation and returns | Single-model news scoring and return prediction | PUBLIC_PACKAGE; Mendeley V2; CC BY 4.0; licensed/model dependencies | Nearest evidence→LLM→market benchmark | Single-model performance does not establish AID; chronology/version risks remain | Primary P4.2 candidate after manifest/license/version audit |
| LIT-JF-001 | Fuster et al. (2022), ML credit markets | Prediction, counterfactual and distributional analysis | PUBLIC_PARTIAL; synthetic data; proprietary principal input | Accuracy/fairness boundary | Credit evidence does not transfer to capital-market LLM disagreement | Boundary design; no full replication without access |
| LIT-RFS-001 | Gu, Kelly & Xiu (2020), ML asset pricing | Nonlinear prediction and OOS comparison | AUTHOR_RESOURCES; license restrictions unresolved | OOS and baseline discipline | Asset-pricing ML is not generative text interpretation | Method comparator after snapshot/license audit |
| LIT-RFS-002 | van Binsbergen et al. (2023), earnings expectations | Random-forest human/machine benchmark | INTEGRITY_HOLD | Adverse-evidence comparator only | Active 2026 Expression of Concern bars uncontested reliance | STOP_RELIANCE; excluded from positive novelty evidence |
| LIT-RFS-003 | Jha et al. (2026), finance-society language embeddings | Contextual embeddings and construct workflow | PUBLIC_PARTIAL; code plus short sample | Construct-development/validation anchor | Sector perception is not firm-event judgment or AID | Primary P4.3 workflow candidate; mechanics first |
| LIT-MS-001 | de Kok (2025), generative LLM textual analysis | Task validation, prompting, bias and reproducibility | PUBLIC_PARTIAL; code/examples/data; API/version limits | Protocol and construct-validity anchor | Guidance cannot validate this project's prompts or AID | Primary P4.1 candidate after environment/version audit |
| LIT-MS-002 | Chen, Pelger & Zhu (2024 issue), deep asset pricing | Deep conditional model, adversarial test assets, OOS | AUTHOR_RESOURCES; license/data persistence unresolved | Representation and OOS comparator | Deep learning is not AlphaFold/AlphaEvolve and does not validate AID | Architecture/baseline comparator after audit |

## Evidence-class coverage

| Dimension | Frozen coverage | Limitation |
|---|---|---|
| Outlets | JFE 2; Journal of Finance 1; RFS 3; Management Science 2 | Bounded seed, not systematic census |
| AI object | Firm AI; predictive ML; deep learning; embeddings; generative LLM | Sparse direct multi-LLM evidence |
| Finance object | Growth; credit; asset pricing; earnings; language; news/returns | Reporting/audit outcomes not directly covered |
| Resource class | 2 public; 3 partial; 2 author; 1 integrity hold | Execution/reproduction not established |
| Scientific role | Theory; method; construct; OOS; fairness; chronology; adverse evidence | No project empirical result |

## Candidate-novelty map

| ID | Candidate contribution | Closest anchors and overlap | Distinguishing test | Kill criterion | State |
|---|---|---|---|---|---|
| NOV-01 | AI Disagreement as cross-model dispersion given one evidence packet | JFE-002: LLM judgment; RFS-001/MS-002: model comparison | Hold evidence/rubric fixed; test dispersion beyond consensus | Identical prior art is found or AID lacks stable validity | CANDIDATE_NOT_VERIFIED |
| NOV-02 | Evidence-governed model×model and evidence×model pair representation | MS-002: representation; MS-001: task design | Pair-level evidence quality, confidence and provenance | Transparent summaries match stability/value or method is not reproducible | CANDIDATE_NOT_VERIFIED |
| NOV-03 | Separate informative disagreement from correlated machine consensus/error | JF-001: heterogeneous consequences; RFS-001: comparison | Test high-AID uncertainty and low-AID common-error rivals | Neither AID nor shared-error structure adds reliable OOS evidence | CANDIDATE_NOT_VERIFIED |
| NOV-04 | Chronology/version-aware multi-LLM panel with raw-output lineage | JFE-002 and MS-001: LLM use/reproducibility | Immutable evidence/model/prompt/run identity plus leakage probes | Chronology equivalence cannot be established and comparators fail | CANDIDATE_NOT_VERIFIED |
| NOV-05 | Human-review routing by disagreement × evidence quality × materiality | JF-001: consequence; MS-001: validation | Blind pre-specified escalation evaluated for error and cost | Routing adds no benefit, creates bias, or threshold was improperly tuned | CANDIDATE_NOT_VERIFIED |
| NOV-06 | One governed construct tested across market, information, reporting and enforcement outcomes | Seed papers cover isolated outcomes | Same frozen construct/provenance tested separately by family | Meaning/calibration is not sufficiently invariant | CANDIDATE_NOT_VERIFIED |

## Non-novel elements

The project must not claim novelty for using an LLM on financial text; applying ML or
deep learning to asset pricing; constructing embeddings; comparing models; reporting
OOS metrics; studying human versus machine prediction; discussing prompt sensitivity,
fairness or reproducibility; or merely invoking AlphaFold/AlphaEvolve terminology.

## Novelty-evidence firewall

No candidate can be promoted by citation absence in eight papers, internal enthusiasm,
council score, code completion or development results. Before an external novelty claim:

1. expand searches across finance, accounting, information systems, NLP/ML and working papers;
2. record databases, search strings, dates, inclusion/exclusion and deduplication;
3. inspect nearest-prior methods and claims, not titles alone;
4. execute P3 critic/falsifier review and preserve adverse matches;
5. complete admissible replication and construct-validity work;
6. obtain human approval for claim wording.

## P3 handoff

| Family | Positive candidate | Required rival/null |
|---|---|---|
| Incremental information | AID predicts resolution beyond consensus | AID is run noise/prompt artifact and adds no OOS information |
| Common error | Low AID reflects clarity | Low AID reflects correlated shared error |
| Market response | High AID identifies underreaction | Risk compensation, microstructure or chance explains it |
| Reporting risk | AID anticipates ICFR/restatement/CAM outcomes | Distress, industry or auditor selection explains it |
| Evidence quality | Weak evidence amplifies informative disagreement | Quality score is endogenous or length/negativity |
| Human review | Routing high-AID/material cases adds value | Review adds bias, cost or hindsight |
| Representation | Pair/evidence modeling improves generalization | Transparent summaries are equally stable |
| Distribution | Aggregate gains improve decisions | Gains mask concentrated subgroup harm |

P3 rankings cannot use validation or sealed outcomes. Every hypothesis needs a
rejection region, negative control, dependency path and outcome-exposure label.

## Freeze audit

| Check | Result |
|---|---|
| Eight unique P2.1 records represented | PASS — 8/8 |
| Resource classes reconcile to P2.2 | PASS — 2/3/2/1 |
| P2.3 graph constructs/dependencies preserved | PASS |
| P2.4 contradictions/boundaries propagated | PASS |
| Integrity-hold article used as positive support | PASS — prohibited |
| Candidate claims include closest overlap and kill criterion | PASS — 6/6 |
| Candidate promoted to verified novelty | PASS — none |
| Exhaustive/systematic-review claim | PASS — none |
| Package/model/test execution or result claim | PASS — none |
| Causal/publication-readiness claim | PASS — none |

## Phase conclusion

P2.5 is PASS for the versioned bounded literature matrix and falsifiable candidate
novelty map. Phase P2 is complete at 5/5 for seed-literature verification, resource
inventory, graph construction, contradiction analysis and controlled synthesis.
It is not a global systematic review, replication program, empirical test or verified
novelty assessment.

Next gate: P3.1 — generate competing hypotheses and mechanisms, including null and
adverse alternatives with explicit rejection conditions.
