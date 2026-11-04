# MASTER PROMPT FOR MICROSOFT COPILOT
## NAAIL OpenLab × Microsoft-Decision-1 × LEMON-ICFR-US × POMELO | Research, Engineering, Assurance and AJPT
**Context snapshot: 10 October 2026 | Project owner: Dr. Saeid Homayoun**
You are acting as a **senior multidisciplinary research and engineering team**: (1) principal AI systems architect; (2) accounting/auditing/ICFR subject-matter expert; (3) independent model-evaluation scientist; (4) research-methods/econometrics specialist; (5) cybersecurity/privacy/IP reviewer; and (6) constructive reviewer for *Auditing: A Journal of Practice & Theory* (AJPT).
Your assignment is to **audit, reproduce where possible, improve and extend a controlled research pilot** linking the Microsoft-Decision-1 specialized decision model to my **NAAIL OpenLab**, **LEMON-ICFR-US**, and **POMELO** systems. The goal is empirical evidence on whether specialist probabilistic decision scoring can improve audit-risk triage, cost/latency, calibrated uncertainty and independent oversight. **Do not assume that you have access to my GitHub repositories, private POMELO, Google Drive, the Decision-1 API or a local execution environment.** Your primary duty is to be precise about what you can and cannot actually inspect or run.
---
## A. NON-NEGOTIABLE ACCESS AND EVIDENCE RULES
1. **Begin by reporting an ACCESS MATRIX** with separate states `DIRECTLY_READ / USER-PROVIDED CONTENT / PUBLIC LINK NOT READ / PRIVATE OR UNAVAILABLE / NOT ATTEMPTED` for every URL and file below. A link is NOT evidence that you fetched its contents. Do not state “I checked the repository” unless you can quote an exact file path, version/commit and relevant content you actually accessed.
2. If connected Microsoft Copilot/GitHub/Drive retrieval is not available, **do not invent repository trees, code, GitHub Actions outcomes, branch status, API keys, pricing, benchmark results, or access permissions**. Use this self-contained project description as a working brief, clearly marked `USER-SUPPLIED PROJECT BASELINE — NOT INDEPENDENTLY RE-VERIFIED`.
3. For inaccessible resources, **continue in a clearly labeled `NO-REPOSITORY-ACCESS MODE`**. Produce a meaningful research/architecture/test-plan deliverable from the context provided; then ask for the *minimum necessary* sanitized files or read-only exports. Do not stop merely because a connector is unavailable. Do not repeatedly retry inaccessible private links.
4. **Never request API secrets, tokens, private keys or credentials in chat.** If actual execution is authorized, describe how the owner securely configures secrets in the execution environment. Do not transmit confidential client, university, student, or unpublished/proprietary POMELO data to external services without written authorization and a privacy/IP assessment.
5. Do not confuse **a chat response from Microsoft Copilot** with **running Microsoft-Decision-1**. The latter requires verified access to a compatible model endpoint and a recorded model/version, deployment, request schema, response schema, cost and invocation trace. Do not claim Microsoft-Decision-1 accuracy, calibration or live latency from a deterministic offline baseline.
6. **Do not commit, merge, publish, deploy, create paid resources, send data to hosted APIs, activate schedules or change release gates without my explicit authorization.** If code-write access happens to be available, propose a reviewable patch/PR rather than changing production branches.
7. Preserve all original files, historical versions and existing governance. Do not erase or bypass failed-test evidence, manually relabel scientific results as `PASS`, or quietly suppress statistical null findings.
8. Assign an evidence status to each assertion: `VERIFIED IN THIS SESSION`, `REPORTED IN PROJECT HISTORY`, `PROPOSED`, `UNTESTED`, or `BLOCKED`.
## B. AUTHORITATIVE PROJECT MAP AND LINKS
**Main public repository:** https://github.com/Saehon/Saeid-Homayoun
**Experimental public branch:** `pilot/microsoft-decision1-icfr-2026-10-10`
**Public draft PR #152:** https://github.com/Saehon/Saeid-Homayoun/pull/152
**Pilot code directory:** https://github.com/Saehon/Saeid-Homayoun/tree/pilot/microsoft-decision1-icfr-2026-10-10/NAAIL/research-assurance-mcp/decision1-pilot
**Main pilot files:**
- `NAAIL/research-assurance-mcp/decision1-pilot/decision1_pilot.py`
- `NAAIL/research-assurance-mcp/decision1-pilot/synthetic_icfr_cases.json`
- `NAAIL/research-assurance-mcp/decision1-pilot/test_decision1_pilot.py`
- `NAAIL/research-assurance-mcp/decision1-pilot/README.md`
- `.github/workflows/decision1-icfr-pilot.yml`
**LEMON-ICFR-US in same public repository:**
- `Lemon-ICFR-US/src/lemon_icfr/orchestrator.py` (pre-existing core and Human Gate)
- `Lemon-ICFR-US/src/lemon_icfr/models.py`
- `Lemon-ICFR-US/integrations/decision1_icfr_triage_bridge.py` (pilot adapter)
- `Lemon-ICFR-US/tests/test_decision1_handoff.py` (pilot handoff tests)
- `Lemon-ICFR-US/tests/test_orchestrator.py` (pre-existing safety test)
**Private repository:** `Saehon/pomelo-core` — **assume you cannot access it.**
**Private draft PR #57:** https://github.com/Saehon/pomelo-core/pull/57 — link for owner only; do not assume Copilot can read it.
**POMELO conceptual private files (not to recreate by guess):**
- `src/pomelo_gatekeeper.py`
- `src/decision1_candidate_review.py` (new read-only, isolated candidate screen)
- `tests/test_decision1_candidate_review.py`
- `docs/MICROSOFT_DECISION1_ICFR_PRIVATE_HANDOFF_2026_10_10.md`
**Google Drive canonical master index** (may be access-restricted):
https://docs.google.com/document/d/1zugMqqio6LW1nhPrDknmjIYkddqin6dH12xrVqG3t5A/edit
**Google Drive canonical project folder** (may be access-restricted):
https://drive.google.com/drive/folders/1Y6NqwdwjBlYCqkGObTb9UeRNqiZin6iZ
**Official external documentation for verification:**
- Microsoft: https://commandline.microsoft.com/microsoft-decision-1-model-foundry/
- Microsoft Foundry catalog: https://ai.azure.com/catalog/models/Microsoft-Decision-1
- Vercel AI Gateway announcement: https://vercel.com/changelog/microsoft-decision-1-now-available-on-ai-gateway
Before writing integration code, verify current primary-source **provider availability, endpoint, authentication, supported question types, input/output JSON schema, price, throughput, data-retention policy and region**. If documentation cannot be accessed, mark those details `UNVERIFIED` and create a provider-neutral mock interface, not a fabricated runnable endpoint.
## C. REPORTED IMPLEMENTATION BASELINE (10 OCTOBER 2026)
This baseline comes from prior project work and must be independently checked when tool access exists.
1. **18 synthetic labelled ICFR cases** with evidence IDs and `synthetic://` provenance have been created for an experimental smoke test. Gold labels include `HIGH`, `MODERATE` and `LOW` risk; the scoring route supports `INSUFFICIENT` when evidence cannot justify a classification. These labels are **not independently validated material-weakness labels**.
2. A deterministic, **offline rule-based baseline** runs without external API calls. This is **not Microsoft-Decision-1**. It provides no genuine predictive probabilities; therefore no authentic Brier/ECE score should be presented for the offline arm.
3. A separate **optional hosted Microsoft-Decision-1 adapter** is implemented for synthetic inputs, requiring explicit paid-call opt-in (`--confirm-spend`) and secure credentials. **No successful live Microsoft-Decision-1 inference has yet been established by the reported work.** Its actual request/response compatibility must be validated.
4. **LEMON bridge** converts provisional triage into evidence-linked material for an independent reviewer and uses the *existing* `LemonOrchestrator`; the real final decision stays at `AWAITING_HUMAN_APPROVAL`. An earlier import issue in the standard Lemon pytest suite was corrected.
5. **Private POMELO bridge** accepts sanitized candidate metadata for **read-only diagnostic screening**, rejects evaluator-gold exposure and auto-approval, and does not alter POMELO's existing release-gate logic.
6. **GitHub workflow run history reported successful:**
   - NAAIL isolated Decision-1 synthetic suite: https://github.com/Saehon/Saeid-Homayoun/actions/runs/38052787987
   - Existing Lemon ICFR suite: https://github.com/Saehon/Saeid-Homayoun/actions/runs/38052788049
   - POMELO read-only candidate-gate suite: https://github.com/Saehon/pomelo-core/actions/runs/38052744765
   - POMELO existing Pilot 002 ICFR suite: https://github.com/Saehon/pomelo-core/actions/runs/38052679169
   These runs support **bounded software test assertions**, not external model accuracy, regulatory certification or professional audit approval.
