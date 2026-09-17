# NAAIL Prototype V1.2 — Falsification & Robustness Record

**Date:** 2026-09-17  
**Run:** `NAAIL-3C-V1.2-2026-09-17-A`  
**Maturity:** `RESEARCH_PROTOTYPE`

## Executed challenges

### F1 — Walmart split contamination
A raw IEX month-end calculation from January 2024 close 165.18 to February 2024 close 58.59 implies **-64.53%**, but Walmart executed a **3-for-1 forward split on 2024-02-26**. Re-expressing the January close on the post-split basis (165.18 / 3 = 55.06) gives a February return of approximately **+6.41%**. The raw unadjusted series is therefore rejected for factor estimation.

**Outcome:** `REVISED_AFTER_CHALLENGE` — the regression input uses split-consistent prices.

### F2 — Dividend sensitivity
The 31-month FF5 models were re-estimated using a monthly cash-dividend-inclusive approximation as a sensitivity check. The central market-beta interpretation is not driven by omitting cash dividends.

**Outcome:** `SUPPORTED_AFTER_CHALLENGE`, subject to the limitation that this is not an exact daily dividend-reinvestment total-return index.

### F3 — Window sensitivity
The primary factor window uses 31 monthly observations (2024-01 through 2026-07). A shorter 19-month window (2025-01 through 2026-07) was also estimated. Coefficients and fit change materially for some firms, especially in the smaller sample.

**Outcome:** `REQUEST_MORE_EVIDENCE` for any strong structural claim based on a single short window. V1.2 reports both windows and does not treat either as causal proof.

### F4 — Factor-source provenance
The U.S. Fama/French 5-factor definition and coverage were verified against the Kenneth R. French Data Library. The executable snapshot is a July-2026 CRSP-vintage mirror whose monthly values cover through 2026-07 and whose source metadata identify the 202607 CRSP database.

**Outcome:** `SUPPORTED_AFTER_CHALLENGE` for reproducibility, while the mirror is retained as a provenance dependency rather than silently presented as the official host.

### F5 — Patent aggregation restraint
Public USPTO/PatentsView availability and representative assignee names were validated, but complete alias/subsidiary entity resolution and bulk aggregation were not completed in this runtime.

**Outcome:** `REQUEST_MORE_EVIDENCE`; aggregate patent counts, forward citations, technology diversity and patent/R&D intensity remain unexecuted.

### F6 — Professional benchmark leakage
A same-session 18-task self-pilot exactly matched the benchmark gold set. Because the same session constructed both gold answers and candidate responses, the result is leakage-prone and cannot support a model-quality claim.

**Outcome:** `REJECTED_BY_FALSIFICATION` for promotion as a performance benchmark. It is retained only as an executed schema/harness check.

### F7 — Sector-comparability constraint
JPMorgan is a bank. Industrial-company measures such as a current ratio or ordinary operating-margin interpretation are not mechanically imposed on the banking Digital Twin.

**Outcome:** `SUPPORTED_AFTER_CHALLENGE`; bank-specific credit-loss, capital and fair-value interpretation remains mandatory.

## Scientific boundary

These challenges improve the prototype but do not establish causal mechanisms, investment performance, production readiness, or independent scientific validation. Failed, revised and unresolved challenges are retained.
