# 🍋 Lemon-ICFR-US

## Scope
US Internal Control over Financial Reporting

## Evidence hierarchy
Primary authoritative sources first: SEC; PCAOB; SOX 404; COSO; CompanyFacts/XBRL; material-weakness evidence.

## Research use
ICFR material weaknesses, controls, risk prediction, inspection and assurance research.

## Scientific agent architecture
Lemon now combines its evidence-governed ICFR pipeline with a provider-neutral scientific agent architecture:

**Evidence → ICFR/COSO Knowledge Core → Structure Discovery → Co-Scientist → Specialized Agents → Scientific Testing → Reviewer → Independent Falsification → Human Approval → Learning Loop**

The design incorporates:
- Co-Scientist multi-agent hypothesis generation and debate
- AlphaFold-inspired latent-structure discovery across process/account/assertion/risk/control/evidence relationships
- AlphaEvolve-inspired benchmark-gated improvement
- Scientific discovery and replication
- Digital Twin / scenario testing
- Evidence Passports and model/tool lineage
- mandatory human approval for consequential conclusions

See [ARCHITECTURE.md](ARCHITECTURE.md).

## Claude financial-services integration
Claude is treated as a **replaceable execution technology layer**, not the source of Lemon's assurance authority.

| Claude capability | Lemon use |
|---|---|
| Claude for Financial Services | financial-domain workflow/interface |
| Financial Analysis Solution | analytical and anomaly-support subagent |
| Claude for Excel | spreadsheet evidence and review interface |
| Claude Code | build, test and maintain Lemon |
| Financial Services Agents | reusable specialist-agent patterns |

See [integrations/CLAUDE-FINANCE-STACK.md](integrations/CLAUDE-FINANCE-STACK.md).

## Agent mesh
Core roles include:
- Lemon Orchestrator
- Scoping & Risk Agent
- COSO Mapping Agent
- Control Design Agent
- Evidence Agent
- Operating Effectiveness Agent
- Financial Analysis Agent
- Deficiency Evaluation Agent
- Co-Scientist Panel
- Structure Discovery Agent
- Reviewer Agent
- Independent Falsification Agent

See [agents/AGENT-MESH.md](agents/AGENT-MESH.md).

## Standard pipeline
Primary Evidence → Structured Registry → Domain Agent → Reviewer/Challenge → Independent Falsification → Human Approval → Reproducible Research Output

## Runnable core
A minimal Python skeleton is included under `src/lemon_icfr/`. It enforces non-bypassable provenance, rights, ICFR/COSO, evidence, review, falsification, reproducibility, and human-approval gates.

Quick test:

```bash
cd Lemon-ICFR-US
python -m pip install -e ".[test]"
pytest -q
python examples/minimal_case.py
```

The demo intentionally ends at **AWAITING_HUMAN_APPROVAL**. Lemon does not approve its own material ICFR conclusions.

## Shared Big4 benchmark
Use the repository's `Big4-Official-Resources/` layer as a cross-cutting public benchmark. Big4 commentary does not replace authoritative standards or regulatory evidence.

## Core folders
- `organized/data/` — reproducible/open or appropriately licensed data references
- `organized/evidence/` — provenance and source registries
- `agents/` — domain-agent specifications
- `integrations/` — provider adapters and external execution layers
- `benchmarks/` — test cases and evaluation protocols
- `research/` / `organized/papers/` — hypotheses, methods and research outputs
- `governance/` — scientific-learning, falsification and approval policies
- `src/lemon_icfr/` — runnable provider-neutral agent core

## Governance
- Non-commercial education and research.
- Preserve provenance and licensing.
- Do not redistribute proprietary material.
- Separate official/primary evidence from third-party material.
- Require independent validation before performance or causal claims.
- No uncontrolled autonomous self-improvement.
- Final academic/professional judgment remains human.

Parent repository: `Saehon/Saeid-Homayoun`
