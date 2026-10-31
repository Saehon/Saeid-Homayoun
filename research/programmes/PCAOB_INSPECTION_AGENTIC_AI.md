# PCAOB Inspection Intelligence | Agentic AI Research

**Principal investigator:** Saeid Homayoun · [Research programme overview](../AGENTIC_AI_ASSURANCE_RESEARCH.md)

**Scientific purpose:** investigate **inspection-oriented analyses of audit-work evidence and quality-control information** through evidence-governed agents, not replicate or impersonate the PCAOB's authority. This is an **independent academic project**; **not affiliated with, endorsed by or deployed at the PCAOB**.

## Journal-grade empirical research protocol

[**PCAOB FT50 Research Protocol — theoretical mechanisms, construct dictionary, randomized study, identification and falsification**](PCAOB_FT50_RESEARCH_PROTOCOL.md) · [Shared verified FT50 literature](../FT50_RESEARCH_DESIGN_AND_EVIDENCE.md).

This is a **methodological extension**, not a replacement for the PCAOB agentic architecture below. Published empirical anchors distinguish firm-level public inspection reports from undisclosed engagement-level inspection selections. No PCAOB endorsement or completed real-world inspection claim is implied.

## Problem and hypotheses to test

A selected audit area may disclose a critical risk but provide a weak or poorly documented connection between **risk assessment**, **procedures performed**, **results**, **control testing**, and **the basis for the final audit conclusion**. A traceable research workflow can flag *potential* inconsistencies and prioritize expert review. It cannot establish a regulatory inspection finding by itself.

**Research questions:** (1) Does source-linked multi-agent review improve identification of risk–procedure–evidence gaps relative to a single-pass model? (2) Can an independent adversarial reviewer reduce false positives in inspection-oriented alerts? (3) Do improvements vary with account complexity, the nature of CAMs, and ICFR evidence?

## Authoritative research anchors

- [PCAOB inspection procedures](https://pcaobus.org/oversight/inspections/inspection-procedures): **risk-based and random selections**, selected audit areas and firm quality-control elements, not all firm audits.
- [AS 1105 — Audit Evidence](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105): sufficiency, appropriateness, reliability and audit-evidence procedures.
- [AS 2301 — Auditor's Responses](https://pcaobus.org/oversight/standards/auditing-standards/details/AS2301): audit-response alignment with assessed material-misstatement risks.
- [AS 1215 — Audit Documentation](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1215): documentation and review traces. Amendments have distinct effective dates; any experiment must identify the **applicable** version for the audit period.
- [PCAOB standards index](https://pcaobus.org/oversight/standards/auditing-standards) for period-specific standards and amendments.

**Important:** PCAOB inspection reports are not overall ratings of audit firms and do not establish that uninspected work is defect-free.

## Proposed agent responsibilities

| Role | Inspectable output | Failure gate |
|---|---|---|
| Scope / period agent | Audit period, jurisdiction, governing standard version | Reject unscoped standards |
| Risk–assertion mapper | Significant accounts, relevant assertions and assessed risks | Detect false mapping |
| Evidence-passport agent | Audit evidence IDs, provenance and permitted source location | Reject fabricated/missing source |
| Controls / ICFR agent | Design vs operating-effectiveness distinction and test evidence | No inferred control success without direct tests |
| CAM intelligence agent | CAM account/topic and described audit response | CAM disclosure is not a substitute for audit workpapers |
| Adversarial inspector / falsifier | Counterevidence, missed procedures, false-positive challenges | Preserve full dissent and uncertainty |
| Human oversight gate | Escalation to qualified auditor/researcher | No automated regulatory deficiency determination |

## Proposed evaluation protocol

**Units of analysis:** company-year, audit engagement or selected CAM/account-risk observations, as permissions allow. **Outcomes:** evidence-gap identification accuracy against a blinded expert gold set; precision/recall with risk-sensitive error costs; reviewer agreement; trace completeness; abstention; and independent falsification outcomes.

**Contrasts:** deterministic check vs single model vs structured multi-agent review. Separate *descriptive* association from causal claims. Stratify by audit area, risk, period and industry; use frozen holdout firms and time periods.

## Public vs private status

Publicly inspectable support: [KIWI research methods](../../NAAIL-OpenLab/KIWI/README.md), [evidence-based evaluator](../ai_evidence_evaluation/README.md) and [NAAIL public research overview](../RESEARCH_HIGHLIGHTS_AND_ONGOING_PROJECTS.md). **Core PCAOB-specific research and substantive work are in progress**, with primary working documents maintained in **private, access-controlled personal Google Drive** and selected confidential implementation remaining outside public release.

**No PCAOB inspection has been conducted by this GitHub programme. No regulatory approval, actual inspection conclusion, access to nonpublic inspection workpapers, or independently verified empirical model performance is claimed.**