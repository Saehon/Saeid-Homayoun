# 09 — Replication Report

## Current status

**PENDING — replication gate is not passed.**

The executable package is designed for two implementations:

1. Python build path: `build_v3.py` / parent `run_study.py`.
2. Stata replication path: `stata/00_master.do` after the Python data package is produced.

## Independence classification

Current design target: **separate code path, shared official source data**. This is stronger than a second prompt but weaker than a fully independent external replication team.

## Required checks

- same common monthly sample;
- same DCS calculations;
- same CAPM/FF3/FF5 alpha direction and economically material magnitudes;
- reconciliation of inference differences caused by implementation details;
- same conclusion-reversal classifications under the frozen rule;
- source hashes and archive URLs preserved;
- ordinary-revision placebo archive pairs added before any causal attribution claim.

## Promotion rule

`replication_or_oos = true` may be set only after actual outputs are generated, independently reproduced, reconciled, and archived.

No replication result is asserted in this pre-run document.
