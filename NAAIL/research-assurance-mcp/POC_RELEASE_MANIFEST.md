# NAAIL Research Assurance MCP — POC Release Manifest

Release gate: **NOT POC_COMPLETE**.

## Canonical progress accounting

Progress is reported against the master-plan acceptance criteria, not as estimated percentages.

### POC gate — 7 of 10 met, 3 partial

| # | POC criterion | Status | Evidence / gap |
|---|---|---|---|
| 1 | Case 001 frozen with verified provenance | PARTIAL | COVID claim remains unsupported; 264/264 is author-output consistency and is not independently re-checkable from the repository alone. |
| 2 | Microsoft reconstruction frozen | PARTIAL | FilingLag is VERIFIED for 10/10 observations; COVID rule remains open. |
| 3 | Error Taxonomy V2 machine-readable | MET | File parses; assurance states/evidence classes are machine-readable. |
| 4 | Benchmark has clean, single, compound and difficult cases | MET | Executable P2 layer has been completed independently: 19/19 plus falsification suite. Repository intake/integration must preserve provenance. |
| 5 | Evidence Graph V1 links the chain | MET | 13/13 graph checks verified; state-label v1.1 correction remains a record-level fix, not a gate failure. |
| 6 | Assurance report can be generated | MET | Executed successfully, exit 0. |
| 7 | Minimal MCP/API tool contracts | MET | Six real functions exist; current implementation is a library, not an MCP server. |
| 8 | End-to-end demo executes | MET | Executed; current demo reads the evidence graph rather than rebuilding from raw inputs. |
| 9 | Tests pass | MET | GitHub Actions run 36998664461 reported success and matches independent local execution. |
| 10 | GitHub and Drive synchronized, with a release record | PARTIAL | Correction/reconciliation record is still being closed; final dual-system readback and intake state must be verified. |

Canonical summary: **POC nearly closed; V1 not started.**

### V1 gate — 0 of 10 met

No V1 acceptance criterion is currently met. Reusable POC foundations do not count as V1 completion. In particular, there are zero valid additional cases, no human ground-truth protocol, and no pilot comparison.

## Corrections to prior progress reporting

1. **Do not use P7 precision/recall/F1 = 1.0 as detection-performance evidence.** The P7 check compares expected answers with themselves and therefore cannot support a claim about detection ability.
2. **P2 executable mutation generation is completed independently.** Treat 19/19 plus the falsification suite as finished work; do not list "finish P2 mutation generator" as remaining.
3. **FilingLag is resolved.** The construct is filing date minus period end; the observed Microsoft values are VERIFIED. The remaining scientific issue is the COVID rule.
4. **GPT does not set POC_COMPLETE.** GPT prepares the final gate matrix; Claude performs an independent review; the user provides the Human Approval decision.

## Remaining POC closure actions

1. Complete repository intake/hash verification for the two ZIP packages, integrate the P2 benchmark/v2 harness under CI as appropriate, and close the correction/reconciliation record.
2. Add `EDGAR_IDENTITY` and run the pre-registered COVID scan. This decides the scientific portion of POC criteria 1 and 2 regardless of whether the result supports or rejects the COVID claim.
3. Produce the final 10-criterion gate matrix with repository/Drive evidence references.
4. Obtain independent Claude review.
5. Obtain explicit user Human Approval before changing `POC_COMPLETE`.

## Scientific boundaries

- 264/264 is author-output consistency only, not independent full-paper reproduction.
- Microsoft is a bounded one-company public-SEC construct reconstruction.
- FilingLag is VERIFIED within the stated public-SEC scope.
- The COVID classification remains unresolved until the pre-registered scan is executed.
- Full-paper independent reproduction remains PARTIAL where licensed/restricted inputs are unavailable.
- Methodological validity remains HUMAN_REVIEW where judgment is required.
- Synthetic, author-provided, public-source reconstructed, and independently regenerated evidence must remain separately labeled.

## Gate rule

`POC_COMPLETE` must remain FALSE until the final gate matrix is prepared, independently reviewed, and explicitly approved by the user.
