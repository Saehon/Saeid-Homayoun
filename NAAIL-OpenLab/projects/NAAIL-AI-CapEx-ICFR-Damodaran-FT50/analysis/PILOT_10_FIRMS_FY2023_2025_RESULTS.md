# Ten-company Damodaran empirical proxy pilot — 10 October 2026

**Actual exploratory Python computations performed; 10 firms × FY2023–FY2025 = 30 firm-years.** This is NOT the full FT50 AI CapEx × ICFR × CAM × PCAOB test.

## Verified links
- [Private underlying 30-row research CSV on Drive](https://drive.google.com/file/d/14RunpgmXgv8NIpUGfcM6pEdIO-ZONavy/view)
- [Canonical detailed numerical report, research claims, QA and source links on Drive](https://docs.google.com/document/d/1Sj_ghTrfGTiRWxkMO7SkSlVaSLdN9q-V008oiSqLIBI/edit)
- [Overall project master](https://drive.google.com/drive/folders/1O5fzl-AIMKGzwtfNavzKawBk6FfaFTR9)

## Sample
Builders: MSFT, GOOGL, AMZN, META, ORCL.
Suppliers: NVDA, AVGO, MU, VRT, ANET.
FY2023–2025 are actual **company fiscal years** (not common calendar years).

## Observed proxy financial ratios from Python
Company-wide gross cash PP&E capital expenditures / net cash provided by operating activities:
- FY2025 sample medians: builders 0.601822; suppliers 0.050492.
- Median change in ratio, FY2025 minus FY2023: builders +0.238214; suppliers −0.037964.
- Exact two-sided 5v5 permutation, **difference in means** of the FY2025 ratio: p=0.031746 (252 allocations).
- Exact two-sided 5v5 permutation, **difference in mean changes** FY2023–FY2025: p=0.007937 (252 allocations).
- Holm correction for these two permutation contrasts: 0.031746 and 0.015873, respectively.
- Exact two-sided Mann–Whitney FY2025 comparison U=22; p=0.055556. Different statistic from mean-difference permutation.
- Exact one-sided Wilcoxon of five builders' ratio changes p=0.031250.
- CapEx growth outpaced operating cash flow growth: 5/5 builders and 1/5 suppliers; two-sided Fisher exact p=0.047619.
- Outlier diagnostics: with Micron removed p=0.007937 (5 versus 4 firms) for mean ratio-change permutation; Oracle removed p=0.134921 (4 versus 5). Ex post sensitivity only.

## Crucial cautions
- **Nothing here identifies AI-specific CapEx**: the key source variable is **TOTAL cash purchases of PP&E**.
- **Gross cash proxy OCF−cash CapEx is NOT Damodaran FCFF** (nor necessarily issuer-disclosed FCF).
- Example Amazon: FY2025 gross capex $131,819m vs company-defined net-of-proceeds/incentives capex $128,320m. Corresponding cash proxies $7,695m vs Amazon reported FCF $11,194m: cite the SEC 10-K.
- The grouping is purposive, not randomized, and the FY periods differ; conditional p-values are diagnostics, not evidence of causality or population effects. Firm and industry effects are not identified with power in ten companies.
- NO actual CAM mapping, ICFR material-weakness classification, PCAOB exposure linkage, return model, firm WACC, ROIC or forward AI investment payoffs estimated. The inspection/CAM code in PR #163 is only a structural test scaffold.
- The 30 records were manually transcribed from publicly displayed StockAnalysis/S&P annual standardized tables. Primary source spot checks: MSFT, AMZN, ORCL; 7 other SEC cross-checks remain pending. The source data are retained in the controlled Google Drive, NOT copied to the public GitHub repo.

## Source manifest (secondary standardized annual cash-flow statements)
https://stockanalysis.com/stocks/msft/financials/cash-flow-statement/
https://stockanalysis.com/stocks/googl/financials/cash-flow-statement/
https://stockanalysis.com/stocks/amzn/financials/cash-flow-statement/
https://stockanalysis.com/stocks/meta/financials/cash-flow-statement/
https://stockanalysis.com/stocks/orcl/financials/cash-flow-statement/
https://stockanalysis.com/stocks/nvda/financials/cash-flow-statement/
https://stockanalysis.com/stocks/avgo/financials/cash-flow-statement/
https://stockanalysis.com/stocks/mu/financials/cash-flow-statement/
https://stockanalysis.com/stocks/vrt/financials/cash-flow-statement/
https://stockanalysis.com/stocks/anet/financials/cash-flow-statement/

## Direct issuer and SEC reconciliation spot checks
- MSFT FY2023–25: https://www.microsoft.com/investor/reports/ar25/index.html
- AMZN FY2023–25: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
- ORCL FY2023–25: https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm

## Replicate
From the research project root, install `pip install pandas numpy scipy`. Download the CSV from Drive to a controlled local folder, then run:

```bash
python analysis/run_10firm_pilot.py /path/to/10firm_pilot_FY2023_FY2025_secondary_cashflows.csv
```

**Next milestone:** SEC archival primary verification and AI-specific CapEx account-level labeling precede CAM/PCAOB interaction testing. No manuscript results should imply this narrow pilot already tests the full causal model.
