# ECONOVA-Bench™

## Benchmarking Governed AI Research Systems in Business Science

ECONOVA-Bench™ evaluates whether a research co-scientist produces better scientific work than simpler LLM workflows.

The benchmark is designed for **accounting, auditing, finance, economics, sustainability, and business research**.

---

## Core comparison arms

1. **Single LLM** — one model, one prompt, no tools or independent review.
2. **Tool-using single agent** — one agent with literature/data/code tools.
3. **Multi-agent Co-Scientist** — generator, critic, defender, ranking, and empirical agents.
4. **Multi-agent + adversarial review** — adds independent replicator, skeptic, judge, and evidence auditor.
5. **Full ECONOVA-S™** — adds ERA empirical objects, ResearchEvolve, latent-structure validation, falsification, Chain-of-Evidence, DAG governance, Failure Memory, and Human Gate.

---

## Benchmark task families

### A. Hypothesis discovery

Given an authoritative dataset and literature corpus, produce competing hypotheses rather than one preferred story.

Metrics:
- novelty;
- theoretical coherence;
- falsifiability;
- economic importance;
- data feasibility;
- identification potential;
- independence from expected statistical significance.

### B. Literature validation

Test whether claims are supported by the cited literature.

Metrics:
- citation accuracy;
- claim–citation entailment;
- source quality;
- phantom citation rate;
- FT50/AJG relevance;
- contradictory-evidence retrieval.

### C. Construct generation

Generate and validate empirical constructs from structured or unstructured data.

Metrics:
- construct validity;
- sensitivity to researcher/model choices;
- convergent/discriminant evidence;
- temporal stability;
- benchmark correlation;
- economic interpretability.

### D. Identification and econometrics

Translate a hypothesis into a defensible empirical design.

Metrics:
- estimand clarity;
- timing correctness;
- treatment/outcome alignment;
- causal-claim calibration;
- standard-error correctness;
- panel/time-series specification correctness;
- leakage and look-ahead detection.

### E. Executable research code

Metrics:
- code execution rate;
- deterministic reproduction;
- package/environment completeness;
- table-to-code traceability;
- data provenance;
- method-description/code alignment.

### F. Robustness and falsification

Metrics:
- placebo quality;
- alternative-measure coverage;
- alternative-specification coverage;
- temporal/OOS validation;
- multiple-testing control;
- sensitivity-analysis quality;
- null-result preservation.

### G. Adversarial review

Metrics:
- error-detection rate;
- false-positive criticism rate;
- severity calibration;
- independence of review;
- correction success after review.

### H. Chain-of-Evidence

Metrics:
- claim completeness;
- claim correctness;
- claim → table → model → code → data linkage;
- theory claim → source linkage;
- broken-edge rate in the Research DAG;
- unsupported-claim blocking rate.

---

## Initial public benchmark datasets

### Finance

- Kenneth R. French factors and industry portfolios;
- Damodaran industry beta, WACC, profitability, growth, and valuation data.

### Accounting / auditing

- SEC EDGAR / XBRL CompanyFacts;
- public PCAOB and SEC materials where applicable.

### Textual analysis

- public financial filings and reproducible open corpora.

The benchmark prioritizes authoritative sources over unofficial mirrors whenever possible.

---

## Scientific fitness function

ResearchEvolve™ must not optimize statistical significance.

A candidate design can instead be evaluated on a frozen scientific fitness vector:

```text
Theory coherence
Construct validity
Identification credibility
Out-of-sample validity
Stability
Falsification survival
Replication
Interpretability
Evidence integrity
Computational reproducibility
```

`p_value_fitness_weight = 0`

---

## Minimum falsification suite

For applicable empirical studies, ECONOVA-Bench expects:

- temporal holdout;
- alternative constructs;
- alternative estimators;
- alternative samples;
- placebo timing;
- randomized or perturbed mappings where relevant;
- leave-one-group-out analysis;
- multiple-testing correction;
- leakage tests;
- crisis/regime sensitivity;
- economic-magnitude assessment;
- null-result reporting.

---

## Discovery status ladder

```text
IDEA
→ CANDIDATE_HYPOTHESIS
→ EMPIRICALLY_SUPPORTED
→ FALSIFICATION_SURVIVED
→ REPLICATED
→ EVIDENCE_VERIFIED
→ VERIFIED_CANDIDATE_DISCOVERY
→ HUMAN_APPROVED_RESEARCH_CLAIM
```

AI cannot autonomously assign the final status.

---

## Why this benchmark matters

A research agent should be judged not by how persuasive its prose sounds, but by whether it:

- discovers testable alternatives;
- uses correct evidence;
- executes the stated method;
- survives attempts to disprove its own result;
- reproduces independently;
- preserves negative findings;
- provides a traceable evidence graph;
- knows when **not** to claim discovery.

That is the standard ECONOVA-S™ is intended to meet.
