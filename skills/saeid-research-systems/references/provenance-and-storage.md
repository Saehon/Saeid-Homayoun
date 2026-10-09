# GitHub, Drive and provenance protocol

Before accessing private content, identify the exact authorized project/repository/folder and confirm connector availability. Search source evidence; do not infer a stored file exists solely from conversational memory. Check data sensitivity and licensing. Do not expose API keys or personal data.

Expected artifact structure: `manuscript/`, `data_dictionary/`, `code/`, `results/`, `appendix/`, `logs/`, `provenance/`, `repair_queue/` where pertinent. Store human-readable manifest fields for sources, SHA-256 where computable, code revision, execution timestamp, dependencies, data-release restrictions and result verification.

Use a private branch/repository by default for unpublished code and preliminary findings. External mutation or publication requires user permission and access. Verify resulting links/commit IDs/upload outcomes through tools before reporting completion. If a connector is inaccessible, report the exact limitation and deliver local files instead. Never claim an upload completed without evidence.

## Canonical Google Drive-first storage policy (approved 2026-10-09)

Apply to all research, teaching, publishing, and AI-engineering projects unless the user overrides it.

1. **Google Drive = authoritative master.** Maintain one canonical Drive folder per project. Search and reuse existing folders before creating anything; do not relocate, overwrite or delete original data, manuscripts, tracked changes, or prior revisions without explicit authorization.
2. **Every project has a `PROJECT_MASTER_INDEX.md`** (or equivalent Google Doc), containing: project ID/title, research objectives, hypotheses and sample/years, data sources/licensing, methodology, manuscript and empirical-result links, current phase and evidence status, next actions, update date, provenance and version history.
3. **Record direct, verified cross-platform project links** in that index: Google Drive folder and source documents; GitHub repo/branch/commit for code and replication; Kaggle dataset/notebooks for suitably licensed public data; Hugging Face repo for approved models/datasets; ChatGPT Project/conversations for research context. Where missing or inaccessible, mark `NOT CONFIGURED` or `NOT VERIFIED`; never invent a link.
4. **Service roles are complementary rather than automatically synchronized:** Drive = documents/data dictionary/results/manuscripts and version archive; GitHub = code/version control and reproducibility; Kaggle = approved shared data and notebooks; Hugging Face = approved models and datasets; ChatGPT = analysis/active minimal working files, not the authoritative archive; local PC = large SEC/EDGAR/XBRL downloads and Llama execution. Link back to Drive as the canonical project source.
5. **Conserve ChatGPT storage:** keep a small active file set and compact project context, retrieving external files as needed. Google Drive storage does not enlarge ChatGPT file quotas. Synchronization requires authorized explicit steps and verifiable writes; do not claim continuous automatic mirroring.
6. **Preservation, privacy and audit trail:** retain original versions and a revision log; avoid gratuitous duplicate large files; preserve SHA-256 checksums where feasible. Keep unpublished manuscripts, restricted datasets, personally identifying data and student work private. Never publish to open GitHub/Kaggle/Hugging Face unless approved and appropriately licensed.
7. **Operational verification:** before writes, verify the exact authorized destination and access rights. After writes, read back real IDs/URLs, commit/revision and status and record them in Drive's master index. Report blocked destinations precisely. Never silently overwrite, delete, or fabricate successful platform connections.

Recommended per-project folders (create selectively): `01_SOURCES/`, `02_DATA/`, `03_MANUSCRIPTS/`, `04_RESULTS/`, `05_REPLICATION/`, `06_VERSION_HISTORY/`. Store `PROJECT_MASTER_INDEX.md` at the root. Cross-platform links in this index should point to actual existing destinations, not placeholders represented as real connections.
