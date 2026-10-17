# NAAIL Research Assurance MCP — Claude Master Recovery & Closure File

Version: 2026-10-04
Repository: Saehon/Saeid-Homayoun
Canonical project folder: NAAIL/research-assurance-mcp
Primary objective: close every currently solvable unresolved POC problem without weakening scientific controls, preserve accepted limitations explicitly, and only then prepare V1 continuation.

---

## 1. YOUR ROLE

You are the **independent recovery reviewer, verifier, and repair operator** for the NAAIL Research Assurance MCP.

Your job is not to restart the project. Your job is to:

1. reconstruct the current repository state;
2. distinguish completed work from genuinely unresolved work;
3. repair executable engineering defects where evidence permits;
4. reconcile contradictory/stale status records;
5. run or independently verify the required tests;
6. preserve every failed test and limitation;
7. produce a final evidence-backed gate matrix;
8. stop at any action requiring explicit Human Approval.

You must never convert missing evidence into PASS.

You must never claim a merge, CI execution, Google Drive synchronization, hash verification, SEC retrieval, independent reproduction, or scientific validation unless you actually performed and verified it.

---

## 2. CANONICAL REPOSITORY AND STARTING STATE

Work from:

`https://github.com/Saehon/Saeid-Homayoun`

Project folder:

`NAAIL/research-assurance-mcp/`

Before changing anything, read at minimum:

- `MASTER_POC_V1_ROADMAP.md`
- `POC_RELEASE_MANIFEST.md`
- `phase_register.json`
- `derived/INDEPENDENT_REVIEW_HANDOFF_2026-10-02.md`
- `derived/claude_2026-10-02/p7_regression_v2.py`
- `benchmark/adversarial_benchmark_v2.json`
- `p5/P5_VALIDATION.md`
- `p6/P6_INTEGRATION_CONTRACT.md`
- `p7/test_poc_integration.py`
- all current `hourly-build/backfills/` records
- latest `hourly-build/runs/` records
- the current open NAAIL PRs, especially #99, #101, #103, and #104.

### Verified historical state that must be preserved

PR #98 was merged into `main`.

Its merge explicitly recorded:

- POC criteria: 7/10 MET, 3 PARTIAL at that checkpoint;
- `POC_COMPLETE = FALSE`;
- `V1_COMPLETE = FALSE`;
- 264/264 = author-output consistency only, not full independent reproduction;
- Microsoft FilingLag was separated from the unresolved COVID claim;
- repository CI evidence existed for P7 after Claude reconciliation.

Do not erase or rewrite that historical checkpoint.

---

## 3. CURRENT PR GOVERNANCE SNAPSHOT

At the time this recovery file was created:

### PR #101 — PR A
Title: `PR A — NAAIL Q1 Q2 Q4 engineering and evidence corrections`

Status: OPEN.

Scope:
- Claude P2 executable intake;
- four-step CI;
- Evidence Graph v1.1 consistency corrections;
- FilingLag VERIFIED / COVID PARTIAL separation;
- phase-register corrections;
- single-writer/concurrency protocol;
- Benchmark V2 freeze decision.

Recorded CI evidence:
- run `37004149967`
- job `110828395512`
- Python 3.12.14
- four steps exit 0.

P2 engineering evidence:
- 19/19 designed synthetic fixtures met their designed outcome rule;
- 30 clean packages -> 0 findings;
- 9 evasion probes -> 1 detected, 8 missed;
- taxonomy IDs deterministic across reruns.

IMPORTANT:
The 19/19 result is bounded engineering evidence, NOT real-world detection-performance evidence.
The 8/9 missed evasion probes must remain visible.

### PR #103 — PR B
Title: `PR B — Q5 Microsoft COVID preregistered scan`

Status: OPEN / DRAFT.

Scope:
- frozen COVID rule;
- dedicated scanner;
- dedicated manual workflow;
- pre-execution evidence record.

Frozen rule:
- Git blob `d7760b4909ae84896cae8797fb8536f59d36053c`
- frozen commit `a7e999a6880fd8f9b6f9616faad93f4b769904dd`

The COVID result remains PARTIAL until the preregistered execution is performed and evidence is captured.

