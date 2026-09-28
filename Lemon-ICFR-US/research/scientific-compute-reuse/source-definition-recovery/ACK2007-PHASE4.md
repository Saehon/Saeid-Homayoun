# ACK2007 — Phase 4 Source-Definition Recovery

Status: PARTIAL / INPUT-DEFINITIONS RECOVERED / RAW-CONSTRUCTION SUB-GATES OPEN / NOT M1-LOCKED

Primary scientific target: Ashbaugh-Skaife, Collins & Kinney (JAE 2007) ICD disclosure logit.

## Recovered definitions and current gates
| Variable | Source-locked operational definition | Source | Gate |
|---|---|---|---|
| FOREIGN_SALES | 1 if firm reports foreign sales; 0 otherwise | Compustat Segment file | PASS |
| RGROWTH | Decile rank of average sales growth rate, 2002–2004; sales = Compustat #12 | Compustat | BLOCKED_MISSING_DATA_RULE |
| %LOSS | Proportion of years 2001–2003 with negative earnings | Compustat | PASS |
| RZSCORE | Decile rank of Altman (1980) z-score/distress measure | accounting inputs / Altman construct | PASS as model input; RAW-CONSTRUCTION SUB-GATE |
| AUDITOR | 1 if 2003 auditor is PwC, Deloitte & Touche, Ernst & Young, KPMG, Grant Thornton, or BDO Seidman; 0 otherwise | Compustat #149 | PASS |
| INST_CON | Percentage shares held by institutional investors divided by number of institutions owning stock; preserve published scaling | Thomson Financial Securities | PASS |
| LITIGATION | 1 for SIC 2833–2836, 3570–3577, 3600–3674, 5200–5961, or 7370; 0 otherwise | SIC | PASS |
| SIZE | Average market value of equity over 2001–2003, USD billions | market data | BLOCKED_MISSING_YEAR_RULE |

## Superseded evidence
The earlier Phase-4 RGROWTH entry using 2001–2003 is superseded and MUST NOT be executed. Current canonical/resolved artifacts use 2002–2004. Missing-data handling for RGROWTH remains unresolved.

## Remaining scientific sub-gates
1. SIZE: primary-evidence missing-year/sample-eligibility rule.
2. RGROWTH: primary-evidence missing-data/ranking eligibility rule.
3. RZSCORE: exact raw formula, eligible population, missing-data policy, and decile-ranking reference sample.

## Phase-4 decision
Executable model code may be tested with already-constructed, ontology-conforming inputs. Raw-data construction and M1 admission remain blocked until all applicable construction sub-gates are closed or explicitly bounded as preconstructed-input requirements. No missing-data behavior may be invented.
