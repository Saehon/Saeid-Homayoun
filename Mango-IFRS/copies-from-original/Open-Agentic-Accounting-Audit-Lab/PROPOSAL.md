# Proposal: Open Agentic Accounting & Audit Lab

## 1. Purpose

This project proposes a provider-neutral experimental platform for studying how agentic AI can support accounting and assurance while remaining **traceable, reproducible, controlled, and human-governed**. Rather than evaluating a foundation model as a black box, the project separates the model from specialist skills, deterministic calculations, evidence provenance, policy controls, cross-model challenge, and human approval.

The intended research domains are:

1. Financial accounting and reporting.
2. External audit and audit evidence.
3. ICFR/internal control and SOX-style control logic.
4. Corporate governance and board/audit-committee evidence.
5. CAM and KAM analysis.
6. IFRS recognition, measurement, presentation and disclosure.
7. ESG/sustainability reporting and assurance.

## 2. Research motivation

FT50 and leading accounting research provides strong motivation for studying AI architecture rather than AI adoption alone. Fedyk et al. (2022, Review of Accounting Studies) associate audit-firm AI investment with improved audit outcomes; Bao et al. (2020, Journal of Accounting Research) and Bertomeu et al. (2021, Review of Accounting Studies) demonstrate the value of machine learning for fraud and misstatement detection; Doyle, Ge, and McVay (2007a, Journal of Accounting & Economics; 2007b, The Accounting Review) show why internal-control quality is economically important; and Management Science research on automation and human–AI collaboration emphasizes task allocation, specialization, and human-centered system design.

Key references:
- Fedyk et al. (2022): https://doi.org/10.1007/s11142-022-09697-x
- Bao et al. (2020): https://doi.org/10.1111/1475-679X.12292
- Bertomeu et al. (2021): https://doi.org/10.1007/s11142-020-09563-8
- Doyle et al. (2007a): https://doi.org/10.1016/j.jacceco.2006.10.003
- Doyle et al. (2007b): https://doi.org/10.2308/accr.2007.82.5.1141
- Chan and Liu (2023): https://doi.org/10.2308/TAR-2020-0121
- Christensen, Hail, and Leuz (2021): https://doi.org/10.1007/s11142-021-09609-5

## 3. Central research question

**When does a provider-neutral, control-gated, evidence-traceable agent architecture outperform a single general-purpose LLM in accounting and auditing, and when is human professional judgment still necessary?**

Sub-questions:
- Does agent specialization improve accuracy and reduce unsupported claims?
- Do deterministic controls reduce unauthorized or numerically incorrect outputs?
- Does cross-model challenge reduce correlated model error?
- Does a human gate create greater value for high-judgment than deterministic tasks?
- How do provider choice, model family, task structure, and jurisdiction interact?
- Which tasks should be automated, augmented, independently replicated, or reserved for human judgment?

## 4. Architecture

### 4.1 Evidence layer
Inputs: PDFs, annual reports, audit reports, XBRL facts, spreadsheets, contracts, board/proxy materials, sustainability reports, synthetic accounting records.

Recommended tools:
- Docling MCP — https://github.com/docling-project/docling-mcp
- SEC EDGAR MCP — https://github.com/stefanoamorelli/sec-edgar-mcp
- SEC EDGAR APIs — https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- ESMA ESEF — https://www.esma.europa.eu/issuer-disclosure/electronic-reporting

### 4.2 Deterministic accounting/audit layer
Recommended components:
- CPA Skills — https://github.com/adoptai/cpa-skills
- FinanceSkills — https://github.com/GAJETOso/financeskills

Target tasks include bank-to-GL reconciliation, trial-balance integrity, three-way matching, sampling, journal-entry screening, cutoff testing, ratio analysis, roll-forwards, and repeatable accounting calculations.

### 4.3 Control and governance layer
- closegate — https://github.com/esploro-group/closegate

Controls include segregation of duties, materiality routing, sensitive-account restrictions, reversibility, escalation, approval envelopes, and replayable audit logs.

