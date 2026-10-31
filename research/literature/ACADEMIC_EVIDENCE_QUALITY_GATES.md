# Academic Evidence Integrity — Release Gates

**Purpose:** turn the NAAIL research literature index into an **auditable scholarly evidence system**, without replacing the existing NAAIL/PCAOB/IFRS/ISSB framework or presenting a literature search as a completed empirical research study.

**Evidence scope:** 21 *seed* references across selected FT50/AJG groups as of 31 October 2026 (**6 publisher-page bibliographic spot-checks; 15 still requiring review**); 11 bounded project-to-literature relationship statements. **Not** an exhaustive FT50/AJG 1–4 census. The primary working research documents remain in the investigator's **private, access-controlled personal Google Drive**; the GitHub site releases only public-safe research documentation and code.

## Why scholarly integrity requires more than references

A DOI resolves to scholarly metadata; it is **not** evidence that the paper tests the exact claims or implementation in a given GitHub repository. A third-party article's status does not make a NAAIL agent a validated product. Incorrect paper titles, wrong author ordering, stale standards, an outdated AJG rating, or uncited summary assertions can undermine the credibility of otherwise useful research software.

The following system deliberately distinguishes four independent checks:

| Gate | What the current system checks | What it **does not** prove |
|---|---|---|
| **1. Bibliographic structure** | Every reference in the public Harvard page has a unique registered key, identical DOI, author/year, article title and journal name | That DOI actually belongs to those author names or that the paper's findings were correctly read |
| **2. Crossref metadata matching** | Optional online API review compares deposited journal/title/year/first-author metadata and flags mismatches | That Crossref is complete; that the publication supports a particular research hypothesis |
| **3. FT50/AJG provenance** | Tier labels are visibly separate from article bibliographic metadata and designated as requiring authoritative CABS confirmation | That Crossref, this project's code, or the Financial Times certifies an individual research study's quality |
| **4. Evidence/claims** | A machine-readable ledger maps research-project assertions to existing reference keys and requires uncertainty and `NOT_TESTED_IN_THIS_REPOSITORY` | That any regression, fine-tuned model, PCAOB finding, ISSB compliance determination or IFRS review was performed |

**[Browse the Harvard research library](../LLM_FINE_TUNING_AGENTIC_AI_HARVARD_REFERENCES.md)** · **[Evidence ledger (JSON)](project_evidence_ledger.json)** · **[Metadata & citation code](harvard_crossref.py)** · **[Fail-closed quality gate](evidence_quality_gate.py)**.

## Claims-to-literature traceability: project scope

| Research line | Academic relationship permitted | Critical missing evidence before empirical conclusions |
|---|---|---|
| PCAOB inspection research | Audit-risk response, evidence-relevance, monitoring and expert skepticism can be motivated by domain studies | Permitted task/workpaper cases; expert adjudication; independent evidence judgments; inspection-selection controls |
| IFRS judgment / POMELO–VERA | Numerical and temporal accuracy, model-and-human complementarity, version-sensitive reasoning | Source text rights and appropriate standard versions; real model results; human IFRS expertise and error-cost measurement |
| ISSB sustainability disclosure | Disclosure quality, financial reporting connectedness, construct-validation and independent assurance boundaries | Applicable S1/S2 regime; industry/period reporting data; verified outcomes and human evidence-entailment |
| KIWI CAM/KAM | Text-analysis overclassification and audit-skepticism methods motivate validity checks | CAM ground truth, source text and assertion coding, external test and construct validation |
| NAAIL/DARWIN and fine-tuning | Human control, scientific provenance, data quality and model-adaptation research suggest viable experimental tests | Frozen permitted datasets, training records, model configurations, untouched holdouts and independent replication |

Read [source-specific ledger entries](project_evidence_ledger.json) for which DOI-keyed studies motivate each bounded assertion. **The ledger makes the theory connections inspectable; it intentionally avoids asserting that every NAAIL project has been theoretically “proven.”**

## Reproduce local scientific integrity checks

```bash
python -m research.literature.evidence_quality_gate \
  --out reports/academic_evidence_quality_offline.json
python -m unittest discover -s research/literature/tests -p 'test_*.py' -v
```

The offline report *explicitly* sets `bibliographic_metadata_verified_against_publisher_api=false`, `official_ajg_ranking_verified=false`, and `all_project_hypotheses_empirically_supported=false`. CI verifies the report cannot be misrepresented as a full literature or empirical validation.

### Metadata verification remains a distinct opt-in stage

```bash
python -m research.literature.harvard_crossref \
  --online --out reports/crossref_metadata_manual_review.json
```

This action requires network access and does **not** automatically rewrite or publish an article citation. A metadata disagreement should trigger a **human comparison to the publisher and Crossref record**, then a PR updating the machine-readable registry *and* the public Harvard page with supporting source evidence. To extend beyond the seed 21 records, the [Crossref candidate discovery](crossref_discovery.py) likewise requires explicit `--online` and a human screening process.

## Scientific standards for any later release

1. Confirm DOI-title-author publication metadata against an official publisher and Crossref and record the review date.
2. Resolve journal ranking **for the exact AJG edition** using an authorized official source; never conflate FT50 with AJG grade.
3. Freeze inclusion/exclusion rules and conduct dual-screened literature reviews if claiming *comprehensive* coverage.
4. Require source-based evidence linking the cited paper's actual findings to each proposed theoretical mechanism; preserve contrary findings and limitations.
5. Use independent expert ratings, real data/permissions, hypothesis pre-registration, reproducible code and holdout tests before claiming that a model or agent is scientifically validated.
6. Preserve the existing public/private separation, source-code rights, no affiliation misrepresentation and professional reviewer gates.

**No automated process here issues a PCAOB inspection opinion, an IASB or ISSB standards interpretation, an ISSA 5000 assurance conclusion, or a publication-level peer review.**
