# NAAIL V1 B5 — Human Ground-Truth Protocol V1

Status: **DRAFT**  
Protocol ID: `NAAIL-V1-B5-HGT-V1`  
Authority: human governance; Claude independent review; repository operator limited to administration and deterministic checks.

## Purpose and boundary

This protocol specifies how blinded human labels may later be collected and reconciled for V1. It does not authorize coding, data retrieval, case selection, scoring, or a scientific conclusion. Execution remains gated on human POC approval, Claude approval of this protocol, and a recorded pre-data freeze.

The repository operator has seen the detector and the disclosed Benchmark V2 evasion examples. The operator therefore may write and validate this protocol but may not author holdout probes, code items, adjudicate labels, select cases, or make the ground-truth decision.

## Human-governance amendment

The following direction is recorded additively from the human authority:

> Hourly runs never stop. On any problem, record it and continue with the next admissible item.  
> When all POC items are blocked on the human or Claude, V1 PREPARATION may proceed. The POC stays OPEN until the human approves it.

This amendment changes workflow authorization only. It does not satisfy a POC or V1 scientific gate.

## Design

- Each scored item receives two independent labels.
- A separate adjudicator reviews locked disagreements only after the preregistered reliability calculation.
- The data custodian randomizes item identifiers and retains the sealed mapping.
- Training items are disjoint from scored items and excluded from V1 metrics.
- Objective fields and judgment-dependent fields remain separate throughout storage, reliability reporting, adjudication, and downstream analysis.

## Blinding

Coders receive the frozen handbook, the materials required to assess the item, a randomized identifier, and a locked coding form. Before their labels are locked, they do not receive detector or baseline outputs, another coder's labels, expected/injected labels, condition identity, or performance summaries. Coders may not discuss scored items with one another before lock.

## Reliability decision rule

The preregistered primary statistic is unweighted Cohen's kappa, computed before adjudication. It is reported separately for eligible binary `error_present` labels and eligible nominal `error_category` labels.

The minimum threshold is **kappa >= 0.70**. The report must also disclose confusion-matrix counts, raw agreement count, eligible item count, marginal label counts, and missing/excluded item counts. If kappa is undefined because the eligible labels lack marginal variation, the threshold is not met. If a required kappa is below threshold, the affected ground truth remains `PRELIMINARY` and `HUMAN_REVIEW` and cannot support confirmatory system claims.

No alternative metric may silently replace the preregistered decision rule.

## Adjudication and preservation

Raw coder labels become immutable before reliability is calculated. The adjudicator receives source materials, the frozen codebook, both raw labels, and coder rationales, but not detector/baseline outputs, condition identity, or performance summaries. Every adjudicated label records the item, both raw labels, decision, rationale, adjudicator, and UTC timestamp. Unresolved items remain `HUMAN_REVIEW`.

Missing labels and exclusions remain visible in the item manifest with reasons. There is no silent exclusion.

## Freeze-before-data gate

Before any scored item is released, the protocol, coder handbook, coding form/schema, item-manifest schema, analysis script, and completed preregistration record must each have a Git blob and SHA-256 fingerprint. The freeze timestamp must precede coder labels, system scoring, and result inspection. A material change creates a new version and new freeze; historical records remain immutable.

The companion template is `human_ground_truth_preregistration_template_v1.json`. The normative machine-readable requirements are in `human_ground_truth_protocol_v1.json`.

## Limitations

This draft has not been independently approved, no coders have been recruited, no items have been selected or labeled, and no agreement statistic has been calculated. Protocol preparation is not detector validation.
