# NAAIL Research Assurance MCP — GPT Handoff Reconstruction

## Scope and source

This record captures GPT's independent reconstruction of the current NAAIL Research Assurance MCP branch using the connected GitHub repository.

- Repository: `Saehon/Saeid-Homayoun`
- Branch: `naail/research-assurance-case-001`
- Branch HEAD inspected: `e1eb7b623acd3fea6350f4e34edd103b70befb27`
- Historical run records are preserved unchanged. Corrections below supersede only the affected status/selection claims.

## Governance decisions

1. **Case 002 duplicate — ACCEPTED.** The V1-0/V1-1 records selected DOI `10.1287/mnsc.2023.4670` as Case 002, but the same DOI is already the canonical Case 001. That Case 002 selection is therefore invalid as a distinct case. New Case 002 and Case 003 must be selected.
2. **Canonical conflict resolver — MASTER PROMPT.** When the master prompt and `MASTER_POC_V1_ROADMAP.md` conflict, the master prompt governs. The roadmap is an implementation plan and must be conformed to the prompt rather than overriding it.
3. **Canonical numbering — P0–P9 and V1-0–V1-14.** Existing P0–P8 and V1.1–V1.11 records remain immutable historical identifiers; future/current status records should use the canonical numbering and document any alias mapping explicitly.

## A. Repository / handoff status

The repository is available through the connected GitHub integration, so a manually uploaded ZIP is no longer a blocker for source inspection of the relevant text/code artifacts. The branch is 59 commits ahead of the inspected merge-base lineage relative to main and contains the P3, P5, P6, P7, P9, benchmark, and Microsoft re-execution artifacts required for this review.

A binary branch ZIP was not exported by the connector. This does not affect the findings below; a ZIP would only be needed for byte-for-byte local execution of the entire repository rather than the reconstructed bounded package.

## B. P7 executable test evidence

The exact branch versions of the P7 harness, P5 core, Evidence Graph V1, and Adversarial Benchmark V2 were reconstructed in the GPT execution environment and the P7 harness was executed.

Command:

```text
/opt/pyvenv/bin/python /mnt/data/naail_p7_reconstructed/NAAIL/research-assurance-mcp/p7/test_poc_integration.py
```

Exit code: **0**

Material output:

```json
{
  "status": "PASS",
  "graph_validation": {
    "node_count": 13,
    "edge_count": 13,
    "all_node_ids_unique": true,
    "unresolved_edges": [],
    "invalid_state_nodes": [],
    "pass": true
  },
  "table_to_code_paths": 1,
  "author_trace_nodes": 8,
  "microsoft_trace_nodes": 7,
  "assurance_overall": "PARTIAL",
  "benchmark_fixtures": 19,
  "benchmark_kinds": ["blinded", "clean_control", "compound", "single"],
  "taxonomy_ids_exercised": 16,
  "scoring_sanity": {
    "tp": 16,
    "fp": 0,
    "fn": 0,
    "precision": 1.0,
    "recall": 1.0,
    "f1": 1.0
  }
}
```

**P7 status: PASS on the reconstructed bounded branch package.**

This replaces the earlier state in which the harness existed but no execution evidence was available. It does not create a GitHub Actions CI run retroactively.

## C. Benchmark reconstruction

`benchmark/adversarial_benchmark_v2.json` contains **19 unique benchmark case definitions**.

Classes present:
- clean control
- single-error cases
- compound cases
- blinded cases

The benchmark exercises **16 taxonomy IDs**.

Important boundary: these are 19 declarative benchmark fixtures/case definitions in the benchmark JSON. Current repository evidence does **not** show that code generates 19 independent mutation artifacts. P9 records explicitly state that executable mutation-generator writes were blocked and no mutation-generator execution PASS was claimed.

**Benchmark definition status: VERIFIED.**
**Executable mutation-generation status: PARTIAL / OPEN.**

## D. Evidence Graph V1

`evidence-graph/evidence_graph_v1_case001.json` contains:

- **13 nodes**
- **13 edges**
- unique node IDs
- no unresolved edge endpoints
- no invalid assurance states

The graph explicitly separates:
- author-output consistency evidence,
- independently regenerated Microsoft SEC evidence,
- restricted/full-reproduction limitations,
- methodological human review.

The P7 execution independently validated these structural properties.

**P3 graph status: VERIFIED for the current Case 001 graph artifact.**

## E. P5 API and P6 integration

The P5 module implements the six bounded POC functions required by the roadmap:

- `inspect_package`
- `map_table_to_code`
- `compare_reported_result`
- `trace_provenance`
- `score_detection`
- `generate_assurance_report`

The module imported and executed in the reconstructed environment. P7 directly exercised graph validation, table-to-code mapping, provenance tracing, assurance-report generation, and scoring. Supplementary execution exercised the remaining bounded package-inspection/result-comparison functions.

**P5 status: executable within the bounded reconstructed package.**

P6 has stronger evidence than the historical log recorded because P7 now executes the P5 integration against the canonical graph and verifies both author and Microsoft provenance chains. However, the repository still does not contain a separately executed dedicated P6 end-to-end demo/orchestrator that reacquires SEC evidence and regenerates the Microsoft dataset from source.

**P6 status: PARTIAL — functional integration evidenced, dedicated end-to-end demo remains open.**

## F. Microsoft FilingLag / COVID reconstruction

The repository defines:

```text
FilingLag = filing_date - period_end
```

for SEC filing metadata.

The frozen Microsoft one-company artifact contains ten observations and the matched same-quarter changes:

```text
+5, -2, +4, -3, +3, -3 days
```

for Q1-2020 through Q2-2021 relative to the same 2019 quarter.

The repository's binary COVID rule is presence of **"covid" or "corona"** in the matched SEC filing text. The frozen result records:
- matched 2019 filings: 0
- matched filings from Q1-2020 through Q2-2021: 1

The frozen one-company artifact also records LateFiler = 0 for all ten observations.

Therefore the Microsoft result can be classified **VERIFIED within the one-company public-SEC construct-reconstruction scope** for the frozen observations/calculations. It must not be promoted to full-paper replication or population-level methodological validation.

## G. Gate status after reconstruction

- P3 Evidence Graph V1: VERIFIED.
- P5 bounded API core: executable.
- P7 bounded integration harness: PASS, exit code 0.
- Benchmark V2: 19 declarative fixtures VERIFIED; executable mutation generation remains OPEN.
- P6: PARTIAL; dedicated full end-to-end demo remains OPEN.
- P9: OPEN/PARTIAL because mutation-generator/regression evidence and final release-gate closure are not yet satisfied.
- Case 002: duplicate selection invalidated; new Case 002 and Case 003 required.

Scientific scope remains unchanged:
- 264/264 is author-output consistency, not full independent reproduction.
- Microsoft is a one-company public-SEC construct reconstruction.
- Full-paper independent reproduction remains PARTIAL.
- Methodological validity remains HUMAN_REVIEW.
