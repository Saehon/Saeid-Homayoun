// Public-source classification fixture; NO restricted CSV or partner information.
const f = {issuer:"META", fiscal_year:2025, cam_secondary_count:2, cam_primary_titles:["Loss Contingencies","Uncertain Tax Positions","Consolidation accounting for a variable interest entity"], venture_ownership_pct:20, venture_total_estimated_development_usdm:27000, venture_max_loss_exposure_usdm:45950, equity_investment_carrying_usdm:1830, future_lease_start_year:2029, cash_ppe_capex_usdm:69691, icfr_firm:"EFFECTIVE", icfr_vie_domain:"UNKNOWN", ai_only_capex_usdm:null};
const c={
primary_cam_count: f.cam_primary_titles.length===3,
cam_delta: f.cam_primary_titles.length-f.cam_secondary_count===1,
unique_cam_titles: new Set(f.cam_primary_titles).size===3,
vie_title: f.cam_primary_titles[2].toLowerCase().includes("variable interest entity"),
venture_not_cash_capex: f.venture_total_estimated_development_usdm!==f.cash_ppe_capex_usdm,
exposure_not_cash_capex: f.venture_max_loss_exposure_usdm!==f.cash_ppe_capex_usdm,
equity_not_cash_capex: f.equity_investment_carrying_usdm!==f.cash_ppe_capex_usdm,
future_lease: f.future_lease_start_year>f.fiscal_year,
noncontrolling_interest: f.venture_ownership_pct<50,
firm_domain_firewall: f.icfr_firm==="EFFECTIVE"&&f.icfr_vie_domain==="UNKNOWN",
ai_capex_unverified: f.ai_only_capex_usdm===null,
no_additive_exposure: f.venture_max_loss_exposure_usdm!==f.venture_total_estimated_development_usdm+f.equity_investment_carrying_usdm
};
const failed=Object.entries(c).filter(([k,v])=>!v).map(([k])=>k);
if(failed.length) throw Error("FAILED: "+failed.join(","));
console.log(JSON.stringify({tests:Object.keys(c).length,passed:Object.keys(c).length,source_class:"PUBLIC_TRANSCRIBED_FIXTURE",original_sec_byte_reproduction:"NOT_RUN",did:"NOT_RUN"}));
