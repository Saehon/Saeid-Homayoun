# NAAIL OpenLab™ — Stage 2B Independent Blind Model Run Gate V1.3B

**Date:** 2026-09-17  
**Stage:** `2B — Independent Blind Model Runs`  
**Current status:** `REGISTERED_NOT_EXECUTED`  
**Blocking condition:** no independently invoked candidate-model run has yet been observed under the frozen V1.3B packet  
**Maturity:** `RESEARCH_PROTOTYPE`

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Goal

Obtain genuinely independent model outputs on the same frozen private V1.3B task packet without exposing the private gold key. A same-session self-comparison, copied answer, simulated provider response or manually reconstructed output is not promotion-eligible evidence.

## Entry conditions

Stage 2B may execute a candidate only when all of the following are true:

1. the V1.3B task packet and gold key are frozen;
2. the evidence manifest is frozen by source artifact and Git blob SHA;
3. the candidate is invoked in a fresh independent provider/model session;
4. the candidate receives the same task order and evidence condition as comparable candidates;
5. the private gold key is inaccessible to the candidate context;
6. run telemetry can be observed or explicitly recorded as unavailable;
7. raw responses can be frozen before scoring.

## Minimum candidate-run evidence

For each candidate run preserve:

- `run_id` and `candidate_id`;
- provider, model and model/version identifier;
- UTC timestamp and fresh session/run identifier;
- V1.3B packet version and evidence-hash set;
- browsing mode and tool-access condition;
- inference settings where exposed;
- complete raw response artifact;
- SHA-256 of the raw response artifact;
- observed latency;
- input/output token counts where exposed;
- observed API/provider cost or explicit `UNAVAILABLE`;
- pricing-source provenance where cost is reported;
- run result: `EXECUTED`, `FAILED_CALL`, `REFUSED`, `NULL_OUTPUT`, or `BLOCKED_PROVIDER`;
- notes sufficient to reproduce the invocation condition.

## Failure-preservation rule

Failed calls, missing telemetry, refusals, null responses and provider-access failures remain part of the scientific record. They are never replaced by synthetic responses and are never silently excluded from denominators where the registered scoring rule requires their inclusion.

## Current execution finding

In the current ChatGPT execution environment, no separate connected inference service is available that can be invoked as an independent candidate while preserving the V1.3B blind-run controls. The active assistant cannot create multiple supposedly independent model observations by answering the packet itself in the same conversation.

Accordingly, Stage 2B is **not marked executed**. This is a controlled blocked dependency, not a benchmark result.

## What is executable now

The following Stage 2B infrastructure is valid to publish before candidate runs:

- candidate roster / provider-access ledger;
- run-manifest template;
- raw-response freeze ledger;
- response hashing and failure-preservation protocol;
- candidate-comparability rules;
- provider-blocked status record.

These are execution controls, not model performance evidence.

## Exit rule

Stage 2B may close only after at least the registered candidate set has been invoked independently and each observed/failed run has a frozen response/failure record and run manifest. Only then may Stage 2C open the private gold key for blinded scoring.

Until that condition is met:

- Stage 2C remains dependent and not executed;
- CVPO remains `NOT_EXECUTED`;
- Phase 2 remains open;
- no Human Gate or independent-replication status changes;
- Phase 3 and Phase 4 are not promoted.
