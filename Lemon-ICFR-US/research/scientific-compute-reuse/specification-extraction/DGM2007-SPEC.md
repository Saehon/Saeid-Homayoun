# DGM2007 — Specification Extraction

Status: STRUCTURE-VERIFIED / COEFFICIENTS-PENDING / NOT M1-LOCKED

Primary Table: Table 5.
Dependent variable: MW = probability of disclosing a material weakness.
Estimator: logistic regression.
Specifications: 3 columns.
Industry controls: 16 industry indicator variables included.
Column 1: baseline determinants.
Column 2: adds BANKRUPTCY RISK; sample falls about 13%; joint predicted probability reported from 3.75% to 26.41%.
Column 3: adds GOVERNANCE SCORE; sample falls about 58% relative to Column 2.
Baseline joint predicted probability reported from 4.17% to 23.66%.
Continuous variables are winsorized at 1% and 99% (per descriptive-table note).

Candidate variables visible in the article include MARKETCAP, FIRM AGE, AGGREGATE LOSS, BANKRUPTCY RISK, SPEs, SEGMENTS, FOREIGN TRANSACTIONS/SALES, ACQUISITION VALUE, EXTREME SALES GROWTH / SALES GROWTH, RESTRUCTURING CHARGE, GOVERNANCE SCORE; exact Table-5 column mapping and coefficients require primary-table cell extraction.

DARWIN gate:
- Estimator/outcome/table: PASS.
- Coefficients/intercept: HOLD — incomplete extraction.
- Variable ontology: HOLD.
- Estimand: observed MW disclosure; authors state aim is underlying internal-control problem, but observed DV remains disclosure.
- M1 admission: HOLD.
No coefficient will be inferred from significance statistics or marginal effects.
