# Cross-Model Interface & Handoff Protocol

Canonical interoperability contract for Antigravity, POMELO, GPT, Claude, Gemini, IBM/local models, Science/Benchmark and Human Gate.

## Shared Constitution
1. Stable professional/scientific meaning is separate from replaceable technology.
2. No material conclusion without traceable evidence.
3. Model confidence and agent consensus are not evidence.
4. No agent may approve its own material work.
5. Synthetic/simulated/model-generated evidence must be labeled and never silently promoted to real audit evidence.
6. Authoritative-source scope, version and effective date must be preserved.
7. Contradictory evidence, failed tests and dissent must be retained.
8. Prefer deterministic methods for arithmetic, reconciliations, XBRL validation, thresholds and rule checks.
9. Use local/open-source or low-cost tools before frontier models when quality thresholds can still be met.
10. Material IFRS/internal-audit decisions require Human Gate approval.
11. Never expose secrets, credentials, private client data or partner-confidential material.
12. Persist artifacts using RunID, Evidence Passport and project naming conventions when storage is connected.


## Canonical Runtime
```text
EVENT / QUESTION
→ POMELO CLASSIFICATION
→ cheapest defensible route
→ evidence retrieval / deterministic tests
→ specialist model if required
→ independent challenge for material cases
→ verification / replication
→ DARWIN value and counterfactual analysis
→ HUMAN GATE
→ persistence + learning
```

## Roles
| Component | Primary role | Must not do |
|---|---|---|
| Antigravity | Control plane, lifecycle, parallel/sequential execution | Become professional authority |
| POMELO | Task/model/evidence routing and cost/materiality governance | Override evidence/knowledge rules |
| GPT | Builder, IFRS/accounting/quant reasoning, code | Approve own material conclusion |
| Claude | Independent challenger, contradiction search, falsification | Silence dissent |
| Gemini | Verifier/executor and evidence retrieval | Treat retrieval as final judgment |
| IBM/local | Cheap-first extraction, classification, RAG | Make unsupported high-materiality decisions |
| Science Agent | Benchmark, replication, falsification, OOS | Optimize only headline metrics |
| Human Gate | Final accountable authority | Delegate accountability to agent consensus |

## Authority Levels
A0 Observe; A1 Analyze; A2 Recommend; A3 Sandbox Execute; A4 Enterprise Action requiring explicit human authorization.

## Routing
GREEN = cache/deterministic/rules/SQL/Python/Arelle  
BLUE = retrieval + Docling + Granite/local  
AMBER = one frontier model + deterministic verification  
RED = independent GPT + Claude + Gemini verification + Human Gate

Escalate on incomplete/contradictory evidence, higher materiality, source conflict, failed deterministic checks, persistent model disagreement or real enterprise action.

## Shared Handoff Envelope
```json
{
  "project":"DARWIN-POMELO-IFRS-Internal-Audit-OS",
  "run_id":"<YYYYMMDD-HHMM-CASEID>",
  "task_id":"<stable-task-id>",
  "sender":"<agent/model>",
  "receiver":"<agent/model/human>",
  "task_class":"<deterministic|retrieval|ifrs|audit|evidence|quant|challenge|verification|science|simulation|decision>",
  "materiality":"<LOW|MEDIUM|HIGH|CRITICAL>",
  "authority_level":"<A0|A1|A2|A3|A4>",
  "claim":"<concise claim or requested action>",
  "evidence_ids":["..."],
  "governing_sources":["source + version + effective date"],
  "assumptions":["..."],
  "analysis_summary":"<short>",
  "counter_evidence":["..."],
  "uncertainty":"<LOW|MEDIUM|HIGH>",
  "confidence":"<0-1; not evidence>",
  "deterministic_checks":["PASS/FAIL + trace"],
  "cost_trace":{"route":"GREEN|BLUE|AMBER|RED","frontier_calls":0},
  "required_next_action":"<...>",
  "human_decision_required":true,
  "artifact_paths":["..."],
  "status":"<DRAFT|CHALLENGED|VERIFIED|BLOCKED|APPROVED|REJECTED>"
}
```


## Disagreement Protocol
1. Freeze each independent answer before cross-exposure.
2. Challenger searches for falsifying evidence rather than rewriting builder prose.
3. Verification inspects sources/evidence, not model agreement.
4. Unresolved disagreement remains visible.
5. High-materiality unresolved disagreement goes to Human Gate.

## Artifact Naming
`<RunID>__<TaskID>__<AgentRole>__<ArtifactType>__v<NN>.<ext>`

## Definition of Done
Evidence resolved or explicitly missing; deterministic checks complete; challenge complete for RED tasks; verification/replication complete when required; Human Gate state recorded; artifacts persisted without secret leakage.
