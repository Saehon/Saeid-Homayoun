# Microsoft Customer-Zero Benchmark v1.0

Status: **REFERENCE BASELINE CREATED; MULTI-ENGINE EXECUTION PENDING**

Pinned issuer: Microsoft Corporation (CIK 0000789019)  
Period end: 2026-06-30  
Form: 10-K  
Accession: 0001193125-26-323660

## v1 reference facts
Nine high-value accounting facts are frozen in `gold_reference.csv`: revenue, operating income, net income, operating cash flow, accounts receivable, inventory, goodwill, total assets, and long-term debt.

The independent Microsoft FY2026 published statements cross-check the reference values. The SEC filing is the canonical filing source.

## Scientific rule
A registered adapter is not a tested adapter. All third-party engines remain `NOT_RUN` until executed in a pinned isolated runtime. Blank metrics are deliberate and must not be interpreted as zero.

## Falsification tests
- wrong fiscal period / quarter-vs-year;
- USD vs USD millions unit mismatch;
- duplicate or alternative XBRL concepts;
- instant vs duration context mismatch;
- extension concept substitution;
- unsupported narrative claim;
- stale filing/accession;
- arithmetic/reconciliation failure;
- provenance missing.

## Promotion
PASS requires reproducible execution + provenance + falsification. Material audit/accounting conclusions additionally require Human Approval.
