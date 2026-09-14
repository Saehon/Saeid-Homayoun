# ECONOVA-S™ Quick Start

This guide gives the shortest reproducible path from cloning the repository to running the first real-data study.

## 1. Clone

```bash
git clone https://github.com/Saehon/Saeid-Homayoun.git
cd Saeid-Homayoun
```

## 2. Run the flagship real-data study

```bash
cd studies/MNSc-FamaFrench-01
python -m venv .venv
```

Activate the environment:

**Windows**
```powershell
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install and test:

```bash
pip install -r requirements.txt
pytest -q
```

Execute the official July 2024 vs July 2025 archive comparison:

```bash
python run_study.py --old 2024 --new 2025 --output artifacts
```

## 3. Expected outputs

The `artifacts/` directory should contain:

- `table1_variable_dna.csv`
- `table2_descriptives.csv`
- `table3_dcs.csv`
- `table4_alpha_models.csv`
- `table5_conclusion_reversals.csv`
- `table6_subperiod_robustness.csv`
- `evidence_passport.json`
- `RUN_SUMMARY.md`

The run also records source hashes inside the Evidence Passport.

## 4. Interpret correctly

A successful run demonstrates reproducibility and measurement-change sensitivity. It does **not** by itself establish a causal explanation for FIZ→CIZ differences or authorize a scientific-discovery claim.

```text
discovery_claim_allowed = false
```

## 5. Explore the workbench

For the GPT-backed research-design/econometrics prototype:

```bash
cd ../../prototype_v02
python -m venv .venv
# activate the environment
pip install -r requirements.txt
streamlit run app.py
```

Set your own API key through environment variables or a local `.env` file. Never commit secrets.

## 6. Read before extending

- [`ARCHITECTURE.md`](../ARCHITECTURE.md) — two-core scientific architecture
- [`SCIENTIFIC_ASSURANCE.md`](../SCIENTIFIC_ASSURANCE.md) — claim classes and scientific gates
- [`DATA_SOURCES.md`](../DATA_SOURCES.md) — provenance and authoritative-source policy
- [`REPRODUCIBILITY.md`](../REPRODUCIBILITY.md) — reproducibility contract
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — contribution rules
