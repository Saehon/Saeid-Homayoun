# P0.3 Development, Validation, and Sealed-Test Firewall

Status: FROZEN v1.0  
Gate: P0.3  
Date: 2026-10-04  
Scope: NAAIL Trust Finance / Multi-LLM Financial Disagreement

## 1. Purpose

This protocol prevents hypothesis, prompt, model, construct, threshold, and specification choices from being optimized against evidence later reported as out-of-sample. It governs all data, labels, outcomes, model judgments, derived constructs, code, logs, tables, and human feedback used by the project.

P0.3 is a design freeze. It does not assert that partitions already exist, that the firewall has been operationally tested, or that any result is validated.

## 2. Partition roles

| Partition | Permitted use | Prohibited use | Access state |
|---|---|---|---|
| Development | Hypothesis exploration; prompt/parser engineering; candidate AID generation; AlphaEvolve-inspired mutation/recombination; debugging; preliminary power and measurement work | Describing tuned results as validation or sealed OOS evidence | Available to authorized project operators after P5.5 assigns immutable observation IDs |
| Validation | One-way diagnosis of generalization; prespecified candidate comparison; calibration and stopping decisions defined before access | Iterative tuning followed by reuse of the same outcomes as untouched validation; feeding validation residuals/outcomes into candidate generation | Closed until development specifications and evaluation plan are versioned and hashed |
| Sealed test | Exactly the preregistered confirmatory analyses, negative controls, and economic tests | Any prompt, feature, construct, threshold, hypothesis, exclusion, model, parser, or specification selection; exploratory subgroup search; repeated opening | Sealed until explicit human approval and all opening conditions pass |

The Microsoft proof of concept is a demonstration environment, not the sealed confirmatory sample. It cannot establish external validity or the main JFE claim.

## 3. Partition construction and immutability

P5.5 must define the sampling frame, observation unit, time axis, eligibility rules, exclusions, assignment algorithm, random seed where applicable, temporal cutoffs, firm/entity separation, and minimum outcome-lag rules. The partition manifest must contain only immutable observation identifiers and metadata necessary to verify assignment; restricted values remain in their authorized location.

Each partition receives a manifest version and SHA-256 hash. Any change creates a new version, preserves the previous manifest and rationale, identifies affected outputs, and triggers the P0.4 amendment process. Records may not migrate from validation or sealed test back into development after outcomes or model judgments are viewed.

Preferred designs are genuinely prospective temporal holdouts and, where scientifically appropriate, firm/entity-disjoint holdouts. Random splitting is not a substitute when chronology, repeated firms, document overlap, or model-training-date contamination can leak information.

## 4. Frozen objects before validation access

Before validation is opened, the following must be versioned, hashed, and logged:

1. research question, estimand, hypothesis family, and direction where directional;
2. evidence inclusion/exclusion and timing rules;
3. prompt templates, scoring rubric, parsers, model registry, parameters, and retry policy;
4. candidate AID/consensus definitions and development-only selection objective;
5. preprocessing, missing-data, winsorization, fixed-effect, clustering, and control rules;
6. primary/secondary outcomes, evaluation metrics, rejection criteria, and multiplicity policy;
7. validation decision rule and stopping rule; and
8. code/environment version and expected output schema.

Validation may reveal that the frozen design performs poorly. Failure is recorded; it is not repaired by silently retuning on validation outcomes.

## 5. Validation one-way rule

Validation results flow only into a documented decision: retain, reject, or request a governed redesign. They may not flow directly into candidate mutation, prompt editing, variable selection, threshold search, subgroup search, or specification selection.

If a material redesign is approved, the used validation sample is reclassified as development history, all affected claims are quarantined, and a genuinely untouched replacement validation set must be designated and hashed before evaluation. The redesign receives a new protocol version and cannot preserve an “untouched validation” label for the used sample.

## 6. Sealed-test opening gate

The human principal investigator must explicitly approve opening. Before access, an opening record must show:

- P0.1–P0.5 governance controls complete or any limitation expressly accepted;
- P5.5 partition manifest frozen and hash verified;
- P6 prompt/model/scoring protocol frozen for the relevant experiment;
- P7 pair representation and P8 AID*/consensus definitions frozen where used;
- hypotheses, primary specifications, outcomes, metrics, negative controls, and multiplicity policy preregistered;
- code completes a dry run on synthetic or development-shaped data;
- development and validation decisions, deviations, and failures are logged;
- no unresolved dependency-critical blocker invalidates the confirmatory test; and
- approver, timestamp, protocol/manifest hashes, permitted analyses, and authorized operator recorded.

Opening is read-once in the scientific sense: the authorized analysis produces an immutable raw result bundle. Re-execution is permitted only for deterministic reproduction or a documented technical failure, never to search for a preferred result.

## 7. Technical and procedural controls

