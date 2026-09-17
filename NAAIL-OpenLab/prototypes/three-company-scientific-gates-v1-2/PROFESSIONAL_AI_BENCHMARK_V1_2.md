# NAAIL Prototype V1.2 — Professional Accounting/Audit AI Benchmark

**Run date:** 2026-09-17  
**Status:** `RESEARCH_PROTOTYPE`  
**Gold tasks:** 18  
**Harness self-check:** 18/18 exact matches  
**Promotion eligibility of self-check:** NO

## Scope

A first NAAIL professional-task gold set is frozen across Microsoft, Walmart, and JPMorgan. It covers:

- CAM count;
- ICFR status;
- sector-adapter selection;
- primary CAM family;
- contradiction detection;
- executed FF5 market-beta retrieval.

## Important leakage boundary

The 18/18 result is **not a model-quality claim**. The same session created the gold set and candidate answers, so the run is intentionally marked leakage-prone and excluded from scientific promotion. Its purpose is only to validate the benchmark schema, scoring logic, and company coverage.

## What remains before Step 10 is complete

A real benchmark requires blind execution by at least two independently invoked models/workflows against the frozen gold set, with:
- no access to gold labels during generation;
- evidence-grounding checks;
- professional-correctness adjudication;
- latency measurement;
- actual inference/tool cost capture;
- failure retention;
- independent human or blinded adjudication for non-exact tasks.

## Status decision

Step 10 moves from `REGISTERED_NOT_EXECUTED` to `RESEARCH_PROTOTYPE`: the benchmark and gold set now exist and the harness is tested, but the required blind multi-model comparison is still open.
