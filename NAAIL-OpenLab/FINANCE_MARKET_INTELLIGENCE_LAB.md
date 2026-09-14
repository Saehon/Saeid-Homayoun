# NAAIL Finance Market Intelligence Lab™

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Specialist family:** ECONOVA-S™  
**Knowledge & RAG Core:** `KRG2026.3` — frozen and governed  
**Layer:** Technology / Market Data / Valuation / Risk / Portfolio / Research  
**Status:** Open-source finance architecture adopted; runtime integrations remain gated

> **NAAIL does not reproduce Bloomberg, S&P Global, S&P ratings, proprietary indices, or other restricted vendor data. It uses open-source software plus public/licensed data through governed adapters.**

## Purpose

The NAAIL Finance Market Intelligence Lab™ provides an open, research-safe financial analytics layer for market data, company fundamentals, valuation, fixed income, derivatives, portfolio construction, risk analytics, AI-finance experimentation, and transparent research scoring.

## Priority open-source projects

| Project | License / status | NAAIL role | Adoption |
|---|---|---|---|
| `OpenBB-finance/OpenBB` | AGPL-3.0 verified | Bloomberg-like open financial terminal / provider abstraction | `REFERENCE_ISOLATED_AGPL` |
| `JerBouma/FinanceToolkit` | MIT verified | financial ratios, valuation, performance, risk, fixed income, technical/fundamental analytics, MCP | `ADOPT_ANALYTICS_REFERENCE` |
| `JerBouma/FinanceDatabase` | MIT verified | security master / instrument reference database | `ADOPT_SECURITY_MASTER_REFERENCE` |
| `ranaroussi/yfinance` | Apache-2.0 verified | market-price and company-information adapter | `ADOPT_MARKET_DATA_ADAPTER` |
| `quantlib/QuantLib` | permissive BSD-style license verified | bonds, rates, term structures, derivatives, options and quantitative pricing | `ADOPT_PRICING_RISK_REFERENCE` |
| `AI4Finance-Foundation/FinRL` | MIT verified | AI / reinforcement-learning finance research environment | `ADOPT_AI_FINANCE_REFERENCE` |
| `PyPortfolio/PyPortfolioOpt` | MIT verified | portfolio optimization and efficient-frontier research | `ADOPT_PORTFOLIO_REFERENCE` |
| `dcajasn/Riskfolio-Lib` | permissive BSD-style license verified | risk measures, portfolio optimization, factor and hierarchical portfolio research | `ADOPT_RISK_PORTFOLIO_REFERENCE` |

## Data boundary

Open-source software licenses do **not** automatically grant rights to redistribute upstream financial data. NAAIL must separately evaluate the terms for every connected data source.

```text
software_license_equals_data_license = false
free_access_equals_free_redistribution = false
vendor_brand_equals_affiliation = false
market_price_equals_authoritative_valuation = false
model_score_equals_credit_rating = false
third_party_tool_may_modify_knowledge_rag_core = false
human_gate_required = true
```

## Canonical architecture

```text
PUBLIC / LICENSED DATA
SEC + FRED + World Bank + Riksbank + Fama-French + Damodaran
+ approved market-data adapters
        ↓
NAAIL Free Data Fabric™ + Evidence Passport™
        ↓
Frozen Knowledge & RAG Core™ — KRG2026.3
        ↓ read-only governed contract
ECONOVA-S™ / FINANCE MARKET INTELLIGENCE LAB™
        ├── OpenBB              → terminal/provider abstraction
        ├── yfinance            → market-data adapter
        ├── FinanceDatabase     → security master
        ├── FinanceToolkit      → ratios/valuation/analytics
        ├── QuantLib            → fixed income/derivatives/pricing
        ├── PyPortfolioOpt      → portfolio optimization
        ├── Riskfolio-Lib       → advanced risk/portfolio analytics
        └── FinRL               → AI-finance simulation/research
        ↓
ECONOVA-S™ Critic → Replicator → Evidence Auditor
        ↓
Human Gate™
```

## Transparent research scores

NAAIL may develop its own research measures using public/licensed evidence, for example:

- **NAAIL Financial Strength Score™**
- **NAAIL Credit Risk Research Score™**
- **NAAIL Distress Probability™**
- **NAAIL Market Risk Score™**
- **NAAIL Sector Risk Score™**

These must be described as **research scores**, not ratings issued by S&P Global Ratings, Moody's, Fitch, Bloomberg, or any other commercial provider.

## Validation requirements

Before runtime promotion of any finance integration:

1. verify exact upstream repository, branch, version or commit;
2. verify software license and attribution requirements;
3. verify the separate data-provider terms and redistribution rights;
4. pin dependencies and run security review;
5. execute on a synthetic or rights-cleared sandbox;
6. preserve data lineage, timestamps and Evidence Passport™ metadata;
7. benchmark against frozen tasks and out-of-sample periods;
8. retain failures and null results in Failure Memory™;
9. preserve the Frozen Knowledge & RAG Core boundary;
10. require Human Architecture / Research Gate approval.

## Relationship to NAAIL

- **ECONOVA-S™:** primary finance/economics specialist agent family.
- **Free Data Fabric™:** governed source acquisition and rights/provenance layer.
- **Scientific Discovery Platform:** hypothesis generation, empirical conversion, robustness and replication.
- **GAA™ / adversarial layer:** challenge assumptions, calculations, evidence and causal claims.
- **ERP Digital Twin Lab™:** transaction-level financial/accounting simulation.

NAAIL OpenLab™ is independent. References to Bloomberg, S&P Global, Yahoo, OpenBB, GitHub projects, universities, or other providers do not imply affiliation, endorsement, certification, partnership, or access to proprietary products or datasets.
