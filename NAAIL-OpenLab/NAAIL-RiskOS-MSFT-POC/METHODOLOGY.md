# NAAIL RiskOS™ — Audit Risk Methodology

## Core equation

\[
AR_{iat}=IR_{iat}\times CR_{iat}\times DR_{iat}
\]

For the POC, each term is a **normalized research-demo index on [0,1]**, not a calibrated probability.

- **IR — Inherent Risk:** susceptibility to material misstatement before considering controls.
- **CR — Control Risk:** risk that relevant controls fail to prevent or detect/correct material misstatement.
- **DR — Detection Risk:** risk that audit procedures fail to detect an existing material misstatement.

## NAAIL mapping

### IR
MANGO / IFRS-shadow, APPLE / CAM, ORANGE / KAM comparator, POMELO / forensic & AAER, cyber inherent exposure, ESG inherent reporting risk, FINANCE / ECONOVA-S, disclosure/text risk.

### CR
LEMON / ICFR, ITGC, cyber controls, ESG controls, governance, control design, control operating effectiveness.

### DR
GRAPE / audit workflow, PEAR / evidence assurance, KIWI / knowledge & challenge, PCAOB requirements, sampling, population coverage, AI model risk, independent reviewer, NAAIL BOARD / Human Gate.

## Back-solving detection risk

Given a user-defined target audit-risk index:

\[
DR_{allowed} = \frac{AR_{target}}{IR\times CR}
\]

This is the practical planning use of the model: higher IR and CR imply a lower allowable DR index and therefore stronger audit evidence/procedures.

## Guardrails

1. Missing evidence is **PENDING/UNKNOWN**, never automatically low risk.
2. KAM is not the primary Microsoft audit disclosure regime; CAM is.
3. IFRS is cross-framework comparison only for Microsoft, which reports under U.S. GAAP.
4. PCAOB firm-level inspection themes are context, not Microsoft engagement findings.
5. A composite AR index is not an audit opinion, statistical probability, credit rating or fraud determination.
6. Production scoring requires calibration, temporal holdouts, company holdouts, false-positive/false-negative analysis, independent replication and human governance.
