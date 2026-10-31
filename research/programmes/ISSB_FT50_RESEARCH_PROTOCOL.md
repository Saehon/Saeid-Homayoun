# ISSB Sustainability Intelligence — FT50 Research Protocol
*Methodological annex to the [existing ISSB Agentic AI track](ISSB_SUSTAINABILITY_AGENTIC_AI.md) · [Shared FT50 research design and scholarship](../FT50_RESEARCH_DESIGN_AND_EVIDENCE.md)*

**Maturity:** research proposal and operationalization plan, not completed ISSB implementation, independent assurance or verified empirical results. **NAAIL architecture unchanged.**

## Theory and scientific novelty

Sustainability-related financial disclosures are informative only when the **underlying business assumptions, source evidence and implications for financial prospects** can be understood. High narrative similarity across a sustainability report and annual report is not itself *economic connectedness*. A governed agentic method may detect verifiable links between financially material climate risks and financial-reporting estimates, or it may simply reward polished boilerplate.

A defensible contribution would establish a **new validated construct for source-backed sustainability–financial connectedness** and test whether it predicts economic outcomes *beyond report length, generic ESG scores, mandatory adoption or assurance badges*.

### FT50 research foundation

- Christensen, Hail & Leuz (2021), *Review of Accounting Studies*, [Mandatory CSR and sustainability reporting: economic analysis and literature review](https://doi.org/10.1007/s11142-021-09609-5). Distinguish investor-focused materiality, incentives, compliance and real effects.
- Barth, Landsman & Lang (2008), *Journal of Accounting Research*, [International Accounting Standards and Accounting Quality](https://doi.org/10.1111/j.1475-679X.2008.00287.x). Information quality depends on institutions and incentives as well as rules.
- Christensen, Hail & Leuz (2013), *Journal of Accounting and Economics*, [Mandatory IFRS Reporting and Changes in Enforcement](https://doi.org/10.1016/j.jacceco.2013.10.007). Adoption changes and enforcement changes must be separated.
- Blankespoor, deHaan & Li (2026), *Journal of Accounting Research*, [Generative AI in Financial Reporting](https://doi.org/10.1111/1475-679x.70050). AI-generated prose can complicate disclosure-quality measurement.
- Bradford Levy (2026), *Journal of Accounting Research*, [AI numerical reasoning and look-ahead bias](https://doi.org/10.1111/1475-679x.70058). AI-based historical measures may be contaminated by later information.

**Do not claim that these studies already validate a specific agentic ISSB index.** They support the underlying scientific questions and identification concerns.

## Important regulatory boundaries

**IFRS S1 and IFRS S2** are ISSB-issued *sustainability disclosure standards*. Their general effective date is for annual periods beginning on/after **1 January 2024**, subject to actual jurisdictional adoption, entity reporting basis, permitted transition relief and changes. The 2024 global effective date **does not mean universal mandatory adoption**.

**IAASB ISSA 5000** is an international *sustainability assurance* standard; assessing an entity's disclosed text under S1/S2 does **not** establish the existence or quality of an assurance engagement. EU **ESRS/CSRD double materiality** has a distinct reporting scope and should never be silently equated to ISSB financial materiality. Verify jurisdiction/year and official issuer guidance before creating treatment groups.

Official sources: [IFRS S1](https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/ifrs-s1-general-requirements/), [IFRS S2](https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/ifrs-s2-climate-related-disclosures/), [IAASB handbook and ISSA 5000](https://www.iaasb.org/publications/2026-handbook-international-quality-management-auditing-review-sustainability-and-other-assurance).

## Research questions and opposing hypotheses

**H1 — Verified connectedness:** a traceable evidence-to-financial-impact measure identifies *expert-verified* links better than lexical overlap, disclosure length, or a single unconstrained LLM.

**H2 — Contextual incremental information:** conditional on observable reporting incentives and firm characteristics, stronger verified connectedness is **associated with** greater forecast-relevance or lower analyst disagreement. **Association does not establish causality.**

**H3 — Adversarial reliability:** adding a specialized omission/nonapplicability and numerical-check agent reduces false disclosure deficiencies relative to a single-pass score.

**Alternative:** templated compliance, greater disclosure budgets, firm size and selective reporting may jointly raise connectedness scores and investor outcomes; more AI agents may produce systematic false positives or substitute boilerplate for verified detail.

## Operationalization and data dictionary

| Construct | Grain | Proposed measurement | Validity requirement |
|---|---|---|---|
| `issb_applicability` | jurisdiction × entity × year | Explicit rule/adoption and relief status | Official local rule and reporting-period verification |
| `disclosure_item_id` | firm × report-year × item | Frozen S1/S2-specific item with scope | Licensed standard mapping, no copied restricted passages |
| `evidence_support` | item × financial disclosure span | Independent expert decision supported / contradicted / insufficient | Source-text span; report filing date; blind reviewer |
| `fin_connectedness` | firm × year × topic | Proportion of **applicable** climate/other topics with a verified causal or decision-relevant financial link, conditional on agreed rubric | Denominator excludes justified nonapplicable/relieved items; not raw keyword count |
| `climate_metric_valid` | firm × year × metric | Units, scope, boundary, base year and disclosed assumptions reconcile | Source trace + deterministic recalculation |
| `greenwashing_flag` | disclosure × claim | **Potential** inconsistency needing human review; *not* a misconduct determination | Confirmed discrepancy and false-positive analysis |
| `actual_assurance` | firm × year | Existence, provider, scope and assurance level from issued report | Independently verifiable assurance statement |
| `document_preparation_cost` | firm/report | Only when genuinely observed, not inferred from report length | Permissioned time/cost evidence |
| `outcomes` | firm × subsequent period | Analyst forecast error/disagreement, liquidity, financing cost, investment | Temporal sequencing, valid observation and confounder controls |

**Suggested index (proposal, not computed):** 
```text
Connectedness_i,t = [sum over applicable topics of source-verified financial links]
                   / [number of applicable topics with sufficient observable evidence]
```
Report **missing evidence** separately: do not make an empty/unknown denominator equal zero. Use expert-validated weighting only if preregistered; perform equal-weight sensitivity tests. Distinguish an **absent disclosure**, an **inapplicable item**, a **permitted relief**, and a **missing source document**.

## Identification strategy: two complementary but noninterchangeable designs

### A. Task-level randomized measurement study (first achievable milestone)

Blind experts label authorized sustainability/financial statement pairs. Randomize cases or coders into rules/keywords, single-LLM, multi-agent evidence, and multi-agent + qualified human-review arms. Primary outcome: adjudicated **entailment and classification error**, separately for applicable/relieved/missing items. Secondary: analyst time, abstention, missed cross-statement links, and cost.

This directly identifies **effects of the AI evaluation method on the task**, not benefits of mandatory ISSB adoption for firms.

### B. Firm-level economic consequence study (conditional future work)

Estimate the association between **validated connectedness** and later economic outcomes with firm and time fixed effects, industry-year structures and relevant incentives/controls, respecting timing and statistical dependence.

If exploiting a staggered reporting mandate, explicitly verify:
- lawful applicability, adoption date, exemptions and transition relief in each jurisdiction;
- baseline treated/control differences, anticipation, **pre-trends** and concurrent reforms;
- heterogeneous treatment effects; avoid naive two-way fixed-effect staggered DiD if treatment effects differ;
- standard and materiality changes, enforcement, assurance regime changes, and economic shocks;
- selection into voluntary reporting and validity of the outcome measurement.

Only call an estimate **causal** if these checks and a defensible source of exogenous variation support the claim. A routine regression with ESG scores is not enough.

## Falsification and robustness

1. **Temporal placebo:** later-known climate metrics or revised disclosures must not enter earlier information sets.
2. **Boilerplate placebo:** matched generic ESG passages should not score as source-verified financial impact.
3. **Adoption relief sensitivity:** distinguish mandatory vs voluntary vs optional/relieved cases, reporting years and IFRS/ESRS differences.
4. **Construct validation:** double-coded expert evidence, reviewer adjudications, financial-statement consistency and missingness audits.
5. **Cross-industry holdout:** energy vs services vs financial issuers; prevent issuer duplicates across train/evaluation.
6. **Ablation:** quantify the incremental value of source resolver, numerical verifier, adversarial critic and human gate.
7. **Assurance boundary:** validate any assurance claim against the actual separate assurance report; an AI disclosure grade is **never** an assurance opinion.

## Journal-fit conditional on executed evidence

**JAR/JAE/RAST:** information economics, regulatory adoption and financial consequences, conditional on credible identification. **CAR/TAR:** disclosure measurement/assurance-user experiment, construct validity and professional decision usefulness. **AOS:** institutional dynamics of sustainability reporting, agency, responsibility and trust using theory-driven qualitative/field evidence.

**Current claim boundary:** research blueprint only; no executed sample, ISSB/ISSA 5000 engagement, validated climate index, verified economic effect, or real-provider performance score is presented. Primary working materials and studies remain in private, access-controlled personal Google Drive.
