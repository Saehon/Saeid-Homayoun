# JKP Global Factors × NAAIL / DARWIN / POMELO

**Status (27 October 2026):** source-aware integration scaffold; reproducible validation with synthetic unit tests. **No licensed data downloaded, no WRDS session opened, no empirical asset-pricing results claimed, no external research collaboration established.**

This integration connects the open-source [JKP Global Factor Data](https://github.com/bkelly-lab/jkp-data) project to Saeid Homayoun's research infrastructure without copying restricted firm-level or vendor data into this public repository.

## Research aim

**Working title:** *Artificial Intelligence Investment, Accounting Information, and the Cross-Section of Stock Returns: A Global Factor Replication Study.*

Proposed initial period: **2020–2024**. Extend to 2025 only after independently verifying source coverage, the disclosure information date, and data-release version.

1. **JKP / factor benchmark:** externally documented factor definitions, universe and dates.
2. **Accounting / AI signal:** independently constructed company-year AI CapEx or disclosure measures, with auditable SEC/XBRL source and information-availability date.
3. **DARWIN:** prespecified models, discovery, temporal separation, sensitivity analysis, multiple-testing controls, negative results and independent falsification.
4. **POMELO / JEV:** evidence passport, dataset licence/provenance ledger, model comparison, human scientific review.
5. **Output:** controlled, reproducible research package; share only materials whose distribution is permitted.

## Local installation and verification

This adapter **does not clone, vendor, or relicense the upstream JKP code**. If you need to recreate the JKP source data from WRDS, independently follow the [upstream README](https://github.com/bkelly-lab/jkp-data/blob/main/README.md) and its access requirements; the upstream code requires valid WRDS access and may require substantial memory/compute.

For precomputed factors, obtain an authorized CSV or Parquet download from [jkpfactors.com](https://jkpfactors.com/) or another permitted source. Before running, inspect the source column names, grain (monthly/daily, geography) and units (decimal vs percent); normalize a local copy if required. Do **not** assume arbitrary downloaded columns are called \`date\`, \`MKT\`, \`SMB\` or \`HML\`.

Example for a **user-prepared wide CSV** with columns \`date,country,MKT,SMB,HML\` (illustrative schema, **not** a claim about JKP's native downloads):

\`\`\`bash
python research-integrations/jkp-global-factors/jkp_bridge.py \
  --input /secure/licensed/jkp_factors_normalized.csv \
  --date-column date \
  --key-columns country \
  --factor-columns MKT,SMB,HML \
  --start 2020-01-01 --end 2024-12-31 \
  --frequency monthly \
  --report /secure/outputs/jkp_provenance_report.json
\`\`\`

This produces a *schema/provenance quality report*, **not an asset-pricing regression or validated scientific finding**. It records file SHA-256, period and key uniqueness, sample coverage and factor missingness. No observations from the input file are included in the report. Factor units remain unverified/unchanged. Parquet input requires \`pandas\` and \`pyarrow\`; CSV uses only the standard library.

Run synthetic tests:

\`\`\`bash
python -m unittest discover \
  -s research-integrations/jkp-global-factors/tests -v
\`\`\`

## Important empirical boundaries

- A contemporaneous factor-return regression measures exposure/attribution; it is **not** by itself a tradable forecast or causal effect.
- Firm-specific AI measures must be dated **as of first public availability**; lag characteristics before forecasting future returns. Contemporaneous benchmark factor realizations are not ex ante predictors.
- Validate firm identifiers, currency, exchange, country, delisting returns, return units, coverage and survivorship before joining.
- Fit and tune models exclusively on training windows; hold out future periods and countries as prespecified. Include Fama–French and JKP traditional baselines.
- Track **every** specification and result, including nulls and replication failures; apply suitable multiple-testing adjustments and report economic as well as statistical significance.
- The [JKP Common Task Framework](https://jkpfactors.com/ctf/rules) has a separate dataset-only input policy. External SEC/AI variables must stay in the **independent research extension**, not an incompatible CTF submission.

## Local repo interoperability

- [NAAIL OpenLab master](https://github.com/Saehon/Saeid-Homayoun): scientific oversight, disclosure provenance, final results.
- [CrossSection](https://github.com/Saehon/CrossSection): existing cross-sectional asset-pricing replication code (based on Chen and Zimmermann, not JKP). Do not silently overwrite its original methods.
- [selective_multiple_testing](https://github.com/Saehon/selective_multiple_testing): existing selective-inference code (based on Pelger and Zou); reuse only with correct sample structure and citation.
- [AuditData-API](https://github.com/Saehon/AuditData-API): potential accounting evidence connector; schema/permission validation required before integration.

See [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md), [DATA_POLICY.md](DATA_POLICY.md) and [JKP_COLLABORATION_DRAFT.md](JKP_COLLABORATION_DRAFT.md).

## Citation and attribution

Jensen, T. I., Kelly, B. T., & Pedersen, L. H. (2023). Is there a replication crisis in finance? *The Journal of Finance, 78*(5), 2465–2518. https://doi.org/10.1111/jofi.13249

Upstream source code licence: **MIT**. Repository-distributed JKP data licence: **CC BY-NC 4.0**, subject also to any underlying vendor/licensed-data restrictions. No affiliation, endorsement, coauthorship or accepted contribution is implied by this integration.

Upstream [contributing guide](https://github.com/bkelly-lab/jkp-data/blob/main/CONTRIBUTING.md) · [ideas discussions](https://github.com/bkelly-lab/jkp-data/discussions/categories/ideas) · [data changelog](https://github.com/bkelly-lab/jkp-data/blob/main/CHANGELOG_DATA.md).
