# Architecture

## Knowledge Core
What the system can retrieve and cite: standards metadata, evidence, ontology, enterprise context, research literature and provenance.

## Technique Core
Executable methods: accounting calculations, valuation, econometrics, ML, simulation, reconciliation and deterministic controls.

## Science Core
Scientific reasoning: hypothesis generation, experiment design, causal logic, robustness, replication and evaluation protocols.

## Adversarial / GAN Core
Alternative generation, falsification, contradictory-evidence search, counterfactuals, stress tests and synthetic-case generation. Classical GANs are optional techniques inside this broader core.

## Agentic Layer
Task decomposition, routing, provider selection, reviewer/falsifier assignment and human gates.

## Value Core
Consequence simulation after compliance screening: financial and six-capital value effects, assurance implications and realized-outcome learning.

## System contract

```text
Economic Event / User Question
          |
          v
    Agentic Router
          |
     +----+----+
     |         |
Knowledge   Science
     |         |
     +----+----+
          |
      Technique
          |
     Adversarial
          |
      Evaluator
          |
   Digital Twin / Value
          |
     Human Approval
          |
        Action
          |
    Outcome / Learning
```

## Provider policy

Foundation models are accessed through adapters. No business rule should depend on one provider name. Routing should optimize quality, risk, cost and latency.

## Evidence policy

Every material claim should resolve to:

```text
claim -> rule/standard reference -> source evidence -> calculation -> reviewer status
```

No generated conclusion is final merely because multiple LLMs agree.
