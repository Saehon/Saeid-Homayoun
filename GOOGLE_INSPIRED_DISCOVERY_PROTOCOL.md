# ECONOVA-S™ Google/DeepMind-Inspired Scientific Discovery Protocol

**Status:** Canonical research protocol for ECONOVA-S™ studies  
**Scope:** Scientific workflow and governance; not a claim of affiliation or external-system execution

## Purpose

This protocol operationalizes a rigorous scientific-discovery loop inspired by current work from Google Research, Google DeepMind, Science One, and adjacent autonomous-R&D systems while preserving ECONOVA-S™ as an independent research project.

External system names in this document describe **methodological inspiration unless the corresponding external system is actually executed and recorded in the Evidence Passport™**.

## Canonical discovery loop

```text
Research Goal
→ Literature Grounding
→ Co-Scientist-Style Hypothesis Tournament
→ DAG / Systems Governance
→ ERA-Style Empirical Conversion
→ Real Data + Code + Metrics
→ AlphaEvolve-Inspired Search
→ Computational Discovery Tournament
→ AlphaFold-Inspired Latent-Structure Search
→ Independent Replication / Holdout
→ AI-to-AI Adversarial Review
→ Science One Chain-of-Evidence
→ CoE Audit
→ Falsification
→ Economic / Welfare Interpretation
→ Human Gate
→ Controlled Learning / Evolution
```

The default state is:

```text
discovery_claim_allowed = false
```

No automated agent can change that state by itself.

---

## 1. Literature Grounding Gate

Before hypothesis generation, build a relevance-gated evidence prior from authoritative research and primary sources.

Minimum requirements:

- define the research question and scope;
- identify core theory and competing mechanisms;
- preserve contradictory literature rather than averaging it away;
- verify that cited sources exist;
- attach provenance to every important evidence item;
- distinguish peer-reviewed evidence, working papers, official data, and model-generated suggestions.

For ECONOVA-S™, FT50 and AJG/ABS 4*/4 literature is prioritized where relevant, with selected high-quality 3 journals added when substantively justified.

---

## 2. AI Co-Scientist-Style Hypothesis Tournament

Inspired by Google Research's AI co-scientist architecture, hypothesis generation should not be a single prompt. ECONOVA-S™ uses a role-separated tournament with the following logical functions:

1. **Generation** — propose competing hypotheses and mechanisms.
2. **Reflection** — critique internal coherence, assumptions, novelty, and plausibility.
3. **Ranking** — compare hypotheses using frozen scientific criteria.
4. **Evolution** — revise and recombine promising hypotheses.
5. **Proximity** — identify overlap, redundancy, and conceptual distance among hypotheses.
6. **Meta-review** — summarize debate, unresolved uncertainty, and the strongest surviving candidates.

### Frozen ranking dimensions

Each hypothesis should be scored on:

- theory coherence;
- novelty relative to grounded literature;
- falsifiability;
- empirical testability;
- data feasibility;
- identification feasibility;
- expected information gain;
- economic importance;
- welfare relevance;
- replication feasibility.

An Elo-like or pairwise ranking may be used as a search heuristic, but **self-ranking is not ground truth**.

Output: `hypothesis_tournament.json` plus a human-readable tournament report.

---

## 3. DAG / Systems Governance

Every surviving hypothesis must be mapped into an explicit causal/system structure before empirical execution.

Required objects:

- treatment/exposure or focal construct;
- outcome(s);
- confounders;
- mediators;
- moderators;
- feedback loops where relevant;
- measurement nodes;
- timing / information-availability nodes;
- plausible alternative causal paths;
- falsifiers and negative controls.

The DAG governs what may be called descriptive, predictive, associational, causal, or structural evidence.

A statistical model cannot upgrade its own evidence class.

---

## 4. ERA-Style Empirical Conversion

Inspired by Google Research's Empirical Research Assistance (ERA), each surviving hypothesis must be translated into executable empirical software.

Each hypothesis requires:

