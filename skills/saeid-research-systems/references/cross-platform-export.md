# Cross-platform export and storage

Treat the installed GPT skill as the active runtime and every external copy as a derivative export. Keep the same skill name and an explicit version/date in every export. Never claim that one platform automatically updates another.

## Canonical package

When an export is requested, assemble only the validated skill files:

```text
saeid-research-systems/
├── SKILL.md
├── agents/openai.yaml
└── references/
```

Add a human-readable provenance manifest containing version, export timestamp, source revision or file hashes, included files, license/data restrictions, and destination status. Exclude credentials, tokens, private datasets, raw restricted data, local caches, and unrelated project artifacts.

## Destination rules

| Destination | Permitted default | Required verification |
|---|---|---|
| GPT personal skills | Install/update the personal skill through the skill-management workflow | Validate frontmatter and confirm the reconciled skill path is present |
| GitHub | Use the exact authorized repository and path; prefer a private branch/repository for unpublished work | Read back the path and record commit SHA and URL |
| Hugging Face | Use an exact authorized repository ID and an explicit repository type; require write scope | Read back repository metadata, revision, file list, and URL |
| Kaggle | Use an exact authorized account and dataset/notebook target; keep unpublished material private where supported | Read back the dataset/notebook version and URL |
| Google Drive | Upload a new versioned copy unless the user explicitly requests an exact-source update | Verify metadata, name, MIME type, file ID, and connector-returned URL |

## Authorization and failure handling

- A destination name alone is not an exact target. If the repository, dataset, notebook, folder, or account is ambiguous, ask for the target or perform only a read-only identity check.
- Use only connected, authenticated write actions. A read-only identity or search result does not authorize an upload.
- For Drive, match the active connector account to the supplied account scope when one exists. Never overwrite an attached snapshot or use a title search as a write target. A new copy may be placed in the user's root only when no folder was requested and the connector permits it.
- Keep public visibility off by default. Ask before changing visibility or publishing unpublished research, confidential material, or licensed content.
- If a connector or CLI is unavailable, record `NOT PERFORMED` or `BLOCKED` with the exact reason and retain the local validated package. Do not substitute a guessed URL, account, or destination.
- Verify after every write. A returned write request without successful readback is `WRITE REQUESTED / NOT VERIFIED`, not complete.

## Per-project run behavior

For an actual project run, update the run manifest with export status only for destinations explicitly requested or configured and authorized. If a project is run hourly, export the artifacts generated in that actual run; do not invent missed runs or imply that the skill itself is executing in the background. Apply the two-failure rule to a repeated export blocker as well as to scientific and engineering tasks.
