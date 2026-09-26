# CAM/KAM Agentic Audit Intelligence — Recruiter Demo

A small, executable NAAIL OpenLab prototype showing how an audit-AI research idea becomes a reproducible benchmark.

## Why this exists

The goal is to make the portfolio easy to evaluate by research and engineering recruiters. This demo deliberately favors **working code, transparent metrics, reproducibility, and limitations** over architectural claims.

It implements a lightweight CAM/KAM quality benchmark using six research-oriented dimensions used in the NAAIL/KIWI program:

- **RPA — Risk–Procedure Alignment**
- **AA — Assertion Alignment**
- **EG — Evidence Grounding**
- **PS — Professional Specificity**
- **DS — Disclosure Specificity**
- **DIST — Distinctiveness**

These scores are **prototype measurements, not validated audit-quality measures**. They are intended to demonstrate an empirical/evaluation pipeline that can later be calibrated against expert labels and archival CAM/KAM data.

## Run in under five minutes

Requirements: Python 3.11+; no third-party packages.

```bash
cd NAAIL-OpenLab/demos/cam-kam-agent-benchmark
python benchmark.py sample_cases.csv --output results.json
```

The command prints a compact score table and writes machine-readable JSON.

Run tests:

```bash
python -m unittest test_benchmark.py
```

## Input schema

CSV columns:

```text
id,risk_text,procedure_text,evidence_text,assertion_text
```

## Pipeline

```text
CAM/KAM text
   ↓
structured fields
   ↓
deterministic feature extraction
   ↓
RPA / AA / EG / PS / DS / DIST
   ↓
weighted prototype score
   ↓
JSON evidence artifact
   ↓
human interpretation
```

## Scientific boundary

This demo does **not** claim that the composite score measures audit quality, investor usefulness, regulatory compliance, or professional correctness. Before use in research, the next validation stages are:

1. expert-labelled gold set;
2. inter-rater reliability;
3. construct validity against established archival proxies;
4. temporal holdout;
5. auditor/industry holdout;
6. sensitivity to alternative weights and dictionaries;
7. adversarial boilerplate tests;
8. comparison with embedding/LLM-based measures;
9. preregistered empirical tests;
10. human approval of interpretations.

## Why this is relevant to AI research roles

The repository demonstrates the core pattern behind NAAIL OpenLab: convert domain expertise into a testable system with explicit inputs, deterministic baselines, evaluation artifacts, failure boundaries, and reproducible execution. A later agentic version can add retrieval, critique, model comparison, and learned scoring while retaining this deterministic baseline.

## Author

Saeid Homayoun  
ORCID: 0000-0002-2536-0446  
NAAIL OpenLab / independent research prototype
