# ACK2007 ontology correction — Phase 6C (secondary-source record; primary verification pending)

A cross-check against the author-team's 2009 JAR Appendix Table 13 exposed a possible material ontology error in the earlier draft. JAR 2009 is secondary evidence for the ACK2007 target and MUST NOT be treated as resolving the JAE 2007 specification without the published JAE primary text/table.

## Correction
For the JAR 2009 Table-13 specification that appears to carry values matching parts of the coefficient vector used by LEMON-SCI-ESM-001 (coefficient origin remains unverified):
- SIZE = average market value of equity from 2001–2003, expressed in $ billions (Compustat #199 × #25). **It is not ln(market value of equity).**
- M&A = indicator for merger/acquisition from 2002–2004.
- RESTRUCTURE = nonzero Compustat #376/#377/#378/#379 from 2002–2004.
- RGROWTH = decile rank of average sales growth rate from 2002–2004 (Compustat #12).
- RESTATEMENT = restatement or SEC AAER from 2002–2004.
- INVENTORY and %LOSS remain defined over 2001–2003 in that Appendix definition.
- RZSCORE = decile rank of Altman (1980) z-score.

## Consequence
Earlier ontology statements using ln(MVE) or 2001–2003 for all change variables are superseded for this executable coefficient vector. No empirical execution on firm data is permitted using the superseded mapping.

## RZSCORE boundary
RZSCORE is provenance-locked as a **preconstructed decile-rank model input**. Raw construction is not claimed reproduced because the exact reference sample/tie/missing-value ranking implementation is not established by the recovered text.

## Primary-evidence boundary (2026-09-29)
The entries above are retained as a secondary-source forensic fingerprint, not as canonical ACK2007 truth. RGROWTH and SIZE remain PROVENANCE_CONFLICT for raw construction; %LOSS remains BLOCKED_MISSING_YEAR_RULE; RZSCORE remains NOT_LOCKED/BLOCKED_RAW_CONSTRUCTION. The coefficient vector remains PENDING_PRIMARY_TABLE until the published JAE 2007 results table is directly verified.
