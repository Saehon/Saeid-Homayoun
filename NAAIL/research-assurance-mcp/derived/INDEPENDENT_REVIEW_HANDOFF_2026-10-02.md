# Independent Review Handoff — NAAIL Research Assurance MCP

Source: Claude handoff supplied by user on 2026-10-02, plus GPT live verification against the active GitHub research-assurance branch and canonical Google Drive records.

## Status rule
Treat this packet as evidence to verify. Do not overwrite historical run logs. Corrections and backfills must be additive and timestamped.

## 1. Critical corrections

### 1.1 Case 002 duplicates Case 001 — CONFIRMED
RUN 021 selected deHaan, de Kok, Matsumoto & Rodriguez-Vazquez, “How Resilient Are Firms’ Financial Reporting Processes?”, Management Science (2023), DOI 10.1287/mnsc.2023.4670, as Case 002.

The canonical Case 001 Google Drive master record identifies the same paper and DOI 10.1287/mnsc.2023.4670.

Required correction:
- preserve RUN 021 unchanged;
- append a correction stating RUN 021 duplicated Case 001;
- V1 currently has zero valid additional cases from that selection;
- add machine-enforced DOI uniqueness to future case selection: duplicate DOI => selection fails.

### 1.2 Microsoft FilingLag vector — CONFIRMED
Canonical master-plan definition is comparison with the SAME 2019 QUARTER.
Correct post-period vector:
+5, -2, +4, -3, +3, -3.

The current Microsoft final reconstruction in the branch uses that same vector.

Do not use the incorrect [+5, -2, +4, -3, -2, -1] vector.

### 1.3 FilingLag definition — PARTIALLY RESOLVED
The project’s current Case 001 materials define FilingLag as:
“filing date minus fiscal period end.”

The Microsoft acquisition helper uses the SEC/EdgarTools filing_date field. Current records do not define an acceptance-timestamp or after-hours roll-forward rule.

Therefore:
- operational date field = SEC filing date;
- acceptance timestamp is not part of the documented current construct;
- the freeze should explicitly state this to prevent future ambiguity.

### 1.4 COVID presence — DOWNGRADE REQUIRED
The current Microsoft final JSON states:
“binary presence of covid/corona in SEC filing text.”

However, the current frozen records do not specify the exact filing sections searched or a complete text-matching protocol. The binary COVID result therefore remains insufficiently documented for independent verification.

Recommended state: PARTIAL until the keyword normalization, section scope, text source, and matching rule are frozen and independently rerun.

### 1.5 Assurance labels
Allowed project assurance states remain:
VERIFIED / CONSISTENT / PARTIAL / FLAGGED / HUMAN_REVIEW.

“REGENERATED” may be used only as an evidence-class description, not as an assurance state.

“MICROSOFT_PUBLIC_RECONSTRUCTION = COMPLETE” is too broad if it includes the under-specified COVID binary. Filing dates/FilingLag/same-quarter changes may be separately assured; the combined reconstruction should remain PARTIAL until the COVID rule is independently frozen and tested.

### 1.6 Dual-save ledger divergence — CONFIRMED
GitHub contains 0627_POC_P9_final_inventory.md, but the canonical Drive Master Log has no separate 06:27 run entry.

Drive contains RUN 019 (09:31) and RUN 020 (10:26), while the GitHub 2026-10-02 hourly folder does not contain corresponding run files.

Required treatment:
- preserve original records;
- create additive backfill records with actual backfill time;
- identify the original source run in each backfill;
- never present a backfill as contemporaneous.

### 1.7 Canonical numbering — RESOLVED
The canonical Google Drive Accelerated POC & V1 Master Plan uses:
- POC: P0–P8
- V1: V1.1–V1.11

Use this numbering scheme in future canonical records. P9 may remain only as a legacy/log label where already present, not as a new canonical phase.

### 1.8 Fail-forward scope
The canonical master plan says:
“Stay on the current gate until exit criteria are met.”
“If blocked, preserve the blocker and immediately move to another executable task in the same gate.”

This is the canonical fail-forward rule. Advancing to V1 while a POC exit criterion remains unmet should be treated as non-canonical unless explicitly approved by the human owner.

### 1.9 P8 manifest provenance — RESOLVED
POC_RELEASE_MANIFEST.md was introduced by GitHub commit:
959c74390c0757732c1b6813f124085253199f56
Commit message: “NAAIL P8: add POC release manifest”
Git author timestamp: 2026-10-02T05:30:53Z (07:30:53 Europe/Stockholm).

## 2. P7 workflow verification

The active branch contains:
NAAIL/research-assurance-mcp/p7/test_poc_integration.py

The research-assurance branch contains many pre-existing repository workflows, but the research-assurance branch diff versus main adds no .github/workflows file. No workflow specific to this P7 harness was added with the research-assurance project.

Result:
P7 repository CI PASS is NOT established.

