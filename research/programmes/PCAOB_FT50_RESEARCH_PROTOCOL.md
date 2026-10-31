# PCAOB Inspection Intelligence — FT50 Research Protocol
*Scientific extension of the [existing PCAOB agentic research track](PCAOB_INSPECTION_AGENTIC_AI.md) · [FT50 methods and verified literature](../FT50_RESEARCH_DESIGN_AND_EVIDENCE.md)*

**State:** proposed empirical tests, not independently validated PCAOB findings. The main architecture and human review remain unchanged.

## Theory, research gap and competing mechanisms

PCAOB inspection findings reveal oversight concerns, but public reports do **not** generally identify the particular client engagements selected. Inspection regimes select on risk and firms respond to perceived inspection exposure; a model that predicts public deficiency language is **not automatically** a model that identifies deficient engagement audit evidence.

The research seeks to test a *risk-to-procedure-to-evidence* mechanism: does separately governed, grounded reasoning reveal missing links that a single LLM or keyword procedure misses? A competing hypothesis is **citation laundering / accountability displacement**, under which a convincing multi-agent narrative increases human reviewer confidence without improving evidence quality.

The distinction is informed by:
- Constance, Lennox & Li (2025), *Contemporary Accounting Research*, [DOI](https://doi.org/10.1111/1911-3846.13000): heterogeneous deficiency types and future misstatement risk.
- Stuber & Hogan (2021), *Journal of Accounting Research*, [DOI](https://doi.org/10.1111/1475-679X.12339): inspection incentives and estimation quality may not move together.
- *Costs and benefits of a risk-based PCAOB inspection regime* (2024), *Accounting, Organizations and Society*, [DOI](https://doi.org/10.1016/j.aos.2024.101552): risk-based inspection selection and accountability.
- Fedyk et al. (2022), *Review of Accounting Studies*, [DOI](https://doi.org/10.1007/s11142-022-09697-x): AI audit investment, quality and efficiency are distinct constructs.

## Pre-registered hypotheses (unverified)

**H1 — Evidence alignment:** versus a deterministic + retrieval baseline, an agentic method with independent falsification reduces **adjudicated false-negative** risk–procedure–evidence gaps in authorised, blind-labelled *task-level cases*.

**H2 — Human complementarity:** a real independent expert review of a grounded agentic output produces a higher correctness–coverage frontier than *human-only* and *agent-only* conditions, but may be slower.

**H3 — Countervailing effect:** unsupported agent explanations and high-complexity CAM narratives increase false-positive flags and/or automation bias; this can offset H1.

**Boundary:** if only **firm-level public inspection reports** are available, use them as **firm-level predictors or text outcomes**; **do not** infer which audited engagements were inspected.

## Data blueprint and measurement

| Variable / key | Grain | Definition or operationalization | Potential source; access gate |
|---|---|---|---|
| `case_id` | task / risk–assertion case | Immutable blind gold-case ID | Independently authored and legally reusable expert cases |
| `audit_firm_id`, `inspection_report_year` | firm-report | Firm identity and report issue date | Public PCAOB inspection reports; actual public coverage to be checked |
| `public_deficiency_category` | firm-report × deficiency category | Manual double-code the disclosed type; *not engagement-specific* | Public inspection narratives; annotation rights |
| `CAM_topic`, `CAM_year` | company-year-CAM | Topic/account, issue date and original wording rights | SEC EDGAR / audit-report publications, authorized corpus |
| `expert_gap_label` | task × reviewer | Gap present / absent / ambiguous; reviewer disagreements preserved | Blinded independent accountant/auditor annotation |
| `evidence_entailment` | task × source | Whether cited text actually supports the risk response | Approved source spans, independent rating |
| `method_arm` | randomized task assignment | Rule-only / retrieval-only / single LLM / agentic / agentic+human | Experiment log, **not** observational adoption |
| `false_negative`, `false_positive` | task × method | Classification error against adjudicated label | Gold-holdout evaluator |
| `review_minutes`, `cost` | reviewer-task / model-run | Human effort and observed permitted API cost | Actual timestamps and billed usage |

**Observation eligibility:** restrict public examples to synthetic or licensed data. Nonpublic PCAOB inspection workpapers, audit-firm client files and proprietary Audit Analytics records **must not** be inferred to be publicly available.

## Identification and analysis plan

**Primary design (recommended):** a *task-level blocked randomized experiment* assigning otherwise comparable cases across methods, with independent human graders blind to assignment. Block on account/industry/complexity and standard version. Participant-level randomization or counterbalancing must prevent the same participant from seeing the same answers across arms.

```text
GapCorrect_{case,reviewer,arm}
  = alpha_case + beta1 AgenticArm
               + beta2 HumanReviewArm
               + beta3 AgenticArm × HumanReviewArm
               + reviewer_covariates + epsilon
```

**Causal estimate:** randomized *intention-to-treat* method effect on independent correctness. Cluster uncertainty by reviewer and/or case according to randomization; present assignment and dependence structure. Define one **primary** error outcome and one **secondary** human-time/cost outcome. Do not treat repeated evaluations of a single case as independent firm-years.

**Archival extension only if defensible:** inspection-report panel with audit-firm and year fixed effects; explicitly address inspection targeting, access constraints, anticipation, report-date leakage, client composition and outcomes observed **after** findings. A plain difference-in-differences estimate is **not causal** without plausible parallel trends and an exogenous assignment mechanism.

## Falsification and failure gates

1. **Selection placebo:** labels derived from report release dates should not predict outcomes that were known only before the release, after correcting for available information.
2. **Cross-firm leakage:** exclude firm/client overlapping identifiers from both development and holdout as appropriate.
3. **Narrative-only ablation:** compare grounded evidence with CAM text alone to isolate mere disclosure recognition.
4. **Agent dependency:** remove falsifier, tool verification and reviewer gate one at a time; measure what each contributes.
5. **False confidence:** assess whether unsupported citations increase professional overreliance.
6. **External validity:** no deployment/inspection claim without actual legally permitted practice and expert approval.

## Expected manuscript contribution if supported

**TAR/JAR/CAR:** a new, independently validated task-level measure of *risk–procedure–evidence alignment* and evidence of whether governed AI improves reviewer decisions.

**AOS:** an account of accountability, expertise, regulatory gaze and machine-generated authority, supported by real observation or qualitative interviews.

**JAE:** economic consequences of monitoring and auditor incentives, but only with a genuinely credible identification strategy.

**Status:** research questions and design only; **no sample counts, effects, real inspection outcomes or model comparisons have been verified by this document**. Primary research materials remain in private access-controlled Google Drive.
