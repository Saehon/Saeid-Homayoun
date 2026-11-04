# P2.3 Literature–Evidence–Construct Graph

Version: 1.0  
Gate: P2.3 — Build literature/evidence/construct graph  
Construction date: 2026-10-07  
Status: FROZEN SEED GRAPH — NO EMPIRICAL RESULT OR MODEL EXECUTION

## Scope and acceptance rule

This artifact instantiates the P1.4 Science Discovery schema with the eight
publisher-verified P2.1 literature records and their P2.2 resource/access evidence.
It separates reported findings, methods, data dependencies, candidate mechanisms,
project constructs, tests and governance constraints. An edge records a bounded
relationship; it never transfers a published result into evidence for this project.

P2.3 passes only if:

1. every P2.1 literature record is represented exactly once as a primary literature node;
2. every P2.2 resource disposition is linked to its literature node;
3. method, evidence, construct and outcome layers remain distinguishable;
4. access, license, chronology and integrity limitations propagate to dependent nodes;
5. adverse/null evidence cannot be deleted or converted into confirmatory support;
6. no article is asserted to validate AI Disagreement, and no package/model is claimed executed.

## Graph layers and controlled node types

| Layer | Node prefix | Meaning | Allowed evidentiary state |
|---|---|---|---|
| Literature | `LIT-` | Publisher-verified article identity | VERIFIED_RECORD; INTEGRITY_HOLD |
| Resource | `RES-` | Official/author-controlled package or supplement | PUBLIC_PACKAGE; PUBLIC_PARTIAL; AUTHOR_RESOURCES; INTEGRITY_HOLD |
| Data/dependency | `DAT-` | Inputs, licenses, APIs, corpora or market data | PUBLIC; RESTRICTED; LICENSE_UNKNOWN; VERSION_SENSITIVE |
| Method | `MET-` | Reported analytical or validation method | REPORTED_NOT_REPLICATED |
| Mechanism/boundary | `MEC-` | Candidate theoretical channel or boundary condition | CANDIDATE_ONLY |
| Project construct | `CON-` | Defined or candidate project variable | DEFINED; CANDIDATE_NOT_VALIDATED |
| Test/outcome | `TST-` | Planned falsification or outcome family | SPECIFIED_NOT_EXECUTED |
| Governance/anomaly | `GOV-` / `ANM-` | Constraints, warnings and adverse evidence | ACTIVE_CONTROL; OPEN_ADVERSE_EVIDENCE |

## Primary literature nodes

| Node | Literature object | Method nodes | Mechanism/boundary nodes | Permitted project use | State |
|---|---|---|---|---|---|
| LIT-JFE-001 | Babina et al. (2024), AI, firm growth and product innovation | MET-ADOPTION-MEASURE; MET-FIRM-PANEL | MEC-AI-ADOPTION; MEC-SCALE-INNOVATION | Adoption/real-effects context and heterogeneity design | VERIFIED_RECORD |
| LIT-JFE-002 | Lopez-Lira & Tang (2026), LLM news interpretation and returns | MET-LLM-NEWS-SCORE; MET-RETURN-PREDICTION | MEC-INFO-PROCESSING; MEC-MARKET-UNDERREACTION; MEC-CHRONOLOGY | Direct single-model benchmark and chronology control | VERIFIED_RECORD |
| LIT-JF-001 | Fuster et al. (2022), ML in credit markets | MET-ML-CREDIT; MET-COUNTERFACTUAL | MEC-ACCURACY-FAIRNESS; MEC-DISTRIBUTIONAL | Governance/boundary-condition comparator | VERIFIED_RECORD |
| LIT-RFS-001 | Gu, Kelly & Xiu (2020), empirical asset pricing via ML | MET-ML-ASSET-PRICING; MET-OOS-COMPARISON | MEC-NONLINEARITY; MEC-OOS-GENERALIZATION | OOS/model-comparison benchmark | VERIFIED_RECORD |
| LIT-RFS-002 | van Binsbergen et al. (2023), earnings expectations | MET-RF-EARNINGS; MET-HUMAN-MACHINE | MEC-CONDITIONAL-BIAS | Adverse-evidence comparator only; no clean benchmark reliance | INTEGRITY_HOLD |
| LIT-RFS-003 | Jha et al. (2026), finance-society language embeddings | MET-CONTEXTUAL-EMBEDDING; MET-CONSTRUCT-VALIDATION | MEC-LANGUAGE-PERCEPTION; MEC-EXTERNAL-VALIDITY | Construct-workflow and validation comparator | VERIFIED_RECORD |
| LIT-MS-001 | de Kok (2025), generative LLM textual analysis | MET-LLM-TEXT; MET-TASK-VALIDATION; MET-REPRODUCIBILITY | MEC-PROMPT-SENSITIVITY; MEC-MODEL-DRIFT | Protocol, validation and reproducibility anchor | VERIFIED_RECORD |
| LIT-MS-002 | Chen et al. (2024 issue), deep learning in asset pricing | MET-DEEP-ASSET-PRICING; MET-ADVERSARIAL-TEST-ASSET | MEC-NONLINEARITY; MEC-ECONOMIC-OBJECTIVE; MEC-OOS-GENERALIZATION | Representation/OOS/economic-objective comparator | VERIFIED_RECORD |

