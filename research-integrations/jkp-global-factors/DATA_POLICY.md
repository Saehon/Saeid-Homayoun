# JKP research-data and secrets policy

- **Public GitHub:** scripts, tests with artificial inputs, schema templates, attributed methodological notes and nonrestricted result summaries only.
- **Private licensed-data store:** WRDS, CRSP, Compustat, IBES, vendor-specific derived stock panels; access governed by the institution's data licences.
- **JKP repository code:** MIT-licensed; if copied, preserve licence and attribution. Here it is **linked**, not copied.
- **JKP repository-distributed data:** CC BY-NC 4.0, with appropriate attribution and no implied endorsement; validate additional conditions for each data asset.
- **No secrets:** never commit WRDS credentials, .pgpass, tokens, cloud keys, .env files, or private evidence passports.
- **No dataset mirroring by default:** do not auto-publish JKP CSV/Parquet data to GitHub, Hugging Face, Kaggle or a public Drive folder.
- **Source freezing:** record upstream commit/tag, input file hash, retrieval date, institution data permission, dimensions, units, transformation pipeline and reproduction environment in a locally controlled evidence passport.
- **Research fairness:** publish negative and nonsignificant findings when sharing permitted summaries; do not advertise tests as PASS unless actually run.
- **Privacy:** avoid including identifiable confidential company/audit records, client details, or restricted research documents in public fixtures.

The bundled Python validator accepts an existing authorized local CSV or Parquet file. No network connections or WRDS authentication occur in its code. It does not itself verify dataset licences or perform substantive scientific estimation.
