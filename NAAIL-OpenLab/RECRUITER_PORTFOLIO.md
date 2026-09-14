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
| **AAA — Audit & Accounting AI Laboratory** | Experimental audit/accounting AI lab | notebooks, audit analytics, multi-agent/NLP experiments |
| **IFRS-AI-Inspector** | Standards-aware public prototype | digital-twin reasoning, deterministic checks, provenance, human review |
| **POMELO™ / VERA™** | Private/proprietary R&D | professional-AI verification, evidence governance, agent evaluation |
| **KIWI™ / CAM-KAM research** | Empirical audit-intelligence program | CAM/KAM measurement, benchmark design, risk–procedure/evidence alignment |
| **ICFR + TimesFM research** | Time-series/risk application | internal-control forecasting and temporal evaluation |

## Start here: executable proof of work

### CAM/KAM Agentic Audit Intelligence benchmark

Path: [`demos/cam-kam-agent-benchmark/`](./demos/cam-kam-agent-benchmark/)

This small standard-library Python demo converts CAM/KAM text into six transparent prototype dimensions:

**RPA · AA · EG · PS · DS · DIST**

It includes sample data, deterministic scoring, JSON output, unit tests, and explicit limitations. The objective is to show how a domain research idea becomes an executable and falsifiable benchmark.

Run:

```bash
cd NAAIL-OpenLab/demos/cam-kam-agent-benchmark
python benchmark.py sample_cases.csv --output results.json
python -m unittest test_benchmark.py
```

## Original work vs. reference infrastructure

A professional research portfolio must distinguish original contributions from upstream or reference projects.

### Original / NAAIL-led
- NAAIL OpenLab / ECONOVA-S architecture and research workflow
- POMELO / VERA research architecture and verification concepts
- KIWI CAM/KAM research architecture and measurement program
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

- convert flagship research ideas into compact runnable demos;
- add frozen benchmark cases and temporal/industry holdouts;
- compare deterministic, single-agent, sequential-agent, and governed multi-agent systems;
- add machine-readable run manifests and evidence artifacts;
- publish evaluation results, including failures;
- maintain clear upstream attribution and third-party rights boundaries;
- keep patent-sensitive and proprietary mechanisms outside the public repository.

## Research identity

**Saeid Homayoun**  
ORCID: [0000-0002-2536-0446](https://orcid.org/0000-0002-2536-0446)  
GitHub: [Saehon](https://github.com/Saehon)

NAAIL OpenLab is an independent research initiative. References to OpenAI, Google, Microsoft, audit firms, regulators, standards organizations, or other organizations do not imply affiliation or endorsement.
