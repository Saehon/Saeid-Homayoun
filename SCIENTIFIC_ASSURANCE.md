# ECONOVA-S™ Scientific Assurance Standard

This document defines how ECONOVA-S classifies evidence, prevents overclaiming and decides whether a result may advance toward a scientific-discovery claim.

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

A claim may advance only if the relevant gates are satisfied:

### Literature Gate
- theory and construct definitions linked to credible literature;
- competing explanations identified;
- evidence conflicts preserved.

### Construct Gate
- Variable DNA™ documented;
- timing, unit, transformation and missingness specified;
- alternative operationalizations considered.

### Provenance Gate
- authoritative source recorded;
- information-availability date distinguished from fiscal/measurement date;
- source versions and hashes preserved where practical.

### Identification Gate
- explicit estimand;
- statement of what identifies the parameter;
- assumptions, threats and falsifiers documented;
- fixed effects or clustered errors never treated as causal identification by themselves.

### Search Integrity Gate
- specification search governed by frozen scientific fitness criteria;
- no optimization for p-values alone;
- DiscoverySystem and ValidationSystem separated where feasible.

### Robustness / Falsification Gate
- alternative measures/specifications;
- placebo or negative-control tests where meaningful;
- sensitivity analysis;
- chronology and leakage checks.

### Replication / OOS Gate
- temporal or external holdout where relevant;
- known facts replicated before extension where feasible;
- independent replication preferred for high-impact claims.

### Economic Significance Gate
- magnitude interpreted in economically meaningful units;
- statistical significance not treated as sufficient.

### Welfare Gate
- private value distinguished from social value;
- externalities, distributional effects, privacy, market power and environmental effects considered when relevant.

### Human Gate
- explicit human approval is required for any scientific-discovery claim.

## Anti-p-hacking rule

ECONOVA-S does not optimize models, prompts, transformations, samples or estimators to manufacture statistical significance. Published estimates may be used as replication benchmarks or priors, not targets to reverse-engineer.

## Adversarial review

The Scientific Red-Team Agent should actively search for:

- omitted-variable bias;
- reverse causality;
- selection and survivorship bias;
- measurement error;
- look-ahead and data leakage;
- multiple testing and researcher degrees of freedom;
- model instability;
- external-validity failure;
- equilibrium/reflexivity effects;
- private-versus-social-value conflicts.

## Evidence Passport™ minimum fields

Each serious research run should preserve:

- question and hypothesis;
- evidence sources;
- data versions and provenance;
- Variable DNA™;
- estimand and identification class;
- model/specification versions;
- code/environment information;
- results and uncertainty;
- robustness/falsification status;
- replication/OOS status;
- red-team findings;
- welfare interpretation;
- human decision.

## Default public status

For the current public prototypes and active v0.3 study:

```text
discovery_claim_allowed = false
```

That status should change only after the relevant scientific gates have been evidenced and explicitly approved by a human reviewer.
