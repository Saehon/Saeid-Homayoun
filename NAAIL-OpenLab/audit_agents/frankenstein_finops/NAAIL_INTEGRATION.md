# NAAIL Integration Contract

## Classification

- Umbrella: **NAAIL OpenLab**
- Home: **Audit Agent Lab**
- Type: **specialist programme**
- Permanent core: **No**
- Technology implementation: **replaceable**
- Human Gate: **required**
- Public status: **research prototype**

## Evidence contract

Each deterministic finding carries a stable finding ID, rule ID, severity, affected transaction IDs, row-level evidence, rationale, risk-domain routing and control objectives. Each run carries source-file provenance including a SHA-256 hash.

AI specialist outputs may interpret validated finding IDs but cannot create new deterministic evidence. Unsupported finding references are removed by the governance layer.

## State semantics

Under NAAIL portfolio governance:

- **IMPLEMENTED** — code/infrastructure exists.
- **EXECUTED** — a preserved real run artifact exists.
- **VALIDATED** — predefined evaluation has passed.
- **EMPIRICAL_RESULT** — inputs, model/provider/version metadata, outputs, evaluation, provenance and required human review are preserved.

This module should not be described as validated or as an empirical result merely because CI passes.

## Extension contract

Future GL, AP, AR, payroll, treasury, tax, revenue, budget/forecast, ERP-workflow, IAM and continuous-monitoring adapters must preserve the same evidence, provenance, falsification and Human Gate rules.
