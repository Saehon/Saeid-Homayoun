# Scientific Discovery Master Architecture v2.0 — Systems Thinking + Co-Scientist + Structure + Evolution + FRANKENSTEIN

**Additive rule:** preserve every existing registry, pilot, dataset, benchmark, document, agent and negative result. v2.0 reorganizes and strengthens the system; it does not delete or overwrite prior scientific assets.

## 1. System purpose

Build a reproducible scientific-discovery infrastructure for accounting, auditing, financial reporting, ICFR, CAM/KAM, fraud/AAER, IFRS/ESEF and ESG/ESRS/VSME research.

The system separates five questions:
1. **What problem matters?** — Systems Thinking.
2. **What competing explanations should be tested?** — Co-Scientist.
3. **What evidence structure links constructs to observations?** — AlphaFold-inspired structure-first reasoning.
4. **Which candidate method/design survives objective evaluation?** — AlphaEvolve-style evolutionary search.
5. **Can heterogeneous agents/tools be integrated without losing control?** — FRANKENSTEIN orchestration.

## 2. Systems Thinking control plane

Problem → boundary → stakeholders → constructs → causal mechanisms → evidence → feedback loops → dependencies → failure modes → measurable outcomes.

Every project begins with a system map before selecting an AI model. Technology is an intervention in the research system, not the research question.

### Required system card
- focal accounting/audit problem;
- decision maker/user;
- unit of analysis;
- construct(s);
- evidence sources;
- temporal boundary;
- feedback loops;
- possible confounders/leakage;
- human judgment point;
- intended research contribution.

## 3. Theory and replication spine

FT50/ABS4 theory/prior evidence
→ verified paper
→ verified replication package
→ reproduce baseline where access permits
→ freeze baseline
→ document unavailable/licensed inputs
→ extend only after baseline provenance is established.

### Primary Management Science replication anchor
deHaan, de Kok, Matsumoto & Rodriguez-Vazquez, “How Resilient Are Firms’ Financial Reporting Processes?”
Replication package: https://github.com/TiesdeKok/mnsc.2023.4670

Adopt its reproducibility logic:
0_data + 1_code → 2_pipeline → 3_output/results.

Extension mapping:
0_data = regulatory/academic Gold evidence;
1_code = deterministic baseline + econometrics + agent adapters;
2_pipeline = immutable derived evidence/feature tables;
3_output = tables, logs, metrics, falsification and human-validation artifacts.

Do not claim an end-to-end replication has been completed until all required licensed/raw inputs have actually been obtained and the original outputs reproduced.

## 4. Co-Scientist hypothesis engine

Research objective + prior evidence
→ Generate
→ Critique
→ Rank by information value
→ Refine
→ Diversify
→ Experiment proposal
→ Falsification criteria.

Every focal hypothesis must have at least one credible rival explanation.

Examples:
- true ICFR weakness vs complexity vs disclosure artifact vs temporal leakage;
- true CAM/KAM change vs wording drift vs auditor-template change;
- true ESG disclosure quality vs report length vs boilerplate;
- true IFRS judgment inconsistency vs taxonomy-extension artifact.

Rejected hypotheses remain in the registry.

## 5. AlphaFold-inspired evidence-structure layer

This is an analogy to **structure-first scientific reasoning**, not a claim to reproduce AlphaFold.

Build a typed Evidence Graph:
Company
→ Filing/Report
→ Statement/Note
→ XBRL/iXBRL/ESRS/VSME datapoint
→ Account/Disclosure
→ Accounting characteristic
→ Audit assertion
→ Internal control
→ Material weakness
→ Audit procedure/opinion
→ CAM/KAM
→ PCAOB/AAER outcome
→ Standard/requirement
→ source evidence.

For every AI claim record:
claim → evidence IDs → structural relations → confidence/uncertainty → contradictory evidence → validation status.

## 6. AlphaEvolve-style experiment engine

Generate a population of candidate scientific solutions:
deterministic rules; econometric baseline; classical ML; transformer/NLP; RAG; GraphRAG; single-agent; multi-agent; hybrid systems.

Automated evaluators score candidates on locked evidence and predeclared metrics.

### Fitness vector
- construct validity;
- predictive validity;
- calibration;
- evidence coverage;
- citation correctness;
- robustness;
- out-of-time/out-of-company generalization;
- reproducibility;
- interpretability;
- latency;
- cost;
- human-review burden.

### Anti-overfitting rule
Evolution/search may use training/development evidence only. Locked holdout evidence is evaluated at defined gates. Candidate proliferation, prompt search and model selection must be logged.

