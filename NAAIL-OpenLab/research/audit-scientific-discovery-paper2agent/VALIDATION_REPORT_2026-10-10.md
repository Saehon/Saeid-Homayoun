# NAAIL Paper2Agent — Verified Engineering Validation
**Verification date:** 2026-10-10 (UTC); **run:** https://github.com/Saehon/Saeid-Homayoun/actions/runs/38087581931
**State:** engineering smoke tests GREEN; independent empirical research BLOCKED.

## Verified source and executable checks
- GitHub Actions job `synthetic-pilot`: SUCCESS.
- **22 / 22 unit tests PASS** across pilot, read-only MCP JSON-RPC, integrated Lemon/CAM, Paper tool contracts, and Bao author-code rights gateway.
- CI ran `python pilot.py --demo`, `python integrated_case.py` using mother Lemon & CAM code, `bao_replication_gateway.py` in rights-aware dry-run.
- Signed scientific approval: NO. CI confirmed `scientific_discovery_claim_allowed=false` and Human Gate `REQUIRED_NOT_GRANTED`.
- Original Bao MATLAB empirical replication: **NOT RUN**. Gateway returned DRY_RUN_ONLY because MATLAB, an authorized local author-code checkout and original data were not supplied.
- External Google Co-Scientist or AlphaEvolve: **NOT RUN**. Only bounded, deterministic, locally authored conceptual implementations were executed.

## Reproducible synthetic test composition
- 80 deterministic synthetic cases, labelled SYN-2018 through SYN-2025.
- Training 2018–2022: 50; validation 2023: 10; untouched selection holdout 2024–2025: 20.
- **Do not interpret toy labels as real fraud, restatement or ICFR deficiencies.**

| Architecture | Brier (20 holdout) | Precision at top 20% | Reviewable with evidence gate |
|---|---:|---:|---:|
| A0 toy heuristic | 0.1499 | 1.000 | 20/20 |
| A1 identical score + evidence gate | 0.1499 | 1.000 | 18/20 |
| A2 training-based Co-Scientist-style candidate ranking | 0.1431 | 1.000 | 18/20 |
| A3 validation-based AlphaEvolve-style bounded search | 0.1426 | 1.000 | 18/20 |

All numbers are **synthetic software-demo metrics**. A tiny, procedurally generated holdout with ceiling precision cannot establish superiority, external validity, statistical significance or auditor decision quality.

## Integration and protocol
- Local MCP server supports initialize / tools-list / tools-call / ping with 4 read-only tools and no network/paid inference.
- An actual Python module import executes `LemonOrchestrator` from existing Lemon and the `score_rows` method from existing NAAIL CAM benchmark, both on generated artificial evidence.
- Lemon result: `AWAITING_HUMAN_APPROVAL`; the CAM benchmark's composite score is explicitly **not** validated audit quality.
- No actual independent second-model reviewer; simulation challenger is declared as simulated.

## Outstanding scientific blockers
1. Original corrected Bao MATLAB RUSBoost author code and authorized data with rights check; reconcile original published tables/metrics and 2022 correction.
2. Chronology-verified SEC/AAER/PCAOB, CAM, material-weakness and actual independent labels.
3. Real agent adapters, host-specific paper skill conversion, actual deployed MCP client test, optional hosted service and controlled real model evaluations.
4. Blinded expert auditor study, preregistration, independent external replication, falsification, risk–CAM prior-art analysis, and institutional research ethics review if needed.
5. Real manuscript results and publication submission.

## Storage
- Canonical Drive: https://drive.google.com/drive/folders/1iXOWJSYIZFhiXZReULHcp9ajatdSaUAB
- GitHub PR (draft, not merged): https://github.com/Saehon/Saeid-Homayoun/pull/164
- CI evidence: https://github.com/Saehon/Saeid-Homayoun/actions/runs/38087581931

**Gate judgment:** S0–S5 engineering completed or implemented as recorded in STAGE_GATES.md; S6–S11 scientifically not completed. Leave PR draft for human science and IP review.