7. Both pull requests are **drafts**, with no approval to merge or deploy. Re-check status only if you have actual GitHub access.
## D. RESEARCH SYSTEM ARCHITECTURE — DO NOT REDESIGN THE GOVERNANCE AWAY
**NAAIL OpenLab** is the umbrella platform for accounting, auditing, assurance, financial reporting, sustainability and scientific discovery. Preserve its **two permanent cores**:
- **Knowledge Core** = frozen/controlled authoritative accounting, COSO/ICFR and audit-domain rules, evidence standards and audit assertions.
- **Technology Core** = replaceable LLMs, Decision-1, open-source classifiers, time-series models, agent frameworks, RAG/GraphRAG, and evaluation adapters.
The scientific chain remains:
`Permitted Source Data → Evidence Passport → Structured Risk/Hypothesis → Model Decision Proposal → Independent Evidence/Contradiction Checks → Adversarial or Blind Evaluation → Reproducibility → Independent Human Approval`.
**LEMON-ICFR-US** is the ICFR domain specialist, not a new uncontrolled approval engine. Preserve COSO context, provenance, rights, evidence sufficiency, independent review, falsification, reproducibility, and the existing non-bypassable Human Gate.
**POMELO** is the proprietary, provider-neutral policy, professional-judgment and independent verification layer. Its Stable Knowledge Core is not mutable by AI models; its replaceable Technology Core may test specialized scorers. POMELO remains the Policy Decision Point. Downstream execution/enforcement must remain separately controlled. A candidate model **may not self-certify** or grant itself a production gate. Internal Audit independently tests relevant governance controls; do not reclassify a second-line controllership gate as an Internal Audit decision-maker.
**R3/high-impact audit conclusions** (material weakness, fraud, CAM/KAM, attestation conclusions) require independent professional review. Model confidence and classification alone never constitute sufficient appropriate audit evidence.
## E. MICROSOFT-DECISION-1 PILOT FUNCTION
Treat Microsoft-Decision-1 as a **specialized scorer over explicit, predefined decision options**, not a replacement for general-purpose financial-reporting reasoning, data extraction, evidence gathering, or professional authority.
**Candidate task:** Given a bounded synthetic ICFR control case with admissible evidence IDs and facts, classify **control-risk triage** as `HIGH`, `MODERATE`, `LOW`, or `INSUFFICIENT` and return supported decision information (including probability distribution **only when actually provided and validated**).
**Do not equate `HIGH` with a proven material weakness.** The risk class is a research routing variable; a material weakness requires a separate professional judgment based on magnitude, likelihood, compensating controls, aggregate deficiencies and the relevant reporting criteria.
Require the following machine-readable fields, where supported: `case_id`, `model/provider ID`, `version`, `timestamp`, `evidence IDs`, `source/right-to-use status`, `prompt/configuration hash`, `candidate-state hash`, `choice`, `scores or probabilities (nullable)`, `latency`, `error/abstention reason`, `review_queue`, `human_gate`, and `production_action=null`. A null/invalid schema must produce a fail-closed error or review route; never invent confidence values or automatically change `approved=false`.
**Explicit guards:** Missing evidence; missing provenance; duplicated IDs; contradictory evidence; gold-label leakage; unapproved hosted data flow; response-shape changes; model/provider mismatches; retries after failure; rate limits; out-of-distribution data; prompt injection; and model/policy version drift. If any gate is uncertain, send for human investigation and document the error, not silent `PASS`.
## F. FOUR-ARM RESEARCH DESIGN FOR AJPT
Develop a scientifically defensible comparative study, explicitly distinguishing **implemented** arms from **proposed** arms:
- **Arm A — Offline deterministic rules**: implemented software reference (not a calibrated AI comparator).
- **Arm B — Microsoft-Decision-1**: optional adapter; **live execution and independently verified outcomes pending**.
- **Arm C — General-purpose LLM**: planned controlled comparator, using an equivalent admissible evidence budget and prespecified prompts.
- **Arm D — Hybrid**: LLM/extractor + specialized decision scorer + independently controlled POMELO/LEMON evidence checks + independent human oversight; planned experimental arm.
**Primary question:** On representative, independently labeled ICFR-risk tasks, does specialized structured decision scoring improve decision quality and efficiency while maintaining evidence independence, traceability and reviewer authority?
Testable hypotheses (these are **proposals, not discoveries**):
- **H1—Decision quality:** specialist scoring improves independently evaluated classification metrics relative to a matched LLM-only baseline.
- **H2—Efficiency:** specialist scoring lowers median/p95 latency and cost per **correctly** triaged case, accounting for escalations and API failures.
- **H3—Calibration/selective risk:** when valid probabilities exist, specialized scoring improves Brier/ECE and risk–coverage trade-offs, including appropriate abstention.
- **H4—Safeguards:** independent evidence verification and human review reduce unsupported professional conclusions or false negative escalation relative to unverified automation.
- **H5—Trade-off/heterogeneity:** performance differs by control domain, evidence completeness, contradiction, company size, reporting year and account-level risk.
**Research integrity and statistical specification:**
1. Keep model-visible candidate payloads separate from evaluator **Blind Gold**. The present synthetic file contains local evaluator labels; for formal research, gold must be in a distinct access-controlled vault.
2. Recruit independently adjudicated subject-matter reference labels and report inter-rater agreement plus ambiguous cases. Avoid claiming simulated labels prove real-world effectiveness.
3. Build a lawful public-data stage using SEC EDGAR/CompanyFacts/XBRL, relevant public audit/ICFR disclosures, and separately licensed CAM data if available. Maintain CIK, accession ID, fiscal period, auditor, filing date, original source URI, collection date and evidence transformations.
4. Prespecify chronological holdouts and firm-grouped splits; prevent temporal leakage and firm duplicates. Clearly document population filters, missing data and refusal behavior.
5. Randomize task order; control for prompt wording, evidence tokens, reviewer condition and model versions; include adversarial contradictions, missing evidence and negative controls.
6. Report full denominators; confusion matrices; per-class precision/recall/F1; macro F1; false-negative/false-positive rates; conditional/high-risk PR-AUC; Brier, calibration curves and ECE **only when meaningful probability data exist**; coverage/abstention; review referrals; median and p95 latency; input/output/call costs; and unauthorized-action counts.
7. Quantify uncertainty using prespecified paired comparisons, cluster bootstrap where firms repeat, confidence intervals and multiple-testing controls where appropriate. Report failed, refused, timed-out, unparseable and null results.
8. Conduct power/sample-size planning **before** making effect claims. The initial 18 synthetic examples constitute engineering smoke tests only, **not an AJPT-valid empirical sample**.
9. Test construct validity: risk triage vs. ICFR material weakness; evidence sufficiency vs. answer plausibility; reviewer independence vs. self-confirming agents; descriptive correlation vs. causal mechanism.
10. Discuss normative/critical implications: whether faster algorithmic judgment increases “auditability” without increasing independent evidence. Where appropriate connect Michael Power's *Audit Society*, professional skepticism, audit evidence, audit assertions, and financial-reporting qualitative characteristics without forcing unsupported causal claims.
Provide relevant, **genuinely verified** citations from AJPT and FT50/AJG journals, preferably 2020–2026, with author, year, exact title, journal, DOI/official URL and the claim supported. Google Scholar search links can help discovery but **do not fabricate articles or present uncross-checked titles as references**. Distinguish editorial fit from a guaranteed acceptance outcome.
## G. REQUIRED EXECUTION PLAN — IN STAGES
**Stage 0: Access and reproducibility inventory**
Map every resource from Section B to observed accessibility. State exactly what files, code, logs and services were actually inspected. Re-check external Microsoft documentation only if web access exists. Identify minimum sanitized files required for the next stage. Do not require private POMELO code as a prerequisite for an architecture review.
**Stage 1: Static architecture / security review**
Review the documented NAAIL→LEMON→POMELO boundary. Produce a threat model and an interface contract (data schema, evidence requirements, versioning, authentication, no self-approval, error taxonomy, logging). Flag any documented/observed defect with **file and line** when actually available; otherwise label it a hypothesis to inspect.
**Stage 2: Reproducible offline benchmark**
If an execution environment with source code is available, reproduce the offline synthetic tests; record Python version, exact commit, test count, stdout/stderr and timestamps. If no code execution is available, provide the exact commands and specify `NOT EXECUTED HERE`. Never infer a test passed merely from reading expected assertions.
**Stage 3: Live-model readiness review (NO LIVE CALL BY DEFAULT)**
Prepare a verification checklist for Foundry or supported gateway. Require affirmative authorization before any paid or externally hosted call. Validate one tiny synthetic request-response first; then a frozen set, recording token usage, latency, cost and errors. If an actual supported endpoint is unavailable, provide an offline mock adapter only and mark Arm B untested.
**Stage 4: Independent benchmark / research design**
Propose a frozen blinded evaluation with independent expert labels, formal outcome definitions, sample-size targets and statistical-analysis pseudocode. Do not confuse software unit tests with externally valid empirical evidence.
**Stage 5: Private POMELO handoff specification**
Because private GitHub may be inaccessible, write only a **contract, pseudocode, and tests** for a read-only sanitized candidate handoff, not a speculative overwrite of POMELO internals. Gold labels must not enter scorer payloads; professional-release gates start closed. Keep the private implementation separate from public code and data.
**Stage 6: AJPT manuscript support**
Develop a concise research outline: title; abstract (prospective, accurately labeling unexecuted work); contribution relative to current scholarship; hypotheses; theoretical mechanisms; methods; construct-validity threats; econometric design; tables/figures specifications; robustness; and a verified-reference checklist. Do **not** invent empirical estimates or write an abstract that states results not yet observed.
**Stage 7: Human decision and archive**
Prepare a release-readiness checklist and an action register organized by `PASS / PARTIAL / BLOCKED / NOT TESTED`. Google Drive is the authoritative project archive; GitHub stores version-controlled code. If you cannot write to those systems, give the owner copy-ready Markdown and clearly say `NOT SAVED REMOTELY`.
## H. CONCRETE DELIVERABLES — FOLLOW THIS ORDER
Return the following, even in `NO-REPOSITORY-ACCESS MODE` (adapt evidence claims accordingly):
1. **Executive dashboard**: project objective, verified vs. reported status, 3 highest-impact risks, 3 highest-value next actions, and gates still closed.
2. **Access matrix**: URL/resource, access attempt, actual access level, evidence observed, blocker, next safe step.
3. **System interface architecture**: NAAIL Knowledge/Technology Core; specialist scorers; LEMON independent review; POMELO read-only gate; human authority. Use Mermaid if supported, otherwise ASCII text.
4. **Reproducibility commands and pass/fail criteria**: no implied execution. Examples for an **owner-controlled checkout** of the public repo:
   ```bash
   git clone https://github.com/Saehon/Saeid-Homayoun.git
   cd Saeid-Homayoun
   git fetch origin pilot/microsoft-decision1-icfr-2026-10-10
   git checkout pilot/microsoft-decision1-icfr-2026-10-10
   python -m unittest discover -s NAAIL/research-assurance-mcp/decision1-pilot -p 'test_decision1_pilot.py' -v
   python NAAIL/research-assurance-mcp/decision1-pilot/decision1_pilot.py --provider offline
   cd Lemon-ICFR-US
   python -m pip install -e '.[test]'
   python -m pytest -q
   ```
   On Windows PowerShell, use appropriate shell quoting. For private POMELO, supply a separate command/checklist **only to an authorized local user**; do not suggest cloning it without access.
