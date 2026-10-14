# DARA — Dual-Spine AI Research Architecture
**Version:** 1.0 · **Date:** 2026-10-14 · **Status:** Approved design; individual runtime connections remain subject to verification

## 1. Architectural decision

DARA is a **dual-spine, multi-agent research architecture**. **GPT / ChatGPT** coordinates research strategy, knowledge integration, planning, code review and validation. **Google Drive** is the authoritative **Knowledge & Data Spine**, organized vertically for each research project and horizontally for validated common research resources. **GitHub** is the **Technology & Code Spine**, containing versioned code, notebooks, schemas and integration interfaces. Google Colab, Gemini, Gemini CLI and Google Cloud are **execution environments and computational services**.

The two spines are **complementary rather than competing**. GitHub is not used as a proxy for ordinary Drive access or every Google service request.

```text
                       GPT / ChatGPT
         Research intelligence · planning · validation
                /                         \
 (Direct connected Drive app)     (Connected GitHub app)
              /                             \
    GOOGLE DRIVE                         GITHUB
 Knowledge & Data Spine            Technology & Code Spine
    /             \                        |
 Vertical       Horizontal             Reviewed code
 per-project    shared methods             |
 data           taxonomy / registry    GOOGLE EXECUTION
                  /                     Colab · Gemini UI
                  /                    Gemini CLI (Cloud Shell)
           Results & logs              Google Cloud · BigQuery
                  ^                     Vertex AI (optional)
                  |                           |
                  +--- verified outputs ------+
```

## 2. Responsibilities

| Component | Authority | Scope |
|---|---|---|
| GPT / ChatGPT | Research coordination and advisory review | Design, assess, propose, inspect connected Drive/GitHub resources; never assume direct Colab runtime control |
| Google Drive | Canonical evidence and data storage | Source documents, raw data, validated results, manuscripts, master indexes, provenance and execution logs |
| GitHub | Version-controlled technology bridge | Code, notebooks, unit tests, non-sensitive specifications, reviewed PRs |
| Google Colab | Python computation | Runs notebooks after user signs in and explicitly approves Drive/Cloud access |
| Gemini (Colab UI) | Interactive coding assistant | Separate from programmatic Gemini inference through Vertex AI |
| Gemini CLI (Cloud Shell) | Browser-hosted coding agent | Can inspect/modify authorized checkout under approval; distinct from Colab runtime |
| Google Cloud | Project-based services | `third-serenity-428705-g2`; requires appropriate permissions, APIs and possibly billing |
| BigQuery, Vertex AI | Optional managed services | Only enabled/used after permissions, cost and security approval |

## 3. Vertical and horizontal integration

**Vertical project pipelines:** Within CAM, ICFR, ESG or valuation, connect source data → quality review → methodological specification → code execution → analysis → manuscript → archived evidence.

**Horizontal reusable fabric:** Share validated research methods, source registries, accounting/control taxonomies, dataset schemas, statistical test utilities, and reusable code **by references with version IDs**. Do **not** pool dissimilar confidential datasets across projects automatically.

A project's `PROJECT_MASTER_INDEX.md` should include: question/hypotheses; verified Drive folder; dataset lineage/permissions; versioned taxonomy; GitHub code path/commit; Colab notebook; analysis status; latest results; and run verification.

## 4. Direct connection topology

1. **GPT ↔ Google Drive:** Directly through the connected Google Drive app with its own permissions.
2. **GPT ↔ GitHub:** Directly through the connected GitHub app for reviewed code and PRs.
3. **Colab ↔ Drive:** `google.colab.drive.mount` with separate user approval.
4. **Colab ↔ Google Cloud:** Colab interactive authentication, `gcloud` project selection and service-specific IAM checks.
5. **Gemini CLI ↔ GitHub:** Authorized checkout in Google Cloud Shell; no implied Colab/Drive session sharing.
6. **Colab/Gemini/Google Cloud:** Native Google integrations where supported; no unnecessary routing of datasets through GitHub.

**GitHub is a code bridge, not a universal data API, authentication broker or automatic Colab execution mechanism.**

## 5. Folder and version design

### Google Drive — logical organization, not forced file relocation
```text
DARA_ResearchOS/                    # Master architecture/index only
  DARA_ARCHITECTURE.md
  PROJECT_MASTER_INDEX.md
  DARA_COLAB_INTEGRATION_GUIDE.md
  DARA_Integration_Bootstrap.ipynb

Existing_CAM_Project_Folder/        # Leave in place, link from index
Existing_ICFR_Project_Folder/       # Leave in place, link from index
Existing_ESG_Project_Folder/        # Leave in place, link from index
Other_Existing_Project_Folders/     # Leave in place, link from index
```

**Vertical**: each existing project uses its own existing Drive folder and versioned substructure, where authorized. **Horizontal**: the DARA master index points to shared methods and evidence/taxonomy registers; source files are not duplicated or silently reclassified.

### GitHub — main repository
```text
Saehon/Saeid-Homayoun/
  DARA/
    README.md
    ARCHITECTURE.md
    PROJECT_MASTER_INDEX.md
    COLAB_INTEGRATION.md
    colab/DARA_Integration_Bootstrap.ipynb
```

## 6. Execution protocol

**Research request → GPT planning/review → GitHub PR for code → user-approved execution in Colab or Cloud Shell → verified Drive readback → GPT evaluation of saved evidence.**

Each execution report should record: timestamp (UTC), project, approved task, source file IDs, code commit, runtime details, model versions, input checksums where practical, outputs, errors, and PASS/PARTIAL/FAIL status. **Do not claim inference or empirical results that were not executed.**

## 7. Governance rules

- Drive authoritative, GitHub code/versioned methods only; do not put API keys, private datasets or confidential manuscripts in public GitHub.
- Keep existing Drive folders, history, shares, projects and GitHub research-specific pause rules unchanged.
- Require human approval for paid API calls, destructive file changes, Github push/merge unless user explicitly authorizes, cloud resource provisioning, IAM changes and dissemination of non-public data.
- `OPENAI_API_KEY` is **optional** for Python code inside Colab to invoke OpenAI API; it is **not** required for ChatGPT's separate connected GitHub/Drive workflows.
- Gemini CLI in Cloud Shell and Colab's Gemini sidebar are distinct tools; both require separate verification.
- Preserve provenance and avoid cross-project data leakage.
- This architecture does **not** provide unattended control of a live Colab runtime merely because GitHub and Drive are connected.

## 8. Engineering assessment

The design is strongest for traceability, reproducibility and incremental adoption. Automated scheduling requires a separately approved execution/orchestration mechanism; free Colab runtime uptime is not guaranteed. Adopt paid services only after measurable scientific and cost justification.

**Canonical Drive folder:** https://drive.google.com/drive/folders/1OXZ6v1zB0G7wmlGezLCAvm8I4Egr2UPL

**GitHub repository:** https://github.com/Saehon/Saeid-Homayoun

**Google Cloud project:** `third-serenity-428705-g2`.
