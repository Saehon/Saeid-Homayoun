# NAAIL OpenLab™ — Current Project State

**Canonical public state date:** 2026-09-14  
**Public release:** v0.2.3  
**Executable milestone:** Audit Workspace V0.4 / Prototype 003  
**Prototype 004 state:** real-provider harness implemented; empirical execution remains credential-gated  
**Architecture snapshot:** V2026.3 — Google + Microsoft Multi-Agent Digital Twin Scientific Discovery Architecture  
**Research-testing extension:** FT50 / AJG 4* Scientific Replication Arena — registry and protocol integrated; benchmark execution pending exact commit pinning and environment reconstruction

## Purpose

This is the compact public checkpoint for NAAIL. It separates validated deterministic benchmark results, implemented provider infrastructure, architecture targets, external replication infrastructure, and provider/model experiments that have or have not actually executed.

## Current validated Prototype 003 benchmark

Prototype 003 is a frozen three-domain synthetic Audit Digital Twin benchmark:

| Case | Deterministic control finding | Synthetic amount | Human Gate |
|---|---|---:|---|
| Revenue Recognition & Cut-off | `TX-002`, `TX-003` | EUR 190,000 proposed adjustment | `PENDING_HUMAN_APPROVAL` |
| Goodwill Impairment | `GW-DR`, `GW-MAR` | EUR 440,000 estimated adjustment | `PENDING_HUMAN_APPROVAL` |
| ICFR Deficiency | `CTRL-JE-02`, `CTRL-IT-03` | EUR 530,000 estimated exposure | `PENDING_HUMAN_APPROVAL` |

For these deliberately constructed frozen synthetic cases, the deterministic control condition has precision/recall of **1.00 / 1.00** with **0 / 0** false positives/false negatives. These values are benchmark properties only and are not claims of real-world audit effectiveness, impairment measurement, ICFR severity, or professional assurance quality.

## FT50 / AJG 4* Scientific Replication Arena — integrated

NAAIL now contains a governed external benchmark layer for selected public replication repositories associated with FT50 and AJG/ABS 4/4* research.

Current integrated assets:

- `benchmarks/ft50_abs4/README.md`;
- `benchmarks/ft50_abs4/registry.json`;
- `benchmarks/ft50_abs4/BENCHMARK_PROTOCOL.md`;
- `benchmarks/ft50_abs4/validate_registry.py`;
- `tests/SCIENTIFIC_REPLICATION_ARENA.md`;
- `external/FT50_ABS4_SOURCE_POLICY.md`;
- formal Layer 7 integration in `EVALUATION_STANDARD.md`.

Initial benchmark families cover Management Science accounting/reproducibility, Review of Financial Studies reproducibility and machine learning, Journal of Financial Economics staggered-DiD/causal inference, and Journal of Finance end-to-end empirical replication.

Scientific status:

```text
benchmark registry                = IMPLEMENTED
rights/provenance policy          = IMPLEMENTED
replication protocol              = IMPLEMENTED
registry validator                = IMPLEMENTED
exact external commit pinning     = PENDING
reconstructed environments        = PENDING
original-result replications      = NOT_YET_EXECUTED
clean-room reproductions          = NOT_YET_EXECUTED
temporal/OOS benchmark runs       = NOT_YET_EXECUTED
cross-dataset/Digital Twin tests  = NOT_YET_EXECUTED
```

Top-journal publication status is not treated as evidence of reproducibility by itself. NAAIL requires source verification, rights review, exact commit pinning, environment reconstruction, replication, robustness, falsification, temporal/OOS testing where appropriate, Chain-of-Evidence, and Human Gate.

## Prototype 004 provider harness — implemented

The public runtime now contains real-provider adapters for:

- **Google Gemini** through the official `google-genai` SDK;
- **Microsoft Foundry model inference** through the official `azure-ai-inference` SDK.

For each configured provider, the harness supports:

