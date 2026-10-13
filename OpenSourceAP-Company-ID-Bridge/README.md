# OpenSourceAP Company-ID Bridge

Builds one firm-year CSV linking public OpenSourceAP firm-level characteristics to company/security identifiers from Std_Security_Code.

## Output
`osap_company_id_master_2019_2024.csv`

One row per PERMNO × calendar year using the December OpenSourceAP observation for 2019–2024. The file places PERMNO/PERMCO/GVKEY/CIK identifiers first, preserves mapping ambiguity flags, and then retains all characteristics present in the public OpenSourceAP wide release.

## Why 2019–2024
U.S. CAM reporting begins in 2019 and the October 2025 OpenSourceAP release states that most characteristics extend through December 2024.

## Public-data limit
The public wide OpenSourceAP file contains 209 predictive firm-level characteristics. OpenSourceAP states that Price, Size, and STreversal are omitted because those come from CRSP. This project does not claim 212 firm characteristics without WRDS/CRSP access.

## Identifier warning
Std_Security_Code states that its identifier links are static snapshots and are intended for preliminary exploration/validation. Historical CIK–GVKEY–PERMNO mappings must be independently verified before publication.

## Storage
- Google Drive: canonical large output.
- GitHub: code, workflow, validation metadata, and small sample.
- The full CSV is kept out of Git history because of file size/provenance constraints.

Sources:
- https://www.openassetpricing.com/data/
- https://github.com/OpenSourceAP/CrossSection
- https://github.com/Wenzhi-Ding/Std_Security_Code
