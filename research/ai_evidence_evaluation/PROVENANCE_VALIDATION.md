# Research Run Provenance — Model-Neutral Validation

This module is an **offline integrity inspector** for the financial-AI research pipeline. It accepts documented local model-output records while keeping prediction content and API credentials out of the public metadata report. It does **not** contact OpenAI, Anthropic or Google.

## Reproduce the synthetic protocol

From the repository root using Python 3.11+:

```bash
python -m research.ai_evidence_evaluation.validate_run \
  --manifest research/ai_evidence_evaluation/examples/provenance_manifest.json \
  --out reports/provenance_synthetic.json
python -m unittest discover -s research/ai_evidence_evaluation/tests -v
```

The provided manifest describes **two duplicate demonstrations of a handwritten synthetic fixture**, *not two model runs*. This is solely a negative/positive contract test. Input file SHA-256, row uniqueness, status consistency, declared run/model identity, token counts, UTC timestamps and paths are checked.

## Independent evaluation readiness

Researchers may inspect a local, lawfully obtained **declared provider output** by supplying a separate manifest under local controlled storage and adding `--inspect-observed`. That gate requires an explicit `data_transfer_authorized=true` declaration, but it **cannot verify consent or source rights**. Do not run it on restricted data without institutional approval. No output is described as provider-authenticated or independently approved by this module.

Every observed run should include a signed/rightful source declaration, exact provider/model/version metadata, token/latency costs (with source and limitations), prompt/template digest, reference and prediction hashes, and independent human adjudication documented outside this script. The published code deliberately leaves `model_performance_claim_permitted=false` and `independent_validation_status=NOT_VERIFIED` in all output reports.

## Scientific limits

- Matching SHA-256 digests confirm **local file integrity**, not the authenticity of a provider's API response.
- Equal case counts do not establish the same case IDs or equal sampling. Pairing and answer grades require separate controlled comparison and human-reviewed gold data.
- This inspection has no LLM-as-a-judge and no paid inference. It cannot establish financial statement accuracy, IFRS compliance or auditing effectiveness.
- The test files, model identifiers and timestamps in the repository are synthetic examples.
- Do not commit confidential financial statements, student information, private model responses or API keys.

See the [benchmark crosswalk](../LLM_BENCHMARKS_AND_EVALUATION.md) and [research evidence policy](../RESEARCH_EVIDENCE_POLICY.md) for academic standards.
