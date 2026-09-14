# Changelog

## Big Four / Industry Partnership Pilot — v0.2.4 target — 2026-09-14
### Executive university–industry pilot layer
- Added `docs/education/BIG4_PARTNERSHIP_PILOT.md` as the executive-facing partnership design for firms, universities, and external reviewers.
- Defined a win–win–win model linking Industry Partner → Educational Proxy Agent → Synthetic Client XYZ Digital Twin → Student professional judgment → governed evaluation → Human Gate → aggregate anonymized partner insight.
- Defined a recommended first pilot of one university course, one industry partner, approximately 20–40 master students, a 4–6 week teaching window, three synthetic Digital Twin cases, one Educational Proxy Agent, instructor dashboard, aggregate partner dashboard, and pre/post learning evaluation.
- Reaffirmed the ten-metric student/professional evaluation framework: RPA, AA, EG, PS, DS, DIST, AIV, CER, HOR, and ESC.
- Added default aggregate/anonymized partner reporting, with individual student disclosure for recruitment only after explicit consent and appropriate institutional/privacy approval.
- Added explicit success criteria covering reproducibility, agent/evidence traceability, learning outcomes, Human Gate enforcement, privacy-safe reporting, data-leakage prevention, limitations/failure documentation, instructor usability, student usability, and partner value without proprietary-system disclosure.
- Linked the partnership design to Student Pilot 001 and Student Pilot 002 — Microsoft Agent Edition.
- Updated `docs/education/CURRENT_STUDENT_AGENT_ACADEMY_STATE.md` so the Big Four / industry pilot is part of the canonical education-state checkpoint.
- Reaffirmed that this is a v0.2.4 target design and does not imply an existing Big Four partnership, Microsoft certification, marketplace approval, or validated recruitment instrument.

## Prototype 004 real-provider harness — 2026-09-14
### Google Gemini + Microsoft Foundry credential-gated execution
- Implemented real-provider adapters for Google Gemini using `google-genai` and Microsoft Foundry using `azure-ai-inference`.
- Added one common provider runner for single-agent, sequential-agent, and governed multi-agent execution against the same frozen Revenue benchmark.
- Withheld frozen gold labels from provider prompts and preserved separate case/gold hashes for reproducibility.
- Added evidence-ID validation, hallucinated-evidence detection, provider/model metadata capture, Evidence Passport™, Professional Decision DAG™, and mandatory Human Gate enforcement.
- Added provider contract tests covering gold withholding, multi-call orchestration, critic/supervisor ordering, evidence validation, and Human Gate protection.
- Extended GitHub Actions so Gemini and Microsoft Foundry jobs run only when required credentials are configured; otherwise the workflow records `NOT_EXECUTED_PROVIDER_REQUIRED` rather than fabricating model results.
- Required provider result artifacts to preserve `PENDING_HUMAN_APPROVAL` and prohibited superiority claims before cross-provider replication and human review.
- Added `PROTOTYPE_004_PROVIDER_EXECUTION.md` as the canonical provider-execution checkpoint.
- Created a synchronized Google Drive mirror folder and uploaded a frozen Prototype 004 archive ZIP plus readable checkpoint.
- Preserved the validated public software release at v0.2.3; Prototype 004 remains the next empirical execution milestone until credential-gated provider jobs complete and pass review.

## FT50 / AJG 4* Scientific Replication Arena — v0.2.4 target — 2026-09-14
### External top-journal reproducibility and methodological benchmark layer
- Added `benchmarks/ft50_abs4/README.md` as the public entry point for external FT50/AJG 4* benchmark integration.
- Added `benchmarks/ft50_abs4/registry.json` with initial Management Science, Review of Financial Studies, Journal of Financial Economics, and Journal of Finance benchmark families.
- Added `benchmarks/ft50_abs4/BENCHMARK_PROTOCOL.md` defining source verification, exact Git commit pinning, environment reconstruction, original-result replication, clean-room reproduction, robustness, falsification, temporal/OOS validation, cross-dataset/Digital Twin tests, Chain-of-Evidence, and Human Gate.
- Added `benchmarks/ft50_abs4/validate_registry.py` for machine-readable registry validation.
- Added `tests/SCIENTIFIC_REPLICATION_ARENA.md` as the NAAIL Scientific Replication Arena™ test contract.
- Added `external/FT50_ABS4_SOURCE_POLICY.md` so third-party repositories remain external sources with their original rights/licenses unless separately permitted.
- Extended `EVALUATION_STANDARD.md` with formal Layer 7 — FT50 / AJG 4* external benchmark tests.
- Updated `README.md` and `CURRENT_PROJECT_STATE.md` so the benchmark layer is visible in the canonical public architecture and current-state checkpoint.
- Preserved v0.2.3 as the validated executable release; the replication arena is a v0.2.4 research-testing capability until external source commits are pinned, environments reconstructed, and benchmark runs executed and reviewed.
- Explicitly prohibited treating journal prestige, statistical significance, or benchmark registration as proof of reproducibility, identification validity, or scientific truth.

