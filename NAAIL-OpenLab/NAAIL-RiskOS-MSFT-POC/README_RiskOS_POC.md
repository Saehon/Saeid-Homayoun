# NAAIL RiskOS™ — Microsoft Golden Anchor POC

**Generated:** 2026-10-04  
**Maturity:** RESEARCH_PROTOTYPE  
**Commercial shell candidate:** ACCO Risk™  
**Anchor company:** Microsoft Corporation (MSFT), FY2026

## Purpose

This package turns the existing NAAIL Microsoft POC into a simple Claude-like risk workspace. It does **not** create a production risk rating. It demonstrates how a commercial risk product can route one company through specialist accounting, audit, control, forensic, cybersecurity, ESG and regulatory modules while preserving evidence, applicability and Human Gate status.

## Why Microsoft

The existing repository already contains the strongest bounded Golden Anchor package: SEC/XBRL facts, CAM/ICFR mapping, text analytics, market data, finance features, Evidence Passport, dashboard and the executed 15-test artifact contract. This makes Microsoft the right first integration case.

## Product architecture

1. Applicability Gate — jurisdiction, reporting basis, audit regime, source period.
2. Evidence Fabric — source ID, rights, timestamp, hash/lineage and Evidence Passport.
3. Specialist engines — ICFR, CAM, KAM, IFRS, AAER/forensic, cybersecurity, ESG, PCAOB, finance.
4. Risk Triage — transparent domain states; missing evidence remains pending.
5. Cross-domain risk graph — connect account → assertion → risk → control → evidence → audit matter → regulator → consequence.
6. Challenger / falsifier — independent review.
7. Human Gate — approve, modify, escalate, reject.
8. Digital Twin / learning — preserve time, version, outcomes and model changes.

## Critical design decision

The POC intentionally does **not** output a single 0–100 enterprise risk score. A commercial score should be introduced only after:
- benchmark calibration;
- outcome definition;
- temporal and company holdouts;
- false-positive / false-negative cost analysis;
- independent replication;
- governance approval.

Until then, domain-level triage is safer and scientifically defensible.

## Current Microsoft module state

- CAM: ELEVATED_JUDGMENT — two high-judgment CAMs.
- ICFR: LOW_SIGNAL — unqualified ICFR opinion, not zero risk.
- Finance/market: WATCH — FY2026 simple price return -24.2%; strong accounting margins.
- Text risk: WATCH_BOUNDED — bounded sample only.
- IFRS: SHADOW_MODE — Microsoft reports U.S. GAAP.
- KAM: N/A as primary regime — comparator only.
- AAER/forensic: PENDING_MATCH.
- Cybersecurity: PENDING_DEDICATED_INGEST.
- ESG: SOURCE_REGISTERED, analytics not executed.
- PCAOB: CONTEXT_ONLY; no engagement-specific deficiency inference.
- Evidence Assurance: EXECUTED.
- Human Gate: RESEARCH_ONLY; production approval NO.

## Fruit / specialist router

| Family | Role |
|---|---|
| LEMON | ICFR / controls |
| APPLE | CAM-US |
| ORANGE | KAM-EU/UK |
| MANGO | IFRS |
| POMELO | Forensic / investigation |
| GRAPE | Audit & assurance workflow |
| KIWI | Knowledge / audit intelligence |
| PEAR | Evidence assurance |
| DATA | Digital Twin / economic value |
| ESG | Sustainability assurance |
| PCAOB | Standards / inspection readiness |
| FINANCE | Valuation / market / scenario risk |
| NAAIL BOARD | Governance / challenge / Human Gate |

## Moat

The defensible moat is the governed evidence and decision system, not any single LLM:
- evidence provenance and rights;
- cross-domain applicability routing;
- domain-specific deterministic tests;
- risk/control/assertion/evidence graph;
- multi-model reviewer/falsifier separation;
- temporal Digital Twin;
- Human Gate;
- regulator/auditor-ready audit trail;
- risk-to-economic-value linkage;
- reproducible research benchmarks.

## Files

- `naail_riskos_msft_poc.html` — interactive standalone demo.
- `riskos_poc_data.json` — structured POC data and domain states.
- `README_RiskOS_POC.md` — this document.

## Scientific boundary

This is a product-design and research prototype. It is not an audit opinion, credit rating, investment recommendation, fraud determination, regulatory finding or production risk model.