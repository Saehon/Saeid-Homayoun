# Concurrency incident and single-writer protocol — 2026-10-02

## Incident evidence

- PR #100 was closed at **2026-10-02T12:06:39Z** (**14:06:39 Europe/Stockholm**).
- GitHub records the actor as account `Saehon`.
- PR #102 was created at **2026-10-02T12:06:37Z**, two seconds before the #100 closure.
- The NAAIL hourly automation's prior recorded run was around **13:31 Europe/Stockholm** and its next hourly cadence was later; therefore the #100 closure is not attributable to that scheduled run.
- GitHub does not expose a ChatGPT/session identifier for the mutation. The strongest supported attribution is: **the concurrent interactive operator activity that created PR #102 also closed PR #100**. No more specific process identity is asserted.

## Single-writer rule

Canonical working branch: `naail/research-assurance-case-001`.

Before any scheduled/hourly mutation, read:
`NAAIL/research-assurance-mcp/hourly-build/LOCK.json`.

If the lock exists with:
- `active: true`,
- an owner different from the hourly operator, and
- an unexpired `expires_at`,

the hourly run must **NO-OP**. It must not:
- edit or commit files;
- open, close, reopen, or modify pull requests;
- rerun or trigger CI;
- write Google Drive project records;
- delete or overwrite another operator's lock.

Interactive writers acquire the lock before mutations and release it at the end of the controlled session. Stale locks must be handled explicitly; they must not be silently ignored.

The active NAAIL hourly automation was updated on 2026-10-02 to enforce this rule before all GitHub/Drive writes.

## PR scope rule

Exactly one pull request per approval scope:
- **PR A #101** — Q1/Q2/Q4 engineering, records, deterministic regression CI, and concurrency governance.
- **PR B #103** — Q5 Microsoft COVID only.

Overlapping PRs #100 and #102 are closed without merge and point to PR A / PR B.

No merge is authorized by this record.
