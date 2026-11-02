function auditICFRcsv(csv) {
 const lines=csv.trim().split(/\r?\n/), head=lines[0].split(",");
 const rows=lines.slice(1).filter(Boolean).map(line=>Object.fromEntries(line.split(",").map((v,i)=>[head[i],v])));
 const required=["ticker","fiscal_year","economic_role","icfr_auditor_opinion","disclosed_material_weakness_2025","cam_topic_count","cam_topics_semicolon","ai_capex_fy2025_usd_m","pcaob_publication_date","auditor_report_date"];
 let tests=0; function ok(cond,msg){if(!cond)throw Error("FAIL "+msg);tests++}
 ok(rows.length===10,"ten pilot firm-years");
 ok(new Set(rows.map(x=>x.ticker+"-"+x.fiscal_year)).size===rows.length,"unique firm-year");
 ok(required.every(k=>head.includes(k)),"required fields");
 ok(rows.every(x=>x.fiscal_year==="2025"),"one fiscal year");
 ok(rows.every(x=>x.icfr_auditor_opinion==="effective_unqualified"),"secondary ICFR opinion claims");
 ok(rows.every(x=>x.disclosed_material_weakness_2025==="0"),"zero disclosed MW flags");
 ok(rows.every(x=>x.ai_capex_fy2025_usd_m===""),"AI-specific capex unobserved");
 ok(rows.every(x=>!head.includes("sic")&&!head.includes("naics")),"SIC/NAICS absent");
 ok(rows.every(x=>x.cam_topics_semicolon.split(";").length===Number(x.cam_topic_count)),"CAM counts reconcile");
 const map={revenue_recognition:"revenue",software_and_support_revenue:"revenue",inventory_and_purchase_commitments:"inventory",inventory_and_supplier_liabilities:"inventory",uncertain_tax_positions:"tax",loss_contingencies:"contingencies",acquired_intangible_valuation:"valuation",chips_act_incentives:"government_incentives"};
 const domains={};let unknown=0;const byRole={};
 for(const r of rows){const role=r.economic_role;byRole[role]??={firms:0,cam_topics:0};byRole[role].firms++;
 for(const topic of r.cam_topics_semicolon.split(";")){const d=map[topic];if(!d){unknown++;continue}domains[d]=(domains[d]||0)+1;byRole[role].cam_topics++}}
 ok(unknown===0,"all CAM topics mapped");
 ok(Object.values(domains).reduce((a,b)=>a+b,0)===13,"13 CAM topics");
 ok(byRole.Builder.firms===5&&byRole.Supplier.firms===5,"5/5 economic roles");
 ok(rows.filter(r=>r.pcaob_publication_date<=r.auditor_report_date).length===9,"nine publication-before-auditor-date flags");
 ok(rows.filter(r=>r.pcaob_publication_date>r.auditor_report_date).length===1,"one future PCAOB report");
 ok(domains.revenue===2&&domains.inventory===2&&domains.tax===5,"key domain counts");
 ok(!head.includes("sec_10k_filing_date"),"SEC filing date absent");
 return {source_rows:rows.length,firm_years:rows.length,distinct_firms:new Set(rows.map(r=>r.ticker)).size,fiscal_years:[...new Set(rows.map(r=>r.fiscal_year))],reported_effective_secondary:rows.length,reported_ineffective_secondary:0,primary_10k_opinion_reverified_this_run:0,icfr_domain_effectiveness_verified:0,disclosed_mw_flags:0,ai_specific_capex_observed:0,sic_naics_available:0,economic_role:byRole,cam_topic_mentions:domains,cam_topic_total:13,pcaob_publication_before_or_on_auditor_report:9,pcaob_publication_after_auditor_report:1,tests_passed:tests,tests_failed:0};
}
if(typeof module!=="undefined"&&module.exports)module.exports={auditICFRcsv};
if(typeof require!=="undefined"&&require.main===module){const fs=require("fs");const result=auditICFRcsv(fs.readFileSync(process.argv[2],"utf8"));process.stdout.write(JSON.stringify(result,null,2)+"\n");}