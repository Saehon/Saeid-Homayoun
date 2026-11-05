# Data access, redistribution boundaries and temporal provenance

**No third-party raw market data or monthly derived panels are bundled or published in this GitHub directory.** The public Python script fetches original research data at runtime from the listed publishers, records SHA-256 checksums, and builds retrospective analysis outputs in a local `outputs/` directory.

| Source | Role | Important boundary |
| --- | --- | --- |
| [OpenSourceAP/CrossSection](https://huggingface.co/datasets/OpenSourceAP/CrossSection) | 2021 and 2026 historical release comparison and research long–short returns | Hugging Face lists CC BY 4.0; attribution and upstream terms apply. The 2026 release is retrospective. |
| [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) | Five factors and RF | Consult publisher terms; current downloads may reflect later revisions. |
| [Tidy factor library](https://huggingface.co/datasets/tidy-finance/factor-library) | Portfolio returns, turnover, modeled costs | Hub lists CC0; each cost applies only to the **matching** Tidy construction ID. |
| [Tidy specification grid](https://huggingface.co/datasets/tidy-finance/factor-library-grid) | Portfolio construction details and identity | Exact `id` match is mandatory; method equivalence with OpenAP is not yet established. |

**Grain:** monthly calendar date, 60 months for the OpenAP+FF5 panel and 48 months for the separate Tidy return/cost panel. All eight selected OpenAP series are **research portfolio returns**, not contemporaneously measured firm characteristics. They must not be treated as evidence of investable signals with historically verified information release dates.

**Security:** never commit API keys, personal financial records, paid CRSP/Compustat/Refinitiv exports, private GitHub material or unpublished technical cores.
