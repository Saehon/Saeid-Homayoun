# Prototype V1.2 — Executed Validation Record

**Date:** 2026-09-17  
**Run:** `NAAIL-3C-V1.2-2026-09-17-A`

Executed locally against the frozen V1.2 package:

```text
PASS: reproduced 18 CAPM/FF3/FF5 specifications across three companies and two return bases.
......                                                                   [100%]
6 passed in 0.07s
```

The six package-integrity tests validate:
1. exactly 60 company-step states and controlled status vocabulary;
2. Fama–French Step 7 is `EXECUTED` for MSFT, WMT and JPM;
3. cost, participant, WMT/JPM Human Gate and independent-replication gates remain protected;
4. Walmart's February 2024 split correction is present;
5. the primary factor summary has 31 observations per company and all three Digital Twins parse;
6. the 18-task same-session professional-benchmark self-pilot is explicitly non-promotion eligible.

This is bounded artifact/reproducibility validation, not independent scientific replication and not GitHub Actions CI.
