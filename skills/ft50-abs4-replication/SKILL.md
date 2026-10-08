---
name: ft50-abs4-replication
description: Use for FT50, AJG 4-star, ABS4, or leading accounting and finance journal positioning; empirical contribution audits; replication and robustness gates; evidence matrices; manuscript, appendix, reviewer-response, and submission packages. Use when a project needs defensible novelty, journal fit, reproducible results, or a repair plan grounded in the closest literature.
---

# FT50 / ABS4 Replication

## Purpose

Turn an accounting, auditing, finance, or management manuscript into a traceable journal-positioning and replication package. Keep four questions separate: Is the contribution genuinely new? Is the design identified? Can the result be reproduced? Is the target journal a credible fit? This skill does not promise acceptance or infer a journal decision from a ranking.

## Operating contract

- Freeze the target journal set before comparing papers. Record the ranking source, version/date, field, and whether “FT50,” “AJG 4/4*,” “ABS4,” or another list is being used.
- Treat claims as `observed`, `computed`, `inferred`, `proposed`, or `unverified`. Never describe a paper as FT50/ABS4 without checking the current source or a user-provided list.
- Prefer the closest design and outcome comparators over a long prestige-only bibliography.
- Treat replication as an executable gate. A citation, repository URL, or high R-squared is not replication evidence.
- Preserve the user’s original files and write repairs, cleaned versions, and manifests as new artifacts.

## Workflow

### 1. Freeze scope and contribution

Write a one-paragraph study card:

`question → setting/sample → treatment or signal → outcome → identification → main result → claimed contribution → target journals`.

Separate contribution types: new theory, new measurement, new institutional setting, new identification, new data, new prediction/decision use, or new boundary condition. Flag relabeling and “same result, new name” risks.

### 2. Build the evidence matrix

For each closest paper, extract only evidence that can be checked:

`paper | journal/year | theory | setting | population/sample | treatment/signal | outcome | identification | key controls | validation/robustness | code/data status | key result | limitation | relation to this study | source location/date`.

Use a separate journal-fit table with `scope`, `method fit`, `audience`, `closest precedent`, `contribution gap`, `data/length constraints`, and `risks`. Do not turn a ranking into a fit judgment.

### 3. Run the replication gate

Classify every claimed result as one of:

- `R0 — not runnable`: no code/data or access is unresolved.
- `R1 — package inspected`: files, license, environment, and entry point are mapped.
- `R2 — executed`: the stated pipeline runs on the stated sample or a documented substitute.
- `R3 — matched`: primary estimates and material tables/figures match within pre-specified tolerances.
- `R4 — stress-tested`: alternative specifications, sample restrictions, leakage checks, and negative/placebo tests are documented.

Record the exact commit/file versions, environment, sample counts, variable mapping, seeds, failures, tolerances, and unresolved discrepancies. Never promote an R0/R1 result to “replicated.”

### 4. Audit design before polishing prose

Check timing and identification first: point-in-time information, pre-treatment variables, selection, missingness, survivorship, measurement error, multiple testing, clustered uncertainty, and whether a predictive claim is being written as a causal claim. Require a temporal split or leakage test for prediction. Use a pre-results analysis plan when feasible; clearly label exploratory branches.

### 5. Use project-specific defaults

- **ICFR / SEC / SEFD prediction:** report prevalence, temporal holdout, PR-AUC, Brier score/calibration, recall at a review-budget `k`, confusion costs, and an auditability or decision-use section. Do not rely on accuracy alone.
- **Risk–CAM alignment:** separate the selection equation (why an item is disclosed) from the outcome equation (what happens afterward); preserve the unit of analysis and the information set at the prediction date.
- **FT50/AJG4 positioning:** compare against the nearest accepted or published design, not only broad field labels. State what the paper enables that the comparator cannot.
- **Replications:** distinguish exact, conceptual, and registered replication; report changed institutions, periods, measures, and power rather than hiding them in an appendix.

### 6. Package for reviewers and submission

Produce a compact package with:

1. evidence matrix and journal-fit table;
2. contribution paragraph with comparator citations;
3. replication ledger and run instructions;
4. main/appendix mapping and robustness decision log;
5. data/code availability, license, and confidential-data plan;
6. reviewer-response table: `comment → evidence → change → location → remaining limitation`.

Keep a “not done” list. A clean submission package states what could not be verified.

## Quality checks

Before delivery, verify that the manuscript, tables, code, data dictionary, and archive manifest agree on sample, dates, variable names, estimands, and file versions. Check that every strong novelty or journal-fit sentence has a source or is labeled as an inference. Re-run the minimum pipeline after any material change.

## Reference

Use `references/replication-gate.md` for the short gate checklist and status vocabulary.
