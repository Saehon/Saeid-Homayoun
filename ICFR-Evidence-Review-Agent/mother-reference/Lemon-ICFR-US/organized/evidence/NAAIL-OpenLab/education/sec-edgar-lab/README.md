# NAAIL SEC EDGAR Education Lab™

**Official SEC evidence → accounting analysis → audit-risk assessment → AI/agent reasoning → student judgment → Human Gate.**

This module brings SEC EDGAR and XBRL data into **NAAIL OpenLab™** as a reproducible education and research environment for accounting, auditing, forensic accounting, finance, sustainability reporting, and AI/data methods.

## Design principle

The authoritative evidence layer is the **U.S. Securities and Exchange Commission (SEC)**. GitHub packages and third-party libraries are treated as tooling, examples, or adapters—not as replacements for the original regulatory source.

Primary SEC resources:

- SEC API documentation: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- CompanyFacts: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
- CompanyConcept: `https://data.sec.gov/api/xbrl/companyconcept/CIK##########/{taxonomy}/{tag}.json`
- Frames: `https://data.sec.gov/api/xbrl/frames/{taxonomy}/{tag}/{unit}/{period}.json`
- Company ticker mapping: `https://www.sec.gov/files/company_tickers.json`

Useful open-source teaching/engineering layers include:

- EdgarTools: https://github.com/dgunning/edgartools
- sec-edgar-downloader: https://github.com/jadchaar/sec-edgar-downloader
- SEC-API notebooks/cookbook: https://github.com/SEC-API-io/sec-api-cookbook

Third-party tools remain subject to their own licenses and should be pinned/versioned for reproducible work.

---

## Learning architecture

```text
SEC EDGAR / XBRL / CompanyFacts
              ↓
Evidence acquisition + provenance
              ↓
Python / pandas / EdgarTools adapter
              ↓
Accounting & disclosure analytics
              ↓
Audit / forensic / ICFR reasoning
              ↓
NLP / LLM / RAG / agent layer
              ↓
Critic / Defender / Replicator
              ↓
Evidence Passport™ + Decision DAG™
              ↓
Student professional judgment
              ↓
Human Gate™
```

## Teaching tracks

### Track A — Bachelor / introductory
1. Identify a registrant and CIK.
2. Retrieve a 10-K/10-Q filing and CompanyFacts.
3. Explain XBRL facts and filing chronology.
4. Reconstruct selected financial-statement ratios.
5. Document data provenance and limitations.

### Track B — Master / professional
1. Build a multi-period CompanyFacts panel.
2. Analyze revenue, receivables, inventory, goodwill, debt, cash flow, and profitability.
3. Extract MD&A and Risk Factors from filings.
4. Map financial-statement movements to audit assertions and potential risks.
5. Compare human judgment with an AI/agent recommendation.
6. Require evidence citations and a Human Gate decision.

### Track C — PhD / research
1. Construct chronology-safe firm-quarter or firm-year panels.
2. Join SEC fundamentals with market/economic datasets.
3. Develop textual constructs from 10-K/10-Q/8-K filings.
4. Run causal, panel, time-series, or predictive designs.
5. Perform temporal/out-of-sample tests, falsification, sensitivity, and replication.
6. Produce an Evidence Passport™ and Chain-of-Evidence before making a research claim.

---

## Ten suggested laboratories

| Lab | Topic | Primary output |
|---|---|---|
| 01 | SEC EDGAR introduction | CIK + filing inventory |
| 02 | 10-K financial statements | structured statement dataset |
| 03 | XBRL / CompanyFacts | reproducible fact panel |
| 04 | MD&A textual analytics | disclosure measures |
| 05 | Risk Factors NLP | risk-topic features |
| 06 | Audit-risk mapping | assertion/risk matrix |
| 07 | AAER / forensic accounting | enforcement case analysis |
| 08 | CAM / audit disclosure linkage | risk-to-evidence exercise |
| 09 | LLM/RAG over filings | evidence-grounded Q&A |
| 10 | Multi-agent SEC Digital Twin | governed student simulation |

## NAAIL agent roles for the SEC lab

- **SEC Evidence Agent** — retrieves and fingerprints source evidence.
- **Accounting Analyst Agent** — derives financial-accounting measures.
- **Audit Risk Agent** — maps evidence to assertions and risks.
- **Forensic Agent** — searches for anomalies and contradictory evidence.
- **Critic Agent** — challenges unsupported interpretations.
- **Replicator Agent** — independently reproduces calculations.
- **Student / Human Reviewer** — accepts, revises, rejects, or escalates the recommendation.

See [`AGENT_SPEC.md`](./AGENT_SPEC.md).

## Reproducibility rules

Every exercise should record at minimum:

- SEC endpoint or filing URL;
- accession number where applicable;
- CIK and ticker;
- retrieval timestamp;
- filing/report period;
- source hash for frozen artifacts where feasible;
- package/environment versions;
- transformation code;
- assumptions and exclusions;
- student/agent decision state.

No model output should be represented as SEC evidence. AI-generated interpretations must remain distinguishable from source filings and computed facts.

## Start here

Run [`sec_companyfacts_starter.py`](./sec_companyfacts_starter.py) after editing the required SEC-compliant User-Agent string.

```bash
pip install -r requirements.txt
python sec_companyfacts_starter.py --cik 0000320193 --tag Revenues
```

The example CIK above is only a technical demonstration. Course exercises should use instructor-approved entities/cases and preserve source provenance.

## Status

**Public educational research module.** This module is not an SEC product and is not endorsed by the SEC. It is not an audit tool for production engagements. It is designed for research, education, reproducibility, and governed experimentation within NAAIL OpenLab™.