1. single-agent AI;
2. sequential-agent AI — Evidence → Risk/Accounting → Review;
3. governed multi-agent AI — Evidence → Audit Risk → Accounting/Procedure → Critic/Falsifier → Supervisor.

Canonical implementation:

[Prototype_003/runtime](./Prototype_003/runtime/README.md)

Provider execution checkpoint:

[PROTOTYPE_004_PROVIDER_EXECUTION.md](./PROTOTYPE_004_PROVIDER_EXECUTION.md)

### Scientific-integrity protection

- provider prompts exclude the frozen `gold` object;
- case/gold objects are separately hashed;
- identical frozen evidence is used across architecture conditions;
- invented evidence IDs are explicitly flagged;
- provider output cannot approve the Human Gate;
- GitHub Actions records missing credentials as `NOT_EXECUTED_PROVIDER_REQUIRED` rather than generating substitute results;
- provider result artifacts are uploaded only after a real provider job runs.

## Architecture-comparison empirical state

The deterministic control is executed. The provider harness is implemented, but a model condition is not empirical evidence until the credential-gated provider job completes.

Current scientifically valid status unless a provider artifact proves otherwise:

```text
deterministic baseline              = EXECUTED
Gemini single-agent                 = NOT_EXECUTED_PROVIDER_REQUIRED
Gemini sequential-agent             = NOT_EXECUTED_PROVIDER_REQUIRED
Gemini governed-multi-agent         = NOT_EXECUTED_PROVIDER_REQUIRED
Microsoft Foundry single-agent      = NOT_EXECUTED_PROVIDER_REQUIRED
Microsoft Foundry sequential-agent  = NOT_EXECUTED_PROVIDER_REQUIRED
Microsoft Foundry governed-agent    = NOT_EXECUTED_PROVIDER_REQUIRED
```

NAAIL never substitutes simulated, deterministic, or placeholder outputs for a missing provider/model run.

## GitHub Actions provider gate

Workflow: `.github/workflows/prototype_003_runtime.yml`

The workflow performs:

- frozen deterministic benchmark tests;
- provider-contract and gold-leakage tests;
- Gemini execution when `GEMINI_API_KEY` exists;
- Microsoft Foundry execution when `AZURE_INFERENCE_ENDPOINT`, `AZURE_INFERENCE_CREDENTIAL`, and `AZURE_INFERENCE_MODEL` exist;
- result validation and artifact upload;
- mandatory `PENDING_HUMAN_APPROVAL` enforcement.

## V2026.3 architecture checkpoint

V2026.3 remains the frozen next-generation architecture target. It defines a provider-neutral design incorporating, where useful and legally appropriate:

- Google ADK / Antigravity-style agent engineering;
- Microsoft Agent Framework;
- A2A + MCP interoperability;
- GraphRAG + NAAIL Digital Twin integration;
- Co-Scientist-style hypothesis generation, critique and ranking;
- ERA-style empirical conversion;
- AlphaEvolve-inspired evaluator-guided search;
- AlphaFold/DeepMind-inspired latent-structure reasoning;
- Computational Discovery;
- Science One-style Chain-of-Evidence;
- AI-to-AI Critic / Defender / Replicator / Falsifier roles;
- Professional Decision DAG™;
- Rights & License gating;
- temporal/out-of-sample validation;
- clean-room replication;
- mandatory Human Gate.

Architecture snapshot: [versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md](./versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md)

## Scientific experimental invariant

**Same case. Same evidence. Same frozen gold labels. Same evaluator. Different execution architecture/provider.**

Provider/model adapters may not change gold labels, bypass Evidence Passport™, bypass the Decision DAG, bypass Human Gate, silently alter the evaluation contract, or access Blind Gold labels during generation.

For external-replication studies, add a second invariant:

**Same published source. Same pinned commit. Same declared environment. Same reconstruction rules. Alternative methods are evaluated against the same frozen empirical target.**

## Evaluation contract

Track at minimum:

