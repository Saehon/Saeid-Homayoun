# FT50 Research Design and Evidence Alignment
## An empirical-methods extension of the existing NAAIL Agentic AI framework

**Research investigator:** Saeid Homayoun · **Updated:** 31 October 2026 · **Status:** methodological research plan, **not** completed experiments.

**Architecture unchanged.** This document strengthens the existing [PCAOB–IFRS–ISSB Agentic AI research framework](AGENTIC_AI_ASSURANCE_RESEARCH.md); it **does not** establish a competing architecture, introduce a new governing core, rename NAAIL/POMELO/VERA, or change professional approval rules.

> **Development and privacy notice.** These projects are in progress. Primary working manuscripts, research records and substantive project materials are maintained in a **private, access-controlled personal Google Drive**. This page presents only authorized public research designs, credible bibliographic links, and methodological standards. Public code tests and synthetic fixtures are not externally validated empirical findings.

**Academic claim-level integrity:** [Evidence traceability and release checks](literature/ACADEMIC_EVIDENCE_QUALITY_GATES.md) distinguish DOI metadata, theory motivation and methods from independently replicated research findings. The [project literature ledger](literature/project_evidence_ledger.json) tracks explicitly untested hypotheses and unresolved evidence.

**Cross-cutting bibliography:** [Harvard-referenced LLM, Fine-Tuning and Agentic AI research registry](LLM_FINE_TUNING_AGENTIC_AI_HARVARD_REFERENCES.md). The living list spans selected FT50 and AJG journal groups; Crossref DOI metadata checks cannot authenticate journal rankings or prove the research hypotheses of this framework.

## 1. Journal basket and honest fit