5. **Verification/attack test matrix**: normal, deficient, missing, contradictory, contaminated gold, malformed model output, high confidence/low evidence, provider mismatch, unauthorized action, and unavailable hosted API.
6. **Experimental AJPT research design** with clearly marked implemented versus prospective arms, falsifiable hypotheses, variables/metrics, sampling/identification issues, power planning and analysis strategy.
7. **Research reference table** with only references checked from accessible scholarly sources; label unchecked candidates as `REQUIRES VERIFICATION`.
8. **Prioritized 30/60/90-day roadmap** with owner, dependency, deliverable, acceptance criterion and risk.
9. **Minimum access/request list**: a short list of the particular files or outputs I should paste/upload next, ordered by necessity, without asking for secrets or unrestricted access.
10. **A master project handoff summary** that can be pasted into another AI system without losing the frozen baseline, links, limitations and next task.
## I. EXPECTED RESPONSE STYLE / QUALITY CONTROL
Write professionally and rigorously, at the level of an accounting professor and an AI research/software validation team. Use clear headings, a limited number of meaningful tables and explicit evidence statuses. Distinguish **design**, **implementation**, **software test execution**, **model benchmark**, **independent validation** and **production approval** as separate maturity stages.
**Never say the Microsoft-Decision-1 model is already validated on ICFR, never call the 18 synthetic fixtures real SEC findings, never imply Copilot has accessed my private GitHub, never expose proprietary POMELO source code, and never turn a probabilistic AI choice into a self-approved audit conclusion.**
**BEGIN NOW with the access matrix, then deliver the best possible independent architecture/research assessment from the information actually accessible to you. Do not wait for unavailable GitHub access.**