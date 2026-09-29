# ACK2007 — Variable Ontology v0.3

Status: **SCIENTIFIC-HOLD / PRIMARY-DEFINITION VERIFICATION REQUIRED / NOT M1-LOCKED**

Scientific object: Ashbaugh-Skaife, Collins & Kinney (JAE 2007), ICD discovery/reporting model.

## Canonical conceptual mapping
| Original | Canonical concept | Compiler-facing meaning | Current evidence/gate |
|---|---|---|---|
| SEGMENTS | Organizational complexity — business segments | Number of reported business segments | PENDING_TIMING |
| FOREIGN_SALES | International operational complexity | Exact paper coding required | SECONDARY_SOURCE |
| M&A | Organizational change — acquisition activity | Exact paper indicator required | PENDING_EXACT_CONSTRUCTION |
| RESTRUCTURE | Organizational change — restructuring | Exact paper construction required | PENDING_EXACT_CONSTRUCTION |
| RGROWTH | Rapid growth | Ranked sales-growth construct | PROVENANCE_CONFLICT: 2001–2003 vs 2002–2004 |
| INVENTORY | Accounting measurement complexity | Inventory / total assets candidate construct | PENDING_TIMING |
| SIZE | Firm scale | Market-value-of-equity size construct | PROVENANCE_CONFLICT: log vs level/average; missing-year rule unresolved |
| %LOSS | Reporting/resource pressure | Loss-frequency construct | BLOCKED_MISSING_YEAR_RULE |
| RZSCORE | Financial distress | Ranked Altman distress construct | BLOCKED_RAW_CONSTRUCTION; exact Altman version unresolved |
| AUDITOR_RESIGN | Auditor change / discovery incentive | Auditor-resignation indicator | PENDING_TIMING |
| AUDITOR | Audit-market / discovery incentive | Exact auditor-group coding required | SECONDARY_SOURCE |
| RESTATEMENT | Prior reporting problem | Exact restatement/AAER window required | PENDING_WINDOW |
| INST_CON | Monitoring / ownership concentration | Exact institutional concentration scaling required | SECONDARY_SOURCE |
| LITIGATION | Litigation exposure | Exact litigation-industry coding required | SECONDARY_SOURCE |

## Machine-readable authority boundary
This ontology explains concepts only. It is not the executable raw-construction source.

Canonical raw-construction status:
`../source-definition-recovery/ACK2007-construction-gates.json`

Fail-closed enforcement:
`../verification/ACK2007/ack2007_admission_validator.py`

Canonical coefficient engineering pin:
`../executable-models/ACK2007/coefficient-contract.json`

If any document, ontology map or historical source-recovery artifact conflicts with the construction registry, raw construction must fail closed. Frozen synthetic fixtures remain separate and test compiler/schema determinism only.

## Scientific risk flags
1. RGROWTH: do not select a window until ACK2007 primary evidence resolves C1/R-002.
2. SIZE: do not select log versus level/average or a missing-year rule until C2/R-003 is resolved.
3. %LOSS: denominator, earnings item and missing-year rule remain blocked under C3/R-004.
4. RZSCORE: do not infer Altman 1968 versus 1980; O3/R-007 remains unresolved.
5. FOREIGN_SALES, AUDITOR, INST_CON and LITIGATION remain SECONDARY_SOURCE under R-005.

## Decision
The executable coefficient vector remains an engineering regression pin only. No unresolved variable may be constructed from raw data. ACK2007 remains SCIENTIFIC-HOLD / NOT M1-LOCKED.