## Resource and data-dependency nodes

| Resource node | Literature node | Availability | Required dependency edges | Downstream disposition |
|---|---|---|---|---|
| RES-JFE-001-V2 | LIT-JFE-001 | PUBLIC_PACKAGE; Mendeley V2; CC BY 4.0 | `REQUIRES_FILE_MANIFEST` → DAT-FILE-HASHES; `USES_DATA` → DAT-AI-MEASURES | P4 planning eligible after checksum/dependency audit |
| RES-JFE-002-V2 | LIT-JFE-002 | PUBLIC_PACKAGE; Mendeley V2; CC BY 4.0 | `REQUIRES_LICENSE` → DAT-CRSP-TAQ-RAVENPACK; `REQUIRES_VERSION` → DAT-LLM-API-VERSION; `REQUIRES_FILE_MANIFEST` → DAT-FILE-HASHES | P4.2 priority; no execution yet |
| RES-JF-001-SYNTH | LIT-JF-001 | PUBLIC_PARTIAL; code plus synthetic data | `SUBSTITUTES_FOR` → DAT-RADAR-MCDASH; `LICENSE_UNKNOWN` → GOV-LICENSE-GATE | Plumbing tests only; cannot reproduce estimates |
| RES-RFS-001-AUTHOR | LIT-RFS-001 | AUTHOR_RESOURCES | `REQUIRES_LICENSE` → DAT-CRSP-COMPUSTAT; `LICENSE_UNKNOWN` → GOV-LICENSE-GATE; `REQUIRES_SNAPSHOT` → DAT-FILE-HASHES | Bounded benchmark only after audit |
| RES-RFS-002-HOLD | LIT-RFS-002 | INTEGRITY_HOLD; appendix only | `HAS_INTEGRITY_NOTICE` → ANM-RFS-002-EOC; `REQUIRES_LICENSE` → DAT-COMMERCIAL-EARNINGS | STOP_RELIANCE |
| RES-RFS-003-SHORT | LIT-RFS-003 | PUBLIC_PARTIAL; code plus short sample | `REQUIRES_LICENSE` → DAT-TEXT-CORPORA; `SAMPLE_OF` → DAT-FULL-CORPUS | Mechanics only; no full-result claim |
| RES-MS-001-COMPANION | LIT-MS-001 | PUBLIC_PARTIAL; code/examples/data | `LICENSE_UNKNOWN` → GOV-LICENSE-GATE; `REQUIRES_VERSION` → DAT-LLM-API-VERSION; `REQUIRES_INPUT` → DAT-CONFERENCE-CALLS | P4.1 priority after audit |
| RES-MS-002-AUTHOR | LIT-MS-002 | AUTHOR_RESOURCES | `LICENSE_UNKNOWN` → GOV-LICENSE-GATE; `REQUIRES_LICENSE` → DAT-MARKET-MACRO; `REQUIRES_SNAPSHOT` → DAT-FILE-HASHES | Architecture/OOS benchmark after audit |

