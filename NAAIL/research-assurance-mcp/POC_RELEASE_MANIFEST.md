# NAAIL Research Assurance MCP — POC Release Manifest

Release gate: P8/P9 candidate; NOT POC_COMPLETE.

## Integrated POC inventory
P0 Case 001 and Microsoft public-SEC proof are frozen with provenance/limitations.
P1 Error Taxonomy V2 is machine-readable.
P2 Adversarial Benchmark V2 contains 19 fixtures spanning clean-control, single, compound, and blinded/difficult classes; executable mutation generators remain deferred.
P3 Evidence Graph V1 contract: 13 nodes / 13 edges, including TABLE_REG -> CODE_MAIN and author/Microsoft provenance chains.
P4 Research Assurance Report V1 uses VERIFIED / CONSISTENT / PARTIAL / FLAGGED / HUMAN_REVIEW.
P5 Minimal MCP/API core is present.
P6 bounded Case 001/Microsoft end-to-end demo artifacts are present.
P7 integration harness exists; bounded isolated execution evidence previously passed, but repository CI PASS is not claimed.
P8 dual-system release synchronization is being closed through hourly verified readbacks.
P9 final blocker-resolution/regression gate remains open.

## Scientific boundaries
- 264/264 means author-output consistency only, not independent full-paper reproduction.
- Microsoft is a bounded one-company public-SEC construct reconstruction.
- Full-paper independent reproduction remains PARTIAL where licensed/restricted inputs are unavailable.
- Methodological validity remains HUMAN_REVIEW where judgment is required.
- Synthetic, author-provided, public-source reconstructed, and independently regenerated evidence must remain separately labeled.

## Open blockers
1. P2 executable mutation-generator layer: deferred after write-surface failures. Next action: smallest atomic derived generator plus regression test.
2. Repository CI execution evidence: no GitHub Actions PASS claimed. Next action: execute integration harness on repository-supported runner when available.
3. Restricted/licensed full-paper reproduction: documented scientific limitation; do not bypass licensing.
4. P9 final regression and gate determination: required before POC_COMPLETE.

## Gate rule
POC_COMPLETE must not be claimed until P9 regression/blocker sweep is executed and no critical blocker invalidates the integrated POC. Non-critical documented limitations may remain.
