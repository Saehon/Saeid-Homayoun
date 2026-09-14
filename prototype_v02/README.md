# ECONOVA-S™ v0.2 — Real Data + Evidence RAG

ECONOVA-S v0.2 upgrades the GPT-5.6 Sol prototype into a governed **design + evidence + real-data + econometrics** workbench.

## New in v0.2
- Controlled evidence registry with verified DOI/source metadata.
- Deterministic relevance-gated metadata RAG.
- Optional OpenAI web search.
- Optional OpenAI File Search against a user-owned/licensed vector store.
- Official Fama–French 5-factor live-data adapter.
- Verified CSV path for firm-year, market, and Climate TRACE exports.
- Generic empirical runner with entity/time fixed effects and clustered/HC3 errors.
- FT50-style Tables 1–6.
- Temporal OOS check.
- Stata `.do` export.
- Evidence Passport with data/empirical gate manifests.
- Human Gate.
- `discovery_claim_allowed = false` remains hard-coded.

## Evidence seed registry
Metadata-only anchors:
- Bergemann & Bonatti (2024), AER, DOI 10.1257/aer.20230478.
- de Kok (2025), Management Science, DOI 10.1287/mnsc.2023.03253.
- Haaland, Roth & Wohlfart (2023), JEL, DOI 10.1257/jel.20211658.
- Haaland et al. (2025), JEL, DOI 10.1257/jel.20251780.
- Cohen, Gurun & Nguyen (2026), Management Science, DOI 10.1287/mnsc.2024.09124.
- Fedyk et al. (2022), Review of Accounting Studies, DOI 10.1007/s11142-022-09697-x.

This is a seed registry, not a claim that every FT50/AJG4*/4 article is bundled.

## Real-data sources
The official Kenneth French Data Library is the default reproducible finance source.
Climate TRACE exports are supported through explicit user field mapping.

## Run
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

## Scientific classification
The generic empirical runner is associational by default. Fixed effects and clustered errors do not create causal identification.

## Two-core rule
1. Stable Economic Knowledge Core™.
2. Replaceable Technology Core™.

Evidence RAG and AI-to-AI Scientific Intelligence Fabric are capabilities/interfaces, not a third core.

## IP
Research/non-commercial license only. Commercial use requires prior written permission.

Copyright © 2026 Saeid Homayoun. ORCID: 0000-0002-2536-0446.