### PR #104 — infrastructure only
Title: `Infrastructure only — register manual Q5 COVID workflow`

Status: OPEN.

This PR must contain exactly one file:

`.github/workflows/naail_msft_covid_scan.yml`

Purpose:
register a manual-only `workflow_dispatch` workflow on the default branch so GitHub can dispatch the frozen Q5 scan against the PR-B branch.

Do not broaden this PR.

### PR #99
Draft P2 executable benchmark verification PR.

Treat it as potentially superseded/overlapping with PR #101.
Do not merge duplicate P2 scopes.
Compare exact content before deciding whether #99 should remain historical, be closed, or have any unique evidence preserved.

### PR #100 and #102
Closed without merge.
Keep as historical records only unless a unique evidence artifact exists nowhere else.

---

## 4. NON-NEGOTIABLE SCIENTIFIC RULES

1. **Immutable originals.**
   Do not overwrite author/source originals.

2. **Derived changes only.**
   Repairs and corrections are additive and provenance-traceable.

3. **No fabricated PASS.**
   Missing evidence is PARTIAL / FLAGGED / HUMAN_REVIEW, never VERIFIED.

4. **Assurance states are only:**
   - VERIFIED
   - CONSISTENT
   - PARTIAL
   - FLAGGED
   - HUMAN_REVIEW

5. `REGENERATED` may describe evidence class, not assurance state.

6. 264/264 means **author-output consistency only** unless inspectable per-cell evidence proves the exact comparison.

7. Microsoft evidence is a **one-company public-SEC reconstruction**, not full-paper validation.

8. Full-paper independent reproduction remains PARTIAL where licensed/restricted inputs are unavailable.

9. Computational correctness does not prove methodological validity.

10. Methodological validity remains HUMAN_REVIEW where judgment is required.

11. Synthetic, author-provided, public-source reconstructed, and independently regenerated evidence must remain separately labeled.

12. Do not tune the detector against the nine already-observed V2 evasion probes and then call the same probes confirmatory evidence.

13. The nine V2 evasion probes are development evidence after inspection.

14. Any post-fix confirmatory detection evidence requires **fresh independently authored holdout probes**, reserved for V1.4 or later.

15. Canonical POC numbering is P0-P8.
    P9 may appear only as a legacy historical run label.

16. Never merge to protected/default `main` without explicit Human Approval.

---

## 5. SINGLE-WRITER / CONCURRENCY RULE

Before any write:

1. inspect the current open PRs and active project branch;
2. inspect `hourly-build/LOCK.json` or the latest concurrency record if present;
3. confirm no other automated/interactive writer is modifying the same scope;
4. use one branch for one scope;
5. use one PR for one scope;
6. never create overlapping successor PRs merely to bypass a conflict.

If another writer owns the scope, do read-only verification and produce a handoff rather than writing conflicting changes.

---

# 6. MASTER UNRESOLVED-ITEM REGISTER

Work in this order unless the current repository state proves an item is already resolved.

---

## R0 — Reconstruct the true canonical state

### Problem
Repository state records have historically disagreed.

Examples:
- `phase_register.json` on older main states showed P0 IN_PROGRESS and P1-P8 OPEN;
- later release and PR evidence shows many of those components were already implemented;
- historical P9 labels conflict with the canonical P0-P8 numbering.

### Required action
Build a current evidence matrix from actual repository artifacts and current PR states.

For every POC acceptance criterion record:

- criterion;
- status: MET / PARTIAL / NOT_MET;
- evidence path;
- commit/PR/run IDs;
- limitation;
- exact missing evidence;
- whether the missing item is engineering-solvable, external-dependency, accepted limitation, or Human Approval.

### Exit condition
One internally consistent current matrix exists.
No completed work is restarted merely because an old register says OPEN.

---

## R1 — Resolve P2 executable-benchmark integration status

### Known evidence
PR #101 records:
- executable P2 intake;
- 19/19 designed fixtures;
- falsification suite;
- 30 clean -> 0 findings;
- 1/9 evasion probes caught;
- 8/9 missed;
- successful four-step CI.

