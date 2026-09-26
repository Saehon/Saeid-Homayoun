# Prototype V1 Results — Microsoft Golden Anchor

**Maturity:** `RESEARCH_PROTOTYPE`  
**Run date:** 2026-09-16  
**Production readiness:** NO  
**Independent replication:** NOT YET

## Dedicated 15-test validation run

The unified Microsoft V1 artifact-validation harness now executes all 15 contract tests:

```text
pytest -q tests/test_microsoft_poc_v1_15_contract.py
...............                                                          [100%]
15 passed in 0.08s
```

See [`VALIDATION_RUN_15_TESTS_2026_09_16.md`](./VALIDATION_RUN_15_TESTS_2026_09_16.md) and [`VALIDATION_MATRIX_15_TESTS.md`](./VALIDATION_MATRIX_15_TESTS.md).

| Contract test | Result |
|---|---|
| SEC/XBRL ingestion | **PASS** |
| Financial statement extraction | **PASS** |
| Variable dictionary validation | **PASS** |
| Evidence Passport generation | **PASS** |
| CAM/audit-risk mapping | **PASS** |
| Text analytics | **PASS** |
| Finance calculation | **PASS** |
| Innovation measure | **PASS** |
| ABC calculation | **PASS — synthetic** |
| TDABC calculation | **PASS — synthetic** |
| AI token/cost calculation | **PASS — synthetic** |
| Model benchmark | **PASS — external benchmark** |
| Human–AI experiment structure | **PASS STRUCTURE / PARTICIPANTS NOT RUN** |
| Dashboard data-load reconciliation | **PASS** |
| Human Gate decision | **PASS FOR RESEARCH-PROTOTYPE PUBLICATION ONLY** |

**Unified harness result: 15/15 PASS.**

This closes the former TEST 03 and TEST 14 automation gaps. It does not convert the actual participant experiment, Fama–French regression, PatentsView analysis, professional-task model benchmark, falsification program, or independent replication into PASS.

## Selected numerical results

- Revenue growth: **17.75%**
- Operating margin: **46.78%**
- Net margin: **40.31%**
- Current ratio: **1.230**
- Liabilities/assets: **41.67%**
- R&D intensity: **10.72%**
- FCF proxy: **$66,987m**
- FCF margin: **20.19%**
- FY2026 MSFT simple price return (IEX close-to-close, no dividends): **-24.22%**
- DGS10 at 2026-06-30: **4.44%**
- Illustrative DGS10 + mature-market ERP proxy: **8.64% (NOT Microsoft WACC)**

## Audit / CAM / ICFR

- Revenue Recognition CAM mapped to assertions, risk, procedures, evidence and judgment.
- Uncertain Tax Positions CAM mapped to valuation/completeness/presentation, transfer-pricing risk and specialist procedures.
- FY2026 ICFR auditor opinion: **unqualified**.

## Scientific boundary

The 15/15 result validates the bounded public artifact package. The broader Microsoft V1 scientific success gate remains **NOT PASSED** because these items remain open:

- actual T0–T3 participant experiment;
- Microsoft Fama–French factor regression;
- aggregate PatentsView patent/citation/technology-diversity measures;
- NAAIL-specific professional-task model pass-rate / Cost per Verified Professional Output™;
- independent cross-source and reviewer replication;
- remaining falsification/robustness challenges;
- fuller rights-cleared raw-filing text workflow.

The formal falsification register remains [`FALSIFICATION_ROBUSTNESS_REGISTER.md`](./FALSIFICATION_ROBUSTNESS_REGISTER.md).

## CI boundary

A dedicated GitHub Actions workflow has been published at `.github/workflows/microsoft_poc_v1_15_test.yml`. The local bounded run above is executed and documented. **GitHub Actions CI success is not claimed until a completed workflow run is separately verified.**

## Human Gate

**APPROVE_RESEARCH_PROTOTYPE_FOR_PUBLICATION_WITH_LIMITATIONS**

Production approval remains **NO**. Scientific validation remains **PENDING_INDEPENDENT_REPLICATION**.

**Final maturity status: `RESEARCH_PROTOTYPE`.**
