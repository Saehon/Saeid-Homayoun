# Product Requirements — ICFR Evidence Review Agent

## Primary buyer
- SOX / ICFR manager
- Internal Audit
- Controller / controllership
- Risk & compliance
- Audit/advisory firm teams

## Primary user
A professional responsible for testing or reviewing financial-reporting controls and the evidence supporting them.

## Core use case
Given a control definition and one or more evidence items, the product should help the reviewer determine whether the evidence appears complete, relevant, current and consistent with the control requirement, while preserving a traceable record for human review.

## MVP functional requirements

### FR-01 Evidence intake
Accept text initially; later PDF, spreadsheet, image, email/export, SharePoint/OneDrive and ERP connectors.

### FR-02 Control definition
Capture control ID, owner, frequency, objective, risk, assertions, required evidence and review period.

### FR-03 Evidence mapping
Map evidence to required evidence fields and identify unmatched or missing items.

### FR-04 Deterministic checks
Check presence, required fields, dates/periods, hashes, duplicates and simple reconciliation rules before LLM reasoning.

### FR-05 AI review
Generate a structured preliminary assessment grounded only in supplied/authorized evidence.

### FR-06 Exception engine
Classify potential exceptions as low/medium/high review priority. The label is triage, not a professional conclusion.

### FR-07 Independent challenge
A separate reviewer/challenger must attempt to falsify the primary assessment and surface contradictions or unsupported claims.

### FR-08 Evidence Passport
Every output records source identifiers, content hash, transformations, model/provider/version when used, timestamps and reviewer status.

### FR-09 Human Gate
No final status becomes approved until a named human reviewer explicitly approves it.

### FR-10 Export
Export JSON first; later PDF/Excel/API/workpaper package.

## Non-functional requirements
- tenant isolation
- encryption in transit and at rest
- least-privilege access
- immutable/auditable event trail
- model/version logging
- configurable retention
- graceful failure if AI provider is unavailable
- no customer evidence used for model training unless customer terms explicitly permit it
- deterministic tests for critical calculations and status transitions

## Success metrics for pilots
- evidence-review time per control
- exception precision / false-positive rate
- exception recall on seeded cases
- reviewer override rate
- percentage of outputs with complete evidence lineage
- user acceptance and repeat usage
