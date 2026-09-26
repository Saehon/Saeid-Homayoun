# T0–T6 Experimental Design

## Treatments

| Treatment | Architecture |
|---|---|
| T0 | Human-only baseline |
| T1 | Single general-purpose foundation model |
| T2 | Single model + structured retrieval |
| T3 | Specialist agent + deterministic domain tools |
| T4 | Multi-agent specialist architecture |
| T5 | T4 + evidence lineage + deterministic verification + policy/control gate |
| T6 | T5 + cross-model challenge/replication + mandatory human approval for material/high-judgment conclusions |

## 30-case portfolio

### United States — 10 cases
Revenue recognition; goodwill impairment; acquisition accounting; tax valuation; inventory valuation; revenue ICFR; IT access/SoD; journal-entry anomalies; SEC/XBRL tie-out; CAM persistence/entry/exit.

### Europe — 10 cases
IFRS 15 revenue; IAS 36 impairment; IFRS 9 ECL; IFRS 16 leases; IFRS 3 acquisitions; IAS 37 provisions; ESEF validation; KAM persistence; ESRS climate evidence; double materiality.

### Asia — 10 cases
Hong Kong KAM extraction; Hong Kong valuation KAM; Hong Kong revenue KAM; Singapore ISSB/climate; Singapore GHG calculations; Singapore KAM; Japan sustainability; Japan impairment; Japan human capital; governance-risk-sustainability consistency.

## Metrics

### Accuracy
- classification accuracy/F1;
- numeric absolute/relative error;
- unsupported-claim rate;
- correct abstention/escalation.

### Evidence
- evidence precision/recall;
- citation correctness;
- provenance completeness;
- workpaper reproducibility.

### Controls
- unauthorized-action attempts;
- policy violations;
- correct human-gate triggers;
- reviewer override rate.

### Efficiency
- time;
- tool/model calls;
- token/inference cost;
- rework/human intervention.

### Human factors
- calibrated reliance;
- reviewer confidence;
- willingness to override;
- time to verify.

## Replication

Freeze and record:
- provider and model family/version;
- agent instructions;
- skill/tool versions;
- retrieval corpus;
- temperature/sampling parameters;
- deterministic scripts;
- case version;
- evaluator version.

Do not pool repeated model runs as statistically independent human observations.