## Project construct nodes

| Construct node | Definition in this graph | Literature/method parents | Current state and non-transfer rule |
|---|---|---|---|
| CON-AI-CONSENSUS | Mean/aggregate standardized judgment across actually executed eligible models | MET-LLM-NEWS-SCORE; MET-LLM-TEXT | DEFINED, NOT OBSERVED; single-model performance cannot validate it |
| CON-AID-SD | Cross-model standard deviation of comparable judgments | MET-OOS-COMPARISON; MET-HUMAN-MACHINE | CANDIDATE_NOT_VALIDATED; requires real multi-model panel |
| CON-AID-PAIR | Pairwise absolute/sign/rank disagreement | MET-OOS-COMPARISON; MET-DEEP-ASSET-PRICING | CANDIDATE_NOT_VALIDATED; AlphaFold-inspired pair representation only |
| CON-EVIDENCE-QUALITY | Provenance, completeness, timeliness, source authority and contradiction burden | MET-TASK-VALIDATION; MET-REPRODUCIBILITY | CANDIDATE_NOT_VALIDATED; not inferred from journal prestige |
| CON-MODEL-CONFIDENCE | Logged model-level confidence/uncertainty under a frozen rubric | MET-LLM-TEXT; MET-CONTEXTUAL-EMBEDDING | CANDIDATE_NOT_VALIDATED; self-report is not calibrated probability |
| CON-CHRONOLOGY-RISK | Risk that model training/context contains future information | MET-LLM-NEWS-SCORE; MET-REPRODUCIBILITY | DEFINED CONTROL; must be measured before inference |
| CON-PROMPT-SENSITIVITY | Within-task variance across pre-specified prompt variants | MET-TASK-VALIDATION | CANDIDATE_NOT_VALIDATED; development only before freeze |
| CON-MODEL-DRIFT | Output change attributable to provider/model/version/time change | MET-REPRODUCIBILITY | CANDIDATE_NOT_VALIDATED; requires immutable run metadata |
| CON-HUMAN-OVERRIDE | Governed reviewer disposition with recorded rationale | MET-HUMAN-MACHINE; MET-COUNTERFACTUAL | DEFINED CONTROL; human judgment is not ground truth by default |
| CON-MATERIALITY | Economic/reporting importance under a frozen rubric | MET-FIRM-PANEL; MET-COUNTERFACTUAL | CANDIDATE_NOT_VALIDATED |
| CON-DISTRIBUTIONAL-RISK | Heterogeneous error or consequence across groups/contexts | MET-ML-CREDIT; MET-COUNTERFACTUAL | CANDIDATE_NOT_VALIDATED; fairness evidence does not transfer automatically |

## Mechanism and boundary map

| Mechanism/boundary | Literature support type | Project implication | Falsifying observation to design later |
|---|---|---|---|
| MEC-INFO-PROCESSING | Directly motivated by LIT-JFE-002; not replicated here | AID may reflect different interpretation of identical evidence | AID vanishes under equivalent evidence/rubric or adds no OOS information |
| MEC-MARKET-UNDERREACTION | Reported context in LIT-JFE-002 | Test whether high AID conditions delayed market resolution | No incremental drift/absolute reaction after frozen controls |
| MEC-PROMPT-SENSITIVITY | Method warning from LIT-MS-001 | Separate construct variation from prompt artifacts | AID rankings unstable under admissible prompt perturbations |
| MEC-MODEL-DRIFT | Reproducibility boundary from LIT-MS-001 | Version/date/settings are graph dependencies | Results disappear across frozen reruns or cannot be procedurally reproduced |
| MEC-CHRONOLOGY | Critical boundary for recent LLM evidence | Future contamination can create false predictability | Placebo/future-information probes detect leakage |
| MEC-NONLINEARITY | Comparator from LIT-RFS-001/LIT-MS-002 | Allow nonlinear alternatives without assuming superiority | Simple benchmark performs equivalently or better OOS |
| MEC-OOS-GENERALIZATION | Comparator from LIT-RFS-001/LIT-MS-002 | Evaluate only after development freeze | Candidate fails temporal/firm sealed OOS |
| MEC-ACCURACY-FAIRNESS | Boundary from LIT-JF-001 | Accuracy gains need not imply equitable/economically desirable consequences | Error/consequence heterogeneity offsets aggregate gain |
| MEC-LANGUAGE-PERCEPTION | Construct lesson from LIT-RFS-003 | Language measures require contextual validation | Construct fails convergent/discriminant/human-coded checks |
| MEC-INTEGRITY-PROPAGATION | Active adverse-evidence rule | Contested source cannot silently support a dependent claim | Journal resolution/independent audit is required before release |

