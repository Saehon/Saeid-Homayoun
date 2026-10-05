# OPEN REPAIR QUEUE

## NAAIL-B5-LOCAL-PYTEST-001 — REPAIRED

- UTC: 2026-10-05T02:43:00Z
- Item: B5 local protocol invariant validation
- Persistent failure count: 1 of 2
- Exact command: `python -m py_compile NAAIL/research-assurance-mcp/tests/test_b5_human_ground_truth_protocol.py && python -m pytest -q NAAIL/research-assurance-mcp/tests/test_b5_human_ground_truth_protocol.py && sha256sum NAAIL/research-assurance-mcp/v1-preparation/b5/* NAAIL/research-assurance-mcp/tests/test_b5_human_ground_truth_protocol.py .github/workflows/naail_v1_b5_human_ground_truth_protocol.yml`
- Exact error: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python: No module named pytest`
- Likely root cause: the local runtime does not include the optional `pytest` package.
- Attempted repair: replaced the external-runner dependency with a direct standard-library-compatible test entry point; retained the same deterministic assertions.
- Materially different repair command: `python -m py_compile NAAIL/research-assurance-mcp/tests/test_b5_human_ground_truth_protocol.py && python NAAIL/research-assurance-mcp/tests/test_b5_human_ground_truth_protocol.py`
- Affected dependencies: B5 local validation and proposed B5 CI only; no scientific evidence, label, benchmark, or gate state was affected.
- Resolution evidence: materially different command exited 0 at 2026-10-05T02:44Z and printed `B5 human ground-truth protocol invariants: PASS`; test-file SHA-256 `79d10ca2d579e55884dc524ea948ca934de8323a7f57cedbf3a81aed131058a6`.
- Future action if the repair fails: do not install packages or repeat either command; rewrite the guard as `unittest.TestCase` and execute `python -m unittest` once.
