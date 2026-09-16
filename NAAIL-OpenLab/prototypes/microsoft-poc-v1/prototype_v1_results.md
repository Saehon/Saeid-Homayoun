# Prototype V1 Results — Microsoft Golden Anchor

**Maturity:** `RESEARCH_PROTOTYPE`  
**Run date:** 2026-09-16  
**Production readiness:** NO  
**Independent replication:** NOT YET

## Executed validation
| Requirement | Result |
|---|---|
| SEC/XBRL ingestion | **PASS** — SEC interactive-XBRL R2/R4/R6/R107 facts ingested into the frozen V1 snapshot |
| Textual-analysis pipeline | **PASS, bounded** — two FY2026 filing samples transformed to numerical features; raw text withheld |
| Finance calculation | **PASS** — ratios, cash-flow measures, FY2026 price return, DGS10 |
| CAM/audit mapping | **PASS** — 2 FY2026 CAMs + ICFR opinion |
| Innovation measure | **PASS** — R&D intensity + GitHub metadata snapshot |
| ABC/TDABC/AI-cost | **PASS, synthetic** — internal-process microcase only |
| AI-model benchmark | **PASS, external benchmark** — LiveBench quality and cost-per-successful-task snapshot |
| Human–AI experiment design | **PASS DESIGN / NOT RUN** |
| Evidence Passport | **PASS** — schema + instantiated SEC XBRL passport |
| Human Gate | **PASS FOR RESEARCH-PROTOTYPE PUBLICATION ONLY** |

## Selected numerical results
- Revenue growth: **17.75%**
- Operating margin: **46.78%**
- Net margin: **40.31%**
- Current ratio: **1.230**
- Liabilities/assets: **41.67%**
- R&D intensity: **10.72%**
- FCF proxy: **$66,987m**
- FCF margin: **20.19%**
- FY2026 MSFT simple price return (IEX close-to-close, no dividends): **-24.22%**
- DGS10 at 2026-06-30: **4.44%**
- Illustrative DGS10 + mature-market ERP proxy: **8.64% (NOT Microsoft WACC)**

## Audit results
- Revenue Recognition CAM mapped to revenue assertions, contract/performance-obligation risk, procedures and high-judgment conclusion.
- Uncertain Tax Positions CAM mapped to tax-liability valuation/completeness/presentation, transfer-pricing risk, specialist procedures and high-judgment conclusion.
- FY2026 ICFR auditor opinion: **unqualified**.

## AI benchmark
LiveBench 2026-06-25 external snapshot includes overall score + cost per successful task. V1 does not infer professional task fitness from leaderboard rank alone.

## Unit-test execution
The upgraded reproducibility package passed **12/12 offline unit tests** on 2026-09-16. Tests cover the two-core constitution, frozen XBRL facts, segment reconciliation, finance calculations, real market-data status, CAM/ICFR mapping, bounded text outputs, innovation boundary, external benchmark labeling, TDABC arithmetic, experiment execution status and Human Gate boundary.

## Human Gate
**APPROVE_RESEARCH_PROTOTYPE_FOR_PUBLICATION_WITH_LIMITATIONS**

Not approved for production reliance, professional assurance, causal innovation conclusions, or scientific-validation claims.

## Remaining unexecuted gates
Fama–French regression; aggregate PatentsView metrics; full raw-filing text pipeline with redistributable intermediate artifacts; actual participant experiment; NAAIL-specific model pass-rate/cost-per-verified-professional-output; independent replication.
