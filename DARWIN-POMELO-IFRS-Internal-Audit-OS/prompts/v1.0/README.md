# DARWIN-POMELO Prompt Suite v1.0

This folder contains provider-specific master prompts and the canonical cross-model contract.

## Files
- `00_CROSS_MODEL_INTERFACE_AND_HANDOFF_PROTOCOL.md` — shared contract.
- `01_ANTIGRAVITY_CONTROL_PLANE_MASTER_PROMPT.md` — orchestration/control plane.
- `02_POMELO_ROUTER_COST_GOVERNOR_MASTER_PROMPT.md` — routing, materiality, token/cost governance.
- `03_GPT_BUILDER_MASTER_PROMPT.md` — builder, accounting/quantitative reasoning, coding.
- `04_CLAUDE_CHALLENGER_FALSIFIER_MASTER_PROMPT.md` — independent challenge and falsification.
- `05_GEMINI_VERIFIER_EXECUTOR_MASTER_PROMPT.md` — evidence verification and Google-native execution.
- `06_IBM_GRANITE_LOCAL_FIRST_MASTER_PROMPT.md` — local/open-source first-pass worker.
- `07_SCIENCE_BENCHMARK_REPLICATION_MASTER_PROMPT.md` — benchmark, replication, OOS and falsification.
- `08_HUMAN_GATE_REVIEWER_MASTER_PROMPT.md` — final accountable review.

## Runtime
Antigravity → POMELO → cheapest defensible route → specialist model → independent challenge when material → verification → science/replication when required → DARWIN value layer → Human Gate.

Word copies are stored in the matching Google Drive project folder under `Prompt-Suite-v1.0`.
