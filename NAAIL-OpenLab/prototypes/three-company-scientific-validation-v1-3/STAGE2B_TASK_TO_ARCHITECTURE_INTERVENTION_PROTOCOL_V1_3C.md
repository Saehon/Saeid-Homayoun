# NAAIL OpenLab™ — V1.3C Task-to-Architecture Intervention Protocol

**Date:** 2026-09-17  
**Design status:** `FROZEN_DESIGN`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`  
**Gold_Key:** `LOCKED`

## Purpose

This protocol isolates the effect of the NAAIL governance architecture while holding the substantive task, provider/model and evidence constant. The scientific question is whether adding governed evidence structure and verification improves professional accounting/auditing judgment beyond a direct model answer.

The intervention is architectural, not informational. **A1 and A2 may transform, organize, challenge and document the same frozen evidence, but they may not receive additional substantive evidence, standards excerpts, web search results, hidden reference answers or human guidance that A0 does not receive.**

## Frozen architecture conditions

### A0 — Model + Frozen Evidence

A0 receives the professional task and the common frozen evidence packet and produces a direct professional answer.

Allowed:
- reason over the supplied evidence;
- cite supplied evidence IDs;
- state uncertainty or request more evidence;
- produce the professional conclusion requested by the task.

Not required / not supplied:
- Evidence Passport™ structure;
- formal claim-evidence map;
- structured contradiction/falsification pass;
- Professional Decision DAG™ / judgment-path summary;
- NAAIL verification checklist.

A0 is not intentionally weakened. It is the best direct answer the same model can produce from the same evidence without the NAAIL governance intervention.

### A1 — Evidence Passport™

A1 receives the identical professional task and identical frozen evidence packet.

A1 adds only structured evidence governance:
- source/evidence inventory;
- evidence relevance to the task;
- provenance/source identifier;
- evidence sufficiency and gap notation;
- claim-to-evidence linkage;
- bounded professional conclusion.

A1 may reorganize or summarize the evidence but may not introduce new facts or sources. A1 does **not** receive the full NAAIL contradiction/falsification and decision-governance intervention.

### A2 — Full NAAIL Verify

A2 receives the identical professional task and identical frozen evidence packet.

A2 adds the full public-safe NAAIL governance sequence:
- Evidence Passport™;
- task-relevant risk/assertion/decision structure;
- explicit claim-to-evidence judgment path;
- contradiction and alternative-explanation challenge;
- falsification / disconfirming-evidence check;
- evidence-sufficiency and uncertainty gate;
- human-review-ready decision-path summary;
- bounded outcome such as conclusion, `REQUEST_MORE_EVIDENCE`, or escalation when justified.

A2 may not retrieve or inject additional substantive evidence. Any standards, accounting rules or factual materials necessary to answer a task must already be part of the common frozen evidence available to A0, A1 and A2.

## Cross-condition parity controls

The following are fixed within every provider-task triplet:

1. **Same task objective.** The substantive professional question is unchanged across A0/A1/A2.
2. **Same evidence.** The same frozen evidence packet and source IDs are available to all conditions.
3. **No external retrieval.** Browsing, search, external tools and additional file retrieval are prohibited during the comparison.
4. **Same provider/model.** A0/A1/A2 are compared within the same registered provider/model.
5. **Same run independence.** No condition may see another condition's response.
6. **Same Gold_Key blindness.** Gold/reference scoring material remains inaccessible during response generation.
7. **Same substantive knowledge boundary.** No condition receives a standards/rules excerpt unavailable to the other two.
8. **Matched visible-output budget.** Within a provider-task triplet, the same maximum visible-output budget applies to all three conditions.
9. **No human hints before freeze.** Human review occurs only after responses are frozen.
10. **Same failure preservation.** Refusals, uncertainty, failed calls and contradictory evidence are retained rather than repaired post hoc.

## Seven-domain intervention map

### D1 — CAM classification

**Task objective:** classify the CAM topic/scope using only the frozen audit evidence.

- **A0:** direct classification with rationale.
- **A1:** classification plus Evidence Passport linking the classification to relevant evidence IDs and noting gaps.
- **A2:** A1 plus alternative classification challenge, risk/assertion linkage where relevant, contradiction check, and a bounded decision-path summary.

A2 may not use a hidden CAM taxonomy unavailable to A0/A1 unless that taxonomy is included in the common frozen packet.

### D2 — Audit assertion mapping

**Task objective:** map the identified risk/CAM to the most relevant audit assertions.

- **A0:** direct assertion mapping with rationale.
- **A1:** assertion mapping with evidence-to-assertion linkage and sufficiency notation.
- **A2:** A1 plus competing-assertion challenge, omitted-assertion check, contradiction/falsification step and decision-path summary.

No additional assertion guidance may be injected only into A2.

### D3 — ICFR reasoning

**Task objective:** reason about the control implication supported by the frozen evidence.

- **A0:** direct ICFR judgment bounded by the supplied facts.
- **A1:** evidence passport separating control evidence, inference and missing evidence.
- **A2:** A1 plus challenge of alternative control interpretations, explicit distinction between observed evidence and severity inference, contradiction check and escalation/`REQUEST_MORE_EVIDENCE` gate.

A2 may not infer a control deficiency, significant deficiency or material weakness merely because the architecture requires a decision node.

### D4 — Accounting judgment

**Task objective:** reach a professional accounting judgment from the supplied facts/rules.

- **A0:** direct accounting conclusion with rationale.
- **A1:** conclusion plus source/rule-to-judgment traceability and evidence gaps.
- **A2:** A1 plus alternative accounting-treatment challenge, assumption sensitivity, disconfirming-evidence check and bounded decision-path summary.

All accounting-rule excerpts needed for the task must be common evidence across conditions.

### D5 — Evidence retrieval from the frozen packet

**Task objective:** identify the most relevant evidence item(s) within the supplied packet.

- **A0:** select relevant evidence and explain why.
- **A1:** structured evidence inventory with relevance/provenance/sufficiency fields.
- **A2:** A1 plus missing-evidence challenge, competing evidence selection, conflict detection and final evidence-set justification.

No condition may search outside the frozen packet.

### D6 — Contradiction detection

**Task objective:** identify and explain conflicts or tensions within the frozen evidence.

- **A0:** directly identify contradictions and their implications.
- **A1:** map each conflicting claim to its evidence source and state unresolved gaps.
- **A2:** A1 plus structured contradiction register, alternative explanations, falsification check and explicit preservation of unresolved conflict.

A2 must not force reconciliation when the evidence remains genuinely contradictory.

### D7 — Professional explanation quality

**Task objective:** provide a clear, professionally usable explanation grounded in the frozen evidence.

- **A0:** direct professional explanation.
- **A1:** explanation with traceable evidence links and sufficiency/gap notation.
- **A2:** A1 plus concise evidence-to-judgment path, challenge outcome, uncertainty boundary and human-review-ready conclusion.

Longer text is not automatically better; the same visible-output budget applies across conditions.

## Contamination rules

A provider-task triplet is flagged `CONTAMINATED` and excluded from the confirmatory paired contrast if any of the following occurs:

- A1 or A2 receives substantive evidence unavailable to A0;
- any condition uses external browsing/search/tools;
- any condition sees another condition's response;
- the Gold_Key or reference answer is exposed before response freeze;
- different substantive task wording changes the underlying question;
- a human edits or repairs a response before freeze;
- provider/model identity changes within the triplet;
- a condition receives a standards/rules excerpt unavailable to the others;
- output-budget treatment differs materially across conditions without a pre-registered exception.

Contaminated observations are preserved and reported; they are not silently replaced.

## Fidelity decision

Each provider-task triplet must receive a pre-scoring fidelity record with one of:

- `PASS`
- `PASS_WITH_DOCUMENTED_DEVIATION`
- `CONTAMINATED_EXCLUDE_CONFIRMATORY`
- `FAILED_CALL`

No OPQS result may be interpreted as an architecture effect until the corresponding intervention-fidelity record is complete.

## Scientific boundary

This protocol freezes what A0, A1 and A2 are allowed to do. It does not generate any of the planned 189 responses, does not open the Gold_Key, does not simulate human review and does not promote Stage 2C.
