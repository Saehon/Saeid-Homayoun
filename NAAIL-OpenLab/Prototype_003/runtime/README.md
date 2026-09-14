# NAAIL OpenLab — Prototype 003 Runtime / Prototype 004 Provider Harness

**Status:** executable public research checkpoint  
**Architecture target:** V2026.3  
**Current public release:** v0.2.3 / Prototype 003  
**Next empirical milestone:** Prototype 004 — real-provider blinded architecture comparison

This directory preserves the Prototype 003 frozen benchmark and now adds a credential-gated Prototype 004 harness for real Google Gemini and Microsoft Foundry model runs.

> **Same case. Same evidence. Same gold labels. Same evaluator. Different execution architecture.**

## Scientific-integrity boundary

Prototype 003 registers four architecture conditions:

1. deterministic baseline — **executed**;
2. single-agent AI — **`NOT_EXECUTED_PROVIDER_REQUIRED`** until a real model runs;
3. sequential-agent AI — **`NOT_EXECUTED_PROVIDER_REQUIRED`** until a real model runs;
4. governed multi-agent AI — **`NOT_EXECUTED_PROVIDER_REQUIRED`** until a real model runs.

Prototype 004 does not simulate provider outputs. A result becomes empirical evidence only after the real provider adapter executes on the same frozen case inputs. Gold labels are never included in provider prompts.

## Current frozen Prototype 003 registry

| Case | Deterministic result | Synthetic amount | Public detailed runtime |
|---|---|---:|---|
| Revenue Recognition & Cut-off | `TX-002`, `TX-003` | EUR 190,000 | Yes |
| Goodwill Impairment | `GW-DR`, `GW-MAR` | EUR 440,000 | Summary only; detailed implementation remains private pending IP review |
| ICFR Deficiency | `CTRL-JE-02`, `CTRL-IT-03` | EUR 530,000 | Summary only; detailed implementation remains private pending IP review |

All benchmark cases require `PENDING_HUMAN_APPROVAL`.

## Prototype 004 provider adapters

### Google Gemini

Implementation: `providers.GeminiProvider` using the official `google-genai` SDK.

Required GitHub secret:

```text
GEMINI_API_KEY
```

Optional repository variable:

```text
GEMINI_MODEL
```

If not set, the adapter uses `gemini-2.5-flash`.

### Microsoft Foundry

Implementation: `providers.FoundryProvider` using the official `azure-ai-inference` SDK.

Required GitHub secrets:

```text
AZURE_INFERENCE_ENDPOINT
AZURE_INFERENCE_CREDENTIAL
AZURE_INFERENCE_MODEL
```

The model value is the Foundry deployment/model identifier configured for the endpoint.

## Architecture conditions executed by a configured provider

`provider_runner.py` supports:

- `single_agent` — one evidence-to-conclusion model call;
- `sequential_agents` — Evidence Agent → Risk/Accounting Agent → Review Agent;
- `governed_multi_agent` — Evidence Agent → Audit Risk Agent → Accounting/Procedure Agent → Critic/Falsifier → Supervisor.

Every executed provider artifact is normalized to the same evaluator contract and forcibly terminates at `PENDING_HUMAN_APPROVAL`. A provider cannot self-approve the Human Gate.

## Local deterministic run

```bash
cd NAAIL-OpenLab/Prototype_003/runtime
python prototype003.py
python -m unittest discover -s tests -v
```

## Local real-provider run

```bash
python -m pip install -r requirements-providers.txt
python provider_runner.py --provider gemini --architecture all
python provider_runner.py --provider foundry --architecture all
```

## GitHub Actions

`.github/workflows/prototype_003_runtime.yml` now has three jobs:

1. frozen deterministic benchmark + contract tests;
2. Gemini real-provider comparison when `GEMINI_API_KEY` is available;
3. Microsoft Foundry real-provider comparison when all required Foundry secrets are available.

When credentials are absent, the workflow records `NOT_EXECUTED_PROVIDER_REQUIRED` rather than fabricating a result. When credentials are present, it uploads JSON result artifacts for all three AI architectures.

## Evaluation

Executed provider runs report:

- RPA — Risk–Procedure Alignment proxy;
- AA — Assertion Alignment;
- EG — Evidence Grounding;
- PS — Professional Skepticism proxy;
- DS — Documentation Sufficiency;
- precision / recall;
- false positives / false negatives;
- adjustment match;
- invalid/hallucinated evidence count;
- Human Gate enforcement.

`DIST` remains unset for a single provider pass and should be populated only after repeated blinded runs under a frozen repetition protocol.

These are engineering benchmark measures. They are not validated professional audit-quality constructs without further empirical validation.

## Official provider documentation used for the adapter contracts

- Google Gemini API Python SDK: https://ai.google.dev/gemini-api/docs/get-started
- Gemini 2.5 Flash model: https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash
- Microsoft Foundry model inference: https://learn.microsoft.com/en-us/rest/api/microsoft-foundry/modelinference/
- Microsoft Foundry Python inference quickstart: https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/how-to/quickstart-ai-project

## Governance invariants

```text
gold_labels_visible_to_provider = false
same_case_across_architectures = true
same_evidence_across_architectures = true
same_gold_labels_across_architectures = true
same_evaluator_across_architectures = true
provider_self_approval_allowed = false
human_gate_required = true
simulated_provider_results_allowed = false
unsupported_discovery_claim_allowed = false
```

The next scientific step is not another architecture document. It is repeated, blinded, frozen-evidence provider execution followed by cross-provider replication, falsification, cost/latency reporting, and human review.
