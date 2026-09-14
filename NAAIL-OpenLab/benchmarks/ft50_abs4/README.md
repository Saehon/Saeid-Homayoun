# NAAIL OpenLab™ — FT50 / AJG 4* Benchmark Lab

This module integrates selected public replication repositories from FT50 and AJG/ABS 4* journals as **external scientific benchmarks** for NAAIL OpenLab™.

## Purpose
Use leading published research workflows to test whether NAAIL methods remain reproducible, robust, portable, falsifiable, and stable out of sample.

## Integration rule
NAAIL does **not** copy third-party source code into the proprietary core by default. External repositories are referenced through a governed registry, pinned to a specific commit before execution, and run through adapters or clean-room reproductions where appropriate.

## Initial benchmark families
- Management Science — accounting / financial-reporting reproducibility
- Review of Financial Studies — R and Stata reproducibility templates
- Journal of Financial Economics — staggered Difference-in-Differences / causal inference
- Review of Financial Studies — machine learning / forecasting
- Journal of Finance — end-to-end empirical replication

## Required test sequence
1. Source and license verification
2. Commit pinning
3. Environment reconstruction
4. Original-result replication
5. Independent reproduction / clean-room implementation
6. Robustness and alternative specification testing
7. Falsification and adversarial review
8. Temporal / out-of-sample validation
9. Cross-dataset generalization where legally possible
10. Digital Twin ground-truth testing where appropriate
11. Chain-of-Evidence capture
12. Human Gate

## Core NAAIL outputs
Each benchmark should produce a machine-readable run manifest and a human-readable benchmark card covering:
- replication fidelity;
- reproducibility;
- specification stability;
- causal robustness;
- temporal/OOS stability;
- cross-dataset generalization;
- falsification survival;
- evidence traceability;
- rights/license status;
- reviewer and Human Gate decision.

See `registry.json`, `BENCHMARK_PROTOCOL.md`, and `validate_registry.py` in this folder.
