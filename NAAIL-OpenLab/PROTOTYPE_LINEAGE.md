# NAAIL OpenLab™ — Prototype Lineage and Status

**Canonical date:** 2026-09-15  
**Public release:** v0.2.3

This file prevents milestone-name drift across the NAAIL OpenLab repository. Prototype numbers identify different engineering/empirical layers and must not be used interchangeably.

## Prototype 002 — original deterministic revenue baseline

Status: **historical frozen baseline**.

Purpose: establish the first governed Audit Digital Twin control condition for Revenue Recognition & Cut-off.

Key rule: results apply only to the deliberately constructed synthetic benchmark and are not real-world audit-effectiveness claims.

## Prototype 003 — three-case synthetic benchmark

Status: **executed deterministic benchmark / active research baseline**.

Frozen domains:

1. Revenue Recognition & Cut-off;
2. Goodwill Impairment;
3. ICFR Deficiency.

The deterministic control condition is executed. Provider-based single-agent, sequential-agent and governed multi-agent comparisons require actual provider execution and may not be replaced with simulated results.

## Prototype 003-C — SEC-anchored evidence extension

Status: **engineering scaffold implemented; empirical evidence pipeline incomplete**.

Prototype 003-C is a research extension, not a replacement name for the synthetic three-case Prototype 003 benchmark.

Exactly three public-company SEC anchors are permitted:

- Microsoft Corporation (`MSFT`, CIK `0000789019`);
- Alphabet Inc. (`GOOGL`, CIK `0001652044`);
- Amazon.com, Inc. (`AMZN`, CIK `0001018724`).

Real-company evidence is restricted to SEC EDGAR / Form 10-K / iXBRL. No fourth issuer may enter without an explicit versioned scope change.

Implemented:

- issuer scope lock;
- pinned filing accessions;
- SEC ingestion scaffold;
- source-manifest contract;
- SHA-256 hashing contract;
- fourth-issuer rejection tests;
- real-evidence / controlled-scenario interpretation firewall;
- GitHub Actions validation.

Not yet complete:

- live raw-source ingestion;
- persisted raw-source hashes from a completed live run;
- normalized evidence tables;
- Evidence Passport™ records from the live source objects;
- controlled SEC-anchored benchmark scenarios;
- frozen scenario gold labels;
- complete architecture-comparison matrix.

Real SEC evidence is immutable. Synthetic perturbations and benchmark gold labels must remain in separate namespaces and must never be represented as actual Microsoft, Alphabet or Amazon audit/accounting findings.

## Prototype 004 — provider execution harness

Status: **infrastructure implemented; empirical provider runs credential-gated**.

Purpose: execute the frozen benchmark through real provider/model conditions while preserving identical evidence/gold/evaluator contracts.

Implemented provider-harness families include Google Gemini and Microsoft Foundry interfaces. A configured adapter is infrastructure only; it is not an empirical result until a credential-gated run produces a validated artifact.

Canonical result states:

- `EXECUTED` — a real validated run artifact exists;
- `NOT_EXECUTED_PROVIDER_REQUIRED` — provider infrastructure exists but credentials/run artifact do not;
- `FAILED_VALIDATION` — a real run occurred but failed the frozen validation contract.

## Research invariants

For synthetic and SEC-anchored comparative experiments:

**Same source/case evidence. Same controlled scenario. Same frozen gold labels. Same evaluator. Different execution architecture/provider.**

Every material conclusion remains subject to:

- Evidence Passport™;
- Professional Decision DAG™;
- Human Gate;
- provenance/version manifests;
- frozen metric definitions;
- failure/null-result preservation;
- reproducibility and leakage controls.

## Release rule

The public software/documentation release number is separate from prototype numbering.

**Current public release: v0.2.3.**

Do not infer a v0.3.0 software release merely because Prototype 003 or Prototype 004 exists. A later release requires its own frozen release checklist, reproducibility evidence, rights/IP review and Human Gate approval.

## Canonical navigation

- `CURRENT_PROJECT_STATE.md` — current overall state.
- `PROTOTYPE_STATUS_V0.4.md` — public executable benchmark status.
- `PROTOTYPE_003C_SEC_SCOPE.md` — three-company SEC scope.
- `PROTOTYPE_003C_SEC_EVIDENCE_SNAPSHOT.md` — public SEC evidence checkpoint.
- `PROTOTYPE_003C_IMPLEMENTATION_STATUS.md` — P003-C engineering state.
- `PROTOTYPE_004_PROVIDER_EXECUTION.md` — provider-harness state.
- `LATEST_UPDATE_2026-09-15.md` — latest dated checkpoint.

GitHub is the canonical source of truth. Google Drive is a mirror/archive.