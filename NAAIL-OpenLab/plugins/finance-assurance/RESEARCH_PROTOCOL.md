# Empirical research protocol — preregistration candidate (NOT executed)
**Research question:** Does evidence-governed multi-agent assistance reduce unsupported accounting/ICFR workpaper conclusions while retaining useful task throughput?

## Conditions (randomize tasks, blind grade)
- A0: deterministic rules/checklists, no LLM.
- A1: single LLM with the same data and time budget.
- A2: multi-agent workflow without evidence gate.
- A3: multi-agent workflow with evidence references, independent verification and human-approval gate.

## Task corpus and measurements
Prepare a frozen **proposed** corpus of 120 synthetic tasks spanning 5 executable workflows plus close/ICFR tasks, seeded with known booking, timing, aging and control-documentation errors. Freeze gold truth *before* execution, separating scoring staff from operators. Include negative and null cases; use identical contexts, tasks and evaluation criteria across arms.
Primary outcome: rate of **unsupported material assertions** per task, adjudicated blind by qualified reviewers. Secondary outcomes: accuracy, exception recall, citation/evidence traceability, reviewer minutes, manual overrides, execution cost and model-version sensitivity. Disclose denominators and confidence intervals, account for task clustering, and correct for repeated comparisons where justified.

## Candidate hypotheses (not asserted novel)
H1: Evidence gating lowers unsupported assertion rates versus otherwise equivalent ungated multi-agent assistance.
H2: Independent AI-to-AI verification improves traceability but increases latency; quantify both effects instead of assuming a net benefit.
H3: The effect of evidence gating is greatest for tasks involving ambiguous cut-off or missing control documentation, not for arithmetic-only tasks.

## Publication pathway
Phase 1: reproducible synthetic benchmark (engineering and construct validity only). Phase 2: reviewer-blind lab experiment with ethics/data review. Phase 3: public SEC EDGAR/XBRL cohort and exogenous event design *only if* an identifiable causal mechanism and appropriate external validity are established. FT50/AJG4 suitability is a stretch target and not evidence of publication readiness. Do not claim simulation establishes effects on real auditor behavior.

## Decision gates
G0 rights and research ethics; G1 corpus/gold freeze; G2 leakage review; G3 reproducible baseline; G4 blind multi-arm execution; G5 professional adjudication; G6 robustness and falsification; G7 independent replication; G8 human scientific approval. Failures remain in the results.
Relevant existing NAAIL research tracks: LEMON-ICFR-US, NAAIL-MCP-A2A-Agent-Assurance, risk–CAM alignment and AJPT agentic auditing.
