# Scout Integration — 2026-09-30

This package adds four complementary components to the GitHub-first accounting/audit/finance research stack.

| Component | Role | License / access policy | Decision |
|---|---|---|---|
| APEX-Accounting Harbor | Accounting agent benchmark: reconciliation, accruals, posting, variance analysis, reporting | Public benchmark subset: CC BY 4.0; preserve attribution and benchmark separation | INTEGRATE as sealed external benchmark |
| XOOMAR MCP | Read-only multi-source financial/regulatory MCP data adapter | Code: Apache-2.0; upstream data terms remain separate | TEST/INTEGRATE as read-only adapter; no dataset mirroring |
| OpenEAGO (FINOS) | Governance/control plane for regulated multi-agent systems | Apache-2.0 | INTEGRATE architecture patterns: identity, policy, auditability, HITL |
| HiFi-KPI | SEC/iXBRL-linked KPI/entity research corpus | Research artifact; redistribution remains HOLD until exact artifact license metadata is pinned | TEST as external scientific benchmark; reference-only by default |

## Architecture

SEC / documents / workpapers
        |
        v
Deterministic extraction + XBRL validation
        |
        +--> XOOMAR read-only evidence adapter
        |
        v
Accounting / Audit / Finance Agents
        |
        v
OpenEAGO-style governance control plane
(identity + policy + jurisdiction + audit trail + human gate)
        |
        +--> APEX-Accounting evaluation
        +--> HiFi-KPI scientific evaluation
        |
        v
Falsification / Reviewer
        |
        v
Evidence Passport
        |
        v
Human Approval

## Non-negotiable gates

1. GitHub is canonical for code, manifests, provenance and decisions.
2. External benchmarks stay sealed from development/training outputs.
3. XOOMAR data are queried, not mirrored, unless upstream data terms explicitly permit redistribution.
4. HiFi-KPI is reference-only until the exact dataset/code artifact license is pinned.
5. No benchmark score is recorded until reproducibly executed.
6. Material accounting/audit conclusions require provenance, falsification and human approval.
7. Hugging Face/Kaggle cross-sync occurs only for artifacts with redistribution-compatible licenses.

## Recommended execution order

1. Add APEX public tasks to the evaluation harness.
2. Add XOOMAR as a read-only challenger adapter in Customer-Zero.
3. Implement OpenEAGO-compatible governance metadata around agent calls.
4. Run HiFi-KPI Lite/reference evaluation after license pinning.
5. Cross-sync only PASS artifacts to Hugging Face/Kaggle.
