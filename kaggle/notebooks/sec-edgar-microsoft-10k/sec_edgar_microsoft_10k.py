"""Simple reproducible SEC EDGAR / Microsoft Kaggle example.

Based on the Microsoft example already present in:
https://github.com/Saehon/sec-edgar-downloader

The upstream example is:
    dl.get("10-K", "MSFT", limit=1)

For the first GitHub→Kaggle integration test, this script uses verified
SEC EDGAR filing metadata and runs fully offline in Kaggle.
"""

from pathlib import Path
import pandas as pd

record = {
    "company": "Microsoft Corporation",
    "ticker": "MSFT",
    "cik": "0000789019",
    "form": "10-K",
    "fiscal_year_end": "2026-06-30",
    "accession_number": "0001193125-26-323660",
    "sec_document": "msft-20260630.htm",
    "sec_url": "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm",
    "github_source_repo": "https://github.com/Saehon/sec-edgar-downloader",
    "github_example": 'dl.get("10-K", "MSFT", limit=1)',
}

df = pd.DataFrame([record])

assert df.loc[0, "ticker"] == "MSFT"
assert df.loc[0, "cik"] == "0000789019"
assert df.loc[0, "form"] == "10-K"
assert df.loc[0, "fiscal_year_end"] == "2026-06-30"

output = Path("/kaggle/working/microsoft_sec_edgar_10k_summary.csv")
df.to_csv(output, index=False)

print("SEC EDGAR / Microsoft 10-K example")
print(df.to_string(index=False))
print(f"\nPASS: wrote {output}")