A minimal inactive workflow candidate is stored separately under:
NAAIL/research-assurance-mcp/derived/P7_WORKFLOW_CANDIDATE.yml

It is intentionally not placed under .github/workflows; a human must review and activate it.

## 3. P2 benchmark execution status

NAAIL/research-assurance-mcp/benchmark/adversarial_benchmark_v2.json contains 19 static benchmark fixture specifications across:
clean_control / single / compound / blinded.

The benchmark directory currently contains only that JSON specification. No executable mutation generator is present in the V2 benchmark directory.

Older Case 001 benchmark code exists under case-001-management-science/benchmark, but it is not the executable generator for the 19-fixture V2 schema.

Conclusion:
- V2 fixtures are currently static specification records;
- executable mutation generation for the V2 schema remains open;
- the Claude candidate mutation script cannot be integrated until its actual bytes are attached or otherwise located.

## 4. Independent Microsoft evidence supplied in handoff

Definition assumed by independent reviewer:
FilingLag = EDGAR Filing Date − fiscal period end, in calendar days.

Reported 10 observations:
Q1-2019 10-Q 2019-03-31 filed 2019-04-24 lag 24
Q2-2019 10-K 2019-06-30 filed 2019-08-01 lag 32
Q3-2019 10-Q 2019-09-30 filed 2019-10-23 lag 23
Q4-2019 10-Q 2019-12-31 filed 2020-01-29 lag 29
Q1-2020 10-Q 2020-03-31 filed 2020-04-29 lag 29
Q2-2020 10-K 2020-06-30 filed 2020-07-30 lag 30
Q3-2020 10-Q 2020-09-30 filed 2020-10-27 lag 27
Q4-2020 10-Q 2020-12-31 filed 2021-01-26 lag 26
Q1-2021 10-Q 2021-03-31 filed 2021-04-27 lag 27
Q2-2021 10-K 2021-06-30 filed 2021-07-29 lag 29

Changes vs same 2019 quarter:
+5, -2, +4, -3, +3, -3.

LateFiler = 0 for all ten observations.

Independent handoff classification:
CONSISTENT for FilingLag reconstruction until the project definition/date-field rule is explicitly frozen.

Important robustness point:
A constant level offset can cancel in year-over-year changes, so a 6/6 change-vector match cannot by itself prove the level definition. Level checks against EDGAR dates are required.

LateFiler is non-discriminating for Microsoft because observed lags are far inside standard deadlines.

The erroneous 2020-baseline vector [+5,-2,+4,-3,-2,-1] should be retained as a naturally occurring benchmark fixture, not as the correct project result.

## 5. Expected external artifacts from Claude — NOT YET AVAILABLE IN THIS CHAT

Expected filenames and supplied SHA-256 values:
- msft_filinglag_independent_check.json
  84228cfdb32b1a7111b822a4be14ed6ddb3663ffda805a29adcefd55d281c731
- msft_filinglag_independent_check_v2.json
  2933ad5ec7e1d1bff11f43469b969966f8f869d820baa855a100a94b15757fc7
- p2_candidate_msft_mutations.py
  51f4478b8ef9f199de5e8f8ab1c8690483ce5c4c6a0013f405b4796a08f49e68
- p2_candidate_msft_mutation_results.json
  e823299c5a3bed917847a4790fcebb31c9ef0083435d80757e17bcf7414bdb10

Status:
The four files are not visible as conversation attachments, Library files, Google Drive files, or GitHub files in the current review pass. Their hashes are therefore recorded as expected external evidence only. Do not fabricate or recreate bytes and do not claim hash verification.

## 6. Required next actions

1. Human-review and activate the P7 workflow candidate; only then run the repository harness and record command/environment/exit code/output.
2. Attach or locate the four Claude artifacts; verify SHA-256 by readback before committing under derived/.
3. Freeze Case 001 construct definitions:
   - FilingLag date field = SEC filing date;
   - acceptance timestamp treatment;
   - COVID keyword normalization;
   - filing sections/text source searched.
4. Integrate the candidate mutation generator into the existing V2 benchmark schema without replacing static fixtures.
5. Complete the additive ledger reconciliation backfills.
6. Add a stop rule: same blocker surviving two consecutive runs with no new information => human queue.
7. Replace the duplicate Case 002 selection. Case 002 and Case 003 must have different DOIs from Case 001, public replication packages with table-to-code mapping, Stata or Python, and at least one case that can exercise a public-data independent-reproduction path.

## 7. Current project status after this review

POC_COMPLETE = FALSE
Reason: no repository P7 CI execution evidence; ledger reconciliation required; combined Microsoft reconstruction includes an under-specified COVID binary.

V1_COMPLETE = FALSE
Reason: RUN 021 duplicated Case 001; zero valid additional cases have been established by that selection.

No prior historical run record is modified by this packet.
