# NAAIL Digital Twin Student Simulation™

## Objective

This specification defines the public, research-safe simulation design for the NAAIL Big Four Student Agent Academy™. It reuses the existing Client XYZ Audit Digital Twin and Prototype 003 case family while adding structured student decisions, educational proxy-agent interaction, scoring, and partner reporting.

## Simulation architecture

```text
Synthetic Client XYZ
    |
    +--> Engagement Context
    +--> Transactions / Controls / Estimates
    +--> Frozen Evidence Pack
    +--> Known Hidden Exceptions
    |
    v
Educational Proxy Agent
    |
    +--> risk hypothesis
    +--> assertion mapping
    +--> suggested procedure
    +--> evidence references
    +--> uncertainty / limitations
    |
    v
Student Decision Workspace
    |
    +--> inspect evidence
    +--> challenge agent
    +--> locate contradictions
    +--> design procedure
    +--> document rationale
    +--> accept / modify / reject
    |
    v
NAAIL Evaluation Layer
    |
    +--> RPA / AA / EG / PS / DS / DIST
    +--> AIV / CER / HOR / ESC
    +--> time / revision / override traces
    |
    v
Professional Decision DAG™
    |
    v
Human Gate
```

## Pilot case set

### Case 1 — Revenue Recognition & Cut-off

**Synthetic condition:** transactions near year-end contain deliberately planted timing exceptions.

**Existing frozen benchmark references:** `TX-002`, `TX-003`; synthetic proposed adjustment EUR 190,000.

**Student responsibilities:**
- identify affected assertions;
- evaluate contract, invoice, shipping, and ledger evidence;
- distinguish valid revenue from cut-off error;
- critique the proxy agent's proposed procedures;
- determine whether additional evidence is required;
- document the final conclusion and escalation decision.

**Primary learning outcomes:** revenue-risk reasoning, cut-off, occurrence, contradictory evidence, AI verification, professional skepticism.

### Case 2 — Goodwill Impairment

**Synthetic condition:** a reporting unit contains deterioration signals and management assumptions that require challenge.

**Existing frozen benchmark references:** `GW-DR`, `GW-MAR`; synthetic estimated adjustment EUR 440,000.

**Student responsibilities:**
- identify impairment indicators;
- assess management assumptions;
- inspect sensitivity / valuation evidence;
- challenge optimistic inputs;
- distinguish evidence from unsupported model narrative;
- decide whether specialist or manager escalation is required.

**Primary learning outcomes:** estimates, valuation uncertainty, management bias, evidence quality, specialist judgment, AI limitations.

### Case 3 — ICFR / Control Deficiency

**Synthetic condition:** control design and operation weaknesses are embedded in journal-entry and IT-related processes.

**Existing frozen benchmark references:** `CTRL-JE-02`, `CTRL-IT-03`; synthetic estimated exposure EUR 530,000.

**Student responsibilities:**
- map deficiency to process and assertion;
- distinguish design from operating-effectiveness issues;
- assess severity and compensating controls;
- evaluate whether the proxy agent overstates or understates the deficiency;
- document escalation and remediation recommendations.

**Primary learning outcomes:** control reasoning, deficiency classification, ICFR evidence, AI-assisted control testing, documentation.

## Controlled agent conditions

The simulation can support experimental or teaching comparisons under identical frozen evidence:

1. **No AI** — traditional case materials only.
2. **General AI assistant** — unstructured conversational support.
3. **Single educational audit agent** — one role with structured outputs.
4. **Sequential specialist agents** — risk → evidence → procedure → reviewer.
5. **Governed multi-agent condition** — specialist roles + evidence rules + Decision DAG + Human Gate.

No condition should be reported as superior until it has been executed under the same evidence, scoring rules, and evaluation protocol.

## Educational proxy-agent response contract

For material recommendations, the agent should return a structured object containing at least:

