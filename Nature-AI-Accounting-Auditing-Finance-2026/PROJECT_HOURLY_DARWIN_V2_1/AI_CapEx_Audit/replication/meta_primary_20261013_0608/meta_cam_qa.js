// Public SEC reference checks; input CSV remains in restricted Drive.
// Usage: node meta_cam_qa.js /path/to/authorized_local_pilot.csv
const fs=require('fs'), assert=require('assert');
const csv=fs.readFileSync(process.argv[2],'utf8').trim().split(/\r?\n/);
const cols=csv[0].split(',');
const rows=csv.slice(1).map(s=>Object.fromEntries(s.split(',').map((v,i)=>[cols[i],v])));
const m=rows.find(r=>r.ticker==='META');
const sec={camCount:3,ppe:69691,lease:2524,cfo:115800,fcf:43585,depBenefit:2920,netIncomeBenefit:2590};
let n=0;function check(cond,msg){assert.ok(cond,msg);n++}
check(rows.length===10,'10 pilot firm-years');
check(new Set(rows.map(r=>r.ticker)).size===10,'unique tickers');
check(rows.filter(r=>r.ticker==='META').length===1,'one META');
check(m.fiscal_year==='2025','year');
check(m.fiscal_year_end==='2025-12-31','fiscal end');
check(m.economic_role==='Builder','role');
check(Number(m.cam_topic_count)===2,'old count');
check(m.cam_topics_semicolon.split(';').length===2,'old topics');
check(sec.camCount-Number(m.cam_topic_count)===1,'one omitted CAM');
check(rows.reduce((a,r)=>a+Number(r.cam_topic_count),0)===13,'old topic total');
check(rows.reduce((a,r)=>a+Number(r.cam_topic_count),0)+1===14,'corrected topic total');
check(Number(m.gross_cash_capex_usd_m)===sec.ppe,'cash PP&E');
check(Number(m.operating_cash_flow_usd_m)===sec.cfo,'CFO');
check(Math.abs(Number(m.capex_to_cfo)-sec.ppe/sec.cfo)<1e-6,'ratio');
check(sec.cfo-sec.ppe-sec.lease===sec.fcf,'FCF reconciliation');
check(m.ai_capex_fy2025_usd_m==='' && sec.depBenefit!==sec.netIncomeBenefit,'AI unknown / accounting distinction');
console.log(JSON.stringify({tests_passed:n,tests_total:16,source:'authorized original pilot CSV',meta_cam_secondary:2,meta_cam_sec:3,old_total:13,corrected_total:14,cash_capex_cfo:sec.ppe/sec.cfo,lease_inclusive_capex_cfo:(sec.ppe+sec.lease)/sec.cfo,independent_source_byte_replication:'NOT_RUN'},null,2));
