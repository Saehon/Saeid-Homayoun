# P1.4 Evidence→AI→Construct→Outcome System Graph

Version: 1.0  
Date: 2026-10-05  
Gate: P1.4 — Build evidence→AI→construct→outcome system graph  
Scope: graph and provenance design only; no node represents verified external availability, an executed model run, an observed result, or a validated scientific claim unless later linked to evidence with the required status.

## 1. Purpose and graph contract

This artifact specifies the project’s Science Discovery graph: a directed, typed, time-aware, provenance-bearing graph connecting theory, literature, evidence, models, judgments, pair representations, disagreement constructs, hypotheses, tests, anomalies, outcomes, claims, reviews, and releases.

The graph is both a digital research twin and a scientific control surface. It must support:

1. forward traceability from source evidence to every reported claim;
2. reverse traceability from a claim to source, code, model, partition, test, and approval;
3. temporal checks against look-ahead information;
4. version and exposure-state control;
5. dependency quarantine and impact propagation;
6. separation of development, validation, sealed, exploratory, and released evidence;
7. explicit contradictions, anomalies, falsifiers, and null/adverse results;
8. human approval before protected release actions.

AlphaFold-inspired pair representations and AlphaEvolve-inspired construct evolution are represented as methodological nodes and development-only edges. They are not claims of running biological AlphaFold or an autonomous scientific-discovery system. Co-Scientist and 10 councils × 10 perspectives are structured review provenance, not independent observations.

## 2. Layered system graph

| Layer | Node prefix | Purpose | Examples |
|---|---|---|---|
| L0 Governance | GOV | authority, question, preregistration, approvals, change and exposure history | research question, sealed-open approval |
| L1 Theory/literature | THY, LIT | mechanisms, prior claims, replication packages, contradictions | ambiguity mechanism, verified paper record |
| L2 Source evidence | SRC, DOC, OBS | original sources, documents, observation identities and availability times | SEC filing, accession, firm-period row |
| L3 Processing | ING, MAP, FEAT | acquisition, parsing, entity/event mapping, transformations | EDGAR retrieval, text segmentation |
| L4 AI laboratory | PRM, MOD, RUN, JUD | prompt, model registry, execution and raw judgment | frozen rubric, actual versioned response |
| L5 Pair representation | PAIR, CONF | model×model/evidence×model representations and uncertainty | GPT–Claude pair, evidence support pair |
| L6 Constructs | CON, AID | consensus, disagreement and measurement definitions | SD, MAD, pairwise AID, AID* |
| L7 Discovery | HYP, MEC, CRT, FAL | hypotheses, mechanisms, critique and rejection designs | H1, alternative explanation, placebo |
| L8 Evaluation | SPL, TST, RES, ANO | partitions, tests, results and anomalies | development split, coefficient, failed control |
| L9 Outcomes | OUT | market, information, reporting and enforcement targets | CAR, volatility, ICFR, CAM, AAER |
| L10 Claim/release | CLM, TAB, MAN, REV, REL | claims, exhibits, manuscript, reviews and release decisions | Table 3, JFE claim, human approval |

## 3. Canonical node types and required fields