The **Financial Times FT50 list was revised in April 2026**. The following six accounting journals are in the FT50 basket: *The Accounting Review (TAR)*, *Journal of Accounting Research (JAR)*, *Journal of Accounting and Economics (JAE)*, *Accounting, Organizations and Society (AOS)*, *Contemporary Accounting Research (CAR)*, and *Review of Accounting Studies (RAST)*. See the [April 2026 University of Alberta library list](https://www.ualberta.ca/en/business/research/publications/top-journals-business-management-list.html) and [Financial Times announcement](https://www.ft.com/content/db863a0a-6524-45f9-bc52-fee997634bdc).

The tables below identify **potential editorial fit, not submission guarantees or journal endorsement**. Journal fit depends on actual theoretical advance, research execution, external validity, and editorial policy—not a particular AI tool or number of agents.

| Journal | Contribution angle worth testing | Appropriate evidence | Avoid |
|---|---|---|---|
| **TAR** | Auditing/accounting constructs: specificity of audit responses, evidence relevance, quality of professional judgments | Registered definitions, reviewer gold, risk- or account-level tests, archival or controlled experiments | Generic NLP accuracy presented as audit quality |
| **JAR** | Information economics, AI-assisted judgment complementarity, econometric inference and credible mechanism | Causal experiment or compelling panel design, careful AI measurement and construct validation | Historical LLM look-ahead bias; treating all observations as independent |
| **JAE** | Incentives, institutional design, standard enforcement, monitoring consequences | Identification strategy, economically meaningful outcomes, simultaneous reforms addressed | Mechanistic causal statements from selective inspections or nonrandom adoption |
| **AOS** | Organizational accountability, professional skepticism, human–AI control relations and institutional tensions | Theory-rich process tracing, interviews, qualitative/field evidence or mixed methods | Assuming greater automation automatically equals professional legitimacy |
| **CAR** | Validated disclosure/audit measurement, heterogeneity, regulatory information content and future risk | Tested constructs, carefully defined reporting outcomes and observable disclosure samples | Treating firm-level inspection findings as engagement-level truth |
| **RAST** | Technology's economic effects, audit efficiency/quality, reporting regulation and sustainability transparency | Strong empirical design, replicability, costs and external validity | Synthetic demo scores or technology-brand stories without outcomes |

**Specialist outlet caveat:** *Auditing: A Journal of Practice & Theory (AJPT)* is an important research outlet but is **not among the six FT50 accounting journals** above; do not label it FT50.

## 2. Core research contribution: beyond a technology demonstration

The research unit should be **a theory-linked economic or organizational mechanism** (risk response, professional accountability, verifiable reporting, investor decision usefulness), with agentic AI serving as an **intervention or measurement instrument**, not the contribution by itself.

**Proposed mechanism chain:**

```text
Uncertainty / information frictions / inspection incentives
    -> evidence retrieval + counterevidence + bounded specialist agents
    -> decision traceability and calibrated human override
    -> measured evidence error, judgment quality and downstream outcomes
    -> heterogeneous effects + economic/organizational trade-offs
```

Compare competing predictions: additional agent coordination may reduce overlooked evidence **or** introduce correlated errors, citation laundering, overreliance, latency and costs. Human review may improve accuracy **or** be undermined by persuasive erroneous explanations. Falsifiable alternatives must appear alongside favorable hypotheses.

## 3. Three research tracks within the unchanged framework

| Existing research lane | Primary unit / question | Pre-specified primary measure | Mechanism / rival explanation | Companion protocol |
|---|---|---|---|---|
| **PCAOB Inspection Intelligence** | Risk–assertion–procedure–evidence **account/engagement task**: can agents improve *expert-confirmed* gap identification? | Adjudicated precision/recall or cost-weighted error **on authorized expert-labelled cases** | Better evidence alignment vs inspection-selection, risk proxies and evaluator bias | [PCAOB FT50 protocol](programmes/PCAOB_FT50_RESEARCH_PROTOCOL.md) |
| **IFRS Judgment Intelligence** | **Accounting case × standard-version × reviewer**: can agents reduce unsupported judgments? | Correct authorized treatment + documented basis + calibrated abstention | Source/version resolution vs case memorization, accounting alternatives and leakage | [IFRS FT50 protocol](programmes/IFRS_FT50_RESEARCH_PROTOCOL.md) |
| **ISSB Sustainability Intelligence** | **Firm–report-year–disclosure item**: can agents measure decision-useful disclosure *connectedness* reliably? | Expert-rated, evidence-grounded financial connectedness with applicable relief/mandate flags | Information quality vs reporting incentives, compliance templates and ESG-data selection | [ISSB FT50 protocol](programmes/ISSB_FT50_RESEARCH_PROTOCOL.md) |

**Common design gate:** separate *measurement validity* (did a tool correctly encode a construct?), *identification* (can effects be causally attributed?), and *external validity* (do findings generalize to regulated work?). A code pass cannot substitute for any of these.

## 4. Verified FT50 scholarship and its methodological relevance

The linked DOI records below are **external published papers**; they are **not authored by this research programme**, and their results are not replicated in this repository. Papers are intentionally included because their published evidence creates *testable tensions*, not to imply uniform support for AI.

| Scholarship (journal, year) | DOI / publisher record | Relevance and scientific challenge |
|---|---|---|
| Constance, Lennox & Li, **PCAOB inspection deficiencies and future financial reporting quality** (*CAR*, 2025; online 2024) | [10.1111/1911-3846.13000](https://doi.org/10.1111/1911-3846.13000) | Distinguish types of deficiencies and future misstatement risk; avoid assigning firm-level findings to individual audits |
| Stuber & Hogan, **Do PCAOB Inspections Improve the Accuracy of Accounting Estimates?** (*JAR*, 2021) | [10.1111/1475-679X.12339](https://doi.org/10.1111/1475-679X.12339) | Inspection incentives may lead to *different* risk-management behaviors; improvements are not automatic |
| **Costs and benefits of a risk-based PCAOB inspection regime** (*AOS*, 2024) | [10.1016/j.aos.2024.101552](https://doi.org/10.1016/j.aos.2024.101552) | Inspection selection and accountability mechanisms are part of identification |
| **Do practitioner assessments agree with academic proxies for audit quality?** (*JAE*, 2019) | [10.1016/j.jacceco.2018.09.001](https://doi.org/10.1016/j.jacceco.2018.09.001) | Academic proxies and inspected process quality are not interchangeable |
| Barth, Landsman & Lang, **International Accounting Standards and Accounting Quality** (*JAR*, 2008) | [10.1111/j.1475-679X.2008.00287.x](https://doi.org/10.1111/j.1475-679X.2008.00287.x) | Institutional incentives/selection and enforcement can confound standard-related associations |
| Christensen, Hail & Leuz, **Mandatory IFRS Reporting and Changes in Enforcement** (*JAE*, 2013) | [10.1016/j.jacceco.2013.10.007](https://doi.org/10.1016/j.jacceco.2013.10.007) | Disentangle adoption and simultaneous enforcement reforms |
| Christensen, Hail & Leuz, **Mandatory CSR and sustainability reporting: economic analysis and literature review** (*RAST*, 2021) | [10.1007/s11142-021-09609-5](https://doi.org/10.1007/s11142-021-09609-5) | Materiality, reporting incentives, real effects, enforcement and assurance trade-offs |
| Fedyk, Hodson, Khimich & Fedyk, **Is artificial intelligence improving the audit process?** (*RAST*, 2022) | [10.1007/s11142-022-09697-x](https://doi.org/10.1007/s11142-022-09697-x) | Separate investments, audit-process quality, costs and labor reallocation |
| Blankespoor, deHaan & Li, **Generative AI in Financial Reporting** (*JAR*, 2026) | [10.1111/1475-679x.70050](https://doi.org/10.1111/1475-679x.70050) | Reporting language and generative-AI measurement require transparent construct validity |
| **Human + AI in Accounting: Early Evidence from the Field** (*JAR*, 2026) | [10.1111/1475-679x.70052](https://doi.org/10.1111/1475-679x.70052) | Human overrides, workflow-level complementarity and field/experimental triangulation |
| Bradford Levy, **Caution Ahead: Numerical Reasoning and Look-Ahead Bias in AI Models** (*JAR*, 2026) | [10.1111/1475-679x.70058](https://doi.org/10.1111/1475-679x.70058) | Numeracy, memorization, historical contamination and temporal holdout are central validity threats |

**Literature status:** a selected, source-linked foundation, **not** a completed systematic review, comprehensive novelty scan, meta-analysis, or verification of every claimed replication package. Follow each publisher DOI before manuscript citation; independently inspect code/data rights where reproduction is proposed.

## 5. Minimum FT50-style scientific evidence package

| Section / artifact | Mandatory question | Release test |
|---|---|---|
| Contribution memo | What existing theoretical mechanism is challenged or extended? | Cite exact paper and document what this project can uniquely test |
| Construct table | What is observed versus latent, and at which statistical grain? | Independent double annotation; inter-rater metrics and construct audit |
| Data lineage | Which observation originates in which authorized source, version and date? | Source-rights register, raw counts, join keys, deduplication, SHA-256 |
| Identification | Why does a change in agent design, standard, or reporting requirement identify an effect? | Causal graph, treatment definition, counterfactual, confounder table |
| Pre-registration | What is primary outcome, sample, exclusion and multiple-testing plan? | Frozen protocol *before* holdout, analysis code and feature selection |
| Benchmarks and ablation | What value do agentic steps add over code-only, retrieval-only, single LLM and human review? | Task-matched runs; no uncontrolled prompts or data leakage |
| Error analyses | Where does the system fail and whom could it harm? | Stratified false positives/negatives, abstentions, human override and cost |
| Robustness/falsification | Which result would refute the preferred mechanism? | Placebos, negative controls, time-shift tests and sensitivity intervals |
| Economic relevance | What decision or organizational outcome changes? | Auditing/financial reporting outcomes, review time, effort, cost, not a single F1 |
| Replication | Can a separate team reproduce eligible outputs? | Reproducible scripts, container/env lock, privacy-safe fixtures and review record |

**No fabricated sample counts or regression findings.** Planned samples are not observed datasets. Privately held data must not appear as publicly available until its existence, grain, rights and usable scope are verified.

## 6. Research governance: external contribution vs retained intellectual property

The research retains **NAAIL's existing two-core architecture** and the published PCAOB/IFRS/ISSB specialist pages. New methodological protocols are annotations to that framework. The actual knowledge sources, licensed accounting standards, case records, restricted supervisory materials, proprietary data, and unpublished working manuscripts remain subject to existing private controls.

- **PCAOB** is an audit oversight/standard-setting authority in the relevant US context.
- **IASB** issues IFRS Accounting Standards.
- **ISSB** issues IFRS Sustainability Disclosure Standards (IFRS S1/S2).
- **IAASB** issues assurance standards including ISSA 5000.
- The project is **not** officially affiliated with any of these authorities and makes **no** finding about an actual PCAOB inspection or a professional audit conclusion.

## 7. Practical next gate

Complete **one** well-bounded, permission-cleared task-level experiment with the same question/evidence across baseline code, one LLM, a tool-using agent and a human-review condition; obtain genuinely independent expert labels, measure intervention costs, and report case-level error patterns. Only then consider a larger archival design with verifiable company-years, access rights, and preregistered hypotheses.

*Framework: unchanged · FT50 methodology: proposed and explicitly not yet empirically executed.*
