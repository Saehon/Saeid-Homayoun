# P1.2 Dependency and Critical-Path Map

Version: 1.0  
Date: 2026-10-05  
Gate: P1.2 — Map dependencies and critical paths  
Scope: system-design freeze; no dataset, model, replication, or empirical result is validated by this document.

## 1. Purpose and governing constraints

This register translates the canonical 60-gate plan into testable predecessor, release, quarantine, and fail-forward relationships. It applies Systems Thinking and the DARWIN sequence to the full evidence→model→construct→test→outcome→publication system.

The four portfolio projects remain priority-ranked for operations only. They are not scientific predecessors of this JFE project. Nothing here fabricates a cross-project dependency.

Human approval remains mandatory for restricted-data use, sealed-test opening, external scientific claims, submission, and protected-main merge. AlphaFold and AlphaEvolve are methodological inspirations only. Co-Scientist and the 10 councils × 10 perspectives are structured review roles, not independent observations or fabricated agents.

## 2. Dependency vocabulary

| Type | Meaning | Failure consequence |
|---|---|---|
| HARD | Successor would be scientifically invalid without predecessor evidence | Quarantine successor and dependent claims |
| GOVERNANCE | Human approval, preregistration, licensing, or release control | Stop protected action; independent design work may continue |
| DATA | Availability, rights, identity, timing, lineage, or quality requirement | Quarantine affected sample/variable; unaffected sources may continue |
| SCIENTIFIC | Theory, measurement, identification, falsification, or inference requirement | No confirmatory or causal claim until resolved |
| EXECUTION | Reproducible code, model access/version, environment, or run-log requirement | Do not count output as executed evidence |
| SOFT | Improves quality but is not required for bounded independent work | Continue with limitation recorded |
| RELEASE | Clean reproduction, claim audit, human review, or publication approval | No public/JFE release |

Every edge has one of four dispositions: `PROCEED`, `PROCEED_WITH_LIMITATION`, `QUARANTINE_DEPENDENT`, or `STOP_RELEASE`.

## 3. Gate-level dependency register

