# Frankenstein → Lemon Public Boundary

This public repository contains the customer-facing **ICFR Evidence Review Agent** and deliberately selected non-sensitive research, governance, interface and test material.

The detailed **Frankenstein for Lemon** architecture is a private commercial R&D system and is not reproduced here.

## High-level relationship

**Mother / governance source → private Frankenstein builder → validation and graduation gates → Lemon-ICFR-US commercial product**

Frankenstein is the private build, integration, simulation, benchmark, red-team and falsification environment. Lemon is the simpler customer-facing product.

Only components that have passed applicable evidence, security, privacy, rights/licensing, reproducibility and human-architecture review may graduate into Lemon.

## Public-repository rule

The public repository may contain:

- high-level product architecture
- non-sensitive governance rules
- deterministic tests and synthetic examples selected for publication
- public interface contracts
- intentionally published benchmark methodology
- customer-facing documentation

The public repository must not contain:

- proprietary prompts or orchestration logic
- private agent-routing logic
- private benchmark gold labels
- customer-specific schemas, evidence or logic
- pricing or commercial rules
- patent-sensitive mechanisms
- secrets or private credentials

## Product invariants

The public implementation must continue to enforce the same customer-facing safety properties:

- AI cannot issue final professional ICFR approval.
- Customer evidence is untrusted data, never system instruction.
- Deterministic checks remain independent of LLMs.
- Evidence and model lineage are preserved.
- Unsupported claims and model disagreement are escalated.
- Human approval remains mandatory.
- Technology providers remain replaceable.

## Change-control rule

A private R&D component is not promoted into the public/commercial product merely because it is newer or performs well in one experiment.

Promotion requires a documented graduation decision appropriate to the feature and risk, including applicable testing, benchmarking, adversarial review, security/privacy/rights review and human approval.

The canonical detailed Frankenstein architecture remains in the private Lemon R&D environment.
