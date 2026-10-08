# GitHub, Drive and provenance protocol

Before accessing private content, identify the exact authorized project/repository/folder and confirm connector availability. Search source evidence; do not infer a stored file exists solely from conversational memory. Check data sensitivity and licensing. Do not expose API keys or personal data.

Expected artifact structure: `manuscript/`, `data_dictionary/`, `code/`, `results/`, `appendix/`, `logs/`, `provenance/`, `repair_queue/` where pertinent. Store human-readable manifest fields for sources, SHA-256 where computable, code revision, execution timestamp, dependencies, data-release restrictions and result verification.

Use a private branch/repository by default for unpublished code and preliminary findings. External mutation or publication requires user permission and access. Verify resulting links/commit IDs/upload outcomes through tools before reporting completion. If a connector is inaccessible, report the exact limitation and deliver local files instead. Never claim an upload completed without evidence.
