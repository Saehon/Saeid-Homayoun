# Empirical evidence and machine-learning protocol

**Data intake:** Check permissions, source versions, variable names/types, unique identifiers, fiscal year vs filing/announcement date, missingness, duplicates, unit harmonization, restatements, look-ahead contamination and join loss. Always print/sample-check raw rows where allowed. Track attrition per stage.

**Reproducible analyses:** Prepare scripts for descriptive stats, variable dictionary, correlations, baseline estimates, standard errors clustered at justified level, FE, sensitivity, placebo/negative control, sample selection, outliers and alternative specifications. If data inadequate, provide executable code and mark results NOT TESTED.

**Causal studies:** Clarify estimand, treated/control definition, common trends when using DiD, event timing, staggered adoption issues, IV relevance/exclusion if relevant, mediation identification assumptions, and avoid treating adjustment alone as causal identification.

**Predictive studies:** Temporal split by information-availability date, grouped splits by issuer when necessary; no post-event features; nested tuning when appropriate; report class prevalence, PR-AUC vs baseline, calibration, Brier score, sensitivity/specificity and action-constrained recall; evaluate drift and uncertainty.

**ICFR:** Distinguish material weakness disclosure timing, SEC filing period, restatement discovery, future outcomes, and audit-fee or governance controls. For the SEFD/SEC/TimesFM track, isolate forecasting features available before the target event and document the observation window.

**CAM/KAM:** Preserve original auditor text, taxonomy, year, firm and account/topic. Map topics to applicable IFRS/US GAAP only after identifying reporting regime. CAM existence is an audit-reporting choice, not an exogenous intervention by default. For Risk–CAM Alignment, measure account risk independently of CAM assignment; assess selection into CAM and subsequent outcomes.

**Synthetic/digital twin:** Label outputs SIMULATED, document generator/parameter assumptions, and keep separate from real-data findings. Never present simulated p-values as empirical support.
