# FT50 / AJG 4-4* — AI, Generative AI, LLMs and Agentic AI (2021–2026)

**As-of:** 2026-10-10. **Window:** 2021-10-10 through 2026-10-10 inclusive. 
**Status:** screened seed list, **NOT an exhaustive systematic census** of all articles published in all FT50 or AJG 4/4* journals; no code was run from external replication archives. 

**Google Drive canonical master folder:** https://drive.google.com/drive/folders/14xKN3F1TJawOl_EsO54VcpwNp59q2_Id
**Parent:** https://drive.google.com/drive/folders/1Uwg6JQnYR7I1d4okogO1eTHyd0NcKo0C

## Evidence registry
The [paper-level CSV](ft50_ai_llm_agentic_papers_2021_2026.csv) contains **42** individually scoped journal articles with URL, paper type, AI type, AJG 2024 rating, FT50 2026 inclusion, research topic, code and data *separately*, and important original-data restrictions. These are **selected, source-backed records**; they do not establish that every FT50 paper was searched.

### Journal coverage (AJG 2024 and updated FT50 2026)
- Journal of Accounting Research: 9
- Management Science: 7
- Information Systems Research: 7
- Journal of Financial Economics: 6
- Review of Accounting Studies: 4
- Marketing Science: 3
- Review of Financial Studies: 2
- Contemporary Accounting Research: 1
- The Accounting Review: 1
- Quarterly Journal of Economics: 1
- Strategic Management Journal: 1

### Access categories
- **Free academic repository code:** JAR Volume 64 AI papers: https://www.chicagobooth.edu/research/chookaszian/journal-of-accounting-research/online-supplements-and-datasheets/volume-64 (academic-only terms; underlying data may be proprietary). 
- **Free GitHub code with derivative/sample datasets:** de Kok, LOLA, Twin-2K-500, LLM Peers. See CSV for exact artifact link and data restriction.
- **Publicly downloaded original/pseudodata mixes:** Babina (2024) JFE has *pseudo inputs* for Cognism/Compustat; full original estimates cannot be reproduced without licensed sources. Lopez-Lira & Tang JFE (2026) offers 500 MB Mendeley package, paper relies on CRSP/RavenPack/TAQ. 
- **Publisher supplementary files only:** a publisher lists files, but executable code, its licensing and numerical replication have not been independently tested.
- **No code located:** lack of verified code link does *not* prove a paper has no code.

### Strongest open tool/data replication onramp
1. **LLM accounting NLP:** https://github.com/TiesdeKok/chatgpt_paper (labelled non-answers in earnings calls + examples).
2. **LLM marketing/experimental data:** https://github.com/DDDOH/LLM_News with public original Upworthy OSF https://osf.io/jd64p/ ; proprietary LLM API can be an optional dependency.
3. **Digital-twin simulation:** https://github.com/tianyipeng-lab/Digital-Twin-Simulation, behavioural survey dataset, privacy/terms audit.
4. **Peer-firm retrieval:** https://github.com/ycao25/LLM_Peers, derived firm peer scores keyed by Compustat GVKEY, original Compustat subscription NOT included.
5. **JAR 2026 research frontiers:** AI in reporting, accounting work, AI trading, intermediary disclosure, bias and leakage with Chicago Booth academic code packages.
6. **JFE LLM return forecasting:** https://data.mendeley.com/datasets/f39x226htv/1; not a freely licensed CRSP/newswire replacement.
7. **QJE labour productivity:** Harvard Dataverse https://doi.org/10.7910/DVN/FSV1X7; code listed, confidential firm microdata restrictions need confirmation.

### Research relevance and novelty discipline
Candidate applications: AI disclosure-implementation gap, ICFR, CAM/KAM risk alignment, AI labour market/mobility, return prediction, human–AI audit decisions, multi-agent audit-evidence governance. Use a PRISMA review with full reproducible journal/year queries before claiming exhaustiveness or new theoretical hypotheses. The limited source audit does not establish novelty, causal identification or significant results.

### Files
- `ft50_ai_llm_agentic_papers_2021_2026.csv` — source-level curated record.
- `FT50_AI_LITERATURE_METHOD.md` — search terms, verification rules and limits.
- `FT50_AI_TOPIC_MAP.md` — topic categories, best entry points and research gaps.
- Drive master docs: canonical scientific record and cross-platform links.

**No proprietary datasets, copyrighted article PDFs, personal résumés, or replication ZIPs are mirrored.**
