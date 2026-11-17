# When AI Agents Become Auditors: Evidence-Grounded Delegation, Multi-Agent Coordination, and Accountability in Financial Reporting Assurance

**AuditGold-PROJECT — Manuscript Version 2 | 17 November 2026 | Research working draft, not submitted**  
**Primary target:** *Journal of Management Information Systems* (JMIS; FT50), special issue *Agentic Organizations: Designing, Governing, and Managing AI Agents*  
**Optional extended abstract:** 15 December 2026 | **Full manuscript:** 1 February 2027  
**Status:** The artifact and research protocol exist; no controlled model experiment, expert gold-key adjudication, or inferential estimates have been completed. This is a proposal and manuscript draft, not a report of empirical findings.

## Abstract

As organizations delegate consequential workflow steps to artificial-intelligence agents, the central governance challenge shifts from answer accuracy to accountable action. This study develops **evidence-grounded delegated assurance** (EGDA), a theory-informed design for governing agentic participation in financial reporting assurance. EGDA posits that the value of delegation depends jointly on (i) verified and temporally valid evidence, (ii) coordination across specialist agents, (iii) explicit decision-right boundaries, and (iv) contestable human authorization. We instantiate this framework in AuditGold-PROJECT, an auditable research testbed for Critical Audit Matters (CAMs), internal control over financial reporting (ICFR), and professional accounting/auditing knowledge. The present candidate bank contains 3,000 algorithmically generated synthetic certification questions built from 112 credential–topic template families; an additional 207 earlier records include 46 CAM/ICFR-centered V3 scenarios. These are candidate questions and provisional answers, not independently verified professional gold standards. We specify a staged empirical design combining publicly accessible SEC filings and PCAOB source materials, documented replication packages from leading accounting/IS journals, and expert-adjudicated multi-document engagement binders. A randomized, matched evaluation would compare six architectures from a standalone language model to verifier-gated specialist multi-agent RAG across contradictory evidence, changing standards, and varying authority constraints. Primary outcomes are correct **authorized** workflow completion, verified evidence provenance, appropriate escalation, and unsafe-action incidence; ordinary answer accuracy is secondary. By distinguishing technical competence from delegated organizational authority, the study aims to extend IS delegation theory to regulated, evidence-intensive professional workflows. All hypothesized performance relationships await empirical testing.

**Keywords:** agentic organizations; accountable autonomy; RAG; multi-agent systems; professional judgment; audit evidence; critical audit matters; ICFR; governance; reproducibility.

## 1. Introduction: From plausible answers to authorized audit actions

Generative AI frequently produces convincing analyses of financial statements, audit standards, and control exceptions. Yet a coherent answer is not equivalent to an audit procedure, and a correct numerical computation is not authorization to amend a journal entry, sign a workpaper, conclude on a material weakness, or issue an audit opinion. The organizational transition to agentic AI entails new delegated goals, autonomy, access to enterprise tools, consequential workflow actions, and accountability arrangements. The July 2026 JMIS special-issue call explicitly identifies these as defining properties of agentic organizations and excludes studies that treat AI solely as a chatbot or productivity tool (JMIS, 2026, pp. 1–4). We therefore move the unit of analysis from a *text response* to a *delegated assurance episode*: a sequence of evidence retrieval, numerical recomputation, contradiction resolution, proposed actions, escalation, approval, and trace logging.

The accounting setting makes this distinction consequential. PCAOB AS 3101 requires auditors on covered issuer engagements to determine and communicate CAMs in a manner linked to challenging, subjective, or complex audit judgment. PCAOB AS 2201 addresses the audit of ICFR, including testing controls and evaluating deficiencies. Neither a published CAM paragraph nor a management Item 9A disclosure, by itself, provides the auditor's complete working papers. Similarly, a risk-scoring model trained on SEC enforcement actions predicts an enforcement-linked proxy rather than proving an issuer's misconduct. AuditGold operationalizes these distinctions as testable governance constraints. The study is grounded in CAM and ICFR rather than in generic multiple-choice examination scoring, although cross-credential cases provide calibrated competency controls.

