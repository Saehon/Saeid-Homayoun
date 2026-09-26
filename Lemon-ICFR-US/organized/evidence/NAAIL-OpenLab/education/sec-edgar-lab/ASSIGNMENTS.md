# NAAIL SEC EDGAR Education Lab — Assignment Bank

These assignments are designed for accounting, auditing, forensic accounting, finance, sustainability, and AI/data courses. Instructors should select entities and periods appropriate to the course and preserve SEC-source provenance.

## Assignment 1 — Filing and XBRL provenance

**Level:** Bachelor / introductory  
**Task:** Select one SEC registrant, identify its CIK, retrieve its filing history and CompanyFacts, and document the source, filing date, reporting period, form type, and accession number.

**Deliverables:**
- one-page provenance memo;
- selected financial facts table;
- short discussion of why filing date and report period are not interchangeable;
- reproducible code or notebook.

## Assignment 2 — Financial statement reconstruction

**Level:** Bachelor / Master  
**Task:** Use SEC XBRL facts to reconstruct selected income-statement and balance-sheet measures for at least three periods.

**Required checks:**
- units and scale;
- annual versus quarterly facts;
- duplicate/revised filings;
- fiscal period labels;
- reconciliation to the filed financial statements where feasible.

## Assignment 3 — Audit-risk mapping

**Level:** Master / auditing  
**Task:** Identify unusual movements in selected accounts and map them to potential risks of material misstatement and relevant assertions.

**Output matrix:**

| Evidence | Observation | Potential risk | Assertion(s) | Additional evidence needed | Student judgment |
|---|---|---|---|---|---|

Students must distinguish a **data anomaly** from an **audit conclusion**.

## Assignment 4 — MD&A and Risk Factors NLP

**Level:** Master / analytics  
**Task:** Extract MD&A and Risk Factors from multiple annual filings and construct transparent textual measures such as length, change, similarity, topic prevalence, uncertainty, or sentiment.

**Required controls:**
- filing chronology;
- section extraction validation;
- model/version record;
- human review of a validation sample;
- no claim that an LLM score is ground truth.

## Assignment 5 — Forensic / enforcement case

**Level:** Master / forensic accounting  
**Task:** Combine public SEC filings with an instructor-approved enforcement case or AAER-related source. Reconstruct a timeline of disclosed accounting signals before, during, and after the enforcement event.

Students must separate:
1. contemporaneous public evidence;
2. later enforcement findings;
3. retrospective interpretation.

## Assignment 6 — AI versus human professional judgment

**Level:** Master / professional  
**Task:** Provide the same frozen SEC evidence packet to a student and an AI/agent workflow. Compare their risk identification, evidence use, unsupported claims, and escalation decisions.

**NAAIL evaluation dimensions:**
- RPA — Risk–Procedure Alignment;
- AA — Assertion Alignment;
- EG — Evidence Grounding;
- PS — Professional Skepticism;
- DS — Documentation Sufficiency;
- DIST — Decision Integrity / Stability over Time.

The student remains responsible for the final Human Gate decision.

## Assignment 7 — SEC CompanyFacts research panel

**Level:** PhD / empirical research  
**Task:** Construct a chronology-safe firm-quarter or firm-year panel using SEC CompanyFacts.

**Minimum research package:**
- variable dictionary;
- source manifest;
- inclusion/exclusion logic;
- duplicate/revision handling;
- missingness diagnostics;
- descriptive statistics;
- code and environment file;
- one falsification or robustness test.

## Assignment 8 — Multi-agent SEC Digital Twin

**Level:** Advanced Master / PhD  
**Task:** Build a synthetic Digital Twin from a frozen SEC evidence packet. Run at least four roles: Evidence Agent, Accounting Analyst, Audit Risk Agent, and Critic.

**Governance requirement:**
The agents may propose interpretations, but they may not fabricate SEC facts. Every material claim must point to source evidence or be explicitly marked as inference. Final disposition remains `PENDING_HUMAN_APPROVAL` until reviewed.

---

## Suggested grading dimensions

| Dimension | Weight suggestion |
|---|---:|
| Source provenance and reproducibility | 20% |
| Accounting/audit correctness | 25% |
| Evidence-to-claim traceability | 20% |
| Analytical rigor | 15% |
| Professional skepticism / critique | 10% |
| Documentation and communication | 10% |

These weights are examples only; instructors should adapt them to local course requirements.
