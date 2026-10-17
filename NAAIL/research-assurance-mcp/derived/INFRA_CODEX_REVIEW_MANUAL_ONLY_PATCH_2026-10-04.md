# Codex Deep Review — manual-only patch

Date: 2026-10-04  
Prepared by: GPT repair operator  
Target: `.github/workflows/codex-review.yml`  
Current Git blob: `f3240a3fbb10201be2b9d4ba185461879f8a1cd7`

This is a **manual-only patch proposal for human application**. It is documentation only: it does not modify the live workflow, dispatch a review, merge a pull request, or approve scientific evidence.

## Purpose

The current workflow automatically runs on every pull-request synchronization. The proposed version runs only through `workflow_dispatch` with an explicit pull-request number. It validates that the target PR is open, non-draft, and internal to this repository before checking out the merge ref. The review remains read-only; only the separate publish job may post the resulting review comment.

## Exact replacement YAML

```yaml
name: Codex Deep PR Review

on:
  workflow_dispatch:
    inputs:
      pr_number:
        description: "Open internal pull request number to review"
        required: true
        type: number

# Human-dispatched, deep read-only review for one open internal pull request.
# Codex Cloud may also provide its own GitHub review; this workflow is the
# repository-controlled evidence/reproducibility review.

jobs:
  codex_review:
    name: Codex Deep Review
    runs-on: ubuntu-latest

    permissions:
      contents: read
      pull-requests: read

    outputs:
      final_message: ${{ steps.codex.outputs.final-message }}

    steps:
      - name: Resolve and validate requested pull request
        id: pr
        uses: actions/github-script@v9
        with:
          github-token: ${{ github.token }}
          script: |
            const number = Number("${{ inputs.pr_number }}");
            if (!Number.isInteger(number) || number < 1) {
              core.setFailed("pr_number must be a positive integer");
              return;
            }

            const { data: pr } = await github.rest.pulls.get({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: number,
            });

            if (pr.state !== "open") {
              core.setFailed(`PR #${number} is not open`);
              return;
            }
            if (pr.draft) {
              core.setFailed(`PR #${number} is still a draft`);
              return;
            }
            if (pr.head.repo.full_name !== `${context.repo.owner}/${context.repo.repo}`) {
              core.setFailed(`PR #${number} is not an internal repository PR`);
              return;
            }

            core.setOutput("number", String(number));
            core.setOutput("base_ref", pr.base.ref);
            core.setOutput("base_sha", pr.base.sha);
            core.setOutput("head_sha", pr.head.sha);

      - name: Checkout pull request merge ref
        uses: actions/checkout@v5
        with:
          fetch-depth: 1
          ref: refs/pull/${{ steps.pr.outputs.number }}/merge
          persist-credentials: false

      - name: Prefetch base and head refs
        shell: bash
        env:
          PR_BASE_REF: ${{ steps.pr.outputs.base_ref }}
          PR_NUMBER: ${{ steps.pr.outputs.number }}
        run: |
          set -euo pipefail
          git fetch --no-tags origin \
            "$PR_BASE_REF" \
            "+refs/pull/$PR_NUMBER/head"

      - name: Preflight — verify OpenAI API key
        shell: bash
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          if [ -z "$OPENAI_API_KEY" ]; then
            echo "::error::OPENAI_API_KEY is not configured. Add it under Settings > Secrets and variables > Actions."
            exit 1
          fi

      - name: Review pull request with OpenAI Codex
        id: codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          permission-profile: ":read-only"
          safety-strategy: "drop-sudo"
          working-directory: "."
          prompt: |
            Perform a deep, read-only review of pull request
            #${{ steps.pr.outputs.number }} in ${{ github.repository }}.

            Read the root AGENTS.md and any nested AGENTS.md files that govern
            changed paths.

            Review only changes between:
              Base: ${{ steps.pr.outputs.base_sha }}
              Head: ${{ steps.pr.outputs.head_sha }}

            Prioritize:
            1. correctness and runtime failures;
            2. exposed secrets, unsafe permissions, prompt/command injection,
               insecure file handling and dependency risks;
            3. research validity, reproducibility and provenance;
            4. look-ahead bias, temporal leakage, train/test contamination,
               fiscal-period alignment and unsupported causal claims;
            5. accounting, auditing, IFRS, PCAOB, CAM/KAM, ICFR, ESG, XBRL and
               SEC-data integrity where applicable;
            6. tests, CI, maintainability and documentation;
            7. distinction between evidence, model output, inference and human
               professional judgment.

            Do not edit files. Do not treat simulated results as real evidence.

            Return:
            ## Codex Deep PR Review
            ### Critical / High
            ### Medium / Low
            ### Research & reproducibility
            ### Security & data governance
            ### Tests & CI
            ### Recommended fixes
            ### Verdict

            Cite file paths and line ranges where possible. If no material
            issues are found, say so explicitly and list the checks performed.

  post_review:
    name: Publish Codex Deep Review
    runs-on: ubuntu-latest
    needs: codex_review
    if: needs.codex_review.outputs.final_message != ''

    permissions:
      issues: write
      pull-requests: write

    steps:
      - name: Post Codex review to pull request
        uses: actions/github-script@v9
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex_review.outputs.final_message }}
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: Number("${{ inputs.pr_number }}"),
              body: process.env.CODEX_FINAL_MESSAGE,
            });
