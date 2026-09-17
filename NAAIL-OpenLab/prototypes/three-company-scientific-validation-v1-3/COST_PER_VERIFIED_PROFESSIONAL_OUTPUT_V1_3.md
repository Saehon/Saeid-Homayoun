# NAAIL Prototype V1.3 — Cost per Verified Professional Output™

**Status:** `RESEARCH_PROTOTYPE`  
**Numeric result:** `NOT_EXECUTED`

## Frozen measurement definition
For a run with model/API cost and human verification:

`CVPO = (AI/API cost + human verification cost + rework cost) / number of verified correct professional outputs`

where:

`human verification cost = reviewer_minutes / 60 × reviewer_hourly_cost`

A verified output must pass the frozen correctness rubric and required evidence-grounding threshold. Token cost alone is not a verified professional-output metric.

## V1.3 telemetry
`cost_per_verified_output_telemetry_template_v1_3.csv` captures model/version, task, tokens, price, latency, correctness, grounding, contradiction handling, reviewer time/cost, rework and final verification outcome.

No numeric CVPO is published until a genuinely blind model run and prospective human-verification telemetry exist.