| Node type | Required identity and content | Required control fields |
|---|---|---|
| GOV.Question | question, estimand, unit, horizon, null | version, approval, effective time |
| GOV.Change | changed object, reason, impact | prior/new hash, exposure state, approver |
| THY.Mechanism | mechanism and boundary conditions | source links, competing mechanism IDs |
| LIT.Work | title, authors, outlet, year, DOI/URL | verification status, access time, package links |
| SRC.Source | provider, URI/accession, license/classification | retrieval time, available-at time, checksum |
| DOC.Evidence | document version, entity, period, section | source ID, hash, accepted/available-at times |
| OBS.Unit | firm/entity, fiscal/event period, observation key | partition, eligibility version, lineage status |
| ING.Process | code/environment/configuration | version/hash, executed-at, input/output hashes |
| MAP.Link | source and target entity/event IDs | mapping rule/version, validation status |
| PRM.Protocol | prompt, rubric, output schema | frozen version, development/validation status |
| MOD.Model | provider, model/version, settings | knowledge/access date, registry status |
| RUN.Execution | prompt/model/evidence IDs, raw output | run ID/time, status, immutable hash |
| JUD.Judgment | dimension, score, confidence, rationale/citations | parser version, run parent, missingness flag |
| PAIR.Representation | ordered/unordered pair and feature vector | inputs, iteration, convergence, version |
| CON.Construct | formula/code, normalization, missingness rule | candidate ancestry, objective, freeze status |
| HYP.Hypothesis | direction, mechanism, unit, timing | freeze time, rejection criteria, exposure status |
| SPL.Partition | membership rule and observation IDs | role, hash, access/open history |
| TST.Test | specification, controls/FE, outcome, metric | preregistration ID, code hash, multiplicity family |
| RES.Result | estimate/metric, uncertainty, sample count | test/run IDs, raw output hash, status label |
| ANO.Anomaly | observed inconsistency or failed control | severity, affected nodes, quarantine status |
| OUT.Outcome | definition, source, horizon, event time | availability, label window, mapping version |
| CLM.Claim | precise statement and strength | supporting/opposing result IDs, limitation IDs |
| REV.Review | role/council, critique, score, recommendation | not-an-observation flag, reviewer/version/time |
| REL.Decision | release/submission/merge action | human approval ID, prerequisites, decision time |

## 4. Canonical edge types

| Edge | Source → target | Meaning | Critical constraints |
|---|---|---|---|
| DERIVED_FROM | any derived node → source parent | direct computational or documentary ancestry | hashes and process ID required |
| RETRIEVED_FROM | DOC/SRC → provider/source | acquisition origin | available-at and retrieved-at required |
| AVAILABLE_BEFORE | evidence/outcome → cutoff/test | chronology relation | must be true for model inputs |
| MAPS_TO | document/row → entity/event/outcome | identity or temporal linkage | rule/version required |
| INPUT_TO | evidence/protocol/model → process/run/test | consumed input | exact version/hash required |
| PRODUCES | process/run/test → output | direct output | immutable output identity required |
| SCORED_AS | raw run → judgment | deterministic or reviewed parsing | parser/correction provenance required |
| PAIRED_WITH | model/evidence/judgment ↔ peer | pair representation membership | pair order/symmetry stated |
| AGGREGATED_INTO | judgment/pair → construct | consensus/AID calculation | formula/version and missingness required |
| MUTATED_FROM | candidate → prior candidate(s) | development-only AlphaEvolve ancestry | no validation/sealed ancestor |
| RECYCLED_FROM | pair iteration → earlier iteration | development refinement | frozen stopping rule required |
| SUPPORTS | theory/evidence/result → hypothesis/claim | positive support | strength and limitations required |
| CONTRADICTS | work/result/anomaly → claim/hypothesis | opposing evidence | never deleted because adverse |
| TESTS | test → hypothesis/mechanism/claim | evaluation relation | preregistration/exposure status required |
| FALSIFIES | result/anomaly → hypothesis/claim | rejection evidence | affected descendants quarantined as needed |
| FAILS_TO_REJECT | result → null/hypothesis | statistical disposition | not equivalent to proof |
| EXPLAINS | mechanism → hypothesis/result/anomaly | proposed explanation | competing explanations linked |
| MEASURES | construct/outcome → latent concept | measurement relation | validity evidence required later |
| EVALUATED_ON | candidate/test → partition | sample exposure relation | role and access history required |
| DEPENDS_ON | any node → predecessor | scientific/execution/governance dependency | inherits quarantine/impact status |
| SUPERSEDES | new version → old version | controlled replacement | old node remains immutable |
| QUARANTINES | incident/anomaly → affected node | invalid or provisional status propagation | scope/reason/reopening required |
| REVIEWED_BY | object/claim → review provenance | structured critique | reviewer roles not treated as data |
| APPROVED_BY | protected action → human decision | authorization | approval ID and scope required |
| REPORTED_IN | result/claim → table/manuscript | presentation link | exact regeneration required |
| RELEASED_AS | package/decision → release | controlled externalization | all release gates satisfied |

## 5. Minimum end-to-end paths

### Path A — Evidence to raw judgment

