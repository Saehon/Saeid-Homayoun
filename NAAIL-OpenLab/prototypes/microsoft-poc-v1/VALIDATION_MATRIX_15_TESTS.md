# Microsoft POC V1 — 15-Test Validation Matrix

**Contract version:** upgraded 2026-09-16  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Purpose:** map the new 15-test contract to evidence already present in the public Microsoft V1 package without converting unexecuted work into PASS.

> Important: the historical offline test harness remains **12/12 passed**. This file is a contract-coverage assessment against the newly upgraded 15-test specification; it is not a claim that a new 15-test automated harness has already been executed.

| Test | Required test | Status | Current evidence / limitation |
|---|---|---|---|
| TEST 01 | SEC/XBRL ingestion | **PASS** | Frozen SEC interactive-XBRL facts are validated in the existing unit tests. |
| TEST 02 | Financial statement extraction | **PASS** | FY2026 financial variables and segment reconciliation are present in the Digital Twin and financial feature artifacts. |
| TEST 03 | Variable dictionary validation | **NOT EXECUTED** | Variable dictionary exists, but the existing 12-test harness does not contain a dedicated schema/completeness validation test. |
| TEST 04 | Evidence Passport generation | **PASS** | Evidence Passport schema and instantiated SEC/XBRL provenance are present in the public package/results. |
| TEST 05 | CAM/audit-risk mapping | **PASS** | Revenue Recognition and Uncertain Tax Positions CAMs plus unqualified ICFR opinion are validated. |
| TEST 06 | Text analytics | **PASS** | Two bounded FY2026 filing samples were transformed to numerical features with hashes; raw text is not redistributed. |
| TEST 07 | Finance calculation | **PASS** | Ratios, FCF proxy, FY2026 close-to-close price return and DGS10 are executed. Fama–French exposure remains unexecuted. |
| TEST 08 | Innovation measure | **PASS** | R&D intensity and public GitHub metadata are executed research indicators. Aggregate patent/citation analysis remains unexecuted. |
| TEST 09 | ABC calculation | **PASS** | Synthetic Microsoft-like management-accounting microcase reports ABC/AI-ABC execution; no Microsoft internal cost data are claimed. |
| TEST 10 | TDABC calculation | **PASS** | Existing offline test validates capacity-cost-rate / TDABC arithmetic. |
| TEST 11 | AI token/cost calculation | **PASS** | Synthetic AI-cost microcase exists. This is not Microsoft internal costing and is not a production FinOps validation. |
| TEST 12 | Model benchmark | **PASS** | LiveBench 2026-06-25 external benchmark snapshot is present; it is not treated as a NAAIL professional-verification rate. |
| TEST 13 | Human–AI experiment structure | **PASS** | T0–T3 conditions exist and the repository test confirms `DESIGN_COMPLETE_NOT_EXECUTED`. This does not mean the participant experiment has run. |
| TEST 14 | Dashboard data load | **NOT EXECUTED** | `dashboard.html` exists and displays current V1 values, but the previous automated harness does not include an explicit dashboard-load/data-binding test. |
| TEST 15 | Human Gate decision | **PASS** | Human Gate boundary is recorded as publication-only; production approval is NO and scientific validation awaits independent replication. |

## Contract coverage summary

- Evidence-backed `PASS`: **13 / 15**
- `NOT EXECUTED`: **2 / 15** — TEST 03 and TEST 14
- `FAIL`: **0 / 15** currently documented
- `BLOCKED`: **0 / 15** currently documented

This summary is a **coverage classification**, not a replacement for executing a dedicated 15-test harness.

## Success-gate distinction

The upgraded specification separately requires actual success-gate execution for the **Human–AI Experiment**. TEST 13 only verifies the experimental structure. The participant experiment remains **NOT EXECUTED**, so the overall Microsoft V1 success gate is **NOT PASSED**.

Other open scientific gates include:

- Fama–French regression / factor exposure;
- aggregate PatentsView patent and citation measures;
- NAAIL-specific professional-task model verification and cost-per-verified-output;
- independent replication;
- explicit dashboard-load automated test;
- dedicated variable-dictionary validation test.

## Required next execution

1. Add and execute TEST 03 variable-dictionary validation.
2. Add and execute TEST 14 dashboard-load/data-integrity validation.
3. Run the complete dedicated 15-test harness and store timestamped output.
4. Execute the preregistered T0–T3 participant experiment before changing the Human–AI Experiment success-gate status.
5. Complete independent replication before any scientific-validation claim.

**Final status:** `RESEARCH_PROTOTYPE`.
