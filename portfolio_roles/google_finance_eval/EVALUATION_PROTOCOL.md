# Evaluation contract — google_finance_eval

## Current proof level

Ten **synthetic specification-based test cases** (8 blocked, 2 ready) test a deterministic rule-gate against the deliberately weak *always ready* baseline. Gold labels are written from the same functional contract as the candidate gate. Perfect accuracy here indicates internal consistency only: it **does not measure real-world accuracy, model quality, hiring success, compliance, professional assurance, or independent validation**.

## Reproduce

```bash
python -m unittest discover -s portfolio_roles/google_finance_eval/tests -v
python -m portfolio_roles.google_finance_eval.benchmark --out reports/google_finance_eval.json
```

Reports contain a canonical SHA-256 of fixtures, per-case decisions/error taxonomy, a confusion matrix, class-specific precision, recall, F1, and Wilson interval. This interval is descriptive only because synthetic cases are neither random nor independently labelled.

## Validation gates

1. Independently label held-out cases with a reviewer blind to candidate output.
2. Document data license, provenance, effective dates, version hashes and sample selection.
3. Check leakage, duplicates, missingness, risk thresholds, independent adversarial attacks and abstentions.
4. Test at least two real models or systems using the same held-out cases; preserve model/version/prompt/cost information.
5. Add subgroup/sector breakdown, 95% uncertainty and the limitations; seek independent review and sign-off.

No licensed data, private model keys, unpublished POMELO methods or third-party source code is distributed in this extension.
