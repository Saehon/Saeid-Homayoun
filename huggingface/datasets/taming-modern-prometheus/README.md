---
pretty_name: Taming the Modern Prometheus - Agentic Financial Assurance Benchmark
language:
- en
license: other
task_categories:
- text-classification
- question-answering
tags:
- accounting
- auditing
- internal-control
- corporate-governance
- cam
- esg
- sustainability
- agentic-ai
- ai-governance
size_categories:
- n<1K
---

# Taming the Modern Prometheus — Agentic Financial Assurance Benchmark

A small, transparent benchmark for evidence-grounded agentic workflows in financial assurance.

## Contents

- 13 labelled cases.
- 3 public-derived Microsoft aggregate financial checks.
- 10 synthetic audit, ICFR, CAM, governance, ESG, adversarial, and reproducibility cases.
- Required evidence, red-team challenge, target assertion, and non-compensatory gate for each case.

The public-derived rows are based on the Microsoft demonstration in the linked GitHub repository. The synthetic rows are not real company findings and must not be treated as audit evidence or ESG disclosures.

## Files

- agentic_assurance_benchmark.csv
- provenance.json
- GITHUB_SOURCE.md

## Use

This dataset is intended for education, academic research, simulation, and benchmark development. Run deterministic checks before model evaluation and retain model, prompt, tool, evidence, and human-gate metadata.

## License

The original benchmark schema, synthetic cases, code, and documentation remain under the research/non-commercial license of the source repository. Third-party public-source terms remain applicable. Do not redistribute licensed standards text or proprietary ESG ratings through this dataset.

Dataset page: https://huggingface.co/datasets/SADHON/taming-modern-prometheus-assurance

Source repository: https://github.com/Saehon/Saeid-Homayoun
