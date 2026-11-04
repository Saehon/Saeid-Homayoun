# P2.1 Verified AI–Finance Literature Register

Version: 1.0  
Gate: P2.1 — Verify JFE/JF/RFS/Management Science AI-finance literature  
Verification date: 2026-10-07  
Status: FROZEN VERIFIED SEED REGISTER

## Scope and acceptance rule

This register verifies a bounded, outlet-balanced seed set for the project's later
literature graph, replication inventory, contradiction map and novelty analysis.
P2.1 passes only if:

1. all four named outlets are represented;
2. title, authors, venue, bibliographic location and DOI are verified against a
   publisher or journal record;
3. each record states what it can and cannot support for this project;
4. corrections, expressions of concern or other integrity notices are checked;
5. replication-package availability is not inferred from publication alone.

This is not an exhaustive systematic review, a novelty claim, a replication, or
evidence that any reported empirical result generalizes to AI Disagreement.

## Verified seed records

| ID | Verified publication record | Method / object | Project use permitted | Claim boundary and integrity status |
|---|---|---|---|---|
| LIT-JFE-001 | Tania Babina, Anastassia Fedyk, Alex Xi He, and James Hodson (2024), “Artificial intelligence, firm growth, and product innovation,” *Journal of Financial Economics* 151, 103745. DOI: [10.1016/j.jfineco.2023.103745](https://doi.org/10.1016/j.jfineco.2023.103745). | Firm AI investment, growth and product innovation. | Theory/evidence node for firm adoption, scale and innovation mechanisms. | Does not validate LLM financial judgments, disagreement constructs, or causal mechanisms outside the paper's design. No integrity notice observed in the checked publisher record. |
| LIT-JFE-002 | Alejandro Lopez-Lira and Yuehua Tang (2026), “Can ChatGPT forecast stock price movements? Return predictability and large language models,” *Journal of Financial Economics* 184, 104335. DOI: [10.1016/j.jfineco.2026.104335](https://doi.org/10.1016/j.jfineco.2026.104335). | LLM interpretation of firm-specific news and subsequent market reactions. | Direct benchmark for P4.2 and chronology/model-version controls. | Supports a single-model news-prediction benchmark, not the project's multi-model AID construct or future performance. Publisher record was in-progress/recent at verification; bibliographic status must be rechecked before final manuscript freeze. |
| LIT-JF-001 | Andreas Fuster, Paul Goldsmith-Pinkham, Tarun Ramadorai, and Ansgar Walther (2022), “Predictably Unequal? The Effects of Machine Learning on Credit Markets,” *The Journal of Finance* 77(1), 5–47. DOI: [10.1111/jofi.13090](https://doi.org/10.1111/jofi.13090). | Machine-learning credit prediction and distributional consequences. | Boundary-condition and governance node for accuracy/fairness tradeoffs. | The publisher explicitly cautions that counterfactual magnitudes are not precise predictions. This does not establish effects for capital-market LLM disagreement. No integrity notice observed in the checked publisher record. |
| LIT-RFS-001 | Shihao Gu, Bryan Kelly, and Dacheng Xiu (2020), “Empirical Asset Pricing via Machine Learning,” *The Review of Financial Studies* 33(5), 2223–2273. DOI: [10.1093/rfs/hhaa009](https://doi.org/10.1093/rfs/hhaa009). | Comparative machine-learning prediction of asset risk premia. | Foundational benchmark for nonlinear prediction, OOS design and model comparison. | It does not study generative LLMs, model disagreement, or text-evidence provenance. No integrity notice observed in the checked publisher record. |
| LIT-RFS-002 | Jules H. van Binsbergen, Xiao Han, and Alejandro Lopez-Lira (2023), “Man versus Machine Learning: The Term Structure of Earnings Expectations and Conditional Biases,” *The Review of Financial Studies* 36(6), 2361–2396. DOI: [10.1093/rfs/hhac085](https://doi.org/10.1093/rfs/hhac085). | Random-forest benchmark for earnings expectations and analyst conditional bias. | Methodological comparator only; quarantined from use as clean confirmatory benchmark. | **Integrity alert:** Oxford Academic published an Expression of Concern in 2026. All downstream reliance is quarantined pending P2.2/P4 review of the notice, data, code and any resolution. It must not be presented as uncontested evidence. |
| LIT-RFS-003 | Manish Jha, Hongyi Liu, and Asaf Manela (2026), “Does Finance Benefit Society? A Language Embedding Approach,” *The Review of Financial Studies* 39(5), 1227–1266. DOI: [10.1093/rfs/hhaf012](https://doi.org/10.1093/rfs/hhaf012). | Contextual BERT embeddings for sentiment toward finance. | Direct methodological anchor for P4.3 embedding/construct workflow and construct-validity tests. | It studies a sector-sentiment construct, not firm-level financial forecasts or multi-LLM disagreement. No integrity notice observed in the checked publisher record. |
| LIT-MS-001 | Ties de Kok (2025), “ChatGPT for Textual Analysis? How to Use Generative LLMs in Accounting Research,” *Management Science* 71(9), 7888–7906. DOI: [10.1287/mnsc.2023.03253](https://doi.org/10.1287/mnsc.2023.03253). | Generative-LLM textual analysis, validation, bias, replicability and data-sharing concerns. | Direct protocol anchor for P4.1, prompt/task validation and reproducibility controls. | Method guidance and task evidence do not validate this project's prompts, constructs or model panel. Publisher record links supplemental material and a companion site; package contents remain P2.2 work. No integrity notice observed. |
| LIT-MS-002 | Luyang Chen, Markus Pelger, and Jason Zhu (published online 2023; issue 2024), “Deep Learning in Asset Pricing,” *Management Science* 70(2), 714–750. DOI: [10.1287/mnsc.2023.4695](https://doi.org/10.1287/mnsc.2023.4695). | Deep neural conditional asset-pricing model with adversarial test-asset construction. | Methodological comparator for nonlinear representation, disciplined OOS evaluation and economic objectives. | It is not an AlphaFold/AlphaEvolve implementation and does not validate LLM disagreement. The year distinction is preserved rather than silently collapsed. No integrity notice observed. |

## Outlet coverage and evidence classes

| Outlet | Verified records | Primary role in this project |
|---|---:|---|
| Journal of Financial Economics | 2 | AI adoption and direct LLM/news-return benchmark |
| The Journal of Finance | 1 | ML credit-market consequences and fairness boundary |
| The Review of Financial Studies | 3 | ML asset pricing, analyst benchmark, language embeddings |
| Management Science | 2 | Generative-LLM research protocol and deep asset pricing |
| **Total** | **8** | Verified seed set, not exhaustive review |

## Cross-record synthesis for the Science Discovery graph

1. **Prediction is not a construct-validity result.** Strong predictive performance
   in returns, credit or earnings cannot by itself validate AI Disagreement.
2. **Text methods require task-specific validation.** LLM and embedding papers motivate
   explicit prompt/model/task provenance, but their reported performance cannot be
   transferred to this project's evidence packets.
3. **Economic and distributional consequences can diverge from accuracy.** The credit
   evidence motivates fairness, heterogeneity and welfare boundary conditions.
4. **Chronology is a first-class control.** Recent-model knowledge, publication timing,
   news timing and outcome timing must be separated before replication or inference.
5. **Integrity notices propagate.** LIT-RFS-002 is a live adverse-evidence node:
   downstream replications and literature claims depending on it remain quarantined.

## Required downstream actions

- P2.2: inventory official supplements, code, data, licenses and access conditions for
  all eight records; inspect the LIT-RFS-002 Expression of Concern and resolution status.
- P2.3: create literature→method→construct→test edges without converting reported
  associations into project evidence.
- P2.4: map conflicts in accuracy, interpretation, fairness, chronology and external
  validity.
- P2.5: expand search coverage, document search strings/dates and freeze the systematic
  literature matrix and novelty map.
- P4.1–P4.3: replicate only where official packages, licenses, data and chronology permit.

## Falsification and audit checks

| Check | Result |
|---|---|
| Four required outlets represented | PASS |
| Eight titles and DOI identities checked against official publisher/journal records | PASS |
| Publication year/issue ambiguity preserved where applicable | PASS |
| Integrity-notice search performed and adverse notice preserved | PASS — LIT-RFS-002 quarantined |
| Replication availability inferred from article publication | PASS — prohibited; deferred to P2.2 |
| External model runs or empirical replication claimed | PASS — none claimed |
| Exhaustiveness or novelty claimed | PASS — none claimed |

## Gate conclusion

P2.1 is PASS for a versioned, primary-record-verified, outlet-balanced seed register.
The PASS does not mean the literature review is exhaustive. The Expression of Concern
is not a blocker to verifying the literature record; it is preserved as adverse evidence
and creates a dependency quarantine for reliance on LIT-RFS-002. No model execution,
replication, causal conclusion or publication-readiness claim is made.
