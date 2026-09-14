# NAAIL OpenLab — GitHub Product Portfolio

This page is the canonical public-facing map that distinguishes **original NAAIL research products** from private R&D, upstream forks, and supporting/reference repositories.

The portfolio is designed to be readable by research collaborators, journal reviewers, software/AI teams, professional-services firms, and prospective employers without implying third-party affiliation or overstating product maturity.

## Flagship original products

| Product / repository | Visibility | Maturity | Primary role |
|---|---|---|---|
| **ECONOVA-S™ / `Saehon/Saeid-Homayoun`** | Public | Research Prototype / flagship research hub | Governed research co-scientist, empirical discovery, reproducibility, scientific evidence, portfolio governance |
| **AAA — Audit & Accounting AI Laboratory / `Saehon/AAA`** | Public | Research Laboratory / Research Prototype | Audit/accounting AI notebooks, empirical prototypes, multi-agent research, education and reproducibility |
| **IFRS-AI Inspector / `Saehon/IFRS-AI-Inspector`** | Public | Research Prototype | Standards-aware financial-reporting and assurance digital-twin research |
| **Multi-Agent Accounting AI Framework / `Saehon/Google-Antigravity-using-a-multi-agent-BERT-architecture`** | Public | Research Prototype | BERT/NLP, anomaly detection, digital twins, multi-agent orchestration and accounting/audit AI research |
| **POMELO™ / POMELO VERA™ / `Saehon/pomelo-core`** | Private | Proprietary R&D / Research Prototype | Professional-intelligence, verification, evaluation, Evidence Passport, decision DAG, benchmark and governance platform |
| **PCAOB Inspection Agent / `Saehon/IFRS-PCAOB-AI`** | Private | Research Prototype | Evidence-linked inspection analytics, deficiency/root-cause/remediation research and POMELO integration |

**Maturity rule:** none of the research-prototype labels above means regulator approval, professional certification, audit-firm endorsement, production authorization, or legal/regulatory compliance.

## Repository engineering baseline

The six original-product repositories are governed by [`NAAIL_PRODUCT_STANDARD.md`](./NAAIL_PRODUCT_STANDARD.md).

As of **14 September 2026**, the portfolio baseline includes the following controls where applicable:

| Control | Main hub | AAA | IFRS-AI Inspector | Multi-Agent Accounting AI | POMELO core | PCAOB Agent |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Professional README | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Citation metadata | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Roadmap | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Security policy | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Contribution/collaboration policy | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Changelog | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Reproducibility contract | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Data/evidence provenance policy | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Third-party/IP notices | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Explicit human-review boundary | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

A check mark means the repository now contains the governance/documentation layer. It does **not** mean every legacy notebook, experiment, dependency, dataset, or benchmark has already been independently validated.

## Supporting / reference repositories

These repositories may be useful for benchmarking, integration, teaching, replication, or experimentation, but should not be presented as original NAAIL inventions unless clearly separated original NAAIL additions are documented.

| Repository | Portfolio classification |
|---|---|
| `Saehon/timesfm` | **Fork/reference of Google Research TimesFM** — upstream forecasting model / integration reference |
| `Saehon/yfinance` | Supporting/reference market-data repository |
| `Saehon/Financial-Sentiment-Analysis-and-Classification-Deep-Learning-Models` | Supporting/reference financial-NLP repository |
| `Saehon/AuditData-API` | Supporting/reference audit-data tooling unless original ownership/provenance is separately documented |
| `Saehon/artificial-analysis-intelligence-index` | Supporting/reference AI benchmarking repository |
| `Saehon/agent-openai-python-banking-assistant` | Supporting/reference agent implementation |
| `Saehon/robosystems` | Supporting/reference automation repository |
| `Saehon/ganlab` | Supporting/reference generative/synthetic-data repository |
| `Saehon/fg-data-synthetic` | Supporting/reference synthetic-data repository |
| `Saehon/desktop-tutorial` | Private utility/staging repository |
| `Saehon/Saeid-Homayoun-` | Private staging/pre-release repository |

## Portfolio presentation rule

Public profiles, job applications, research proposals, and collaboration materials should lead with the **original-product repositories**. Forks and supporting repositories should be described as **upstream references, integrations, benchmarks, replications, dependencies, or experiments** rather than inventions developed by NAAIL.

The recommended public flagship order is:

1. **ECONOVA-S™ / NAAIL research hub** — `Saeid-Homayoun`
2. **AAA — Audit & Accounting AI Laboratory** — `AAA`
3. **IFRS-AI Inspector** — `IFRS-AI-Inspector`
4. **Multi-Agent Accounting AI Framework** — current long-name repository, with a recommended future neutral rename to `naail-multi-agent-accounting-ai`

Do not use the TimesFM fork as a flagship invention.

## Professional research-software contract

All original products should preserve:

**problem → evidence/data → architecture → executable method → evaluation → reproducibility → failure/limitations → human review → citation/provenance**.

The portfolio should distinguish four different statements:

- **Research specification** — a documented architecture/method;
- **Implemented prototype** — executable code exists;
- **Validated research prototype** — validation/replication exists for a defined scope;
- **Production system** — requires separate security, legal, regulatory, professional, organizational and deployment approval.

Never collapse these categories into one claim.

## Public/private IP boundary

Public repositories should contain research-safe specifications, demonstrations, lawful evidence, reproducibility material, and appropriately scoped source code.

Patent-sensitive orchestration logic, private benchmark answers, confidential datasets, unpublished product logic, and proprietary POMELO/VERA implementation should remain private until an explicit IP/publication review authorizes disclosure.

Existing third-party/open-source licences remain controlling for material already distributed under them.

## GitHub account actions still requiring UI/account-level access

The connected repository-content tools cannot perform several account-level operations. The following remain manual GitHub actions unless a future connector exposes them:

1. Create a **public repository named exactly `Saehon`** so GitHub can render a profile README on `github.com/Saehon`.
2. Populate `Saehon/Saehon` with a concise professional profile README linking the four public original products.
3. Consider renaming `Google-Antigravity-using-a-multi-agent-BERT-architecture` to **`naail-multi-agent-accounting-ai`**.
4. Pin the four public original products on the profile.
5. Set concise repository **Description / Website / Topics** fields in the GitHub UI where still missing.

## Canonical documentation

- [`NAAIL_PRODUCT_STANDARD.md`](./NAAIL_PRODUCT_STANDARD.md) — repository requirements.
- [`NEXT_UPDATE_HANDOFF.md`](./NEXT_UPDATE_HANDOFF.md) — continuation state for the next portfolio upgrade.
- [`GITHUB_PORTFOLIO_INDEX.md`](./GITHUB_PORTFOLIO_INDEX.md) — account-wide repository map.
- [`RESEARCH_RECORD.md`](./RESEARCH_RECORD.md) — research provenance convention.
- [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md) — account-hub third-party and non-affiliation boundary.

## Scientific governance rule

For major NAAIL studies and product claims, preserve:

**literature validation → competing hypotheses → executable empirical design → lawful data/evidence → code → adversarial review → robustness → falsification → replication → Chain-of-Evidence/provenance → human approval.**

Agent consensus, model confidence, statistical significance, benchmark score, or predictive accuracy alone is not sufficient for a scientific or professional claim.
