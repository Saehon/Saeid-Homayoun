# ECONOVA-S™ Scientific Assurance Standard

This document defines how ECONOVA-S™ classifies evidence, prevents overclaiming, audits autonomous research workflows, and decides whether a result may advance toward a scientific-discovery claim.

The canonical discovery protocol is defined in [`GOOGLE_INSPIRED_DISCOVERY_PROTOCOL.md`](GOOGLE_INSPIRED_DISCOVERY_PROTOCOL.md).

## Evidence classes

Every output must be labeled as one of:

1. **Theoretical** — mechanism or formal argument without empirical validation.
2. **Descriptive** — summary of observed data.
3. **Associational** — statistical relationship without credible causal identification.
4. **Predictive** — out-of-sample or forecasting performance.
5. **Causal** — effect estimate supported by a defensible identification strategy.
6. **Structural / equilibrium** — model-based economic mechanism with calibrated/estimated structure and validation.
7. **Replicated** — independently reproduced result under a documented protocol.

The system must not silently upgrade one class into another.

## Mandatory scientific gates

A claim may advance only if the relevant gates are satisfied.

### Literature Validation Gate
- theory and construct definitions linked to credible literature;
- competing explanations identified;
- contradictory evidence preserved;
- important references verified as real/retrievable;
- source provenance recorded.

### Co-Scientist Hypothesis Gate
- multiple candidate hypotheses considered where discovery is the goal;
- generation, reflection, ranking, evolution and meta-review logic recorded;
- ranking criteria frozen before final selection;
- self-ranking treated as search guidance, not truth;
- rejected hypotheses retained with reasons where practical.

### DAG / Systems Governance Gate
- theory mechanism mapped explicitly;
- confounders, mediators, moderators and timing recorded;
- information-availability chronology represented;
- evidence class justified before estimation;
- statistical fit cannot silently upgrade causal status.

### Construct Gate
- Variable DNA™ documented;
- timing, unit, transformation and missingness specified;
- alternative operationalizations considered.

### ERA Empirical Conversion Gate
- hypothesis translated into real data or clearly labelled simulation;
- executable code exists;
- estimand/model specified;
- evaluation metrics specified;
- robustness/falsification plan specified;
- replication/OOS path specified.

### Provenance Gate
- authoritative source recorded;
- information-availability date distinguished from fiscal/measurement date;
- source versions and hashes preserved where practical;
- tool/model versions recorded.

### Identification Gate
- explicit estimand;
- statement of what identifies the parameter;
- assumptions, threats and falsifiers documented;
- fixed effects or clustered errors never treated as causal identification by themselves.

### Search Integrity Gate
For AlphaEvolve-inspired or Computational Discovery search:
- scientific fitness frozen before search;
- no optimization for p-values alone;
- candidate lineage retained;
- failed candidates not silently erased;
- DiscoverySystem and ValidationSystem separated where feasible;
- holdout boundaries respected.

### Latent-Structure Gate
When AlphaFold-inspired latent-structure reasoning is used:
- latent structure clearly defined;
- exploratory vs identified status explicit;
- simpler baseline included;
- economic interpretation supplied;
- stability tested;
- external/OOS validation used where feasible.

### Robustness / Falsification Gate
- alternative measures/specifications;
- placebo or negative-control tests where meaningful;
- sensitivity analysis;
- chronology and leakage checks;
- alternative causal explanations;
- distribution-shift/OOS tests where relevant.

### Replication / OOS Gate
- temporal or external holdout where relevant;
- known facts replicated before extension where feasible;
- independent replication preferred for high-impact claims;
- material discrepancies preserved as results.

### AI-to-AI Adversarial Review Gate
The red-team must search for:
- omitted-variable bias;
- reverse causality;
- selection/survivorship bias;
- measurement error;
- look-ahead/data leakage;
- multiple testing and researcher degrees of freedom;
- construct drift;
- model instability;
- unsupported causal language;
- method-code mismatch;
- external-validity failure;
- welfare conflicts.

A second agent label alone does not establish independence.

### Science One Chain-of-Evidence Gate
Every material claim must have a recorded evidence chain satisfying:

1. **Completeness** — important claims have evidence.
2. **Correctness** — the evidence genuinely supports the claim.

Claim types include references, methods, numerical results, robustness statements and conclusions.

### CoE Audit Gate
Publication-grade work should verify:
- references are real and retrievable;
- reported results reproduce from code/inputs;
- executed code respects the frozen specification;
- manuscript method descriptions match code;
- final claims stay within evidentiary support.

### Economic Significance Gate
- magnitude interpreted in economically meaningful units;
- statistical significance not treated as sufficient.

### Welfare Gate
- private value distinguished from social value;
- externalities, distributional effects, privacy, market power and environmental effects considered when relevant.

### Reproducibility Gate
- code commit recorded;
- environment and dependencies recorded;
- data versions/hashes preserved;
- random seeds recorded where relevant;
- artifacts can be regenerated from documented inputs.

### Human Gate
- explicit human approval is required for any scientific-discovery claim;
- automated systems cannot self-authorize discovery;
- unresolved limitations must be recorded.

## Anti-p-hacking and anti-evaluator-gaming rule

ECONOVA-S™ does not optimize models, prompts, transformations, samples or estimators to manufacture statistical significance or exploit an evaluator. Published estimates may be used as replication benchmarks or priors, not targets to reverse-engineer.

## Closed-loop improvement boundary

Mirendil-inspired or other self-accelerating R&D loops may improve execution speed, code quality, model selection, evaluator reliability or research throughput. They may not rewrite:

- evidence-class definitions;
- discovery acceptance criteria;
- Human Gate requirements;
- provenance requirements;
- falsification requirements;
- licensing/security boundaries.

## Evidence Passport™ minimum fields

Each serious research run should preserve:

- question and hypotheses;
- hypothesis-tournament record;
- evidence sources;
- data versions and provenance;
- causal DAG;
- Variable DNA™;
- estimand and identification class;
- search/evolution lineage where applicable;
- latent-structure results where applicable;
- model/specification versions;
- code/environment information;
- results and uncertainty;
- robustness/falsification status;
- replication/OOS status;
- red-team findings;
- Chain-of-Evidence status;
- CoE Audit status;
- welfare interpretation;
- human decision.

## Machine-enforced discovery boundary

The repository defines:

- [`discovery/study_manifest.schema.json`](discovery/study_manifest.schema.json)
- [`discovery/validate_study_manifest.py`](discovery/validate_study_manifest.py)
- [`discovery/test_discovery_manifest.py`](discovery/test_discovery_manifest.py)

A study may not set `discovery_claim_allowed = true` unless the required gates and Human Gate are satisfied.

## Default public status

For current public prototypes and active v0.3 work:

```text
discovery_claim_allowed = false
```

That status changes only after applicable scientific gates have been evidenced and explicitly approved by a human reviewer.
