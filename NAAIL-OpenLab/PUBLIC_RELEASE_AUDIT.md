# NAAIL OpenLab — Public Release Audit

## Decision gate
Do **not** change Hugging Face or Kaggle visibility to public until every item below passes.

## Confirmed safeguards in canonical GitHub source
The repository-level NAAIL `.gitignore` excludes:
- patent/private draft paths and claim drafts
- `.env` and `.env.*`
- private key material (`*.pem`, `*.key`)
- `secrets/` and `credentials/`

These exclusions reduce accidental publication risk but do not prove that the full history or external mirrors are clean.

## Required pre-publication checks
- [ ] No credentials, tokens, API keys, passwords, cookies, or private keys in files or history.
- [ ] No private/patent-enabling drafts.
- [ ] No confidential client, student, employer, audit-firm, or regulator data.
- [ ] Every third-party dataset/model/code asset has redistribution permission and attribution.
- [ ] Synthetic/public data are clearly labelled.
- [ ] LICENSE, AUTHORS, CITATION.cff and codemeta metadata are consistent.
- [ ] README states educational/research purpose and limitations.
- [ ] Hugging Face inventory matches the approved HF subset.
- [ ] Kaggle inventory matches the approved benchmark/notebook subset.
- [ ] Public URLs are tested after visibility change.

## Platform-specific approved scope
**Hugging Face:** public/redistributable datasets, models, model cards, dataset cards, selected demos.

**Kaggle:** public/redistributable benchmark datasets and reproducible notebooks. Do not use Kaggle as a full GitHub mirror.

**GitHub:** canonical architecture, code, agents, tests, provenance and release metadata.

## Release rule
Public release is approved only after the checklist is complete. Visibility changes remain a deliberate human approval action.
