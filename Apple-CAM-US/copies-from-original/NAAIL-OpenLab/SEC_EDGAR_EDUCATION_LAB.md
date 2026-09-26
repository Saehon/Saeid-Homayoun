# NAAIL SEC EDGAR Education Lab™

**Integrated into NAAIL OpenLab™ on 14 September 2026.**

**Official SEC evidence → reproducible data → accounting analytics → audit/forensic reasoning → AI/agent analysis → student professional judgment → Evidence Passport™ → Human Gate™.**

The **NAAIL SEC EDGAR Education Lab™** is the public-data education layer of NAAIL OpenLab for accounting, auditing, assurance, forensic accounting, finance, sustainability reporting, and AI/data methods. It uses the U.S. Securities and Exchange Commission as the authoritative evidence source and treats GitHub libraries as software adapters, teaching aids, or reproducibility tools rather than substitutes for regulatory evidence.

## Canonical module

**[Open the NAAIL SEC EDGAR Education Lab →](./education/sec-edgar-lab/README.md)**

Core resources:

- [Assignment Bank](./education/sec-edgar-lab/ASSIGNMENTS.md)
- [Governed Agent Specification](./education/sec-edgar-lab/AGENT_SPEC.md)
- [SEC CompanyFacts Starter](./education/sec-edgar-lab/sec_companyfacts_starter.py)
- [Python Requirements](./education/sec-edgar-lab/requirements.txt)
- [Integration Manifest](./education/sec-edgar-lab/INTEGRATION_MANIFEST.md)
- [NAAIL Education Hub](./docs/education/README.md)

## Evidence and tooling hierarchy

1. **SEC EDGAR / data.sec.gov** — authoritative filing and XBRL evidence.
2. **SEC CompanyFacts / CompanyConcept / Frames** — structured accounting data for reproducible analysis.
3. **EdgarTools** — open-source Python adapter for filing and XBRL workflows.
4. **sec-edgar-downloader** — filing acquisition utility for teaching and reproducibility.
5. **SEC-API cookbook/notebooks** — examples and notebook patterns, subject to third-party terms.
6. **NAAIL agents and Digital Twins** — governed analytical and educational layer; never represented as SEC evidence.

Third-party packages retain their own licenses, attribution requirements, and release histories. NAAIL does not claim ownership of external software.

## Integrated educational architecture

```text
SEC EDGAR / XBRL / CompanyFacts
              ↓
Evidence acquisition + provenance
              ↓
Python / pandas / EdgarTools adapters
              ↓
Accounting & disclosure analytics
              ↓
Audit / ICFR / forensic reasoning
              ↓
NLP / LLM / RAG
              ↓
Governed multi-agent analysis
              ↓
Critic + Defender + Replicator
              ↓
Evidence Passport™ + Professional Decision DAG™
              ↓
Student challenge / revision / escalation
              ↓
Human Gate™
```

## Three teaching levels

### Bachelor / introductory
Students identify a registrant and CIK, retrieve filings, understand XBRL facts and chronology, reconstruct basic financial ratios, and document provenance.

### Master / professional
Students build multi-period CompanyFacts panels, analyze financial-statement movements and disclosures, map evidence to assertions and audit risks, and compare their professional judgment with governed AI recommendations.

### PhD / research
Researchers construct chronology-safe panels, create textual constructs, merge SEC data with economic/market sources, run causal/panel/time-series/predictive designs, and require robustness, falsification, replication, and Chain-of-Evidence before research claims.

## Ten-laboratory curriculum

| Lab | Topic | Main output |
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

## NAAIL agent roles

- **SEC Evidence Agent** — retrieves, identifies, and fingerprints source evidence.
- **Accounting Analyst Agent** — computes and explains accounting measures.
- **Audit Risk Agent** — maps evidence to assertions, risks, and procedures.
- **Forensic Agent** — searches for anomalies, inconsistencies, and contradictory evidence.
- **Critic Agent** — challenges unsupported interpretations.
- **Replicator Agent** — independently reproduces calculations and transformations.
- **Student / Human Reviewer** — accepts, revises, rejects, or escalates recommendations.

## Reproducibility and governance gates

Every educational or research run should preserve the SEC source/end point or filing URL, CIK/ticker, accession number when applicable, filing/report period, retrieval timestamp, transformation code, package versions, assumptions/exclusions, source hash where feasible, and the final human decision state.

AI-generated text is not regulatory evidence. Model output must remain distinguishable from SEC filings, structured facts, calculations, and instructor-approved synthetic evidence. Production audit conclusions are outside the scope of this public education module.

## NAAIL integration status

**Status: INTEGRATED — PUBLIC EDUCATION / RESEARCH MODULE.**

The SEC Education Lab is now part of the NAAIL OpenLab education architecture and is designed to interoperate with the Student Agent Academy™, Audit Digital Twin, Evidence Passport™, Professional Decision DAG™, Scientific Replication Arena, and Human Gate™.

A synchronized documentation copy is maintained in the connected **NAAIL OpenLab** Google Drive workspace for project continuity.

## Independence notice

NAAIL OpenLab is an independent research initiative. This module is not an SEC product, is not endorsed by the SEC, and does not imply partnership, sponsorship, certification, or endorsement by any regulator, audit firm, university, software project, or technology provider referenced in the documentation.
