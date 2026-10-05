# P1.3 Feedback Loops and Leakage/Overfitting Risk Map

Version: 1.0  
Date: 2026-10-05  
Gate: P1.3 — Map feedback loops and leakage/overfitting risks  
Scope: system-control design only; no data, model, construct, result, or leakage test has been empirically validated by this artifact.

## 1. Purpose and scientific boundary

This map identifies legitimate learning loops, prohibited backward information flows, leakage and overfitting risks, detection tests, incident responses, and quarantine scope across the 60-gate JFE research system. It operationalizes the P0 scientific firewall and P1.2 dependency register.

The permitted scientific direction is:

`historically available evidence → frozen prompt/model protocol → raw judgments → frozen pair/AID construct → prespecified outcome test → falsification/OOS → claim audit`.

Information may move backward only inside an explicitly labeled DEVELOPMENT loop with versioned history. Validation outcomes cannot select or evolve candidates. Sealed-test outcomes cannot modify hypotheses, data filters, prompts, models, constructs, specifications, thresholds, or narratives.

AlphaEvolve-inspired search is development-only. AlphaFold-inspired recycling is representation refinement under prespecified development rules, not biological AlphaFold. Co-Scientist and 10 councils × 10 perspectives may critique designs but are not observations, independent replications, or a source of outcome truth.

## 2. Feedback-loop classes

| Class | Direction | Permitted use | Required record | Prohibited use |
|---|---|---|---|---|
| F0 Forward evidence flow | Past evidence → later process/output | Normal pipeline execution | source time, hash, version, run ID | future information inserted upstream |
| F1 Development learning | Development result → revised development candidate | Generate, criticize, mutate, reject, rerun | candidate lineage, objective, exposure log, version increment | relabeling development as sealed evidence |
| F2 Validation checkpoint | Frozen candidate → validation result | One-way selection checkpoint under frozen rule | validation access, candidates, rule, full results | tuning on validation then reusing it as untouched validation |
| F3 Sealed test | Frozen final system → one-time OOS result | Confirmatory evaluation after human approval | opening approval, hashes, immutable outputs | any feedback into selection or specification |
| F4 Falsification feedback | Failed control → quarantine/repair/new development cycle | Diagnose and invalidate claims | incident ID, affected descendants, repair decision | deleting adverse evidence or preserving confirmatory label |
| F5 Governance feedback | Audit/reviewer finding → controlled change | Correct governance or release defects | change request, approval, impact analysis | silent rewrite of preregistered objects |
| F6 Operational feedback | Runtime/availability event → engineering repair | Restore execution without scientific tuning | logs, error class, before/after hashes | calling adverse scientific output a technical failure |
| F7 Publication feedback | Referee/editor request → robustness or extension | Labeled replication/exploratory extension | request, exposure status, analysis label | portraying post-review analysis as preregistered |

## 3. Information-flow zones and one-way valves

| Zone | Contents | May receive from | May send to | One-way valve |
|---|---|---|---|---|
| Z0 Governance | question, approvals, change records, ledger | human authority, audited history | all zones | outcome knowledge never erases prior versions |
| Z1 Evidence acquisition | filing/text/data snapshots and provenance | historically available sources | Z2, Z3, Z6 | source availability time must precede prediction cut-off |
| Z2 Development | candidate prompts, models, pair/AID variants, exploratory tests | Z0, Z1, development outcomes | frozen objects in Z3 | validation/sealed outcomes cannot enter |
| Z3 Frozen protocol | approved prompts, registry, hypotheses, partitions, constructs, tests | approved Z2 objects | Z4, Z5 | changes require new version and impact analysis |
| Z4 Validation | limited one-way checkpoint | Z3 | pass/fail decision and full immutable record | used validation becomes development history after redesign |
| Z5 Sealed test | untouched firm/time OOS outcomes | human-approved Z3 package | immutable result to Z6 | no return path to Z2–Z4 |
| Z6 Falsification/audit | negative controls, reproducibility, claim audit | Z1–Z5 | quarantine, limitation, release decision | failure changes claim status, never raw history |
| Z7 Publication/release | manuscript, tables, package, public code/data | audited Z6 outputs | public/JFE audience | human approval and protected-main control |