## Student Pilot 002 — Microsoft Agent Edition — v0.2.4 target — 2026-09-14
### Microsoft-connected university–industry Digital Twin roadmap
- Added `Student_Pilot_002_Microsoft/README.md` as the next education-facing executable roadmap.
- Defined a Microsoft 365 / Copilot-compatible agent surface connected through a NAAIL adapter boundary to the Educational Proxy Agent and Synthetic Client XYZ Digital Twin.
- Preserved the ten-metric evaluation framework: RPA, AA, EG, PS, DS, DIST, AIV, CER, HOR, and ESC.
- Defined separate Student, Instructor, and Industry-Partner views, with aggregate/anonymized partner reporting by default.
- Required explicit separation between academic grading and recruitment use; individual student disclosure requires explicit consent plus institutional/privacy approval.
- Reused the frozen Student Pilot 001 case family: Revenue Recognition & Cut-off, Goodwill Impairment, and ICFR / Control Deficiency.
- Added release gates for real Microsoft-compatible provider identity, frozen evidence, privacy/consent, regression/evaluation tests, Human Gate, and no confidential client/firm data.
- Updated `marketplace/microsoft/README.md` so the Microsoft distribution package and Student Agent Academy share the same next milestone.
- Reaffirmed that no Microsoft or Big Four partnership, endorsement, certification, or production-system equivalence is claimed without written authorization.
- Kept the validated software release at v0.2.3; Student Pilot 002 remains part of the v0.2.4 target until a real provider-backed execution is completed and validated.

## Student Agent Academy + Digital Twin Education — v0.2.4 target — 2026-09-14
### University–industry AI audit learning layer
- Added the **NAAIL Big Four Student Agent Academy™** as a public university–industry education and talent-readiness model.
- Added a governed **Educational Proxy Agent** concept so firms can contribute learning objectives, challenge briefs, synthetic scenarios, guest sessions, or approved proxy-agent specifications without exposing proprietary production systems or confidential client data.
- Added the **NAAIL Digital Twin Student Simulation™** specification using the existing Client XYZ three-case family: Revenue Recognition & Cut-off, Goodwill Impairment, and ICFR / Control Deficiency.
- Added controlled teaching/research conditions: no AI, general AI assistant, single educational audit agent, sequential specialist agents, and governed multi-agent + Human Gate.
- Added student decision states: `ACCEPT_AGENT`, `MODIFY_AGENT`, `REJECT_AGENT`, `REQUEST_MORE_EVIDENCE`, and `ESCALATE_TO_HUMAN`.
- Extended evaluation beyond RPA, AA, EG, PS, DS, and DIST with education-specific constructs: **AIV** (AI Verification), **CER** (Contradictory Evidence Recognition), **HOR** (Human Override Reasoning), and **ESC** (Escalation Judgment).
- Added a privacy-governed **Student Learning Twin** for event traces, evidence use, revisions, escalation choices, and educational feedback.
- Added default aggregate/anonymized partner reporting and explicit separation of academic grading from recruitment pathways.
- Prohibited automatic employment decisions from NAAIL student scores and prohibited individual-level partner disclosure without explicit student consent and appropriate institutional/privacy approval.
- Updated `README.md`, `ARCHITECTURE.md`, and `AGENTS.md` so the education layer is a first-class NAAIL capability.
- Preserved the current validated executable version at **v0.2.3**; the Student Agent Academy remains part of the **v0.2.4 target** until institutional controls, provider adapters, and pilot validation are completed.

## Marketplace Edition scaffold — 2026-09-14
### OpenAI + Google + Microsoft distribution preparation
- Added `marketplace/` as a provider-neutral distribution layer without exposing the private NAAIL scientific core.
- Added provider packages for OpenAI ChatGPT Apps SDK/MCP, Google Cloud Marketplace/Gemini Enterprise, and Microsoft Marketplace/Microsoft 365 Copilot.
- Added a provider-neutral public API contract for research-question framing, competing hypotheses, evidence metadata, empirical design, reproducible analysis, robustness/falsification, Chain-of-Evidence, Human Gate, and research-artifact export.
- Added common marketplace submission gates covering production service, privacy/security, rights/licensing, provider-specific review, commercial/IP review, and Human Gate authorization.
- Added public security/data-handling policy plus draft privacy policy, draft terms of use, support policy, and marketplace listing metadata.
- Preserved a strict public/private boundary: proprietary orchestration, unpublished prompts, provider credentials, private gold labels, licensed/restricted data, patent-candidate mechanisms, and commercial logic remain outside the public marketplace package.
- Marketplace documents explicitly state that NAAIL has not yet been submitted, approved, certified, endorsed, or listed by OpenAI, Google, or Microsoft.
- This scaffold is a **v0.2.4 target** and does not replace the validated v0.2.3 executable software release until production endpoints and provider-specific validations are completed.

