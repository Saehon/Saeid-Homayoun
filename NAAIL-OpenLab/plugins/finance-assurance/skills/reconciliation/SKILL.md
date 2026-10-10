---
name: reconciliation
description: Reconcile bank and general ledger balances; isolate timing differences and missing evidence.
argument-hint: "<account, period, or case>"
---

# Reconciliation

**Scope:** Research/education prototype; independent professional review mandatory.

Compare adjusted bank = bank + deposits in transit - outstanding checks to adjusted GL = GL + unrecorded credits - unrecorded debits. Investigate reconciling items and age rather than silently clearing. Use python src/naail_finance.py reconciliation examples/reconciliation.json. Do not treat zero arithmetic difference as verified evidence.

## Evidence Passport and human gate
Capture source IDs, period, data rights, model/tool version when used, exceptions, result hash and reviewer status. Do not equate model output with primary evidence. No external mutations or final financial, audit, regulatory, or publication decisions.
