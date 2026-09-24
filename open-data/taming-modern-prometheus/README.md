# Agentic Financial Assurance Benchmark

**Dataset:** Taming the Modern Prometheus v0.1.0  
**Rows:** 13  
**Purpose:** small, transparent benchmark for evidence gates and falsification in accounting, auditing, ICFR, CAM, governance, ESG/sustainability, adversarial, and reproducibility workflows.

## Composition

| Segment | Rows | Meaning |
|---|---:|---|
| Public-derived | 3 | Recomputed from the existing Microsoft financial-data demonstration in this repository and its SEC provenance record |
| Synthetic | 10 | Controlled teaching and research scenarios; not real Microsoft findings, not real audit evidence, and not real ESG disclosures |

The Microsoft rows use only public aggregate financial figures already stored in [open-data/microsoft-demo-001](../microsoft-demo-001/). They do **not** make claims about Microsoft's internal controls, audit quality, ESG performance, or management assertions.

## Columns

- source_type: public_derived or synthetic.
- source_anchor: file or synthetic-case identifier.
- claim_or_event: proposition to test.
- benchmark_label: expected outcome (pass, review, or fail).
- expected_gate: non-compensatory gate that should control the result.
- required_evidence: minimum evidence packet.
- red_team_challenge: falsification question.
- target_assertion: accounting/audit assertion or governance target.
- synthetic_flag: 0 for public-derived rows and 1 for synthetic rows.

## Run

~~~text
python open-data/taming-modern-prometheus/validate.py
~~~

The validator uses only the Python standard library and checks row count, stable IDs, required fields, source labels, and the public/synthetic split. The benchmark is intentionally small enough to inspect manually before attaching an AI provider.

## Suggested research design

1. Give the same evidence packet to each provider or open model.
2. Require every agent to output a claim, evidence locations, calculations, uncertainty, and gate decision.
3. Run the deterministic validator before any language-based score is considered.
4. Send every review or fail result to an independent reviewer agent.
5. Record provider/model version, prompt version, tool calls, run ID, and human approval.
6. Report false-pass, false-stop, unsupported-claim, contradiction, and human-override rates.

## Provenance and licensing

- Original benchmark schema, synthetic scenarios, validation code, and documentation are covered by the repository's research/non-commercial license.
- The three public-derived rows are linked to the SEC-originated Microsoft demonstration; the originating source terms remain applicable.
- This is a publication-ready small sample, not a substitute for a full SEC/XBRL panel, commercial audit dataset, proprietary ESG ratings, or licensed standards text.
