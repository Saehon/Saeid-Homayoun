# NAAIL Research Assurance MCP

**Evidence-governed research assurance for accounting, auditing, finance, and AI-enabled scientific workflows.**

> **Current POC status (2026-10-04): 7 MET / 3 PARTIAL / 0 NOT_MET out of 10**
>
> **POC_COMPLETE = FALSE**
>
> **NOT_READY_FOR_HUMAN_POC_APPROVAL**

This folder contains the current Proof-of-Concept implementation of the **NAAIL Research Assurance MCP**. The project is designed to make computational research claims traceable from a published or reported claim back to the underlying table, result, code, data/source, execution evidence, and assurance state.

The project deliberately separates:

- **author-provided evidence** from independently regenerated evidence;
- **computational consistency** from methodological validity;
- **historical claims** from independently verified claims;
- **automated checks** from decisions requiring human review;
- **engineering test success** from scientific robustness.

Missing evidence is never treated as PASS.

---

## 1. What this POC is trying to prove

The POC asks whether a research-assurance layer can:

1. freeze a research case with clear provenance and limitations;
2. reconstruct a bounded public-data result independently;
3. maintain a machine-readable error taxonomy;
4. run adversarial and falsification benchmarks;
5. connect claims to evidence through an Evidence Graph;
6. generate bounded assurance states;
7. expose minimal MCP/API tools for research inspection;
8. execute an end-to-end research-assurance demonstration;
9. preserve executable test evidence; and
10. maintain synchronized release/status records across the project repositories.

The canonical assurance states are:

`VERIFIED` · `CONSISTENT` · `PARTIAL` · `FLAGGED` · `HUMAN_REVIEW`

---

## 2. Current POC gate

| Area | Current treatment |
|---|---|
| Case 001 provenance / freeze | Active POC evidence |
| Microsoft FilingLag public-data reconstruction | Separately supported |
| Microsoft COVID text claim | **PARTIAL — retrospective re-derivation under review** |
| Error Taxonomy V2 | Machine-readable POC component |
| Evidence Graph | Claim → evidence lineage |
| Designed adversarial fixtures | 19/19 designed outcomes |
| Falsification probes | **1/9 caught, 8/9 missed — limitation preserved** |
| P7 1.0 / 1.0 / 1.0 | **SELF_CONSISTENCY_CHECK only** |
| 264/264 author-output consistency | **PARTIAL under documented limitation (Option B)** |
| POC completion | **FALSE** |

The project intentionally does **not** convert these engineering results into claims of broad detector accuracy or scientific validity.

---

## 3. Scientific articles used and referenced

The project distinguishes between the **article directly used in the current POC** and broader **scientific/methodological anchors** used to guide future replication, AI-assurance, NLP, uncertainty, and falsification work.

| # | Article | Journal | Role in NAAIL Research Assurance MCP | Status |
|---|---|---|---|---|
| **1** | **deHaan, de Kok, Matsumoto & Rodriguez-Vazquez (2023), “How Resilient Are Firms’ Financial Reporting Processes?”** | **Management Science** | **Primary Case 001**; supports manuscript → claim → table → output → code → data → provenance testing, the Microsoft SEC re-derivation, Evidence Graph construction, and the current POC assurance workflow. DOI: `10.1287/mnsc.2023.4670` | 🟢 **Directly used in POC** |
| **2** | **de Kok (2025), “ChatGPT for Textual Analysis? How to Use Generative LLMs in Accounting Research”** | **Management Science** | Methodological anchor for LLM-based textual analysis, construct validation, reproducibility, and controlled use of generative AI in accounting research. DOI: `10.1287/mnsc.2023.03253` | 🔵 Methodological foundation |
| **3** | **Law & Shen, “How Does Artificial Intelligence Shape Audit Firms?”** | **Management Science** | Research anchor for AI adoption in audit firms and a future candidate for audit-agent and evidence-assurance testing. | 🔵 Research anchor / future case |
| **4** | **Huang, Li, Li & Lin, “Local Information Advantage and Stock Returns: Evidence from Social Media”** | **Contemporary Accounting Research** | Reproducible accounting/finance NLP pipeline and candidate NLP assurance case. | 🔵 Future replication case |
| **5** | **Brown, Ma & Tucker, “Financial Statement Similarity”** | **Contemporary Accounting Research** | Financial-statement textual measurement and reproducible similarity analysis; candidate for future assurance testing. | 🔵 Future replication case |
| **6** | **Breuer & Schütt, “Accounting for Uncertainty: An Application of Bayesian Methods to Accruals Models”** | **Review of Accounting Studies** | Methodological anchor for uncertainty, calibration, and probabilistic assurance testing. | 🔵 Methodological / future case |
| **7** | **Jensen, Kelly & Pedersen — replication-crisis research in finance** | **Journal of Finance** | Replication and falsification architecture; candidate foundation for future finance assurance cases. | 🔵 Replication foundation |

