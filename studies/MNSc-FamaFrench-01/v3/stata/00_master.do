/**********************************************************************
 MNSc FIZ-CIZ V3 — Frozen one-command Stata replication
 Primary design: exact July-2024 FIZ-era vs July-2025 CIZ-era archives.
 No p-value-driven model selection. Damodaran layer = external validation only.

 Literature logic: Management Science / FT50-AJG4* standards emphasize
 factor-dimension discipline, multiple-testing control, robust inference,
 economic magnitude, and replication (He et al.; Chen; Feng-Giglio-Xiu;
 Giglio-Xiu-Zhang; Harvey et al.).
**********************************************************************/
version 18
clear all
set more off
capture log close

* Change only this root path if running outside the package.
global ROOT "."
global CLEAN "$ROOT/02_Data_Clean"
global OUT   "$ROOT/04_Output_5_Tables/Stata"
cap mkdir "$OUT"
log using "$OUT/master.log", replace text

*-----------------------------*
* Table 1: descriptive + DCS  *
*-----------------------------*
use "$CLEAN/fiz_ciz_monthly.dta", clear
local vars mktrf smb hml rmw cma rf sl sm sh bl bm bh
postfile T1 str12 series double old_mean new_mean old_sd new_sd mean_diff_bps dcs_bps max_abs_bps corr_old_new long N using "$OUT/table1_descriptive_dcs_stata.dta", replace
foreach v of local vars {
    quietly summarize old_`v'
    local om=r(mean)
    local os=r(sd)
    local N=r(N)
    quietly summarize new_`v'
    local nm=r(mean)
    local ns=r(sd)
    gen double __abs = abs(d_`v')
    quietly summarize d_`v'
    local md=10000*r(mean)
    quietly summarize __abs
    local dcs=10000*r(mean)
    local mx=10000*r(max)
    quietly correlate old_`v' new_`v'
    matrix C=r(C)
    local cc=C[1,2]
    post T1 ("`v'") (100*`om') (100*`nm') (100*`os') (100*`ns') (`md') (`dcs') (`mx') (`cc') (`N')
    drop __abs
}
postclose T1

*-----------------------------*
* Table 2: correlation matrix *
*-----------------------------*
pwcorr d_mktrf d_smb d_hml d_rmw d_cma d_rf d_sl d_sm d_sh d_bl d_bm d_bh, sig obs
matrix R=r(C)
putexcel set "$OUT/table2_revision_correlations_stata.xlsx", replace
putexcel A1=matrix(R), names

*----------------------------------------------*
* Table 3: CAPM / FF3 / FF5, HAC(Newey-West 6) *
*----------------------------------------------*
postfile T3 str5 model str3 portfolio str3 vintage double alpha_month alpha_annual t_alpha p_alpha adjr2 long N using "$OUT/table3_baseline_regressions_stata.dta", replace
foreach model in CAPM FF3 FF5 {
    if "`model'"=="CAPM" local xs mktrf
    if "`model'"=="FF3"  local xs mktrf smb hml
    if "`model'"=="FF5"  local xs mktrf smb hml rmw cma
    foreach p in sl sm sh bl bm bh {
        foreach tag in old new {
            gen double __y = `tag'_`p' - `tag'_rf
            local xvars
            foreach x of local xs {
                local xvars `xvars' `tag'_`x'
            }
            quietly newey __y `xvars', lag(6)
            local a=_b[_cons]
            local se=_se[_cons]
            local tt=`a'/`se'
            local pp=2*ttail(e(df_r),abs(`tt'))
            local r2=e(r2_a)
            local NN=e(N)
            post T3 ("`model'") ("`p'") ("`tag'") (`a') (12*`a') (`tt') (`pp') (`r2') (`NN')
            drop __y
        }
    }
}
postclose T3

*-------------------------------------------------------*
* Table 4: Damodaran external validation, robust errors *
*-------------------------------------------------------*
use "$CLEAN/damodaran_industry_2026.dta", clear
postfile T4 str3 model str20 term double coef se t p r2 adjr2 long N using "$OUT/table4_damodaran_external_validation_stata.dta", replace
local m1 beta
local m2 beta wacc
local m3 beta wacc netcapex_sales
local m4 beta wacc netcapex_sales ln_n_firms
forvalues j=1/4 {
    local xx ``m`j'''
    quietly regress jensen_alpha `xx', vce(robust)
    foreach term in _cons `xx' {
        local b=_b[`term']
        local s=_se[`term']
        local t=`b'/`s'
        local p=2*ttail(e(df_r),abs(`t'))
        post T4 ("M`j'") ("`term'") (`b') (`s') (`t') (`p') (e(r2)) (e(r2_a)) (e(N))
    }
}
postclose T4

*------------------------------------------------------*
* Table 5: robustness — HAC 3/6/12 + frozen subperiods *
*------------------------------------------------------*
use "$CLEAN/fiz_ciz_monthly.dta", clear
postfile T5 str18 panel str12 series str16 spec double estimate_bps se_bps t p long N using "$OUT/table5_robustness_stata.dta", replace
foreach L in 3 6 12 {
    foreach v of local vars {
        quietly newey d_`v', lag(`L')
        local b=_b[_cons]
        local s=_se[_cons]
        local t=`b'/`s'
        local p=2*ttail(e(df_r),abs(`t'))
        post T5 ("HAC_mean_revision") ("d_`v'") ("NW_lag_`L'") (10000*`b') (10000*`s') (`t') (`p') (e(N))
    }
}
foreach period in full post_1990 post_2000 post_gfc post_covid {
    preserve
    if "`period'"=="post_1990" keep if date_str>="1990-01-01"
    if "`period'"=="post_2000" keep if date_str>="2000-01-01"
    if "`period'"=="post_gfc"  keep if date_str>="2009-01-01"
    if "`period'"=="post_covid" keep if date_str>="2020-01-01"
    foreach v of local vars {
        gen double __abs=abs(d_`v')
        quietly summarize __abs
        post T5 ("subperiod_DCS") ("d_`v'") ("`period'") (10000*r(mean)) (.) (.) (.) (r(N))
        drop __abs
    }
    restore
}
postclose T5

log close
exit, clear
