# ACK2007 — Phase 4 Source-Definition Recovery

Status: SOURCE-DEFINITIONS RECOVERED / RAW-RZSCORE SUB-GATE OPEN / NOT M1-LOCKED

Primary scientific target: Ashbaugh-Skaife, Collins & Kinney (JAE 2007) ICD disclosure logit.

## Recovered blocked definitions

| Variable | Source-locked operational definition | Source | Gate |
|---|---|---|---|
| FOREIGN_SALES | 1 if firm reports foreign sales; 0 otherwise | Compustat Segment file | PASS |
| RGROWTH | Decile rank of average sales growth rate, 2001–2003; sales = Compustat #12 | Compustat | PASS |
| %LOSS | Proportion of years 2001–2003 with negative earnings | Compustat | PASS |
| RZSCORE | Decile rank of Altman (1980) z-score/distress measure | accounting inputs / Altman construct | PASS as model input; RAW-CONSTRUCTION SUB-GATE |
| AUDITOR | 1 if 2003 auditor is PwC, Deloitte & Touche, Ernst & Young, KPMG, Grant Thornton, or BDO Seidman; 0 otherwise | Compustat #149 | PASS |
| INST_CON | Percentage shares held by institutional investors divided by number of institutions owning the stock; source reports scaling ×100 in reused definition | Thomson Financial Securities | PASS, scaling must remain exact |
| LITIGATION | 1 for SIC 2833–2836, 3570–3577, 3600–3674, 5200–5961, or 7370; 0 otherwise | SIC | PASS |

## Additional recovered timing
M&A: 1 if merger/acquisition 2001–2003 (Compustat AFNT #1).
RESTRUCTURE: 1 if nonzero Compustat #376/#377/#378/#379 during 2001–2003.
INVENTORY: average inventory/total assets over 2001–2003 (Compustat #3/#6).
AUDITOR_RESIGN: 1 if auditor resigns in 2003 (8-K).
RESTATEMENT: 1 if restatement or SEC AAER during 2001–2003.
The reused definitions state ICD determinants are measured at 2003 fiscal year-end or as averages over 2001–2003 where applicable.

## Provenance assessment
The 2009 Journal of Accounting Research paper by Ashbaugh-Skaife et al. explicitly reuses the ICD determinants from Ashbaugh-Skaife, Collins & Kinney (2007) and publishes their operational definitions. This is strong author-continuity evidence, but the 2007 primary article remains the target scientific object.

## Remaining scientific sub-gate
RZSCORE is now defined at the model-input level. To construct RZSCORE from raw accounting fields, separately lock the exact Altman (1980) z-score formula, eligible population treatment, missing-data policy, and decile-ranking reference sample used by ACK.

## Phase-4 decision
All seven previously BLOCKED variables are unblocked at the published-model input level.
ACK2007 can advance to Phase 5: Executable Scientific Model Object + unit tests.
Do NOT call the raw-data pipeline fully reproduced until the RZSCORE raw-construction sub-gate is closed.
