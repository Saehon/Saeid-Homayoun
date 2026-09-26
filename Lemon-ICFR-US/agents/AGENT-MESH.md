# Lemon Agent Mesh

## Orchestrator
The **Lemon Orchestrator** routes a case through evidence acquisition, ICFR reasoning, specialized agents, challenge, falsification, and human approval. It cannot approve its own material conclusions.

## Specialist agents

### 1. Scoping & Risk Agent
Determines significant accounts/disclosures, relevant assertions, processes, risks, and candidate key controls.

### 2. COSO Mapping Agent
Maps evidence and observations to COSO components/principles and records gaps without inventing compliance.

### 3. Control Design Agent
Evaluates whether a control, as described, is logically capable of preventing or detecting the stated risk. Design effectiveness and operating effectiveness are kept separate.

### 4. Evidence Agent
Builds Evidence Passports; verifies source, date, version, lineage, rights, and relevance.

### 5. Operating Effectiveness Agent
Creates or executes approved test logic over samples, populations, reconciliations, approvals, access evidence, or transaction trails.

### 6. Financial Analysis Agent
Uses financial statements, XBRL, ratios, trend analysis, and anomaly signals to generate risk hypotheses. Financial anomalies are risk indicators, not automatic control failures.

### 7. Deficiency Evaluation Agent
Structures evidence relevant to deficiency, significant deficiency, and material weakness evaluation. Final classification remains human.

### 8. Co-Scientist Agent Panel
Generates competing explanations and tests them against the evidence set.

### 9. Structure Discovery Agent
Searches for hidden or weakly observed relationships among process, account, assertion, risk, control, evidence, and exception. Outputs are hypotheses until validated.

### 10. Reviewer Agent
Independently reviews logic, evidence completeness, assumptions, and reproducibility.

### 11. Falsification Agent
Attempts to disprove the proposed conclusion by:
- finding contradictory evidence,
- testing alternative explanations,
- identifying missing evidence,
- checking temporal mismatch,
- testing whether the control actually addresses the stated assertion/risk,
- challenging materiality/severity reasoning,
- reproducing the result independently.

### 12. Human Approval Agent Interface
Presents the evidence, competing hypotheses, unresolved contradictions, and model lineage to an authorized human. It records the decision but never fabricates approval.

## Separation-of-duty rule
The same agent instance may not both originate and finally validate a material conclusion.

## Minimum workflow
```text
Evidence
  ↓
Scoping/Risk
  ↓
COSO + Control Design
  ↓
Evidence + Operating Effectiveness
  ↓
Co-Scientist hypotheses
  ↓
Financial/Structure analysis
  ↓
Deficiency candidate
  ↓
Reviewer
  ↓
Independent Falsification
  ↓
Human Approval
```

## Agent output contract
Every agent returns:
- `case_id`
- `claim`
- `evidence_refs[]`
- `assumptions[]`
- `alternative_explanations[]`
- `confidence` (calibrated support, not truth)
- `limitations[]`
- `model_tool_version`
- `reproducibility_ref`
- `requires_human_review`
