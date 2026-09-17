# XYZ-CH02 — Chapter 2 Architecture Benchmark

## NAAIL OpenLab™ V1.3C

**Public package status:** `RESEARCH_BENCHMARK / AUTHOR_FINALIZED_CASE / EXPERIMENT_PENDING`  
**Book case status:** `AUTHOR_FINALIZED` by Saeid Homayoun and Zabihollah Rezaee for book publication.  
**Validation claim:** No A0–A3 architecture-effect result is claimed until actual blind execution and evaluation are completed.

## Purpose

XYZ-CH02 is the first calibration benchmark for testing whether governed multi-agent architecture improves evidence-grounded forensic-accounting judgment relative to simpler architectures. It uses the author-finalized Chapter 2 XYZ Digital Twin, *The Last Week of the Quarter*, under strict longitudinal information cutoffs.

## Scientific design

The experiment compares the same professional problem and permitted evidence across four architecture conditions:

- **A0** — deterministic workflow;
- **A1** — single agent;
- **A2** — sequential agents;
- **A3** — governed NAAIL multi-agent architecture.

Initial calibration design: **5 runs per architecture = 20 primary runs**.

The experiment preserves failed, null, negative and contradictory evidence. A3 is not assumed to outperform simpler architectures.

## Canonical pipeline

`Author-Finalized XYZ Case → Protected Gold Benchmark → Blind Test Packet → Evidence Passport™ → A0/A1/A2/A3 → Professional Decision DAG™ → Blind Evaluation → Falsification & Robustness → Human Gate™ → Independent Replication`

## Public artifacts

1. [`TEST_001_CH02_BLIND_FOUR_ARCHITECTURE_PILOT.md`](./TEST_001_CH02_BLIND_FOUR_ARCHITECTURE_PILOT.md) — full experimental protocol.
2. [`TEST_001A_GOLD_FREEZE_AND_LEAKAGE_GATE.md`](./TEST_001A_GOLD_FREEZE_AND_LEAKAGE_GATE.md) — Gold Vault and leakage-control contract.
3. This README — public entry point and scientific-status boundary.

## Protected artifacts — not public

The public repository intentionally excludes the instructor solution, protected Gold answer/rubric, private regulatory or historical identity crosswalk, hidden labels, evaluator-only material, publisher-restricted content, and patent-sensitive implementations.

## Evidence classes

The benchmark never silently mixes:

1. real historical/public evidence;
2. XYZ Digital Twin evidence;
3. synthetic/counterfactual evidence.

The Construct Firewall additionally separates verified facts, regulatory findings, allegations, simulated evidence, anomalies, AI constructs, predictions, causal claims, counterfactual estimates, damages/economic estimates and recommendations.

## Release/maturity rule

The case being finalized for book publication establishes `AUTHOR_FINALIZED`; it does not establish an AI architecture effect. Promotion requires actual evidence.

`AUTHOR_FINALIZED → GOLD_FROZEN → BLIND_TEST_READY → EXECUTED → HUMAN_GATE_EVALUATED → FALSIFICATION/ROBUSTNESS → INDEPENDENTLY_REPLICATED → EXECUTED_VALIDATED`

Until those stages are evidenced, this package remains a research benchmark and must not be described as an empirically validated architecture benchmark.

## Frozen NAAIL boundary

XYZ-CH02 does not create a third core. NAAIL retains exactly:

1. **Stable Knowledge Core™**
2. **Replaceable Technology Core™**

The benchmark is an evidence/evaluation layer connecting the two cores.

## Human accountability

The author-finalized book case is attributed to **Saeid Homayoun and Zabihollah Rezaee**. Human professional judgment remains the final gate. Blind evaluation should conceal architecture identity where feasible.

## Patent-first and publication-rights boundary

**Patent first → public disclosure second.** Only high-level scientific protocol and rights-cleared reproducibility material belong in the public repository. Protected algorithms, private provenance mechanisms, unpublished embodiments, answer keys and publisher-restricted material remain private.

## Citation

When referring specifically to this benchmark before empirical execution, describe it as:

> Homayoun, S., & Rezaee, Z. (2026). *XYZ-CH02: An Author-Finalized Longitudinal Forensic Digital-Twin Benchmark for Evidence-Governed AI Architecture Evaluation*. NAAIL OpenLab™ V1.3C research benchmark.

Do not append a validated-performance claim until TEST 001B and the subsequent validation gates are completed.
