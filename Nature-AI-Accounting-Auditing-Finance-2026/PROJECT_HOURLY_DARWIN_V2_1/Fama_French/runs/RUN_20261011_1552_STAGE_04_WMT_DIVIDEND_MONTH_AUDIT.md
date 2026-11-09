# DARWIN V5 Fama–French — WMT dividend-month audit

2026-10-11 15:52 Europe/Stockholm. One scientific task executed: JS comparison of existing Drive WMT monthly cash dividend rows with official Walmart 2024–2026 dividend announcements.

Input: 93 ticker-month rows, WMT 31 monthly rows. Official expected dividends: 2024 March/May/August/December 0.2075 each; 2025 same four months 0.235 each; 2026 March/May 0.2475 each. Actual 10/10 events, 0 month/amount mismatches across 31 WMT rows, sum USD 2.265, 0/31 arithmetic mismatches. January 2025/2026 cash dividends zero; dividends are allocated to ex-dividend month rather than payment month.

Official source 2024: https://corporate.walmart.com/news/2024/02/20/walmart-raises-annual-dividend-9-percent-to-83-per-share-the-largest-increase-in-over-10-years-marking-51st-consecutive-year-of-dividend-increases
Official source 2025: https://corporate.walmart.com/news/2025/02/20/walmart-raises-annual-dividend-13-percent-to-0-94-per-share-marking-52nd-consecutive-year-of-dividen-increases
Official source 2026: https://corporate.walmart.com/news/2026/02/19/walmart-raises-annual-dividend-to-0-99-per-share-marking-53rd-consecutive-year-of-dividend-increases

Only bounded dividend event timing/arithmetic PASS. Price adjustment flag and potential dividend double counting remain UNVERIFIED; firm-wide return panel, survivorship-safe sampling, AI exposure and regression remain BLOCKED. No CI PASS, Codex, alpha, p-value or independent replication claimed.

Drive report: https://docs.google.com/document/d/1_gXph5aNX60giMAW15D4xf0GNPKrrTay9uENHzjGdrE/edit
Source sheet: https://docs.google.com/spreadsheets/d/1M7aCxdHxFCc61jnyiAgdPQg5YIpHYDFoCcf19VD29oY/edit
Next: independently verify vendor price adjustment flag before constructing total stock returns.
