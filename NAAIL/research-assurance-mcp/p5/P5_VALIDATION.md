# P5 Minimal MCP/API — validation contract

This POC exposes six bounded tools: inspect_package, map_table_to_code, compare_reported_result, trace_provenance, score_detection, and generate_assurance_report.

Validation performed in this run:
- GitHub readback confirms the Python core and JSON contract exist on the active branch.
- Evidence Graph V1 readback confirms 13 nodes / 13 edges and the expected Case 001 IDs used by the core.
- Static interface check: the Python core defines all six contract functions plus graph validation and a Case 001 runner.
- Governance boundary remains explicit: no licensed-data bypass; computational consistency is not methodological validity.

Deferred to P7 integration tests: executable CI invocation and benchmark mutation generators.
