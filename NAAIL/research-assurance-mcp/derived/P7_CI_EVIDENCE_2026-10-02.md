# P7 Repository CI Evidence — 2026-10-02

This is an additive execution-evidence record. Historical run logs remain unchanged.

## Workflow activation
- Workflow: `.github/workflows/naail_research_assurance_p7.yml`
- Activation commit: `7e3a59a0eef6d8fde76a1316371d55f4036f3656`
- Trigger: push
- Runner: Ubuntu 24.04
- Python: CPython 3.12.14

## GitHub Actions execution
- Run ID: `36998664461`
- Run number: 1
- Job ID: `110811087411`
- Job: `p7-integration`
- Status: completed
- Conclusion: **success**
- Command:
  `python NAAIL/research-assurance-mcp/p7/test_poc_integration.py`

## Material harness output
- status: PASS
- graph: 13 nodes / 13 edges
- unresolved graph edges: 0
- invalid assurance-state nodes: 0
- table-to-code paths: 1
- author provenance trace nodes: 8
- Microsoft provenance trace nodes: 7
- overall assurance: PARTIAL
- benchmark fixture definitions: 19
- benchmark kinds: blinded, clean_control, compound, single
- taxonomy IDs exercised: 16
- scoring sanity: precision=1.0, recall=1.0, f1=1.0

## Scope guards preserved
- 264/264 is author-output consistency only.
- Microsoft is a one-company public-SEC construct reconstruction only.
- Full-paper independent reproduction remains PARTIAL.
- Methodological validity remains HUMAN_REVIEW.

## Gate effect
The specific P7 blocker "no repository CI execution evidence" is closed by this run.

This does **not** make POC_COMPLETE true. Remaining blockers include, at minimum:
- Claude external artifact bundle bytes/hash verification not completed;
- the four externally referenced Claude artifacts remain unavailable for byte-level verification/commit;
- public-main correction PR is not yet complete/merged;
- other open scientific/governance issues remain as documented in the correction/handoff records.

POC_COMPLETE = FALSE
V1_COMPLETE = FALSE