### How and why these articles were selected

The articles were not chosen simply because they are highly cited or published in strong journals. They were selected because, together, they provide a useful **research-assurance test bed** for NAAIL.

The selection followed six criteria:

1. **Reproducibility and inspectable evidence.** Preference was given to studies with public or author-provided code, replication repositories, documented pipelines, output files, or clearly traceable empirical procedures. NAAIL needs research objects that can be linked from claim → table → result → code → data/source → assurance state.

2. **Direct relevance to accounting, auditing, finance, and reporting.** The project focuses on domains where research evidence may affect auditors, regulators, investors, boards, researchers, and AI systems. The selected papers therefore cover financial reporting processes, auditing and AI, financial-statement analysis, accounting/finance NLP, uncertainty, and replication.

3. **Methodological diversity.** The set deliberately includes regression-based empirical accounting, public-filing reconstruction, NLP/textual analysis, similarity measures, Bayesian/uncertainty methods, AI-related audit research, and replication/falsification research. This helps test whether the assurance architecture can generalize beyond one statistical design.

4. **Suitability for adversarial and provenance testing.** NAAIL is designed to detect broken links between claims and evidence, not merely rerun code. The selected studies provide useful opportunities to test provenance, missing dependencies, restricted data, output consistency, construct validity, sensitivity analysis, and human-review gates.

5. **Availability of a defensible bounded test.** A study does not need fully open raw data to be useful. Where licensed or proprietary inputs prevent full reproduction, NAAIL can still test bounded claims such as author-output consistency, public-data reconstruction, code-to-table lineage, or methodological limitations—provided those boundaries are stated explicitly.

6. **Value for future agentic research assurance.** The broader anchor papers were chosen because they can become future cases for AI-to-AI checking, evidence-grounded agents, falsification, uncertainty calibration, and independent scientific review. They extend the project from one accounting case toward a reusable research-assurance architecture.

#### Why deHaan et al. (2023) was selected as Case 001

deHaan, de Kok, Matsumoto & Rodriguez-Vazquez (2023) was selected as the **Primary POC Article** because it offers an unusually useful combination of:

- a Management Science research setting directly related to financial-reporting processes;
- an author replication package with documented code and outputs;
- multiple computational components, including Python, SAS and Stata;
- clear table/output/code relationships that can be mapped into an Evidence Graph;
- important real-world dependencies that are not fully public, allowing NAAIL to demonstrate the distinction between author-output consistency and full independent reproduction; and
- a public SEC-based component that can be independently re-derived without pretending that restricted-data replication has been completed.

That combination makes it a strong first test of the project's core proposition:

> **Research assurance should verify not only whether code runs, but whether every scientific claim is supported by an inspectable, provenance-preserving evidence chain with explicitly bounded assurance.**

#### Why the other papers are included

The remaining papers are not claimed as completed NAAIL replications. They are included as **scientific and methodological anchors** because each extends a different capability that the platform will eventually need:

- **de Kok (2025):** generative LLM use, textual-analysis validity, and construct validation.
- **Law & Shen:** AI in audit firms and future audit-agent/evidence-assurance testing.
- **Huang, Li, Li & Lin:** accounting/finance NLP and reproducible text-analysis pipelines.
- **Brown, Ma & Tucker:** financial-statement similarity and measurement reproducibility.
- **Breuer & Schütt:** uncertainty, probabilistic reasoning, and calibration.
- **Jensen, Kelly & Pedersen:** replication, robustness, and falsification at scale.

Accordingly, the article set is intentionally layered:

`Case 001 direct POC evidence → methodological anchors → future replication cases → broader agentic research-assurance benchmark library`

This prevents the README from implying that every cited paper has already been independently reproduced by NAAIL.

### Primary POC article

The core scientific article actually exercised in the present POC is:

