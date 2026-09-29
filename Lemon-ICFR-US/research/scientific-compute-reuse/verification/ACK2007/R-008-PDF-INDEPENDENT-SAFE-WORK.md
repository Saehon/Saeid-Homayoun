# R-008 — ACK2007 PDF-Independent Safe Repair Run

Date: 2026-09-29
Scope: ACK2007 only; PDF-independent safe work only.
Scientific-upgrade authority: NONE. This record does not verify the primary table, change coefficients, or upgrade scientific status.

## Live state at start
- PR: #76, open, not merged.
- Starting HEAD: d932c2ea554b9488827158c4edc69c4e1c42d5cc.
- Previously reported HEAD 3125fbf3... and run 36542291941 were treated as unverified until observed.
- Live verification found run #44 / 36542291941 SUCCESS on 3125fbf3..., but it is historical rather than current.
- Historical run #34 / 36431534510 FAILURE is preserved as falsification evidence.

## Repairs performed
1. Enforced R-005 downgrade:
   - FOREIGN_SALES -> SECONDARY_SOURCE
   - AUDITOR -> SECONDARY_SOURCE
   - INST_CON -> SECONDARY_SOURCE
   - LITIGATION -> SECONDARY_SOURCE
2. Preserved unresolved gates:
   - SIZE -> PROVENANCE_CONFLICT
   - RGROWTH -> PROVENANCE_CONFLICT
   - %LOSS -> BLOCKED_MISSING_YEAR_RULE
   - RZSCORE -> BLOCKED_RAW_CONSTRUCTION / O3 unresolved
3. Removed misleading Phase-4 PASS/supersession language and neutralized C1/C2/O3 definitions.
4. Established coefficient single source of truth:
   - coefficient-contract.json is the only numerical vector/intercept authority.
   - model.yaml references the contract and retains PENDING_PRIMARY_TABLE / UNKNOWN_ORIGIN / regression_pin_only.
   - ack2007.py loads the contract.
   - ACK2007-SPEC.md no longer duplicates coefficient values.
   - tests pin a semantic contract digest instead of duplicating the vector.
5. Hardened contract tests for missing, extra, duplicate, renamed, changed and sign-flipped predictors and intercept deletion/duplication/mutation.
6. Added end-to-end fail-closed execution wrapper and tests proving blocked/secondary inputs stop before constructors run.
7. Added adversarial cases for scale, unit, log-vs-level, window, missing-year policy, denominator, ranking direction, schema drift and silent exceptions.
8. Added checksum-mutation detection and explicit exception propagation.
9. Frozen fixture was NOT modified.

## Single-source-of-truth audit
Before repair:
- coefficient values were duplicated in ack2007.py, ACK2007-SPEC.md and tests;
- Phase-4/resolved artifacts selected RGROWTH/SIZE definitions that the Resolution Log keeps unresolved;
- four secondary-only variables were VERIFIED in the executable construction registry.

After repair:
- numerical coefficients/intercept: coefficient-contract.json only;
- raw-construction status: ACK2007-construction-gates.json only;
- ontology/spec/historical maps are descriptive and fail closed when unresolved;
- historical snapshots remain preserved but no longer claim executable PASS.

## Test/CI evidence
Implementation commit: d7051d45aef1dfd48bb8797dd0a2494a99dae6c2.
- Run #48 / 36546388009: FAILURE in executable compiler test due to a newly introduced zero-vector probability test expression. This failure is preserved.

Correction commit: 2f4f5f9333c90bcd5408860f3f9caa02682a9111.
- Run #49 / 36546469226: SUCCESS.
- Executable compiler tests: PASS.
- Fail-closed admission + frozen-fixture falsification: PASS.
- Frozen fixture execution/checksum: PASS.
- Two clean fixture executions use independent output directories and assert identical payload/checksum.
- Expected unchanged fixture checksum: c420891c605066edc1fe0e895ab5412decd65b648d25a42a1ceaeeb96113dda6.
- Frozen fixture blob SHA remains 438ef1e783e4e32d5b46b58ccd1b6cb29bde83d9.

## Codex
Fresh review requested on candidate HEAD 2f4f5f9333c90bcd5408860f3f9caa02682a9111.
Status at time of this record: CODEX_REVIEW_PENDING.
No Codex approval is claimed.

## Status
- Scientific: SCIENTIFIC_HOLD / NOT_M1_LOCKED / PENDING_PRIMARY_TABLE.
- Engineering: ENGINEERING_HOLD pending fresh Codex response, despite exact-candidate CI success.
- Overall gate: REVISE / HOLD.
- Primary-paper dependency: DEPENDENCY_CRITICAL for scientific verification.

## Boundaries
No primary-table verification was attempted.
No coefficient or intercept value was changed.
No frozen fixture was regenerated or changed.
No main merge was attempted.
No scientific status was upgraded.

## NEXT_EXECUTABLE_GATE
Primary: inspect the fresh Codex review when it arrives and repair any valid PDF-independent engineering finding without weakening tests.
Secondary safe work if Codex remains pending: audit remaining non-VERIFIED raw variables for status/definition consistency only; do not investigate primary definitions without the PDF.
