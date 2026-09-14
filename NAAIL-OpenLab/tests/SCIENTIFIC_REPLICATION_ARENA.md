# NAAIL Scientific Replication Arena™

The Scientific Replication Arena is the NAAIL test layer for evaluating published empirical methods, replication packages, AI/ML pipelines, and causal designs against a common evidence-governed protocol.

## Test matrix

| Test family | Core question | Typical outputs |
|---|---|---|
| Replication | Can the reported result be regenerated? | table/figure/statistic deltas, logs |
| Independent reproduction | Does the conclusion survive a clean implementation? | coefficient/sign/effect comparison |
| Robustness | Is the conclusion stable to reasonable alternatives? | specification grid, stability score |
| Causal verification | Does identification survive diagnostics/falsification? | placebo, pretrend, sensitivity results |
| ML/AI verification | Is performance real and leakage-free? | OOS metrics, calibration, ablation |
| Temporal validation | Does the model/method survive future periods? | rolling/holdout performance |
| Cross-dataset validation | Does the conclusion generalize? | external-validation deltas |
| Digital Twin | Does the method recover known ground truth? | FP/FN, bias, coverage, stability |
| Adversarial review | Can a Critic invalidate the claim? | challenge-response evidence log |
| Evidence governance | Can every claim be traced to lawful evidence? | Chain-of-Evidence / Evidence Passport |

## Benchmark families
The initial external benchmark registry is maintained in:
`../benchmarks/ft50_abs4/registry.json`

The governing protocol is:
`../benchmarks/ft50_abs4/BENCHMARK_PROTOCOL.md`

The external-source policy is:
`../external/FT50_ABS4_SOURCE_POLICY.md`

## Comparative estimator arena
Where substantively justified, NAAIL should compare rather than assume a single preferred estimator. Examples include:

### Causal designs
- TWFE;
- modern staggered-DiD estimators;
- event-study alternatives;
- synthetic approaches;
- doubly robust estimators;
- DML when identification assumptions are appropriate.

### Prediction / ML
- linear/logistic baselines;
- tree ensembles;
- gradient boosting;
- domain language models;
- embeddings + conventional estimators;
- LLM / multi-agent approaches.

### Textual accounting / audit
- dictionary measures;
- traditional NLP baselines;
- FinBERT/domain transformers;
- sentence embeddings;
- LLM scoring;
- KIWI™ / NAAIL multi-agent analysis.

## Professional audit metrics
When the benchmark concerns auditing, CAM/KAM, ICFR, assurance, or professional judgment, include:
RPA, AA, EG, PS, DS, and DIST.

## Decision rule
No single metric is sufficient. A benchmark may improve predictive performance while failing causal validity, rights/provenance, evidence grounding, or professional judgment. Such a result cannot be promoted as a scientific improvement without qualification and Human Gate approval.
