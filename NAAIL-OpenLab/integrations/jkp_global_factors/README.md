# JKP Global Factors → NAAIL Research Bridge

**Status:** Python adapter tested with synthetic observations; **no licensed WRDS dataset downloaded, installed or redistributed**, and no external JKP empirical replication claimed.

**Sources:** https://github.com/bkelly-lab/jkp-data · https://github.com/bkelly-lab/jkp-data/discussions · https://jkpfactors.com

Jensen, T. I., Kelly, B., & Pedersen, L. H. (2023). Is there a replication crisis in finance? *Journal of Finance, 78*(5), 2465–2518. https://doi.org/10.1111/jofi.13249

## Scope and integration

- **ECONOVA-S / Fama–French AI asset pricing:** estimate *retrospective* local-factor exposures using properly aligned excess returns and JKP factor series.
- **DARWIN:** pass an evidence passport, exclusions and failure records into the science/reviewer/falsification gates. Out-of-sample testing is a separate downstream research task.
- **POMELO / Evidence Passport:** preserve SHA-256 digests, data provenance, exact matching dates, units and the decision review gate. Do not write to or modify POMELO's stable Knowledge Core.
- **Damodaran AI valuation:** factor exposures can be candidate discount-rate sensitivity controls, **not** a directly calibrated cost of equity.
- **KIWI CAM/KAM risk / JEV:** factor outputs are context variables only. They **cannot** produce account-level CAM-risk scores or determine audit responses without independently validated accounting evidence.

## Safe inputs

Obtain JKP data through the original maintainers' site/WRDS under applicable terms. The original repository's **Python source is MIT**; its distributed data carry separate **CC BY-NC 4.0** terms, while underlying WRDS/CRSP/Compustat/IBES data remain under vendor licenses. This adapter never copies upstream data or credentials into GitHub. Do not expose WRDS credentials, raw proprietary extracts or identifiable records in public artifacts.

Convert legitimately obtained wide-format factor data to a local CSV with columns such as `date,MKT,SMB,HML`, and a local entity excess-return CSV `date,entity_id,excess_return`. Actual JKP files may use other schemas; **explicitly map and independently check** factor names, market definitions, factor portfolio breakpoints, frequencies, units and currency before conversion. `excess_return` must already subtract the appropriate risk-free rate; do not pass total returns as excess returns.

Run from the folder containing the code (Python 3.11+, standard library only):

```bash
python jkp_bridge.py \
  --factors /secure/jkp_factors_converted.csv \
  --returns /secure/entity_excess_returns.csv \
  --output-dir /secure/jkp_bridge_output \
  --factor-cols MKT,SMB,HML \
  --factor-unit percent --return-unit decimal \
  --source-version YOUR_VERIFIED_JKP_RELEASE --universe YOUR_MARKET \
  --license-confirmed
python -m unittest discover -s . -p 'test_*.py' -v
```

The adapter does *not* automatically download or install JKP's original build system. To use the upstream build pipeline independently, follow its README for `uv` and `jkp connect` with your **own licensed WRDS access**, in a secure compute environment. Upstream notes that full replication needs substantial HPC resources.

## Scientific gate / pseudocode

```text
P01 DEFINE research question, market universe, time frequency, rights, and benchmark.
P02 VERIFY JKP release/commit, source license, portfolio definitions and return units.
P03 VALIDATE unique factor dates and unique firm/date return keys.
P04 MATCH on exact contemporaneous dates without forward fill or guessing currency.
P05 ESTIMATE retrospective factor exposures; log exclusions and insufficient histories.
P06 RECORD each input hash, transformations, sample window and software version.
P07 SEND outputs to DARWIN critic/falsifier with null results and alternative specifications.
P08 HOLD JEV/CAM decisions until independent accounting risk evidence and human approval.
P09 REQUIRE out-of-time/market falsification before a publication or forecast claim.
```

**Evidence artifacts:** `factor_exposures.json` and `evidence_passport.json`; default evaluation state remains `UNVERIFIED_RESEARCH_OUTPUT` (or `SIMULATED` for synthetic fixture). All fitted coefficients are decimal-per-period and require independent period normalization and diagnostics. A run finishing without error does not establish causal identification, predictive performance, journal acceptance, or scientific validation.

**Risk and systems view:** data update/coverage is the input flow; the backlog of records awaiting licenses and independent mapping checks is the validation stock; release lag and WRDS MFA are bottlenecks. Errors in factor units or forward-filled dates are feedback signals. Overspecification and survivorship create unintended risks. Maintain a frozen holdout, log all models (including insignificant results), and prevent tuning on it.

**Release policy:** the design and synthetic tests may be public; private empirical estimates and licensed source files must stay in authorized restricted storage. GitHub holds code and source links, Google Drive may hold permitted controlled analysis, Hugging Face/Kaggle only redistribution-cleared demonstrations. No cross-platform sync is implied.