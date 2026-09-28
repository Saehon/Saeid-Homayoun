# ACK2007 — Variable Ontology v0.2

Status: ONTOLOGY-CORRECTED / SOURCE-VERIFICATION REQUIRED BEFORE M1 LOCK

Scientific object: Ashbaugh-Skaife, Collins & Kinney (JAE 2007), ICD discovery/reporting model.

## Canonical mapping

| Original | Canonical concept | Operational meaning for compiler | Type | Timing / source note | Confidence |
|---|---|---|---|---|---|
| SEGMENTS | Organizational complexity — business segments | Number of reported business segments | count | Compustat segment reporting; align to model fiscal-year convention | HIGH |
| FOREIGN_SALES | International operational complexity | Indicator/measure of foreign sales activity; exact paper coding must be preserved | requires source-exact coding | Compustat/segment data | MEDIUM — exact construction must be cross-checked |
| M&A | Organizational change — acquisition activity | Merger/acquisition activity indicator as defined by paper | binary | financial statement/Compustat construction | MEDIUM |
| RESTRUCTURE | Organizational change — restructuring | Restructuring activity/charge indicator as defined by paper | binary | Compustat | MEDIUM |
| RGROWTH | Rapid growth | Decile rank of average sales growth rate | ranked continuous | 2002–2004 correction; exact missing-data rule still source-sensitive | MEDIUM |
| INVENTORY | Accounting measurement complexity | Inventory scaled by total assets | ratio | Compustat | HIGH subject to exact fiscal timing |
| SIZE | Firm scale | Average market value of equity during 2001–2003, USD billions | continuous | market data; missing-year/sample-eligibility rule unresolved | MEDIUM — NON-EXECUTABLE until missing-year rule is verified |
| %LOSS | Financial reporting/resource pressure | Proportion/frequency of loss years over authors' lookback window | ratio | Compustat history | MEDIUM |
| RZSCORE | Financial distress | Decile-ranked modified Altman Z-score / distress proxy used by authors | ranked continuous | accounting inputs | MEDIUM |
| AUDITOR_RESIGN | Auditor change / discovery incentive | Indicator for auditor resignation | binary | auditor-change disclosure/source | HIGH concept; timing cross-check required |
| AUDITOR | Audit-market / discovery incentive | Indicator for auditor type/market position as defined by authors | binary | audit-firm identity | MEDIUM |
| RESTATEMENT | Prior reporting problem / discovery incentive | Indicator for prior/relevant financial-statement restatement | binary | restatement source | HIGH concept; exact window pending |
| INST_CON | Monitoring / ownership concentration | Institutional ownership concentration measure | continuous | institutional holdings source | MEDIUM |
| LITIGATION | Litigation exposure | Indicator for membership in higher-litigation-risk industries | binary | industry classification | HIGH concept; exact SIC set pending |

## Compiler rule
A variable is executable only after its exact paper formula, unit, transformation, timing, source and missing-value rule are locked. Conceptual equivalence is not sufficient.

## Machine-readable authority boundary
This ontology defines scientific meaning but is **not** the executable raw-construction admission source.

Canonical raw-construction status is maintained in:
`../source-definition-recovery/ACK2007-construction-gates.json`

Enforcement is implemented by:
`../verification/ACK2007/ack2007_admission_validator.py`

If this ontology and the construction-gate registry disagree, raw construction must fail closed until the discrepancy is resolved. Historical/resolved maps remain evidence records, not parallel executable gate lists.

Frozen synthetic fixtures are intentionally separate from the raw-construction gate and test only compiler/schema determinism with preconstructed inputs.

## Ontology risk flags
1. SIZE: do not execute raw-data construction until missing-year/sample-eligibility rule is verified from primary evidence.
2. RGROWTH: preserve corrected 2002–2004 window; do not substitute generic sales growth.
3. FOREIGN_SALES: preserve source-exact coding.
4. %LOSS, RZSCORE, AUDITOR, INST_CON and LITIGATION remain source-sensitive where noted.

## Decision
The coefficient-vector executable fixture remains a technical test object. Raw-data zero-retraining execution and M1 admission remain blocked wherever source-sensitive construction is unresolved.