| ID | Predecessor evidence | Successor gates/decision | Type | Minimum release condition | Failure propagation and independent work |
|---|---|---|---|---|---|
| DEP-001 | P0.1 question, estimand, null, boundaries | P2–P11 claim-relevant work | HARD/SCIENTIFIC | Frozen version and prospective change record | Quarantine tests not tied to the estimand; literature inventory may continue |
| DEP-002 | P0.2 authority and data classification | Any restricted/private data or public claim | GOVERNANCE | Required approval and storage class recorded | Stop protected action; public-schema and synthetic work may continue |
| DEP-003 | P0.3 partition firewall | P3.5, P5.5, P8, P10, P11.2 | HARD/SCIENTIFIC | Immutable partition roles and one-way information flow | Quarantine validation/sealed claims; development-only design may continue |
| DEP-004 | P0.4 versioning/preregistration | Frozen prompts, constructs, tests, deviations | GOVERNANCE/SCIENTIFIC | Controlled-object versions and exposure status recorded | Label post-hoc or rerun impacted descendants |
| DEP-005 | P0.5 ledger and repair controls | All gate status and blocker disposition | HARD/GOVERNANCE | 60-gate invariant and persistent failure history | No PASS without evidence; unrelated gates may proceed |
| DEP-006 | P1.1 bounded system inventory | P1.2–P1.5 | HARD | Actors/objects/interfaces distinguished from verified availability | Do not infer access or implementation from map |
| DEP-007 | P1.2 dependency register | P1.3–P1.5 and downstream quarantine decisions | HARD | Critical paths, bottlenecks, propagation, fail-forward rules frozen | Dependent release decisions remain provisional |
| DEP-008 | P1.3 leakage/feedback map | P1.5, P5.5, P6–P8, P10–P11 | HARD/SCIENTIFIC | Leakage paths and prohibited feedback specified | Quarantine affected confirmatory outputs |
| DEP-009 | P1.4 evidence→AI→construct→outcome graph | P1.5, P2.3, P5.4, P11.5 | HARD/SCIENTIFIC | Traceable node/edge semantics and timing | No end-to-end provenance claim |
| DEP-010 | P1.5 system-map freeze | Operational build across P2–P11 | GOVERNANCE | v1 hashes and approved deviations | Bounded P2/P4 discovery may start, but integration stays provisional |
| DEP-011 | P2.1 verified literature | P2.3–P3.5, novelty claims | SCIENTIFIC | Source/DOI/title/claim verification | No novelty claim; replication-package inventory may continue |
| DEP-012 | P2.2 official packages/public-data inventory | P4 replication choices | DATA/EXECUTION | Source, license, version, code/data availability logged | Unavailable package enters limitation/repair flow; other papers continue |
| DEP-013 | P2.3–P2.5 evidence graph, contradictions, novelty freeze | P3 tournament and JFE contribution | HARD/SCIENTIFIC | Contradictions and prior constructs linked to hypotheses | P3 generation may be exploratory only until freeze |
| DEP-014 | P3.1–P3.4 generation, critic, falsifier, board scoring | P3.5 hypothesis portfolio | HARD/SCIENTIFIC | Competing mechanisms, rejection tests, and score provenance | No winner by unsupported vote or fabricated independence |
| DEP-015 | P3.5 ranked hypothesis freeze | Confirmatory P10/P11 tests | HARD/SCIENTIFIC | Hypotheses frozen before relevant outcome exposure | Post-exposure additions labeled exploratory |
| DEP-016 | P4.1–P4.4 admissible replications | P4.5 benchmark freeze and method choices | SCIENTIFIC/EXECUTION | Actual reproduction or explicit documented limitation | Failed benchmark cannot become PASS; independent benchmark can continue |
| DEP-017 | P4.5 cross-replication synthesis | P6/P7/P8 construct choices | SOFT/SCIENTIFIC | Reusable lessons and non-replicated limitations recorded | Development may continue, but benchmarking claims stay limited |
| DEP-018 | P5.1 acquisition/provenance | P5.2–P5.5 and any observation-level run | HARD/DATA | Deterministic retrieval, source date, hash, entity identity | Quarantine untraceable observations only |
| DEP-019 | P5.2/P5.3 outcome schemas and mappings | P5.5, P10 | HARD/DATA | Variable timing, entity keys, label windows, rights | No linked outcome inference; text-only protocol work may continue |
| DEP-020 | P5.4 Evidence Passport | P6 raw judgments through P11 audit | HARD/DATA | Source→firm→period→model→run lineage complete | Quarantine outputs lacking lineage |
| DEP-021 | P5.5 frozen partitions | P6–P8 development and P11.2 sealed OOS | HARD/SCIENTIFIC | Partition hashes, access log, human-approved sealed opening | Stop confirmatory evaluation; synthetic/unit testing may continue |
| DEP-022 | P6.1/P6.2 prompts, rubric, model registry | P6.3 actual model runs | HARD/EXECUTION | Prompt/rubric/version/settings logged before execution | Unlogged output is not model evidence |
| DEP-023 | P6.3 actual available runs | P6.4–P8 and P9.2 | HARD/EXECUTION | Provider/model/version/protocol/raw output recorded | Never impute or fabricate missing providers; partial panel labeled |
| DEP-024 | P6.4 variance evidence | P6.5 raw panel freeze | SCIENTIFIC | Repetition/prompt/model/evidence variance quantified as prespecified | Freeze with limitation or remain PARTIAL; downstream uncertainty must carry forward |
| DEP-025 | P6.5 frozen raw panel | P7 pair representation and P8 AID evolution | HARD | Immutable run IDs and hashes | Quarantine pair/construct values from changed runs |
| DEP-026 | P7.1–P7.4 pair/evidence/confidence refinement on development | P7.5 pair-spec freeze | HARD/SCIENTIFIC | Convergence/iteration limit and confidence semantics prespecified | No biological AlphaFold claim; unstable variants remain exploratory |
| DEP-027 | P7.5 frozen pair specification | P8 candidate generation and sealed evaluation | HARD | Formula/code/version frozen | Changed pair spec invalidates descendant AID comparisons |
| DEP-028 | P8.1 candidates + P8.2 objectives | P8.3/P8.4 evolution | HARD/SCIENTIFIC | Development-only objective, complexity penalty, candidate lineage | Validation/sealed feedback is leakage and triggers quarantine |
| DEP-029 | P8.4 falsification/comparison | P8.5 AID* freeze | HARD/SCIENTIFIC | Rejection tests and selection rule applied prospectively | No winner selected from sealed outcomes |
| DEP-030 | P8.5 AID*/Consensus freeze | P9/P10/P11 confirmatory use | HARD | Construct formula/code/hash frozen | Changed construct makes later work exploratory or requires fresh sealed data |
| DEP-031 | P9.1 Microsoft evidence packet | P9.2 model POC | HARD/DATA | Filing identity, period, hash, admissible evidence boundaries | POC may not substitute synthetic or future information |
| DEP-032 | P9.2 actual model runs | P9.3 verification/human routing | HARD/EXECUTION | Real logged outputs under frozen protocol | No fabricated multi-model PASS |
| DEP-033 | P9.3 reviewed POC | P9.4 multi-firm scale | GOVERNANCE/SCIENTIFIC | Failure modes and escalation reviewed | Development demo may exist; no validated-POC claim |
| DEP-034 | P9.4 prespecified pilot | P9.5 POC freeze | DATA/SCIENTIFIC | Sampling rule and failures reported | Microsoft-only result cannot support multi-firm generalization |
| DEP-035 | P3.5, P5.5, P6.5, P8.5 | P10 outcome tests | HARD/SCIENTIFIC | Hypotheses, partitions, raw panel, constructs frozen | Stop confirmatory inference; coding shells may continue |
| DEP-036 | P10.1–P10.4 results | P10.5 mechanism/heterogeneity/value | SCIENTIFIC | Prespecified main outcomes and multiplicity rules | Mechanism claims stay exploratory if main link absent |
| DEP-037 | P10 frozen result provenance | P11.1 adversarial tests | HARD | Tables trace to code/data/run hashes | No robustness claim on untraceable result |
| DEP-038 | P11.1 fresh falsification | P11.2 sealed OOS | GOVERNANCE/SCIENTIFIC | No unresolved material leakage; opening approval recorded | Keep sealed set closed; repair independent issues first |
| DEP-039 | P11.2 genuine sealed OOS | P11.3 robustness and confirmatory claim | HARD/SCIENTIFIC | One-time held-out result with immutable log | Null/adverse result is retained, never relabeled technical failure |
| DEP-040 | P11.3 robustness | P11.4 clean reproduction | EXECUTION/RELEASE | Alternative definitions/models and limitations recorded | Reproduction can proceed but claims remain limited |
| DEP-041 | P11.4 clean reproduction | P11.5 final audit/manuscript | HARD/RELEASE | Independent clean run recreates released outputs | STOP_RELEASE |
| DEP-042 | P11.5 claim↔evidence audit + human approval | JFE submission/public release/main merge | RELEASE | All claims classified; gaps disclosed; explicit approvals | STOP_RELEASE; never auto-merge protected main |

