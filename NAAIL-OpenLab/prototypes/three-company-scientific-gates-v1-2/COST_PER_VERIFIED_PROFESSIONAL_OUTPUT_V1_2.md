# NAAIL Prototype V1.2 — Cost per Verified Professional Output™

**Run date:** 2026-09-17  
**Status:** `REGISTERED_NOT_EXECUTED`

## Metric contract

For a benchmark run:

`Cost per Verified Professional Output = (model inference cost + retrieval/tool cost + rerun cost + verification labor cost) / number of outputs that pass the frozen professional verification gate`

A verified output must pass the applicable gold/evidence check; merely producing an answer does not enter the denominator.

## Required inputs

- actual model/API usage and price at run timestamp;
- tool/retrieval charges where applicable;
- rerun/retry usage;
- verification minutes and an explicitly defined labor-cost assumption;
- verified pass/fail result for each professional task.

## Why no value is reported yet

The current V1.2 benchmark self-check is leakage-prone and does not contain independently measured model/API invoices or human verification time. Reporting a numeric cost would therefore be false precision.

Step 11 remains `REGISTERED_NOT_EXECUTED` until a blind professional benchmark run supplies these inputs.
