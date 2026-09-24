# CAM/KAM Data Schema

The preparation script requires three core fields:

| Field | Purpose |
|---|---|
| `title` | Short CAM/KAM heading |
| `description` | Auditor narrative describing the significant matter |
| `topic` | Accounting/audit topic label |

Recommended provenance and audit-context fields:

| Field | Purpose |
|---|---|
| `record_id` | Stable local identifier |
| `jurisdiction` | US / UK / EU / other |
| `matter_type` | CAM or KAM |
| `company` | Issuer name or anonymized identifier |
| `fiscal_year` | Fiscal year |
| `response` | Auditor response/procedures |
| `conclusion` | Auditor conclusion/observations, where available |
| `source_type` | SEC/EDGAR, licensed database, synthetic, other |
| `accession_number` | SEC accession number for public U.S. filings |
| `filing_url` | Public filing URL when redistribution is permitted |
| `topic_fkey` | Original topic key if present in licensed source |

## Public-release rule
Do not upload licensed Audit Analytics records unless the license explicitly permits redistribution. Public releases should use SEC/EDGAR-derived records with provenance, or synthetic examples.
