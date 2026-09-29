# Architecture

## 1. System-of-record vs system-of-decision

The ERP remains the system of record.

DARWIN IFRS Integrated Value Brain™ acts as a governed **system of economic decision**:

```text
SAP / Oracle / Dynamics / ERPNext / other ERP
                  ↓
            Connector Mesh
                  ↓
      Economic Semantic Layer
                  ↓
           IFRS Value Brain
                  ↓
        Decision + Assurance
                  ↓
             Human Gate
                  ↓
              ERP Action
```

## 2. Layer model

| Layer | Engine | Purpose |
|---|---|---|
| 0 | ERP / Event Layer | Receive PO, SO, invoice, project, inventory, supplier, contract, lease, CapEx and M&A events |
| 1 | Economic Semantic Layer | Link transactions to supplier, product, project, customer, capacity, cash and capital |
| 2 | IFRS Accounting Brain™ | Identify applicable IFRS/IAS logic and accounting consequences |
| 3 | Internal Audit Assurance Brain™ | Test evidence, controls, data quality, assumptions, governance and model risk |
| 4 | Cost Truth Engine™ | Reconstruct decision-relevant cost |
| 5 | Management Accounting Decision Engine™ | Relevant cost, contribution, throughput, TCO, target cost, avoidable cost, opportunity cost |
| 6 | Economic Value Ledger™ | Record value created, preserved, destroyed or uncertain |
| 7L | Economic Value Hemisphere | EVI, EVA, capital charge, profitability, opportunity loss |
| 7R | Sustainability Value Hemisphere | materiality, ESG/ISSB, six-capital effects, sustainability value |
| 8 | Six-Capital Transformation Graph™ | Map value transmission across Financial, Manufactured, Intellectual, Human, Social/Relationship and Natural capital |
| 9 | Systems Thinking Engine™ | Dependencies, feedback loops, delays, constraints and trade-offs |
| 10 | Counterfactual & Scenario Engine™ | Compare do-nothing, approve, reprice, reschedule, replace, outsource, renegotiate and reject |
| 11 | DARWIN MetaBrain™ | Generate, challenge, optimize, falsify and select decision alternatives |
| 12 | Pre-Transaction Value Gate™ | Approve / Modify / Reprice / Renegotiate / Reschedule / Replace / Reject |
| 13 | Outcome & Learning Loop | Compare expected and actual value, attribute outcome and learn |

## 3. Construct Firewall

Every output must remain explicitly typed as one of:

- **VERIFIED_FACT**
- **ACCOUNTING_CONSTRUCT**
- **ESTIMATE**
- **PREDICTION**
- **CAUSAL_CLAIM**
- **RECOMMENDATION**
- **APPROVED_ACTION**
- **REALIZED_OUTCOME**

The system must not silently convert a prediction into a fact or a recommendation into an approved action.

## 4. Three-gate control model

### Gate A — Accounting / IFRS
Is the proposed treatment compliant with the applicable accounting requirements and evidence?

### Gate B — Assurance
Are the data, controls, assumptions, provenance and model outputs sufficiently reliable for the decision?

### Gate C — Integrated Value
Does the action create more integrated sustainable economic value than the best feasible alternative?

Only then does the case reach the Human Approval Gate.