```text
case_id
risk_statement
assertions
recommended_procedures
evidence_ids
contradictory_evidence_ids
uncertainties
alternative_explanations
confidence_or_calibration_note
required_human_review
```

The agent may be intentionally imperfect in selected teaching scenarios, but any planted error must be documented in the instructor key and must not be presented publicly as a real provider/model failure unless that provider/model was actually tested.

## Student decision states

Each material decision should record:

- `ACCEPT_AGENT`
- `MODIFY_AGENT`
- `REJECT_AGENT`
- `REQUEST_MORE_EVIDENCE`
- `ESCALATE_TO_HUMAN`

Students must provide a rationale and evidence references. A final case cannot close without a Human Gate.

## Scoring model

### Professional dimensions

- **RPA** — Risk–Procedure Alignment
- **AA** — Assertion Alignment
- **EG** — Evidence Grounding
- **PS** — Professional Skepticism
- **DS** — Documentation Sufficiency
- **DIST** — Decision Integrity / Stability

### AI-readiness dimensions

- **AIV** — AI Verification: tests whether the student independently verifies AI-generated claims.
- **CER** — Contradictory Evidence Recognition: detects evidence inconsistent with the leading conclusion.
- **HOR** — Human Override Reasoning: quality of accept/modify/reject decisions and supporting rationale.
- **ESC** — Escalation Judgment: recognizes when specialist, manager, instructor, or other human review is necessary.

### Illustrative composite score

A course may define a documented weighting such as:

```text
Professional Judgment Core = mean(RPA, AA, EG, PS, DS, DIST)
AI Readiness Core          = mean(AIV, CER, HOR, ESC)
```

A single headline score should not be used unless the weighting, reliability, construct validity, and intended use have been reviewed. Academic grading and recruitment decisions should remain separable.

## Digital Twin event log

The simulation should preserve an auditable timeline such as:

```text
case_opened
agent_query
agent_response
source_viewed
contradiction_flagged
procedure_changed
decision_submitted
decision_revised
escalation_requested
human_feedback
human_gate_status
case_closed
```

This event log enables teaching feedback, reproducibility, research analysis, and process mining without exposing proprietary firm systems.

## Instructor controls

The instructor should be able to:

- activate/deactivate evidence;
- choose agent condition;
- reveal evidence progressively;
- insert a known misleading recommendation;
- freeze or randomize selected case parameters;
- review student decision paths;
- release feedback after submission;
- export anonymized research data subject to ethics/privacy rules.

## Partner report

The default partner-facing report should contain aggregate, anonymized indicators only, for example:

- proportion identifying the hidden exception;
- average RPA / AA / EG / PS / DS / DIST;
- AI verification rate;
- contradictory-evidence detection rate;
- agent acceptance / modification / rejection rate;
- escalation rate;
- median task time;
- common reasoning weaknesses;
- recommended curriculum/pre-employment training topics.

Individual-level disclosure requires explicit student consent and appropriate institutional/privacy approval.

## Safety, privacy, and IP rules

- Synthetic or properly licensed data only for the public teaching benchmark.
- No confidential client data.
- No reverse engineering of proprietary firm platforms.
- No use of firm names/logos without authorization.
- No automated recruitment decisions from NAAIL scores.
- No claim that a proxy agent represents a firm's real production system.
- Human Gate required for material simulated professional conclusions.
- Research use requires appropriate consent/ethics/privacy governance.

## Pilot completion criteria

A Student Agent Pilot is considered technically ready only when:

1. all three cases have frozen evidence packs and instructor keys;
2. scoring rules are versioned;
3. at least one educational proxy-agent condition is connected;
4. no-AI baseline is available;
5. planted exceptions are reproducible;
6. student event logging is tested;
7. privacy/consent text is approved for the intended institution;
8. Human Gate is enforced;
9. aggregate report generation is validated;
10. the pilot clearly distinguishes simulation evidence from real-world audit effectiveness claims.
