# Harvard-Style Research Literature Registry | LLMs, Fine-Tuning & Agentic AI

**A curated, updatable literature companion for NAAIL OpenLab**, PCAOB Inspection Intelligence, IFRS Judgment Intelligence, ISSB Sustainability Intelligence, KIWI/CAM-KAM, POMELO/VERA and related financial-AI work.

**Researcher:** Saeid Homayoun · University of Gävle, Sweden · [ORCID](https://orcid.org/0000-0002-2536-0446) · [Google Scholar](https://scholar.google.com/citations?user=1PKckooAAAAJ&hl=en)

**Public state, 31 October 2026:** 21 **curated DOI-linked bibliographic seed records**. This is a **living, explicitly non-exhaustive register**, *not* all papers in FT50 or every AJG 1–4 journal. Exhaustive claims would require a documented full-coverage database search, licensed journal-list coverage, screening, deduplication, forward/backward citation tracing and expert review. All project research remains in progress; the **primary substantive working materials are held in my private, access-controlled personal Google Drive**, not in this public repository.

> **Evidence-integrity statement:** Relevant scholarly articles **inform or motivate the theoretical, methodological and governance design** of the GitHub research programmes. They **do not demonstrate that every proposed hypothesis, agent architecture, model result or scientific claim in this account has been independently tested or supported**. Some references are methodological cautions, some are domain-specific empirical evidence, and some are indirect background. Every project retains its existing architecture and human professional approval boundaries.

## Evidence integrity controls — publication references are not project validation

The [**Academic Evidence Integrity and Release Gates**](literature/ACADEMIC_EVIDENCE_QUALITY_GATES.md) describe how research support is **bounded, inspectable and tested**. A [machine-readable claims-to-sources ledger](literature/project_evidence_ledger.json) records **11 specific research-programme claims**, exact reference keys, degree of theoretical/methodological relevance, missing evidence, and the explicit status **NOT_TESTED_IN_THIS_REPOSITORY**.

The [offline evidence gate](literature/evidence_quality_gate.py) will fail GitHub CI if a listed Harvard author/year/title/journal/DOI drifts from its structured record, or if a project claim references an unknown source, omits limitations or is incorrectly presented as empirically verified. Passing this check **does not prove DOI publisher metadata, journal ranking, full-text content or any program's performance**.

**Source-check status:** a subset of article metadata has been independently cross-checked against publisher websites; the full 21-item seed list has **not** completed a recorded Crossref API round-trip, official AJG license-based classification review, systematic literature screening or comprehensive full-text adjudication. References remain provisional for manuscript citation until individually checked.

## Navigate the evidence

- **[FT50 empirical and conceptual research protocols](FT50_RESEARCH_DESIGN_AND_EVIDENCE.md)** — identification, falsification, theory and research designs.
- **[Integrated PCAOB / IFRS / ISSB Agentic AI programme](AGENTIC_AI_ASSURANCE_RESEARCH.md)** — unchanged architecture and professional responsibilities.
- **[Crossref metadata audit and Harvard generator](literature/harvard_crossref.py)** — optionally checks deposited DOI metadata via [Crossref's public REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) and flags inconsistencies. It cannot verify AJG rankings, substantive findings, or data rights.
- **[Machine-readable seeded bibliography](literature/llm_agentic_ai_seed_registry.json)** — DOI, authors, year, venue, project tags, relevance and transparent tier uncertainty.
- **[Bibliographic quality tests](literature/tests/test_harvard_crossref.py)** — non-network unit tests for uniqueness, citation formatting and metadata verification boundaries.

## Journal classification and coverage

FT50 membership and Chartered ABS **Academic Journal Guide 2024 (AJG)** categories are **journal-level attributes**, not intrinsic quality scores of individual articles. AJG **4\*** is a distinction *within* grade 4. FT50 and AJG overlap but are not identical lists.

| Reported group | Number of curated records | Status and source reliability |
|---|---:|---|
| FT50, AJG 4*/4 | 10 | 2026 FT50 journal basket plus independently reproduced AJG 2024 journal list; official AJG register check advised |
| AJG 3 | 1 | The British Accounting Review is shown as grade 3 on the AJG accounting listing; confirm edition through CABS |
| AJG 2 | 4 | IJAIS and Accounting Research Journal shown at 2 in secondary AJG 2024 reproduction |
| AJG 1 | 1 | **Indirect** AI-disclosure paper, not an LLM/fine-tuning/agentic AI experiment |
| Cross-disciplinary / grade unverified | 5 | Do **not** assign speculative AJG grades. Check official classifications, ISSNs, field inclusion |

**Ranking authorities:** [Financial Times FT50 revised in April 2026](https://www.ft.com/content/db863a0a-6524-45f9-bc52-fee997634bdc) · [Chartered ABS AJG methodology (2024)](https://assets.charteredabs.org/ajg-2024-methodology.pdf) · [AJG accounting list (third-party reproduction; not official CABS)](https://journalindexes.com/ajg/accounting/).

## Project-to-literature evidence matrix

| Research programme | Closely relevant cited studies | What the literature can support | What still requires direct evidence |
|---|---|---|---|
| **PCAOB Inspection Intelligence / KIWI** | Stuber & Hogan (2021); Fedyk et al. (2022); Fotoh & Mugwira (2025); Grey & Li (2026) | Inspection incentives, audit quality measurement, model limitations and professional skepticism | Real inspection/workpaper access, account-level expert gold, identification, false-flag measurement |
| **IFRS Judgment Intelligence / POMELO–VERA** | Blankespoor et al. (2026); Choi & Xie (2026); Levy (2026); Navas-Loro et al. (2026) | AI reporting use, human complementarity, temporal leakage, deterministic versus LLM reasoning | Licensed/dated IFRS source texts, authorized case gold, unit/currency validity, independently reviewed judgments |
| **ISSB Sustainability Intelligence** | Blankespoor et al. (2026); Stratopoulos & Wang (2025); Wobst & Lueg (2025); Lui (2026, indirect AI-disclosure) | Disclosure measurement, reporting incentives, risk of textual misclassification | ISSB S1/S2 source rights and application, assurance boundaries, causal links to outcomes, verified climate data |
| **NAAIL / DARWIN multi-agent scientific governance** | Gopal et al. (2025); Zhong (2025); Wang et al. (2026); Bick et al. (2026) | Human oversight, delegation, rigorous evaluation, organizational adoption | Reproducible autonomous runs, failure analysis, expert human validation, measured operational costs |
| **LLM training / fine-tuning / evidence graphs** | Zhang et al. (2026); Yan et al. (2025); Amelio et al. (2026); Navas-Loro et al. (2026) | Risks of synthetic-only fine-tuning, parameter-efficient adaptation, symbolic checks and knowledge-graph design | An **actually executed** fine-tuned model, lawful training rights, untouched holdout, model/version/cost reporting |

### Explicit levels of theoretical support

- **Direct domain evidence:** a published paper evaluates the relevant phenomenon (e.g., audit assistance, accounting disclosures, fine-tuned LLM performance).
- **Methodological support:** a paper justifies a *way of evaluating* model outputs or estimating effects; it does **not** endorse this repository's outputs.
- **Conceptual or theoretical motivation:** a framework helps form testable mechanisms but does **not** verify them.
- **Negative or cautionary evidence:** studies of hallucinations, overclassification, training-data contamination or overreliance are **reasons to strengthen controls**, not affirmations that existing tools solve these issues.
- **Untested research proposition:** no published research listed here is evidence that a proposed NAAIL component has been executed, deployed or professionally approved.

## Harvard-style reference list

Harvard has multiple institutional variants. Entries below use **Author(s) (Year) ‘Article title’, *Journal*. DOI link**; volume/issue/page fields are omitted when not independently established rather than fabricated. Source identities and publication metadata should be checked against the DOI registry before reuse in manuscripts. Titles and DOI links are not copied full-text articles.

### FT50 / AJG 4* and 4 (10 records)

- **JAR-2026-blankespoor:** Blankespoor, E., deHaan, E. and Li, Q. (2026) ‘Generative AI in Financial Reporting’, *Journal of Accounting Research*. [DOI](https://doi.org/10.1111/1475-679x.70050). **Focus:** LLM, disclosure, measurement. **Project links:** IFRS, ISSB, NAAIL. **Evidence relationship:** direct.
- **JAR-2026-choi:** Choi, J. H. and Xie, C. L. (2026) ‘Human + AI in Accounting: Early Evidence from the Field’, *Journal of Accounting Research*. [DOI](https://doi.org/10.1111/1475-679x.70052). **Focus:** LLM, human oversight, accounting. **Project links:** IFRS, PCAOB, NAAIL. **Evidence relationship:** direct.
- **JAR-2026-levy:** Levy, B. (2026) ‘Caution Ahead: Numerical Reasoning and Look-Ahead Bias in AI Models’, *Journal of Accounting Research*. [DOI](https://doi.org/10.1111/1475-679x.70058). **Focus:** LLM, look-ahead, temporal validity. **Project links:** IFRS, PCAOB, ISSB. **Evidence relationship:** direct.
- **MS-2026-zhang:** Zhang, J., Yang, M., Qiao, D. and Wei, Q. (2026) ‘Regurgitative Training: The Value of Real Data in Training Large Language Models’, *Management Science*. [DOI](https://doi.org/10.1287/mnsc.2024.07005). **Focus:** fine-tuning, synthetic data, training validity. **Project links:** NAAIL, POMELO, KIWI. **Evidence relationship:** direct.
- **MS-2025-zhong:** Zhong, H. (2025) ‘Optimal Integration: Human, Machine, and Generative AI’, *Management Science*. [DOI](https://doi.org/10.1287/mnsc.2024.07401). **Focus:** human oversight, delegation, AI. **Project links:** PCAOB, IFRS, ISSB. **Evidence relationship:** direct.
- **ISR-2025-gopal:** Gopal, R. D., Li, J., Riemer, K., Sarker, S., Singh, P. V., Susarla, A., Bichler, M. and Thatcher, J. B. (2025) ‘Inventing with Machines: Generative AI and the Evolving Landscape of IS Research’, *Information Systems Research*. [DOI](https://doi.org/10.1287/isre.2025.editorial.v36.n4). **Focus:** agentic AI, multiagent, research governance. **Project links:** NAAIL, DARWIN, POMELO. **Evidence relationship:** direct.
- **ISR-2026-wang:** Wang, W., Pei, S. and Sun, T. (2026) ‘Unraveling Generative AI from a Human Intelligence Perspective: A Battery of Experiments’, *Information Systems Research*. [DOI](https://doi.org/10.1287/isre.2023.0487). **Focus:** LLM, human intelligence, experiments. **Project links:** IFRS, NAAIL. **Evidence relationship:** direct.
- **MS-2026-bick:** Bick, A., Blandin, A. and Deming, D. J. (2026) ‘The Rapid Adoption of Generative AI’, *Management Science*. [DOI](https://doi.org/10.1287/mnsc.2025.02523). **Focus:** AI adoption, productivity. **Project links:** SME, NAAIL. **Evidence relationship:** contextual.
- **RAST-2022-fedyk:** Fedyk, A., Hodson, J., Khimich, N. and Fedyk, T. (2022) ‘Is artificial intelligence improving the audit process?’, *Review of Accounting Studies*. [DOI](https://doi.org/10.1007/s11142-022-09697-x). **Focus:** AI auditing, process quality. **Project links:** PCAOB, KIWI. **Evidence relationship:** contextual.
- **JAR-2021-stuber:** Stuber, S. B. and Hogan, C. E. (2021) ‘Do PCAOB Inspections Improve the Accuracy of Accounting Estimates?’, *Journal of Accounting Research*. [DOI](https://doi.org/10.1111/1475-679X.12339). **Focus:** PCAOB inspection, accounting estimates. **Project links:** PCAOB, IFRS. **Evidence relationship:** foundational/indirect.

### AJG 3 (1 records)

- **BAR-2026-darcy:** d'Arcy, A., Haas, C. and Wallner, N. (2026) ‘Large Language Models as Research Assistants: The Risk of Topic-Overclassification in Financial Disclosure Research’, *The British Accounting Review*. [DOI](https://doi.org/10.1016/j.bar.2026.101986). **Focus:** LLM, construct validity, financial text. **Project links:** PCAOB, KIWI, ISSB. **Evidence relationship:** direct.

### AJG 2 (4 records)

- **IJAIS-2025-strat:** Stratopoulos, T. C. and Wang, V. X. (2025) ‘Artificial intelligence and accounting research: a framework and agenda’, *International Journal of Accounting Information Systems*. [DOI](https://doi.org/10.1016/j.accinf.2025.100760). **Focus:** AI, accounting research, methods. **Project links:** PCAOB, IFRS, ISSB. **Evidence relationship:** direct.
- **IJAIS-2025-fotoh:** Fotoh, L. E. and Mugwira, T. (2025) ‘Exploring Large Language Models in external audits: Implications and ethical considerations’, *International Journal of Accounting Information Systems*. [DOI](https://doi.org/10.1016/j.accinf.2025.100748). **Focus:** LLM, audit ethics, human judgment. **Project links:** PCAOB, KIWI. **Evidence relationship:** direct.
- **IJAIS-2026-li:** Li, H., Freitas, M. M. d., Lee, H. (. and Vasarhelyi, M. A. (2026) ‘Enhancing continuous auditing with large language models: AI-assisted real-time accounting information cross-verification’, *International Journal of Accounting Information Systems*. [DOI](https://doi.org/10.1016/j.accinf.2026.100786). **Focus:** LLM, continuous audit, evidence. **Project links:** PCAOB, KIWI, NAAIL. **Evidence relationship:** direct.
- **ARJ-2026-grey:** Grey, L. F. and Li, Y. (2026) ‘Can ChatGPT be skeptical? A case-based evaluation of generative AI in financial statement auditing’, *Accounting Research Journal*. [DOI](https://doi.org/10.1108/ARJ-12-2025-0527). **Focus:** LLM, audit skepticism. **Project links:** PCAOB, KIWI. **Evidence relationship:** direct.

### AJG 1 — contextual scope (1 records)

- **AJAR-2026-lui:** Lui, T. K. (2026) ‘From black box to bottom line: the role of AI disclosure in bank performance in Malaysia’, *Asian Journal of Accounting Research*. [DOI](https://doi.org/10.1108/AJAR-06-2025-0237). **Focus:** AI disclosure, bank performance. **Project links:** ISSB, SME, NAAIL. **Evidence relationship:** AI disclosure only; NOT LLM.

### Technical and cross-disciplinary references — AJG verification pending (5 records)

- **IJIM-2024-handler:** Handler, A., Larsen, K. R. and Hackathorn, R. (2024) ‘Large language models present new questions for decision support’, *International Journal of Information Management*. [DOI](https://doi.org/10.1016/j.ijinfomgt.2024.102811). **Focus:** LLM, decision-support, governance. **Project links:** NAAIL, IFRS. **Evidence relationship:** direct.
- **ESWA-2025-yan:** Yan, Y., Yu, H., Wang, D., Ye, J., Liu, F. and Xu, W. (2025) ‘STP: Special token prompt for parameter-efficient tuning of pre-trained language models’, *Expert Systems with Applications*. [DOI](https://doi.org/10.1016/j.eswa.2025.127665). **Focus:** fine-tuning, PEFT, NLP. **Project links:** POMELO, KIWI, NAAIL. **Evidence relationship:** direct.
- **ESWA-2026-amelio:** Amelio, A., Buratti, C., Marchetti, M., Traini, D., Ursino, D. and Virgili, L. (2026) ‘Exploiting knowledge graph communities to fine-tune large language models’, *Expert Systems with Applications*. [DOI](https://doi.org/10.1016/j.eswa.2025.129816). **Focus:** fine-tuning, knowledge graph, LLM. **Project links:** POMELO, IFRS. **Evidence relationship:** direct.
- **ESWA-2026-navas:** Navas-Loro, M., Takeda, H. and Satoh, K. (2026) ‘Large Language Models for translating contract-related texts to logical predicates: Prompting, fine-tuning or dedicated library?’, *Expert Systems with Applications*. [DOI](https://doi.org/10.1016/j.eswa.2025.131031). **Focus:** fine-tuning, symbolic verification, contract reasoning. **Project links:** IFRS, POMELO. **Evidence relationship:** direct.
- **JBR-2025-wobst:** Wobst, J. and Lueg, R. (2025) ‘Avoiding algorithm errors in textual analysis: A guide to selecting software, and a research agenda toward generative artificial intelligence’, *Journal of Business Research*. [DOI](https://doi.org/10.1016/j.jbusres.2025.115571). **Focus:** construct validity, LLM, text analysis. **Project links:** KIWI, ISSB. **Evidence relationship:** contextual.

## Reproducible Harvard bibliography / Crossref API workflow

From the repository root with **Python 3.11+** (no external packages or tokens):

```bash
# Offline reproducibility — seed records only (NO API metadata certification)
python -m research.literature.harvard_crossref --out reports/harvard_bibliography_offline.json

# Opt-in DOI metadata checks through Crossref REST API
python -m research.literature.harvard_crossref --online --delay 1 \
  --out reports/harvard_crossref_checks.json

# Tests for DOI/schema integrity, citation formatting and fail-closed reporting
python -m unittest discover -s research/literature/tests -p 'test_*.py' -v
```

Each online DOI retrieval uses `https://api.crossref.org/works/{doi}`; metadata is used for **mismatch detection**, not silent changes to a reviewed record. The API returns deposited bibliographic metadata (authors, date, title, venue, DOI); it does **not** certify relevance, reproducibility, article quality, copyright compliance, official AJG rating, or complete coverage of every paper on a topic. Optional polite-pool identification can be supplied via `--email` if desired. Crossref source: [REST documentation](https://www.crossref.org/documentation/retrieve-metadata/rest-api/).

### Opt-in API discovery queue for additional FT50 / AJG 4–1 references

The [journal and keyword search scope](literature/crossref_journal_search_scope.json) provides an **illustrative** eight-journal ISSN seed spanning AJG 4*, 4, 3, 2 and 1, and the [Crossref discovery script](literature/crossref_discovery.py) searches deposited DOI records for six LLM/fine-tuning/agentic AI query concepts. It saves a **candidate queue**, not accepted references, and intentionally cannot assert complete retrieval.

```bash
# Optional discovery — network access required, bounded by journal and keyword
python -m research.literature.crossref_discovery --online \
  --rows 20 --delay 1 \
  --out reports/llm_crossref_candidates_review_required.json

# Offline tests of the discovery restrictions
python -m unittest discover -s research/literature/tests -p 'test_*.py' -v
```

**Workflow:** a domain expert must extend the authorized AJG ISSN universe to all target journals, resolve 2024 grades against CABS, screen candidate titles/abstracts/full texts with permissions, reconcile duplicates and exclusions, and only then add verified DOI records to the reviewed bibliography. Search results cannot automatically validate relevance or theoretical claims. No live discovery request is made by GitHub Actions.

For the comprehensive review the user envisions, the next authorized stage is a **PRISMA-style search protocol** over all in-scope journals and years, using normalized ISSN, Crossref/OpenAlex/disciplinary indexes, search strings for `"large language model"`, `"generative AI"`, `"fine-tuning"`, `"agentic AI"`, `"multi-agent"`, `"RAG"`, and accounting/audit/finance/sustainability variants; screening and two-reviewer adjudication are still required. Search APIs can miss records and cannot infer AJG 2024 grade reliably. Keep a dated frozen reference corpus and an update log, and do not redistribute restricted publisher full text.

### Scientific status of this registry

- **Completed:** curated DOI-linked public list, structured topics and project maps, Harvard formatting rules, a manual grade-evidence register and Python audit/tests.
- **Not completed:** an exhaustive FT50/AJG 4–1 bibliometric census, a systematic/meta-analytic inclusion protocol, independent screening, actual API metadata check of all entries, full-text rights review, independent article replication or validation of every NAAIL claim.
- **Private working record:** original manuscripts, primary research notes and broader materials remain in **private, access-controlled personal Google Drive**; no access to that personal archive is implied by public links.

*Living research reference page — updated 31 October 2026.*
