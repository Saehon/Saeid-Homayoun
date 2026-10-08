# Archive manifest schema

Recommended fields:

`archive_id, project_slug, artifact_role, title, provider, provider_id, url, local_path, mime_type, created_at, modified_at, retrieved_at, sha256_or_revision, version_label, status, supersedes_id, sensitivity, access, license, canonical_reason, last_checked, notes`.

Recommended `artifact_role` values: `manuscript`, `appendix`, `review-response`, `data`, `code`, `results`, `figure`, `table`, `dictionary`, `protocol`, `metadata`, `release`.

Recommended `status` values: `current`, `candidate`, `superseded`, `archive`, `needs-review`, `conflict`, `missing`, `restricted`.

Every canonical decision belongs in a decision log with the evidence, person/date, and affected IDs.

