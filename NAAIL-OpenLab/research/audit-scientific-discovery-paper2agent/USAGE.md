# NAAIL Paper2Agent — MCP Usage (Local, Read-only)
**Operational level:** Local MCP JSON-RPC stdio tool server; **not** a full author-generated Paper2Agent skill conversion and not a hosted SaaS.

## Install
Prerequisite: Python 3.10+; repository checkout including the existing `Lemon-ICFR-US` and `NAAIL-OpenLab` folders. No package installation, API key, network, or external model is required for synthetic MCP tools.

```bash
cd NAAIL-OpenLab/research/audit-scientific-discovery-paper2agent
python -m unittest discover -v -p 'test_*.py'
python mcp_server.py
```
When run directly the server reads newline-separated MCP/JSON-RPC requests on **stdin**, writing only JSON-RPC responses on **stdout**. It waits for a compatible MCP client rather than displaying an interactive prompt. Configure a client that supports local *stdio* MCP servers using the absolute path to `mcp_server.py`.

## Example client configuration (path must be replaced)
```json
{
  "mcpServers": {
    "naail-audit-paper2agent": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/TO/Saeid-Homayoun/NAAIL-OpenLab/research/audit-scientific-discovery-paper2agent/mcp_server.py"]
    }
  }
}
```
This JSON is illustrative; consult your specific client documentation for its supported MCP config format.

## Registered tools
- `get_paper_method`: Bao 2020 provenance and accurate author-replication status.
- `run_architecture_benchmark`: 80-case synthetic A0–A3 science-software benchmark.
- `inspect_synthetic_case`: synthetic evidence passport for one `SYN-YYYY-NN` ID only.
- `get_assurance_policy`: immutable approval, rights and professional-boundary rules.

## Real integration to existing NAAIL code
```bash
python integrated_case.py --case-id SYN-2024-00 --out results/integrated_evidence_passport.json
```
This executes the existing `lemon_icfr.orchestrator.LemonOrchestrator` and existing CAM/KAM benchmark's `score_rows` method on explicitly artificial evidence/text, preserving human approval as required. It does **not** connect live SEC/PCAOB tools or any actual external AI reviewer.

## Author-code replication gate
Clone or provide your authorized local copy of https://github.com/JarFraud/FraudDetection with its original MATLAB source and final dataset; do not redistribute data into this repo. Check the local environment:

```bash
python bao_replication_gateway.py --source-dir /authorized/local/FraudDetection
```
Execute original code **only** when rights have been verified, MATLAB is installed, author files match pinned Git blob hashes, and the data schema is valid:
```bash
python bao_replication_gateway.py --source-dir /authorized/local/FraudDetection --execute --rights-authorized
```
Successful MATLAB execution is *not* a validated replication until coefficients/tables/metrics, 2022 correction and independent review are completed. The gateway records a blocked report instead of pretending to execute unavailable software/data.

## Technical / scientific boundaries
- This is not the original Paper2Agent host-driven conversion with specialist code agents and fresh verifiers. Original method: https://github.com/jmiao24/Paper2Agent ; follow its upstream `skills/paper2agent/SKILL.md` in a supported local coding-agent host to perform that separate conversion.
- No autonomous audit opinion, PCAOB judgment, confirmed fraud findings, proprietary data uploads, or secret-key handling.
- Use published CAM only for post-report descriptive comparison; PCAOB AS 3101 defines additional criteria, so high risk without CAM never establishes auditor error.
