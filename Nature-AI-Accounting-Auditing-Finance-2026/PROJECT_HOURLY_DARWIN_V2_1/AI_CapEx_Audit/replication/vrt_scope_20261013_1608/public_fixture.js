// SEC Vertiv FY2025 manually transcribed fixture; not raw SEC extraction.
const v={cik:'0001674101',year:2025,sec_filed:'2026-02-13',
  management:'EFFECTIVE',auditor:'EFFECTIVE',
  excluded:['PurgeRite','Great Lakes'],assets_pct:2.7,sales_pct:0.6,
  cam_count:2,domain_controls:'UNKNOWN',ai_capex:null};
const tests=[v.cik==='0001674101',v.year===2025,
v.management==='EFFECTIVE',v.auditor==='EFFECTIVE',
v.excluded.length===2,v.assets_pct===2.7,v.sales_pct===0.6,
v.cam_count===2,v.domain_controls==='UNKNOWN',v.ai_capex===null];
if(!tests.every(Boolean))throw Error('fixture consistency failed');
console.log('PASS '+tests.length+'/'+tests.length+' fixture checks; causal NOT_RUN');
