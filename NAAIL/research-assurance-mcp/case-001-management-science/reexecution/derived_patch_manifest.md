# Case 001 — Derived Reproduction Patch Manifest

Original author artifacts remain immutable. Apply these changes only to a **derived reproduction copy**.

## R001 — WRDS filing extract filename
**File:** `1_code/a_1_generate_filing_dataset.ipynb`, cell 10

Original:
```python
wrds_file = Path.cwd() / '0_data' / 'external' / 'wrds_all_10qk_filings_08132021.xlsx'
```

README/placeholder:
```text
wrds_all_10qk_filings_07022022.xlsx
```

Derived patch:
```python
wrds_file = Path.cwd() / '0_data' / 'external' / 'wrds_all_10qk_filings_07022022.xlsx'
```

## R002 — clean-run cache check
**File:** `1_code/a_1_generate_filing_dataset.ipynb`, cell 11

Original:
```python
if not speed_bypass_loc.exists:
```

Derived patch:
```python
if not speed_bypass_loc.exists():
```

Reason: the uncalled bound method is truthy, so the clean-run branch is skipped and the code attempts to read a cache that does not exist.

## R003 — current-environment PyYAML compatibility
**File:** `1_code/preamble.py`

Original:
```python
CONFIG = yaml.load(f)
```

Possible derived compatibility patch:
```python
CONFIG = yaml.safe_load(f)
```

This is an environment/version compatibility patch, not yet classified as an original-environment defect.

## Governance
Never overwrite the authors' source package. Every re-execution must log the patch set, exact environment, source-data versions, and regenerated output hashes.
