# GPT Operator — Independent Review Package for Claude

**Date:** 2026-10-04  
**Author:** GPT repair operator  
**Independence state:** All GPT-authored/operator-managed material below is **INDEPENDENT_REVIEW_PENDING (Claude)**.

## 1. PR #101 identity

Head: `b58e36d69409de5a09dba9f43eaf13a7004243a5`

Exact changed files:
- `.github/workflows/naail_msft_covid_scan.yml`
- `.github/workflows/naail_research_assurance_p7.yml`
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

## 2. Evidence Graph v1.0 → v1.1

Source v1 Git blob:
`32c751b574cd3db3eb283c9a8e5a83a3b8a65475`

Proposed v1.1 Git blob:
`861a34245fbe8cea8e06911d886cfa9b9303c86b`

Exact line-oriented comparison:
`NAAIL/research-assurance-mcp/derived/GPT_EVIDENCE_GRAPH_V1_TO_V1_1_DIFF_2026-10-04.diff`

Review focus:
- CLAIM_AOC: VERIFIED → PARTIAL.
- RESULT_AOC: VERIFIED → PARTIAL.
- Adds VERIFICATION_AOC as PARTIAL.
- Single Microsoft claim split to FilingLag VERIFIED and COVID PARTIAL.
- DATA_MSFT PARTIAL because unresolved COVID values coexist with verified FilingLag fields.
- Adds LIMIT_COVID_RULE.
- Adds independent FilingLag verification reference.
- Validation changes from 13 nodes/13 edges to 17 nodes/18 edges.

## 3. PR #101 edit to original P7 workflow

Exact patch:
`NAAIL/research-assurance-mcp/derived/GPT_P7_WORKFLOW_PATCH_2026-10-04.diff`

The edit:
- expands push paths to the Claude-derived executable evidence;
- retains the original P7 harness;
- adds explicit exit-code capture;
- adds Claude P7 regression v2;
- adds executable P2 benchmark;
- adds P2 falsification.

Important interpretation:
- original P7 `scoring_sanity` = SELF_CONSISTENCY_CHECK, not detection evidence.
- 19/19 designed fixtures = bounded engineering evidence only.
- fresh falsification = 1/9 caught, 8/9 missed.

## 4. PR #104 — complete YAML, unedited

PR #104 head:
`2bdd1b3bf4ece2adb4832c90dc5ccb784467353e`

Changed-file count:
**1**

File:
`.github/workflows/naail_msft_covid_scan.yml`

Git blob:
`82db9f718e48a1e1946026a7fa83c47eb7d559f7`

```yaml
name: NAAIL Microsoft COVID Scan

on:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  msft-covid-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Verify frozen COVID rule
        shell: bash
        run: |
          expected="d7760b4909ae84896cae8797fb8536f59d36053c"
          actual="$(git hash-object NAAIL/research-assurance-mcp/derived/covid_rule_v1.json)"
          echo "expected_blob=$expected"
          echo "actual_blob=$actual"
          if [ "$actual" != "$expected" ]; then
            echo "Frozen covid_rule_v1.json blob mismatch" >&2
            exit 1
          fi

      - name: Run preregistered Microsoft COVID scan
        shell: bash
        env:
          EDGAR_IDENTITY: ${{ secrets.EDGAR_IDENTITY }}
        run: |
          set +e
          python NAAIL/research-assurance-mcp/derived/msft_covid_scan.py
          rc=$?
          echo "exit_code=$rc"
          exit "$rc"

      - name: Upload Microsoft COVID scan evidence
        if: success()
        uses: actions/upload-artifact@v4
        with:
          name: msft-covid-scan-evidence
          path: NAAIL/research-assurance-mcp/derived/msft_covid_scan_result.json
          if-no-files-found: error
```

### GPT operator checklist for #104

| Requirement | Operator result | YAML lines |
|---|---|---|
| manual-only workflow_dispatch | PASS | 3–4 |
| read-only contents permission | PASS | 6–7 |
| no push / pull_request / schedule | PASS | 3–4 |
| secret is not printed | PASS | 33–42; environment injection at 35–36 |
| frozen blob verified before scan | PASS | 21–31 |
| scanner executes preregistered path | PASS | 33–42, command at 39 |
| evidence upload only on success | PASS | 44–50 |
| no repository contents write permission | PASS | 6–7 |
| frozen rule is not mutated | PASS | 21–31 |

Actions are **not pinned to full commit SHAs**:
- `actions/checkout@v4`;
- `actions/setup-python@v5`;
- `actions/upload-artifact@v4`.

Treat this only as hardening advice. Do not alter the frozen scientific rule because of it. Dependabot #81/#83/#84 are out of scope.

## 5. R1/R2 fresh execution evidence

Run:
`37197307006`

Job:
`111421719443`

Execution commit:
`51ff7fc460d9f950030d3f3ab084e277101656e1`

Base current PR #101 head:
`b58e36d69409de5a09dba9f43eaf13a7004243a5`

The execution commit differs from the #101 head by exactly one non-scientific trigger record:
`NAAIL/research-assurance-mcp/derived/claude_2026-10-02/GPT_REEXECUTION_TRIGGER_2026-10-04.md`.

Python:
CPython 3.12.14

