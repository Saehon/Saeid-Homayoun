# P0.4 Change Control, Versioning, and Preregistration Rules

Status: FROZEN v1.0  
Gate: P0.4  
Date: 2026-10-04  
Scope: NAAIL Trust Finance / Multi-LLM Financial Disagreement

## 1. Purpose

This protocol makes the research history auditable and prevents retrospective changes from being presented as prospectively specified. It governs the canonical plan, research question, estimands, hypotheses, partitions, evidence rules, prompts, models, parsers, constructs, analysis code, outcomes, tables, claims, and release artifacts.

P0.4 is a governance-design freeze. It does not itself preregister the later empirical study, validate any implementation, or authorize access to validation or sealed-test outcomes.

## 2. Source-of-truth hierarchy

When records conflict, authority is resolved in this order:

1. recorded human approval for protected scientific decisions;
2. canonical GitHub artifacts on the authorized branch at their immutable commit SHA;
3. immutable preregistration snapshot and its hashes;
4. canonical gate ledger, deviation register, and OPEN REPAIR QUEUE;
5. controlled Google Drive mirror and archived research materials; and
6. working notes, dashboards, messages, and local files.

The Drive mirror is required for resilience and controlled materials, but a mirror does not silently supersede the versioned canonical record. Any resolved discrepancy must be logged and both locations reconciled by readback.

## 3. Versioning model

Every controlled object uses `MAJOR.MINOR.PATCH` plus immutable content hashes.

| Increment | Meaning | Examples | Effect |
|---|---|---|---|
| MAJOR | Changes scientific meaning, confirmatory scope, estimand, hypothesis family, partition logic, primary construct, primary outcome, or interpretation boundary | New estimand; replacing AID*; changing sealed sample; adding an outcome after viewing results | Requires human approval, new preregistration snapshot, impact assessment, and loss of prior confirmatory status where applicable |
| MINOR | Prospective, substantively relevant extension that preserves the frozen primary design | Prespecified secondary robustness test; additional model family before validation access | Requires change request, rationale, affected-object list, tests, and approval when protected objects are involved |
| PATCH | Non-substantive correction with no effect on scientific meaning or results | Typo; broken link; formatting; deterministic bug fix proven not to alter outputs | Requires logged diff, tests/readback, and explicit statement of no scientific effect |

Versions never overwrite history. Git commits, Drive revisions or replacement records, hashes, and supersession links preserve lineage. Reusing an old version label for changed content is prohibited.

## 4. Controlled-object registry

Each frozen object must have a registry entry containing:

- stable object ID and title;
- object type and owner;
- current semantic version;
- canonical GitHub path/commit or controlled Drive ID;
- SHA-256 content hash, or provider revision plus exported hash where appropriate;
- status: DRAFT, FROZEN, SUPERSEDED, QUARANTINED, or RETIRED;
- effective timestamp in UTC;
- dependency and downstream-output links;
- data classification and permitted locations;
- human approval ID when required; and
- predecessor/successor versions and related deviation/change IDs.

The registry must distinguish a document version from a data snapshot, model version, environment lock, and analysis run. A model alias without an exposed exact version is recorded as an alias with uncertainty; it is never upgraded silently to an exact version.

## 5. Change-request workflow

Every substantive change follows:

`PROPOSE → CLASSIFY → IMPACT MAP → REVIEW → APPROVE/REJECT → IMPLEMENT → TEST → DUAL-SAVE → READBACK → CLOSE`

A stable change request (`CR-JFE-YYYY-NNN`) records:

1. proposer, timestamp, reason, and requested effective date;
2. old and proposed object versions with diffs/hashes;
3. MAJOR/MINOR/PATCH classification and justification;
4. affected gates, hypotheses, data partitions, experiments, tables, claims, code, and downstream artifacts;
5. whether any validation/sealed outcomes were visible to any participant or process;
6. contamination, leakage, multiplicity, and overfitting assessment;
7. required reruns, quarantines, withdrawals, or replacement samples;
8. reviewer and human-approval decision where required;
9. implementation commits/Drive revisions and tests; and
10. closure status with unresolved limitations.

Rejected proposals remain in history. Emergency technical changes use the same record and cannot bypass scientific impact review.

## 6. Protected changes requiring human approval

Human approval is mandatory before changing:

- primary research question, estimand, hypothesis family, or claimed contribution;
- development/validation/sealed-test construction or access rule;
- information cutoff, eligibility/exclusion rule, primary outcome, metric, model, prompt, parser, scoring rubric, AID*/consensus definition, or primary specification after its freeze;
- external-model use involving non-public evidence;
- classification or release status of restricted/internal material;
- a dependency-critical quarantine or CLOSED/PASS scientific status;
- public claims, replication release, journal submission, or protected-main merge.

Automation may draft a change request and implement an already authorized bounded change. It cannot approve its own protected change.

## 7. Preregistration stages

The project uses three cumulative prospective snapshots.

### PREREG-A — discovery and replication design

Created before formal hypothesis ranking and benchmark evaluation. It freezes the literature/replication scope, discovery roles, scoring dimensions, negative-control families, and rules preventing the 100-perspective board from becoming fabricated independent evidence.

### PREREG-B — construct and model protocol

Created before validation access. It freezes evidence timing, prompts, model registry rules, parsers, scoring rubric, candidate-generation space, development objective, complexity penalty, validation decision/stopping rule, and planned AID*/consensus freeze procedure.