The proposed theoretical question is: **Under what conditions does specialist multi-agent RAG improve the effectiveness of delegated financial assurance work without undermining human accountability?** The primary operational question is whether system architecture and verification gates causally affect correct *authorized* completion, not merely answer correctness. The design targets the JMIS call's questions about delegated autonomy, multi-agent orchestration, epistemic governance, and accountable work redesign; the aim is theoretical and organizational rather than a model leaderboard.

Three contributions are proposed, subject to future evidence. First, we conceptualize **evidence-grounded delegated assurance** as a governance capability coupling retrieval provenance to decision rights. Second, we propose a **delegation envelope** defining which actions an agent may propose, execute in a sandbox, or must escalate to a licensed professional. Third, we develop an inspectable measurement system capable of comparing architectures under identical evidence and authority constraints. In doing so we distinguish the reproducibility of *published source papers*, the accessibility of *their datasets*, and the validity of *our own newly generated answers*.

## 2. Relevant FT50/AJG research and available replication materials

### 2.1 Theory of delegated agency and sociotechnical governance

Baird and Maruping (2021, *MIS Quarterly*, FT50) provide a theory of delegation to and from agentic information-system artifacts. Their framework implies that organizations must specify task allocation, allocation of accountability, monitoring, and feedback rather than viewing technology as passive infrastructure. Dennis, Lakhiwal, and Sachdeva (2023, *JMIS*, FT50) theorize and examine AI agents as team members, informing coordination and trust. Queiroz, Anand, and Baird (2024, *JMIS*, FT50) examine managerial appraisal of AI investment. These papers motivate EGDA, but we have not established that their complete author data and code are publicly downloadable; we classify them as **theory and design evidence**, not as ready-to-run replication packages.

### 2.2 Audit quality, internal control, and fraud prediction

Doyle, Ge, and McVay (2007, *Journal of Accounting and Economics*, FT50) establish heterogeneity in weaknesses in ICFR; Ashbaugh-Skaife et al. (2009, *Journal of Accounting Research*, FT50) analyze links between deficiencies, firm risk, and the cost of equity. Such studies justify focusing on the seriousness of evidence and the aggregation of deficiencies. They do not justify labeling every control exception a material weakness. We did not verify unrestricted code-and-data packages for these foundational articles.

