# Source and join map

| Source role | Useful evidence | Join keys to verify | Common risk |
| --- | --- | --- | --- |
| EDGAR/XBRL or filings | filing text, facts, accession, filing date | CIK/accession, issuer, fiscal period | revisions, duplicate filings, section drift |
| SRAF / AnalyText | text measures or validated feature definitions | project ID, issuer, filing/period | unclear construct or version |
| Ken French | returns, factors, portfolios | date, market/industry convention | look-ahead, frequency mismatch, factor definition drift |
| Damodaran | valuation/cost-of-capital inputs | date, country/industry, definition | assumptions and release-date mismatch |
| GitHub / Kaggle | code, data, notebooks, releases | commit/version, project ID | unclear license, mutable files, hidden preprocessing |
| Hugging Face | models, datasets, demos, revisions | repo/revision, sample ID | model drift, gated data, training-data opacity |

For every join, keep pre- and post-join counts, duplicate keys, unmatched records, date rules, and the exact source revision.

