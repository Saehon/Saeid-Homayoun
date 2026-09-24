# Microsoft Demo 001 — Phase 1 Open Accounting Data

This is the smallest end-to-end demonstration for the Open Accounting & Finance AI workflow.

## Goal

Use one public company, three fiscal years, four accounting variables, and one dependency-free Python script.

**Company:** Microsoft Corporation (MSFT)  
**CIK:** 0000789019  
**Years:** FY2023–FY2025  
**Unit:** USD millions

## Data

The example uses Microsoft FY2025 Annual Report figures for total revenue, gross profit, operating income, and net income.

Source: Microsoft Investor Relations, FY2025 Annual Report.

## Run

```bash
cd open-data/microsoft-demo-001
python analysis.py
```

Expected headline result for FY2025:

- Revenue: **$281.724bn**
- Revenue growth: **14.93%**
- Gross margin: **68.82%**
- Operating margin: **45.62%**
- Net margin: **36.15%**

## Files

- `microsoft_financials.csv` — compact research-ready data
- `analysis.py` — reproducible calculation
- `provenance.json` — provenance, company identifiers, field definitions and XBRL alignment

## Phase-1 architecture

```text
Microsoft public filing / annual report
               ↓
        canonical CSV
               ↓
        Python validation
               ↓
   GitHub source of truth
               ↓
Future: Hugging Face + Kaggle
```

This package is intentionally small. The next phase can replace the frozen three-year file with an automated SEC CompanyFacts/XBRL pull while retaining the same schema and provenance record.
