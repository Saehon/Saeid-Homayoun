# Position-specific project evidence matrix

**Snapshot date: 2026-10-31.** Inventory drawn from GitHub account and open PR metadata. This record intentionally does **not** substitute an independent review, deployment audit, real-model benchmark, or up-to-date employment vacancy check.

| Priority | Target capability | Reviewable changes | Visibility | Development level | Independent approval |
|---|---|---|---|---|---|
| 1 | Google DeepMind — Finance Expert Lead | [PR #195](https://github.com/Saehon/Saeid-Homayoun/pull/195) | public | Synthetic specification/tests, open PR | Not verified |
| 2 | OpenAI — GRC Program Manager, Audit & Controls | [PR #3](https://github.com/Saehon/IFRS-AI-Inspector/pull/3) | public | Synthetic specification/tests, open PR | Not verified |
| 3 | OpenAI — Frontier Assurance | [PR #16](https://github.com/Saehon/Saeid-Homayoun-Test/pull/16) | public | Synthetic specification/tests, open PR | Not verified |
| 4 | OpenAI — Research Program Manager, Governance | [PR #4](https://github.com/Saehon/RISK-INDEX/pull/4) | private | Synthetic specification/tests, open PR | Not verified |
| 5 | Anthropic — Audit Operations Lead | [PR #5](https://github.com/Saehon/IFRS-PCAOB-AI/pull/5) | private | Synthetic specification/tests, open PR | Not verified |
| 6 | Google — Finance Subject Matter Expert | [PR #1](https://github.com/Saehon/MACEI-AI-Cost-Manag/pull/1) | private | Synthetic specification/tests, open PR | Not verified |
| 7 | OpenAI — Applied AI Architect, Education | [PR #17](https://github.com/Saehon/Saeid-Homayoun-Test/pull/17) | public | Synthetic specification/tests, open PR | Not verified |
| 8 | Anthropic — Finance Data Science | [PR #2](https://github.com/Saehon/MACEI-AI-Cost-Manag/pull/2) | private | Synthetic specification/tests, open PR | Not verified |
| 9 | Anthropic — International Finance Program Management | [PR #4](https://github.com/Saehon/IFRS-AI-Inspector/pull/4) | public | Synthetic specification/tests, open PR | Not verified |

## Evidence definitions

- **Code present / CI:** code and automated checks exist in the PR branch. Some prior GitHub Actions runs passed, but recheck the **latest PR head** before asserting current build status.
- **Synthetic test:** deliberately constructed inputs used to verify deterministic control logic. It is not a blind research sample or actual LLM performance test.
- **Model evaluation:** requires actual preserved model outputs, model/version/prompt data, timing, authorized input provenance and appropriate independent adjudication.
- **Private PR:** recruiters without repository permission cannot inspect code. A sanitized, licensed, independently reviewable public derivative may be considered after intellectual property review.
- **Independent approval:** requires a named and qualified human reviewer, documented conflicts, reproducibility evidence, and a recorded decision. No approvals are asserted here.

## High-impact next gates

1. Confirm all latest GitHub Actions checks pass, including new tests and static analysis, without bypassing security.
2. Resolve review automation failures in the Finance and Frontier PRs, and obtain independent technical plus accounting/audit reviewer sign-off.
3. Execute a small, duly licensed financial benchmark with model-provider terms and approved data transmission; preserve source hashes and invoices/usage.
4. Generate a verified, comparable results table and failure taxonomy for at least two model outputs on the same inputs; distinguish deterministic tests from independent empirical performance.
5. Keep original research public only when permissions and prepublication/IP clearance allow it.

**Project registry:** [catalog.json](catalog.json). Machine checks are offline and do not check GitHub remote state.
