# Research Design: From Human-AI Collaboration to AI-to-AI Assurance

## Research question

When does a multi-agent decision architecture improve the reliability, verifiability and managerial value of high-stakes accounting and audit judgments relative to a single AI agent or conventional human-AI collaboration?

## Experimental conditions

1. Base LLM, no tools.
2. Single agent + MCP tools.
3. Multiple specialist agents + A2A collaboration.
4. Multi-agent + independent reviewer/falsifier.
5. Multi-agent + reviewer/falsifier + risk-triggered human approval.

## Initial task domains

- SEC/XBRL fact retrieval and reconciliation
- ICFR evidence-to-deficiency classification
- IFRS 15/IAS 36 treatment and judgment
- CAM/KAM extraction and comparison
- GL/AP/AR anomaly and control testing

## Primary outcomes

- factual/judgment accuracy against independent gold labels;
- unsupported-claim rate;
- evidence completeness;
- reproducibility of calculations;
- calibration/confidence;
- adversarial defect-detection rate;
- human override quality;
- latency and inference cost;
- traceability/auditability.

## Key hypotheses

**H1 — Specialization:** role-specialized agents connected through explicit protocols outperform a single generalist agent on heterogeneous tasks when domain tools and evidence schemas differ.

**H2 — Independent challenge:** an operationally independent reviewer/falsifier reduces undetected material errors relative to consensus-only multi-agent collaboration.

**H3 — Evidence mediation:** the benefit of multi-agent systems is stronger when outputs include an inspectable Evidence Passport rather than unstructured rationale alone.

**H4 — Selective human authority:** risk-triggered human approval produces a better error-cost tradeoff than either universal automation or universal manual review when task risk is heterogeneous.

**H5 — Correlated-error boundary:** adding agents does not improve reliability when agents share sufficiently correlated failure modes; architectural diversity without epistemic independence can create false assurance.

## Study sequence

### Study 1 — Computational benchmark
Use frozen public-source cases and fresh holdout variants written independently of the detector/agent developers.

### Study 2 — Controlled human experiment
Accounting/audit participants review AI outputs under different architectures and evidence displays. Outcomes: error detection, reliance, confidence, time, and override quality.

### Study 3 — Field or design-partner pilot
Deploy a narrow workflow such as ICFR evidence review or agentic transaction assurance. Compare pre-specified quality, time and escalation metrics.

## Non-negotiable validity rule

Any case used to design prompts, detectors or reviewer logic becomes a development case and cannot serve as independent test evidence. Fresh, blinded holdouts are required for confirmatory claims.