Commands:
```text
python NAAIL/research-assurance-mcp/p7/test_poc_integration.py
exit_code=0
source_git_blob=ddbc5fbebf9f33916c9c9af7a2f34762aa95d911

python NAAIL/research-assurance-mcp/derived/claude_2026-10-02/p7_regression_v2.py NAAIL/research-assurance-mcp NAAIL/research-assurance-mcp/derived/claude_2026-10-02
exit_code=0
source_git_blob=b76ced76a75f6c15562cd324bbd99b8bb9457958

python NAAIL/research-assurance-mcp/derived/claude_2026-10-02/p2_executable/p2_adversarial_v2_executable.py NAAIL/research-assurance-mcp
exit_code=0
source_git_blob=bc9e06cb68dedf3308ceb624ce6ff99c6c71a599
manifest_sha256=0e22e75139dc2c827a4badfa66cd888bb3d63ae54fc1651e850e706196bfc1b8

python NAAIL/research-assurance-mcp/derived/claude_2026-10-02/p2_executable/p2_falsification.py NAAIL/research-assurance-mcp
exit_code=0
source_git_blob=aa2683aff65dd54e31c7fc7c0ffe766030901ccf
manifest_sha256=b7d6f17c85367818d8834c4aacd013858cfc0ac17991a30dcfc407b33eafa8ee
```

Benchmark source:
- Git blob `b90ee73073907baa5f577b0534b766ae29ed278b`;
- manifest SHA-256 `6237d06b0fbad0f236446df246d8f4fbdf4ee9256241be4706b7934e0ce06013`.

Observed fresh results:
- original P7 PASS;
- original P7 scoring_sanity 1.0/1.0/1.0 = SELF_CONSISTENCY_CHECK ONLY;
- Claude v2 blocking failures = [];
- 19/19 designed fixture outcome rules met;
- 30 clean packages, 0 with findings;
- 9 evasion probes, 1 caught, **8 missed**;
- detected taxonomy IDs deterministic across reruns.

No detector tuning was performed against the nine probes.

## 6. #99 vs #101

#99 head:
`c7f04eff3bfa075126cba6100210d3b1f96235a6`

Unique paths in #99:
- `NAAIL/research-assurance-mcp/derived/claude_2026-10-02/GPT_P2_VERIFICATION_2026-10-02.md` — Git blob `af9ddc198874b01851e9e1947f70c242f4fa1c4c`.
- `NAAIL/research-assurance-mcp/derived/claude_2026-10-02/derived_claude_2026-10-02_p2.zip` — Git blob `277295be2b55728c8a8ecdc5725157c40abdc49d`.

No changed-path overlap exists with #101.

Therefore:
- do **not** label #99 SUPERSEDED under the owner's rule;
- operator recommendation = DO_NOT_MERGE as-is;
- preserve desired unique historical evidence deliberately before closure.

## 7. PR #101/#104 overlap

PR #101 and PR #104 contain the same workflow file with the same Git blob:
`82db9f718e48a1e1946026a7fa83c47eb7d559f7`.

This is a one-PR-per-scope governance issue.

Claude should advise whether:
- #104 remains the sole infrastructure registration PR, followed by cleanup/rebase of #101;
- or another explicit scope disposition is preferable.

GPT made no silent scope edit.

## 8. R3 state

Frozen rule on #103:
- Git blob `d7760b4909ae84896cae8797fb8536f59d36053c`;
- status inside rule: FROZEN_PREREGISTERED.

Scanner on #103:
- Git blob `1b65c3cc60b0305aed244a642923ea50c95b0045`.

Planned command:
```text
python NAAIL/research-assurance-mcp/derived/msft_covid_scan.py
```

Execution:
**NOT_EXECUTED — BLOCKED_HUMAN_QUEUE**.

No SEC text, document SHA-256, match count, binary flag or snippet was generated by this recovery run.

## 9. R4 state

The accessible repository contains the aggregate 264/264 statement but no machine-readable per-cell comparison artifact.

Drive search did not locate:
- `EBSCO-FullText-2026-10-01.pdf`;
- the raw `3_output/logs/c_2a_run_regressions_main.smcl` file.

Only references to those names were found.

Operator disposition:
- do not reconstruct;
- keep author-output consistency PARTIAL;
- human chooses full-evidence option A or documented-limitation option B.

## 10. Microsoft fiscal/form check

Six matched-quarter changes:
- +5: 10-Q vs 10-Q;
- -2: 10-K vs 10-K;
- +4: 10-Q vs 10-Q;
- -3: 10-Q vs 10-Q;
- +3: 10-Q vs 10-Q;
- -3: 10-K vs 10-K.

None compares a 10-K to a 10-Q.

## 11. Drive readback evidence

Live Drive records read:
- Master Plan: `1LnvGBKB41KZVLL2DT3dOVBX-vJ7_QIbZmhIprHlldfI`;
- Master Log: `1FV8qyLJaxDVbOuh_FBkKVcD1bcDPoHQRI4VPabG1vNI`;
- Case 001 Master: `1B1d9imxK1MBYGx-AurACBlKgC51vHH_G_iOpINU64A0`;
- Independent Handoff/Reconciliation: `1PGjtVOA5FQA_YTcGaN7xUuq4l_q99h26erkOZN_7jxA`.

Master Log contains RUN 019 and RUN 020.
GitHub contains additive backfills for the 06:27 Drive gap and the RUN 019/020 GitHub gap.
No historical record was rewritten.

## Requested independent-review output

Please return separately for PR #101 and PR #104:
- APPROVE;
- REJECT; or
- CHANGES_REQUIRED.

Also state whether the current project remains:
- 7 MET / 3 PARTIAL / 0 NOT_MET out of 10;
- NOT_READY_FOR_HUMAN_POC_APPROVAL before R3 execution.

NOT_READY_FOR_HUMAN_POC_APPROVAL
