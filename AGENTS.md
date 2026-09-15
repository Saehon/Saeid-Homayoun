# AGENTS.md

## NAAIL OpenLab™ — Codex Repository Instructions

This repository is the public research and software home for **NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin**. Codex and other coding agents should treat this file as the top-level repository instruction set.

## 1. Repository Mission

NAAIL OpenLab is an evidence-governed research, education, and professional-intelligence platform for accounting, auditing, assurance, sustainability, economics, and AI-enabled scientific discovery.

Primary specialist agents and modules include:

- **KIWI™** — Audit / CAM / KAM intelligence
- **POMELO™** — Forensic accounting co-scientist
- **VERA™** — IFRS / assurance intelligence
- **ECONOVA-S™** — Data Economy Agent
- **IFRS Agent** — IFRS reasoning and assurance workflows
- **PCAOB Agent** — PCAOB standards, inspection, and audit-quality workflows
- **ICFR / TimesFM Agent** — internal-control and forecasting research workflows
- **Research Lab** — reproducible scientific discovery workflows
- **Audit Agent Lab** — audit planning, risk, controls, evidence, analytics, ICFR, and inspection workflows
- **Student Lab** — education and simulation workflows for accounting, auditing, assurance, sustainability, and analytics

## 2. Canonical Architecture Rule

Keep **NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin** at the top level.

Do not present ECONOVA-S, POMELO, KIWI, VERA, IFRS Agent, PCAOB Agent, or other specialist agents as alternatives to NAAIL OpenLab. They are specialist agents or modules inside the NAAIL architecture.

Where the dual-core architecture applies, preserve exactly two permanent cores:

1. **Knowledge Core** — stable, evidence-based domain knowledge
2. **Technology Core** — replaceable, continuously evaluated technology components

Supporting configurable layers may include Jurisdiction Packs, Sector Packs, Language Adapters, Enterprise Policies, Trust & Assurance controls, connectors, and evaluation infrastructure. Do not convert supporting layers into additional permanent cores.

## 3. Scientific Discovery Governance

Research workflows should follow this general chain:

**Real Evidence → Evidence Passport → Hypothesis → Empirical Test → Falsification → Adversarial Review → Reproducibility → Human Approval**

Where relevant, support:

- hypothesis generation, critique, ranking, and refinement
- reproducible empirical research designs
- model, algorithm, measure, and specification comparison
- latent-structure discovery
- chain-of-evidence verification
- temporal and out-of-sample validation
- robustness and sensitivity testing
- human approval before scientific or professional claims are promoted

Never represent model output alone as a validated scientific discovery, professional judgment, audit conclusion, or regulatory conclusion.

## 4. Evidence and Data Rules

Prefer reproducible, traceable, legally usable data sources where possible, including:

- SEC EDGAR / XBRL
- PCAOB public materials
- Fama-French research data
- Damodaran public datasets
- public macroeconomic and market datasets
- approved research datasets
- IFRS or other standards content only where licensing and access terms permit

For every empirical workflow, preserve or generate metadata for:

- source
- retrieval date
- entity identifiers
- fiscal/reporting period
- transformations
- variable construction
- sample filters
- missing-value handling
- train/validation/test splits where applicable
- code version / commit reference
- random seed where stochastic methods are used

Never commit API keys, passwords, access tokens, private credentials, proprietary datasets, confidential student information, or restricted research data.

## 5. Coding Standards

Prefer:

- Python 3.11+ for new Python components unless an existing project specifies otherwise
- modular, testable code
- explicit configuration rather than hidden constants
- type hints where useful
- deterministic seeds for stochastic empirical work
- unit tests for important transformations and calculations
- clear docstrings and README documentation
- structured logging for reproducibility-relevant steps
- separation of raw, interim, processed, and output data
- small, reviewable pull requests

Do not silently rewrite research results, coefficients, tables, or conclusions to make hypotheses appear supported.

## 6. Statistical and Empirical Research Standards

For accounting, auditing, finance, economics, and sustainability projects, default analytical outputs should support, when appropriate:

