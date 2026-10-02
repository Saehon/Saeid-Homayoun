# LEMON-ICFR-US — Master Problem-Solving Prompt for Claude

You are acting as the **Lead AI Systems Architect, Senior Python Engineer, ICFR/Audit Methodologist, Scientific Reviewer, and Adversarial Falsification Engineer** for a project called **LEMON-ICFR-US**.

You do **not** currently have access to my GitHub or Google Drive. Therefore:

1. Do not claim that you inspected files that I have not pasted here.
2. Work entirely from the architecture, code facts, and problems provided below.
3. When additional repository files would be useful, do not stop. Make the best technically defensible solution using explicit assumptions.
4. Produce complete, copy-paste-ready code/files rather than merely explaining what should be changed.
5. I will copy your completed response back into GPT, which has access to the project repository, for verification and implementation.

---

## 1. PROJECT PURPOSE

LEMON-ICFR-US is an evidence-governed scientific AI system for **U.S. Internal Control over Financial Reporting (ICFR)**.

Primary authoritative sources should include:
- SEC
- PCAOB
- SOX Section 404
- COSO
- SEC filings
- CompanyFacts/XBRL
- company primary evidence
- properly licensed/reproducible datasets

The system is for research, education, controlled experimentation, and eventually validated professional-support workflows.

AI must NOT:
- sign an audit opinion;
- replace management's ICFR assessment;
- replace auditor professional judgment;
- automatically approve material ICFR conclusions.

Consequential conclusions require a Human Approval Gate.

---

## 2. TARGET SCIENTIFIC ARCHITECTURE

Authoritative Evidence
→ Evidence & Rights Gateway
→ Evidence Passport
→ ICFR/COSO Knowledge Core
→ Process → Account → Assertion → Risk → Control → Evidence Graph
→ Risk & Scoping Agent
→ Control Design Agent
→ Evidence Agent
→ Operating Effectiveness Agent
→ Financial Analysis Agent
→ Deficiency Evaluation Agent
→ Co-Scientist / Competing Hypotheses
→ Independent Reviewer
→ Independent Falsification Agent
→ Evidence Reconciliation
→ Digital Twin / Counterfactual Testing
→ Benchmark & Reproducibility Gate
→ Human Approval
→ Final Evidence Passport + Audit Trail
→ Controlled Learning / Improvement

**Permanent assurance logic must remain provider-neutral.** Claude, GPT, Gemini, IBM Granite, local/open-source models, or future models must be replaceable execution providers. No model vendor is the assurance authority.

---

## 3. CURRENT RUNNABLE CORE

Current gates are approximately:

```python
_REQUIRED_GATES = (
    "provenance",
    "rights_license",
    "icfr_coso_grounding",
    "evidence_sufficiency",
    "independent_review",
    "falsification",
    "reproducibility",
    "human_approval",
)
```

Evidence resembles:

```python
@dataclass(frozen=True)
class EvidenceItem:
    evidence_id: str
    source: str
    provenance: str
    rights_status: str
    content: str
    version: str | None = None
```

Finding resembles:

```python
@dataclass
class Finding:
    agent: str
    claim: str
    evidence_refs: list[str]
    assumptions: list[str]
    alternative_explanations: list[str]
    limitations: list[str]
    model_tool_version: str
    requires_human_review: bool = True
```

Result resembles:

```python
@dataclass
class LemonCaseResult:
    case_id: str
    findings: list[Finding]
    gates: list[GateResult]
    contradictions: list[str]
    status: str
    human_disposition: str | None = None
```

---

## 4. CRITICAL VERIFIED PROBLEMS

### P0-1 — Fake independent review

Current logic effectively contains:

```python
reviewer_ok = bool(hypotheses)
```

Hypothesis exists → Independent Review PASS.

Replace this with a real independent reviewer that evaluates claim, evidence, evidence-to-claim linkage, assumptions, omitted evidence, alternative explanations, ICFR/COSO grounding, reproducibility, uncertainty, and materiality implications.

Reviewer outcomes must include:
- PASS
- FAIL
- INSUFFICIENT_EVIDENCE
- CONTRADICTED
- ESCALATE

A hypothesis cannot approve itself.

### P0-2 — Fake falsification gate

Current logic approximately contains:

```python
falsification_ok = bool(challenges)
```

Any challenge exists → Falsification PASS.

The falsifier must explicitly attempt to destroy or weaken the hypothesis by testing contradictory evidence, unsupported inference, missing population evidence, alternative explanations, causal ambiguity, data leakage, wrong period/entity/assertion, provenance, source hierarchy, materiality, false positives, and false negatives.

### P0-3 — No real independence

The same provider may generate and challenge the same hypothesis. Implement role separation:

