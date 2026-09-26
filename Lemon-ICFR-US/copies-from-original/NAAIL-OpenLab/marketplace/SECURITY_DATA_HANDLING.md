# NAAIL OpenLab™ Marketplace Security & Data Handling

## Purpose

This document defines the minimum public security, privacy, data-governance, and human-control requirements for any NAAIL OpenLab distribution adapter.

## Core principles

1. **Data minimization** — collect and transmit only data required for the active research task.
2. **Purpose limitation** — user-provided data must not be silently repurposed for unrelated model training, benchmarking, advertising, or profiling.
3. **Least privilege** — every agent and tool receives only the permissions required for its current task.
4. **Tenant isolation** — production deployments must prevent cross-user or cross-tenant data leakage.
5. **Rights before retrieval** — licensed, restricted, confidential, personal, and copyrighted materials must pass a rights/policy gate before use.
6. **Evidence provenance** — material evidence should carry source, timestamp/version, transformation, and rights metadata where practicable.
7. **Human Gate** — consequential scientific, audit, accounting, assurance, financial, or professional conclusions require explicit human review/approval.
8. **No fabricated execution** — unavailable provider/tool runs must be represented as not executed; they must never be replaced with simulated empirical outcomes and reported as real.

## Data classes

### Class A — Public / synthetic
Publicly distributable documentation, synthetic Digital Twin cases, public metadata, open datasets used consistently with their licenses, and research-safe examples.

### Class B — User confidential
Unpublished manuscripts, working papers, uploaded datasets, internal documents, draft analyses, or organization-specific material supplied by a user.

### Class C — Restricted / licensed
Licensed databases, copyrighted standards text, contractual datasets, private repositories, paid journal content, or material whose redistribution is limited.

### Class D — Secrets / credentials
API keys, OAuth tokens, passwords, private signing keys, provider secrets, database credentials, and other authentication material. These must never be committed to the public repository or exposed in model-visible outputs.

## Logging

Production logging should:

- default to metadata and event-level traces rather than raw sensitive payloads;
- redact secrets and high-risk identifiers;
- maintain access controls;
- define retention periods;
- preserve sufficient information for incident review and reproducibility without creating an unnecessary copy of confidential datasets.

## Prompt-injection and tool-abuse controls

All marketplace adapters must treat retrieved documents, web content, user uploads, and tool results as untrusted inputs. The orchestration layer should separate instructions from evidence, validate tool parameters, constrain file/network access, and require confirmation for consequential or irreversible actions.

## Model/provider boundary

Provider-specific adapters must be replaceable. The core research record should preserve, where technically feasible:

- provider/model identifier;
- model/version or deployment identifier;
- execution timestamp;
- tool calls and material parameters;
- evidence IDs;
- limitations/failures;
- human override/approval state.

## Research and professional claims

NAAIL is a research platform, not an autonomous substitute for qualified professional judgment. AI output, agent agreement, model confidence, statistical significance, or benchmark performance alone does not constitute an approved scientific or professional conclusion.

## Incident response baseline

A production release must define an owner for security/privacy incidents, a method for users to report issues, a process to revoke credentials or disable compromised tools, and a documented path to patch or withdraw a marketplace version when necessary.
