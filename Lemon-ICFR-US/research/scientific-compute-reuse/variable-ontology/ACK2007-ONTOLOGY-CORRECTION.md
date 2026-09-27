# ACK2007 ontology correction — Phase 6C

Falsification/provenance cross-check against the author-team's 2009 JAR Appendix Table 13 exposed a material ontology error in the earlier draft.

## Correction
For the reproduced Table-13 specification carrying the coefficient vector used by LEMON-SCI-ESM-001:
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