## 4. Leakage and overfitting risk register

| ID | Risk / prohibited path | Earliest gate | Detection or falsification test | Required response | Quarantine scope |
|---|---|---|---|---|---|
| LR-001 | Filing amendment or later restatement treated as contemporaneous evidence | P5.1 | compare filing accepted/accession timestamps and version hashes | rebuild historical snapshot | affected evidence and descendants |
| LR-002 | Future market/accounting outcome included in prompt/evidence | P5.2/P6.1 | token/source audit against prediction cut-off | leakage incident; rerun from clean evidence | affected runs, constructs, outcome tests |
| LR-003 | Outcome-derived sample filter or label used before partition freeze | P5.5 | recompute eligibility using only pre-cutoff fields | re-freeze partitions under change control | affected sample and confirmatory tests |
| LR-004 | Firm appears across train/validation/test through aliases, parents, mergers, or duplicates | P5.5 | entity-resolution and group-overlap test | regroup and re-split | overlapping entities and results |
| LR-005 | Time-window overlap lets later documents inform earlier target | P5.2/P5.5 | interval-overlap and embargo-gap checks | adjust window/embargo prospectively | affected periods |
| LR-006 | Pretrained model may contain post-cutoff knowledge | P6.2 | knowledge-cutoff/vendor record; chronology probes; source-grounded scoring | label limitation; use chronology-safe benchmark where possible | historical-prediction claim, not necessarily POC |
| LR-007 | Retrieval/search performed after outcome realization without historical snapshot | P5.1/P6.3 | query, cache, source-version, retrieval-time audit | quarantine run; reconstruct admissible corpus | affected retrieval/model runs |
| LR-008 | Prompt embeds outcome hints, firm identity proxies, or target labels | P6.1 | adversarial prompt review and blinded-template diff | revise/version before validation | affected prompt family and runs |
| LR-009 | Model output parser uses target labels or hand corrections informed by outcomes | P6.1/P6.3 | parser code review; synthetic gold tests; correction log | quarantine corrected outputs; deterministic rerun | affected model judgments |
| LR-010 | Unlogged model/version drift across runs | P6.2/P6.3 | registry completeness and response-fingerprint checks | split versions; no pooled full-panel claim | unidentified/drifted runs |
| LR-011 | Missing provider output imputed as if actually executed | P6.3 | raw-output existence and run-ID referential integrity | mark missing; use partial-panel label only | full-panel AID claims |
| LR-012 | Repeated prompts selected for favorable result | P6.4 | enumerate all attempts; compare prespecified aggregation | retain all runs; apply frozen aggregation | cherry-picked judgment panel |
| LR-013 | Confidence elicitation calibrated using outcomes | P7.3 | calibration-data lineage audit | development-only recalibration/new version | affected confidence-weighted measures |
| LR-014 | Pair representation recycling continues until downstream outcome improves | P7.4 | iteration-count/convergence rule versus outcome-access log | invalidate selected pair spec | pair descendants and AID candidates |
| LR-015 | AID candidates generated from validation/sealed residual patterns | P8.1/P8.3 | candidate timestamp and ancestry versus exposure log | leakage incident; retire candidate lineage | candidate and recombinations |
| LR-016 | Candidate tournament optimizes many specifications without complexity/multiplicity control | P8.2/P8.4 | search-space count, effective trials, null simulation | apply penalty/correction; disclose search | selected AID and claims |
| LR-017 | Best model/construct chosen on validation and re-tested on same validation | P8.4 | selection/evaluation set identity test | validation becomes development; obtain fresh validation | claimed validation performance |
| LR-018 | Sealed outcome opened before hypotheses/construct/tests freeze | P3.5/P8.5/P11.2 | compare approval/opening time to artifact hashes | critical incident; no confirmatory claim on that set | sealed set and dependent claims |
| LR-019 | Sealed adverse result prompts threshold, covariate, FE, horizon, or sample change | P11.2 | post-opening commit/deviation diff | retain original; label changes exploratory; require fresh sealed data | revised confirmatory claim |
| LR-020 | Multiple outcomes/horizons/subgroups reported selectively | P10/P11 | preregistered analysis manifest versus executed/reported matrix | report full family; multiplicity control | selective tables/claims |
| LR-021 | Hyperparameters or stopping rules tuned to validation/OOS | P7/P8/P10 | configuration chronology and hash comparison | rerun on development; invalidate exposed checkpoint | tuned model/construct result |
| LR-022 | Controls/FE selected after seeing significance | P10 | specification registry versus executed code | classify post-hoc; report multiverse/sensitivity | causal/incremental claim |
| LR-023 | Hypothesis or mechanism rewritten after results | P3.5/P10 | version-history and result-exposure comparison | preserve original; label HARKing/exploratory | confirmatory theory claim |
| LR-024 | Microsoft POC drives main-sample construct/test choices without development label | P9/P10 | POC exposure-to-change trace | treat POC as development; freeze before fresh OOS | generalization claim |
| LR-025 | Human reviewers see outcomes while labeling inputs or scoring evidence | P5/P9 | reviewer blinding/access log | quarantine labels; independent blinded relabel | affected human validation |
| LR-026 | 100-perspective scores counted as 100 independent observations | P3.4 | unit-of-analysis audit | collapse to structured review provenance | statistical independence claim |
| LR-027 | Duplicate firm-year/text/model outputs inflate sample | P5/P6 | primary-key uniqueness and content-hash duplicate checks | deduplicate under frozen rule | affected estimates/SEs |
| LR-028 | Cross-sectional preprocessing uses full sample, including held-out periods/firms | P5/P7/P8 | fit-object lineage; train-only transform test | refit on development only | transformed validation/test data |
| LR-029 | Normalization/ranking computed using future or sealed distribution | P6/P8 | compare fit-window max date to observation date | rolling/train-only normalization | affected standardized scores |
| LR-030 | Early stopping based on repeated validation probes | P8 | validation query-count and decision-log test | validation becomes development; fresh checkpoint needed | selected candidate performance |
| LR-031 | Falsification test designed after observing anomaly solely to rescue claim | P11.1 | test timestamp and rationale audit | label diagnostic/post-hoc; retain original anomaly | claim-strength upgrade |
| LR-032 | Failed run removed because it worsens dispersion/performance | P6.3/P6.4 | expected-run manifest versus raw-store reconciliation | restore or mark failure/missingness | variance and AID estimates |
| LR-033 | Code/table/manuscript uses different data or construct versions | P10/P11 | end-to-end hash and lineage reconciliation | stop release; regenerate consistently | mismatched tables/claims |
| LR-034 | External benchmark/test result copied without verified provenance | P2/P4/P11 | source/package/version/readback verification | exclude or label unverified | replication/novelty claim |
| LR-035 | Referee-requested analysis silently presented as original confirmatory evidence | P11.5 | revision provenance and manuscript label audit | label response/post-hoc; preserve chronology | presentation/claim classification |
| LR-036 | Portfolio or engineering success treated as scientific completion | All | gate evidence audit against PASS criteria | correct ledger/status | overstated completion claim |

