# OPEN REPAIR QUEUE — B6 branch-local additive record

Earlier repair records remain preserved on their originating branches. This B6 branch-local queue entry must be reconciled additively before any approved merge; it does not supersede prior records or upgrade an assurance state.

## NAAIL-B6-LOCAL-HASH-ENUMERATION-001 — REPAIRED

- UTC: 2026-10-07T04:03:00Z
- Item: B6 local protocol validation and file fingerprint enumeration
- Persistent failure count: 1 of 2
- Exact command: `python -m py_compile b6/test_b6_pilot_comparison_protocol.py && python b6/test_b6_pilot_comparison_protocol.py && sha256sum b6/*`
- Exact error: `sha256sum: b6/__pycache__: Is a directory`; the compound command returned exit 1 after compilation and invariant validation had already passed.
- Likely root cause: the successful Python compile created a directory matched by the shell glob; `sha256sum` accepts files, not directories.
- Attempted repair: preserved the successful compile/test evidence and did not rerun either test.
- Materially different repair command: `find b6 -maxdepth 1 -type f -print0 | sort -z | xargs -0 sha256sum`
- Affected dependencies: local packaging fingerprints only. Protocol content, frozen hashes, CI design, and scientific states were unaffected.
- Resolution evidence: the file-only command exited 0 and enumerated all seven B6 files; protocol SHA-256 `128e1d3f385435a2181b79a0432f884071322effcae49b097d6368b3955e9081`; metrics SHA-256 `150eb820a0461d8d74faf1c5af162dac90018c0321aa188af4d602556b3948bb`.
- Future action if the repair fails: use an explicit immutable file list once; do not rerun the protocol test or broaden the hash target.

## NAAIL-B6-PR-COMMENT-001 — REPAIRED

- UTC: 2026-10-07T04:04:00Z
- Item: B6 PR #133 CI/readback comment
- Persistent failure count: 1 of 2
- Exact failed action: `github_add_comment_to_issue` with arguments `issue_number` and `body`.
- Exact error: `InvalidActionArgumentsError: Missing required tool arguments: pr_number, comment`.
- Likely root cause: the connector action is named for issues but its live schema accepts `pr_number` and `comment`.
- Attempted repair: inspected the live action schema and used its required argument names once; the failed call made no mutation.
- Resolution evidence: corrected call returned comment ID `6030661709` on PR #133.
- Affected dependencies: PR conversation logging only; protocol, CI, freeze hashes, and scientific states were unaffected.
- Future action if the repair fails: do not repeat either call; preserve CI evidence in the review package and park PR-comment logging as a connector limitation.
