# Phase 4 — Observed Controlled-Mutation Benchmark

## Result
- Single controlled mutations detected: **10/10**
- Clean negative-control flags: **0**
- Compound errors detected: **5/5**
- Unit-test macro precision: **1.00**
- Unit-test macro recall: **1.00**
- Observed false-positive rate in the clean control: **0.00**

## Scope
This is an **engineering unit benchmark**. The numerical fixture is synthetic. It validates that the deterministic checking machinery behaves as specified for known E01–E10 mutations. It is **not** an estimate of performance on real manuscripts or evidence that the Management Science paper contains these errors.

## Gate
**PHASE_4_ENGINEERING_PASS**

Next scientific gate: external validity on multiple real replication packages with blinded mutations and human-coded ground truth.