## 5. Overfitting budget and search governance

Before P8 development search begins, freeze an `OVERFITTING_BUDGET` containing:

| Field | Requirement |
|---|---|
| Candidate families | Enumerate baseline, pairwise, rank/sign, confidence- and evidence-weighted families |
| Maximum generated candidates | Finite prespecified bound per evolution cycle |
| Maximum cycles | Finite bound; no indefinite search |
| Development objective | Frozen predictive/scientific objective and direction |
| Complexity penalty | Frozen cost for parameters, branches, interactions, and representation depth |
| Multiplicity accounting | Number of tried candidates/specifications/outcomes retained in audit |
| Stopping rule | Objective convergence, budget exhaustion, or falsification failure—not validation/OOS improvement |
| Validation queries | Prespecified maximum; every access logged; no adaptive repeated probing |
| Sealed queries | One approved evaluation per frozen package unless preregistered otherwise |
| Reporting | Full finalist set, failed candidates, selection rule, and post-hoc analyses disclosed |

Exceeding the budget does not automatically prove a false result, but it removes the confirmatory label until a fresh, untouched evaluation set and approved change record exist.

## 6. Incident severity and mandatory response

| Severity | Example | Immediate action | Scientific disposition |
|---|---|---|---|
| L0 Logging defect | non-scientific metadata missing but reconstructable | repair immutably; record before/after | no status promotion from repair alone |
| L1 Local contamination | one traceable observation/run affected | quarantine row/run and descendants | unaffected work may continue |
| L2 Partition/process contamination | validation reused adaptively or transform fit on held-out data | stop affected evaluation; redesign in development | old checkpoint cannot remain confirmatory |
| L3 Sealed contamination | sealed outcome influenced any upstream selection | preserve incident evidence; close set to further tuning | all dependent confirmatory claims quarantined |
| L4 Release integrity failure | claim/table/package mismatch or undisclosed contamination | STOP_RELEASE and human escalation | no submission/public release/main merge |

