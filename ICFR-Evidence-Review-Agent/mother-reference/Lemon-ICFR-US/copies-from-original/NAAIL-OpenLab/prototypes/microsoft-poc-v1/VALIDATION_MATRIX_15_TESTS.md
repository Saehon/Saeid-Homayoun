# Microsoft POC V1 — 15-Test Validation Matrix

**Contract version:** upgraded 2026-09-16  
**Execution date:** 2026-09-16  
**Maturity:** `RESEARCH_PROTOTYPE`

## Dedicated unified harness result

The current Microsoft V1 package now includes and has executed:

`tests/test_microsoft_poc_v1_15_contract.py`

Bounded execution result:

```text
...............                                                          [100%]
15 passed in 0.08s
```

| Test | Required test | Status | Executed evidence / boundary |
|---|---|---|---|
| TEST 01 | SEC/XBRL ingestion | **PASS** | Validates Microsoft CIK, required R2/R4/R6/R107 reports and executed SEC Evidence Passport source/provenance. |
| TEST 02 | Financial statement extraction | **PASS** | Reconciles required FY2026 facts in the Digital Twin to the financial feature artifact. |
| TEST 03 | Variable dictionary validation | **PASS** | Validates required columns, non-empty metadata, uniqueness, required variable coverage and source-ID registration. |
| TEST 04 | Evidence Passport generation | **PASS** | Validates required schema fields, rights gate, human review status and transformation metadata. |
| TEST 05 | CAM/audit-risk mapping | **PASS** | Validates auditor, unqualified ICFR opinion, two CAM topics and non-empty account/assertion/risk/procedure/evidence/judgment fields. |
| TEST 06 | Text analytics | **PASS** | Validates two bounded-source outputs, execution status, positive text counts, SEC URLs and 64-character sample hashes. |
| TEST 07 | Finance calculation | **PASS** | Recomputes FCF, price return and current ratio and validates DGS10 snapshot. Fama–French regression remains a separate open scientific gate. |
| TEST 08 | Innovation measure | **PASS** | Recomputes R&D intensity and validates executed GitHub research indicators while preserving PatentsView as NOT EXECUTED. |
| TEST 09 | ABC calculation | **PASS** | Validates the declared synthetic Microsoft-like activity set and reconciles activity tool-cost allocation to the total. |
| TEST 10 | TDABC calculation | **PASS** | Recomputes each activity TDABC human cost from capacity cost rate × human minutes and reconciles the total. |
| TEST 11 | AI token/cost calculation | **PASS** | Reconciles input/output token totals and tool cost to the Digital Twin totals. |
| TEST 12 | Model benchmark | **PASS** | Validates LiveBench release label, positive scores/costs and external-benchmark cost status. |
| TEST 13 | Human–AI experiment structure | **PASS** | Validates T0–T3 structure and `DESIGN_COMPLETE_NOT_EXECUTED`; this does not mean participants have been run. |
| TEST 14 | Dashboard data load | **PASS** | Reconciles headline dashboard values to the current Digital Twin financial/finance state. |
| TEST 15 | Human Gate decision | **PASS** | Validates publication-only approval boundary, production approval NO and scientific validation pending independent replication. |

## Executed contract summary

- Dedicated artifact-validation harness: **15 / 15 PASS**
- `NOT EXECUTED` within the 15-test artifact harness: **0 / 15**
- `FAIL`: **0 / 15**
- `BLOCKED`: **0 / 15**

## Scientific success-gate distinction

The 15/15 result validates the bounded public artifact package and closes the former TEST 03 / TEST 14 automation gaps. It does **not** convert broader unexecuted scientific work into PASS.

Still open:

- actual T0–T3 participant experiment;
- Microsoft Fama–French factor regression;
- aggregate PatentsView patent/citation/technology-diversity analysis;
- NAAIL-specific professional-task model verification / Cost per Verified Professional Output™;
- independent cross-source and reviewer replication;
- remaining falsification/robustness challenges.

Therefore the overall Microsoft V1 scientific success gate remains **NOT PASSED**, production approval remains **NO**, and maturity remains **`RESEARCH_PROTOTYPE`**.

See [`VALIDATION_RUN_15_TESTS_2026_09_16.md`](./VALIDATION_RUN_15_TESTS_2026_09_16.md) for the timestamped run record.