- Generator Provider
- Reviewer Provider
- Falsifier Provider

Support cross-provider mode (e.g. Claude → Generator; GPT → Reviewer; Gemini/Granite → Falsifier), while remaining provider-neutral. Allow same-provider fallback for development, but mark independence as LOW; cross-provider independence as HIGH. Include independence in the Evidence Passport.

### P0-4 — Evidence sufficiency is too weak

Evidence IDs alone do not prove evidence supports a claim. Create a semantic Evidence Support Gate:

Claim → Evidence ID → Evidence content → Entailment/relevance → Reliability → Source hierarchy → Temporal validity → Entity validity → Assertion relevance → Contradictions → Support result

Support results:
- SUPPORTED
- PARTIALLY_SUPPORTED
- UNSUPPORTED
- CONTRADICTED
- INSUFFICIENT_EVIDENCE

No material claim passes merely because an evidence ID exists.

### P0-5 — ICFR/COSO grounding is only a Boolean

Replace `coso_context_supplied: bool` with structured grounding including:
- Entity
- Process
- Subprocess
- Account
- Financial statement line item
- Assertion
- Risk
- Control objective
- Control
- Control type
- Frequency
- Control owner
- Population
- Sample/test
- Evidence
- Exception
- Deficiency candidate
- COSO component
- COSO principle
- PCAOB/SEC grounding where applicable

Target graph:
ENTITY → PROCESS → ACCOUNT → ASSERTION → RISK → CONTROL OBJECTIVE → CONTROL → TEST PROCEDURE → EVIDENCE → EXCEPTION → DEFICIENCY EVALUATION

---

## 5. P1 PROBLEMS TO IMPLEMENT

### Human Gate
Create an operational `HumanDisposition` with reviewer ID, role, decision, timestamp, comments, reviewed findings, and override reason. Decisions: APPROVED, APPROVED_WITH_CONDITIONS, REJECTED, RETURN_FOR_MORE_EVIDENCE, ESCALATED. AI cannot populate final approval.

### Agent interfaces
Create clean interfaces for Scoping & Risk, COSO Mapping, Control Design, Evidence, Operating Effectiveness, Financial Analysis, Deficiency Evaluation, Co-Scientist, Structure Discovery, Reviewer, and Falsification. Prefer deterministic rules where possible; use LLMs only for semantic judgment.

### Digital Twin
Implement a minimal executable ICFR Digital Twin interface supporting scenarios such as control failure, evidence removal, increased override frequency, population growth, segregation-of-duties removal, and competing explanations.

### Structure Discovery
Implement a graph for process ↔ account ↔ assertion ↔ risk ↔ control ↔ evidence with candidate missing-link generation, confidence, evidence requirement, and validation status. AlphaFold is inspiration only; do not claim use of AlphaFold.

### AlphaEvolve-style controlled improvement
Candidate prompts/rules/routing/retrieval/thresholds → frozen benchmark → metrics → safety/provenance/reproducibility checks → compare to baseline → ACCEPT/REJECT. No autonomous production mutation and no self-promotion.

### Canonical Evidence Passport
Create one JSON-serializable schema with at least:
- passport_id, case_id, timestamp, entity, period, question
- evidence (source, source_type, provenance, rights, version, hash, retrieval time)
- ICFR scope (process, account, assertion, risk, control, COSO component/principle)
- findings, hypotheses, evidence support results
- review results, falsification results, contradictions
- digital twin results
- reproducibility (code version, provider, model, prompt/version, config, seed)
- independence (generator, reviewer, falsifier, level)
- human disposition
- final status

### Model output validation
Do not accept arbitrary provider dictionaries. Use validated schemas (dataclasses or Pydantic). Fail closed when required fields are absent.

---

## 6. TESTING REQUIREMENTS

Create executable pytest tests, with no paid API requirement, covering at least:
1. missing provenance;
2. missing rights;
3. fake evidence ID;
4. evidence ID exists but does not support claim;
5. unsupported claim;
6. reviewer FAIL;
7. reviewer INSUFFICIENT_EVIDENCE;
8. falsifier finds contradiction;
9. meaningless falsifier result;
10. same model used for generator/reviewer/falsifier;
11. cross-provider independence;
12. malformed provider response;
13. missing COSO grounding;
14. incorrect assertion mapping;
15. missing reproducibility reference;
16. Human Gate cannot be auto-approved;
17. valid authorized human approval;
18. human rejection;
19. evidence removed after analysis;
20. deterministic replay;
21. Evidence Passport serialization;
22. Digital Twin scenario;
23. model disagreement;
24. source hierarchy conflict;
25. contradictory authoritative evidence.

Use fake/test providers where appropriate.

---

