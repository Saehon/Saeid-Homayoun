# Microsoft-only Case 001 — FINAL

## Decision
The one-company proof is **finished**. No additional company is required for this case.

## Company
Microsoft Corporation (MSFT), CIK 0000789019.

## Public-data source
Official SEC EDGAR filing metadata and filing text.

## Reconstructed observations
| Quarter | Form | Period end | Filing date | FilingLag | Change vs same 2019 quarter | LateFiler | COVID present |
|---|---|---|---|---:|---:|---:|---:|
| Q1-2019 | 10-Q | 2019-03-31 | 2019-04-24 | 24 | 0 | 0 | 0 |
| Q2-2019 | 10-K | 2019-06-30 | 2019-08-01 | 32 | 0 | 0 | 0 |
| Q3-2019 | 10-Q | 2019-09-30 | 2019-10-23 | 23 | 0 | 0 | 0 |
| Q4-2019 | 10-Q | 2019-12-31 | 2020-01-29 | 29 | 0 | 0 | 0 |
| Q1-2020 | 10-Q | 2020-03-31 | 2020-04-29 | 29 | **+5** | 0 | 1 |
| Q2-2020 | 10-K | 2020-06-30 | 2020-07-30 | 30 | **-2** | 0 | 1 |
| Q3-2020 | 10-Q | 2020-09-30 | 2020-10-27 | 27 | **+4** | 0 | 1 |
| Q4-2020 | 10-Q | 2020-12-31 | 2021-01-26 | 26 | **-3** | 0 | 1 |
| Q1-2021 | 10-Q | 2021-03-31 | 2021-04-27 | 27 | **+3** | 0 | 1 |
| Q2-2021 | 10-K | 2021-06-30 | 2021-07-29 | 29 | **-3** | 0 | 1 |

## Core result
For Microsoft alone, the within-company change in filing lag relative to the same 2019 quarter is:

**+5, -2, +4, -3, +3, -3 days**

for Q1-2020 through Q2-2021.

Microsoft was not a late filer in any of the ten observations.

The 2019 matched filings contain no COVID reference in the SEC text checks used here. Each matched filing from Q1-2020 through Q2-2021 contains COVID/coronavirus discussion.

## Assurance conclusion
**SEC_ONE_COMPANY_RECONSTRUCTION_COMPLETE**

Verified:
- period end
- SEC filing date
- FilingLag
- same-quarter 2019 comparison
- LateFiler for this issuer
- binary COVID presence

Not claimed:
- full-sample regression reproduction
- population inference
- Audit Analytics/IBES variables
- exact paper-level narrative-count/FOG metrics
- methodological generalization

## Scientific meaning
This is a completed **proof of independent construct reconstruction** using public SEC data. It shows that the central timeliness variable can be rebuilt outside the authors' WRDS pipeline for one issuer and compared across the same calendar-quarter structure used by the paper.

It should be described as a **one-company replication case**, not as a replication of the full Management Science study.
