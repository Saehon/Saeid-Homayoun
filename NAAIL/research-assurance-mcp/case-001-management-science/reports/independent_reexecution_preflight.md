# Case 001 — Independent Re-execution Preflight

## Gate result
**BLOCKED_BEFORE_DATA_CONSTRUCTION**

This is **not a failed replication**. The independent run was initiated from the original uploaded replication ZIP, but required source data and proprietary statistical runtimes are unavailable in the current execution environment.

## Verified package state
- Original ZIP extracted successfully.
- Author code, README, environment specification, and stored logs are present.
- `2_pipeline` contains no generated intermediate datasets, as documented.
- `0_data/external` contains only placeholder files.

## Missing source inputs
1. `wrds_all_10qk_filings_07022022.xlsx`
2. `spac_main.xlsx`

The README also requires licensed WRDS datasets: Compustat, CRSP, Audit Analytics, WRDS SEC Analytics Suite, IBES, WRDS Linking Tables, Compustat Snapshot, and Thomson-Reuters 13F.

## Runtime comparison
| Component | Required | Current |
|---|---|---|
| Python | 3.9 | 3.13.5 |
| Conda | replication instructions | not installed |
| SAS | 9.4 | not installed |
| Stata | 17+ | not installed |

## Clean-run findings
- **R001:** Input-file naming mismatch: `08132021` in the first notebook vs `07022022` in README/placeholder.
- **R002:** `speed_bypass_loc.exists` is missing `()`; on a clean run the branch attempts to read a cache that has not been created.
- **R003:** `yaml.load(f)` does not run under the current PyYAML 6.x without a Loader. This is classified as environment compatibility unless reproduced in the specified Python 3.9 environment.

## Existing verified evidence
The prior author-output consistency result remains: **264/264 checked regression cells match the stored author Stata output at published precision.**

## Next gate
Independent reproduction becomes testable after authorized source data and compatible SAS/Stata/Python runtimes are available. Then the full pipeline should be executed and regenerated outputs compared against both the supplied logs and the 264-cell gold baseline.
