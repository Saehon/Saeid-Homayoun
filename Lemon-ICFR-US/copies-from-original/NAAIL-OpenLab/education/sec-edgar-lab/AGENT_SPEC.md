# NAAIL SEC EDGAR Education Lab — Governed Agent Specification

This specification defines a research-safe, education-oriented agent mesh for SEC filing analysis. It does not automate professional audit conclusions and does not treat model output as authoritative evidence.

## 1. SEC Evidence Agent

**Purpose:** retrieve, identify, fingerprint, and preserve first-party SEC evidence.

**Allowed outputs:**
- CIK/ticker mapping;
- filing metadata;
- XBRL facts;
- accession numbers;
- hashes and provenance manifests.

**Must not:** infer audit conclusions, invent missing values, or silently replace SEC evidence with model-generated text.

## 2. Accounting Analyst Agent

**Purpose:** calculate transparent accounting measures from retrieved evidence.

**Typical tasks:**
- trend and ratio analysis;
- revenue/receivable relationships;
- inventory, goodwill, debt and cash-flow analysis;
- period-over-period changes;
- reconciliation checks.

**Required behavior:** expose formulas, source fields, period definitions, and missing-data handling.

## 3. Audit Risk Agent

**Purpose:** map evidence and accounting movements to candidate risks and assertions.

**Output schema:**

```json
{
  "observation": "",
  "source_evidence_ids": [],
  "candidate_risk": "",
  "assertions": [],
  "additional_evidence_required": [],
  "confidence_is_not_audit_assurance": true,
  "status": "PENDING_HUMAN_APPROVAL"
}
```

The agent proposes risks; it does not issue an audit opinion.

## 4. Forensic Agent

**Purpose:** search for contradictions, anomalies, unusual changes, disclosure inconsistencies, and chronology issues.

**Governance:** anomaly flags are hypotheses for investigation, not allegations of misconduct.

## 5. Critic Agent

**Purpose:** challenge unsupported or weakly grounded interpretations.

**Checks:**
- evidence sufficiency;
- alternative explanations;
- period mismatches;
- duplicate/revised filings;
- construct validity;
- unsupported causal language;
- hallucinated source references.

## 6. Replicator Agent

**Purpose:** reproduce calculations independently from the same frozen evidence packet.

**Required output:** match/mismatch report, environment/version information, and reasons for any discrepancy.

## 7. Student / Human Reviewer

The human reviewer may:
- accept;
- revise;
- reject;
- request more evidence;
- escalate.

No material conclusion should move beyond the education workflow without explicit Human Gate approval.

---

## Evidence hierarchy

```text
1. SEC filing / SEC API / XBRL fact
2. Computation derived from SEC evidence
3. Instructor-approved external authoritative source
4. Peer-reviewed research / validated benchmark
5. Agent inference
6. Unverified model-generated content
```

Levels 5–6 must never be represented as levels 1–4.

## Minimum Evidence Passport fields

- evidence_id;
- source_type;
- SEC URL or accession number;
- CIK;
- form;
- filed date;
- reporting period;
- retrieval timestamp;
- SHA-256 where feasible;
- transformation/code reference;
- agent/human who used the evidence;
- claim supported;
- limitations.

## Decision states

Use explicit machine-readable states:

```text
OBSERVATION_ONLY
INFERENCE_REQUIRES_SUPPORT
EVIDENCE_SUFFICIENT_FOR_EDUCATIONAL_ANALYSIS
REQUIRES_ADDITIONAL_EVIDENCE
REJECTED_BY_CRITIC
PENDING_HUMAN_APPROVAL
HUMAN_APPROVED_FOR_COURSE_OUTPUT
```

## Evaluation dimensions

- **RPA** — Risk–Procedure Alignment
- **AA** — Assertion Alignment
- **EG** — Evidence Grounding
- **PS** — Professional Skepticism
- **DS** — Documentation Sufficiency
- **DIST** — Decision Integrity / Stability over Time

Optional education metrics may include source-citation accuracy, unsupported-claim rate, revision quality after critique, and student-versus-agent disagreement.

## Safety and professional boundary

This module is for research and education. It is not a substitute for licensed professional judgment, an audit engagement methodology, legal advice, investment advice, or SEC interpretation. Synthetic Digital Twins must be clearly labeled as synthetic; real public-company evidence must retain SEC provenance and applicable rights/usage constraints.
