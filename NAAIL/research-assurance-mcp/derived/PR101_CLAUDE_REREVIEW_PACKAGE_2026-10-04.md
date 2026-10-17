# PR #101 Claude Re-Review Package — 2026-10-04

Author: GPT repair operator. Independent decision remains with Claude.

## Additive A1 update at 2026-10-04T16:30:32Z

- PR #101 head before this packet: `88c7f0d750cba17ac883d14779361f667196cade`.
- Rebase state: BLOCKED, attempt 1/2, stable blocker `NAAIL-A1-PR101-REBASE-001`; PR was 12 commits ahead and 22 behind current `main` when checked. Exact repair is in `derived/OPEN_REPAIR_QUEUE.md`.
- Duplicate COVID workflow: absent from PR #101 changed-file list.
- Evidence Graph edge preserved: `RESULT_MSFT -> CODE_MSFT` = `partially_generated_by`.
- COVID limitation corrected additively: retrospective v1-R run `37204180146` regenerated all 10 FilingLag rows and COVID sensitivity outputs; claim remains PARTIAL pending Claude file/snippet review.
- Exact phase-register note added: “v1-R run 37204180146 regenerated all 10 FilingLag rows (pending Claude file review)”.
- FilingLag artifact: Git blob `f39916fad6b7b2f4e62be7e20f8db24be98a7033`; SHA-256 `2933ad5ec7e1d1bff11f43469b969966f8f869d820baa855a100a94b15757fc7`.
- Author-output consistency artifact: Git blob `7b268210c15a2426d0cd2ec8cd5ef5162b76e7ce`; SHA-256 `a2a9d5e47d79cc6c5d01d755c556d6fc5428335f0fd1f5c0b7d571d30f2946b1`.
- Corrected-head four-step CI: run `37216963901`, job `111479331104`, conclusion `success`.
- Four engineering steps all concluded success:
  1. P7 integration harness.
  2. Claude P7 regression v2.
  3. Executable P2 adversarial benchmark.
  4. P2 falsification suite.
- Scientific interpretation unchanged: Benchmark V2 remains frozen; 8 of 9 realistic error variants were missed; no detector-validation claim is made.
- Gate state unchanged: POC 7 MET / 3 PARTIAL / 0 NOT_MET; POC_COMPLETE = FALSE; V1_COMPLETE = FALSE.

## Prior package with full requested diffs

The prior package is reproduced verbatim below so the full `phase_register.json` and concurrency-protocol diffs remain in this single review file.

---

# PR #101 Independent Re-Review Evidence — 2026-10-04

Author: GPT repair operator.
Purpose: satisfy Claude independent-review requests without claiming independent approval.

## Current PR #101

- Head branch: `naail/research-assurance-pr-a-q1-q2-q4`
- Head SHA at evidence preparation: `ab9c4ecebec6f363aa290de2d0bb265d79401d93`
- Exact changed-file count: 14
- Changed files:
  - `.github/workflows/naail_research_assurance_p7.yml`
  - `NAAIL/research-assurance-mcp/case-001-management-science/P0_CASE001_FREEZE.md`
  - `NAAIL/research-assurance-mcp/derived/CLAUDE_ARTIFACT_INTAKE_MANIFEST_2026-10-02.md`
  - `NAAIL/research-assurance-mcp/derived/DECISION_BENCHMARK_V2_V3_2026-10-02.md`
  - `NAAIL/research-assurance-mcp/derived/NONCANONICAL_ASSURANCE_LABEL_MAPPING_2026-10-02.md`
  - `NAAIL/research-assurance-mcp/derived/PR_A_Q1_Q2_Q4_CI_EVIDENCE_2026-10-02.md`
  - `NAAIL/research-assurance-mcp/derived/claude_2026-10-02/p2_executable/MANIFEST_P2.md`
  - `NAAIL/research-assurance-mcp/derived/claude_2026-10-02/p2_executable/falsification_result.json`
  - `NAAIL/research-assurance-mcp/derived/claude_2026-10-02/p2_executable/p2_adversarial_v2_executable.py`
  - `NAAIL/research-assurance-mcp/derived/claude_2026-10-02/p2_executable/p2_falsification.py`
  - `NAAIL/research-assurance-mcp/derived/claude_2026-10-02/p2_executable/p2_result.json`
  - `NAAIL/research-assurance-mcp/evidence-graph/evidence_graph_v1_1_case001.json`
  - `NAAIL/research-assurance-mcp/hourly-build/CONCURRENCY_SINGLE_WRITER_PROTOCOL_2026-10-02.md`
  - `NAAIL/research-assurance-mcp/phase_register.json`