`SRC.Source → RETRIEVED_FROM → DOC.Evidence → INPUT_TO → ING.Process → PRODUCES → FEAT/TextPacket → INPUT_TO → RUN.Execution → SCORED_AS → JUD.Judgment`

Release conditions: evidence available before prediction cut-off; source/document hashes; prompt/model/settings; actual run log; raw output; parser lineage. Missing provider output remains missing and cannot be fabricated or imputed as a real run.

### Path B — Judgment to disagreement construct

`JUD.Judgment → PAIRED_WITH → PAIR.Representation → AGGREGATED_INTO → CON.AIDCandidate → MUTATED_FROM/RECYCLED_FROM (development only) → CON.AIDStar`

Release conditions: frozen development objective, candidate ancestry, complexity/multiplicity record, no validation/sealed ancestor, falsification results, and pre-sealed AID* hash.

### Path C — Hypothesis to outcome result

`THY.Mechanism + LIT.Work → SUPPORTS/CONTRADICTS → HYP.Hypothesis → TESTS ← TST.Test → EVALUATED_ON → SPL.Partition; OUT.Outcome → INPUT_TO → TST.Test → PRODUCES → RES.Result`

Release conditions: hypothesis and test frozen before relevant exposure; partition and outcome timing verified; full specification and multiplicity family recorded.

### Path D — Result to claim and publication

`RES.Result + ANO.Anomaly + FAL.ControlResult → SUPPORTS/CONTRADICTS/FALSIFIES → CLM.Claim → REVIEWED_BY → REV.Review → REPORTED_IN → TAB/MAN → APPROVED_BY → REL.Decision → RELEASED_AS`

Release conditions: adverse and null evidence included; clean reproduction; claim strength matches evidence; limitations disclosed; human approval; no automated protected-main merge.

### Path E — Reverse claim audit

Every `CLM.Claim` must traverse backward to at least one `RES.Result`, `TST.Test`, `SPL.Partition`, `CON.Construct`, `JUD.Judgment`/`RUN.Execution` where applicable, `DOC.Evidence`/`OUT.Outcome`, processing code/environment, and relevant governance approvals. Missing mandatory ancestry changes the claim to `QUARANTINED` or `UNSUPPORTED`.

## 6. Core graph node inventory v1