### Required action
Independently verify:
1. the P2 executable files exist on the relevant PR branch;
2. source ZIP/payload hashes match the recorded manifest;
3. execution reproduces the recorded designed-fixture outcomes;
4. falsification results reproduce;
5. no result text describes 19/19 as general robustness;
6. the 8/9 misses remain preserved;
7. Benchmark V2 stays frozen as the POC engineering baseline.

### Critical rule
Do NOT repair the detector against those nine known probes and re-score those same nine as confirmatory performance.

If a genuine implementation bug is fixed:
- label the old probes development evidence;
- add regression tests for the bug;
- defer confirmatory performance measurement to fresh independently authored holdouts.

### Exit condition
P2 executability is either VERIFIED for its bounded POC scope or a precise reproducible failure is recorded.

---

## R2 — Verify P7 / CI as engineering evidence

### Required action
Reproduce or independently inspect:
1. original P7 harness;
2. Claude P7 regression v2;
3. executable P2 benchmark;
4. P2 falsification suite.

Verify the cited run IDs and job logs if accessible.

Do not use the original expected-versus-expected `scoring_sanity` check as evidence of detection performance.

### Exit condition
CI evidence is clearly separated into:
- structural/integration PASS;
- designed-fixture engineering PASS;
- falsification findings;
- scientific limitations.

---

## R3 — Close the Microsoft COVID preregistered-scan blocker

This is one of the highest-priority unresolved POC items.

### Step R3.1 — Review PR #104
Review the entire one-file workflow.

Verify:
- only `workflow_dispatch` trigger;
- `contents: read` permission;
- no push / pull_request / schedule trigger;
- secret is not printed;
- frozen blob check occurs before scanning;
- scanner executes only the preregistered rule;
- evidence artifact uploads only on success;
- no hidden write permission;
- no rule mutation.

Also assess action-version supply-chain risk.
If action pinning is changed, treat that as infrastructure hardening only and do not change the scientific rule.

### Step R3.2 — Human gate for infrastructure merge
If PR #104 is safe:
- recommend approval;
- DO NOT merge without explicit Human Approval.

### Step R3.3 — Dispatch frozen test
Only after the workflow exists on default `main`:

1. verify the workflow file on `main`;
2. verify the exact frozen rule blob;
3. verify the target branch/ref is the PR #103 Q5 branch;
4. dispatch the workflow manually;
5. do not edit the rule after seeing data;
6. capture workflow run ID, job ID, Python version/environment, commit/ref, exit code, artifact ID/hash, and logs;
7. download/read the result artifact;
8. verify the exact accession/filing set used;
9. verify the text source;
10. verify keyword normalization;
11. verify filing-section scope;
12. verify matching rule;
13. verify all returned binary results against the frozen rule.

### Step R3.4 — Independent review
Independently review the scan evidence.

Do not change Microsoft COVID from PARTIAL merely because the workflow exited 0.
The evidence must support the construct exactly as preregistered.

### Exit condition
Either:
- Microsoft COVID obtains evidence sufficient for its declared bounded assurance state; or
- it remains PARTIAL with an exact documented reason.

Do not invent a workaround if SEC/network/service access prevents execution.

---

## R4 — Resolve 264/264 evidence transparency

### Problem
The repository contains a historical claim that 264/264 published regression cells match author Stata output at published precision, but later reconciliation correctly noted that inspectable per-cell evidence must exist before this is treated as fully transparent verification.

### Required action
Search the repository, attached artifacts, public author replication package, and permitted sources for:
- article table cells;
- `3_output/logs` or equivalent author output;
- any existing machine-readable per-cell comparison.

If sufficient evidence exists:
1. hash the source files;
2. construct a per-cell comparison table;
3. record table / row / column / reported value / author-output value / tolerance / match;
4. verify 264 cells;
5. preserve the raw comparison artifact.

If the necessary exact source evidence is not available:
- do not recreate or guess it;
- leave the claim PARTIAL or CONSISTENT as supported;
- state exactly which file/input is missing.

### Exit condition
The claim is traceable to inspectable cell-level evidence, or the limitation is explicitly and correctly preserved.

---

## R5 — Reconcile Evidence Graph and assurance-state consistency

### Required action
Compare:
- Evidence Graph V1;
- v1.1 correction in PR #101;
- P4 report;
- P5 API outputs;
- Microsoft final JSON/CSV;
- phase register;
- release manifest.

