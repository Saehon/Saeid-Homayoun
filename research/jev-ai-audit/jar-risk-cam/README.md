# Journal of Accounting Research — Risk–CAM publication package

**Principal investigator:** Dr. Saeid Homayoun  
**Date:** 2026-10-16  
**Status:** Pre-results manuscript and executable synthetic QA starter; not submission ready.

## Study
**Do Auditors Disclose the Risks That Matter? Ex Ante Accounting Risk, Critical Audit Matter Alignment, and Subsequent Reporting Quality**

The JAR manuscript, the publication plan, and original CAM datasets are authoritative in Google Drive. The GitHub repository is PUBLIC. **Do not commit private observations, human-coded confidential labels, tokens or copyrighted third-party data.** The unpublished DOCX stays on Google Drive; there is no public manuscript mirror.

## Canonical documents
- [Google Drive publication folder](https://drive.google.com/drive/folders/1rX5r3VIS5x4prq0hlFFNIrH6OTACyuvB)
- [Word manuscript (private Drive)](https://docs.google.com/document/d/1ARsLl2pDqf1wmtwo8GWO2vxr5UKMxegc/edit)
- [Replication starter ZIP (private Drive)](https://drive.google.com/file/d/1qGtbIOubT4X6NOxbybTI-F-whWIRETWX/view)
- [Publication plan / master source index](https://docs.google.com/document/d/1CT6pp2160s51kgY1k2vF31jCGaS_DM22hUvMnslLf18/edit)
- [Canonical CAM results and FT50 replication registry](https://docs.google.com/spreadsheets/d/1q7IFjPfUT5Wx1tDU3pz_VYHpa941yqCrKiDD3xlrB-Y/edit)

## Contents here
- `src/validate_panel.py`: fail-closed, chronological schema and outcome validity checks.
- `tests/test_contract.py`: six synthetic contract tests.
- `data/SYNTHETIC_demo.csv`: invented examples ONLY.
- `docs/PUBLICATION_PLAN_AND_SOURCE_INDEX.md`: mirror of the original research workplan, sourced from the Drive master on 2026-10-16.
- `JAR_Risk_CAM_Replication_Starter_2026-10-16.zip`: exact synthetic starter archive from Google Drive.
- Shared `../common_risk_engine.py`: eight *untrained* FT50-supported candidate features; *no fitted scores*.
- Shared `../benchmark.py`: descriptive evaluator, *not a Jev installation*.

## Reproduce
From this folder run:
```sh
python -m unittest discover -s tests -v
python src/validate_panel.py data/SYNTHETIC_demo.csv
```

## Integrity gates
- Previous diagnostic: 609 CAM topic rows / 44 firms / 87 firm-years, but just 11 temporally eligible risk rows from four firms in the narrow pilot. **Do not claim the 609 rows are ready for regressions.**
- No causal effect, positive hypothesis, FT50 empirical replication, fitted risk model, or Jev inference has yet been verified.
- Construct accounting risk only from variables available before the chosen CAM-disclosure cutoff; future outcomes must be subsequent.
- Select CAM topics and measure ICFR effects independently; absence of a CAM or disclosed weakness does not establish audit quality.
- JAR data-description requirements and potential preregistration applicability need a research governance review.

Third-party replication code is referenced via links and not copied without license review.