| ID | Type | Description | Initial status |
|---|---|---|---|
| GOV-Q1 | GOV.Question | Incremental information in cross-LLM disagreement beyond consensus | FROZEN_DESIGN |
| GOV-FW1 | GOV.Firewall | Development/validation/sealed-test rules | FROZEN_DESIGN |
| THY-A1 | THY.Mechanism | disagreement as information ambiguity/interpretation difficulty | CANDIDATE |
| THY-A2 | THY.Mechanism | disagreement as model noise/miscalibration | COMPETING_CANDIDATE |
| LIT-REG | LIT.Register | verified literature/replication inventory | NOT_POPULATED |
| SRC-SEC | SRC.Source | SEC/EDGAR/XBRL candidate source family | CANDIDATE_NOT_VERIFIED |
| SRC-MKT | SRC.Source | market/accounting outcome source family | CANDIDATE_NOT_VERIFIED |
| SRC-AUD | SRC.Source | ICFR/CAM/restatement/AAER source family | CANDIDATE_NOT_VERIFIED |
| DOC-PKT | DOC.Evidence | historically bounded evidence packet | SCHEMA_ONLY |
| OBS-FY | OBS.Unit | firm-period observation | SCHEMA_ONLY |
| ING-EDGAR | ING.Process | deterministic evidence acquisition | NOT_IMPLEMENTED |
| MAP-ENTITY | MAP.Link | entity/period/event linkage | NOT_IMPLEMENTED |
| PRM-FIN | PRM.Protocol | financial judgment prompt/rubric | NOT_FROZEN |
| MOD-REG | MOD.Model | model registry entry | NOT_POPULATED |
| RUN-RAW | RUN.Execution | actual provider/model execution | NOT_EXECUTED |
| JUD-RISK | JUD.Judgment | risk/direction/confidence judgment | NOT_OBSERVED |
| PAIR-MM | PAIR.Representation | model×model pair representation | SPEC_NOT_FROZEN |
| PAIR-EM | PAIR.Representation | evidence×model pair representation | SPEC_NOT_FROZEN |
| CON-CONS | CON.Construct | AI consensus | NOT_FROZEN |
| CON-AID | CON.Construct | candidate AI disagreement family | DEVELOPMENT_ONLY |
| CON-AIDSTAR | CON.Construct | selected AID* | NOT_SELECTED |
| HYP-PORT | HYP.Portfolio | ranked hypotheses/mechanisms | NOT_FROZEN |
| SPL-DEV | SPL.Partition | development sample | NOT_CREATED |
| SPL-VAL | SPL.Partition | validation sample | NOT_CREATED |
| SPL-SEALED | SPL.Partition | sealed firm/time OOS sample | NOT_CREATED |
| TST-MKT | TST.Test | market outcomes | NOT_PREREGISTERED |
| TST-INFO | TST.Test | information outcomes | NOT_PREREGISTERED |
| TST-REP | TST.Test | reporting outcomes | NOT_PREREGISTERED |
| TST-ENF | TST.Test | enforcement/fraud outcomes | NOT_PREREGISTERED |
| OUT-CAR | OUT.Outcome | returns/CAR/volatility family | SCHEMA_ONLY |
| OUT-EARN | OUT.Outcome | earnings surprise/forecast error family | SCHEMA_ONLY |
| OUT-ICFR | OUT.Outcome | ICFR/restatement/CAM-KAM family | SCHEMA_ONLY |
| OUT-AAER | OUT.Outcome | AAER/fraud family | SCHEMA_ONLY |
| RES-MAIN | RES.Result | main prespecified results | NOT_RUN |
| ANO-REG | ANO.Anomaly | anomaly/failed-control register | EMPTY |
| CLM-INC | CLM.Claim | incremental information claim | UNSUPPORTED_PENDING_RESULTS |
| CLM-MEC | CLM.Claim | ambiguity mechanism claim | UNSUPPORTED_PENDING_RESULTS |
| REV-100 | REV.Review | 10 councils × 10 structured perspectives | DESIGN_ROLE_ONLY |
| REL-JFE | REL.Decision | manuscript/submission decision | NOT_AUTHORIZED |
| REL-MAIN | REL.Decision | protected-main merge decision | HUMAN_APPROVAL_REQUIRED |

## 7. Prohibited edges and graph invariants

| ID | Prohibited edge/path | Reason and disposition |
|---|---|---|
| PE-01 | OUT/RES from validation or sealed sample → MUTATED_FROM/RECYCLED_FROM candidate | outcome-driven tuning; quarantine candidate lineage |
| PE-02 | sealed result → prompt/model/data filter/construct/specification change with confirmatory label retained | sealed contamination; exploratory only or fresh sealed sample |
| PE-03 | future DOC/OUT → INPUT_TO earlier RUN | temporal leakage; quarantine run and descendants |
| PE-04 | missing RUN → JUD treated as observed | fabricated model evidence; prohibited |
| PE-05 | REV-100 → RES as 100 independent observations | structured perspectives are not statistical units |
| PE-06 | Microsoft POC result → main-sample general claim without prespecified multi-firm evidence | invalid generalization |
| PE-07 | engineering/CI status → scientific PASS/CLM support | engineering success is not scientific evidence |
| PE-08 | unsupported CLM → RELEASED_AS | STOP_RELEASE |
| PE-09 | unverified LIT/SRC record → verified novelty/replication claim | source must be verified first |
| PE-10 | automation → APPROVED_BY protected human decision | human authority cannot be delegated to automation |

Graph invariants:

1. Each derived node has at least one parent and process/version edge.
2. Each model judgment has exactly one actual run parent or is explicitly `MISSING/FAILED`.
3. Every model input evidence timestamp is no later than its prediction cut-off.
4. Every result identifies one test specification, partition version, outcome version, and code/environment hash.
5. Every claim links to supporting and opposing evidence, or states that none exists.
6. Validation/sealed exposure edges are append-only and never removed.
7. Quarantine propagates through `DEPENDS_ON`, `DERIVED_FROM`, `PRODUCES`, and `AGGREGATED_INTO` descendants unless a documented no-impact proof breaks propagation.
8. Superseded nodes remain immutable and discoverable.
9. CLOSED and engineering green states never imply scientific PASS.
10. Release nodes require clean reproduction and explicit human approval.