## Evidence path proof

### Microsoft FilingLag independent check v2

Path exists at PR #101 head:

`NAAIL/research-assurance-mcp/derived/claude_2026-10-02/msft_filinglag_independent_check_v2.json`

- Git blob: `f39916fad6b7b2f4e62be7e20f8db24be98a7033`
- Fresh SHA-256 from repository file bytes: `2933ad5ec7e1d1bff11f43469b969966f8f869d820baa855a100a94b15757fc7`
- Expected SHA-256: `2933ad5ec7e1d1bff11f43469b969966f8f869d820baa855a100a94b15757fc7`
- Result: **MATCH**

### Author-output consistency JSON

Path exists at PR #101 head:

`NAAIL/research-assurance-mcp/case-001-management-science/verification/author_output_consistency_v01.json`

- Git blob: `7b268210c15a2426d0cd2ec8cd5ef5162b76e7ce`
- Fresh SHA-256 from repository file bytes: `a2a9d5e47d79cc6c5d01d755c556d6fc5428335f0fd1f5c0b7d571d30f2946b1`
- Result: **PATH_AND_BYTES_VERIFIED**
- Scientific treatment remains bounded by the 2026-10-04 Option B correction: aggregate author-output consistency is PARTIAL for the current POC because the per-cell source evidence is not currently inspectable.

## Claude-required #101 corrections applied

1. Removed `.github/workflows/naail_msft_covid_scan.yml` from #101; PR #104 remains the infrastructure-only workflow scope.
2. In Evidence Graph v1.1, `RESULT_MSFT -> CODE_MSFT` relation changed from `generated_by` to `partially_generated_by`.
3. Added `LIMIT_MSFT_10ROW_GENERATOR`: no in-repository generator currently reproduces the complete 10-row `msft_one_company_final.csv`; the historical script covers four observations.
4. Updated `LIMIT_COVID_RULE`: the rule is already frozen; remaining condition is execution of the preregistered scan plus independent review.
5. Added an additive Option B correction to `P0_CASE001_FREEZE.md`; no unavailable 264-cell evidence was reconstructed.
6. Updated `phase_register.json` to record Option B while retaining POC = 7/10 and `POC_COMPLETE=false`.

## Full requested diff — phase_register.json

