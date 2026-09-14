# ECONOVA-S™ Reproducibility Contract

ECONOVA-S treats reproducibility as a first-class scientific requirement rather than a final packaging step.

## Minimum reproducibility record

A publication-grade run should preserve:

1. **Research question and frozen hypothesis**
2. **Data provenance** — authoritative source, retrieval date, version/release and source URL
3. **Source fingerprints** — SHA-256 or equivalent where practical
4. **Information chronology** — when each datum became observable to the researcher/market
5. **Variable DNA™** — concept, formula, unit, source, timing, transformations and missingness
6. **Code version** — repository commit SHA
7. **Environment** — Python/R/Stata versions and dependency versions
8. **Model/tool versions** — including LLM/backend identifiers when used
9. **Random seeds** — whenever stochastic components exist
10. **Estimand and identification class**
11. **Primary specification and frozen thresholds**
12. **Robustness/falsification tests**
13. **Replication/OOS protocol**
14. **Red-team findings**
15. **Evidence Passport™**
16. **Human scientific decision**

## Source hierarchy

Prefer official sources over mirrors. For the current public stack:

1. Kenneth R. French Data Library
2. SEC EDGAR / XBRL CompanyFacts
3. Aswath Damodaran / NYU Stern
4. Other authoritative/public sources documented per study
5. GitHub/Kaggle mirrors only as secondary replication aids when appropriate

## Chronology rule

A variable must not enter an empirical design before it was observable at the study's information date.

For SEC data, the relevant control is generally the filing date, not merely the fiscal-period end date. For archived asset-pricing data, the exact archive/release snapshot must be preserved when studying data-construction changes.

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

Where model/specification search is used, ECONOVA-S should separate:

- **DiscoverySystem** — proposes candidate measures/models/specifications;
- **ValidationSystem** — evaluates them using frozen criteria and untouched/held-out evidence where feasible.

The validation process must not be optimized solely for statistical significance.

## Re-running the flagship study

```bash
cd studies/MNSc-FamaFrench-01
pip install -r requirements.txt
pytest -q
python run_study.py --old 2024 --new 2025 --output artifacts
```

A valid run should regenerate Tables 1–6 plus the Evidence Passport and summary from official archive inputs.

## Publication boundary

Reproducibility does not by itself imply causal validity or scientific discovery. A reproduced associational result remains associational unless the Identification Gate is separately satisfied.
