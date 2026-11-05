# NOMOS V6 Phase 1 — Dataset Dictionary and Source Boundaries

**Primary output:** `reports/v6_revised_openap_ff5_2021_2025.csv` (60 monthly observations, Jan 2021–Dec 2025).

- `date`: first calendar day of the portfolio return month, ISO format. Single unique primary key.
- `historical_pit_verified`: constant `False` by design. A feature lag does not prove historical availability or prospective tradability.
- `data_release`: descriptive `OpenAP_2026.10_revised` for all rows; source is a 2026 revised retrospective file.
- `Accruals`, `AssetGrowth`, `BM`, `Mom12m`, `GP`, `Investment`, `EP`, `STreversal`: research portfolio **monthly long–short returns**, converted from OpenAP *percent* to **decimal fractions**. These are returns, **not contemporaneous firm characteristics**.
- `Mkt-RF`,`SMB`,`HML`,`RMW`,`CMA`,`RF`: Kenneth French monthly factor returns / RF, converted from *percent* to **decimal fractions**.
- `lag1_*`: previous calendar month's observation of the named *return* or *factor*; the 2021 January lag is computed from December 2020 historical data before slicing the 2021–2025 panel. **Cannot certify availability date of underlying accounting signals.**

**Auxiliary output:** `reports/v6_auxiliary_tidy_costs_2021_2024.csv` (48 monthly observations, Jan 2021–Dec 2024).

- Same `date`, eight OpenAP research series and French monthly factors.
- `tidy_<signal>_ret`: return of a **separately constructed Tidy Finance portfolio** for the selected immutable `id` listed in `v6_quality_report.json`; decimal fraction.
- `tidy_<signal>_turnover`: Tidy Finance turnover in the repository's native units.
- `tidy_<signal>_cost`: Tidy Finance modeled transaction cost in the repository's native units; **not a measured GPT/Claude inference charge** and not necessarily applicable to the corresponding OpenAP original portfolio.
- `tidy_<signal>_microcap_share`: Tidy Finance microcap share in the original source units.

**Primary key and data grain:** one row per calendar month. All eight Tidy cost and return IDs have been joined to their exact grid specification and matched monthly on ID and date; no zero-valued returns were silently imputed as missing.

**Critical limitations:** current 2026 release is retrospectively curated; the Tidy 2025.10 specification grid and 2026.10 OpenAP series differ in portfolio methods and possible data revisions. No prospective investment results, measure of real compute cost, alpha test, Sharpe test, or inference on expected investor profits is included here.
