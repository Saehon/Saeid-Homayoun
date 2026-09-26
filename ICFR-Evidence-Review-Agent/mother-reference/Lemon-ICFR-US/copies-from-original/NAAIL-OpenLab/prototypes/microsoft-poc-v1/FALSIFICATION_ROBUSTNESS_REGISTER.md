# Microsoft POC V1 — Falsification & Robustness Register

**Maturity:** `RESEARCH_PROTOTYPE`  
**Golden Anchor:** Microsoft Corporation only  
**Rule:** no result is promoted merely because an artifact exists.

This register implements the upgraded requirement to challenge each major Microsoft V1 result with alternative evidence, models, specifications, periods and contradictory evidence.

| Area | Falsification question | Current status | Required evidence / next action |
|---|---|---|---|
| SEC/XBRL financial facts | Can another authoritative source reproduce the same FY2026 values? | **NOT EXECUTED** | Reconcile selected variables to Microsoft annual-report presentation and independently rerun CompanyFacts extraction. |
| Accounting ratios | Does another specification materially change the ratios/conclusions? | **PARTIAL / OPEN** | Recompute using alternative denominator and period definitions where economically defensible; document sensitivity. |
| CAM / ICFR mapping | Can an independent reviewer reproduce ACCOUNT→ASSERTION→RISK→CAM→PROCEDURE→EVIDENCE→JUDGMENT? | **NOT EXECUTED** | Independent coding / reviewer agreement and contradiction log. |
| Text analytics | Do another dictionary/model and another text window produce materially different results? | **NOT EXECUTED** | Compare open dictionary and model-based measures; test section/period sensitivity. |
| Finance | Are results robust to factor specification, period choice and market-return definition? | **NOT EXECUTED** | Run Fama–French model(s), alternative return windows, and clearly separated dividend-adjusted measures where data permit. |
| Innovation | Does GitHub activity actually measure innovation and do patent indicators corroborate it? | **NOT EXECUTED** | Execute PatentsView counts/citations/technology-diversity and test construct convergence. |
| ABC/TDABC/AI cost | Are results driven by assumed activity times, capacity or token prices? | **NOT EXECUTED** | Sensitivity/scenario grid for time, utilization, model price, tool calls and human-review time. |
| AI benchmark | Does another benchmark or professional task set change model conclusions? | **NOT EXECUTED** | Compare external benchmark with NAAIL accounting/audit task set; report quality/cost frontier rather than rank alone. |
| Human–AI experiment | Can contradictory evidence overturn AI-reliant judgments? | **DESIGN ONLY** | Execute T0–T3 participant experiment; test treatment effects, calibration and skepticism. |
| Evidence leakage | Could evaluation inputs leak target answers or benchmark labels? | **NOT EXECUTED** | Add data-lineage/evaluation-isolation review and contamination checks where feasible. |
| Evidence Passport | Can provenance be independently traced from promoted result to source and transformation? | **PARTIAL / OPEN** | Independent replay of selected passports and hash/source checks. |
| Dashboard | Does every displayed figure reconcile to a source artifact? | **NOT EXECUTED** | Add automated dashboard-data integrity test and source-to-card reconciliation. |
| Human Gate | Would another qualified reviewer reach the same publication decision? | **NOT EXECUTED** | Independent reviewer decision with rationale; preserve disagreement rather than overwrite it. |

## Mandatory failure handling

For each challenged result, record one of:

- `SUPPORTED_AFTER_CHALLENGE`
- `REVISED_AFTER_CHALLENGE`
- `REQUEST_MORE_EVIDENCE`
- `REJECTED_BY_FALSIFICATION`
- `BLOCKED`
- `NOT_EXECUTED`

A contradictory result must not be silently removed. It should be preserved in the Evidence Passport / validation record with the specification, period, model, source and reviewer rationale that produced it.

## Current conclusion

The public Microsoft V1 package contains useful bounded execution evidence, but the upgraded falsification program is **not yet complete**. Therefore:

- production approval remains **NO**;
- scientific validation remains **PENDING INDEPENDENT REPLICATION**;
- the maturity label remains **`RESEARCH_PROTOTYPE`**;
- expansion to SAP, Walmart, Intuit, Shopify, JPMorgan, ExxonMobil, Fluor or Boeing remains gated.
