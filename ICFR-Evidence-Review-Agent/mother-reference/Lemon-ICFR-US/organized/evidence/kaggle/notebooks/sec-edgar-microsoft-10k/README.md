# SEC EDGAR Microsoft 10-K — Version 2

This experiment extends the first GitHub → Kaggle connection test into a small accounting analysis using Microsoft SEC 10-K data.

## Research question

How did Microsoft revenue, total assets, and R&D change from fiscal 2024 through fiscal 2026?

## Measures

All figures come from Microsoft annual filings and are reported in USD millions in the source filings.

| Fiscal year | Revenue | Total assets | R&D |
|---|---:|---:|---:|
| 2024 | 245,122 | 512,163 | 29,510 |
| 2025 | 281,724 | 619,003 | 32,488 |
| 2026 | 331,839 | 758,376 | 35,562 |

The script calculates year-over-year growth and R&D intensity (R&D / revenue), then creates an indexed trend chart with 2024 = 100.

## Outputs

- `microsoft_sec_edgar_trend_2024_2026.csv`
- `microsoft_sec_edgar_indexed_trends.png`

## Sources

- Microsoft 2024 Form 10-K: https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm
- Microsoft 2025 Annual Report: https://www.microsoft.com/investor/reports/ar25/
- Microsoft 2026 Form 10-K: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm

This remains a simple reproducible research demonstration, not investment advice.