- real data source(s) or a clearly labelled simulation;
- Variable DNA™ for every construct;
- exact sample construction;
- chronology rules;
- estimand;
- empirical model;
- code;
- evaluation metrics;
- robustness tests;
- falsification tests;
- replication/OOS design;
- expected failure modes.

The deliverable is not prose alone. It must include runnable code and a machine-readable empirical manifest.

---

## 5. AlphaEvolve-Inspired Search

Inspired by AlphaEvolve, ECONOVA-S™ may evolve candidate algorithms, measures, estimators, prompts, model architectures, and specifications using automated evaluators.

### Search objects

Permitted search objects include:

- variable construction;
- measurement functions;
- forecasting models;
- estimators;
- feature sets;
- algorithms;
- prompt/program logic;
- robustness procedures;
- simulation policies.

### Frozen scientific fitness

Search must optimize a pre-specified scientific fitness function rather than p-values alone. Candidate dimensions include:

- OOS performance;
- theory consistency;
- causal credibility;
- robustness;
- economic magnitude;
- parsimony;
- interpretability;
- reproducibility;
- welfare relevance;
- computational cost.

DiscoverySystem and ValidationSystem should be separated wherever feasible.

---

## 6. Computational Discovery Tournament

Inspired by Google Research's Computational Discovery approach, multiple executable candidate solutions should be generated and evaluated in parallel rather than sequentially accepting the first plausible model.

Requirements:

- parallel or batched candidate generation;
- frozen evaluator(s);
- immutable raw evaluator outputs;
- explicit exploration vs exploitation policy;
- no silent deletion of failed candidates;
- holdout evidence not exposed to the generator where feasible;
- retained lineage from parent candidate to evolved candidate.

Output: candidate registry, evaluator scores, lineage graph, winning/retained candidates, and rejected-candidate reasons.

---

## 7. AlphaFold-Inspired Latent-Structure Reasoning

AlphaFold is a domain-specific biological system; ECONOVA-S™ does **not** claim to run AlphaFold for economics. Instead, the project borrows the methodological idea that difficult scientific problems may require inference over hidden structure rather than direct surface prediction.

Possible economic latent structures include:

- hidden factor systems;
- latent firm types;
- unobserved regimes;
- network/community structure;
- latent risk dimensions;
- temporal state transitions;
- hidden causal mechanisms;
- hierarchical construct structure.

Any latent structure must be:

1. statistically identified or clearly labelled exploratory;
2. economically interpretable;
3. compared with simpler baselines;
4. tested OOS or externally where possible;
5. stress-tested for instability;
6. linked back to theory and observable implications.

---

## 8. Science One Chain-of-Evidence™ Layer

Inspired by Google Research's Science One Framework, verifiability is an architectural property rather than final proofreading.

Every material research claim must satisfy two requirements:

### Completeness
Every important claim has an attached evidence chain.

### Correctness
The attached evidence genuinely supports the claim.

Supported claim types include:

- literature/reference claims;
- data/source claims;
- reported numerical results;
- method descriptions;
- model-performance statements;
- robustness statements;
- causal interpretations;
- final conclusions.

Evidence may point to:

- verified literature;
- source data and hashes;
- code commit;
- executed logs;
- result tables;
- evaluator outputs;
- replication outputs;
- red-team reports.

No citation should be generated solely from model memory.

---

## 9. CoE Audit

Every publication-grade study should run a post-hoc Chain-of-Evidence audit inspired by Science One's CoE Audit.

Minimum checks:

1. **Reference verification** — does each citation correspond to a real retrievable source?
2. **Score/result verification** — can reported numerical outputs be reproduced from code and inputs?
3. **Specification integrity** — does the executed code respect the frozen protocol and avoid evaluator leakage or forbidden shortcuts?
4. **Method-code alignment** — does the manuscript accurately describe what the code actually executed?
5. **Claim-evidence alignment** — does each substantive claim stay within what its evidence supports?

A failed CoE Audit blocks a scientific-discovery claim.

---

## 10. Mirendil-Inspired Closed-Loop R&D