```

## Exact unified diff

```diff
@@
 on:
-  pull_request:
-    types: [opened, synchronize, reopened, ready_for_review]
+  workflow_dispatch:
+    inputs:
+      pr_number:
+        description: "Open internal pull request number to review"
+        required: true
+        type: number
 
-# Deep read-only review for internal pull requests.
+# Human-dispatched, deep read-only review for one open internal pull request.
@@
   codex_review:
     name: Codex Deep Review
-    if: >-
-      github.event.pull_request.draft == false &&
-      github.event.pull_request.head.repo.full_name == github.repository
     runs-on: ubuntu-latest
 
     permissions:
       contents: read
+      pull-requests: read
@@
     steps:
+      - name: Resolve and validate requested pull request
+        id: pr
+        uses: actions/github-script@v9
+        with:
+          github-token: ${{ github.token }}
+          script: |
+            const number = Number("${{ inputs.pr_number }}");
+            if (!Number.isInteger(number) || number < 1) {
+              core.setFailed("pr_number must be a positive integer");
+              return;
+            }
+            const { data: pr } = await github.rest.pulls.get({
+              owner: context.repo.owner,
+              repo: context.repo.repo,
+              pull_number: number,
+            });
+            if (pr.state !== "open") {
+              core.setFailed(`PR #${number} is not open`);
+              return;
+            }
+            if (pr.draft) {
+              core.setFailed(`PR #${number} is still a draft`);
+              return;
+            }
+            if (pr.head.repo.full_name !== `${context.repo.owner}/${context.repo.repo}`) {
+              core.setFailed(`PR #${number} is not an internal repository PR`);
+              return;
+            }
+            core.setOutput("number", String(number));
+            core.setOutput("base_ref", pr.base.ref);
+            core.setOutput("base_sha", pr.base.sha);
+            core.setOutput("head_sha", pr.head.sha);
+
       - name: Checkout pull request merge ref
         uses: actions/checkout@v5
         with:
           fetch-depth: 1
-          ref: refs/pull/${{ github.event.pull_request.number }}/merge
+          ref: refs/pull/${{ steps.pr.outputs.number }}/merge
           persist-credentials: false
@@
         shell: bash
         env:
-          PR_BASE_REF: ${{ github.event.pull_request.base.ref }}
-          PR_NUMBER: ${{ github.event.pull_request.number }}
+          PR_BASE_REF: ${{ steps.pr.outputs.base_ref }}
+          PR_NUMBER: ${{ steps.pr.outputs.number }}
@@
             Perform a deep, read-only review of pull request
-            #${{ github.event.pull_request.number }} in ${{ github.repository }}.
+            #${{ steps.pr.outputs.number }} in ${{ github.repository }}.
@@
             Review only changes between:
-              Base: ${{ github.event.pull_request.base.sha }}
-              Head: ${{ github.event.pull_request.head.sha }}
+              Base: ${{ steps.pr.outputs.base_sha }}
+              Head: ${{ steps.pr.outputs.head_sha }}
@@
               owner: context.repo.owner,
               repo: context.repo.repo,
-              issue_number: context.payload.pull_request.number,
+              issue_number: Number("${{ inputs.pr_number }}"),
               body: process.env.CODEX_FINAL_MESSAGE,
```

## Human application and validation

1. A human applies the replacement to `.github/workflows/codex-review.yml` on a dedicated infrastructure scope.
2. Review the GitHub-generated workflow diff before merge.
3. After merge, manually dispatch once against one approved, open, non-draft internal PR.
4. Confirm the resolver rejects a draft, closed, missing, or fork PR.
5. Do not treat the review workflow’s success as scientific evidence or gate approval.

Status: `READY_FOR_HUMAN_APPLICATION`.
