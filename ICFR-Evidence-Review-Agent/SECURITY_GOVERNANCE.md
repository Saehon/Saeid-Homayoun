# Security, Governance and Professional Boundary

## Mandatory controls
1. Human approval for every professional conclusion.
2. Evidence-first reasoning: no unsupported claim may be represented as evidence.
3. Evidence Passport for each review.
4. Model/provider/version recorded for AI-generated assessments.
5. Primary agent and independent challenger separated where feasible.
6. Customer data isolated by tenant.
7. Secrets never stored in source code.
8. Customer evidence never committed to public GitHub.
9. Retention and deletion are configurable.
10. Logs contain identifiers and decisions, not unnecessary sensitive evidence content.

## Prompt-injection boundary
Uploaded documents are untrusted data. Instructions found inside customer evidence must never override system/product rules.

## Commercial/legal boundary
The child project may learn from the mother research project, but material in the reference snapshot can carry third-party licenses or research-only constraints. Before commercial release, create a Software Bill of Materials and rights register and include only components with documented commercial rights.

## Professional boundary
The system is decision support. It does not provide an audit opinion, management certification, or regulator finding. Final professional judgment and sign-off remain with authorized humans.