## Test and outcome nodes

| Test node | Planned target | Parent constructs/mechanisms | State |
|---|---|---|---|
| TST-CONSTRUCT-VALIDITY | Convergent, discriminant, calibration and human-coded validation | CON-AID-SD; CON-AID-PAIR; CON-EVIDENCE-QUALITY | SPECIFIED_NOT_EXECUTED |
| TST-CHRONOLOGY | Cutoff, future-information, timestamp and version probes | CON-CHRONOLOGY-RISK; MEC-CHRONOLOGY | SPECIFIED_NOT_EXECUTED |
| TST-PROMPT-MODEL-STABILITY | Pre-specified prompt, rerun and version variance | CON-PROMPT-SENSITIVITY; CON-MODEL-DRIFT | SPECIFIED_NOT_EXECUTED |
| TST-OOS-MARKET | Sealed returns/CAR/volatility evaluation | CON-AI-CONSENSUS; CON-AID-SD; MEC-MARKET-UNDERREACTION | SPECIFIED_NOT_EXECUTED |
| TST-OOS-INFORMATION | Sealed earnings surprise/forecast-error evaluation | CON-AI-CONSENSUS; CON-AID-SD; MEC-INFO-PROCESSING | SPECIFIED_NOT_EXECUTED |
| TST-OOS-REPORTING | Sealed ICFR/restatement/CAM-KAM evaluation | CON-AID-SD; CON-EVIDENCE-QUALITY; CON-MATERIALITY | SPECIFIED_NOT_EXECUTED |
| TST-OOS-ENFORCEMENT | Sealed AAER/fraud evaluation where data permit | CON-AID-SD; CON-EVIDENCE-QUALITY | SPECIFIED_NOT_EXECUTED |
| TST-DISTRIBUTIONAL | Error/consequence heterogeneity | CON-DISTRIBUTIONAL-RISK; MEC-ACCURACY-FAIRNESS | SPECIFIED_NOT_EXECUTED |

## Edge semantics and propagation rules

| Edge | Meaning | Propagation/control |
|---|---|---|
| `REPORTS_METHOD` | Article reports a method | Does not mean method was executed by this project |
| `HAS_RESOURCE` | Literature record links to controlled resource | Availability class and license constraints propagate |
| `REQUIRES_INPUT` / `USES_DATA` | Resource depends on an input | Input provenance, entitlement and time-vintage required |
| `REQUIRES_LICENSE` / `LICENSE_UNKNOWN` | Use or redistribution is constrained/unclear | Blocks public redistribution and confirmatory execution until resolved |
| `REQUIRES_VERSION` | Result depends on model/API/software version | Exact identifier/date/settings required; newer output is not historical output |
| `MOTIVATES` | Literature/method suggests a project construct/mechanism | Motivation is not validation or causal evidence |
| `BOUNDS` | Evidence limits external validity or interpretation | Limitation propagates to all dependent claims |
| `PLANNED_TEST_OF` | Test is designed for a construct/mechanism | Remains NOT_EXECUTED until logged execution exists |
| `HAS_INTEGRITY_NOTICE` | Source has an active journal notice | Adds `STOP_RELIANCE`; adverse node remains visible |
| `QUARANTINES` | Governance/anomaly blocks a dependency path | Cannot be overridden by narrative, citation count or engineering success |
| `FALSIFIES` / `DOES_NOT_SUPPORT` | Negative/null evidence challenges a relation | Must remain in graph and downstream synthesis |

