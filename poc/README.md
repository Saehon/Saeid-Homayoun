# ECONOVA-S™ Proof of Concept — POC-001

This runnable POC converts the ECONOVA-S architecture into an auditable research pipeline around the mechanism:

**Data Capability → Green Innovation → Firm Value → Social Data Value**

It demonstrates the **Stable Economic Knowledge Core™**, **Replaceable Technology Core™**, and the supporting **AI-to-AI Scientific Intelligence Fabric™** without adding a third core.

### Included scientific controls

- causal-mechanism governance and three explicit hypotheses;
- Co-Scientist-style deterministic hypothesis ranking;
- ERA-style empirical specifications;
- firm/year fixed-effect regressions with firm-clustered standard errors;
- AlphaEvolve-inspired specification tournament using a frozen fitness rule;
- chronological 2020–2024 training / 2025 out-of-sample evaluation;
- adversarial placebo/sign checks;
- FT50-style Tables 2–6;
- Evidence Passport™;
- Human Gate with `discovery_claim_allowed = false`.

The first POC uses deterministic **synthetic** firm-year data (20 firms × 6 years) so the repository is reproducible and does not redistribute proprietary datasets. It is demonstration evidence only, not empirical support for the hypotheses.

## Run

```bash
cd poc
python -m pip install -r requirements.txt
python econova_poc.py
pytest -q
```

Generated files appear under `poc/results/`:
`demo_firm_year.csv`, `table2_descriptives.csv`, `table3_correlations.csv`,
`table4_main_regressions.csv`, `table5_robustness_falsification.csv`,
`table6_model_tournament_oos.csv`, `hypothesis_tournament.csv`, and
`evidence_passport.json`.

To use a real dataset:

```bash
python econova_poc.py --data path/to/firm_year.csv --out results_real
```

The required schema is visible in `generate_demo()` inside the script.

### Scientific status

The POC models are **associational**. No causal or scientific-discovery claim is allowed until relevant FT50/AJG/ABS 4*/4 literature validation, real-data provenance, construct validation, credible identification, external replication, falsification, economic significance, welfare interpretation, and human approval are complete.

### Model fitness

The specification tournament uses:

`Fitness = 2025 OOS RMSE + complexity penalty + expected-sign violation penalty`

It deliberately does **not** optimize p-values.

### IP

This POC is governed by the repository ECONOVA-S™ Research and Non-Commercial License. Commercial use requires prior written permission and a separate commercial license.