Verify:
- FilingLag and COVID are separate claims;
- FilingLag evidence does not automatically verify COVID;
- 264/264 author-output claim uses the correct bounded assurance;
- non-canonical state labels are mapped, not silently rewritten as scientific upgrades;
- graph edges point to real evidence objects;
- every VERIFIED claim has a traceable evidence path.

### Exit condition
No contradictory assurance state exists across the canonical active artifacts.

---

## R6 — Finish GitHub / Google Drive reconciliation

### Historical issue
Earlier GitHub and Drive run ledgers diverged.
Backfill commits were later added.

### Required action
Verify, do not assume, that all previously identified gaps are now represented as additive backfills:
- 06:27 GitHub-only run;
- RUN 019;
- RUN 020;
- any later material run/CI evidence.

Rules:
- historical records remain immutable;
- backfill time must be distinct from original run time;
- backfills must cite the original source record;
- never represent a backfill as contemporaneous.

If Google Drive is accessible, perform readback.
If it is not accessible, say so and do not claim synchronization.

### Exit condition
A reconciliation ledger clearly identifies:
- both-system records;
- GitHub-only;
- Drive-only;
- backfilled;
- still missing.

---

## R7 — Build the final POC gate matrix

After R0-R6:

Re-evaluate all ten formal POC acceptance criteria from `MASTER_POC_V1_ROADMAP.md`.

For each criterion output:
- MET / PARTIAL / NOT_MET;
- evidence;
- test/run;
- limitations;
- remaining action.

### Important
Claude does NOT self-authorize `POC_COMPLETE`.

Claude may recommend:
- READY_FOR_HUMAN_POC_APPROVAL
or
- NOT_READY_FOR_HUMAN_POC_APPROVAL.

Only the human owner may approve the final transition.

---

# 7. V1 RECOVERY — DO NOT CONTINUE UNTIL POC HUMAN GATE

Historical RUN 021/022 attempted V1 Case 002 selection before POC closure.

That selected paper was actually the same paper as Case 001.

This duplication is CONFIRMED.

## V1-R1 — Preserve and correct duplicate Case 002

Preserve RUN 021 and RUN 022 unchanged as historical records.

Append a correction that:
- the selection duplicated Case 001;
- DOI = `10.1287/mnsc.2023.4670`;
- it does not count as a valid additional V1 case;
- V1 gained zero new valid cases from that selection.

Do not delete the historical runs.

## V1-R2 — Add machine-enforced DOI uniqueness

Before a new case can be accepted:
- Case DOI must be normalized;
- DOI must not match Case 001;
- DOI must not match any already accepted V1 case;
- duplicate DOI => hard selection failure.

Add a deterministic test.

## V1-R3 — Replace Case 002 and select Case 003

Only after POC Human Approval, identify two real additional replication cases.

Minimum selection requirements:
1. different DOI from Case 001 and each other;
2. public replication package;
3. documented table-to-code mapping;
4. executable Stata or Python path;
5. clear provenance;
6. at least one case should support a meaningful public-data independent-reproduction path rather than only licensed-data consistency checks;
7. no invented PASS where raw inputs remain restricted.

Before accepting each case, create a case-selection record with:
- citation;
- DOI;
- author repository/archive URL;
- software;
- data availability;
- execution path;
- table-code map;
- expected limitations;
- independent reproduction feasibility;
- DOI uniqueness test result.

---

# 8. ACCEPTED LIMITATIONS — DO NOT WASTE RETRIES

These are not ordinary bugs.

## L1 — Licensed/restricted full-paper inputs
If full independent reproduction requires WRDS, proprietary software, restricted source data, or another unavailable licensed input:

- preserve as PARTIAL;
- specify the missing dependency;
- verify all publicly verifiable subpaths;
- do not bypass licensing;
- do not fabricate a complete reproduction.

## L2 — Methodological validity
Statistical code execution does not settle methodological judgment.
Keep HUMAN_REVIEW where appropriate.

## L3 — V2 adversarial robustness
The known 8/9 missed probes are a real limitation.
Do not hide them.
Do not call V2 robust.
Fresh blinded probes belong in V1.4.

---

# 9. TWO-FAILURE FAIL-FORWARD RULE

