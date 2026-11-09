"""AVGO FY2025 public-fact QA; assertions do not independently re-fetch SEC/PCAOB."""
from datetime import date
import json
r = dict(cik='0001730168', fy=2025, end='2025-11-02',
         accession='0001730168-25-000121', filed='2025-12-18',
         accepted='2025-12-18 16:04:47', sic='3674',
         management_icfr='EFFECTIVE', auditor_icfr='EFFECTIVE',
         auditor='PricewaterhouseCoopers LLP', cam='REVENUE_ASC606',
         cam_count=1, revenue_control_effectiveness='UNKNOWN',
         pcaob_report='104-2025-040', pcaob_dated='2025-02-26',
         pcaob_public='2025-03-31', deficient=10, inspected=64,
         ai_specific_capex=None, form_ap_verified=False)
checks = {
 'cik10': len(r['cik']) == 10 and r['cik'].isdigit(),
 'fy': r['fy'] == 2025,
 'accession': r['accession'].startswith(r['cik']),
 'fiscal_before_filing': date.fromisoformat(r['end']) < date.fromisoformat(r['filed']),
 'acceptance': r['accepted'][:10] == r['filed'],
 'sic': r['sic'] == '3674',
 'management_explicit': r['management_icfr'] == 'EFFECTIVE',
 'auditor_explicit': r['auditor_icfr'] == 'EFFECTIVE',
 'one_revenue_cam': r['cam_count'] == 1 and r['cam'] == 'REVENUE_ASC606',
 'domain_not_inferred': r['revenue_control_effectiveness'] == 'UNKNOWN',
 'pcaob_report_before_public': date.fromisoformat(r['pcaob_dated']) < date.fromisoformat(r['pcaob_public']),
 'pcaob_public_before_sec': date.fromisoformat(r['pcaob_public']) <= date.fromisoformat(r['filed']),
 'pcaob_rate': r['deficient'] / r['inspected'] == 0.15625,
 'ai_capex_unknown': r['ai_specific_capex'] is None,
 'form_ap_unknown': r['form_ap_verified'] is False,
}
assert all(checks.values()), {k:v for k,v in checks.items() if not v}
print(json.dumps(dict(tests_passed=sum(checks.values()), total=len(checks),
                      issuer_years=1, pcaob_asof_days=(date.fromisoformat(r['filed'])-date.fromisoformat(r['pcaob_public'])).days,
                      domain_effectiveness='UNKNOWN', regression='NOT_RUN'),sort_keys=True))
