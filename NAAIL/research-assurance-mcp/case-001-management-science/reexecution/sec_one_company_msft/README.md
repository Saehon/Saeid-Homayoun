# SEC One-Company Proof — Microsoft

## Purpose
Test whether the deHaan et al. filing-lag construct can be reconstructed for **one company** using only public SEC EDGAR data, avoiding WRDS for this proof-of-concept.

## Selected open-source SEC package
**dgunning/edgartools** — MIT-licensed, structured filing/XBRL access, actively maintained. For this NAAIL use case it is preferable to a raw downloader because it exposes company filings and filing metadata as structured Python objects.

## Company
Microsoft Corporation
- Ticker: MSFT
- CIK: 0000789019

## SEC-verified observations
| Matched calendar quarter | Form | Period end | Filing date | FilingLag |
|---|---|---:|---:|---:|
| Q1-2019 | 10-Q | 2019-03-31 | 2019-04-24 | 24 days |
| Q1-2020 | 10-Q | 2020-03-31 | 2020-04-29 | 29 days |
| Q2-2019 | 10-K | 2019-06-30 | 2019-08-01 | 32 days |
| Q2-2020 | 10-K | 2020-06-30 | 2020-07-30 | 30 days |

Within-company changes:
- Q1-2020 vs Q1-2019: **+5 days**
- Q2-2020 vs Q2-2019: **-2 days**

## Interpretation
This demonstrates that a core Case 001 construct — filing lag = filing date minus fiscal period end — can be reconstructed for one issuer directly from SEC EDGAR metadata.

This does **not** reproduce the paper's cross-sectional regression, filer-status controls, Audit Analytics fields, earnings-announcement dates, or full sample. It is a one-company public-data proof.

## Reproducibility rule
Use official SEC EDGAR as source of truth. The Python helper uses EdgarTools only as an acquisition/parsing layer and requires the user to set `EDGAR_IDENTITY`; no identity is hard-coded.
