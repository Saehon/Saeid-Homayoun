# KIWI™ AAR Corp CAM Unit Test

**One-company proof-of-mechanism for Critical Audit Matter measurement and attention reallocation.**

This public demo intentionally uses **AAR Corp only**. It is the permanent unit-test company for the KIWI™ CAM research program before any model is allowed to scale to a multi-company U.S. CAM sample.

## Research question

Can CAM disclosures reveal how professional audit attention is reallocated across competing risks even when the total number of CAMs does not change?

For AAR Corp, the observed CAM sequence is:

| Year | CAM 1 | CAM 2 |
|---|---|---|
| 2020 | Inventory | Revenue |
| 2021 | Inventory | Revenue |
| 2022 | Inventory | Revenue |
| 2023 | Inventory | Revenue |
| 2024 | Inventory | Acquired Intangibles / Business Combination |

The central 2024 pattern is therefore:

```text
Revenue -> EXIT
Acquired Intangibles / Business Combination -> ENTRY
Inventory -> PERSIST
CAM_COUNT -> unchanged at 2
CARS -> 0.667
```

**CAM quantity is unchanged, but CAM composition changes sharply.**

## Why only AAR Corp

AAR is used as a measurement-development, falsification, temporal-structure, and proof-of-mechanism case. Five company-years are **not** sufficient for credible company-year OLS, fixed effects, DiD, or population-level causal inference.

This repository should therefore pass before any larger KIWI CAM model is treated as research-ready.

## Source and public/private boundary

The private research source is `AAR_CORP_CAM_EMPIRICAL_PROTOTYPE.xlsx`, built from the licensed/controlled CAM source dataset and retained in the research Drive environment.

The source workbook contains three linked empirical levels:

1. `CAM_LEVEL` — 10 AAR CAM observations;
2. `COMPANY_YEAR` — 5 AAR company-years;
3. `CAM_TOPIC_YEAR` — topic transition structure.

The public GitHub demo does **not** publish the complete underlying CAM descriptions and auditor responses. It publishes only the metadata, derived measures, transformation tables, code, and validation summaries needed to reproduce the unit-test logic.

## Files

- `aar_cam_public_extract.csv` — 10 CAM metadata rows, 2020–2024.
- `aar_company_year.csv` — one row per AAR company-year.
- `aar_cam_frozen_results.csv` — frozen RPA/EDS/SIS/SQI/CIIS/CARS pilot results.
- `aar_cam_unit_test.py` — executable validation and robustness runner.
- `test_aar_cam_unit_test.py` — regression tests for the frozen AAR pattern.

## Frozen constructs

### RPA — Risk–Procedure Alignment
Measures whether disclosed audit procedures structurally address the risks and assumptions identified in the CAM.

### EDS — Evidence Depth Score
Seven evidence/procedure categories are used in the pilot:

1. internal-control testing;
2. IT-control testing;
3. external/market/industry evidence;
4. historical validation;
5. specialist involvement;
6. sensitivity analysis;
7. sampling/supporting-document testing.

### SIS — Structural Integrity Score
Represents the connected structure:

`Risk -> Assumption/Judgment -> Procedure -> Evidence -> Financial-statement reference`

### SQI — CAM Structural Quality Index

```text
SQI = 100 x (0.50 RPA + 0.30 EDS + 0.20 SIS)
```

**SQI is a CAM communication/structural-quality measure. It is not an audit-quality score.**

### CIIS — CAM Incremental Information Score
For recurring topics:

```text
CIIS(j,t) = 1 - cosine_similarity(CAM(j,t), CAM(j,t-1))
```

For a newly entering topic, CIIS remains missing and `NEW_TOPIC = 1` is used instead.

### CARS — CAM Attention Reallocation Score

```text
CARS(t) = 1 - |CAM(t) intersect CAM(t-1)| / |CAM(t) union CAM(t-1)|
```

For AAR:

- 2020–2021: 0
- 2021–2022: 0
- 2022–2023: 0
- 2023–2024: **0.667**

## Frozen AAR pilot result

The 2024 Acquired Intangibles CAM is the structurally strongest CAM in the frozen pilot (`SQI = 90.1`, `EDS = 0.857`). Inventory remains persistent and structurally strong. Revenue exits in 2024.

Recurring Inventory and Revenue CAMs become highly textually stable by 2022–2023, supporting the distinction between **structural quality** and **incremental information**.

## Falsification architecture

The AAR pilot retains the following frozen validation logic:

- correct auditor response vs same-year swapped response: correct alignment wins in all 5 years;
- year is the independent unit, giving exact one-sided sign-test `p = 0.03125`;
- average reported correct SQI approximately `78.6` vs wrong-response SQI approximately `35.1`;
- removing the audit response reduces reported average structural quality from about `78.6` to `7.9`;
- history-only prediction of the new 2024 acquisition CAM is **rejected** because the risk does not exist in prior AAR CAM history.

That last rejection is a scientific safeguard against look-ahead bias, not a model failure to be hidden.

## Run

Python 3.11+; no third-party packages required.

```bash
cd NAAIL-OpenLab/demos/aar-cam-unit-test
python aar_cam_unit_test.py
```

Run regression tests:

```bash
python -m unittest test_aar_cam_unit_test.py
```

The runner writes `aar_cam_unit_test_results.json` and reports:

- frozen structure PASS/FAIL;
- 2024 CAM entry/exit/persistence;
- CARS;
- exact year-level sign-test p-value;
- positive-weight robustness of the structural ranking;
- explicit scientific non-claims.

## Mandatory scientific boundary

This AAR case supports **measurement development and proof of mechanism only**. It does not establish population causality, audit quality, investor usefulness, or regulatory effectiveness.

Any future KIWI CAM model should reproduce this AAR benchmark before scaling to the full U.S. CAM population.

## Research identity

**Saeid Homayoun**  
NAAIL OpenLab / KIWI™ CAM research program  
ORCID: 0000-0002-2536-0446
