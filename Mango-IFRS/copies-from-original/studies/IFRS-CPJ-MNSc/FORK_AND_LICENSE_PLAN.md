# Fork and License Plan

## Important runtime limitation

The connected GitHub tool used to create this integration does **not expose GitHub's Fork API endpoint**. Therefore, this repository records the verified upstreams and integration plan, but does not falsely claim that top-level forks were created.

## Fork priority

### Priority A — recommended forks

1. **trr266/treat** — MIT; use as the reproducibility skeleton.
2. **European-Securities-Markets-Authority/esef_toolkit** — EUPL-1.2; use as ESEF ingestion reference.
3. **trr266/esef-website** — MIT; academic ESEF research pipeline.
4. **jadchaar/sec-edgar-downloader** — MIT; SEC/20-F ingestion.

### Priority B — dependency/reference

5. **Arelle/Arelle** — Apache-2.0; prefer dependency/reference over vendoring the full codebase.

### Priority C — isolated research environment

6. **reeyarn/openesef** — GPL-3.0; keep isolated unless the target distribution is GPL-compatible.

## Clean-room integration boundary

The proprietary/startup layer should contain only newly written adapters, schemas, scoring logic, agent orchestration, human-gate logic, experiment code, and Mirendal-specific functionality.

Do **not** copy third-party source code into proprietary modules unless its license permits the intended use and all notice/redistribution obligations are satisfied.

## Proposed architecture

```
upstreams/
  esef-toolkit/      # fork/reference, EUPL-1.2
  trr266-esef/       # fork/reference, MIT
  sec-edgar/         # fork/reference, MIT
external/
  arelle/            # dependency, Apache-2.0
  openesef/          # isolated GPL research environment
studies/IFRS-CPJ-MNSc/
  cases/
  adapters/
  agents/
  experiment/
  analysis/
  tables/
  figures/
  provenance/
```

## Kaggle rule

Do not copy Kaggle datasets into a public GitHub repository by default. Store only metadata, source URL, download date, checksum, license/terms snapshot, and preprocessing script. Put large/raw data in an external research-data location consistent with the dataset's terms.

## Reproducibility rule

Every published result should be reproducible from a top-level script or workflow that records:

- upstream dataset/repository version;
- commit SHA/tag;
- retrieval date;
- preprocessing configuration;
- model/provider/version;
- prompts;
- random seeds;
- retrieval-corpus hash;
- raw agent outputs;
- deterministic calculations;
- treatment assignment;
- analysis code;
- generated tables and figures.