**deHaan, de Kok, Matsumoto & Rodriguez-Vazquez (2023), _How Resilient Are Firms’ Financial Reporting Processes?_, Management Science, 69(4), 2536–2545. DOI: `10.1287/mnsc.2023.4670`.**

Within this repository it underpins:

`Case 001 → author-output consistency → Microsoft SEC FilingLag reconstruction → Evidence Graph → adversarial benchmark → Research Assurance MCP`

The remaining papers are currently treated as **scientific or methodological anchors**, not as completed POC replications.

---

## 4. Important scientific correction: Microsoft COVID v1

The original Microsoft COVID v1 rule was frozen after earlier project artifacts had already recorded COVID-presence outcomes for the same ten Microsoft observations.

That means v1 cannot honestly be described as a clean preregistered or blind confirmation.

The historical v1 artifacts are preserved unchanged:

- frozen rule Git blob:  
  `d7760b4909ae84896cae8797fb8536f59d36053c`
- original historical scanner blob:  
  `1b65c3cc60b0305aed244a642923ea50c95b0045`
- later historical scanner blob:  
  `4602d71d9a1db84405a17470fea03638a8595758`

The independent-review decision was:

`Q5_PROTOCOL_DECISION = REJECT_V1_PREREGISTRATION`

This is a rejection of the **preregistration label**, not necessarily of the bounded factual reproduction question.

---

## 5. Retrospective re-derivation: v1-R

The POC now uses a clearly labeled **retrospective re-derivation protocol (v1-R)**.

Current candidate fingerprints:

- amended v1-R protocol:  
  `83af7a6859b2d44b782b5d838420f07717ea79d3`
- amended v1-R scanner:  
  `5b0b31de72f67fd14439875db58cab7f6427f5a1`

### Term-set design

The deciding term sets are:

- **PRIMARY** — historical v1 COVID pattern;
- **S1** — adds compact COVID19, plural coronavirus, and SARS-CoV-2 forms;
- **S2** — S1 without the broad word `corona`.

**S3** includes the generic term `pandemic`, but independent review correctly identified that this captures a broader construct such as generic pandemic-risk language.

Therefore:

- PRIMARY / S1 / S2 = **DECIDING**
- S3 = **BROAD_DIAGNOSTIC only**

### Decision rule

The scanner is designed so that:

- disagreement among PRIMARY / S1 / S2 → `FLAGGED`;
- any PRIMARY / S1 / S2 match in **Q4-2019** → `FLAGGED`;
- S3-only matches do **not** automatically flag the run;
- every S3 match snippet for an S3-only filing is retained for independent human review;
- the automated scanner can emit `HUMAN_REVIEW` or `FLAGGED`;
- the automated scanner **cannot emit VERIFIED**.

A bounded `VERIFIED` conclusion is only possible after independent review of the execution evidence and relevant snippets.

### Key files

- [v1-R protocol](./derived/covid_rederivation_protocol_v1r.json)
- [v1-R scanner](./derived/msft_covid_rederivation_scan_v1r.py)
- [S3 pre-execution amendment](./derived/Q5_V1R_PREEXECUTION_AMENDMENT_S3_2026-10-04.md)
- [October-1 provenance correction](./derived/Q5_CORRECTION_OCT1_COVID_PROVENANCE_2026-10-04.md)
- [Protocol-validity amendment](./derived/Q5_PREEXECUTION_PROTOCOL_AMENDMENT_2026-10-04.md)
- [Latest Claude review package](./derived/Q5_V1R_CLAUDE_REVIEW2_PACKAGE_2026-10-04.md)

---

## 6. Execution remains blocked pending independent review

**No v1-R SEC retrieval has been performed.**

**No Microsoft COVID workflow-dispatch run has been executed for v1-R.**

The current state is:

`COVID_R3_STATUS = BLOCKED_INDEPENDENT_REVIEW`

The amended protocol and scanner must be independently approved before execution.

---

## 7. Infrastructure PR — #116

**Draft PR #116** replaces the rejected v1 execution path with the v1-R execution path.

