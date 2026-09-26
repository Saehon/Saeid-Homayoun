# Development Stages — Prototype to Microsoft Marketplace

## Stage 0 — Product boundary and IP
**Goal:** freeze exactly what is being sold.

Deliverables:
- product name and one-sentence value proposition
- defined buyer/user
- one-control evidence-review workflow
- source/license inventory
- separation of research/open-source references from proprietary commercial implementation

**Gate:** no restricted/proprietary third-party content enters the commercial core.

## Stage 1 — Deterministic prototype
**Goal:** prove the workflow without depending on an LLM.

Build:
- control input schema
- evidence input
- required-evidence matching
- exception rules
- risk triage
- Evidence Passport
- Human Gate state
- automated unit tests

**Gate:** identical input produces reproducible results; all critical status transitions are tested.

## Stage 2 — GPT-enabled review agent
**Goal:** add evidence-grounded reasoning.

Build:
- provider abstraction
- GPT primary reviewer
- structured output contract
- prompt-injection defenses
- evidence citation/trace IDs
- fail-closed behavior when evidence is missing

**Gate:** model cannot approve a control; it can only recommend/flag.

## Stage 3 — Independent reviewer / falsification
**Goal:** reduce single-model error.

Build:
- separate challenger prompt/model
- contradiction detection
- unsupported-claim checks
- disagreement routing to human reviewer

**Gate:** disagreement is visible and cannot be silently collapsed.

## Stage 4 — Professional benchmark
**Goal:** demonstrate useful performance.

Dataset:
- synthetic seeded exceptions
- public SEC/ICFR examples where rights permit
- de-identified pilot cases only with authorization

Measure:
- precision
- recall
- false-positive/negative rates
- reviewer override
- evidence-lineage completeness
- review-time savings

**Gate:** results are documented with limitations; no unsupported production claims.

## Stage 5 — Usable MVP
**Goal:** make the workflow usable by a design partner.

Add:
- authentication
- upload UI
- control library
- evidence viewer
- review queue
- reviewer comments
- export
- audit log

**Gate:** a professional user can complete the entire workflow without developer intervention.

## Stage 6 — Security and enterprise hardening
Add:
- Microsoft Entra ID / SSO
- tenant isolation
- encryption
- role-based access
- secrets management
- retention/deletion controls
- backups
- monitoring
- vulnerability/dependency scanning
- incident-response and privacy documentation

**Gate:** security questionnaire can be answered with evidence, not intentions.

## Stage 7 — Paid pilot
Run with a narrow design partner:
- one process
- limited control population
- agreed success measures
- human review of every output
- explicit limitations

Commercial learning:
- willingness to pay
- onboarding friction
- integrations required
- buyer vs user distinction
- support burden

## Stage 8 — SaaS product
Replace prototype UI with production web service:
- multi-tenant backend
- API
- customer admin
- metering/plan enforcement
- support tooling
- SLA/health monitoring
- production model routing and cost controls

## Stage 9 — Microsoft Marketplace
Prepare two separate offers: DEV/test and PROD.

For a transactable SaaS offer:
- Partner Center Marketplace enrollment
- Microsoft Entra authentication / SSO
- 24/7 landing page
- Microsoft SaaS Fulfillment API integration
- connection webhook for subscription lifecycle
- plan/pricing configuration
- preview-audience end-to-end purchase tests
- security/privacy/legal documentation
- Marketplace listing assets and AI Apps & Agents categorization

## Stage 10 — Scale
After validated paid use:
- SharePoint/OneDrive
- Excel/Teams/Copilot surface
- SAP/Dynamics/Oracle connectors
- continuous controls monitoring
- portfolio dashboard
- CAM/KAM and IFRS modules as separate products/add-ons

## Do not do first
- do not build all 37 audit agents
- do not start with every ICFR process
- do not promise automated audit conclusions
- do not add ERP integrations before the basic evidence-review workflow works
- do not mix research licenses with proprietary commercial code without review
