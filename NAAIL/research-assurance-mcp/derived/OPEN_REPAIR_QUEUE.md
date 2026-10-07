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

## NAAIL-B6-DRIVE-READBACK-HASH-001 — PARKED / TOOLING

- UTC: 2026-10-07T04:06:00Z
- Item: RUN 033 Google Drive normalized-text readback SHA-256
- Persistent failure count: 2 of 2; stop retrying until a new execution context or final repair sweep.
- Failure record 1: attempted an in-isolate SHA-256 over the connector-normalized paragraph text using `crypto.subtle.digest`; exact error `ReferenceError: crypto is not defined`. No Drive mutation occurred.
- Failure record 2: materially different repair opened an interactive `sha256sum` process and streamed the normalized text through `write_stdin`; the TTY echoed the document and the returned output was truncated before any reliable digest or exit code could be observed. No Drive mutation occurred.
- Likely root cause: this orchestration isolate lacks the Web Crypto global, while the interactive PTY path echoes large stdin and exceeds the bounded output surface.
- Attempted repairs: in-memory Web Crypto, then a separate system `sha256sum` process with streamed stdin. Neither produced a trustworthy digest.
- Affected dependencies: RUN 033 readback hash only. The Drive write succeeded atomically at revision `ANLCKQnloBpgxxYkY2HkY8j8Dzhv3JihCEjGSFvXv0xqdwVUKtIDztwxYznm-bocPmnDK5GfxfleT1GmXlvcHqApwCNpWJ7YUDd-ylLBW3g`; connector readback confirms RUN 033 content in document `1FV8qyLJaxDVbOuh_FBkKVcD1bcDPoHQRI4VPabG1vNI` tab `t.0`.
- Quarantine: do not claim a Drive SHA-256 for RUN 033. Dual-save content is readable, but the digest field remains PARKED.
- Exact future repair action: during a later genuinely new context or final repair sweep, rerun the checked-in trusted-read bridge into a fresh immutable output directory and hash its persisted `document-text.md` with a non-interactive file-based `sha256sum`; record the bridge artifact hash and document revision without streaming content through a TTY.
