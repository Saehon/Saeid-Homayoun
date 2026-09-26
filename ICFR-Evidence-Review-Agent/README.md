# ICFR Evidence Review Agent

**Objective:** build a commercial, evidence-traceable AI agent for ICFR/SOX evidence review and prepare it for sale as a SaaS/AI agent, including Microsoft Marketplace.

## Customer problem

SOX/ICFR teams spend substantial professional time collecting evidence, matching evidence to controls, identifying missing or stale support, documenting exceptions, reviewing conclusions, and preserving an audit trail.

## Product promise

**Upload evidence → map to control → deterministic tests → AI review → independent challenge → Human Gate → Evidence Passport/report.**

The agent assists professional review. It does not issue an audit opinion and does not replace management, internal audit, external audit, or other professional judgment.

## Product architecture

1. Evidence intake
2. Control/evidence mapping
3. Deterministic validation
4. Primary AI evidence-review agent
5. Risk/exception engine
6. Independent reviewer/challenger
7. Evidence Passport
8. Human Approval gate
9. Export/API/dashboard
10. Enterprise identity, security and billing

## Darwin product system

The commercial child uses a Darwin product operating system plus a forward-deployed learning loop:

- [Darwin Product OS](DARWIN_PRODUCT_OS.md)
- [Forward-Deployed / Customer-Zero Playbook](FORWARD_DEPLOYED_PLAYBOOK.md)
- [Venture Stage Gates](VENTURE_GATES.md)
- [Vercel + Azure Production Architecture](VERCEL_AZURE_ARCHITECTURE.md)

The stable product core remains auditable. Customer deployments generate learning that is promoted into the core only when reusable, rights-cleared and testable.


## Private R&D factory boundary

The detailed **Frankenstein for Lemon** architecture is maintained in the private Lemon R&D environment and is intentionally not reproduced in this public repository.

Public product development follows the high-level relationship:

**Mother / governance source → private Frankenstein builder → validation and graduation gates → Lemon-ICFR-US commercial product.**

Only validated, rights-cleared and deliberately publishable components graduate into this repository. See [Frankenstein → Lemon Public Boundary](FRANKENSTEIN_PUBLIC_BOUNDARY.md).

## Child-project rule

This directory is the commercial child project. The original research projects remain unchanged.

- `mother-reference/` contains snapshots of relevant research material for provenance/design reference.
- `prototype/` is the clean commercial runtime prototype.
- Third-party or research-only material in `mother-reference/` must not automatically be redistributed or embedded in the commercial product. License and rights review is mandatory before reuse.

## Prototype status

### V0 — deterministic evidence review
- control/evidence schema
- required-evidence matching
- evidence gaps and risk triage
- Evidence Passport
- Human Gate
- CI tests

### V1 — Darwin / multi-model scaffold
- provider-neutral AI review contract
- optional Vercel AI Gateway adapter
- primary + independent challenger orchestration
- unsupported evidence-basis detection
- escalation when models disagree
- synthetic Customer-Zero benchmark
- Human Gate remains locked regardless of model output

### V2 — Customer Zero regression benchmark
- 20 synthetic ICFR control/evidence cases across five control families
- explicit wrong-period, stale, conflicting, duplicate, no-evidence and prompt-injection cases
- deterministic exception flags and evidence-lineage checks
- benchmark precision/recall and false-positive/false-negative reporting
- controlled GPT vs Claude vs IBM Granite experiment plan
- Human Gate and provider-neutral architecture remain unchanged

See [Customer Zero V2](CUSTOMER_ZERO_V2.md) and [Model Benchmark Plan](MODEL_BENCHMARK_PLAN.md).

## First sellable MVP

The MVP reviews one control at a time and produces:

- control ID and objective
- evidence received
- required-evidence coverage
- missing evidence / exception list
- evidence freshness/completeness flags
- preliminary risk level
- primary model review
- independent challenger result
- disagreement/escalation status
- evidence hash and provenance record
- Human Gate status
- exportable JSON result

See `DEVELOPMENT_STAGES.md` for the end-to-end path.
