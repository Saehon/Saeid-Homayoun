# B7 — MCP server skeleton

Status: **OPERATOR IMPLEMENTATION / INDEPENDENT REVIEW REQUIRED**

This bounded Python stdio server exposes the six existing P5 tool contracts:

1. `inspect_package`
2. `map_table_to_code`
3. `compare_reported_result`
4. `trace_provenance`
5. `score_detection`
6. `generate_assurance_report`

The server implements MCP initialization, `tools/list`, and `tools/call` over newline-delimited JSON-RPC 2.0. Inputs and outputs are checked against `tool_schemas.json`. Package inspection is restricted to project-relative directories. No network, subprocess, credential, licensed-data, case-selection, benchmark-probe, or state-promotion capability is exposed.

The server imports the existing P5 functions without modifying their assurance logic. It neither asserts methodological validity nor converts missing evidence into a stronger assurance state.

## Local validation

Run exactly once before opening the PR:

```bash
python -m py_compile b7/naail_mcp_server.py b7/test_b7_mcp_server.py
python b7/test_b7_mcp_server.py
```

The dedicated workflow is restricted to the pull-request `opened` event to support one authoritative B7 CI execution. Do not rerun it to select a preferred result.
