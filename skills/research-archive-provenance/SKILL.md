---
name: research-archive-provenance
description: Use to organize and reconcile large research archives containing Word or Google Docs manuscripts, appendices, review responses, data, code, results, and multiple Drive/GitHub/Hugging Face/Kaggle versions. Use when a canonical version, project registry, provenance manifest, duplicate review, or non-destructive archive plan is needed.
---

# Research Archive Provenance

## Purpose

Create a trustworthy, non-destructive map from research questions to manuscripts, data, code, results, appendices, review states, and public or private copies. The archive is an evidence system: names and folders help navigation, while IDs, hashes, dates, and decision logs establish provenance.

## Safety and preservation

- Inventory before changing anything. Never delete, overwrite, or silently rename a source file by default.
- Treat Drive, GitHub, Hugging Face, Kaggle, and local copies as distinct locations with distinct permissions and versions.
- Never move confidential, restricted, or personally identifying data to a public repository. Record sensitivity and allowed destinations.
- If two files conflict, preserve both and label the conflict. A “current” label is a decision, not an inference from title alone.

## Workflow

### 1. Inventory

For each file or native document, collect `archive_id`, title/name, MIME/type, parent/folder, owner, location URL, provider ID, created/modified time, size, version marker, sensitivity, sharing state, and retrieval time. For local files, add SHA-256 and relative path. For cloud-native documents where a byte hash is unavailable, record provider revision or a normalized text snapshot hash when permitted.

### 2. Cluster and reconcile versions

Cluster by project signals, title stems, identifiers, content similarity, dates, and explicit version markers such as `v2`, `revised`, `final`, `submission`, or `response`. Do not rely on title alone. For each family, record:

`canonical candidate | supersedes | sibling/duplicate | source of truth | reason | decision-maker | decision date`.

Use `current`, `superseded`, `archive`, `needs-review`, and `conflict` labels. A newer timestamp is evidence, not a final decision.

### 3. Build the project graph

Represent each project as:

`project → manuscript → data → code → results → appendix → journal/submission → review state`.

Add links to related dictionaries, preregistration/protocol, replication package, figures, tables, and correspondence. For each edge, store relationship type, source location, last checked date, and confidence. Keep one project registry rather than making a new folder for every search result.

### 4. Use a durable archive layout

When creating a new derivative archive, prefer:

```text
archive/
  manifest.csv
  decision-log.md
  projects/<project-slug>/
    manuscript/
    data/
    code/
    results/
    appendix/
    review/
    provenance/
```

Keep provider-native files in their original location when possible. The derivative archive should contain pointers, manifests, and explicitly copied versions—not a confusing second source of truth.

### 5. Check document structure

For Word or Google Docs, verify title, abstract, introduction, theory, hypotheses, method, sample, measures, results, tables/figures, discussion, limitations, references, data/code statement, and version note. If a document is being edited, use structural and visual QA; if it is only being inventoried, do not rewrite it. Reconcile table/figure numbers and sample counts against code and the manifest.

### 6. Maintain an open repair queue

Track `issue_id | artifact | symptom | impact | proposed repair | owner | status | evidence | resolved version`. Typical issues include duplicate “final” files, broken links, missing data dictionaries, inconsistent sample dates, untracked generated outputs, and public links to sensitive material.

### 7. Publish safely

Before a public GitHub, Hugging Face, or Kaggle release, run a secret scan, license check, PII/confidentiality review, dependency/license inventory, and provenance check. Publish the minimum needed artifact; keep restricted data and private working papers in their permitted store. Record the public URL, release date, commit/version, and what is intentionally omitted.

## Quality checks

An archive is ready when a second person can answer: Which file is current? Which data and code generated the result? What changed since the prior version? What is public, restricted, or missing? Which claims remain unverified? If any answer depends on memory, add a manifest or decision-log entry.

## Reference

Use `references/archive-schema.md` for manifest fields and status vocabulary.
