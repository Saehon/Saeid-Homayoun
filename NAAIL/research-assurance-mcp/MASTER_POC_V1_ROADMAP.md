# NAAIL Research Assurance MCP — Accelerated POC & V1 Master Plan

## Objective
Finish a scientifically defensible working POC as fast as possible, then immediately build V1. Execution is hourly in bounded ~15-minute work packets.

## Current verified baseline
- Case 001: deHaan et al. (2023), Management Science.
- Author-output consistency: VERIFIED.
- 264/264 checked published regression cells match author Stata output at published precision.
- Full raw-data independent reproduction: PARTIAL / blocked by missing licensed source data and proprietary runtimes.
- Microsoft-only SEC reconstruction: COMPLETE.
- Microsoft matched-quarter FilingLag changes vs same 2019 quarter: +5, -2, +4, -3, +3, -3 days.
- LateFiler: 0 for all ten Microsoft observations.
- Binary COVID presence: 0 in matched 2019 filings; 1 in matched Q1-2020 through Q2-2021 filings.
- Original author/source artifacts remain immutable; reproduction changes are derived artifacts only.

## Hourly execution contract
- Run every hour.
- Spend approximately 15 minutes of effective execution per run.
- Reconstruct the OPEN WORK REGISTER at the start of every run.
- Work on the highest-value executable item for POC/V1.
- Do not restart completed work.
- Stay on the current gate until exit criteria are actually met.
- If blocked, record the blocker and move immediately to another executable task within the same delivery gate.
- Save meaningful outputs to GitHub and Google Drive when tools permit.
- Verify writes by readback.
- Never fabricate evidence, execution, results, citations, saves, timings, or completion.
- Never convert missing evidence into PASS.
- Keep synthetic, author-provided, and independently regenerated evidence separately labeled.
- Never merge protected main without explicit user authorization.

# POC Gate — Finish First

POC is complete only when all criteria below are satisfied.

1. Case 001 frozen with verified provenance and limitations.
2. Microsoft one-company SEC reconstruction frozen as the independent public-data proof.
3. Error Taxonomy V2 exists and is machine-readable.
4. Adversarial benchmark includes clean controls, single errors, compound errors, and at least one difficult code/provenance case.
5. Evidence Graph V1 links Claim -> Table -> Result -> Code -> Data/Source -> Assurance state.
6. Research Assurance Report V1 can be generated from a case using VERIFIED / CONSISTENT / PARTIAL / FLAGGED / HUMAN_REVIEW.
7. Minimal MCP/API tool contracts are implemented for:
   - inspect replication package
   - map table to code
   - compare reported result
   - trace provenance
   - score detection
   - generate assurance report
8. One end-to-end POC demo executes using Case 001/Microsoft evidence without pretending licensed-data reproduction occurred.
9. Tests pass for implemented POC components.
10. GitHub and Google Drive contain synchronized POC artifacts plus a POC release/status record.

## POC work order
P0. Freeze Case 001.
P1. Error Taxonomy V2.
P2. Adversarial benchmark V2.
P3. Evidence Graph V1.
P4. Assurance Report V1.
P5. Minimal executable MCP/API layer.
P6. End-to-end Case 001 demo.
P7. Tests/QA.
P8. Freeze POC release.

# V1 Gate — Start Immediately After POC

V1 is complete only when:

1. At least 3 real research cases are supported: Case 001 plus at least two additional replication packages.
2. Stata + Python support is operational; SAS evidence extraction retained; add R if selected cases require it.
3. Error taxonomy and benchmark extend beyond deterministic E01-E10 and include blinded/compound cases.
4. Human ground-truth protocol separates objective from judgment-dependent labels.
5. Small pilot comparison covers frontier LLM, LLM+RAG, NAAIL, and Human+NAAIL where feasible.
6. Evidence Graph V2 and assurance-report schema are reusable across cases.
7. Journal Evidence Library V1 includes documented policies only and separates official requirements from observed convention.
8. Researcher pre-flight workflow accepts manuscript/code/output/data and produces a structured assurance report.
9. Security/governance basics are in place: immutable originals, provenance, derived artifacts, no silent overwrite, confidential-input guidance, human-review gate.
10. A clearly identified V1 candidate state exists in GitHub and the corresponding V1 master record exists in Google Drive.

## V1 work order
V1.1 Select Case 002 and Case 003.
V1.2 Build case adapters/gold baselines.
V1.3 Add required software support.
V1.4 Build blinded/compound benchmark set.
V1.5 Human ground-truth protocol.
V1.6 Pilot comparative evaluation.
V1.7 Evidence Graph V2.
V1.8 Journal Evidence Library V1.
V1.9 Researcher pre-flight workflow.
V1.10 Security/governance baseline.
V1.11 V1 QA and release candidate freeze.

# Post-V1 Roadmap
- Cases 004-010 and larger multi-paper corpus.
- R, SPSS, SEM/SmartPLS/AMOS, Excel/notebook expansion as needed.
- Formal human-ground-truth study.
- Full comparative experiment and performance evaluation.
- Qualitative Research MCP.
- Mixed-Methods MCP.
- Research-MCP Gateway.
- Scientific Reviewer/Falsification Agent.
- 50-100 paper external validation.
- Research Paper 1.
- University MVP and pilot.
- Journal/editor pilot.
- Publisher pilot.
- Security/governance hardening.
- Commercial MVP and business validation.
- Scientific Model Marketplace.
- NAAIL Benchmark Lab.
- Production multi-tenant Research Assurance Platform.

## Run-report contract
Every hourly run records:
START_TIME, END_TIME, DURATION, delivery gate, current task/phase, starting and ending GitHub HEAD when available, open work considered, work attempted, work completed, evidence produced, files changed, commits, tests/CI, Drive updates, blockers, exit-criteria progress, exact next executable task, and status: OPEN / BLOCKED / POC_COMPLETE / V1_COMPLETE / PROJECT_COMPLETE.