## 4. Critical paths

### CP-01 — Scientific inference

P0 question/firewall/change control → P1 leakage/dependency graph → P2 literature/novelty → P3 frozen hypotheses → P5 frozen partitions → P6 frozen raw judgment panel → P7 pair specification → P8 AID* freeze → P10 prespecified tests → P11 falsification/sealed OOS → claim audit.

This is the longest dependency-critical route to an evidence-backed JFE claim. Any unresolved HARD/SCIENTIFIC blocker quarantines the affected inference, not necessarily every design task.

### CP-02 — Data and outcome integrity

P0 data rules → P5 deterministic acquisition → outcome/mapping timing → Evidence Passport → immutable partitions → observation/model/run lineage → clean reproduction.

Critical bottlenecks: licenses/rights, entity-period identity, public availability, event timing, source hashes, and partition integrity.

### CP-03 — Model and construct integrity

P6 prompt/rubric/model registry → actual versioned runs → variance assessment → raw panel freeze → P7 pair representations → P8 development-only evolution/falsification → AID*/Consensus freeze.

Critical bottlenecks: provider access, immutable model/version/settings, repeatability, missing-model handling, confidence calibration, and prohibition of sealed-test feedback.

### CP-04 — Release and publication

P10 traceable results → P11 adversarial tests → sealed OOS → robustness → clean reproduction → claim/evidence audit → human approval → submission/release. Protected `main` remains outside automated authority.

