# IFRS Judgment Intelligence — FT50 Research Protocol
*Methodological annex of the [existing IFRS judgment programme](IFRS_JUDGMENT_AGENTIC_AI.md) · [Shared FT50 design and literature](../FT50_RESEARCH_DESIGN_AND_EVIDENCE.md)*

**State:** planned scientific design, not a certified IFRS engine, advice, or verified empirical effectiveness result. **NAAIL's governing architecture is unchanged.**

## Central contribution

Accounting-standard expertise cannot be reduced to question answering: reporting outcomes depend on **standard version**, **legal reporting regime**, **source evidence**, **estimation uncertainty**, **professional judgment**, and **enforcement incentives**. This programme tests whether a *source-restricted, falsification-capable, human-governed* AI workflow increases **appropriate judgment calibration** rather than merely producing plausible accounting-language explanations.

Competing predictions: extra reasoning steps and reviewer access may improve traceability; they may instead anchor reviewers on an invalid but persuasive IFRS passage, generate spurious precision, or increase cost with little gain.

### Theory and confirmed scholarly anchors

- Barth, Landsman & Lang (2008), *Journal of Accounting Research*, [International Accounting Standards and Accounting Quality](https://doi.org/10.1111/j.1475-679X.2008.00287.x): accounting quality and standards are jointly shaped by incentives and institutions.
- Christensen, Hail & Leuz (2013), *Journal of Accounting and Economics*, [Mandatory IFRS Reporting and Changes in Enforcement](https://doi.org/10.1016/j.jacceco.2013.10.007): standard adoption must be separated from simultaneous changes to enforcement.
- Blankespoor, deHaan & Li (2026), *Journal of Accounting Research*, [Generative AI in Financial Reporting](https://doi.org/10.1111/1475-679x.70050): model-derived financial-reporting text demands sound measurement.
- Bradford Levy (2026), *Journal of Accounting Research*, [Caution Ahead: Numerical Reasoning and Look-Ahead Bias in AI Models](https://doi.org/10.1111/1475-679x.70058): numerical calculation and historic model contamination warrant strict validation.
- *Human + AI in Accounting: Early Evidence from the Field* (2026), *Journal of Accounting Research*, [DOI](https://doi.org/10.1111/1475-679x.70052): human escalation and workflow complementarity can be studied at the task level.

## Hypotheses and opposing alternatives (not tested)

**H1 — Version/authority resolution:** compared with an unguided LLM, a time-aware, source-constrained agentic process reduces *expert-confirmed* errors attributable to inapplicable IFRS versions or unsupported standard citations.

**H2 — Numerical delegation:** assigning arithmetic to deterministic code rather than natural-language generation lowers correct-unit/correct-period calculation errors in identical accounting tasks.

**H3 — Calibrated oversight:** a separate falsification agent followed by a qualified human decision produces fewer **unwarrantedly confident** responses in ambiguous judgment cases than a single model.

**Rival hypothesis:** adding tool and agent steps can cause anchoring, accumulated source errors, correlated misjudgments or higher review cost; benefits may disappear once an independent expert gold standard and matched case complexity are imposed.

## Standards-aware task taxonomy

| Substantive accounting case | Evidence requirement | What counts as an error | Primary research measure |
|---|---|---|---|
| IFRS 15 revenue | Contract terms, satisfaction pattern, period | Wrong obligation/timing or invented contract clause | Adjudicated treatment correctness |
| IFRS 9 impairment / ECL | Segmentation, scenarios, assumptions, model inputs | Wrong inputs/horizon, formula, or unjustified forecast | Numeric result + explanation support |
| IFRS 16 leases | Contracts, extension assessment and rate | Incorrect liability roll-forward or omitted option | Deterministic reconciliation accuracy |
| IAS 36 impairment | Cash-generating unit, cash flows, discount assumptions | Incorrect aggregation, unsupported estimate | Review of assumptions and uncertainty |
| IAS 37 provisions | Past event, present obligation, probability, estimate | Asserted certainty where judgment is required | Appropriate uncertainty/abstention |
| IFRS 18 presentation | Effective date, adopted framework, presentation requirements | Retroactively applying 2027 rules without justified early adoption | Version-valid response |
| IFRS 10 / IFRS 3 | Ownership and control facts, transaction evidence | Conflating legal ownership with control | Expert-adjudicated conclusion |

**Critical version control:** IFRS 18 is effective for annual periods beginning on/after **1 January 2027**, earlier application permitted. A model answering a 2024 IFRS reporting question by applying IFRS 18 without applicable early adoption is a temporal/source error, not clever reasoning. Official issuer: [IFRS Foundation IFRS 18](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/).

## Dataset specification

| Field | Grain | Operational definition | Source/right |
|---|---|---|---|
| `case_id` | accounting case | Immutable version of fact pattern, fiscal year, currency and reporting basis | Original expert case or authorized real disclosure |
| `standard_version_id` | case × standard | Standard, amendment/effective dates, authoritative text version | Licensed IFRS materials; public metadata only |
| `evidence_passport_id` | case × document span | Evidence locator, reporting date and permitted source use | Source-rights gated document inventory |
| `judgment_alternatives` | case × candidate treatment | Permissible choices plus fact-specific conditions | Two qualified experts, independently coded |
| `arithmetic_expected` | numeric task | Machine-verifiable correct calculation with explicit units and tolerance | Independent reference calculations |
| `method_arm` | randomized task/participant | Pure code, ungrounded LLM, retrieval, agentic+code, agentic+human | Random-assignment log |
| `source_supported` | response × independent reviewer | Entailment of actual permitted source text | Blinded evidence assessment |
| `appropriate_abstention` | response | Refusal or escalation where not enough evidence exists | Predeclared expert rubric |
| `review_cost` | task × reviewer | Observed time/cost and override frequency | Session logs, consented research |

**Access gate:** public SEC annual reports or sample financial statements may support *illustrative cases*; they do **not** automatically grant redistribution rights to IFRS full texts, commercial financial databases, analyst reports or client workpapers.

## Identification: controlled research design

Primary identification through a **randomized, blocked vignette/task experiment**, not a before/after AI launch story. Randomize qualified participants/tasks to source-only, single LLM, governed multi-agent, and governed multi-agent + professional reviewer conditions; preregister the primary outcome and ensure no treatment contamination across reviewers.

```text
JudgmentQuality_{case,reviewer}
  = case fixed effect + treatment-arm effects
    + expertise stratum + design-prescribed interactions + error
```

Use **case and participant dependency-aware** uncertainty. Primary outcome: independently adjudicated **decision and support correctness**. Secondary: accuracy conditional on response, coverage, calibration, review minutes, monetary cost, reviewer trust and uncertainty. Evaluate effects separately for unambiguous computations vs contestable judgments.

**Archival extension:** do not claim that IFRS adoption *caused* improved reporting quality without identifying the relevant concurrent enforcement changes, compliance incentives, jurisdiction-specific implementation and selection. A cross-country association alone is not enough (Christensen, Hail & Leuz, 2013).

## Mandatory falsification and robustness

1. Deliberately vary **effective standard dates** and test whether the source resolver notices the mismatch.
2. Change currency units, sign, denominators and financial periods; run deterministic and LLM-only numeracy arms.
3. Construct ambiguous cases with multiple expert-acceptable responses; forbid single-label forced correctness where unjustified.
4. Adversarially insert nonauthoritative summaries; detect citation laundering and prompt injection.
5. Separate cases already widely published on the web from newly authored, chronologically valid cases; discuss model training leakage.
6. Report agent ablations, reviewer overrides, total cost and latency, not accuracy alone.
7. Explicitly record contrary predictions and *what would falsify H1–H3*.

## Journal contribution map, conditional on data

**JAR/TAR:** reliability and professional complementarity in judgment-intensive accounting. **JAE:** incentives, enforcement and reporting institutions when a defensible causal design is present. **CAR/RAST:** measurement validity, economic outcomes and heterogeneity; **AOS:** contested authority, expertise and accountability using organizational evidence.

**Private/public boundary:** detailed project working records and unpublished methods are maintained in private access-controlled personal Google Drive; the existing public [IFRS-AI Inspector](https://github.com/Saehon/IFRS-AI-Inspector) remains a research prototype. **No actual model run, source-text compliance verification, independent expert panel, or effect estimate is asserted in this plan.**
