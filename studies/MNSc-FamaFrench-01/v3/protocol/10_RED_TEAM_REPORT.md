# 10 — Scientific Red-Team Report

## Status

**PRE-RUN ATTACK PLAN — adversarial-review gate remains false.**

## Blocking attacks to test

1. **Attribution confounding** — archive differences may combine FIZ→CIZ with ordinary revisions. Mitigation: Attribution Firewall; causal language blocked.
2. **Calendar mismatch** — old/new factors and portfolios may not use an identical monthly intersection. Mitigation: explicit common-sample intersection and sample reporting.
3. **Parser drift** — historical archive layout changes could create artificial differences. Mitigation: same-archive self-comparison and parser tests.
4. **Scale/unit error** — percent vs decimal conversion could inflate DCS/alfa. Mitigation: range checks and explicit Variable DNA units.
5. **Look-ahead / chronology** — later vintage is intentionally used for a measurement-stability comparison, not as information available historically. Manuscript must not reinterpret it as real-time predictability.
6. **Multiple testing** — many series/models can generate chance reversals. Mitigation: frozen families + BH FDR.
7. **Specification shopping** — HAC lag/model/subperiod cannot be selected after results. Mitigation: primary HAC(6), fixed CAPM/FF3/FF5, fixed robustness lags/subperiods.
8. **Weak-factor / test-asset sensitivity** — apparent structure changes may depend on test assets. Mitigation: planned additional portfolio families and reduced-rank robustness.
9. **Economic-vs-statistical importance** — tiny but significant revisions may not matter. Mitigation: DCS and alpha-change magnitudes in bps.
10. **Damodaran overclaiming** — industry regressions do not validate FIZ→CIZ. Mitigation: classify as complementary benchmark only.
11. **Non-independent AI review** — multiple roles using the same context/model can share blind spots. Mitigation: independent code path, isolated review context, and human gate.
12. **Survivorship of successful hypotheses** — failed/null hypotheses must remain in the record. Mitigation: frozen tournament and rejected/null preservation.

## Gate rule

`adversarial_review = true` only after the actual empirical outputs have been attacked and all blocking findings are either resolved or explicitly carried into the interpretation.

`discovery_claim_allowed = false`