For an engineering task:

- attempt 1;
- diagnose and make one materially different repair;
- attempt 2.

If the same blocker survives two consecutive attempts with no new information:

1. stop retrying that blocker in the current run;
2. record:
   - exact command/action;
   - exact error;
   - environment;
   - artifacts;
   - attempted fixes;
   - likely root cause;
   - exact next repair;
3. classify it:
   - HUMAN_QUEUE;
   - EXTERNAL_DEPENDENCY;
   - ACCEPTED_LIMITATION;
   - DEFERRED_ENGINEERING;
4. continue to the next scientifically admissible executable task in the SAME delivery gate.

Never mark a failed blocker PASS.

Do not advance to V1 merely to escape an unmet POC exit criterion unless the human owner explicitly changes the governance rule.

---

# 10. PR / MERGE RULES

1. One PR per scope.
2. Avoid duplicate overlapping PRs.
3. Do not revive #100 or #102 as active delivery PRs.
4. Compare #99 with #101 and preserve unique evidence without double-merging.
5. Keep #103 COVID-only.
6. Keep #104 infrastructure-only.
7. Never merge a PR merely because CI is green.
8. Before recommending a merge:
   - verify exact changed files;
   - verify scope;
   - verify CI/test evidence;
   - identify scientific limitations;
   - confirm no overlapping active writer.
9. Explicit Human Approval is required before merge to `main`.

---

# 11. FINAL REQUIRED OUTPUT FROM CLAUDE

Create a final additive file:

`NAAIL/research-assurance-mcp/derived/CLAUDE_RECOVERY_REPORT_<YYYY-MM-DD>.md`

It must contain:

## A. Executive status
- POC recommendation;
- number of criteria MET / PARTIAL / NOT_MET;
- V1 status;
- major accepted limitations.

## B. Resolved-item table
For each R0-R7:
- before state;
- action;
- evidence;
- after state;
- commit/PR/run;
- confidence/limitation.

## C. Open blocker table
Every remaining blocker with:
- severity;
- type;
- reason;
- owner;
- exact next action;
- whether Human Approval is required.

## D. Test evidence
- commands/workflows;
- run IDs;
- job IDs;
- environment;
- exit codes;
- artifacts;
- hashes where available.

## E. Scientific boundary statement
Explicitly repeat:
- 264/264 scope;
- Microsoft one-company scope;
- licensed-data limitation;
- methodological HUMAN_REVIEW;
- Benchmark V2 8/9 missed-probe limitation.

## F. PR recommendation
For #99, #101, #103, #104:
- MERGE_RECOMMENDED / DO_NOT_MERGE / SUPERSEDED / WAITING_FOR_HUMAN / WAITING_FOR_EVIDENCE;
- reason;
- exact next action.

## G. Final gate decision recommendation
Output exactly one:

`READY_FOR_HUMAN_POC_APPROVAL`

or

`NOT_READY_FOR_HUMAN_POC_APPROVAL`

Do not set `POC_COMPLETE = TRUE` yourself.

---

# 12. SUCCESS DEFINITION

This recovery is successful when:

1. no known solvable POC defect is left undocumented;
2. no stale register contradicts the verified evidence;
3. P2 and P7 evidence are reproducible and correctly scoped;
4. the frozen COVID protocol has either been validly executed or remains explicitly blocked with no unsafe workaround;
5. author-output evidence is transparent or correctly limited;
6. GitHub/Drive reconciliation is explicit;
7. the duplicate Case 002 is preserved as an error and cannot recur;
8. the final gate matrix is complete;
9. all failures and limitations remain visible;
10. the human owner receives a clean, evidence-backed decision package.

---

## 13. FIRST COMMAND / FIRST ACTION

Do not begin by editing.

Begin with a read-only inventory:

1. current `main` HEAD;
2. current project-folder tree;
3. open PRs #99/#101/#103/#104;
4. changed files for each;
5. CI/workflow evidence;
6. latest `phase_register.json`;
7. release manifest;
8. latest recovery/backfill records.

Then print:

`RECOVERY_BASELINE_RECONSTRUCTED`

with the initial unresolved-item table.

Only after that baseline is evidence-backed should you write repairs.
