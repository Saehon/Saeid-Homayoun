# FT50 Research Repositories (2023–2026): Integration Registry

**27 October 2026 · Status: registered source metadata only; no empirical model executed or replication PASS awarded.**

This catalog makes published FT50 accounting, finance and Management Science source repositories discoverable from the [NAAIL OpenLab](https://github.com/Saehon/Saeid-Homayoun). The [machine-readable registry](sources.json) includes source URLs, author roles, paper DOIs, rights flags and project mappings. It is not a bulk import or endorsement of third-party research.

## Research paper catalog (all 14 sources)

| ID | FT50 publication | Repository | Scope |
|---|---|---|---|
| 1 | [Machine Learning and the Implementable Efficient Frontier (2026)](https://doi.org/10.1093/rfs/hhag022) — The Review of Financial Studies | [theisij/ml-and-the-implementable-efficient-frontier](https://github.com/theisij/ml-and-the-implementable-efficient-frontier) | DARWIN asset pricing |
| 2 | [Generative AI in Financial Reporting (2026)](https://www.gsb.stanford.edu/faculty-research/publications/generative-ai-financial-reporting) — Journal of Accounting Research | [ed-dehaan/GenScore](https://github.com/ed-dehaan/GenScore) | POMELO, DARWIN AI CapEx |
| 3 | [Man versus Machine Learning Revisited (2025)](https://doi.org/10.1093/rfs/hhaf066) — The Review of Financial Studies | [yandi-zhu/Man-versus-Machine-Learning-Revisited](https://github.com/yandi-zhu/Man-versus-Machine-Learning-Revisited) | DARWIN earnings, independent falsification |
| 4 | [Measuring Investor Attention Using Google Search (2024)](https://doi.org/10.1287/mnsc.2022.02174) — Management Science | [robinlitjens/GoogleTickerStock-SVI](https://github.com/robinlitjens/GoogleTickerStock-SVI) | DARWIN announcements |
| 5 | [Using GPT to Measure Business Complexity (2026)](https://doi.org/10.2308/TAR-2023-0716) — The Accounting Review | [TiesdeKok/gpt-business-complexity](https://github.com/TiesdeKok/gpt-business-complexity) | KIWI CAM, POMELO IFRS |
| 6 | [Consensus? An Examination of Differences in Earnings Information Across Forecast Data Providers (2026)](https://doi.org/10.1111/1475-679x.70072) — Journal of Accounting Research | [eweisbrod/consensus](https://github.com/eweisbrod/consensus) | DARWIN earnings, analyst forecasts |
| 7 | [Company Websites: A New Measure of Disclosure (2026)](https://doi.org/10.1111/1475-679X.70007) — Journal of Accounting Research | [r-boulland/Company-Website-Disclosure](https://github.com/r-boulland/Company-Website-Disclosure) | POMELO ESG, VSME |
| 8 | [ChatGPT for Textual Analysis? How to Use Generative LLMs in Accounting Research (2025)](https://doi.org/10.1287/mnsc.2023.03253) — Management Science | [TiesdeKok/chatgpt_paper](https://github.com/TiesdeKok/chatgpt_paper) | KIWI CAM-Q, POMELO, DARWIN NLP |
| 9 | [Growing the Efficient Frontier on Panel Trees (2025)](https://doi.org/10.1016/j.jfineco.2025.104024) — Journal of Financial Economics | [Quantactix/PTree](https://github.com/Quantactix/PTree) | DARWIN factors, portfolio comparison |
| 10 | [Global Evolution of Environmental and Social Disclosure in Annual Reports (2024)](https://doi.org/10.1111/1475-679X.12575) — Journal of Accounting Research | [jar-es-disclosure/global-es-disclosure](https://github.com/jar-es-disclosure/global-es-disclosure) | POMELO ESG, Swedish VSME |
| 11 | [How Does Carbon Footprint Information Affect Consumer Choice? A Field Experiment (2024)](https://doi.org/10.1111/1475-679X.12505) — Journal of Accounting Research | [trr266/carbonfood](https://github.com/trr266/carbonfood) | POMELO sustainability, experimental design |
| 12 | [The Virtue of Complexity in Return Prediction (2024)](https://doi.org/10.1111/jofi.13298) — The Journal of Finance | [zivmi/voc_reproduction](https://github.com/zivmi/voc_reproduction) | DARWIN asset pricing, valuation |
| 13 | [Deep Learning-Based Causal Inference for Large-Scale Combinatorial Experiments (2025)](https://doi.org/10.1287/mnsc.2024.04625) — Management Science | [ysd1123/DeDL_Replication](https://github.com/ysd1123/DeDL_Replication) | DARWIN science core, JEV evaluation |
| 14 | [Is There a Replication Crisis in Finance? (2023)](https://doi.org/10.1111/jofi.13249) — The Journal of Finance | [bkelly-lab/jkp-data](https://github.com/bkelly-lab/jkp-data) | DARWIN Fama-French, JKP bridge |

**Publication window:** entries 1–13 have papers published within the approximately October 2023–October 2026 window. The JKP study (entry 14) was first published online in May 2023 and is deliberately marked as a pre-window foundational reference. The publication date of online-first work can differ from the printed issue year. Entry 12 and 13 GitHub repositories are **independent reproductions** rather than the authors' official materials.

## Installed mapping to research programmes

| Programme | Sources | Scientific objective |
|---|---|---|
| DARWIN Fama–French / AI CapEx asset pricing | 1, 9, 12, 14 | Factor construction, trading costs, out-of-time generalization |
| DARWIN earnings announcements and analyst forecasts | 2, 3, 4, 6 | Look-ahead bias, analyst-surprise definition, information sets |
| KIWI neuro-fuzzy CAM risk / POMELO | 5, 8 | Construct validation, financial-text complexity, interpretable account-risk features |
| POMELO sustainability and disclosures | 2, 7, 10, 11 | Disclosure intensity, firm websites, ESG and registered experiments |
| DARWIN Scientific Core and JEV | 3, 8, 13 | Negative controls, falsification, causal ML and post-model governance |

**Existing owner-side reference repos (not recopying):** [Saehon/jkp-data](https://github.com/Saehon/jkp-data) and [Saehon/gpt-business-complexity](https://github.com/Saehon/gpt-business-complexity). Existing [JKP bridge](../jkp-global-factors/README.md) is preserved. Private POMELO software remains in [pomelo-core](https://github.com/Saehon/pomelo-core); no private source is included in this public catalog.

## Controlled replication workflow

```text
FT50 DOI / upstream source
   -> G0 verify rights, licensing and attribution
   -> G1 source commit, SHA256, data-vintage, Evidence Passport
   -> G2 point-in-time CIK/GVKEY/PERMNO/account key + schema validation
   -> G3 prespecified estimand, training/evaluation split, leakage scan
   -> G4 benchmark execution, placebo / adversarial tests, FDR controls
   -> G5 independent reviewer, failure logging, no fabricated PASS
   -> JEV scientific judgement / human approval
```

**License policy:** An absent GitHub license is **not** permission to reproduce or relicense the source. GPL-3.0 implementations and CC BY-NC datasets must be reviewed separately. CC-BY-4.0 metadata is not authority to publish provider-restricted analyst forecasts or vendor data. Never sync WRDS/CRSP/Compustat, I/B/E/S, FactSet, confidential audit data or other restricted source files into public repositories, Kaggle, or Hugging Face without distribution rights.

**Dependency policy:** Do not merge the 14 sources into one Python environment. For an authorized selected source, pin its upstream commit, inspect its LICENSE and README, isolate dependencies, preserve citation, and store source access and experiment outputs privately. This index intentionally references third-party repositories without copying their contents.

## Verify the integration

```bash
python research-integrations/ft50-github-replication-2023-2026/verify_catalog.py
python research-integrations/ft50-github-replication-2023-2026/verify_catalog.py --online  # optional, queries GitHub public metadata
```

These commands validate references; they do **not** execute experiments. Retain insignificant results, all evaluated specifications, and replication failures for DARWIN/POMELO science governance.
