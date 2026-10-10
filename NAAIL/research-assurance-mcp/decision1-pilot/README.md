# Microsoft-Decision-1 × NAAIL / LEMON ICFR — controlled pilot (2026-10-10)

**Status: implemented experimental harness on a review branch; not deployed, independently validated, or clinically/professionally approved.** All included observations are **synthetic**. Neither Microsoft-Decision-1 nor the hosted gateway has been called as part of this commit.

## Purpose and project mapping

- **NAAIL Research Assurance MCP**: evaluates candidate decisions against the evidence passport, traceability, blind benchmark, falsification and Human Gate.
- **LEMON-ICFR-US**: provides control-risk triage *recommendations* from predefined options only; Lemon's independent reviewer/falsification and human gate remain authoritative.
- **POMELO**: policy decision point, versioned provider router, Evidence Passport, independent Blind Gold / VERA evaluation. This public pilot does **not** copy or modify proprietary POMELO code or replace its production promotion gate.
- **AJPT research**: compare (A) deterministic rule baseline, (B) specialized decision model, (C) general-purpose LLM, and (D) hybrid model + independent verification + human approval on equivalent blind cases. Only A is implemented in this artifact; B is an **opt-in adapter**, C/D are prospective experiments.

## Safe quick start

Python 3.11+ (standard library only):

```bash
cd NAAIL/research-assurance-mcp/decision1-pilot
python -m unittest -v test_decision1_pilot.py
python decision1_pilot.py --provider offline --output local_results.json
```

**Offline != Microsoft-Decision-1.** Baseline probabilities deliberately remain `null`, and their Brier score is deliberately omitted.

## Optional hosted Microsoft-Decision-1

The Vercel AI Gateway exposes `microsoft/microsoft-decision-1` via an OpenAI-compatible Decisions API. Obtain your own key, review pricing/data processing, confirm API response schema against your deployment, and explicitly opt into the paid call:

```bash
# set AI_GATEWAY_API_KEY in your OS environment; NEVER commit it
python decision1_pilot.py --provider gateway --confirm-spend --output gateway_results.json
```

Default makes **zero** external calls. Only `data_class=SYNTHETIC` is allowed; adding SEC records or client data requires a separate input-provenance, rights, redaction and temporal-alignment review. The connector fails closed if a decision or probability is missing/invalid. The example adapter has **not** been exercised against the actual hosted model here.

Microsoft Foundry is a separate deployment/authentication option and would require a specific adapter (not silently reused as though the endpoints were identical).

## Evidence and decision controls

1. Risk choices: `HIGH | MODERATE | LOW | INSUFFICIENT` (triage **only**, NOT an assertion that a SOX 404 material weakness exists).
2. Structured input includes only the case ID and referenced synthetic facts. **Gold labels are withheld** from the model's request body.
3. Evidence IDs, synthetic provenance and contradictory evidence are checked **before** model routing.
4. Confidence threshold: 0.85 for routing priority only; **never** autonomous audit approval.
5. Every decision is `AWAITING_INDEPENDENT_HUMAN_APPROVAL`, with `approved=false` and `production_action=null`.
6. Retain provider/model identifier, run time, evidence IDs, candidate-state hash, prompt hash, prediction, uncertainty and reviewer queue. Hashes are *lineage checks*, not proof of factual validity.
7. **No agent can self-certify** or change POMELO knowledge-core policy; unverified results cannot be promoted to released audit conclusions.

## Experimental study protocol (pre-analysis)

- **H1 (accuracy):** decision scoring improves blind ICFR-risk triage accuracy versus an LLM-only arm.
- **H2 (efficiency):** decision scoring reduces response latency and input/output cost per correctly triaged case.
- **H3 (calibration):** calibrated probabilities improve selective prediction (risk–coverage) and Brier/ECE relative to uncalibrated baselines.
- **H4 (safeguards):** independent evidence checks and a human gate reduce unsupported automated conclusions, with potential review costs.
- Randomize case presentation/order and synonyms; freeze model versions and prompt variants; hold out firms, periods and control families; preregister inclusion/exclusion and minimum effect. Case labels require **independent domain expert adjudication**, blinded to candidates.
- Measure per-class precision/recall/F1, macro F1, full-sample accuracy including abstentions, PR-AUC for high-risk, Brier/ECE where calibrated probabilities exist, false-negative/false-positive rates, review burden, p50/p95 latency, token cost and zero unauthorized production actions. Use cluster bootstrap/appropriate paired tests by firm; report confidence intervals and all null effects.
- Synthetic fixtures are software smoke tests **not publishable empirical findings**; next stage needs verified open SEC/XBRL filings, separate extraction, stable identifiers, risk-label adjudication, chronological hold-out, and legally authorized data handling.
- Blind Gold is stored separately from model-accessible features; the current local fixture JSON contains labels for evaluator convenience but the adapter explicitly strips them. For formal tests, store labels in a separately permissioned evaluator vault.

## Official external references

- Microsoft: https://commandline.microsoft.com/microsoft-decision-1-model-foundry/
- Foundry: https://ai.azure.com/catalog/models/Microsoft-Decision-1
- Vercel gateway: https://vercel.com/changelog/microsoft-decision-1-now-available-on-ai-gateway
- Relevant Lemon core: `Lemon-ICFR-US/src/lemon_icfr/` and `Lemon-ICFR-US/tests/test_orchestrator.py`.
- Relevant NAAIL core: `NAAIL/research-assurance-mcp/`.
- Canonical project archive: Google Drive NAAIL Research Assurance MCP (link recorded in project's Drive master index).

### Explicit limitations

No live API responses, public EDGAR extraction, CI execution, model-comparison results, audit opinion or AJPT acceptance claim is created by the pilot. Need independent reviewer approval before integrating with production POMELO or LEMON policies.