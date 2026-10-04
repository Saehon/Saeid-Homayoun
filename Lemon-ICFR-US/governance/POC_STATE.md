# LEMON POC STATE

**Updated:** 2026-10-04  
**Governance status:** human approval required for every merge, including merges into stacked/base branches.

## Current phase

| Stage | Status | Evidence / constraint |
|---|---|---|
| S1 — Assurance-core + legacy-orchestrator rewiring | **COMPLETE FOR HUMAN REVIEW** | Claude verdict: `R2_ACCEPTABLE_FOR_HUMAN_REVIEW`; C1–C7 implemented; repository-native CI green; fail-closed demo executed in CI. |
| S2 — Fact extraction with source spans and hashes | **READY / NOT STARTED** | ORQ-006. Start only after owner-approved R2 merge sequence is completed and R2 is on `main`. |

## S1 verification

- R2 remainder PR: **#119** — draft, not merged.
- Verified CI SHA: `cc4dba1c7993e563ef2ea75606be1c7c28428064`
- GitHub Actions run: `37219701891`
- Python: `3.11.16`
- Test result: **66 passed, 26 subtests passed**
- CI demo step: **PASS**
- Real executed first line: `BLOCKED:icfr_coso_grounding,evidence_consistency`
- The demo is intentionally fail-closed because it provides no structured `ICFRScope` and no `EvidenceStore`.

## Scientific status

- ACK2007: **SCIENTIFIC_HOLD**
- M1 locked: **false**
- SIZE: **QUARANTINED / NON-EXECUTABLE**
- RGROWTH: **QUARANTINED / NON-EXECUTABLE**
- Sprint 1 metrics: **DEVELOPMENT_ONLY**

## Governance holds

- **ORQ-013 remains OPEN** until the human owner explicitly acknowledges the deviation and the rule: no merge into any branch, including stacked bases, without owner approval.
- **ORQ-014 is OPEN / P3 / NON-BLOCKING**: legacy challenge text in `contradictions` needs an explicit unvalidated label or typed replacement in a later scope.
- No merge to `main` is authorized by this state file.

## Owner-controlled merge sequence

1. PR #119 → `lemon/r1-assurance-core`
2. Rebase PR #115 onto current `main`, then rerun CI
3. PR #115 → `main`

Each step requires explicit owner approval and a reported SHA + CI result.
