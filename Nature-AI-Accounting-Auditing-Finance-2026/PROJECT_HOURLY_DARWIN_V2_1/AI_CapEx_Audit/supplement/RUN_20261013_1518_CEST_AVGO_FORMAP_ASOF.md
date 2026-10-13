# AI_CAPEX_20261013_1518_CEST_AVGO_FORMAP — Form AP as-of firewall (PARTIAL)

Timestamp: 2026-10-13 15:18 CEST (Europe/Stockholm). Single independent scientific substep: verify public Form AP 146520 contents for Broadcom FY2025, without imputing its missing filing timestamp. Prior 14:13 META-VIE fixture retained; not rerun.

Official PCAOB source: https://pcaobus.org/api/auditorsearch/downloadfiling?ID=146520&filename=Broadcom+Inc_Jan+06+2026.pdf . Official data dictionary: https://assets.pcaobus.org/pcaob-dev/docs/default-source/rusdocuments/auditorsearch-form-ap-data-references.pdf . SEC FY2025 filing: https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm .

Source-transcribed findings: one Form AP (ID 146520) names issuer CIK 1730168, PwC auditor, audit report 2025-12-18, fiscal period end 2025-11-02, one named engagement partner (not disclosed in this report), one Singapore participating firm with 5%-<10% audit hours, one additional participant under 5% (aggregate under 5%). Form AP was signed 2026-01-05, 18 calendar days after SEC 2025-12-18 filing. Filename references Jan 06 but is NOT proof of actual filed date/time. Official dictionary specifies CSV column 62 BJ for filing timestamp, column 55 BC for signature, column 24 X for report date; date/time Eastern. Filing timestamp remains UNKNOWN because bulk row ID 146520 was not obtained.

Scientific inference: Form AP participant identities and hour shares were NOT public in this Form AP at the SEC filing cutoff, because signature postdates it. No claim about an earlier independent disclosure. Never backfill this Form AP into a 2025-12-18 information set. Participating audit firm hours are not a client-level inspection finding, ICFR material weakness, or AI-specific CapEx. This is a descriptive provenance gate, not a causal estimate.

Actual original restricted Drive CSV read in memory only: 10 firm-year rows, 31 columns, exactly 1 AVGO FY2025 row. 17/17 deterministic in-memory checks passed, including four sample-structure checks; public fixture code contains 13 checks and is NOT a raw PDF extraction. No private CSV uploaded. No DiD/regression. Nature35 method NOT_USED. Rival explanation: audit-hour participation may reflect global operations, not audit risk or quality; no test possible with one filing.

Blocked source: AuditorSearch daily bulk ZIP could not be retrieved twice (download failure and container DNS failure); dependent exact filing timestamp QUARANTINED in OPEN REPAIR QUEUE, not guessed. Five living artifacts preserved: manuscript, original sample, empirical results, variables/methods, replication code. Eight-gate study status PARTIAL; no independent replication or human review.

Next independent eligible step: retrieve official AuditorSearch bulk CSV row 146520 and verify BJ filing timestamp, or select another unvalidated issuer-year while repair is blocked. No merge or submission.