## v0.2.3 — 2026-09-14
### Audit Digital Twin Prototype 003
- Extended the frozen synthetic benchmark from Revenue Recognition to three domains: Revenue Recognition & Cut-off, Goodwill Impairment, and ICFR Deficiency.
- Added a common provider-neutral comparison harness for deterministic baseline, single-agent AI, sequential-agent AI, and governed multi-agent AI.
- Executed only the deterministic control condition; unconfigured AI modes are explicitly recorded as `NOT_EXECUTED_PROVIDER_REQUIRED` rather than simulated or reported as empirical results.
- Preserved Evidence Passport™, Professional Decision DAG™, RPA, AA, EG, PS, DS, DIST, precision/recall, false-positive/false-negative tracking, and mandatory Human Gate.
- Added seven validated regression/scientific-integrity tests in the private R&D master.
- Frozen deterministic synthetic outcomes: Revenue exceptions `TX-002`/`TX-003` with EUR 190,000 proposed adjustment; Goodwill exceptions `GW-DR`/`GW-MAR` with EUR 440,000 synthetic estimated adjustment; ICFR deficiencies `CTRL-JE-02`/`CTRL-IT-03` with EUR 530,000 synthetic estimated exposure.
- Updated VERSION, `CITATION.cff`, BibTeX, CodeMeta, README, public prototype status, research record, and portfolio index to reflect Prototype 003.
- Kept detailed orchestration, private benchmark extensions, provider adapters, prompts/specifications, and patent-sensitive implementation private pending IP review.

## Daily activity — 2026-09-14
- Published the full [Daily Research & Engineering Activity — 14 September 2026](./docs/activity/2026-09-14.md), covering architecture, scientific discovery, Audit Digital Twin development, evaluation, data-integration scope, education, GitHub professionalization, citation/DOI readiness, IP governance, and next implementation priorities.

## Architecture snapshot V2026.3 — 2026-09-14
### Google + Microsoft Multi-Agent Digital Twin Scientific Discovery Architecture
- Added a frozen next-architecture snapshot without replacing the validated public software release.
- Added Google ADK / Antigravity-style development plus Microsoft Agent Framework as a vendor-neutral dual-stack reference.
- Added A2A + MCP interoperability and explicit GraphRAG + NAAIL Digital Twin integration.
- Added Co-Scientist-style hypothesis generation, critique and ranking.
- Added ERA-style conversion of hypotheses into reproducible empirical tests with explicit data provenance, variables, code and evaluation metrics.
- Added AlphaEvolve-style evaluator-guided model, algorithm, measure, prompt and specification search.
- Added AlphaFold/DeepMind-inspired latent-structure reasoning and Computational Discovery.
- Added dedicated Critic, Defender, Replicator and Falsifier roles for AI-to-AI adversarial review.
- Added Science One-style Chain-of-Evidence and Professional Decision DAG™ governance from evidence to claim.
- Added Research Study Twin, ResearchHypothesis, EmpiricalDesign and ReplicationRun entities to the Digital Twin domain model.
- Added rights/licensing gate before evidence enters the Digital Twin.
- Added mandatory temporal/out-of-sample validation, clean-room replication and Human Gate before professional or scientific claims.
- Added `versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md` and linked it from the public README and architecture.

## v0.2.2 — 2026-09-14
### Audit Digital Twin Prototype 002
- Advanced the public prototype status from Prototype 001 to Prototype 002.
- Added explicit Materiality and Risk agent roles to the private executable baseline.
- Added Evidence Passport™ with reproducible source hashing, evidence IDs, assertions, adapter identity and limitations.
- Added Professional Decision DAG™ with dependency-aware nodes and a mandatory Human Gate.
- Added a provider-neutral model-adapter contract.
- Added five regression tests covering frozen exceptions, materiality comparison, evidence hashing, Human Gate termination and baseline error rates.
- Preserved the frozen synthetic Client XYZ revenue-recognition benchmark and public/private IP boundary.

## v0.2.1 — 2026-09-14
### Governance and engineering hardening
- Added public seven-layer reference architecture.
- Added governed Agent Card/risk-class standard.
- Added eval-first benchmark standard with RPA, AA, EG, PS, DS and DIST.
- Added security/privacy/governance standard.
- Added staged product/research roadmap.
- Added public-release checklist.
- Added contribution and contributor-IP policy.
- Added Microsoft/Google/OpenAI public engineering benchmark.
- Added `CITATION.bib`, `codemeta.json`, `AUTHORS.md`, and version marker.

## v0.2.0 — 2026-09-14
### Evidence-enabled public research release
- Business-school scope: Accounting, Auditing, Finance, Economics.
- Audit Digital Twin with 37-role architecture.
- FT50/AJG evidence architecture.
- Synthetic Firm Alpha–Delta and Client XYZ concepts.
- Non-commercial research/education licensing and IP notices.
- Initial machine-readable citation metadata.