## 7. FRANKENSTEIN integration layer

FRANKENSTEIN connects heterogeneous components while preserving scientific controls.

Gold data / SEC / PCAOB / AAER / ESEF / ESRS / VSME
→ Databricks/Delta
→ Evidence Graph
→ provider-neutral task contract
→ OpenAI / Claude / Gemini / Microsoft / open-source agents
→ domain agents
→ deterministic controls
→ Reviewer/Falsification
→ human gate.

Provider identity is blinded where feasible during comparative evaluation.

## 8. Gold data layer

### Authoritative/academic anchors
- SEC EDGAR/CompanyFacts/XBRL;
- Stanford EDGAR Filings Dataset (SEFD);
- PCAOB machine-readable inspection data;
- SEC AAER + USC AAER academic dataset;
- ESMA ESEF/iXBRL;
- EFRAG ESRS/VSME digital structures;
- controlled CAM/KAM and ICFR datasets with documented provenance.

### Platform roles
GitHub = code/provenance/replication manifests.
Hugging Face = public datasets/models/benchmarks.
Kaggle = executable public notebooks/benchmarks.
Databricks/Delta = versioned evidence/data engineering.
MLflow = experiment/tracing/evaluation lineage.
Google Drive = controlled research files/manuscripts.
arXiv = frontier-method discovery.

A platform copy is never assumed identical to source evidence. Preserve source ID, version, snapshot hash and transformation commit.

## 9. Domain programs

A. SEC/XBRL verification
B. Financial-reporting resilience/replication
C. Audit assertions
D. ICFR/material weaknesses
E. CAM/KAM
F. Fraud/AAER
G. IFRS/ESEF judgment and tagging
H. ESG/ESRS/VSME assurance
I. Evidence/citation verification
J. Cross-provider evaluation
K. Student research replication.

Existing Microsoft SEC/XBRL Pilot 001 remains preserved as Program A’s first executable pilot.

## 10. Scientific falsification stack

Data QA
→ deterministic accounting checks
→ baseline replication
→ evidence verification
→ standards/rule checks
→ blind cross-agent challenge
→ Reviewer
→ Falsification Agent
→ independent rerun
→ human expert.

Failure taxonomy:
data; linkage; retrieval; temporal leakage; construct; reasoning; arithmetic; standards; unsupported claim; citation; calibration; provider disagreement; reproducibility.

## 11. Human governance

Final consequential judgment remains human.

States:
APPROVE / REJECT / NEEDS_MORE_EVIDENCE / REPLICATE.

Record rationale, evidence reviewed, unresolved uncertainty and whether the human reviewer saw provider identity.

## 12. End-to-end scientific discovery loop

Problem
→ Systems map
→ FT50/ABS4 theory
→ replication baseline
→ Co-Scientist competing hypotheses
→ Evidence Graph
→ candidate experiment population
→ AlphaEvolve-style search
→ FRANKENSTEIN orchestration
→ multi-agent execution
→ deterministic checks
→ blind falsification
→ independent replication
→ human validation
→ manuscript/benchmark
→ outcome learning
↺ failures and contradictions return to the hypothesis pool.

## 13. Reproducibility identity

Every result must be traceable by:
research_question_id
+ hypothesis_id
+ dataset_id
+ source_record_id
+ source_version
+ snapshot_hash
+ transformation_commit
+ code_commit
+ experiment_id
+ provider/model/version
+ prompt/config hash
+ evaluator version
+ human decision.

## 14. Management Science research design

The scientific contribution is not “using many agents.” The contribution is the design and evidence on how **structured scientific discovery and falsification change the reliability, efficiency and governance of AI-enabled financial reporting and assurance research**.

Primary empirical design:
1. reproduce a published financial-reporting baseline using a verified replication package;
2. construct Gold evidence from public/regulatory data where possible;
3. introduce controlled AI interventions;
4. compare candidate architectures on identical evidence/tasks;
5. lock holdout evidence;
6. measure accuracy, calibration, evidence coverage, false positives/negatives, cost/time and human-review burden;
7. falsify with rival hypotheses and independent reruns;
8. report negative results.

## 15. Non-deletion governance

- preserve all prior artifacts;
- version superseded designs;
- never rewrite historical results;
- preserve failures and negative results;
- add adapters instead of provider-specific forks of domain logic;
- require explicit authorization for destructive operations.

## 16. Core principle

**Preserve → Map the System → Replicate → Hypothesize → Structure Evidence → Evolve Experiments → Orchestrate → Challenge → Falsify → Replicate Again → Human Judge → Publish → Learn**

Version 2.0 — 2026-09-25.
