# GPT-5.6 Sol Review — FF49 × Damodaran 2026 Crosswalk

## Status

- Reviewer: **GPT-5.6 Sol**
- Review type: semantic/economic industry mapping review
- Source year: **2026 Damodaran U.S. industry taxonomy**
- Output: `gpt56sol_reviewed_crosswalk_2026.csv`
- `review_status = AI_REVIEWED`
- `human_gate_approved = false`
- This file is **not** a substitute for a human-approved historical crosswalk.

## Evidence basis

The Fama–French 49-industry portfolios are assigned using four-digit SIC codes at the end of June. The 2026 Damodaran U.S. industry taxonomy was reviewed directly from NYU Stern's current industry beta table. The mapping therefore uses economic-sector correspondence between the FF49 label and one or more Damodaran 2026 categories.

## Mapping policy

1. Prefer one-to-one mappings where sector definitions align closely.
2. Use weighted many-to-many mappings when Damodaran splits a broader FF49 category into multiple sectors.
3. Require mapping weights to sum to 1.00 within each FF49 industry.
4. Assign `HIGH`, `MEDIUM`, or `LOW` confidence.
5. Preserve uncertain/residual mappings instead of forcing false precision.
6. Do not copy the 2026 crosswalk mechanically to 2012–2025. Each historical Damodaran vintage must be reconciled against its own taxonomy.
7. No empirical result based on this mapping may be called a verified discovery before the Human Gate.

## Highest-confidence direct matches

Examples include Agriculture → Farming/Agriculture; Food → Food Processing; Soft Drinks → Beverage (Soft); Beer → Beverage (Alcoholic); Tobacco → Tobacco; Books → Publishing & Newspapers; Medical Equipment → Healthcare Products; Rubber → Rubber & Tires; Steel → Steel; Machinery → Machinery; Aerospace → Aerospace/Defense; Ships → Shipbuilding & Marine; Gold → Precious Metals; Mines → Metals & Mining; Coal → Coal & Related Energy; Paper → Paper/Forest Products; and Boxes → Packaging & Container.

## Important split mappings

Broad FF49 categories are intentionally decomposed. Examples: Oil is split across integrated, exploration/production, distribution, and oilfield services; Utilities across Power, Utility (General), and Utility (Water); Telecom across services, wireless, and equipment; Retail across general, special lines, automotive, building supply, and grocery; Insurance across general, life, property/casualty, and reinsurance; Real Estate across REITs, development, diversified real estate, and operations/services; Finance across non-bank financial services, brokerage/investment banking, and investments/asset management.

## Low-confidence areas requiring priority human review

`Toys`, `Txtls`, `FabPr`, `PerSv`, selected `BusSv` components, `Hardw` office-equipment allocation, and especially `Other` are less clean because the Damodaran taxonomy does not provide a direct one-to-one category. These rows must receive priority manual review before promotion into `reviewed_crosswalk.csv`.

## Next scientific step

Use this 2026 crosswalk as a **semantic seed**. For each Damodaran historical vintage from 2012–2025, compare the available industry labels against the seed, retain direct matches, flag taxonomy changes, revise weights only with documented evidence, and produce a year-specific reviewed crosswalk. Only after that should the panel merge and Tables 1–5 be run.