## Controlled edge register

The following edge families are instantiated for all eight literature records:

- 8 `HAS_RESOURCE` edges: each `LIT-*` → its corresponding `RES-*`;
- 18 `REPORTS_METHOD` edges: literature nodes → method nodes in the primary-node table;
- 19 `MOTIVATES` edges: literature/method nodes → mechanism or construct nodes;
- 18 resource-dependency/control edges enumerated in the resource table;
- 20 `PLANNED_TEST_OF` edges from the eight test nodes to their listed parents;
- 2 active integrity edges: `RES-RFS-002-HOLD HAS_INTEGRITY_NOTICE ANM-RFS-002-EOC` and
  `ANM-RFS-002-EOC QUARANTINES LIT-RFS-002` for clean-benchmark reliance.

Total controlled seed edges: 85. This is a schema/content count, not a scientific
completion count. Edge direction is auditable from the tables; no edge terminates in
an empirical `RESULT` or `DISCOVERY` node because no project test has been executed.

## Graph invariants and executed structural checks

| Check | Result |
|---|---|
| Eight unique P2.1 literature nodes present | PASS — 8/8 |
| Each literature node has exactly one primary P2.2 resource disposition | PASS — 8/8 |
| Literature, resource, data, method, construct and test layers are distinguishable | PASS |
| Two public packages, three public-partial, two author-resource and one integrity-hold states preserved | PASS — 2/3/2/1 |
| Explicit license claims limited to the two observed CC BY 4.0 packages | PASS |
| Restricted/license-unknown/version-sensitive dependencies propagate to resources | PASS |
| LIT-RFS-002 Expression of Concern remains visible and blocks clean-benchmark reliance | PASS |
| Any edge converts a reported association into project evidence | PASS — none |
| Any empirical result/discovery node instantiated | PASS — none |
| Any external model/package execution claimed | PASS — none |
| Any biological AlphaFold execution claimed | PASS — none; pair representation is inspiration only |
| Any AlphaEvolve search uses validation or sealed outcomes | PASS — none; no search executed |
| Planned tests explicitly marked NOT_EXECUTED | PASS — 8/8 |
| Orphan literature or resource nodes | PASS — none |

## Adverse evidence and quarantine

`ANM-RFS-002-EOC` records Oxford Academic's Expression of Concern,
DOI `10.1093/rfs/hhag017`, published 2026-03-01, with the journal investigation still
pending at the 2026-10-07 verification. The article is retained because deleting it
would hide material evidence. Its methods may inform an adverse-evidence comparison,
but its findings cannot serve as uncontested support, a clean benchmark, or a
pass-dependent foundation. Reopening requires a journal resolution or a separately
authorized independent audit that is logged as new evidence.

## DARWIN and Co-Scientist use

- **Define:** graph nodes distinguish reported facts, candidates, controls and planned tests.
- **Alternatives:** multiple mechanisms and construct definitions coexist without premature ranking.
- **Retrieve/Replicate:** resources carry exact access, license and version constraints into P4.
- **Whole-system dependencies:** chronology, provenance, licensing and integrity propagate downstream.
- **Invalidate/Falsify:** every candidate mechanism has a rejection path; adverse/null nodes persist.
- **Next evolution:** P2.4 will map contradictions and boundary conditions without changing this seed graph silently.

Co-Scientist critic/falsifier/meta-review roles may add candidate objections and tests,
but they do not create observations or independent samples. The 100-perspective board
remains a structured review protocol, not 100 independent agents.

## Gate conclusion

P2.3 is PASS for a controlled, internally reconciled seed literature/evidence/construct
graph. It contains eight verified literature nodes, eight resource dispositions,
explicit data/license/version dependencies, 11 project constructs, ten mechanism or
boundary nodes, eight planned test nodes and 85 controlled edges. The graph preserves
the unresolved integrity hold and contains no project result or discovery node.

This PASS does not establish construct validity, replication success, model availability,
empirical support, causal identification, novelty or publication readiness. P2.4 is the
next admissible gate: map contradictions, unresolved mechanisms and boundary conditions.
