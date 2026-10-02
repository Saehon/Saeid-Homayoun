# Q4 — Non-canonical assurance label mapping

Date: 2026-10-02  
Scope: NAAIL Research Assurance MCP, Case 001 correction layer.

This is an additive compatibility note. Historical artifacts and their original labels remain unchanged. New/derived records use only the five canonical assurance states:

`VERIFIED`, `CONSISTENT`, `PARTIAL`, `FLAGGED`, `HUMAN_REVIEW`.

| Legacy non-canonical label | Canonical mapping | Scope-preserving interpretation |
|---|---|---|
| `SEC_SOURCE_VERIFIED_ONE_COMPANY_PROOF` | `VERIFIED` | Verified only for the bounded Microsoft public-SEC construct that was actually reconstructed; it is not full-paper replication. |
| `OUT_OF_SCOPE_FOR_ONE_COMPANY_CASE` | `PARTIAL` | The one-company test does not establish the out-of-scope claim; evidence remains incomplete rather than verified or falsified. |
| `NOT_CLAIMED` | `PARTIAL` | No affirmative assurance claim was made. For canonical machine-state compatibility it remains unresolved/incomplete; retain the original semantic qualifier when rendering reports. |

## Application rule

1. Do not rewrite immutable historical evidence merely to replace legacy labels.
2. Apply this mapping only in derived/corrected artifacts and machine-normalization layers.
3. Preserve scope qualifiers so `VERIFIED` cannot be read as full-paper independent reproduction.
4. A missing or unclaimed proposition must never be promoted to `VERIFIED` or `CONSISTENT`.
5. Methodological validity remains `HUMAN_REVIEW` where judgment is required.

Related correction artifact: `derived/evidence_graph_v1_1_case001.json`.
