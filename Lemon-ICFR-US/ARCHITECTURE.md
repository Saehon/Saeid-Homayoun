# 🍋 Lemon-ICFR-US — Scientific Agent Architecture

## Mission
Lemon-ICFR-US is an evidence-governed agent system for US Internal Control over Financial Reporting (ICFR), designed for research, education, prototyping, and controlled professional experimentation.

It combines:
- authoritative ICFR evidence and standards,
- COSO-oriented control reasoning,
- Claude financial-services capabilities as a replaceable technology layer,
- Co-Scientist multi-agent reasoning,
- AlphaFold-inspired latent-structure discovery,
- AlphaEvolve-inspired controlled improvement,
- scientific-discovery workflows,
- independent falsification,
- Digital Twin / scenario testing,
- Evidence Passports and full lineage,
- mandatory human approval for consequential conclusions.

## Design rule
**Permanent assurance logic must not depend on one model vendor.**

Claude is currently a preferred execution layer for agent orchestration, financial analysis, spreadsheet interaction, and software development. The Lemon control, evidence, scientific, governance, and approval architecture remains provider-neutral.

## Core architecture

```text
Authoritative Evidence
SEC | PCAOB | SOX 404 | COSO | Filings | XBRL | Workpapers | ERP evidence
        │
        ▼
Evidence & Rights Gateway
source → license/rights → provenance → Evidence Passport → version
        │
        ▼
ICFR Knowledge Core
entity/process/account/assertion/control/risk/deficiency graph
        │
        ├─────────────► Structure Discovery Engine
        │                AlphaFold-inspired latent relationship discovery
        │                process ↔ account ↔ assertion ↔ risk ↔ control ↔ evidence
        │
        ▼
Lemon Orchestrator
        │
        ├─ Risk & Scoping Agent
        ├─ Control Design Agent
        ├─ Evidence Agent
        ├─ Operating Effectiveness Agent
        ├─ Financial Analysis Agent
        ├─ Deficiency Evaluation Agent
        ├─ Reviewer Agent
        └─ Independent Falsification Agent
        │
        ▼
Co-Scientist Layer
generate hypotheses → competing explanations → evidence search → debate
        │
        ▼
Scientific Discovery Engine
observe → hypothesize → test → replicate → challenge → update
        │
        ▼
Digital Twin / Scenario Lab
transaction/control simulations + counterfactuals + stress cases
        │
        ▼
AlphaEvolve-style Improvement Loop
propose variants → benchmark → reject unsafe/weak variants → retain validated improvements
        │
        ▼
Adversarial / Falsification Gate
independent contradiction search + evidence sufficiency test
        │
        ▼
Human Approval Gate
controller / internal audit / external audit / researcher
        │
        ▼
Decision + Evidence Passport + Reproducible Audit Trail
        │
        └─────────────► Learning Loop / Skill Passport
```

## COSO alignment
Lemon maps each material conclusion to the five COSO components:
1. Control Environment
2. Risk Assessment
3. Control Activities
4. Information & Communication
5. Monitoring Activities

The agent system should store the relevant COSO component/principle, financial-statement assertion, process, risk, key control, test procedure, evidence, exception, deficiency rationale, reviewer result, falsification result, and human disposition.

## Claude finance stack mapping

| Claude capability | Lemon role | Architectural status |
|---|---|---|
| Claude for Financial Services | Financial-domain interaction and workflow surface | Replaceable technology |
| Financial Analysis Solution | Financial analysis and anomaly support | Specialist subagent/tool |
| Claude for Excel | Spreadsheet evidence review and controlled analyst interface | Interface/tool |
| Claude Code | Build, test, maintain and evaluate Lemon | Developer plane |
| Financial Services Agents | Reusable workflow/subagent patterns | Agent template layer |

No Claude-generated conclusion becomes trusted evidence merely because Claude produced it.

## Scientific intelligence layers

### Co-Scientist
Multiple role-separated agents generate competing hypotheses about:
- control failures,
- missing evidence,
- transaction anomalies,
- root causes,
- potential material weaknesses,
- alternative explanations.

Consensus is not sufficient. Minority hypotheses and contradictory evidence are preserved.

### AlphaFold-inspired Structure Discovery
This is an analogy, not use of the AlphaFold biological model. Lemon searches for latent structure across:
`entity → process → account → assertion → risk → control → evidence → exception → deficiency`.

The engine may propose hidden relationships or clusters, but all material links require evidence and review.

### AlphaEvolve-inspired Improvement
Candidate prompts, test strategies, rules, thresholds, retrieval plans, and agent-routing variants are generated and evaluated against frozen benchmark cases. A variant graduates only when it improves defined metrics without degrading safety, provenance, reproducibility, or false-positive controls.

### Scientific Discovery
Every important finding follows:
`Observation → Question → Hypotheses → Evidence → Test → Replication → Falsification → Human Judgment → Learning`.

## Required gates
A material Lemon conclusion must pass:
1. Source/provenance gate
2. Rights/license gate
3. ICFR/COSO grounding gate
4. Evidence sufficiency gate
5. Independent reviewer gate
6. Falsification/challenge gate
7. Reproducibility gate
8. Human approval gate

## Non-negotiable boundaries
- AI does not sign an audit opinion.
- AI does not replace management's ICFR assessment.
- AI does not replace auditor professional judgment.
- Vendor commentary does not outrank SEC/PCAOB/COSO/primary evidence.
- Self-improvement is benchmark-gated and version-controlled; no uncontrolled autonomous mutation.
- All consequential outputs retain provenance and human disposition.

## Primary product outcome
Lemon should produce a structured **ICFR Evidence Passport** containing:
- scoped process/account/assertion,
- identified risk,
- control objective and control,
- evidence used,
- test performed,
- exceptions,
- alternative hypotheses,
- reviewer challenge,
- falsification result,
- deficiency classification rationale,
- model/tool/version lineage,
- human approval and final disposition.
