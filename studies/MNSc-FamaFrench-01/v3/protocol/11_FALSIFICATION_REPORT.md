# 11 — Falsification Plan

## Status

**PENDING — falsification gate is not passed.**

## Pre-specified falsification and stress tests

1. **Same-archive identity test** — comparing an archive with itself must yield zero DCS and zero conclusion reversals up to numerical tolerance.
2. **FIZ-era placebo pair** — compare adjacent official annual archive vintages that both precede CIZ (candidate: July 2023→July 2024) to estimate ordinary revision sensitivity.
3. **CIZ-era placebo pair** — compare adjacent official annual archive vintages after CIZ where comparable data are available (candidate: July 2025→July 2026) to estimate ordinary post-transition revision sensitivity.
4. **HAC sensitivity** — primary HAC(6) compared with frozen lags 3 and 12.
5. **Multiplicity control** — BH FDR for the pre-specified family of mean-revision tests.
6. **Subperiod stability** — full, post-1990, post-2000, post-GFC 2009, post-COVID 2020.
7. **Alternative test assets** — replicate on additional official Fama–French portfolio families.
8. **Model-family stability** — compare CAPM, FF3, FF5 without selecting a model based on desired results.
9. **Scale/parser checks** — compare raw archive observations at sampled dates against parsed values and enforce plausible return ranges.
10. **Latent-structure falsification** — any factor-dimension result must beat/simple-baseline checks and remain stable under reasonable sample/test-asset changes.

## Decision rule

A falsification failure does not get deleted. It becomes part of the Evidence Passport and can block or narrow the scientific claim.

`falsification = false` until these tests are executed and reviewed.
