# Benchmark V3 holdout specification — V1 preparation

Status: **FROZEN OPERATOR SPECIFICATION — PENDING CLAUDE AND HUMAN APPROVAL**

This document freezes the protocol before any V3 probe, ground-truth label, detector output, or score exists. It authorizes no data retrieval, case selection, probe authorship, scoring run, scientific claim, or gate approval.

## Independence firewall

The operator has seen the detector, its rules, the Benchmark V2 results, and the nine disclosed V2 probes. The operator is therefore permanently ineligible to author, edit, suggest, preview, or approve V3 probes or ground truth.

The holdout must be authored by a human or separate agent with no access to:

- detector source code, rules, prompts, or implementation discussions;
- Benchmark V2 probe content or expected outputs;
- detector outputs before sealing; or
- operator suggestions about probe construction.

The independent author must sign the four attestations in the machine-readable specification. Any failed attestation disqualifies the holdout.

## Frozen composition

V3 contains 48 packages:

- 32 error-bearing packages: four in each of eight design strata;
- 16 clean controls.

The eight strata are provenance integrity, numeric/result consistency, code/output consistency, temporal leakage, sample/missingness, methodological overclaim, reproducibility/environment, and compound cross-artifact errors. These are allocation strata only; they are not probe examples or construction instructions.

## Seal-before-score sequence

1. The independent author finalizes separate probe and ground-truth archives.
2. The author hashes each archive and every contained file with SHA-256.
3. A manifest records filenames, sizes, hashes, category counts, authorship attestation, and creation time.
4. The manifest and sealed artifacts are frozen before the operator receives test-time access.
5. Claude checks the manifest, attestation, counts, and hashes.
6. At test time, the operator runs the frozen detector once on the frozen probes.
7. Raw detector outputs are immediately hashed and committed.
8. Ground truth is released only after that raw-output commit.
9. The frozen scorer runs once and the complete result is preserved.

No probe, label, rule, threshold, or metric may change after any detector output is observed.

## Frozen scoring

The primary unit is the package. The primary endpoint is binary detection of whether a package contains at least one planted error.

Primary metrics are TP, FP, FN, TN, precision, recall, F1, and false-positive rate. Secondary metrics are category recall, exact-category match, human-review escalation, and unsupported-claim rate. Wilson 95% confidence intervals accompany binomial proportions.

The proposed decision rule is conjunctive:

- precision at least 0.80;
- recall at least 0.75;
- F1 at least 0.75; and
- false-positive rate at most 0.10.

Undefined metrics remain null with an explanation. Missing or unreadable packages are reported and count as scored failures; they are never silently excluded. Category results remain visible regardless of the aggregate outcome.

## One-run rule

There is one authoritative scoring run. A technical abort is possible only when no detector output or score was emitted. A replacement attempt requires explicit Claude and human authorization and must preserve the abort evidence. Results are reported as observed; no rerun, tuning, probe deletion, or result substitution is allowed.

## Activation boundary

V3 execution remains locked until all of the following are present:

1. human POC approval;
2. Claude approval of this specification;
3. documented independent authorship; and
4. hashed, frozen probe and ground-truth artifacts.

Until then, this is a V1-preparation governance artifact only.
