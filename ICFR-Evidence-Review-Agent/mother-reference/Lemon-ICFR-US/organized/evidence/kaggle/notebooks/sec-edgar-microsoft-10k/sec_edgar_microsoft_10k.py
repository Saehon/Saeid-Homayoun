"""Microsoft SEC EDGAR accounting trends, FY2024-FY2026.

Source: Microsoft Corporation Forms 10-K filed with the U.S. SEC.
All financial statement amounts are USD millions.

Outputs:
- microsoft_sec_edgar_trend_2024_2026.csv
- microsoft_sec_edgar_indexed_trends.png
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

data = [
    {
        "fiscal_year": 2024,
        "revenue_usd_m": 245122,
        "total_assets_usd_m": 512163,
        "rd_usd_m": 29510,
        "sec_source": "https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm",
    },
    {
        "fiscal_year": 2025,
        "revenue_usd_m": 281724,
        "total_assets_usd_m": 619003,
        "rd_usd_m": 32488,
        "sec_source": "https://www.microsoft.com/investor/reports/ar25/",
    },
    {
        "fiscal_year": 2026,
        "revenue_usd_m": 331839,
        "total_assets_usd_m": 758376,
        "rd_usd_m": 35562,
        "sec_source": "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm",
    },
]

df = pd.DataFrame(data).sort_values("fiscal_year").reset_index(drop=True)

# Convert to USD billions for presentation.
for col in ["revenue_usd_m", "total_assets_usd_m", "rd_usd_m"]:
    df[col.replace("_usd_m", "_usd_bn")] = df[col] / 1000

# Accounting/research metrics.
df["revenue_yoy_pct"] = df["revenue_usd_m"].pct_change() * 100
df["assets_yoy_pct"] = df["total_assets_usd_m"].pct_change() * 100
df["rd_yoy_pct"] = df["rd_usd_m"].pct_change() * 100
df["rd_intensity_pct"] = df["rd_usd_m"] / df["revenue_usd_m"] * 100

# Indexed trend chart (2024 = 100) so the three accounting measures are comparable.
for col in ["revenue_usd_m", "total_assets_usd_m", "rd_usd_m"]:
    df[col.replace("_usd_m", "_index_2024_100")] = df[col] / df.loc[0, col] * 100

output_csv = Path("/kaggle/working/microsoft_sec_edgar_trend_2024_2026.csv")
df.to_csv(output_csv, index=False)

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(df["fiscal_year"], df["revenue_index_2024_100"], marker="o", label="Revenue")
ax.plot(df["fiscal_year"], df["total_assets_index_2024_100"], marker="o", label="Total assets")
ax.plot(df["fiscal_year"], df["rd_index_2024_100"], marker="o", label="R&D")
ax.axhline(100, linewidth=1)
ax.set_title("Microsoft SEC 10-K Trends, FY2024-FY2026 (2024 = 100)")
ax.set_xlabel("Fiscal year")
ax.set_ylabel("Index")
ax.set_xticks(df["fiscal_year"])
ax.legend()
ax.grid(True, alpha=0.25)
fig.tight_layout()

output_png = Path("/kaggle/working/microsoft_sec_edgar_indexed_trends.png")
fig.savefig(output_png, dpi=160)
plt.close(fig)

display_cols = [
    "fiscal_year",
    "revenue_usd_bn",
    "total_assets_usd_bn",
    "rd_usd_bn",
    "revenue_yoy_pct",
    "assets_yoy_pct",
    "rd_yoy_pct",
    "rd_intensity_pct",
]

print("Microsoft SEC EDGAR accounting trends (USD billions unless %)")
print(df[display_cols].round(2).to_string(index=False))

print("\nKey observations")
print(f"- Revenue grew {df.loc[1,'revenue_yoy_pct']:.1f}% in 2025 and {df.loc[2,'revenue_yoy_pct']:.1f}% in 2026.")
print(f"- Total assets grew {df.loc[1,'assets_yoy_pct']:.1f}% in 2025 and {df.loc[2,'assets_yoy_pct']:.1f}% in 2026.")
print(f"- R&D intensity declined from {df.loc[0,'rd_intensity_pct']:.1f}% in 2024 to {df.loc[2,'rd_intensity_pct']:.1f}% in 2026, while absolute R&D spending increased.")

print(f"\nPASS: wrote {output_csv}")
print(f"PASS: wrote {output_png}")
