# NAAIL Student Agent Pilot 001

## Executable synthetic Digital Twin education checkpoint

This folder provides a small, dependency-free Python demonstration of the **NAAIL Big Four Student Agent Academy™** concept.

It is intentionally limited and research-safe:

- synthetic **Client XYZ** only;
- no confidential client data;
- no Big Four proprietary methodology;
- no claim that the proxy agent reproduces Deloitte, EY, KPMG, PwC, or any other firm's production technology;
- no real provider/model calls;
- deterministic educational proxy responses;
- transparent illustrative scoring;
- mandatory `PENDING_HUMAN_APPROVAL` Human Gate.

The purpose is to demonstrate the workflow in code before connecting a real provider/model adapter or an institutional student platform.

## Cases

The pilot reuses the three public Prototype 003 case families:

1. Revenue Recognition & Cut-off
2. Goodwill Impairment
3. ICFR / Control Deficiency

## Workflow

```text
Synthetic case
→ educational proxy recommendation
→ student inspect/challenge
→ student accept/modify/reject/request evidence/escalate
→ transparent illustrative scoring
→ Human Gate
```

## Run

Requires Python 3.10+ and the standard library only.

```bash
python student_digital_twin.py --demo
```

Run one case interactively:

```bash
python student_digital_twin.py --case revenue
python student_digital_twin.py --case goodwill
python student_digital_twin.py --case icfr
```

Run tests:

```bash
python -m unittest test_student_digital_twin.py
```

## Student decision states

- `ACCEPT_AGENT`
- `MODIFY_AGENT`
- `REJECT_AGENT`
- `REQUEST_MORE_EVIDENCE`
- `ESCALATE_TO_HUMAN`

## Illustrative dimensions

The demo produces transparent 0–100 educational indicators for:

- **RPA** — Risk–Procedure Alignment
- **AA** — Assertion Alignment
- **EG** — Evidence Grounding
- **PS** — Professional Skepticism
- **DS** — Documentation Sufficiency
- **DIST** — Decision Integrity / Stability
- **AIV** — AI Verification
- **CER** — Contradictory Evidence Recognition
- **HOR** — Human Override Reasoning
- **ESC** — Escalation Judgment

These scores are **not validated psychometric measures**, are not professional-competence determinations, and must not be used for automated recruitment decisions.

## Next implementation step

Replace the deterministic `EducationalProxyAgent` with a governed provider adapter under the existing NAAIL model-provider boundary, freeze prompts/evidence, preregister the evaluation protocol, and compare no-AI / single-agent / sequential-agent / governed multi-agent conditions under identical case evidence.

Related specifications:

- [Student Agent Academy](../docs/education/NAAIL_BIG4_STUDENT_AGENT_ACADEMY.md)
- [Digital Twin Student Simulation](../docs/education/DIGITAL_TWIN_STUDENT_SIMULATION.md)
- [Agent Governance](../AGENTS.md)