```diff
@@ -5,56 +5,68 @@
   "schedule": "hourly",
   "current_gate": "POC",
   "current_baseline": {
-    "case_001_author_output_consistency": "VERIFIED",
+    "case_001_author_output_consistency": "PARTIAL",
     "case_001_regression_cells": "264/264",
     "case_001_full_reproduction": "PARTIAL",
-    "microsoft_sec_one_company": "COMPLETE"
+    "microsoft_sec_one_company": "PARTIAL",
+    "case_001_regression_cells_evidence": "Documented limitation accepted for POC on 2026-10-04 (Option B); no inspectable per-cell comparison artifact currently available; do not reconstruct unavailable cells.",
+    "microsoft_filinglag": "VERIFIED",
+    "microsoft_covid": "PARTIAL"
   },
   "poc_tasks": [
     {
       "id": "P0",
       "name": "Freeze Case 001",
-      "status": "IN_PROGRESS"
+      "status": "PARTIAL",
+      "evidence_basis": "READBACK-VERIFIED repository artifacts; canonical POC gate remains 7 of 10 met"
     },
     {
       "id": "P1",
       "name": "Error Taxonomy V2",
-      "status": "OPEN"
+      "status": "VERIFIED",
+      "evidence_basis": "READBACK-VERIFIED repository artifacts; canonical POC gate remains 7 of 10 met"
     },
     {
       "id": "P2",
       "name": "Adversarial Benchmark V2",
-      "status": "OPEN"
+      "status": "CONSISTENT",
+      "evidence_basis": "CI-EVIDENCE run 37004149967, job 110828395512; 19/19 designed synthetic fixtures met outcome rules; falsification suite: 30 clean packages with 0 findings, 1/9 evasion probes caught and 8/9 missed; engineering evidence only."
     },
     {
       "id": "P3",
       "name": "Evidence Graph V1",
-      "status": "OPEN"
+      "status": "VERIFIED",
+      "evidence_basis": "READBACK-VERIFIED repository artifacts; canonical POC gate remains 7 of 10 met"
     },
     {
       "id": "P4",
       "name": "Research Assurance Report V1",
-      "status": "OPEN"
+      "status": "CONSISTENT",
+      "evidence_basis": "READBACK-VERIFIED repository artifacts; canonical POC gate remains 7 of 10 met"
     },
     {
       "id": "P5",
       "name": "Minimal MCP/API layer",
-      "status": "OPEN"
+      "status": "CONSISTENT",
+      "evidence_basis": "READBACK-VERIFIED repository artifacts; canonical POC gate remains 7 of 10 met"
     },
     {
       "id": "P6",
       "name": "End-to-end Case 001 demo",
-      "status": "OPEN"
+      "status": "CONSISTENT",
+      "evidence_basis": "READBACK-VERIFIED repository artifacts; canonical POC gate remains 7 of 10 met"
     },
     {
       "id": "P7",
       "name": "POC tests and QA",
-      "status": "OPEN"
+      "status": "VERIFIED",
+      "evidence_basis": "CI-EVIDENCE run 37004149967, job 110828395512; four engineering steps exit 0 on CPython 3.12.14; scientific scope guards unchanged."
     },
     {
       "id": "P8",
       "name": "Freeze POC release",
-      "status": "OPEN"
+      "status": "PARTIAL",
+      "evidence_basis": "READBACK-VERIFIED repository artifacts; canonical POC gate remains 7 of 10 met"
     }
   ],
   "v1_tasks": [
@@ -123,5 +135,59 @@
     "author-output consistency != independent reproduction",
     "computational correctness != methodological validity",
     "no protected-main merge without explicit authorization"
-  ]
-}
\ No newline at end of file
+  ],
+  "changelog": [
+    {
+      "date": "2026-10-02",
+      "change_id": "Q4-EVIDENCE-GRAPH-V1.1",
+      "change": "Correct Microsoft one-company baseline and record Evidence Graph v1.1 split.",
+      "previous": {
+        "microsoft_sec_one_company": "COMPLETE"
+      },
+      "current": {
+        "microsoft_sec_one_company": "PARTIAL"
+      },
+      "rationale": "FilingLag is VERIFIED for the 10 frozen observations, but the COVID classification remains PARTIAL until the preregistered primary-filing scan is executed.",
+      "evidence": "evidence-graph/evidence_graph_v1_1_case001.json"
+    },
+    {
+      "date": "2026-10-02",
+      "change_id": "Q4-STATUS-EVIDENCE-RECONCILIATION",
+      "change": "Refresh stale POC task states; retain FilingLag VERIFIED, COVID PARTIAL, and the uninspectable author-output cell claim PARTIAL.",
+      "evidence": [
+        "evidence-graph/evidence_graph_v1_1_case001.json",
+        "derived/NONCANONICAL_ASSURANCE_LABEL_MAPPING_2026-10-02.md",
+        "derived/CLAUDE_ARTIFACT_INTAKE_MANIFEST_2026-10-02.md",
+        "CI run 37004149967, job 110828395512"
+      ],
+      "note": "Task states describe bounded artifact/engineering evidence, not a POC-completion decision."
+    },
+    {
+      "date": "2026-10-02",
+      "change_id": "Q4-FOUR-STEP-CI-RECONCILIATION",
+      "change": "Bind Q4 corrected states to the four-step engineering CI including the P2 falsification suite.",
+      "evidence": [
+        "CI run 37004149967",
+        "job 110828395512",
+        "CPython 3.12.14"
+      ],
+      "note": "POC criteria remain 7 of 10; Q5 Microsoft COVID remains separate and PARTIAL."
+    },
+    {
+      "date": "2026-10-04",
+      "change_id": "OPTION-B-264-DOCUMENTED-LIMITATION",
+      "change": "Record the human-selected Option B treatment for the historical 264/264 author-output consistency statement.",
+      "current": {
+        "case_001_author_output_consistency": "PARTIAL"
+      },
+      "rationale": "Current POC lacks inspectable per-cell comparison evidence; the claim remains bounded author-output consistency and is not reconstructed or promoted to independent reproduction.",
+      "evidence": "case-001-management-science/P0_CASE001_FREEZE.md",
+      "note": "POC criteria remain 7 of 10 until the remaining COVID and final release/synchronization gates are resolved."
+    }
+  ],
+  "poc_criteria_met": 7,
+  "poc_criteria_total": 10,
+  "POC_COMPLETE": false,
+  "V1_COMPLETE": false,
+  "v1_criteria_met": 0
+}
```

