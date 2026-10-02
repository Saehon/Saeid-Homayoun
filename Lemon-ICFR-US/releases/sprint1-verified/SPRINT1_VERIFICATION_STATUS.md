# LEMON-ICFR-US — Sprint 1 Verification & Sprint 2 Handoff

**Date:** 2026-10-02  
**Artifact:** `lemon_icfr_sprint1.zip`  
**SHA-256:** `f3dd26ad4982c8a9812e5a1472f0d5f1a0470cc1470d5f77cf9c0d77f4d733e1`

## Verified Sprint 1 status

The uploaded Sprint 1 package was inspected and executed. The reported results reproduced:

- 86/86 unit tests pass.
- 12/12 mutation tests are killed.
- 20-case benchmark executes successfully.
- Gate TPR: 16/17 = 94%.
- Gate FPR: 3/115 = 3%.
- Unsupported-claim detection: 4/5 = 80%.
- Bypass detection: 7/7 = 100%.
- Machine execution cannot directly produce `APPROVED`.
- Separate generator → reviewer → falsifier roles are genuinely enforced.
- Human approval is a real terminal gate rather than a placeholder.

## Architectural finding

The previous architectural defect—where the existence of hypotheses/challenges effectively satisfied review/falsification—is fixed in this Sprint 1 package.

## Main remaining problems

The primary remaining issue is semantic evidence validation rather than the orchestrator.

### G04 — false rejection

A legitimate paraphrased claim is rejected because the lexical matcher does not recognize semantic equivalence.

### G08 — dangerous false acceptance

Keyword-stuffed evidence passes even though it does not genuinely support the claim. This is the higher-priority failure because an unsupported ICFR conclusion can reach `AWAITING_HUMAN_APPROVAL`.

Additional architectural gaps:

1. COSO grounding is still represented largely as a Boolean `coso_context_supplied` rather than a structured evidence/relationship model.
2. Reproducibility validates the SHA format but does not confirm the referenced commit actually exists.
3. Falsifier test execution remains substantially self-attested rather than independently verified from execution traces.
4. Human approval is authorized through a registry but is not cryptographically signed/authenticated.

## Project state

**SPRINT 1 — PASS / GATE HARDENING COMPLETE**  
**SPRINT 2 — SEMANTIC + COSO EVIDENCE ENGINE REQUIRED**

Sprint 1 should remain the baseline. Do not rewrite it. Build Sprint 2 on top of the verified package.

## Sprint 2 priority sequence

`Evidence Passport → COSO graph → Semantic Support Evaluator → competing hypotheses → verified falsification traces → signed Human Gate`

## Critical Sprint 2 acceptance criterion

Fix G04 without causing G08 to pass, then evaluate the semantic evaluator on a held-out test set rather than optimizing only against the known benchmark cases.