- Separate paths/namespaces: `data/development`, `data/validation`, and access-controlled `data/sealed_test`; public GitHub stores no restricted raw data.
- Development code must accept a partition parameter but default to development and refuse sealed-test execution without a verified approval record.
- Outcome columns unavailable for a stage must be physically withheld or masked, not merely ignored by convention.
- Logs record operator, timestamp, gate, code commit, environment, partition manifest/hash, input hashes, model/protocol versions, command, exit status, and output hash.
- Model prompts may include only evidence available by the prespecified information date; future filings, labels, prices, enforcement outcomes, and post-event summaries are forbidden.
- Caches, embeddings, retrieval indexes, feature stores, fine-tuning corpora, and human annotations inherit partition restrictions and must not bridge partitions.
- Human reviewers may not communicate sealed outcomes back to development selection. Their decisions are append-only and linked to evidence IDs.
- Generated model outputs count only when actually executed and logged; no imputation of unavailable model judgments as real observations.

These controls are specifications for later implementation and testing. Their existence in this document is not evidence that they are already enforced in code.

## 8. Leakage taxonomy and response

| Leakage class | Examples | Required response |
|---|---|---|
| Temporal | Post-filing data, future price/outcome, later restatement or enforcement text enters an earlier prediction | Stop analysis; quarantine affected observations/outputs; reconstruct as-of evidence; assess repartitioning |
| Entity/document | Same firm-period, amended filing, near-duplicate passage, or linked document crosses partitions | Quarantine; deduplicate/group-split; regenerate manifests and hashes through change control |
| Outcome/label | Outcome-derived feature, target encoding, reviewer knowledge, or outcome-aware prompt | Quarantine affected pipeline; remove contamination; require untouched replacement evaluation set |
| Model/pretraining | Model knowledge cutoff or training corpus may include future documents/outcomes | Record model cutoff uncertainty; use chronology-safe controls/older evidence; qualify or reject causal/predictive interpretation |
| Selection | Validation/test results change candidates, thresholds, hypotheses, exclusions, or reported subgroups | Reclassify used sample as development history; withdraw OOS claim; obtain new untouched evaluation data |
| Operational | Logs, filenames, caches, dashboards, or shared artifacts reveal sealed values | Revoke access; preserve incident record; rotate affected artifacts; assess full contamination scope |

Every suspected exposure creates a leakage incident ID. The incident record states discovery time, exposed objects/people/processes, evidence, containment, affected gates/claims, quarantine decision, repair action, and whether a new sample is required. Concealment or deletion of exposure history is prohibited.

## 9. AlphaEvolve- and Co-Scientist-specific boundary

Co-Scientist generation, criticism, novelty ranking, and AlphaEvolve-inspired mutation/recombination may use development evidence and development metrics only. Validation supplies a bounded one-way diagnostic under the frozen rule. Neither validation nor sealed-test residuals, rankings, errors, economic outcomes, or human commentary may enter the evolutionary objective, prompt context, memory, retrieval index, or candidate archive used for further selection.

The development objective must penalize complexity and record every evaluated candidate, including failed variants, to reduce undisclosed specification search. The winning AID* is frozen before confirmatory access.

## 10. Deviation and emergency rules

Technical failures are distinguished from scientific disappointment. A technical rerun is allowed only when the failure prevented the prespecified computation from completing and the original raw logs are preserved. A completed unfavorable or null result is not a technical failure.

Any material deviation requires a stable deviation ID, reason, discovery time, affected objects and claims, decision authority, repair/quarantine action, and prospective status. Post-test amendments are labeled post hoc and cannot restore confirmatory status.

Two persistent failed attempts on the same blocker trigger the OPEN REPAIR QUEUE and move-on rule. A dependency-critical firewall failure quarantines downstream validation/test claims and cannot be bypassed.

## 11. Machine-checkable minimum record

Every evaluation bundle must expose at least:

```yaml
experiment_id: string
partition: development|validation|sealed_test
partition_manifest_version: string
partition_manifest_sha256: string
protocol_version: string
protocol_sha256: string
code_commit: string
environment_lock_sha256: string
information_cutoff: ISO-8601
operator: string
human_approval_id: string|null
opened_at: ISO-8601|null
input_hashes: [string]
output_hashes: [string]
deviation_ids: [string]
leakage_incident_ids: [string]
```

For a sealed-test bundle, `human_approval_id`, `opened_at`, manifest/protocol hashes, code commit, and output hashes are mandatory and immutable.

## 12. Acceptance test and gate conclusion

P0.3 may be marked PASS only if the design specifies distinct partition purposes, immutable assignment/versioning, pre-validation frozen objects, one-way validation, human-controlled sealed opening, technical/logging controls, leakage taxonomy and response, evolutionary-search restrictions, deviation rules, and a machine-checkable evaluation record.

All design elements are present in v1.0. Therefore P0.3 is PASS for firewall design only. Operational enforcement, partition construction, access-control testing, and sealed-test execution remain future gates and must not be inferred from this PASS.
