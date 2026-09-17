# NAAIL Prototype V1.3 — Patent / Innovation Aggregate Gate

**Date:** 2026-09-17  
**Status:** `REGISTERED_NOT_EXECUTED` for aggregate counts/citations/diversity  
**Companies:** Microsoft · Walmart · JPMorgan Chase

## Current source state
USPTO states that PatentsView is now hosted through the Open Data Portal and that annualized data were updated through **December 2025**. PatentsView supplies research-grade entity resolution for organizations and inventors and makes annualized, granted-patent and other research datasets available.

Current access conditions matter for reproducibility. USPTO Open Data Portal documentation states that ODP access requires a USPTO.gov sign-in beginning **June 18, 2026**, and programmatic Search API use requires an API key.

Sources:
- https://www.uspto.gov/ip-policy/economic-research/patentsview
- https://www.uspto.gov/subscription-center/2026/june-17-new-update-patentsview-annualized-datasets
- https://data.uspto.gov/apis/bulk-data/search

## V1.3 decision
The public source is suitable for the planned patent/innovation module, but this runtime does not have the user's authenticated ODP/API credential. Therefore NAAIL does **not** publish manufactured company patent counts, citation totals or technology-diversity measures.

## Required execution
1. Resolve canonical PatentsView organization IDs plus controlled subsidiary/alias lists.
2. Freeze the annualized/disambiguated source release.
3. Compute granted-patent counts by grant year.
4. Compute forward citations using a documented citation window.
5. Compute CPC/technology-class diversity.
6. Scale only where conceptually meaningful (for example, patents/R&D for technology-intensive firms).
7. Preserve `NOT_MEANINGFUL_FOR_CONSTRUCT` outcomes rather than forcing comparability across MSFT, WMT and JPM.
8. Attach source hash, query manifest and entity-resolution decisions to the Evidence Passport.

**Scientific boundary:** source availability is verified; aggregate innovation evidence is not yet executed.