Bao et al. (2020, *Journal of Accounting Research*, FT50) provide unusually strong reproducibility support: the authors' [FraudDetection repository](https://github.com/JarFraud/FraudDetection) contains a final firm-year CSV, AAER firm-year observations, a datasheet, SAS processing documentation, and MATLAB RUSBoost code (`run_RUSBoost.m`, `tune_RUSBoost.m`, `data_reader.m`, `evaluate.m`). The published paper's DOI is [10.1111/1475-679X.12292](https://doi.org/10.1111/1475-679X.12292); the publisher also posted an [erratum](https://doi.org/10.1111/1475-679X.12454). This supports a reproducible **risk-triage benchmark** and a method check for severe class imbalance, but AAER-linked cases are not a gold label for every type of corporate fraud. Historical financial inputs originated in Compustat; researchers must read the repository's provenance and licensing before redistribution.

Law and Shen (2025, *Management Science*, FT50) examine the hiring of AI-related employees in U.S. audit offices and audit outcomes, including internal-control opinions. Their publisher- and author-linked [replication package](https://kelvinlaw.me/data) is described as containing data and code to reproduce tables and figures; the article DOI is [10.1287/mnsc.2022.04040](https://doi.org/10.1287/mnsc.2022.04040). These materials support an audit-industry contextual extension or external validity analysis, **not** a direct test of our agents unless office–firm and period linkages can be independently constructed and appropriately licensed. Data/code presence was confirmed at the source site; this project has not downloaded or executed the archive.

### 2.3 AI in financial reporting, independent verification, and methodological falsification

Blankespoor, deHaan, and Li (2026, *Journal of Accounting Research*, FT50) document generative-AI use in disclosure text and provide the publicly released [GenScore dataset](https://github.com/ed-dehaan/GenScore), under CC BY 4.0; their [published article](https://doi.org/10.1111/1475-679x.70050) specifies the construct and validation approach. **Data availability does not imply open-source reproduction of their original commercial detection algorithm.** GenScore may help construct disclosure-risk strata or test sensitivity to AI-like narrative properties. It must not be treated as a definitive machine-authorship or audit-quality label.

Ciconte, Rozario, and Urcan (2026, *Review of Accounting Studies*, AJG 4), [10.1007/s11142-026-09967-y](https://doi.org/10.1007/s11142-026-09967-y), examine AI-driven discovery of securities-law shocks and the dangers of plausible but spurious results. Their [AI-Powered Accounting Scholarship repository](https://github.com/AIPoweredAccountingScholarship/Base) contains notebooks, prompts and AI-generated manuscript artifacts. This creates an important benchmark for **falsification and epistemic safeguards**, but it is not a collection of audit opinions or a substitute for authenticated workpapers.

Nguyen and Nguyen (2026, *Information Systems Research*, FT50) provide a versioned [replication package](https://github.com/mikenguyen13/p-hacking-publication-bias-information-systems) with R/Quarto scripts, analysis data and documentation for tests of reporting and specification bias in IS research ([archived record](https://zenodo.org/records/21855538)). It is particularly useful for pre-registration, multiple-testing corrections, and transparent statistical reporting. The package is an **evaluation-methodology analogue**, not an audit-case dataset.

Eulerich et al. (2024, *Review of Accounting Studies*, AJG 4) demonstrate the relevance of CPA/CMA/CIA/EA certification benchmarks, but passing professional questions is distinct from conducting a sufficiently documented audit. Griffith, Rousseau, and Zehms (2026, *Review of Accounting Studies*, AJG 4) examine auditors' CAM implementation experiences; their work motivates a distinction between narrative compliance and substantive responsiveness. Verified public computational materials were not established for either source in this review.

### 2.4 Open technical benchmarks and primary public evidence (not FT50/AJG4 journal papers)

**FinQA** (Chen et al., 2021, EMNLP) makes 8,281 financial numerical reasoning questions, gold programs, and model code accessible at [GitHub](https://github.com/czyssrs/FinQA). **TAT-QA** (Zhu et al., 2021, ACL) provides 16,552 hybrid tabular/textual questions and evaluation code at [GitHub](https://github.com/NExTplusplus/TAT-QA); the authors describe the dataset as CC BY 4.0. **FinanceBench** (Islam et al., 2023, arXiv) makes only a **150-question sample** openly available with annotated evidence and source PDFs at [GitHub](https://github.com/patronus-ai/financebench); the Hugging Face dataset card specifies **CC BY-NC 4.0**, and the 10,231-case complete corpus is not freely licensed. Their benchmarks measure financial retrieval/reasoning, not audit authorization. Distinct publication categories and licenses are preserved in Table 1.

The [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) provide public company submissions and XBRL companyfacts. They can support reproducible CAM narrative extraction, Section 9A ICFR disclosures, and financial reconciliation after appropriate access handling. [PCAOB AS 3101](https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101), [AS 2201](https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201), and public inspection reports are primary audit-source anchors, but published filings and inspection reports do **not** expose complete confidential engagement working papers. The AS 2201 December 2026 effective-date amendments must be version-tagged; no future-effective standard may be retroactively applied to earlier audit cases.

### Table 1. Reproducibility and transferability matrix

| Category | Source / venue | Public code | Public data | Immediate AuditGold use | Limitation |
|---|---|---|---|---|---|
| A — data + code verified | Bao et al. (2020), *JAR* FT50 | MATLAB RUSBoost, SAS materials | Final CSV and AAER labels | Fraud triage and imbalance control | AAER proxy and historic Compustat provenance |
| A — publisher-described package | Law & Shen (2025), *Management Science* FT50 | Publisher says yes | Publisher says yes | Audit AI adoption/ICFR context | Archive not locally executed; audit-office links needed |
| A — analysis package verified | Nguyen & Nguyen (2026), *ISR* FT50 | R and Quarto | Coded research-test dataset | Research statistical transparency | Not a CAM/ICFR dataset |
| B — variable dataset | Blankespoor et al. (2026), *JAR* FT50 | Original detection code not verified | GenScore CSV ZIP | Disclosure AI-proxy stratification | Not authorship ground truth |
| C — workflows/prompts | Ciconte et al. (2026), *RoAS* AJG 4 | Notebook/prompt artifacts | Generated research papers | Agent falsification tests | Input-data completeness not established |
| D — theory only | Baird & Maruping; Dennis et al.; Doyle et al.; Ashbaugh-Skaife et al. | Not verified | Not verified | Delegation, teamwork, ICFR theoretical mechanisms | Do not call these replicable |
| E — open non-FT50 benchmarks | FinQA; TAT-QA | Yes | Yes | Numerical reasoning and provenance | Not agentic action; license compliance |
| E — limited open non-FT50 sample | FinanceBench | Public dataset/eval resources | 150 cases only | Evidence-span retrieval | CC BY-NC; full corpus restricted |
| F — public primary records | SEC EDGAR; PCAOB | API/parser can be written | Filings/standards/inspections | CAM/ICFR case construction | No full audit workpapers; access limits |

## 3. Evidence-grounded delegated assurance: theoretical model

We define a **delegation envelope** D = (G, A, E, T, P, O), where G is the delegated organizational goal; A the agent's tool/action authority; E the admissible evidence set and provenance; T the governing time and standards version; P the intervention, escalation, and override policy; and O the observable trace of actions. An agent's ability to infer a plausible answer does not establish permission to take an organizational action. A delegated assurance episode is successful only when the evidence-backed conclusion is correct, the process complies with P, and O supports ex post review.

We propose an **epistemic escalation threshold**: when source validity, record completeness, or contradictory material evidence is unresolved, the permitted terminal state is *request evidence* or *escalate*, not *close issue*. This is distinct from a model refusing all difficult cases. Correctly calibrated escalation balances two losses: unsafe unsubstantiated closure and excessive rejection of adequately evidenced routine tasks. We hypothesize that independent verification changes that frontier.

The multi-agent mechanism contains five separable activities: (1) claim decomposition by an orchestrator; (2) source retrieval and version control; (3) specialized accounting, ICFR, CAM, and forensic analysis; (4) an independent claim/evidence contradiction checker; and (5) execution policy enforcement plus professional approval for consequential outputs. No agent receives independent authority to modify signed assurance opinions or write into production ERP systems. All simulated actions take place within sandbox case records.

### Hypotheses

**H1 (specialization):** Holding foundation model, admissible documents, token budgets, and tools constant, specialist multi-agent RAG improves source-grounded judgment for cross-document CAM/ICFR tasks relative to a tool-using single agent, particularly where evidence spans distinct accounting and audit domains. This is not a prediction that multi-agent always outperforms simpler methods.

**H2 (contradiction amplification):** The relative advantage of independent contradiction verification in avoiding unsupported closure increases when authoritative evidence conflicts with later management narratives, alternative ledgers, or undated generated summaries.

**H3 (bounded authority):** Explicit, testable decision-right gates reduce unauthorized financial/audit action and unjustified issue closure compared with ungated orchestration; the improvement may entail more escalations and higher cost.

**H4 (temporal provenance):** Version-aware authority routing reduces answers based on rules not yet in force, with the greatest effects in time-sensitive ICFR and professional-standards cases.

**H5 (organizational efficiency and calibration):** Improvements in safe completion are not explained solely by larger prompts, more retrieval calls, additional compute, or indiscriminate abstention; results are therefore evaluated on a quality–cost–escalation frontier rather than aggregate accuracy alone.

These hypotheses specify falsifiable theoretical mechanisms. No positive or statistically significant effects are asserted.

## 4. Artifact, sample selection, and publicly reproducible source construction

### 4.1 What already exists—and what does not

AuditGold V4 has **3,000** generated credential questions (1,000 each at easy, intermediate, difficult levels), including **100 core questions for each of 14 designations**. This is primarily a synthetic competency bank built from **112 credential-by-topic template families**: it is not 3,000 independently constructed audit engagements. Family-blocked splits contain 1,501 development, 749 validation, and 750 holdout question records. V1–V3 contribute 207 additional candidate records, including V3's **20 CAM and 26 ICFR cases**. Counting all files gives 3,207 provisional records before semantic deduplication. No 3,207-answer expert validation or actual LLM model comparison exists. The most credible high-stakes *agentic* experiment should prioritize the 46 CAM/ICFR cases and subsequently expand them into adjudicated multi-document case binders; V4 supplies calibration rather than the main causal outcome.

### 4.2 Sampling units, labels, and evidence binders

**Stage A — public-paper replication controls:** inventory and locally reproduce, where license/software permit, a selected subset of Bao et al. RUSBoost; Nguyen and Nguyen's research-analysis scripts; and numerical QA checks using FinQA/TAT-QA. This is a *methods transfer and validation exercise*, not an assertion that original journal samples have been replicated today. Record source commit/release, license, row count, metric definition, original vs reconstructed numerical results, and source restrictions.

**Stage B — public CAM and ICFR archival records:** create issuer–year–issue tasks from SEC annual filings and accompanying public auditors' reports, with company CIK, accession, filing date, fiscal year, source section, audit-report paragraph, and archive hash. CAM presence and language should be separately labeled from ICFR auditor/management opinions and material-weakness assertions. Sample strata should include industries, accounting issues, years, filers with and without material-weakness disclosures, and varying CAM risk/response specificity. Observed correlations between these disclosures do not prove audit failure; the construct is **public-document consistency and defensibility**.

**Stage C — synthetic, expert-reviewed engagement binders:** for each CAM/ICFR anchor, assemble at least three time-stamped documents (e.g., contract, journal schedule, control-test record, audit committee excerpt, draft CAM). Insert randomized contradictions, missing evidence, signed/unsigned documents, and outdated rules. Preserve an inaccessible-to-agents adjudication file containing clause-level standard support, acceptable alternative outcomes, and conditional authorization decisions. Target an initial independently adjudicated **50–100 unique scenario families**, not hundreds of repeated numeric permutations. Report both case-family N and augmented-variant N.

**Stage D — organizational workflow actions:** in a sandbox, require agents to select valid next actions: `RETRIEVE_MORE`, `RECALCULATE`, `DRAFT_FINDING`, `ESCALATE_HUMAN`, `CLOSE_WITH_EVIDENCE`, or `BLOCK_UNAUTHORIZED`. An action is scored by its professional appropriateness and authorization, independent of the narrative fluency of the accompanying explanation. Sensitive actions (signing final audit reports, changing ERP master data, modifying control-owner attestations) must remain prohibited to agents.

### 4.3 Example CAM × ICFR test case

An issuer's contract ledger suggests $9.0 million of services revenue, while underlying delivery evidence supports only $6.75 million before year-end. Management asserts that an automated ERP cutoff control was effective, yet a dated access log records an administrator override with no retest. A draft CAM describes complex revenue judgments but provides only generic audit responses. The agent must: (i) reconcile the **$2.25 million potential overstatement under the stipulated facts**, (ii) seek signed delivery and control-test evidence, (iii) distinguish revenue misstatement risk from ICFR deficiency severity, (iv) evaluate whether the CAM communication meets the elements of AS 3101 without inferring unseen audit workpapers, and (v) escalate rather than autonomously conclude fraud or sign an opinion. The numerical outcome is conditional on the synthetic facts; actual recognition would require contractual and accounting analysis. Success requires a *correct action*, not simply the correct dollar difference.

## 5. Multi-agent architecture and treatment arms

**A0 Closed-book LLM:** no retrieval, no permitted external action.  
**A1 Standard hybrid RAG:** lexical/vector search over frozen sources; one answer.  
**A2 Tool-using single agent:** retrieval, calculator and sandbox actions with logs.  
**A3 GraphRAG:** relationship-aware evidence routing, one agent and matched tools.  
**A4 Specialist multi-agent RAG:** CAM, ICFR, fraud, numerical, standard-version and coordination agents, but no independent verifier.  
**A5 Verifier-gated multi-agent RAG:** A4 plus independent contradiction check, an evidence-passport ledger, explicit least-privilege action permissions, and mandatory human sign-off on high-risk transitions.

To identify architecture effects, freeze the base model version and use the same admissible corpus, parser, embedding model, retrieval budget, number of attempted tool calls, maximum tokens, and run seeds where feasible. Because specialized methods have intrinsically different operations, report both fixed-budget performance and unconstrained best-effort performance with token, latency and expense accounting. Randomize arm execution order within cases; isolate immutable source snapshots; avoid feeding answer keys to the retriever. An **oracle retrieval condition** (gold evidence supplied) separates source-retrieval failure from downstream reasoning failure.

The central **evidence passport** should preserve `{claim_id, source_doc_id, accession, page_or_section, quotation_or_hash, source_timestamp, valid_from, valid_to, jurisdiction, reviewer, tool_trace_id, action_authority}`. A proposed conclusion with missing required fields can generate a draft but cannot transition to `CLOSE_WITH_EVIDENCE`.

## 6. Measures, estimands, and statistical design

### 6.1 Primary and secondary outcomes

The **primary outcome** is *Authorized Evidence-Grounded Completion* (AEGC): one if the system reaches the gold-adjudicated next action with sufficient cited evidence and within its permissions, zero otherwise. Critically, a model that confidently recommends closing an unresolved material control issue scores zero. For cases where escalation is the correct conclusion, a correctly justified escalation scores one. AEGC is not the same as willingness to provide any answer.

Secondary measures are: substantive conclusion score (0–2); standards application score (0–2); citation validity and clause-level provenance score (0–2); numerical reconciliation (0–2); uncertainty/conflict handling (0–2); unauthorized-action incidence (binary); justified-abstention precision/recall; evidence retrieval precision@k and recall@k; unsupported-citation rate; elapsed cost/latency/tokens; human override frequency; and supervisor burden. Provide disagreement rates and blinded double coding by CPA/CIA/CFE subject experts before considering a gold answer final.

### 6.2 Statistical models and inference

For case family *i*, variant *v*, architecture *a* and run *r*, estimate a hierarchical logistic model of AEGC with fixed effects for architecture, contradiction regime, standard-version challenge, their pre-specified interactions, and relevant task controls, plus random effects for source-case family and (where identifiable) issuer. Report marginal probability contrasts with uncertainty, not only odds ratios. Complement with a pre-specified linear probability specification using case-family fixed effects and standard errors clustered by case family, as a diagnostic robustness check. For outcomes involving human raters, include rater terms or adjudicate disagreement before estimation.

For critical unsafe actions, report incidence and Wilson confidence intervals by arm even when event counts are low; avoid claiming zero risk based on zero observed incidents. Adjust across the five main hypotheses using Holm's procedure, distinguish confirmatory from exploratory interactions, and report within-family paired bootstrap confidence intervals. For 112 templates and 3,000 generated variants, **do not** treat 3,000 as independent professional concepts. Use unique case-family counts in power and effective-sample-size calculations. The research design should be preregistered before running competitive model arms.

### 6.3 Planned tables and exhibits (results intentionally blank)

- **Table 1:** replication-source matrix, verified public availability and licensing restrictions (completed in source registry; not experimental results).
- **Table 2:** benchmark composition by credential, CAM/ICFR, case family, standard version and frozen split (descriptive artifact only).
- **Table 3:** independently adjudicated gold-case inter-rater reliability, disagreements, and excluded cases (**not yet available**).
- **Table 4:** arm-by-arm AEGC, evidence scores, escalations, critical failures, latency and tokens (**not yet available**).
- **Table 5:** H1–H5 contrasts and confidence intervals (**not yet available**).
- **Table 6:** oracle retrieval, fixed-token, false-authority, and cross-model ablations (**not yet available**).
- **Figure 1:** EGDA delegation envelope and governance transitions.
- **Figure 2:** evidence and authority processing trace (source → claim → verifier → permitted next action).

## 7. Construct validity, threats, and falsification

**Source sufficiency:** SEC filings are useful for auditing publicly reported assertions but cannot reveal every control test or private audit workpaper. Present these cases as *public-source plausibility and consistency tasks*. **Enforcement-label validity:** Bao et al.'s AAER-informed observations are fraud-related enforcement proxies; misstatements not detected or not enforced can distort sensitivity/specificity estimates. **GAI-proxy validity:** GenScore estimates AI-like text rather than legal proof of AI authorship. **Template dependence:** numerical variants from 112 source templates do not confer 3,000 independent evaluation units. **Temporal leakage:** avoid source filings and professional standards published after the case's evidence cutoff. **Prompt contamination:** any public development release may be known to foundation models; holdout and real-case extensions need private adjudication. **Model dependence:** run multiple model families as a robustness dimension only after freezing the primary architecture experiment.

Pre-specified falsification exercises should include swapped dates that render a standard inapplicable; contradictory authorized/unauthorized source documents; irrelevant-but-salient retrieval passages; intentional prompt injection in the synthetic document; incorrect citation IDs; missing denominators for fraud-alert rates; and counterfeit 'auditor sign-off' tokens. Agents should continue to respect hierarchy of instruction and least-privilege approval policy. Also compare A5 to **verification-only single agent** to distinguish an independent checker effect from genuine multi-agent coordination.

## 8. Scope, ethics, open-science protocol, and submission fit

The proposed contribution to JMIS is a theory and design of delegated organizational assurance rather than an evaluation of professional exams. It demands observable workflow transitions, authorized tool use, provenance and escalation. The field should not confuse professional designation knowledge with licensure or competence to issue assurance opinions. All developed questions are synthetic and cannot be presented as AICPA, CFE, CFA or other organizations' official exam items. The original private gold answer bank, unreleased client data, contract-protected data, and certification materials must remain access controlled. Only license-permitted data and documentation should be public, with source URLs rather than unauthorized copies.

Preserve a **frozen evidence manifest** (URL, access date, upstream commit/DOI, declared license, local SHA-256, extraction unit and exclusion flags). GitHub's public research package may contain the manuscript working draft, case schemas, evaluation scripts, and aggregate tables once verified, but it must never expose unadjudicated holdout answers or documents with confidentiality restrictions. A public preprint is *not* journal acceptance; prior to submission reconfirm JMIS editorial policies governing preprints and generative-AI assistance and apply appropriate disclosure. The optional extended abstract and February 2027 submission deadlines are verified from the journal's July 2026 CFP. No completed tests, causal estimates, accepted paper, or completed replication of an FT50 archive are claimed here.

## 9. Research execution milestones and decision gates

**M1 — Source reproducibility audit:** verify publication versions, download conditions, archive content, and hashes for Bao, GenScore, Law/Shen and Nguyen/Nguyen. Report whether each package runs with current toolchains and what remains proprietary.  
**M2 — Gold-100 evidence validation:** select at least 50–100 distinct CAM/ICFR *scenario families*, ensure two expert reviewers per case, adjudicate each standards clause and next action, and freeze gold/holdout.  
**M3 — Agentic sandbox:** implement six treatment arms, least-privilege API stubs, evidence passports and stable log schema; demonstrate that unauthorized ledger/posting/signature actions fail by construction.  
**M4 — Registered evaluation:** preregister primary estimand, family-level split, error taxonomy, costs and sample-size assumptions.  
**M5 — Experimental runs:** conduct actual foundation-model comparisons, verify rerun integrity and collect costs/latencies; independent research staff should review the held-out outputs.  
**M6 — Publication revision:** replace the results placeholders with actual evidence, revise theory according to supported mechanisms, report nulls and sensitivity analyses, and submit only after authors' approval.

## References

Anderson, M. C., Banker, R. D., & Janakiraman, S. N. (2003). Are selling, general, and administrative costs sticky? *Journal of Accounting Research, 41*(1), 47–63. https://doi.org/10.1111/1475-679X.00095

Ashbaugh-Skaife, H., Collins, D. W., Kinney, W. R., Jr., & LaFond, R. (2009). The effect of SOX internal control deficiencies on firm risk and cost of equity. *Journal of Accounting Research, 47*(1), 1–43. https://doi.org/10.1111/j.1475-679X.2008.00315.x

Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts. *MIS Quarterly, 45*(1), 315–341. https://doi.org/10.25300/MISQ/2021/15882

Bao, Y., Ke, B., Li, B., Yu, Y. J., & Zhang, J. (2020). Detecting accounting fraud in publicly traded U.S. firms using a machine learning approach. *Journal of Accounting Research, 58*(1), 199–235. https://doi.org/10.1111/1475-679X.12292

Blankespoor, E., deHaan, E., & Li, Q. (2026). Generative AI in financial reporting. *Journal of Accounting Research, 64*(3), 1189–1232. https://doi.org/10.1111/1475-679x.70050

Chen, Z., Chen, W., Smiley, C., Shah, S., Borova, I., Langdon, D., Moussa, R., Beane, M., Huang, T.-H., Routledge, B., & Wang, W. Y. (2021). FinQA: A dataset of numerical reasoning over financial data. *Proceedings of EMNLP 2021*, 3697–3711. https://doi.org/10.18653/v1/2021.emnlp-main.300

Ciconte, W. A., Rozario, A. M., & Urcan, O. (2026). Using AI to identify exogenous shocks and conduct archival accounting research. *Review of Accounting Studies*. https://doi.org/10.1007/s11142-026-09967-y

Dennis, A. R., Lakhiwal, A., & Sachdeva, A. (2023). AI agents as team members: Effects on satisfaction, conflict, trustworthiness, and willingness to work with. *Journal of Management Information Systems, 40*(2), 307–337. https://doi.org/10.1080/07421222.2023.2196773

Doyle, J. T., Ge, W., & McVay, S. (2007). Determinants of weaknesses in internal control over financial reporting. *Journal of Accounting and Economics, 44*(1–2), 193–223. https://doi.org/10.1016/j.jacceco.2006.10.003

Eulerich, M., Sanatizadeh, A., Vakilzadeh, H., & Wood, D. A. (2024). Is it all hype? ChatGPT's performance and disruptive potential in the accounting and auditing industries. *Review of Accounting Studies, 29*, 2318–2349. https://doi.org/10.1007/s11142-024-09833-9

Griffith, E. E., Rousseau, L. M., & Zehms, K. M. (2026). Why do critical audit matters lack teeth? Insights from auditors' implementation experiences. *Review of Accounting Studies*. https://doi.org/10.1007/s11142-026-09938-3

Islam, P., Kannappan, A., Kiela, D., Qian, R., Scherrer, N., & Vidgen, B. (2023). FinanceBench: A new benchmark for financial question answering. *arXiv:2311.11944*. https://arxiv.org/abs/2311.11944

Law, K. K. F., & Shen, M. (2025). How does artificial intelligence shape audit firms? *Management Science, 71*(5), 3641–3666. https://doi.org/10.1287/mnsc.2022.04040

Nguyen, M., & Nguyen, M. (2026). p-Hacking and publication bias in design-based causal studies in information systems. *Information Systems Research*. https://doi.org/10.1287/isre.2024.1365

Queiroz, M., Anand, A., & Baird, A. (2024). Manager appraisal of artificial intelligence investments. *Journal of Management Information Systems, 41*(3), 682–707. https://doi.org/10.1080/07421222.2024.2376383

Zhu, F., Lei, W., Huang, Y., Wang, C., Zhang, S., Lv, J., Feng, F., & Chua, T.-S. (2021). TAT-QA: A question answering benchmark on a hybrid of tabular and textual content in finance. *Proceedings of ACL-IJCNLP 2021*, 3277–3287. https://doi.org/10.18653/v1/2021.acl-long.254

**End of V2 draft — theoretical hypotheses and empirical outcomes are untested.**
