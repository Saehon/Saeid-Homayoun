# Governance

## Purpose

This project is an evidence-first research and engineering platform for multi-agent accounting, audit and finance assurance. It does not treat model agreement as evidence.

## Decision rights

- **Specialist agents** may retrieve, calculate, classify and propose.
- **Reviewer/falsifier agents** may challenge, replicate and flag conflicts but may not self-certify their own generating work.
- **The control plane** enforces permissions, risk thresholds and segregation of duties.
- **Humans** retain authority for material approvals, exceptions, benchmark freezes, releases and production policy changes.

## Independence requirements

A reviewer is not considered independent merely because it has a different role label. Record provider/model/version, prompt lineage, tool/data access and benchmark exposure. Shared benchmark knowledge, shared hidden state or developer-tuned probes must be treated as correlated-error risks.

## Benchmark integrity

1. Development examples are never reported as independent evaluation evidence.
2. A probe becomes development data once it is inspected during tuning.
3. Confirmatory evaluation uses fresh, held-back cases authored independently of the implementation.
4. Benchmark versions are frozen and hashed.
5. Failures are retained; they are not silently removed from the denominator.
6. Claims must identify population, task domain, benchmark version and evaluation date.

## Evidence states

Permitted result labels are:

- **VERIFIED** — directly checked against authoritative evidence under the stated procedure.
- **REPLICATED** — independently reproduced from the documented inputs/method.
- **INFERRED** — supported by analysis but not directly verified.
- **UNRESOLVED** — evidence is insufficient or conflicting.
- **FALSIFIED** — the tested claim failed the stated check.
- **DRAFT** — work not yet through the required assurance gate.

## Merge and release policy

Production-impacting changes require human approval. CI success is necessary but not sufficient for a release. No automated agent may merge a governance-sensitive change solely because tests pass.
