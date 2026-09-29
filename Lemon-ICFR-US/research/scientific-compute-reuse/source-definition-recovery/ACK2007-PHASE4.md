# ACK2007 — Phase 4 Source-Definition Recovery

Status: **SECONDARY-EVIDENCE SNAPSHOT / NON-EXECUTABLE / SCIENTIFIC-HOLD**

Primary scientific target: Ashbaugh-Skaife, Collins & Kinney (JAE 2007) ICD disclosure logit.

> Authority note: this file is a historical/source-recovery record. It is not executable admission logic. The canonical raw-construction authority is `ACK2007-construction-gates.json`. R-005 established that the recovered Phase-4 definitions below are secondary unless separately matched to ACK2007 primary evidence.

## Recovered candidate definitions and current evidence status
| Variable | Candidate operational definition | Evidence status | Current raw gate |
|---|---|---|---|
| FOREIGN_SALES | 1 if firm reports foreign sales; 0 otherwise | SECONDARY_SOURCE | SECONDARY_SOURCE |
| RGROWTH | Decile rank of average sales growth; competing 2001–2003 and 2002–2004 claims remain | SECONDARY_SOURCE + PROVENANCE_CONFLICT | PROVENANCE_CONFLICT |
| %LOSS | Proportion of years 2001–2003 with negative earnings | SECONDARY_SOURCE | BLOCKED_MISSING_YEAR_RULE |
| RZSCORE | Decile-ranked Altman z-score/distress measure; exact version unresolved | SECONDARY_SOURCE | BLOCKED_RAW_CONSTRUCTION |
| AUDITOR | Candidate auditor-group indicator | SECONDARY_SOURCE | SECONDARY_SOURCE |
| INST_CON | Candidate institutional-ownership concentration measure | SECONDARY_SOURCE | SECONDARY_SOURCE |
| LITIGATION | Candidate litigation-risk industry indicator | SECONDARY_SOURCE | SECONDARY_SOURCE |
| SIZE | Market-value-of-equity size construct; log-versus-level/window unresolved | PROVENANCE_CONFLICT | PROVENANCE_CONFLICT |

## Corrections from the earlier Phase-4 narrative
- The 2001–2003 RGROWTH claim is **not superseded** by 2002–2004. R-002 keeps the window unresolved.
- The SIZE level/average definition is **not locked**. R-003 keeps log-versus-level/window unresolved.
- %LOSS is not PASS because the earnings item, denominator and missing-year rule remain unresolved.
- RZSCORE is not PASS as a raw construct; R-007 forbids inferring the Altman version.
- FOREIGN_SALES, AUDITOR, INST_CON and LITIGATION are not primary-verified; R-005 requires SECONDARY_SOURCE.

## Phase-4 decision
This record may guide forensic comparison only. It must not construct raw inputs or upgrade scientific status. Raw construction is governed exclusively by the canonical registry and fail-closed validator. ACK2007 remains SCIENTIFIC-HOLD / NOT M1-LOCKED.