The same bounded incident follows the persistent two-failure rule. After the second failed repair attempt, assign `BLK-JFE-YYYY-NNN`, record both failures and exact future repair, move it to `OPEN_REPAIR_QUEUE.md`, quarantine descendants, and advance only to scientifically independent work.

## 7. Required automated and manual checks

| Check ID | Check | Expected result |
|---|---|---|
| CHK-01 | `evidence_available_at <= prediction_cutoff` | true for every model input |
| CHK-02 | development/validation/test entity-group intersection | empty under frozen grouping rule |
| CHK-03 | time windows plus embargo overlap | no prohibited overlap |
| CHK-04 | prompt/evidence scan for target/outcome tokens and future dates | no unresolved target leakage |
| CHK-05 | raw-run manifest ↔ stored output reconciliation | every expected run present or explicitly failed/missing |
| CHK-06 | model registry completeness | provider/model/version/settings/time recorded |
| CHK-07 | transform/model fit lineage | fitted only on permitted development data |
| CHK-08 | candidate ancestry ↔ exposure log | no validation/sealed ancestor |
| CHK-09 | frozen hashes before validation/sealed opening | exact match |
| CHK-10 | executed specification matrix ↔ reported tables | full reconciliation with post-hoc labels |
| CHK-11 | table/manuscript numbers ↔ reproducible outputs | exact regeneration |
| CHK-12 | human approval IDs for protected actions | present and valid |

These are specifications for later implementation. They have not yet been executed on a research dataset.

## 8. Machine-readable risk record

```yaml
risk_id: LR-000
gate_detected: P0.0
source_zone: Z0
destination_zone: Z0
prohibited_flow: string
exposure_time: ISO-8601|null
affected_object_hashes: [sha256]
affected_gates: [P0.0]
severity: L0|L1|L2|L3|L4
detection_test: CHK-00
test_result: PASS|FAIL|NOT_RUN
fail_count: 0|1|2
incident_or_blocker_id: string|null
quarantine_scope: [string]
repair_action: string
reopening_condition: string
human_approval_id: string|null
scientific_label: DEVELOPMENT|VALIDATION|SEALED|EXPLORATORY|QUARANTINED
```

## 9. Acceptance and adversarial review

P1.3 may be PASS for design only if:

1. Permitted development feedback is separated from validation and sealed-test flow.
2. At least one risk covers each of evidence timing, entity/time splits, retrieval, prompts/parsing, model drift/missingness, pair/AID evolution, specifications/outcomes, human review, and release integrity.
3. Every validation/sealed contamination rule preserves adverse evidence and removes the confirmatory label rather than erasing history.
4. AlphaEvolve-inspired search has an explicit development-only budget and stopping rule.
5. Co-Scientist/100-perspective review cannot create statistical independence or empirical evidence.
6. Incident severity, quarantine, two-failure escalation, human authority, and STOP_RELEASE are explicit.
7. The artifact does not claim that checks were run or that leakage is absent.

## 10. Explicit non-claims and next gate

This artifact freezes a leakage and overfitting control design only. It does not demonstrate historical-data integrity, model chronology safety, clean partitions, absence of leakage, construct validity, predictive power, causal identification, successful replication, or publication readiness.

Next gate: P1.4 — build the evidence→AI→construct→outcome system graph with typed, timed, provenance-bearing edges and explicit prohibited paths.
