# RW2012 — Specification Extraction

Status: ESTIMAND-VERIFIED / COEFFICIENTS-PENDING / NOT M1-LOCKED

Paper: Rice & Weber (2012), Journal of Accounting Research 50(3), 811–843.
Estimand: P(report existing MW during misstatement period | underlying control weakness/restating-firm design).
Design purpose: separate detection/disclosure incentives from existence of weakness.
Verified directional factors:
Negative association: external capital needs, firm size, non-audit fees, presence of a large audit firm.
Positive association: financial distress, auditor effort, previously reported control weaknesses/restatements, recent auditor changes, recent management changes.
Generalizability warning: sample is constructed from restating firms linked to underlying control weaknesses.

DARWIN gate:
- Estimand: PASS and classified as REPORTING | UNDERLYING MW.
- Exact regression table/column: PENDING.
- Coefficients/intercept/SE: PENDING.
- Exact variable construction: PENDING.
- Replication package: PENDING.
- M1 common ensemble with DGM/ACK: FAIL unless a structural multi-stage model is explicitly used.
Decision: HOLD FOR PRIMARY TABLE EXTRACTION.
