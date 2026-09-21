# FRANKENSTEIN Architecture — NAAIL OpenLab

## Constitutional position

FRANKENSTEIN is a **specialist programme in the Audit Agent Lab**. It does not create a new permanent core.

| NAAIL element | FRANKENSTEIN use |
|---|---|
| Stable Knowledge Core | Accounting, audit, ICFR, finance, professional judgment, evidence rules |
| Data & Evidence | Transaction population, row evidence, source hash, control objectives |
| Replaceable Technology Core | OpenAI Agents SDK, model selection, pandas/Pydantic, orchestration |
| Specialist programme | Finance/operations audit agents and deterministic tests |
| Verification | Independent evidence challenger + programmatic evidence-ID validation |
| Evidence Passport | SHA-256 source provenance, run metadata, finding IDs, limitations |
| Human Gate | Final state remains pending qualified human review |

## Workflow

~~~text
Professional Audit Question
    ↓
Input Population + Provenance
    ↓
Deterministic Tests
    ↓
Domain-Routed Evidence
    ↓
11 Specialist Assessments
    ↓
Independent Falsification / Challenge
    ↓
Programmatic Evidence Validation
    ↓
Audit Leader Synthesis
    ↓
Evidence Passport / Limitations
    ↓
NAAIL Human Approval Gate
~~~

## Fail-closed principles

1. Model output alone is not audit evidence.
2. Unsupported finding IDs are rejected programmatically.
3. A domain specialist should abstain when relevant evidence is absent.
4. Risk indicators must not be converted into allegations.
5. The system does not autonomously issue audit opinions or ICFR classifications.
6. Materiality and thresholds must be calibrated to the entity/process before professional use.
7. Final decision rights remain human.

## Replaceability

The implementation can change model providers, LLMs, agent SDKs, analytics libraries, storage, connectors and dashboards without redefining the Stable Knowledge Core. This is required by the NAAIL Two-Core Constitution.

## Public boundary

This module exposes a research-scale, non-enabling implementation. It does not disclose confidential data, proprietary client methodology, restricted standards text, private credentials or patent-sensitive private orchestration details.
