# Microsoft FY2026 Customer-Zero Benchmark

Purpose: a reproducible, free-first benchmark for SEC/XBRL extraction, accounting/audit evidence, ICFR-oriented review, falsification and human approval.

## Authoritative filing
- Issuer: Microsoft Corporation
- CIK: 789019
- Form: 10-K
- Fiscal year end: 2026-06-30
- SEC filing document: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm

## Pipeline
SEC filing -> deterministic extraction -> XBRL/provenance validation -> parallel tool adapters -> normalization -> benchmark comparison -> falsification gate -> Evidence Passport -> Human Approval.

## Compared paths
1. Existing canonical SEC/XBRL pipeline / sec-data.
2. EDGAR MCP (read-only agent data interface).
3. SEC-10-K-Structured-Extraction (MIT).
4. Verified Credit Research Agent (MIT).

TradingAgents is technology-layer only and is not an authoritative accounting evidence source. Finch/FinWorkBench is an external benchmark and is kept sealed from development outputs.

## Free-first routing
Deterministic parsers and SEC facts run first. Open-source/local models may be used only where deterministic extraction is insufficient. Paid/proprietary LLM calls are optional fallbacks and must never overwrite source facts.

## Acceptance gates
- filing identity and period match;
- every numeric claim has source/provenance;
- normalized units and periods;
- cross-tool agreement measured, not assumed;
- disagreements preserved for review;
- no unsupported accounting/audit conclusion;
- falsification result recorded;
- material conclusion requires Human Approval.

This is an educational/research benchmark, not an audit opinion or investment recommendation.
