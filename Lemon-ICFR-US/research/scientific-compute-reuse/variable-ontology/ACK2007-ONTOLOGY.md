# ACK2007 — Variable Ontology v0.1

Status: ONTOLOGY-EXTRACTED / SOURCE-VERIFICATION REQUIRED BEFORE M1 LOCK

Scientific object: Ashbaugh-Skaife, Collins & Kinney (JAE 2007), ICD discovery/reporting model.

## Canonical mapping

| Original | Canonical concept | Operational meaning for compiler | Type | Timing / source note | Confidence |
|---|---|---|---|---|---|
| SEGMENTS | Organizational complexity — business segments | Number of reported business segments | count | Compustat segment reporting; align to model fiscal-year convention | HIGH |
| FOREIGN_SALES | International operational complexity | Indicator/measure of foreign sales activity; exact paper coding must be preserved | requires source-exact coding | Compustat/segment data | MEDIUM — exact binary/continuous construction must be cross-checked |
| M&A | Organizational change — acquisition activity | Merger/acquisition activity indicator as defined by paper | binary | financial statement/Compustat construction | MEDIUM |
| RESTRUCTURE | Organizational change — restructuring | Restructuring activity/charge indicator as defined by paper | binary | Compustat | MEDIUM |
| RGROWTH | Rapid growth | Relative/recent sales-growth measure used by authors | continuous | Compustat | MEDIUM — exact denominator/window must be cross-checked |
| INVENTORY | Accounting measurement complexity | Inventory scaled by total assets | ratio | Compustat | HIGH subject to exact fiscal timing |
| SIZE | Firm scale | Natural logarithm of market value of equity | continuous/log | market data / fiscal alignment | HIGH |
| %LOSS | Financial reporting/resource pressure | Proportion/frequency of loss years over authors' lookback window | ratio | Compustat history | MEDIUM — exact window must be cross-checked |
| RZSCORE | Financial distress | Decile-ranked modified Altman Z-score / distress proxy used by authors | ranked continuous | accounting inputs | MEDIUM — exact rank direction and formula must be locked |
| AUDITOR_RESIGN | Auditor change / discovery incentive | Indicator for auditor resignation | binary | auditor-change disclosure/source | HIGH concept; timing cross-check required |
| AUDITOR | Audit-market / discovery incentive | Indicator for auditor type/market position as defined by authors | binary | audit-firm identity | MEDIUM — exact coding label must be verified |
| RESTATEMENT | Prior reporting problem / discovery incentive | Indicator for prior/relevant financial-statement restatement | binary | restatement source | HIGH concept; exact window pending |
| INST_CON | Monitoring / ownership concentration | Institutional ownership concentration measure | continuous | institutional holdings source | MEDIUM — exact concentration formula pending |
| LITIGATION | Litigation exposure | Indicator for membership in higher-litigation-risk industries | binary | industry classification | HIGH concept; exact SIC set pending |

## Compiler rule
A variable is executable only after its exact paper formula, unit, transformation, timing, source and missing-value rule are locked. Conceptual equivalence is not sufficient.

## Ontology risk flags
1. FOREIGN_SALES: do not infer whether indicator or ratio without primary definition.
2. RGROWTH: do not substitute generic sales growth.
3. %LOSS: do not choose a lookback horizon from convention.
4. RZSCORE: do not substitute raw Altman Z for the paper's ranked construction.
5. AUDITOR: do not assume Big 4/5 coding until exact paper definition is verified.
6. INST_CON: do not substitute generic institutional ownership percentage.
7. LITIGATION: exact high-litigation SIC definition must be recovered.

## Phase-3 decision
Coefficient vector is available, but the model is NOT yet approved as zero-retraining executable because seven ontology details remain source-sensitive.
Next action: source-definition recovery for flagged variables, then compiler unit tests.
