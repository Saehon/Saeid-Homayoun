# DGM2007 — Specification Extraction

Status: TABLE5-TEXT-CELLS-RECOVERED / PUBLISHER-VISUAL-CROSSCHECK-PENDING / NOT M1-LOCKED

Paper: Doyle, Ge & McVay (2007), Journal of Accounting and Economics 44, 193–223.
DOI: 10.1016/j.jacceco.2006.10.003

## Primary specification
Primary Table: Table 5 — Logistic regression of the probability of disclosing a material weakness.
Dependent variable: MW = 1 if the firm disclosed a material weakness in internal control from August 2002 to August 2005; 0 otherwise.
Estimator: logistic regression.
Specifications: 3 columns.
Industry controls: 16 industry indicator variables included in all three specifications.
Continuous variables: winsorized at the 1st and 99th percentiles.

Column 1: baseline determinants.
- Material-weakness observations: 707.
- Total observations: 4,984.
- Likelihood-ratio chi-square: 230.247 (reported p-value 0.001).
- Joint predicted probability reported in text: 4.17% to 23.66%.

Column 2: adds BANKRUPTCY RISK.
- Material-weakness observations: 627.
- Total observations: 4,333.
- Likelihood-ratio chi-square: 229.690 (reported p-value 0.001).
- Sample declines about 13%.
- Joint predicted probability reported in text: 3.75% to 26.41%.

Column 3: adds GOVERNANCE SCORE.
- Material-weakness observations: 273.
- Total observations: 1,841.
- Likelihood-ratio chi-square: 126.085 (reported p-value 0.001).
- Sample falls about 58% relative to Column 2.
- MARKETCAP, SPEs, and ACQUISITION VALUE are no longer statistically significant in the paper's discussion; GOVERNANCE SCORE is also not significant.

## Table-5 coefficient extraction
Exact text cells were recovered from a public full-article mirror and preserved separately in:
`DGM2007-TABLE5-EXTRACTION.csv`.

This is a material advance over the earlier structure-only extraction, but it is not yet a final scientific lock because a publisher-rendered PDF/table visual cross-check has not been completed.

No coefficient is inferred from significance statistics, marginal effects, or narrative prose.

## Variable construction recovered from article text
- MARKETCAP: log of market value of equity (share price × shares outstanding; Compustat items #25 × #199).
- FIRM AGE: log of the number of years the firm has been public, measured by years with CRSP price information.
- AGGREGATE LOSS: indicator for whether the sum of earnings before extraordinary items for years t and t-1 is negative.
- BANKRUPTCY RISK: decile rank of percentage bankruptcy probability from the Shumway (2001) hazard model.
- SPEs: log of the number of special-purpose entities associated with the firm.
- SEGMENTS: log of the sum of operating and geographic segments.
- FOREIGN TRANSACTIONS: indicator based on the existence of a foreign-currency adjustment.
- ACQUISITION VALUE: aggregate dollar value of acquisitions yielding at least 50% ownership in years t and t-1, scaled by year-t market capitalization.
- EXTREME SALES GROWTH: indicator equal to 1 when year-over-year industry-adjusted sales growth is in the top industry quintile.
- RESTRUCTURING CHARGE: aggregate restructuring charges in years t and t-1 scaled by year-t market capitalization.
- GOVERNANCE SCORE: Brown & Caylor (2006) composite of 51 factors across eight governance categories.

## Provenance boundary
Publisher metadata/abstract verifies the article identity, journal, pages, DOI, population framing, and high-level findings.
The exact Table-5 numeric cells were recovered from a public full-article text mirror. Because publisher-PDF visual verification is still pending, the extraction is classified as CANDIDATE-EXACT rather than M1-LOCKED.

## DARWIN gate
- Article identity / primary table / outcome / estimator: PASS.
- Table-5 text-cell extraction: PASS at text-replication level.
- Publisher-rendered visual cross-check: HOLD.
- Variable ontology: PARTIAL — definitions materially recovered; exact source/item details still need structured lock.
- Replication code/data: HOLD / not yet verified.
- Estimand: observed MW disclosure; authors use disclosure as a proxy for underlying control weakness, so disclosure-vs-underlying-MW distinction remains explicit.
- Executable-model compilation: HOLD until visual coefficient cross-check and ontology gate.
- M1 admission: HOLD.

Next gate: publisher-rendered Table-5 visual verification or equivalent independent primary-artifact replication, then lock a specific column/specification before compiling an executable DGM object.