1. sample construction and data provenance
2. variable definitions
3. descriptive statistics
4. correlation analysis
5. main regression / causal specification
6. robustness and sensitivity tests
7. diagnostic tests
8. out-of-sample or temporal validation where applicable
9. reproducibility manifest
10. evidence passport / chain-of-evidence record

Flag potential problems involving:

- look-ahead bias
- temporal leakage
- train/test contamination
- survivorship bias
- duplicate observations
- incorrect fiscal-year alignment
- post-treatment controls
- inappropriate fixed effects or clustering
- invalid standard-error assumptions
- unexplained sample attrition
- p-hacking or specification searching without disclosure
- target leakage in machine learning

## 7. Audit / CAM / KAM Research Rules

When working with CAM/KAM projects, preserve firm, filing, auditor, topic, fiscal period, and report-date identifiers.

For longitudinal CAM/KAM analysis, explicitly verify chronological ordering before constructing variables such as:

- NEW_TOPIC
- CAM_ENTRY
- CAM_EXIT
- CAM_PERSISTENCE
- CAM_COUNT
- DESCRIPTION repetition / adaptation
- RESPONSE repetition / adaptation

Do not infer consecutive observations solely from row order.

## 8. Professional-Agent Governance

For professional-facing modules such as KIWI, POMELO, VERA, IFRS Agent, PCAOB Agent, or ICFR agents:

- distinguish evidence from inference
- cite or record the authoritative source used
- expose uncertainty and unresolved conflicts
- preserve jurisdiction and effective-date context
- require a Human Gate for consequential conclusions
- do not present simulated findings as real audit evidence
- do not claim compliance without appropriate source validation

## 9. Security Review Rules

Codex reviews should flag:

- exposed secrets or tokens
- unsafe deserialization
- command injection risks
- prompt injection paths in agent/tool workflows
- unvalidated external inputs
- insecure file handling
- excessive permissions
- unsafe subprocess execution
- leakage of private or licensed data
- dependencies with material known vulnerabilities where detectable

Prefer least-privilege tool permissions and explicit allow-lists for high-risk external actions.

## 10. Repository Review Priorities

When asked to review a pull request, prioritize findings in this order:

1. correctness
2. research validity
3. data leakage / temporal validity
4. security and secrets
5. reproducibility
6. architecture consistency
7. tests
8. maintainability
9. documentation

For material issues, explain why the issue could change empirical conclusions, professional judgments, or reproducibility.

## 11. Codex Change Policy

Before making substantial changes:

- inspect the nearest README and any nested `AGENTS.md`
- preserve existing interfaces unless the task explicitly requires a breaking change
- make the smallest coherent change that satisfies the task
- add or update tests when behavior changes
- document material assumptions
- avoid deleting research outputs or data mappings unless explicitly requested
- do not rename canonical NAAIL products or architecture elements without explicit instruction

After changes:

- run relevant tests or checks when available
- report what changed
- report tests run and their results
- identify anything that could not be verified

## 12. NAAIL Canonical Research Workflow

A preferred high-level workflow is:

**Professional / Scientific Problem → Real Evidence → Jurisdiction Resolver → Evidence Passport → Structured Analysis / Judgment Graph → Reproducible Empirical or Agent Test → Critic / Defender or Adversarial Review → Temporal / Cross-Sectional Validation → Falsification → Reproducibility Check → Human Gate**

Technology components may evolve, but evidence governance, reproducibility, auditability, and human approval remain mandatory.

## 13. Citation and Attribution

Preserve attribution for external code, datasets, models, standards, and research methods. Do not remove existing copyright, license, citation, DOI, ORCID, or provenance metadata unless explicitly instructed and legally appropriate.

## 14. Default Codex Review Prompt

When no narrower review instruction is provided, interpret `@codex review` as:

> Review for correctness, reproducibility, statistical validity, temporal/data leakage, security, secrets, tests, documentation, and consistency with the NAAIL OpenLab canonical architecture. Prioritize findings that could materially change research conclusions, professional judgments, or reproducibility.
