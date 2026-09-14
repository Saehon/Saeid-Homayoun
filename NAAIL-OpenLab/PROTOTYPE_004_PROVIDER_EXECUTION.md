# NAAIL OpenLab™ — Prototype 004 Real-Provider Execution Checkpoint

**Status:** provider harness implemented; empirical provider execution is credential-gated  
**Base release:** v0.2.3 / Prototype 003  
**Architecture target:** V2026.3  
**Updated:** 2026-09-14

## Objective

Prototype 004 executes the frozen Prototype 003 Revenue Recognition benchmark with real model providers under one invariant:

> **Same case. Same evidence. Same hidden gold labels. Same evaluator. Different execution architecture/provider.**

The initial provider pair is:

- Google Gemini via the official `google-genai` SDK;
- Microsoft Foundry model inference via the official `azure-ai-inference` SDK.

## Implemented execution conditions

Each configured provider can execute:

1. **single-agent AI** — one evidence-to-conclusion call;
2. **sequential-agent AI** — Evidence Agent → Risk/Accounting Agent → Review Agent;
3. **governed multi-agent AI** — Evidence Agent → Audit Risk Agent → Accounting/Procedure Agent → Critic/Falsifier → Supervisor.

The deterministic Prototype 003 control remains the common baseline.

## Frozen-input protection

The provider runner removes `gold` from the model-visible case before prompt construction. Input and gold objects are separately hashed for reproducibility. Provider outputs are evaluated only after generation.

A provider may not:

- access frozen gold labels in its prompt;
- change the benchmark case;
- change evidence;
- change the evaluator;
- self-approve the Human Gate;
- silently introduce invented evidence IDs;
- claim scientific or professional superiority without replication and human review.

## Provider configuration

### Google Gemini

Required GitHub secret:

```text
GEMINI_API_KEY
```

Optional repository variable:

```text
GEMINI_MODEL
```

Default model in the adapter: `gemini-2.5-flash`.

### Microsoft Foundry

Required GitHub secrets:

```text
AZURE_INFERENCE_ENDPOINT
AZURE_INFERENCE_CREDENTIAL
AZURE_INFERENCE_MODEL
```

`AZURE_INFERENCE_MODEL` must match the configured Foundry model/deployment identifier for the endpoint.

## GitHub Actions behavior

Workflow: `.github/workflows/prototype_003_runtime.yml`

The workflow:

1. runs the frozen deterministic benchmark and all public contract tests;
2. installs official provider SDKs;
3. executes all three Gemini architecture conditions when Gemini credentials exist;
4. executes all three Microsoft Foundry architecture conditions when Foundry credentials exist;
5. records `NOT_EXECUTED_PROVIDER_REQUIRED` when credentials are absent;
6. uploads provider JSON result artifacts;
7. keeps every run at `PENDING_HUMAN_APPROVAL`.

## Current empirical status

At this checkpoint, the **provider adapters and orchestration harness are implemented**. A provider/model result must not be reported as executed unless its credential-gated job actually completes.

Until that occurs, the scientifically correct status is:

```text
Gemini single-agent                = NOT_EXECUTED_PROVIDER_REQUIRED
Gemini sequential-agent            = NOT_EXECUTED_PROVIDER_REQUIRED
Gemini governed-multi-agent        = NOT_EXECUTED_PROVIDER_REQUIRED
Microsoft Foundry single-agent     = NOT_EXECUTED_PROVIDER_REQUIRED
Microsoft Foundry sequential-agent = NOT_EXECUTED_PROVIDER_REQUIRED
Microsoft Foundry governed-agent   = NOT_EXECUTED_PROVIDER_REQUIRED
```

This status is a feature, not a failure: NAAIL does not convert unexecuted provider conditions into synthetic evidence.

## Initial evaluation fields

- RPA — Risk–Procedure Alignment proxy;
- AA — Assertion Alignment;
- EG — Evidence Grounding;
- PS — Professional Skepticism proxy;
- DS — Documentation Sufficiency;
- precision / recall;
- false positives / false negatives;
- proposed-adjustment match;
- invalid/hallucinated evidence count;
- Human Gate enforcement.

`DIST` requires repeated blinded runs and remains unpopulated for a one-pass provider result.

## Next scientific gate

After credentials are configured and the first real provider artifacts exist:

1. freeze provider/model/version metadata;
2. repeat each provider × architecture condition under a predeclared repetition count;
3. calculate DIST and run-to-run variance;
4. record cost and latency;
5. perform adversarial review and falsification;
6. replicate across the second provider;
7. preserve all null, failed and unfavorable runs;
8. submit provider results to Human Gate review;
9. only then create the first cross-provider empirical comparison table.

No superiority claim is assumed in advance.

## Google Drive mirror

Prototype 004 is mirrored in the NAAIL OpenLab Google Drive archive.

- Drive folder: https://drive.google.com/drive/folders/1m4IrriQ4bPm_O4OVt8s4dRhb_f9ygkFL
- Frozen archive ZIP: https://drive.google.com/file/d/186iK2UbKUAaOOCdZsfbJqhVXCVuIuyCr/view?usp=drivesdk
- Readable checkpoint: https://drive.google.com/file/d/13kHKgHFF72o28CDOi9XpWHQ90qYbd-Tt/view?usp=drivesdk

GitHub remains the source of truth for version-controlled implementation. Google Drive is the synchronized archive/mirror checkpoint.

## Official technical references

- Google Gemini API getting started: https://ai.google.dev/gemini-api/docs/get-started
- Google Gemini 2.5 Flash: https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash
- Microsoft Foundry model inference API: https://learn.microsoft.com/en-us/rest/api/microsoft-foundry/modelinference/
- Microsoft Foundry inference Python quickstart: https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/how-to/quickstart-ai-project

## Governing principle

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**
