# Phase 3 — CAM + ICFR + Governance + ESG Research Modules

Phase 3 adds audit and sustainability/governance research layers to the same 10-company universe established in Phase 2.

## Scope

**Fully coded latest-year audit modules**
- CAM: auditor, CAM count, CAM topics, fiscal year and SEC 10-K source.
- ICFR: management assessment, auditor opinion, material-weakness flag and COSO framework.

**Source-registered research modules**
- Corporate governance: SEC DEF 14A source locator and target variables.
- ESG: issuer/public source locator and target dimensions.

This separation is intentional. Governance and ESG metrics are not filled by guesswork; their source registries are ready for a subsequent controlled extraction pass.

## Files

- `cam_latest.csv`
- `icfr_latest.csv`
- `governance_source_registry.csv`
- `esg_source_registry.csv`
- `validate.py`
- `research_agent.py`

## Research architecture

```text
Phase 2 financial panel
        ↓
same 10-company key
        ↓
┌─────────┬─────────┬────────────┬─────────┐
│   CAM   │  ICFR   │ Governance │   ESG   │
└─────────┴─────────┴────────────┴─────────┘
        ↓
deterministic validation
        ↓
GitHub canonical research layer
     ↙                 ↘
 Kaggle             Hugging Face
        ↓
free research agent
```

## Current coded audit snapshot

The current CAM module contains **14 CAMs across 10 companies** in the latest curated 10-K year.

The current ICFR module codes all 10 latest 10-K observations as management-assessed effective with auditor effective/unqualified ICFR opinions and no coded material weakness.

## Governance target variables

- board size
- independent-director share
- CEO-chair duality
- audit committee size
- audit committee financial expert
- dual-class flag

## ESG target dimensions

- climate / emissions
- energy
- water / materials / waste where relevant
- human capital
- supply chain
- governance/risk
- cybersecurity or responsible AI where relevant to the issuer

## Free research agent

```bash
python open-data/sec-10-company-phase3/research_agent.py profile MSFT
python open-data/sec-10-company-phase3/research_agent.py cam TSLA
python open-data/sec-10-company-phase3/research_agent.py icfr AAPL
python open-data/sec-10-company-phase3/research_agent.py sources META
```

## Boundary

This is a curated research dataset and source registry, not an audit opinion, assurance conclusion, ESG rating, governance score, or investment recommendation. Governance/ESG source registration does not mean the target variables have yet been coded.
