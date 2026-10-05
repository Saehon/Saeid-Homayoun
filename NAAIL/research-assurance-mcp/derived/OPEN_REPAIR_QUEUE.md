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

## NAAIL-B5-REVIEW-PACKAGE-COMMIT-001 — REPAIRED

- UTC: 2026-10-05T02:45:00Z
- Item: B5 Claude review-package commit
- Persistent failure count: 1 of 2
- Exact action: connector script attempted `GET /repos/Saehon/Saeid-Homayoun/commits/naail%2Fv1-b5-human-ground-truth-2026-10-05` and then parsed the absent `structuredContent.content` field.
- Exact error: `SyntaxError: "undefined" is not valid JSON`; diagnostic readback then returned `HTTPError: 400: GitHub Fetch URL contains an invalid repository path.`
- Likely root cause: the generic fetch connector rejects an encoded slash in the commit path for a branch name; no GitHub mutation occurred.
- Attempted repair: none before recording; the review package remains local only.
- Materially different repair: fetch PR #123 metadata, compare its exact `head_sha` with the expected commit, fetch that full commit SHA for the base tree, and atomically commit the review package plus this queue update.
- Affected dependencies: B5 review handoff and dual-save record only; the already successful CI run and protocol files are unaffected.
- Resolution evidence: the SHA-guarded atomic repair committed both files at `384fa398eac880070b1ee853548074fdf53ad3be`; review-package blob `cf5aae2f5e5f965030634bd1405d5ec21af9d81b`.
- Future action if the repair fails: do not repeat branch-name lookup; use `fetch_file` on the PR branch plus a SHA-guarded contents update.

## NAAIL-B5-QUEUE-UPDATE-001 — REPAIR IN PROGRESS

- UTC: 2026-10-05T02:47:00Z
- Item: publish repaired status for the B5 review-package failure record
- Persistent failure count: 1 of 2
- Exact action: read the local queue with `base64 -w0`, then decode inside the connector script with `atob` before a SHA-guarded `update_file` call.
- Exact error: `ReferenceError: atob is not defined`
- Likely root cause: this V8 orchestration environment does not expose the browser `atob` global.
- Attempted repair: none before recording; the SHA guard confirmed remote blob `e0895972d2c5409f08b684c3f5439bb9303270d5`, and no mutation occurred.
- Materially different repair: serialize the UTF-8 file as a JSON string with the local Python standard library, parse that string in the orchestration environment, then use the same live blob SHA exactly once.
- Affected dependencies: repair-queue readback only; protocol, CI, and review-package evidence are unaffected.
- Future action if the repair fails: park the queue update as a connector limitation and leave the already committed evidence unchanged.