## 8. Example machine-readable records

```yaml
node:
  id: RUN-000001
  type: RUN.Execution
  version: 1.0.0
  scientific_status: NOT_EXECUTED
  exposure_state: DEVELOPMENT
  entity_id: null
  period_end: null
  available_at: null
  created_at: ISO-8601
  content_hash: sha256|null
  code_or_model_version: string|null
  source_or_parent_ids: [DOC-000001, PRM-000001, MOD-000001]
  human_approval_id: null
  quarantine_status: CLEAR|QUARANTINED
```

```yaml
edge:
  id: EDGE-000001
  type: INPUT_TO
  from: DOC-000001
  to: RUN-000001
  valid_from: ISO-8601
  observed_at: ISO-8601
  version: 1.0.0
  evidence_hash: sha256
  rule_or_process_id: ING-000001
  partition_role: DEVELOPMENT|VALIDATION|SEALED|null
  allowed: true
  violation_id: null
```

## 9. Required graph queries and tests

| Query/test | Expected result before relevant PASS/release |
|---|---|
| QG-01 Claim ancestry completeness | zero mandatory missing ancestors |
| QG-02 Future-to-past input edges | zero |
| QG-03 Validation/sealed ancestors of candidate mutation/recycling | zero |
| QG-04 Judgments without actual run or explicit missing/failed state | zero |
| QG-05 Results without test/partition/outcome/code lineage | zero |
| QG-06 Claims without opposing/null/anomaly audit | zero |
| QG-07 Released nodes with quarantined ancestors | zero |
| QG-08 Protected actions without human approval | zero |
| QG-09 Duplicate primary IDs/content hashes in observation/run layer | zero unresolved |
| QG-10 Changed upstream hash with stale released descendant | zero |
| QG-11 Model/prompt/construct versions absent from a result path | zero |
| QG-12 Structured reviews counted as empirical observations | zero |

These queries are specifications for later implementation; they have not been executed against a populated research graph.

## 10. DARWIN and Science Discovery use

| DARWIN stage | Graph operation |
|---|---|
| Define | create question, estimand, theory, outcome, and governance nodes |
| Alternatives | create competing mechanisms, hypotheses, model/construct candidates, and contradiction edges |
| Retrieve/Replicate | attach verified literature, packages, sources, executions, and reproduction results |
| Whole-system dependencies | traverse dependency, ancestry, timing, partition, and approval edges |
| Invalidate/Falsify | add falsifier, anomaly, contradiction, quarantine, and null/adverse-result nodes |
| Next evolution | create versioned development descendants while preserving exposure history |

No adverse evidence may be deleted to simplify the graph. The Science Discovery graph is cumulative: it records why candidates were rejected, which claims weakened, and what new evidence would reopen a quarantined path.

## 11. Acceptance and adversarial review

P1.4 may be PASS for design only if:

1. Governance, theory/literature, source evidence, processing, AI runs, pair representations, constructs, discovery, evaluation, outcomes, claims, reviews, and releases have explicit node types.
2. Every primary path includes version, time, hash, partition/exposure, and approval controls where applicable.
3. At least one prohibited edge covers sealed feedback, temporal leakage, fabricated model runs, false independence, engineering-as-science, and unauthorized release.
4. Null, adverse, contradictory, and anomaly evidence are first-class nodes/edges.
5. Reverse claim audit and quarantine propagation are specified.
6. Initial inventory distinguishes schema/design nodes from verified, executed, observed, or supported states.
7. The artifact does not claim that the graph is populated or that any required query passed on real data.

## 12. Explicit non-claims and next gate

This artifact validates a graph schema and controlled scientific-flow design only. It does not verify literature, data licenses or availability, evidence acquisition, entity mappings, model access or execution, partitions, constructs, hypotheses, results, causal effects, novelty, reproducibility, or publication readiness.

Next gate: P1.5 — freeze the v1 system map and dependency register by reconciling P1.1–P1.4, resolving internal inconsistencies, hashing the control artifacts, and recording explicit limitations.
