# Empirical Data and Five-Table Analysis

## Management Science–Oriented Fama–French and Damodaran Validation Module

**MNSc FIZ–CIZ FT50 Study — Replication-ready Stata and Python package**

**Author:** Saeid Homayoun  
**ORCID:** https://orcid.org/0000-0002-2536-0446

## 1. Data and empirical positioning

The empirical module uses two deliberately separate evidence streams. First, monthly Fama–French five-factor observations provide the asset-pricing time-series benchmark. Second, Damodaran industry cost-of-capital data provide an external cross-sectional construction/consistency check. The sources are not mechanically merged because they represent different units of analysis and economic objects.

The factor specification follows the five-factor architecture of Fama and French (2015), while statistical discipline is motivated by the multiple-testing concerns in Harvey, Liu, and Zhu (2016) and the high-dimensional factor-selection framework of Feng, Giglio, and Xiu (2020). Contemporary *Management Science* work further supports treating factor structure and state dependence as empirical objects rather than assuming a single immutable factor representation (Massacci, Sarno, and Trapani 2025).

## 2. Sample construction and inference

The frozen Fama–French GitHub sample contains 127 monthly observations from January 2010 through July 2020. The Damodaran module contains 45 industries from a frozen 2024 GitHub mirror. Descriptive statistics and Pearson correlations characterize the two modules. Cross-sectional WACC specifications use heteroskedasticity-robust HC3 standard errors. Robustness tests compare alternative covariance estimators, an alternative dependent variable, 5th/95th-percentile winsorization, and exclusion of finance-related industries.

**Interpretation safeguard.** The Damodaran WACC regressions must not be read as causal estimates: WACC is mechanically constructed from risk, capital-structure, and financing-cost inputs. Their role is therefore external validation of measurement coherence. The matched FIZ→CIZ archive comparison in the broader study remains the principal design for testing data-construction sensitivity.

## 3. Core empirical tables

1. Table 1 — Variable definitions, sources, and empirical roles
2. Table 2 — Descriptive statistics
3. Table 3 — Pairwise correlations
4. Table 4 — Baseline WACC regressions with HC3 inference
5. Table 5 — Robustness and alternative specifications

The machine-readable versions are stored under `Tables/`.

## 4. Main empirical reading

The monthly factor sample shows economically meaningful variation across market, size, value, profitability, and investment factors. In the industry validation sample, WACC is positively associated with beta and negatively associated with the debt weight. The full WACC model explains approximately 99% of cross-industry variation. This exceptionally high R² should be interpreted as evidence that the reproduced variables cohere with the WACC construction identity—not as evidence of a new causal mechanism.

The beta coefficient remains positive and statistically precise across conventional, HC1, and HC3 inference, the winsorized sample, and the sample excluding finance-related industries. Using cost of equity as an alternative dependent variable also retains a strong positive beta relation. These checks support data consistency and code reproducibility.

## 5. Reproducibility protocol

The repository contains frozen CSV inputs, a Stata do-file, a Python script, and CSV outputs for each of the five tables. The Stata workflow uses native commands for the main analysis and implements winsorization without requiring external packages. The Python workflow uses pandas and statsmodels. For final submission, GitHub-mirrored inputs should be refreshed against the authoritative Kenneth R. French Data Library and NYU Stern/Damodaran archive, with source hashes preserved.

The complete binary submission package, including Word and Excel artifacts, is maintained in the synchronized Google Drive study folder. GitHub stores the reproducible unpacked scientific content because the connector used for this update cannot reliably commit the full ZIP as one binary blob.

## 6. How to cite this study

> Homayoun, S. (2026). *MNSc FIZ–CIZ FT50 Five-Table Study: Fama–French and Damodaran empirical replication package* (Version 1.0) [Data set and computer software]. GitHub, Saehon/Saeid-Homayoun. https://github.com/Saehon/Saeid-Homayoun/tree/mnsc-fiz-ciz-ft50-5table-study-v1/studies/MNSc_FIZ_CIZ_FT50_5Table_Study. ORCID: https://orcid.org/0000-0002-2536-0446

## References

Fama, E. F., & French, K. R. (2015). A five-factor asset pricing model. *Journal of Financial Economics*, 116(1), 1–22. https://doi.org/10.1016/j.jfineco.2014.10.010

Feng, G., Giglio, S., & Xiu, D. (2020). Taming the Factor Zoo: A Test of New Factors. *Journal of Finance*, 75(3), 1327–1370. https://doi.org/10.1111/jofi.12883

Harvey, C. R., Liu, Y., & Zhu, H. (2016). … and the Cross-Section of Expected Returns. *Review of Financial Studies*, 29(1), 5–68. https://doi.org/10.1093/rfs/hhv059

Massacci, D., Sarno, L., & Trapani, L. (2025). Factor Models of Asset Returns and Bear Market Risk. *Management Science*. https://doi.org/10.1287/mnsc.2023.04276
