version 18.0
clear all
set more off
capture log close

*============================================================*
* MNSc FIZ-CIZ FT50 5-Table Study
* Management Science / FT50-style empirical data section
* Sources: GitHub mirrors of Fama-French FF5 and Damodaran WACC
*============================================================*

global ROOT ".."
global DATA "$ROOT/Data"
global TABLES "$ROOT/Tables"

log using "$TABLES/Stata_replication.log", replace text

*-----------------------------*
* TABLE 2A & TABLE 3A:
* Fama-French descriptive statistics and correlations
*-----------------------------*
import delimited using "$DATA/fama_french_ff5_github_2010_2020.csv", clear varnames(1)
rename Mkt_RF mkt_rf
rename SMB smb
rename HML hml
rename RMW rmw
rename CMA cma
rename RF rf

destring date mkt_rf smb hml rmw cma rf, replace force
gen year = floor(date/100)
gen month = mod(date,100)

summarize mkt_rf smb hml rmw cma rf, detail
pwcorr mkt_rf smb hml rmw cma, sig obs

* Mean factor-return inference using Newey-West HAC.
foreach y in mkt_rf smb hml rmw cma {
    newey `y', lag(6)
}

*-----------------------------*
* TABLE 2B & TABLE 3B:
* Damodaran industry descriptives and correlations
*-----------------------------*
import delimited using "$DATA/damodaran_wacc_github_2024_subset.csv", clear varnames(1)

rename Number_Firms number_firms
rename Beta beta
rename Cost_Equity cost_equity
rename E_weight e_weight
rename Stock_SD stock_sd
rename Cost_Debt cost_debt
rename Tax_Rate tax_rate
rename AfterTax_Cost_Debt aftertax_cost_debt
rename D_weight d_weight
rename WACC wacc

summarize wacc beta d_weight stock_sd aftertax_cost_debt, detail
pwcorr wacc beta d_weight stock_sd aftertax_cost_debt, sig obs

*-----------------------------*
* TABLE 4:
* Baseline regressions
* Heteroskedasticity-robust inference
*-----------------------------*
regress wacc beta, vce(robust)
estimates store M1

regress wacc beta d_weight, vce(robust)
estimates store M2

regress wacc beta d_weight stock_sd, vce(robust)
estimates store M3

regress wacc beta d_weight stock_sd aftertax_cost_debt, vce(robust)
estimates store M4

* Optional HC3 in Stata 18+; robust is a portable fallback.
capture noisily regress wacc beta d_weight stock_sd aftertax_cost_debt, vce(hc3)
if _rc != 0 {
    regress wacc beta d_weight stock_sd aftertax_cost_debt, vce(robust)
}

*-----------------------------*
* TABLE 5:
* Robustness tests
*-----------------------------*

* A. Conventional versus robust inference
regress wacc beta d_weight stock_sd aftertax_cost_debt
estimates store R_OLS
regress wacc beta d_weight stock_sd aftertax_cost_debt, vce(robust)
estimates store R_ROB

* B. Alternative dependent variable
regress cost_equity beta d_weight stock_sd, vce(robust)
estimates store R_ALT

* C. 5/95 winsorization without external packages
foreach v in wacc beta d_weight stock_sd aftertax_cost_debt {
    quietly summarize `v', detail
    local p5 = r(p5)
    local p95 = r(p95)
    gen `v'_w = `v'
    replace `v'_w = `p5' if `v'_w < `p5'
    replace `v'_w = `p95' if `v'_w > `p95'
}
regress wacc_w beta_w d_weight_w stock_sd_w aftertax_cost_debt_w, vce(robust)
estimates store R_WIN

* D. Exclude finance-related industries
preserve
gen industry_l = lower(industry)
drop if regexm(industry_l,"bank|financial|insurance|investment")
regress wacc beta d_weight stock_sd aftertax_cost_debt, vce(robust)
estimates store R_NOFIN
restore

*-----------------------------*
* Scientific interpretation safeguard
*-----------------------------*
display as text "NOTE: Damodaran WACC regressions are external construction/consistency validation."
display as text "They are NOT causal because WACC is mechanically constructed from risk, capital structure,"
display as text "and financing-cost inputs. The matched FIZ-CIZ archive comparison remains the study's core design."

estimates dir
log close