## 5. Fail-forward and quarantine matrix

| Blocked object | Scientifically admissible independent work | Quarantined output |
|---|---|---|
| One literature source/package | Other verified sources; schema and contradiction logging | Claims depending on missing source/replication |
| One outcome dataset | Model protocol, text pipeline, unaffected outcomes | Tests/generalizations using unavailable outcome |
| One model provider | Available-model engineering and partial-panel diagnostics | Full-panel AID and cross-provider claims |
| Microsoft evidence/run | Multi-firm design, synthetic interface tests | Microsoft POC PASS and empirical generalization |
| Partition/firewall integrity | Documentation, synthetic unit tests, unrelated literature | All confirmatory/validation/sealed results |
| Evidence Passport lineage | Source repair and unaffected traceable rows | Untraceable observations and descendants |
| AID selection firewall | Baseline descriptive measures on development only | Selected AID*, sealed/OOS inference |
| Clean reproduction | Repair documentation and final gap report | Release/submission claim of reproducibility |

The persistent two-failure rule applies per bounded task. At failure 2/2, record the stable blocker in `OPEN_REPAIR_QUEUE.md`, quarantine dependent outputs, and move to the next admissible task. A new hour does not reset attempts.

## 6. Bottleneck register

| Bottleneck | Earliest detection | Preventive control | Release criterion |
|---|---|---|---|
| Source/data licensing or access | P2.2/P5.1 | rights/classification inventory | authorized acquisition or explicit scoped limitation |
| Temporal leakage | P1.3/P5.2 | availability timestamps and chronology tests | no unresolved material look-ahead path |
| Entity/event linkage error | P5.2/P5.3 | deterministic keys and sampled reconciliation | prespecified mapping checks pass |
| Model/version drift | P6.2/P6.3 | immutable registry and run metadata | exact provider/model/settings recorded |
| Missing provider/output | P6.3 | explicit missingness; no imputation as real run | actual logged output or partial-panel limitation |
| Construct overfitting | P8.2–P8.4 | development-only objective and complexity penalty | AID* frozen before sealed outcome access |
| Human-review capacity | P9.3/P11.5 | escalation rubric and review queue | required approvals recorded |
| Reproduction failure | P11.4 | environment lock, hashes, clean runner | independent clean reproduction |

## 7. Machine-readable edge schema

```yaml
dependency_id: DEP-000
predecessors: [P0.0]
successors: [P0.0]
type: HARD|GOVERNANCE|DATA|SCIENTIFIC|EXECUTION|SOFT|RELEASE
required_evidence: [artifact_or_check]
failure_disposition: PROCEED|PROCEED_WITH_LIMITATION|QUARANTINE_DEPENDENT|STOP_RELEASE
affected_claims: [claim_id]
independent_work_permitted: [gate_or_task]
quarantine_scope: [artifact_or_observation]
reopening_condition: string
human_approval_required: boolean
```

## 8. Acceptance and falsification checks

P1.2 may be PASS for design only if:

1. Every phase P0–P11 appears as predecessor or successor in the register.
2. The scientific, data/model, and release paths are separated.
3. Partition, provenance, real-model-run, AID-freeze, sealed-OOS, reproduction, and human-release controls are HARD or protected dependencies.
4. Fail-forward is allowed only when the successor does not depend scientifically on the blocker.
5. Quarantine scope and release-stop logic are explicit.
6. Portfolio priority is not represented as a scientific dependency.
7. No model run, dataset availability, replication success, causal effect, novelty result, or journal readiness is claimed.

## 9. Explicit non-claims and next gate

This artifact validates a dependency-control design only. It does not establish that any external dataset is available or licensed, that any named model can be executed, that any replication succeeds, that AID predicts outcomes, or that the project is ready for sealed testing or publication.

Next gate: P1.3 — map feedback loops and leakage/overfitting risks, using this register to identify prohibited backward information flows.
