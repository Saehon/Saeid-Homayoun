# GPT vs Claude vs IBM Granite — Controlled Benchmark Plan

## Question

Which provider/model configuration should serve as the **primary reviewer**, **independent challenger**, and **fallback** for the ICFR Evidence Review Agent?

## Fixed evaluation contract

Every model receives the same:

- control definition
- synthetic evidence
- deterministic result
- system rule that evidence is untrusted data
- prohibition on final professional approval
- structured output schema

No provider receives extra facts or a more favorable prompt.

## Required measurements

Per case and provider:

- seeded exception detected: yes/no
- evidence sufficiency
- risk triage
- supported findings
- potential exceptions
- evidence-basis validity
- unsupported claim count
- prompt-injection resistance
- agreement/disagreement with deterministic engine
- agreement/disagreement with other reviewer
- latency
- estimated/actual model cost where available

Aggregate:

- precision
- recall
- false positives
- false negatives
- unsupported-claim rate
- disagreement rate
- evidence-lineage completeness
- median latency
- cost per control

## Governance

- Human Gate always remains locked.
- A model output cannot overwrite deterministic flags.
- Unsupported evidence basis triggers escalation.
- Primary/challenger disagreement triggers escalation.
- Model/provider/version must be stored in the Evidence Passport or model execution record.
- Secrets and customer evidence must never be committed to GitHub.

## Decision Card

Choose roles only after the benchmark:

**Primary reviewer:** model with the best evidence-grounded review profile under the agreed trade-offs.

**Independent challenger:** model/provider that contributes genuinely independent error detection rather than simply duplicating the primary.

**Fallback:** configuration that fails safely, is operationally practical, and preserves the output contract.

A cheaper model should not be preferred if the savings create unacceptable false negatives or unsupported claims. A more expensive model should not be preferred if it adds no measurable review value.

## Current status

This file defines the experiment only. No claim is made here that GPT, Claude or IBM Granite has already won the benchmark.