## 7. FIRST POC — MICROSOFT

Design the first complete POC around one Microsoft public ICFR/financial-reporting case using only public SEC filings, CompanyFacts/XBRL if needed, authoritative SEC/PCAOB/COSO references, and reproducible public inputs.

Do NOT fabricate an ICFR deficiency. The purpose is to prove the workflow:

Evidence → ICFR scope → hypotheses → independent review → falsification → contradiction handling → scenario testing → Evidence Passport → Human Gate

If evidence is insufficient, the correct result is `INSUFFICIENT_EVIDENCE`.

---

## 8. SYSTEM DESIGN PRINCIPLES

- Evidence before narrative.
- Fail closed.
- Separate Knowledge, Evidence, Reasoning, Execution, Evaluation, Governance, and Human authority.
- Provider neutrality.
- Genuine review independence.
- Reproducibility for all material results.
- Full provenance.
- Human authority for consequential final disposition.
- Scientific falsifiability for every material hypothesis.

---

## 9. DARWIN / 100-YEAR SYSTEM THINKING

Think as if this architecture must remain useful and evolvable for 100 years. Distinguish permanent invariants from temporary technologies. Decide what remains stable if Claude, GPT, Gemini, Python libraries, databases, interfaces, and vendors change. Decide where knowledge and evidence live, which rules are deterministic, which tasks truly require AI, how a failed provider is replaced, how contradictory agents improve the system without merely voting, how failed hypotheses are preserved, and how ICFR can later generalize to audit, CAM, KAM, IFRS, ESG, and internal audit without creating one monolith.

---

## 10. REQUIRED DELIVERABLES — PHASE A THROUGH H

### PHASE A — Diagnosis
Table: Problem | Severity | Root cause | Risk | Proposed correction.

### PHASE B — Final architecture
Produce corrected LEMON V0.2 architecture:
Evidence → deterministic gates → domain reasoning → hypothesis generation → reviewer → falsifier → reconciliation → Digital Twin → reproducibility → Human Gate → Evidence Passport.
Clearly label DETERMINISTIC / LLM-MODEL / HUMAN components.

### PHASE C — File tree
Propose a clean repository tree under `Lemon-ICFR-US/`, avoiding duplication.

### PHASE D — Complete code
Provide copy-paste-ready Python for minimum viable V0.2, including models, provider protocol, evidence validation, semantic support structures, ICFR grounding, reviewer, falsification, independence evaluation, gate engine, Human Disposition, Evidence Passport, Digital Twin, orchestrator, and fake/test providers. Prefer executable code over pseudocode.

### PHASE E — Tests
Provide complete pytest files executable without paid APIs.

### PHASE F — Microsoft POC
Provide case specification, inputs, expected workflow, expected outputs, Evidence Passport example, and human approval example. Do not invent audit findings.

### PHASE G — Migration plan
Classify every change as KEEP / MODIFY / DEPRECATE / ADD. Preserve working components where possible.

### PHASE H — Acceptance test
Define measurable criteria for calling V0.2 the **LEMON-ICFR-US FIRST VALIDATED POC**: all tests pass; unsupported evidence cannot pass; reviewer genuinely evaluates claims; falsification is substantive; same-provider independence is flagged; Human Gate cannot be bypassed; Evidence Passport is generated; deterministic replay succeeds; POC finishes without fabricated deficiency.

---

## 11. IMPLEMENTATION PRIORITY

Do not solve this by adding architecture documents only. The current weakness is:

**Architecture > Implementation**

Prefer:

1 working orchestrator
+ 1 real reviewer
+ 1 real falsifier
+ 1 canonical Evidence Passport
+ 1 Microsoft POC
+ strong tests

over 50 new conceptual agents.

---

## 12. UNCERTAINTY RULE

When repository information is unavailable, label it `ASSUMPTION`, proceed, and distinguish:
- PROPOSED
- CODE PROVIDED
- LOCALLY TESTABLE
- REQUIRES REPOSITORY VERIFICATION

Do not claim code was merged, tested in GitHub, or saved to Google Drive.

---

# FINAL OBJECTIVE

Transform LEMON from **strong documentation + runnable skeleton** into **a small but scientifically credible, testable, provider-neutral ICFR agent POC**.

Replace:

Hypothesis exists → Reviewer PASS
Challenge exists → Falsification PASS

with:

Evidence → evidence-to-claim validation → ICFR grounding → hypothesis → independent reviewer decision → independent falsification → contradiction reconciliation → scenario/benchmark test → reproducibility → Human Gate → Evidence Passport.

Start with PHASE A and continue through PHASE H without asking for permission between phases. If the response becomes too long, prioritize executable code, tests, and the Microsoft POC over explanatory prose.