[Open PR #116](https://github.com/Saehon/Saeid-Homayoun/pull/116)

Scope:

- exactly **one changed file**;
- file: `.github/workflows/naail_msft_covid_scan.yml`;
- `workflow_dispatch` only;
- `permissions: contents: read`;
- verifies the reviewed rule, protocol, and scanner Git blobs before the scanner can access SEC;
- executes only the reviewed v1-R scanner;
- uploads the result or partial-failure record with `if: always()`.

Current workflow candidate blob:

`a3bef871f827674c2b24123dd25746b792ca9dc4`

**PR #116 is not yet approved for merge or execution.**

---

## 8. Prior-exposure governance — #117

A separate governance PR addresses the institutional lesson from this case.

[Open PR #117](https://github.com/Saehon/Saeid-Homayoun/pull/117)

Its direction is to strengthen future rule governance by:

1. checking whether the declared source data already existed at the freeze commit;
2. requiring explicit `prior_exposure` treatment;
3. using Git-history ancestry rather than author dates to establish ordering;
4. validating the governance registry against a real JSON Schema; and
5. expanding rule/protocol coverage under `derived/**`.

This PR is **separate from the scientific v1-R execution gate** and remains subject to independent review.

---

## 9. What readers should understand about the 8/9 missed probes

The POC deliberately preserves a negative result:

> **8 of 9 realistic evasion probes were missed.**

This is not hidden or tuned away.

The known nine probes are now considered **development evidence**, not an independent future test set. Any later detector improvement must be evaluated on fresh, independently authored or held-out probes.

That limitation is scientifically useful: the purpose of the POC is not to manufacture a perfect detector score, but to demonstrate an evidence-governed assurance process that records both successes and failures.

---

## 10. Case 001 and the 264/264 result

The project contains a historical statement that **264/264 published regression cells matched author-provided output at published precision**.

However, the currently accessible POC package does not provide a fully inspectable per-cell evidence chain sufficient to re-perform all 264 comparisons independently.

Therefore the POC records this as:

**author-output consistency = PARTIAL**

The human governance decision for this POC is **Option B: documented limitation**.

The project does not reconstruct unavailable evidence.

---

## 11. Current execution sequence

The intended order is:

```text
Independent review of amended v1-R protocol/scanner/workflow
        ↓
Human approval of infrastructure PR #116
        ↓
Merge #116 only
        ↓
Execute the reviewed retrospective v1-R scanner
        ↓
Collect the 10-filing evidence package
        ↓
Independent review of snippets and sensitivity results
        ↓
Reassess POC criterion 2
        ↓
Final GitHub / Drive release reconciliation
        ↓
Human POC approval gate
```

The project must remain inside the POC gate until those evidence steps are completed.

---

## 12. Repository map

| Location | Purpose |
|---|---|
| [MASTER_POC_V1_ROADMAP.md](./MASTER_POC_V1_ROADMAP.md) | POC → V1 roadmap |
| [POC_RELEASE_MANIFEST.md](./POC_RELEASE_MANIFEST.md) | release/status manifest |
| [phase_register.json](./phase_register.json) | phase-state record |
| [case-001-management-science/](./case-001-management-science/) | frozen Case 001 materials |
| [benchmark/](./benchmark/) | benchmark materials |
| [taxonomy/](./taxonomy/) | error taxonomy |
| [evidence-graph/](./evidence-graph/) | claim/evidence lineage |
| [p4/](./p4/) | POC phase implementation |
| [p5/](./p5/) | POC phase implementation |
| [p6/](./p6/) | POC phase implementation |
| [p7/](./p7/) | integration / assurance-report layer |
| [derived/](./derived/) | derived evidence, corrections, re-derivations, review packages |
| [hourly-build/](./hourly-build/) | execution records, repairs, and operational history |

---

## 13. Governance principles

This project follows several hard rules:

- immutable historical evidence is preserved;
- corrections are additive;
- missing evidence never becomes PASS;
- no scientific claim is upgraded because an automated process says so;
- no protected merge occurs without human approval;
- detector limitations remain visible;
- preregistration claims require actual pre-exposure discipline;
- retrospective re-derivation must be labeled as retrospective;
- human review remains a formal gate where judgment is required.

---

## 14. Current reader takeaway

The NAAIL Research Assurance MCP POC is **scientifically active but not complete**.

The strongest evidence of progress is not a perfect score. It is the project’s ability to detect its own provenance errors, preserve negative benchmark results, reject an invalid preregistration label, redesign the test transparently before execution, and keep human approval as the final assurance gate.

**Current state:**

`7 MET / 3 PARTIAL / 0 NOT_MET out of 10`

`POC_COMPLETE = FALSE`

`NOT_READY_FOR_HUMAN_POC_APPROVAL`
