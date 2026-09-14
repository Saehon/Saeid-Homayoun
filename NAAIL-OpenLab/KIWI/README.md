# KIWI™ — Key & Critical Audit Intelligence

**NAAIL OpenLab flagship research program for CAM/KAM intelligence, evidence alignment, empirical auditing, and governed AI.**

**Principal Investigator:** Dr. Saeid Homayoun  
**Parent hub:** [NAAIL OpenLab](../README.md)  
**Status:** Research architecture / public documentation layer

> KIWI is an independent research program. It is not affiliated with or endorsed by audit firms, regulators, standard setters, OpenAI, Google, Microsoft, or other referenced organizations.

## Research objective

KIWI studies whether AI can extract, structure, evaluate, and empirically test the information contained in **Critical Audit Matters (CAMs)** and **Key Audit Matters (KAMs)** while preserving jurisdiction, provenance, evidence quality, temporal validity, reproducibility, and human professional judgment.

The central research question is:

> **When auditors communicate a critical/key audit matter, how much useful information is provided about the underlying risk, assertions, procedures, evidence, professional attention, and changes over time?**

## Canonical KIWI pipeline

**Real Evidence → Jurisdiction Resolver → Evidence Passport → CAM/KAM Topic Classifier → Audit Assertions Mapper → RPA → AA → EG → PS → DS → DIST → Adversarial Critic–Defender → Temporal Holdout → Cross-Auditor / Cross-Industry Validation → Human Gate**

The architecture separates measurement, prediction, professional interpretation, and scientific inference. No LLM score is treated as ground truth without validation.

## Core measurement family

| Construct | Purpose |
|---|---|
| **RPA** | Risk–Procedure Alignment |
| **AA** | Assertion Alignment |
| **EG** | Evidence Grounding |
| **PS** | Procedure Specificity |
| **DS** | Disclosure Specificity |
| **DIST** | Distinctiveness / incremental information relative to comparison disclosures |

Construct definitions, coding rules, reliability thresholds, and validation procedures should be frozen before confirmatory tests.

## Data architecture

KIWI uses three linked analytical levels:

```text
CAM_LEVEL
    one row per CAM/KAM
        ↓ aggregation/linkage
COMPANY_YEAR_CAM
    one row per company-year
        ↓ topic decomposition
CAM_TOPIC_YEAR
    one row per company-year-topic
```

Public releases should use only data that can legally be redistributed. Restricted or licensed datasets should be represented through manifests, schemas, synthetic examples, or user-side reproduction instructions rather than copied into the repository.

## Empirical research design

A KIWI study should progress through:

1. research question and theory;
2. FT50 / high-quality audit-literature validation;
3. competing hypotheses and adversarial critique;
4. pre-specified construct definitions;
5. human-gold annotation and inter-rater reliability where required;
6. model/agent measurement validation;
7. temporal holdout and leakage controls;
8. company-year econometric tests;
9. cross-auditor, cross-industry, and jurisdiction validation;
10. alternative measures and falsification tests;
11. reproducibility package;
12. human scientific gate.

## Initial research themes

- Revenue recognition
- Goodwill and intangible assets
- Asset impairment
- Financial instruments and credit losses
- Going concern
- Business combinations
- Taxation
- Provisions and contingencies
- Inventory and biological assets
- Valuation and fair value
- CAM/KAM persistence, entry, exit, and reallocation
- Auditor attention and disclosure specificity

## Digital twin

KIWI may use a fictional audit digital twin named **xyz** for simulation and teaching. The digital twin must use synthetic or appropriately licensed evidence and must not imitate confidential audit-firm systems, methodologies, client engagements, or restricted standards content.

## Reproducibility target

```text
KIWI/
├── README.md
├── docs/
├── data_manifest/
├── schemas/
├── src/
├── tests/
├── notebooks/
├── configs/
├── results/
└── run_manifest.json
```

## Public/private boundary

This public folder documents the scientific architecture. Patent-sensitive implementation details, restricted datasets, private benchmarks, confidential gold labels, credentials, and proprietary POMELO components must remain outside the public repository until an explicit release decision is made.

## Citation

> Homayoun, S. (2026). *KIWI: Key & Critical Audit Intelligence* [Research program]. NAAIL OpenLab. GitHub. https://github.com/Saehon/Saeid-Homayoun/tree/main/NAAIL-OpenLab/KIWI

## Relationship to POMELO™

KIWI is the CAM/KAM-focused research vertical within the broader NAAIL ecosystem. POMELO/VERA provides the broader evidence-governance and professional-intelligence concepts; KIWI specializes those ideas for CAM/KAM measurement, validation, simulation, and empirical research.
