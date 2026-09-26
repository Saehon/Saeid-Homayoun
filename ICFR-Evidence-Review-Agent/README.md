# ICFR Evidence Review Agent

**Objective:** build a commercial, evidence-traceable AI agent for ICFR/SOX evidence review and prepare it for sale as a SaaS/AI agent, including Microsoft Marketplace.

## Customer problem

SOX/ICFR teams spend substantial professional time collecting evidence, matching evidence to controls, identifying missing or stale support, documenting exceptions, reviewing conclusions, and preserving an audit trail.

## Product promise

**Upload evidence → map to control → test sufficiency → identify exceptions → independent challenge → human sign-off → export evidence passport/report.**

The agent assists professional review. It does not issue an audit opinion and does not replace management, internal audit, external audit, or other professional judgment.

## Product architecture

1. Evidence intake
2. Control/evidence mapping
3. Deterministic validation
4. AI evidence-review agent
5. Risk/exception engine
6. Independent reviewer/challenger
7. Evidence Passport
8. Human Approval gate
9. Export/API/dashboard
10. Enterprise identity, security and billing

## Child-project rule

This directory is the commercial child project. The original research projects remain unchanged.

- `mother-reference/` contains exact copies or snapshots of relevant research material for provenance and design reference.
- `prototype/` is the clean commercial prototype.
- Third-party or research-only material in `mother-reference/` must **not** automatically be redistributed or embedded in the commercial product. License and rights review is mandatory before reuse.

## First sellable MVP

The MVP reviews one control at a time and produces:

- control ID and objective
- evidence received
- required-evidence coverage
- missing evidence / exception list
- evidence freshness/completeness flags
- preliminary risk level
- reviewer/challenger result
- evidence hash and provenance record
- Human Gate status
- exportable JSON result

See `DEVELOPMENT_STAGES.md` for the end-to-end path.
