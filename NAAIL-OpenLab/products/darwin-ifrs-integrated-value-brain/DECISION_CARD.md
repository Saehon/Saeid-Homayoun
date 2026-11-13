# DARWIN Decision Card™

Every material recommendation must be rendered as a compact, auditable decision card.

## Required fields

| Field | Meaning |
|---|---|
| Event ID | ERP / source-system event identifier |
| Event type | PO, SO, contract, lease, CapEx, etc. |
| IFRS route | Applicable standard family / rule domain |
| Accounting status | PASS / REVIEW / FAIL |
| Assurance status | ASSURED / CONDITIONAL / UNRESOLVED |
| True economic cost | Decision-relevant economic cost |
| EVI / EVA | Economic value impact |
| SVA | Sustainability value impact, where relevant |
| Opportunity cost | Value of the best displaced alternative |
| Integrated Decision Value | Combined governed value estimate |
| Best alternative | Highest-ranked feasible alternative |
| Recommendation | Controlled action vocabulary |
| Confidence | Calibrated confidence / uncertainty |
| Evidence gaps | Missing or contradictory evidence |
| Human gate | Required approver / review tier |
| Expected outcome | Forecast after approved action |
| Actual outcome | Filled after realization |
| Attribution | Decision effect vs external effects |

## Example

```yaml
event_id: PO-4517
event_type: purchase_order
accounting_status: PASS
assurance_status: CONDITIONAL
true_economic_cost: 8200000
currency: SEK
evi: 900000
sva: -400000
opportunity_cost: 800000
integrated_decision_value: -300000
best_alternative: PRODUCT_REDESIGN
best_alternative_expected_value: 1200000
recommendation: MODIFY
human_gate: CFO_AND_PROCUREMENT
```
