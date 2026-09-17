# NAAIL Prototype V1.3 — Blind Professional AI Benchmark Readiness

**Status:** `RESEARCH_PROTOTYPE`  
**Promotion status:** `NOT_EXECUTED`

V1.2's public gold set can no longer serve as a promotion-grade blind test because the answers are public. V1.3 therefore creates a fresh holdout packet whose public task prompts are separated from a private gold key.

## Public artifacts
- `blind_professional_benchmark_holdout_tasks_v1_3.csv`
- `blind_benchmark_scoring_schema_v1_3.csv`
- `cost_per_verified_output_telemetry_template_v1_3.csv`

## Private artifact
The answer key is intentionally excluded from public GitHub and should remain in a private Drive location until all candidate model responses are frozen.

## Required blind run
Each candidate model must be invoked independently with the same evidence packet and task order. Record model/version, timestamp, response, latency, token counts, API cost and provider price provenance. Freeze outputs before opening the gold key. Score exact factual correctness plus grounding and contradiction handling.

A same-session self-pilot is not promotion eligible because model/context leakage cannot be ruled out.

**Status:** benchmark infrastructure is ready; blind multi-model evidence is not yet executed.
