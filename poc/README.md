# ECONOVA-S™ Proof of Concept — POC-001

This runnable POC converts the ECONOVA-S architecture into an auditable research pipeline around the illustrative mechanism:

**Data Capability → Green Innovation → Firm Value → Social Data Value**

It demonstrates the **Stable Economic Knowledge Core™**, **Replaceable Technology Core™**, and the supporting **AI-to-AI Scientific Intelligence Fabric™** without adding a third core.

## Validation status

POC-001 has been executed end-to-end in a clean local validation run. The pipeline generated the full research-output package and the automated test suite passed **2/2 tests**. The Evidence Passport correctly preserves `discovery_claim_allowed = false`, demonstrating that the Human Gate prevents a synthetic-data demonstration from being mislabeled as a scientific discovery.

The current POC uses deterministic **synthetic** firm-year data (20 firms × 6 years, 2020–2025). It establishes **computational feasibility, reproducibility, and scientific-governance feasibility** only. It does not provide empirical support for the economic hypotheses.

## Included scientific controls

- systems/mechanism map and three explicit hypotheses;
- Co-Scientist-style deterministic hypothesis ranking;
- ERA-style empirical specifications;
- firm/year fixed-effect regressions with firm-clustered standard errors;
- AlphaEvolve-inspired specification tournament using a frozen fitness rule;
- chronological 2020–2024 training / 2025 out-of-sample evaluation;
- adversarial placebo and expected-sign checks;
- FT50-style Tables 2–6;
- Evidence Passport™;
- Human Gate with `discovery_claim_allowed = false`.

## Run

```bash
cd poc
python -m pip install -r requirements.txt
python econova_poc.py
pytest -q
```

Generated files appear under `poc/results/`:

- `demo_firm_year.csv`
- `table2_descriptives.csv`
- `table3_correlations.csv`
- `table4_main_regressions.csv`
- `table5_robustness_falsification.csv`
- `table6_model_tournament_oos.csv`
- `hypothesis_tournament.csv`
- `evidence_passport.json`

To use a real dataset:

```bash
python econova_poc.py --data path/to/firm_year.csv --out results_real
```

The required schema is visible in `generate_demo()` inside the script.

## Scientific status

The POC models are **associational**. No causal or scientific-discovery claim is allowed until relevant FT50/AJG/ABS 4*/4 literature validation, real-data provenance, construct validation, credible identification, independent or external replication, falsification, economic significance, welfare interpretation, and human approval are complete.

The correct interpretation is:

**POC-001 proves that the ECONOVA-S architecture can execute the governed scientific workflow; it does not prove that the illustrative economic mechanism is true.**

## Model fitness

The specification tournament uses:

`Fitness = 2025 OOS RMSE + complexity penalty + expected-sign violation penalty`

It deliberately does **not** optimize p-values.

## Next stage — POC-002

POC-002 should replace the synthetic panel with real public or properly licensed economic/financial data while preserving the same two-core architecture and scientific gates. The real-data stage should add construct validation, provenance manifests, literature-linked Variable DNA™, stronger identification where justified, independent replication, and external/out-of-sample validation.

## IP

This POC is governed by the repository ECONOVA-S™ Research and Non-Commercial License. Commercial use requires prior written permission and a separate commercial license.
