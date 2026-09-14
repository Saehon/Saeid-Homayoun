# MNSc FIZ–CIZ FT50 Five-Table Study

## Purpose
This folder supplies a compact empirical data section for a Management Science-oriented manuscript. It combines a Fama–French factor-data module with a Damodaran industry-level external-validation module.

## Author and citation

**Author:** Saeid Homayoun  
**ORCID:** https://orcid.org/0000-0002-2536-0446

### Recommended citation

> Homayoun, S. (2026). *MNSc FIZ–CIZ FT50 Five-Table Study: Fama–French and Damodaran empirical replication package* (Version 1.0) [Data set and computer software]. GitHub, Saehon/Saeid-Homayoun. https://github.com/Saehon/Saeid-Homayoun/tree/mnsc-fiz-ciz-ft50-5table-study-v1/studies/MNSc_FIZ_CIZ_FT50_5Table_Study. ORCID: https://orcid.org/0000-0002-2536-0446

### BibTeX

```bibtex
@misc{homayoun2026mnsc_fiz_ciz,
  author       = {Homayoun, Saeid},
  title        = {MNSc FIZ--CIZ FT50 Five-Table Study: Fama--French and Damodaran Empirical Replication Package},
  year         = {2026},
  version      = {1.0},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/Saehon/Saeid-Homayoun/tree/mnsc-fiz-ciz-ft50-5table-study-v1/studies/MNSc_FIZ_CIZ_FT50_5Table_Study}},
  note         = {ORCID: 0000-0002-2536-0446}
}
```

## Five manuscript tables
1. **Table 1 — Variable definitions and provenance**
2. **Table 2 — Descriptive statistics**
3. **Table 3 — Pairwise correlations**
4. **Table 4 — Baseline multivariate regressions**
5. **Table 5 — Robustness and alternative specifications**

## Data
- `Data/fama_french_ff5_github_2010_2020.csv`: frozen GitHub mirror sample, 127 monthly observations, 2010-01 through 2020-07.
- `Data/damodaran_wacc_github_2024_subset.csv`: frozen 45-industry subset from a GitHub mirror of Damodaran/NYU Stern industry cost-of-capital data.
- `Data/SOURCE_PROVENANCE.txt`: source URLs and provenance notes.

## Reproduction
### Python
```bash
pip install pandas numpy statsmodels
cd Code
python reproduce_5_tables.py
```

### Stata
Open Stata in the `Code` directory and run:
```stata
do management_science_5table.do
```

## Scientific interpretation
The Damodaran WACC regressions are **external construction/consistency validation**, not causal tests. WACC is mechanically constructed from beta/risk, debt/equity weights, and financing costs, so very high explanatory power is expected. The paper's principal scientific identification remains the matched FIZ→CIZ archive comparison in the broader V2 package.

## FT50/AJG-4*/4 methodological anchors
- Fama, E. F., & French, K. R. (2015). A five-factor asset pricing model. *Journal of Financial Economics*, 116(1), 1–22.
- Harvey, C. R., Liu, Y., & Zhu, H. (2016). … and the Cross-Section of Expected Returns. *Review of Financial Studies*, 29(1), 5–68.
- Feng, G., Giglio, S., & Xiu, D. (2020). Taming the Factor Zoo: A Test of New Factors. *Journal of Finance*, 75(3), 1327–1370.
- Massacci, D., Sarno, L., & Trapani, L. (2025). Factor Models of Asset Returns and Bear Market Risk. *Management Science*.

## Submission safeguard
Before final submission, refresh GitHub-mirrored inputs against the authoritative Kenneth R. French Data Library and NYU Stern/Damodaran archive, preserve hashes, and rerun all code.
