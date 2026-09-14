# ECONOVA-S™ Reproducibility Contract

ECONOVA-S™ treats reproducibility as a first-class scientific requirement rather than a final packaging step.

## Minimum reproducibility record

A publication-grade run should preserve:

1. **Research question and research goal**
2. **Literature grounding record** — verified sources, competing explanations, contradictory evidence
3. **Hypothesis tournament** — generated candidates, critiques, ranking criteria, selected/rejected candidates
4. **Causal DAG / systems map**
5. **Data provenance** — authoritative source, retrieval date, version/release and source URL
6. **Source fingerprints** — SHA-256 or equivalent where practical
7. **Information chronology** — when each datum became observable to the researcher/market
8. **Variable DNA™** — concept, formula, unit, source, timing, transformations and missingness
9. **Empirical manifest** — estimand, model, sample, metrics, robustness/falsification plan
10. **Code version** — repository commit SHA
11. **Environment** — Python/R/Stata versions and dependency versions
12. **Model/tool versions** — including LLM/backend identifiers when used
13. **Random seeds** — whenever stochastic components exist
14. **Primary specification and frozen thresholds**
15. **Discovery-search lineage** — candidates, evaluators, parent-child lineage and scores when search/evolution is used
16. **Holdout boundary** — evidence not exposed to the generator where feasible
17. **Latent-structure record** — method, interpretation, baseline, stability and OOS/external validation when used
18. **Robustness/falsification tests**
19. **Replication/OOS protocol and report**
20. **AI-to-AI red-team findings**
21. **Chain-of-Evidence** — claim-to-evidence links
22. **CoE Audit** — reference, result, specification and method-code integrity checks
23. **Evidence Passport™**
24. **Human scientific decision**

## Canonical study package

Publication-grade studies should aim to preserve:

```text
01_RESEARCH_GOAL.md
02_LITERATURE_GROUNDING.md
03_HYPOTHESIS_TOURNAMENT.json
04_CAUSAL_DAG.md
05_VARIABLE_DNA.csv
06_EMPIRICAL_MANIFEST.json
07_DISCOVERY_SEARCH.json
08_LATENT_STRUCTURE.md
09_REPLICATION_REPORT.md
10_RED_TEAM_REPORT.md
11_FALSIFICATION_REPORT.md
12_CHAIN_OF_EVIDENCE.json
13_COE_AUDIT.json
14_EVIDENCE_PASSPORT.json
15_HUMAN_GATE.md
```

Use [`templates/STUDY_DISCOVERY_TEMPLATE.md`](templates/STUDY_DISCOVERY_TEMPLATE.md) as the human-readable checklist.

## Source hierarchy

Prefer official sources over mirrors. For the current public stack:

1. Kenneth R. French Data Library
2. SEC EDGAR / XBRL CompanyFacts
3. Aswath Damodaran / NYU Stern
4. Other authoritative/public sources documented per study
5. GitHub/Kaggle mirrors only as secondary replication aids when appropriate

## Literature verification rule

Important citations should be retrieved or verified from scholarly/authoritative sources rather than produced from model memory alone. A reference used in a final claim must be traceable through the Chain-of-Evidence.

## Chronology rule

A variable must not enter an empirical design before it was observable at the study's information date.

For SEC data, the relevant control is generally the filing date, not merely the fiscal-period end date. For archived asset-pricing data, the exact archive/release snapshot must be preserved when studying data-construction changes.

## Hypothesis-search reproducibility

For Co-Scientist-style workflows, preserve:

- candidate hypotheses;
- agent role/function;
- critique text or structured critique;
- frozen ranking dimensions;
- pairwise/tournament results where used;
- evolution/revision lineage;
- meta-review;
- final human selection.

Agent ranking is part of the search record, not independent validation.

## ERA-style empirical reproducibility

The hypothesis-to-test conversion must preserve:

- data source;
- executable code;
- exact variable definitions;
- estimand;
- evaluation metrics;
- expected failure modes;
- robustness/falsification design;
- replication/OOS design.

A prose-only empirical plan does not satisfy this requirement.

## AlphaEvolve / Computational Discovery reproducibility

Where scientific search is used, record:

- search object;
- initial candidates;
- mutation/evolution logic;
- automated evaluator definition;
- frozen scientific fitness;
- raw evaluator outputs;
- candidate lineage;
- rejected candidates;
- exploration/exploitation policy;
- validation/holdout boundary.

Do not optimize solely for p-values.

## AlphaFold-inspired latent-structure reproducibility

When hidden structures are inferred, preserve:

- latent variable/factor/network/regime definition;
- estimation method;
- initialization/seeds;
- simpler baseline;
- economic interpretation;
- stability/sensitivity tests;
- external/OOS validation where feasible.

## Science One Chain-of-Evidence reproducibility

Every material claim should point to its evidence artifact. The chain should support both:

- **completeness** — material claims are covered;
- **correctness** — evidence supports what the claim says.

A publication package should make it possible to reconstruct the path:

`Claim → Source/Data/Code → Execution → Result → Verification → Interpretation`

## CoE Audit reproducibility

Archive the outcome of:

- reference verification;
- score/result re-execution;
- specification-integrity check;
- method-code alignment check;
- claim-evidence alignment check.

Failed checks are retained; they are not overwritten by later narrative edits.

## Environment capture

For Python studies, create a frozen dependency record after a successful run:

```bash
python --version
pip freeze > artifacts/requirements-lock.txt
```

For Stata, R or other tools, record software versions and package/library versions in the run manifest.

## Commit capture

Before archiving a result, record the Git commit used to generate it:

```bash
git rev-parse HEAD
```

Store the SHA in the Evidence Passport or run manifest.

## Discovery vs validation separation

Where model/specification search is used, ECONOVA-S™ should separate:

- **DiscoverySystem** — proposes candidate measures/models/specifications;
- **ValidationSystem** — evaluates them using frozen criteria and untouched/held-out evidence where feasible.

The validation process must not be optimized solely for statistical significance.

## Machine validation

Run:

```bash
python discovery/validate_study_manifest.py discovery/sample_study_manifest.json
python -m pytest -q discovery/test_discovery_manifest.py
```

The current sample manifest is expected to validate while preserving:

```text
discovery_claim_allowed = false
```

## Re-running the flagship study

```bash
cd studies/MNSc-FamaFrench-01
pip install -r requirements.txt
pytest -q
python run_study.py --old 2024 --new 2025 --output artifacts
```

A valid run should regenerate Tables 1–6 plus the Evidence Passport and summary from official archive inputs.

## Publication boundary

Reproducibility does not by itself imply causal validity or scientific discovery. A reproduced associational result remains associational unless the Identification Gate is separately satisfied. Agent consensus, search performance, or evaluator score does not waive this boundary.