### 4.4 Specialist agents
The proposed system has ten bounded agents:
- Financial Accounting Agent
- Audit Testing Agent
- Evidence Agent
- ICFR/Internal Control Agent
- Corporate Governance Agent
- CAM Agent
- KAM Agent
- IFRS Agent
- ESG Agent
- Reviewer Agent

An Orchestrator routes tasks but cannot bypass control gates.

### 4.5 Provider-neutral model layer
Provider families to compare:
- OpenAI GPT/Codex
- Anthropic Claude
- Google Gemini
- Microsoft/Azure-hosted model services
- Kimi/Moonshot
- DeepSeek
- Optional local Ollama models

Recommended adapter:
- LiteLLM — https://github.com/BerriAI/litellm

Recommended orchestration frameworks:
- Google ADK — https://github.com/google/adk-docs
- Microsoft Agent Framework — https://github.com/microsoft/agent-framework

## 5. Three-study design

### Study 1 — United States: 10 cases
Focus: CAM, ICFR, SEC/XBRL, journal-entry testing, governance and audit evidence.

Example task families:
1. Revenue recognition/cutoff.
2. Goodwill impairment.
3. Acquisition accounting.
4. Tax valuation allowance.
5. Inventory valuation.
6. Revenue ICFR.
7. IT access/segregation of duties.
8. Journal-entry anomalies.
9. Financial-statement/XBRL tie-out.
10. CAM entry/exit/persistence.

### Study 2 — Europe: 10 cases
Focus: IFRS, KAM, ESEF/iXBRL, ESRS/ESG.

Example task families:
1. IFRS 15 revenue.
2. IAS 36 impairment.
3. IFRS 9 ECL.
4. IFRS 16 leases.
5. IFRS 3 acquisitions.
6. IAS 37 provisions.
7. ESEF/XBRL validation.
8. KAM persistence/boilerplate.
9. ESRS climate evidence.
10. Double materiality.

### Study 3 — Asia: 10 cases
Focus: KAM, IFRS-aligned reporting, sustainability and governance variation across Hong Kong, Singapore and Japan.

Example task families:
1. Hong Kong KAM extraction.
2. Hong Kong valuation KAM.
3. Hong Kong revenue KAM.
4. Singapore ISSB/climate disclosure.
5. Singapore Scope 1/2 calculations.
6. Singapore financial-report KAM.
7. Japan sustainability disclosure.
8. Japan impairment/valuation.
9. Japan human-capital disclosure.
10. Governance-risk-sustainability consistency.

Total: **30 cases**.

## 6. T0–T6 experimental treatments

| Treatment | Design |
|---|---|
| T0 | Human-only baseline |
| T1 | Single general-purpose foundation model |
| T2 | Single model + structured retrieval |
| T3 | Specialist agent + deterministic tools |
| T4 | Multi-agent specialist architecture |
| T5 | T4 + deterministic verification + policy/control gate + evidence lineage |
| T6 | T5 + cross-model challenge + mandatory human approval for material/high-judgment conclusions |

Core design size: **30 cases × 7 treatments = 210 case-treatment cells** before provider replications.

If six AI provider families are tested at the relevant treatment levels, the benchmark can expand to approximately **1,260 case-treatment-provider cells**, subject to the exact replication design.

## 7. Outcomes

Primary outcomes:
- Classification accuracy/F1.
- Numeric error.
- Unsupported-claim rate.
- Evidence precision/recall.
- Correct abstention/escalation.
- Reproducibility.
- Control-policy violations.
- Reviewer overrides.
- Completion time.
- Inference/tool cost.
- Human interventions and rework.
- Cross-model disagreement.
- Calibration of reviewer reliance.

## 8. Data and benchmark sources

