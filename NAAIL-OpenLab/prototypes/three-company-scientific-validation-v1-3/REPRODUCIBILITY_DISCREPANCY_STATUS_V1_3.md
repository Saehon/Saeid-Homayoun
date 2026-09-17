# Prototype V1.3 — Reproducibility Discrepancy Status

**Date:** 2026-09-17  
**Status:** `REQUEST_MORE_EVIDENCE`  
**Scope:** technical clean replay of the frozen V1.2 factor package

## Finding

The first clean replay did not reproduce the frozen V1.2 factor table exactly. The discrepancy was detected before V1.3 publication and is preserved as a falsification/reproducibility finding.

## Interpretation

The mismatch may reflect specification, return-label, source-window or frozen-output differences. No cause is asserted until the replay contract is reconciled against the exact V1.2 inputs and model definitions.

## Governance response

- do not mark independent replication as PASS;
- do not overwrite the original V1.2 result silently;
- compare frozen input hashes, return construction, factor window, model formula and output precision;
- publish the reconciled outcome as `SUPPORTED_AFTER_CHALLENGE`, `REVISED_AFTER_CHALLENGE` or `REQUEST_MORE_EVIDENCE`;
- retain both the original and replay evidence.

This discrepancy is a scientific control result, not a reason to conceal or delete the replay.
