# NAAIL OpenLab — Recruiter Portfolio View

## Saeid Homayoun
**Accounting & Audit AI Researcher | Agentic AI | Scientific Discovery | Financial/Economic Data Science**

This page is the short hiring-manager view of the portfolio. Detailed architecture, research governance, licensing, and scientific documentation remain elsewhere in NAAIL OpenLab.

## 30-second summary

I build evidence-governed AI systems for accounting, auditing, finance, economics, and sustainability research. My work combines domain expertise with multi-agent systems, retrieval/GraphRAG, empirical methods, reproducible evaluation, deterministic verification, and explicit human approval.

The portfolio is intentionally organized around **working systems and measurable research artifacts**, not only conceptual architectures.

## Flagship portfolio

| Project | Role in portfolio | What to inspect |
|---|---|---|
| **NAAIL OpenLab / ECONOVA-S™** | Public research hub | scientific workflow, executable audit prototypes, reproducibility, evaluation |
| **KIWI™ AAR Corp CAM Unit Test** | Primary executable audit benchmark | one-company CAM measurement, falsification, temporal reallocation, regression tests |
| **AAA — Audit & Accounting AI Laboratory** | Experimental audit/accounting AI lab | notebooks, audit analytics, multi-agent/NLP experiments |
| **IFRS-AI-Inspector** | Standards-aware public prototype | digital-twin reasoning, deterministic checks, provenance, human review |
| **POMELO™ / VERA™** | Private/proprietary R&D | professional-AI verification, evidence governance, agent evaluation |
| **ICFR + TimesFM research** | Time-series/risk application | internal-control forecasting and temporal evaluation |

## Start here: executable proof of work

### KIWI™ AAR Corp CAM Unit Test

Path: [`demos/aar-cam-unit-test/`](./demos/aar-cam-unit-test/)

This is the preferred CAM research benchmark in the public portfolio. It uses **AAR Corp only** as a permanent unit-test company before any KIWI CAM model is scaled to a larger U.S. CAM population.

Observed structure:

- 10 CAM observations;
- 2020–2024;
- exactly 2 CAMs per year;
- Inventory persists across all five years;
- Revenue persists through 2023 and exits in 2024;
- Acquired Intangibles / Business Combination enters in 2024;
- 2024 CAM count remains 2;
- 2024 CARS = **0.667**.

The central result is simple and testable: **CAM quantity is unchanged while CAM composition changes sharply.**

The demo includes frozen RPA, EDS, SIS, SQI, CIIS and CARS measures; correct-vs-swapped-response falsification; a year-level exact sign test; weight robustness; public metadata/company-year extracts; and regression tests.

Run:

```bash
cd NAAIL-OpenLab/demos/aar-cam-unit-test
python aar_cam_unit_test.py
python -m unittest test_aar_cam_unit_test.py
```

### Scientific boundary

AAR provides five company-year observations. It is used as a **measurement-development, falsification and proof-of-mechanism case**, not as a basis for population OLS, fixed effects, DiD, or causal claims. SQI is a CAM structural/communication-quality measure, not an audit-quality score.

This explicit boundary is part of the research design: strong AI research should document where inference is valid and where it is not.

## Original work vs. reference infrastructure

A professional research portfolio must distinguish original contributions from upstream or reference projects.

### Original / NAAIL-led
- NAAIL OpenLab / ECONOVA-S architecture and research workflow
- KIWI AAR Corp CAM measurement and unit-test architecture
- POMELO / VERA research architecture and verification concepts
- NAAIL Audit Digital Twin research prototypes
- IFRS-AI-Inspector integration/research framework
- accounting/audit applications and empirical research designs

### Upstream / reference infrastructure
Repositories or codebases such as **TimesFM**, **yfinance**, **AuditData-API**, and other third-party/open-source projects should be cited and described as upstream/reference infrastructure unless a specific original contribution is documented. Their presence in the account does not imply authorship of the underlying project.

## What I want a technical reviewer to evaluate

1. Can the research question be translated into an executable empirical object?
2. Are data and transformations traceable?
3. Are deterministic baselines separated from model-generated reasoning?
4. Can another researcher reproduce the result?
5. Are failure modes and negative results preserved?
6. Are evaluation metrics explicit and falsifiable?
7. Are agents/models prevented from silently redefining professional authority?
8. Is human responsibility preserved for scientific and professional conclusions?

## Current engineering priorities

- keep AAR Corp as the frozen CAM regression/unit-test company;
- require future CAM models to reproduce the AAR benchmark before scale-up;
- add controlled degradation tests while preserving the original CAM reference boundary;
- compare deterministic, embedding, LLM and governed multi-agent measures against the same AAR cases;
- maintain machine-readable run manifests and evidence artifacts;
- publish evaluation failures as well as successes;
- maintain clear upstream attribution and third-party rights boundaries;
- keep patent-sensitive and proprietary mechanisms outside the public repository.

## Research identity

**Saeid Homayoun**  
ORCID: [0000-0002-2536-0446](https://orcid.org/0000-0002-2536-0446)  
GitHub: [Saehon](https://github.com/Saehon)

NAAIL OpenLab is an independent research initiative. References to OpenAI, Google, Microsoft, audit firms, regulators, standards organizations, or other organizations do not imply affiliation or endorsement.