See `docs/DATA_SOURCES.md`. Priority sources include:
- SEC EDGAR / CompanyFacts / XBRL.
- PCAOB CAM rules and audit reports.
- ESMA ESEF filings/taxonomy.
- IFRS/ISSB public navigation and licensed/permitted materials.
- Hugging Face SEC filing datasets.
- Kaggle fraud and ESG datasets for non-authoritative benchmarking.
- Researcher-created synthetic ledgers and case packets.

## 9. Open-source/reuse policy

The project **does not vendor third-party code by default**. It links to upstream repositories and records their licenses. This is important because not all “free” resources are OSI-open-source. For example, AI4SustainableX currently uses BUSL-1.1 for the source-available free tier. IFRS copyrighted standards should not be redistributed inside a public repository without appropriate permission.

## 10. Expected contributions

1. **Architecture contribution:** makes model, evidence, tools, controls, agents, challenge and human approval separately observable.
2. **Method contribution:** holds accounting procedures constant while changing model/provider.
3. **Assurance contribution:** treats provenance, reproducibility, abstention and control compliance as outcomes, not just predictive accuracy.
4. **Cross-jurisdiction contribution:** compares U.S., European and Asian reporting/assurance settings.
5. **Open-science contribution:** publishes prompts, synthetic cases, evaluation scripts, provider-neutral configs, and permissible public data links.

## 11. Deliverables

- Integrated GitHub research scaffold.
- 30-case benchmark registry.
- T0–T6 experiment protocol.
- Provider-neutral routing configuration.
- Agent catalogue and data-source registry.
- Reproducibility and evidence-lineage specification.
- Academic manuscript and supplementary appendix.
- Teaching version using synthetic or public data.

## 12. Milestones

**Phase 1 — Infrastructure:** install provider gateway, document parser, evidence store and deterministic accounting tools.

**Phase 2 — Gold standards:** create expert-labelled answers and evidence sets for the first 6–10 cases.

**Phase 3 — Pilot:** run T0–T6 on a small set across GPT, Claude and Gemini, then extend to Kimi and DeepSeek.

**Phase 4 — Full 30-case experiment:** preregister metrics, freeze prompts/tool versions, repeat runs and collect human-review outcomes.

**Phase 5 — Paper:** estimate architecture effects, heterogeneity by task/jurisdiction, cost-effectiveness and human-review interactions.

## 13. Boundary condition

This repository is a research and educational platform. It is not an audit firm, does not issue assurance, and must not be used to automate material accounting judgments without qualified human review.


## 14. Implementation Status — Version 0.2

As of 24 September 2026, the integrated research scaffold has been implemented in the GitHub repository and mirrored in Google Drive.

Completed:
- provider-neutral project structure;
- specialist-agent catalogue;
- official/public and benchmark data-source registry;
- 30-case U.S.–Europe–Asia portfolio;
- T0–T6 experimental protocol;
- provider configuration for GPT/Codex, Claude, Gemini, Microsoft/Azure, Kimi, DeepSeek and local models;
- provider-routing Python scaffold;
- third-party licensing/reuse guidance;
- Google Drive proposal mirror.

GitHub project:
https://github.com/Saehon/Saeid-Homayoun/tree/main/Open-Agentic-Accounting-Audit-Lab

Google Drive project folder:
https://drive.google.com/drive/folders/1_Zaq6PFJIZUX9O6AzBvmrf-_CRRWw_5s

Google Drive proposal:
https://docs.google.com/document/d/16Mq0zEZJsTNd73tGzfnE86WhRL2je4fUC92iiVJgINk/edit

### Next executable milestone

The next release should implement one end-to-end pilot case with:
1. a frozen evidence packet;
2. expert/gold-standard answer and evidence labels;
3. deterministic calculation/validation scripts;
4. T0–T6 run templates;
5. model/version metadata;
6. cross-model Reviewer Agent challenge;
7. policy/human-gate event log; and
8. exportable results suitable for statistical analysis.

A U.S. CAM + ICFR case is the preferred first pilot because SEC/PCAOB evidence is public and the case combines structured retrieval, accounting judgment, audit evidence and control evaluation.
