# NAAIL OpenLab™ — Portfolio Governance

**Status:** canonical public governance record  
**Date:** 2026-09-15  
**Canonical source of truth:** `Saehon/Saeid-Homayoun/NAAIL-OpenLab`

## Governing rule

NAAIL OpenLab™ is the umbrella architecture. KIWI™, POMELO™, VERA™, ECONOVA-S™, IFRS/PCAOB agents, ICFR/TimesFM, Research Lab, Audit Agent Lab, Student Lab, ESG Intelligence, and Forensic Intelligence are specialist modules or research families under the umbrella; they are not competing top-level platforms.

GitHub is the canonical source of truth. Google Drive is a mirror/archive. Private repositories may contain pre-release, IP-sensitive, provider-specific, restricted-data, or experimental implementation and must not be treated as public release evidence.

## Repository classifications

| Repository | Visibility | Governance classification | NAAIL role | Provenance / attribution rule |
|---|---|---|---|---|
| `Saehon/Saeid-Homayoun` | Public | **CORE PRODUCT / CANONICAL** | NAAIL OpenLab public architecture, governance, public runtime, benchmarks, docs | Original/custom NAAIL materials must be distinguished from registered external assets |
| `Saehon/Saeid-Homayoun-` | Private | **CORE R&D / STAGING** | private pre-release implementation and Prototype 003-C engineering | Private R&D; not public release evidence |
| `Saehon/pomelo-core` | Private | **CORE R&D** | POMELO / VERA implementation family | Private R&D; preserve product/IP boundaries |
| `Saehon/IFRS-PCAOB-AI` | Private | **CORE R&D** | IFRS/PCAOB agent implementation | Private R&D; standards provenance required |
| `Saehon/AAA` | Public | **RESEARCH PROJECT** | Audit & Accounting AI research | Do not present as separate umbrella platform |
| `Saehon/IFRS-AI-Inspector` | Public | **RESEARCH PROJECT** | IFRS assurance / inspection research | IFRS source/version provenance required |
| `Saehon/Google-Antigravity-using-a-multi-agent-BERT-architecture` | Public | **RESEARCH / ENGINEERING PROJECT** | multi-agent experimentation and reusable engineering patterns | No Google affiliation/endorsement claim; provenance for imported components required |
| `Saehon/Financial-Sentiment-Analysis-and-Classification-Deep-Learning-Models` | Public | **RESEARCH PROJECT** | financial NLP / sentiment benchmark research | Dataset/model provenance and reproducibility required |
| `Saehon/agent-openai-python-banking-assistant` | Public | **EDUCATION / DEMO / REFERENCE** | multi-agent banking/finance engineering reference | Do not infer OpenAI/Microsoft ownership or endorsement; upstream/example provenance must be explicit |
| `Saehon/AuditData-API` | Public | **DATA / DEPENDENCY / REFERENCE** | audit-data interoperability reference | Treat as dependency/reference unless custom NAAIL components are separately identified |
| `Saehon/artificial-analysis-intelligence-index` | Public | **DATA / DEPENDENCY / REFERENCE** | model-intelligence reference source | Source attribution to Artificial Analysis must remain explicit |
| `Saehon/robosystems` | Public | **DATA / DEPENDENCY / REFERENCE** | financial-intelligence/knowledge-graph reference | Provenance and license review required before reuse |
| `Saehon/fg-data-synthetic` | Public | **DATA / DEPENDENCY / REFERENCE** | synthetic-data stress-testing reference | Provenance/license review required before reuse |
| `Saehon/ganlab` | Public | **EDUCATION / DEMO / REFERENCE** | GAN visualization/education reference | Treat as external/reference unless custom NAAIL work is explicitly separated |
| `Saehon/yfinance` | Public | **UPSTREAM FORK** | market-data dependency | Upstream project; never attribute upstream code/IP to NAAIL |
| `Saehon/timesfm` | Public | **UPSTREAM FORK** | time-series foundation-model dependency | Google Research upstream; never attribute upstream code/IP to NAAIL |
| `Saehon/desktop-tutorial` | Private | **UTILITY / ARCHIVE** | GitHub Desktop tutorial only | Not part of NAAIL scientific/product evidence |

## Default-branch governance

Different default branches currently exist across the portfolio (`main`, `master`, and `dev`). This is not automatically an error. Do **not** rewrite an upstream or dependency repository solely to normalize branch names. For original NAAIL repositories, new work should default to `main` unless a documented development-branch policy applies.

## Required attribution boundary

A repository existing under the `Saehon` account does not by itself establish NAAIL authorship or ownership. Every reuse decision must distinguish:

1. original/custom NAAIL code and documentation;
2. modified upstream code;
3. unchanged upstream forks;
4. external reference repositories;
5. third-party datasets/models/standards;
6. private/restricted/licensed assets.

Where provenance is uncertain, Codex and human reviewers must mark it **REQUIRES_PROVENANCE_REVIEW** rather than infer ownership.

## Scientific-state boundary

Documentation, architecture, scaffold code, provider adapters, synthetic benchmarks, and empirical results are separate evidence states.

- `IMPLEMENTED` means code/infrastructure exists.
- `EXECUTED` means a real run artifact exists.
- `VALIDATED` means predefined tests/evaluation passed.
- `EMPIRICAL RESULT` requires preserved inputs, model/provider/version metadata, outputs, evaluator results, provenance, and Human Gate review where material.

Never convert `IMPLEMENTED` into an empirical-performance claim.

## Prototype lineage

See [`PROTOTYPE_LINEAGE.md`](./PROTOTYPE_LINEAGE.md).

- Prototype 002 — historical revenue deterministic baseline.
- Prototype 003 — three-case synthetic benchmark; deterministic condition executed.
- Prototype 003-C — SEC-anchored Microsoft/Alphabet/Amazon evidence extension; implementation scaffold exists, live evidence pipeline remains incomplete until raw hashes/normalized evidence/scenarios/gold are preserved.
- Prototype 004 — real-provider harness; infrastructure exists, provider empirical runs remain credential/artifact dependent.

## Mandatory scientific governance

Material NAAIL experiments must preserve, as applicable:

**Evidence Passport™ → Professional Decision DAG™ → frozen evaluation contract → adversarial/critic review → reproducibility/falsification → Human Gate.**

No model, agent, reviewer, or benchmark may self-approve a material scientific/professional conclusion.

## Codex review contract

`Codex Portfolio Review v2` must treat this file and `portfolio_registry.json` as governance inputs, not as proof that every classification is factually complete. Codex should challenge classifications when repository evidence conflicts with them and report the conflict rather than silently changing attribution.

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**