### PREREG-C — confirmatory empirical analysis

Created before sealed-test opening. It freezes the final hypotheses and directions, estimands, sample/partition manifests and hashes, information cutoffs, primary/secondary outcomes, AID*/consensus definitions, controls, transformations, fixed effects, clustering, missing-data and outlier handling, multiplicity policy, economic-significance criteria, negative controls, heterogeneity tests, robustness set, exclusion rules, code/environment commit, table shells, and permitted claims.

Each snapshot includes a UTC timestamp, author/approver, Git commit, Drive archive ID, complete manifest of component hashes, and a plain-language summary. A preregistration is prospective only when created before the relevant protected outcomes are accessed.

## 8. Prospective versus post-hoc labeling

Every hypothesis, variable, outcome, model, subgroup, test, and claim is labeled one of:

- `CONFIRMATORY_PREREGISTERED` — fully specified prospectively in the applicable snapshot;
- `PRESPECIFIED_SECONDARY` — prospectively defined but not primary;
- `EXPLORATORY_DEVELOPMENT` — generated and evaluated only in development;
- `POST_HOC_VALIDATION` — conceived after validation access;
- `POST_HOC_SEALED_TEST` — conceived after sealed-test access; or
- `REPLICATION_ONLY` — deterministic reproduction without new selection.

Post-hoc work may be valuable but cannot be relabeled confirmatory. It must be presented separately, with exposure timing and rationale, and requires new untouched data for later confirmation.

## 9. Outcome-access and amendment rules

Before any change is classified, the record must answer whether development, validation, or sealed-test outcomes were visible and to whom. The highest exposed partition controls the label.

- Before validation access: approved prospective amendments may retain confirmatory eligibility if the preregistration is superseded transparently before access.
- After validation access: changes influenced by validation are exploratory; used validation becomes development history if it drives redesign, and a new untouched validation set is required.
- After sealed-test access: changes are post hoc; the opened sealed sample cannot regain confirmatory status through amendment. Confirmation requires a genuinely untouched future sample.

Null or unfavorable completed results are not errors and do not justify silent amendment. A technical rerun is permitted only when the prespecified computation failed to complete or was implemented incorrectly, with raw logs preserved and impact assessed.

## 10. Deviation register

Any departure from a frozen protocol receives `DEV-JFE-YYYY-NNN` and records discovery time, object/version, expected versus actual behavior, cause, evidence, affected partitions/gates/outputs/claims, outcome-exposure state, severity, containment, quarantine, repair, approval, rerun decision, and closure evidence.

Severity is:

- D0 administrative — no scientific effect;
- D1 minor technical — bounded and proven not to affect inference;
- D2 material scientific — may alter measurements, estimates, or interpretation;
- D3 critical integrity — leakage, partition contamination, fabricated/missing provenance, unauthorized restricted-data/model use, or loss of reproducibility.

D2/D3 deviations quarantine affected outputs until reviewed. D3 requires immediate stop on dependent confirmatory claims and human escalation. Two persistent failed repairs also create or update the OPEN REPAIR QUEUE under its stable blocker ID.

## 11. Dependency and rerun rules

Every change/deviation impact map traverses:

`evidence → extraction → features → model runs → parsed judgments → pair representations → AID/consensus → regressions/tests → tables/figures → manuscript claims`

Downstream outputs inherit the most restrictive status of their dependencies. A changed upstream hash invalidates downstream reproducibility until deterministic rerun or an evidence-backed no-impact determination. Partial reruns must state the exact unaffected boundary; convenience is not evidence of independence.

## 12. Dual-save and release discipline

Meaningful controlled changes are saved to the authorized GitHub branch and project Drive folder, then independently read back. Public GitHub receives no proprietary/restricted raw data. One active branch/scope and one Draft PR are maintained; protected `main` is never merged without explicit approval.

A change is not CLOSED until canonical and mirror identifiers, versions/hashes, tests, readback, ledger/run-log updates, and remaining limitations are recorded. `DUAL_SAVE_STATUS=PASS` confirms preservation and readback, not scientific validity.

## 13. Machine-checkable change record

```yaml
change_id: CR-JFE-YYYY-NNN
object_id: string
old_version: string
new_version: string
classification: MAJOR|MINOR|PATCH
status: PROPOSED|APPROVED|REJECTED|IMPLEMENTED|CLOSED
requested_at: ISO-8601
effective_at: ISO-8601|null
outcome_exposure: NONE|DEVELOPMENT|VALIDATION|SEALED_TEST
affected_gates: [string]
affected_partitions: [string]
old_sha256: string|null
new_sha256: string|null
github_commit: string|null
drive_id_or_revision: string|null
human_approval_id: string|null
deviation_ids: [string]
quarantined_outputs: [string]
required_reruns: [string]
tests: [string]
```

## 14. Acceptance test and gate conclusion

P0.4 may be marked PASS only if the frozen design specifies the source-of-truth hierarchy, semantic version classes, controlled-object registry, change workflow, protected decisions, staged preregistration, prospective/post-hoc labels, outcome-exposure rules, deviation severity, dependency/rerun logic, dual-save requirements, and a machine-checkable record.

All design elements are present in v1.0. Therefore P0.4 is PASS for change-control and preregistration design only. No empirical preregistration snapshot, operational registry, validation access, sealed-test opening, or scientific result is implied.