## Full requested diff — CONCURRENCY_SINGLE_WRITER_PROTOCOL_2026-10-02.md

```diff
@@ -0,0 +1,42 @@
+# Concurrency incident and single-writer protocol — 2026-10-02
+
+## Incident evidence
+
+- PR #100 was closed at **2026-10-02T12:06:39Z** (**14:06:39 Europe/Stockholm**).
+- GitHub records the actor as account `Saehon`.
+- PR #102 was created at **2026-10-02T12:06:37Z**, two seconds before the #100 closure.
+- The NAAIL hourly automation's prior recorded run was around **13:31 Europe/Stockholm** and its next hourly cadence was later; therefore the #100 closure is not attributable to that scheduled run.
+- GitHub does not expose a ChatGPT/session identifier for the mutation. The strongest supported attribution is: **the concurrent interactive operator activity that created PR #102 also closed PR #100**. No more specific process identity is asserted.
+
+## Single-writer rule
+
+Canonical working branch: `naail/research-assurance-case-001`.
+
+Before any scheduled/hourly mutation, read:
+`NAAIL/research-assurance-mcp/hourly-build/LOCK.json`.
+
+If the lock exists with:
+- `active: true`,
+- an owner different from the hourly operator, and
+- an unexpired `expires_at`,
+
+the hourly run must **NO-OP**. It must not:
+- edit or commit files;
+- open, close, reopen, or modify pull requests;
+- rerun or trigger CI;
+- write Google Drive project records;
+- delete or overwrite another operator's lock.
+
+Interactive writers acquire the lock before mutations and release it at the end of the controlled session. Stale locks must be handled explicitly; they must not be silently ignored.
+
+The active NAAIL hourly automation was updated on 2026-10-02 to enforce this rule before all GitHub/Drive writes.
+
+## PR scope rule
+
+Exactly one pull request per approval scope:
+- **PR A #101** — Q1/Q2/Q4 engineering, records, deterministic regression CI, and concurrency governance.
+- **PR B #103** — Q5 Microsoft COVID only.
+
+Overlapping PRs #100 and #102 are closed without merge and point to PR A / PR B.
+
+No merge is authorized by this record.
```

## Independence

This packet is operator evidence only.

Required next review state:

`INDEPENDENT_REVIEW_PENDING (Claude)`

Do not merge #101 without explicit human approval after Claude re-review.
