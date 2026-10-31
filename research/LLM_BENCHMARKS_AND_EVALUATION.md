# Evaluation methods and benchmarking governance

## Purpose

NAAIL evaluates evidence-grounded financial reasoning, audit-related judgments, and AI-assisted professional research with **task-specific rubrics, reproducible protocols, and documented limits**. This page is a methodological crosswalk—not an endorsement by any model provider or a claim that NAAIL has run the benchmark datasets listed below.

**Status (2026-10-31):** the public cross-model evaluation script uses **only five handwritten synthetic cases and synthetic outputs**. It makes no GPT/Claude/Gemini performance claim. No external model was called in the public CI.

## Benchmark and evaluation framework crosswalk

| Framework | What it contributes | Application to accounting / auditing | Status and constraints |
|---|---|---|---|
| [OpenAI evaluation practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Task-specific rubrics, code vs human vs model graders, grader calibration, error analysis | Numerical answer correctness, wrong reporting periods, unsupported citations and abstentions | **Methodology reference only.** OpenAI's Evals platform documentation indicates a 2026 deprecation; do not build a new production dependency on a sunset API |
| [Anthropic test and evaluation guidance](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) | Success criteria, graded task scenarios, edge cases, calibration to human judgments | Audit evidence review, ICFR control checks, IFRS/ESG reasoning ambiguity | **Methodology reference only.** No Claude scores asserted |
| [Google Gen AI evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview) | Adaptive/static rubrics, deterministic and rubric-based scoring, comparable model evaluations | Financial statement reasoning, materiality and evidence anchoring | **Methodology reference only.** No Gemini scores asserted |
| [FinanceBench (Patronus AI)](https://huggingface.co/datasets/PatronusAI/financebench) | Open-book financial QA with answer and evidence strings | Domain QA and evidence consistency | The public set has **150 examples** under **CC BY-NC 4.0**, subject to attribution and non-commercial terms; the published larger corpus is not fully open. **No FinanceBench data copied here** |
| [UK AI Security Institute Inspect](https://inspect.aisi.org.uk/) | Composable datasets, agents, tools, scorers, traces and eval inspection | Reproducible tool-using audit agents and adversarial agent traces | This NAAIL demo does **not** embed or run Inspect |
| [Stanford HELM](https://github.com/stanford-crfm/helm) | Multi-metric, transparent evaluation across tasks/models | Comparability, efficiency, safety and domain robustness | HELM announced **maintenance mode June 1, 2026**; use as methodology/reference, not an assumed maintained integration |
| [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | Reusable tasks, metrics, model adapters and benchmark configuration | Reproducibility reference for future controlled finance/evidence tasks | Its 2026 interface has evolved; any integration requires version-pinned testing and task-license review |

### Scientific reference

Islam et al. (2023), *FinanceBench: A New Benchmark for Financial Question Answering*, [arXiv:2311.11944](https://arxiv.org/abs/2311.11944). **NAAIL does not claim authorship of FinanceBench.** The upstream research and dataset must be attributed to the actual authors and Patronus AI; merely hosting an upstream copy is not authorship.

## NAAIL evaluation dimensions

| Axis | Operational metric | Failure class | Validation needed |
|---|---|---|---|
| Financial accuracy | Numeric within pre-registered currency/scale/tolerance; exact categorical answers | Sign, currency, denominator, timing, GAAP/IFRS scope | Independent finance-domain reference answer |
| Grounding | Citation ID coverage **and** evidence text entailment | Fabricated source, stale evidence, unsupported inference | Blind human adjudication and evidence provenance |
| Selective accuracy | Accuracy among answered cases plus *coverage* and *abstention rate* | Selective refusal, silent error | Report all denominators |
| Agentic process | Correct tool selection, allowed system scopes, complete immutable traces | Missing tools, tool misuse, cross-tenant access | Tool/environment simulation plus separate reviewer |
| Professional judgment | Human approval and explicit reviewer responsibility | AI self-approval of audit conclusions | Independent accountant or auditor approval |
| Fairness/robustness | Stratification by accounting task, company/sector/year, jurisdiction and difficulty | Measurement bias, data contamination | Representative holdout and uncertainty |
| Efficiency | Token counts, latency, cost per task, uncertainty about billing | Cost overrun, prompt inflation, provider-specific counts | Recorded genuine run manifests and invoiced/usage evidence |

**Do not collapse these dimensions into one marketing "AI accuracy" score.** The synthetic Python test reports only internal scoring contracts and case-level discrepancies; citation ID matching is **not** document entailment.

## Model-neutral experiment contract (not yet executed)

1. Freeze a scoped study design before calling any provider: task domains, source-rights register, model IDs, temporal evidence requirements, split and metric definitions.
2. Build **expert-labelled, licensed** cases independently from model outputs, preserving blind labels and reviewer disagreements. Mark ambiguous IFRS/audit matters as judgment-dependent rather than mechanically right/wrong.
3. Use the *same admissible evidence and equivalent task instructions* for GPT, Claude, Gemini and open models, with vendor-specific adaptations logged.
4. Capture actual provider/model/version, prompt template and input hashes, run timestamp, temperature/sampling configuration, input/output token counts, error/timeout status and source-based costs.
5. Score numeric correctness, groundedness, abstentions, failure categories and human adjudication. Use paired case-level analysis, uncertainty estimates when sampling permits, and reviewer independence.
6. Publish only license-safe summaries and reproducible, redacted code, plus an **honest validation status**. Keep regulated/restricted data and private methods out of public GitHub.

**Minimum release standard:** independently inspected code; permitted test data; frozen methods; completed true model-inference artifacts; a documented human review and no misleading affiliations or scientific claims.

## What is implemented in this repository

- [Deterministic answer/evidence evaluator](ai_evidence_evaluation/evaluate.py): hand-written synthetic cases, conservative numerical matching and explicit missing/abstention failures.
- [Paired offline run comparison](ai_evidence_evaluation/compare_runs.py): compares two synthetic case-result files on identical gold IDs; reports case-level failure patterns, domain splits, paired groundedness differences and SHA-256 input hashes.
- [Tests](ai_evidence_evaluation/tests/): negative/adversarial assertions; no external dependencies or API secrets.
- [Reproducibility workflow](../.github/workflows/scientific-python-reproducibility.yml): CI checks and JSON artifacts, with no paid API calls.
