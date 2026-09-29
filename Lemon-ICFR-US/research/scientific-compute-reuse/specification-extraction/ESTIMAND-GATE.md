# Pilot-3 Estimand Gate — Decision Register

> **ACK2007 supersession notice (R-006/R-008/R-009 engineering repair):**
> This register is an estimand-structure record, not coefficient-verification evidence.
> Any earlier statement that the ACK2007 full coefficient vector/intercept/SE was
> "cross-checked" is superseded. The current coefficient contract is
> `PENDING_PRIMARY_TABLE / UNKNOWN_ORIGIN / regression_pin_only`.

| Model | Observed target | Structural layer | Specification status | Common flat M1 ensemble? |
|---|---|---|---|---|
| DGM2007 | disclosed MW | MW existence/disclosure mixture | structure record; coefficients pending | NO, pending alignment |
| ACK2007 | existence + discovery/reporting ICD | mixed exposure/discovery/reporting | SCIENTIFIC-HOLD; coefficient origin unverified | NO flat averaging |
| RW2012 | reporting existing MW | reporting conditional on underlying weakness | estimand record; coefficients pending | NO |

## Decision
The Pilot-3 papers do not currently inhabit one homogeneous prediction function space. Flat averaging is rejected.

Preferred conceptual structure:
P(MW*=1 | X)
P(Discovery=1 | MW*, X)
P(Reporting=1 | Discovery, MW*, X)

ACK2007 may proceed only through PDF-independent engineering/provenance work while the published JAE primary results table is unavailable. Its 14-predictor identity is known, but numerical coefficient/intercept origin remains unverified.

DGM2007 remains on its own primary-evidence gate.
RW2012 remains a reporting-stage model and requires exact primary regression extraction.

No M1 lock occurs here. Green CI is engineering evidence only.