Mirendil is not a Google product. ECONOVA-S™ uses **Mirendil-inspired** language only for the general idea of accelerating the R&D loop through automation, evaluation, observability, and recursive improvement.

Canonical loop:

```text
Propose
→ Build
→ Execute
→ Evaluate
→ Diagnose Failure
→ Revise / Mutate
→ Re-run
→ Compare
→ Preserve Improvement
```

### Containment rule

Self-improvement may optimize execution quality, model selection, code quality, evaluator performance, or research throughput, but it must not rewrite:

- scientific acceptance criteria;
- human-approval requirements;
- provenance rules;
- falsification requirements;
- evidence-class definitions;
- licensing / security boundaries.

AI may improve the research process. It may not relax the constitution governing the research process.

---

## 11. AI-to-AI Independent Review

AI-to-AI review must preserve disagreement and record independence strength.

A stronger review uses one or more of:

- different model/model family;
- isolated context;
- separate code path;
- separate retrieval context;
- blinded holdout;
- independent Evidence Passport reconstruction;
- independent replication;
- external human reviewer.

The system must never equate role separation with true independence automatically.

```text
agent_consensus != scientific_truth
```

---

## 12. Falsification Gate

Before a claim advances, the system should attempt to make it fail.

Where relevant, require:

- placebo tests;
- negative controls;
- alternative operationalizations;
- alternative samples;
- sensitivity bounds;
- multiple-testing control;
- temporal stability tests;
- distribution shift / OOS tests;
- alternative causal explanations;
- specification stress tests.

Failure is a valid scientific result and must be preserved in the Evidence Passport™.

---

## 13. Human Gate

No automated system can authorize a scientific discovery.

Human review must assess:

- theory and contribution;
- construct validity;
- identification credibility;
- provenance;
- search integrity;
- reproducibility;
- robustness/falsification;
- Chain-of-Evidence integrity;
- economic significance;
- welfare interpretation;
- overclaiming risk.

Only a human may change a study from `candidate` to `approved_for_scientific_claim`, and only after all applicable gates are evidenced.

---

## Mandatory per-study artifacts

Every ECONOVA-S™ publication-grade study should contain:

```text
01_RESEARCH_GOAL.md
02_LITERATURE_GROUNDING.md
03_HYPOTHESIS_TOURNAMENT.json
04_CAUSAL_DAG.md
05_VARIABLE_DNA.csv
06_EMPIRICAL_MANIFEST.json
07_DISCOVERY_SEARCH.json
08_LATENT_STRUCTURE.md
09_REPLICATION_REPORT.md
10_RED_TEAM_REPORT.md
11_FALSIFICATION_REPORT.md
12_CHAIN_OF_EVIDENCE.json
13_COE_AUDIT.json
14_EVIDENCE_PASSPORT.json
15_HUMAN_GATE.md
```

Not every study needs every advanced method, but any omitted artifact or gate should record why it is not applicable.

---

## External-method provenance

The conceptual mapping above is grounded in public descriptions of:

- Google Research AI co-scientist — specialized Generation, Reflection, Ranking, Evolution, Proximity, and Meta-review agents for iterative hypothesis improvement.
- Google Research Empirical Research Assistance (ERA) — AI-assisted construction of empirical software for hypothesis evaluation and computational discovery.
- Google DeepMind AlphaEvolve — evolutionary algorithm discovery/optimization using LLM generation and automated evaluators.
- Google Research Computational Discovery — built with ERA and AlphaEvolve for large-scale computational search.
- Google DeepMind AlphaFold — used here only as inspiration for hidden/latent-structure reasoning and rigorous benchmarking, not as an economics model.
- Google Research Science One Framework — Chain-of-Evidence and CoE Audit for verifiable autonomous research.
- Mirendil — referenced only as inspiration for self-accelerating R&D loops; no affiliation or execution is implied.

## Final rule

> **Generate broadly. Ground literature. Convert hypotheses to executable tests. Search scientifically. Discover hidden structure cautiously. Preserve every evidence chain. Attack the result. Reproduce it. Let humans decide.**