- RPA — Risk–Procedure Alignment;
- AA — Assertion Alignment;
- EG — Evidence Grounding;
- PS — Professional Skepticism;
- DS — Documentation Sufficiency;
- DIST — Decision/Inference Stability;
- precision / recall;
- false positives / false negatives;
- invalid/hallucinated evidence references;
- evidence/citation traceability;
- reproducibility;
- latency and execution cost;
- human overrides and reasons;
- replication fidelity;
- specification stability;
- causal/identification robustness where applicable;
- temporal/OOS stability;
- falsification survival;
- provenance completeness.

`DIST` requires repeated blinded provider runs and is not inferred from a single run.

## Next empirical gate

Two empirical tracks now run in parallel.

### Provider-comparison track

Once provider credentials are configured and real result artifacts exist:

1. freeze provider/model/version metadata;
2. repeat every provider × architecture condition under a predeclared repetition count;
3. populate DIST and run-to-run variance;
4. record cost and latency;
5. conduct adversarial review and falsification;
6. replicate across the second provider;
7. retain failed/null/unfavorable runs;
8. submit results to Human Gate review;
9. create the first cross-provider empirical comparison table.

### FT50/AJG replication track

1. verify publication/repository association and applicable rights;
2. pin the exact Git commit for each selected benchmark;
3. freeze environment and dependency metadata;
4. reproduce the original published/archived result where technically possible;
5. run an independent or clean-room implementation;
6. add alternative specifications and estimators without optimizing for favorable p-values;
7. run temporal/OOS, placebo, falsification and cross-dataset tests where applicable;
8. preserve failed and null replications;
9. produce a NAAIL benchmark card and Chain-of-Evidence;
10. submit interpretation to Human Gate.

No superiority or reproducibility claim is assumed in advance.

## First empirical research questions

**Provider architecture:** Does governed multi-agent audit orchestration improve evidence grounding and professional judgment relative to single-agent AI?

**External replication:** Which published empirical conclusions remain stable under exact replication, independent reproduction, alternative specifications, temporal/OOS validation, and adversarial falsification?

The benchmark system is designed to test these questions, not prove a preferred architecture, journal, model, or method.

## Public / private boundary

**Public:** research-safe documentation, synthetic benchmark descriptions, deterministic summary results, selected reproducibility code, provider adapter code, external benchmark manifests/metadata, citation metadata, governance/evaluation rules and credential-gated provider harness.

**Private:** provider credentials, patent-sensitive orchestration, detailed Goodwill/ICFR implementation, unpublished prompts/agent specifications, restricted data, private benchmark extensions, pre-commercial logic and unreleased experimental results.

**Third-party external replication assets:** retain their original ownership and licenses; registry inclusion does not transfer rights to NAAIL.

## Scientific rule

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**

No model output, agent consensus, statistical significance, journal prestige, or predictive accuracy is automatically treated as a scientific discovery.

## Canonical links

- NAAIL OpenLab: https://github.com/Saehon/Saeid-Homayoun/tree/main/NAAIL-OpenLab
- FT50/AJG 4* Benchmark Lab: https://github.com/Saehon/Saeid-Homayoun/tree/main/NAAIL-OpenLab/benchmarks/ft50_abs4
- Scientific Replication Arena: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/tests/SCIENTIFIC_REPLICATION_ARENA.md
- Public runtime: https://github.com/Saehon/Saeid-Homayoun/tree/main/NAAIL-OpenLab/Prototype_003/runtime
- Prototype 004 provider execution: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/PROTOTYPE_004_PROVIDER_EXECUTION.md
- Prototype status: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/PROTOTYPE_STATUS_V0.4.md
- V2026.3 architecture: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md
- Companion multi-agent engineering repository: https://github.com/Saehon/Google-Antigravity-using-a-multi-agent-BERT-architecture
- ORCID: https://orcid.org/0000-0002-2536-0446

GitHub remains the source of truth. Google Drive is a private mirror/archive unless explicitly changed.
