# ECONOVA-S™ Canonical Public Data Sources

ECONOVA-S prioritizes authoritative first-party data over mirrors. GitHub and Kaggle copies may be useful for examples or reproducibility checks, but they should not silently replace an official source when the official source is available.

## Priority 1 — Fama–French Data Library

**Provider:** Kenneth R. French / Dartmouth Tuck  
**Official page:** https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

Recommended ECONOVA-S uses:
- Fama/French 3 Factors;
- Fama/French 5 Factors (2x3);
- momentum factors;
- size, value, profitability, investment and momentum portfolios;
- developed, European, North American, Asia-Pacific and emerging-market factors;
- historical archives for chronology-safe replication and FIZ/CIZ comparison work.

Research role: asset-pricing benchmark, market-factor prior, replication anchor, temporal/OOS benchmark.

## Priority 2 — Aswath Damodaran / NYU Stern

**Provider:** Aswath Damodaran  
**Current data page:** https://pages.stern.nyu.edu/adamodar/New_Home_Page/datacurrent.html

Current official spreadsheet endpoints used by ECONOVA-S v0.3 adapters:
- Cost of capital by industry: https://pages.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls
- Fundamental EPS growth by industry: https://pages.stern.nyu.edu/~adamodar/pc/datasets/fundgr.xls
- PE / PEG / growth data: https://pages.stern.nyu.edu/~adamodar/pc/datasets/pedata.xls
- EVA and Equity EVA by industry: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVA.xls

Research role: valuation priors, industry risk/cost-of-capital benchmarks, economic magnitude, growth/return-on-capital context, welfare/value interpretation.

Important: Damodaran data are primarily industry-level benchmarks and should not be confused with firm-level causal variables.

## Priority 3 — SEC EDGAR XBRL / CompanyFacts

**Provider:** U.S. Securities and Exchange Commission  
**Documentation:** https://www.sec.gov/search-filings/edgar-application-programming-interfaces

Primary endpoints:
- CompanyFacts: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
- CompanyConcept: `https://data.sec.gov/api/xbrl/companyconcept/CIK##########/{taxonomy}/{tag}.json`
- Frames: `https://data.sec.gov/api/xbrl/frames/{taxonomy}/{tag}/{unit}/{period}.json`
- SEC company ticker map: `https://www.sec.gov/files/company_tickers.json`
- Bulk CompanyFacts archive: `https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip`

Research role: firm-level accounting fundamentals, quarterly/annual panel construction, chronology-safe filing dates, financial statement variables, real-data econometrics.

SEC access rules:
- no API key is required for the data APIs;
- automated requests must comply with SEC fair-access and privacy/security policies;
- use an identifying User-Agent with researcher/application contact information;
- cache results and prefer bulk files for large-scale studies.

## Secondary Sources — GitHub and Kaggle

GitHub/Kaggle datasets may be used only when:
1. provenance to an authoritative source is documented;
2. licensing permits reuse;
3. hashes/version dates are preserved;
4. the source is checked against the official dataset where feasible;
5. ECONOVA-S labels the copy as a mirror/derived dataset rather than an authoritative source.

They are appropriate for tutorials, benchmark replications, code examples and frozen replication snapshots. They are not automatically suitable as the primary evidence source for publication-grade inference.

## Canonical v0.3 Merge Strategy

```text
Fama–French factors / portfolios
              +
SEC XBRL firm fundamentals
              +
Damodaran industry valuation priors
              ↓
Chronology-safe firm-period research panel
              ↓
Variable DNA™ + provenance manifest
              ↓
Tables 1–6 + OOS/replication + Red Team
              ↓
Evidence Passport™ + Human Gate
```

## Scientific rule

Data-source convenience never overrides provenance, licensing, chronology, construct validity or identification. Mirrored data must not be treated as more authoritative than their original source.
