# NAAIL Journal Co-Scientist — Finance, Accounting & Audit Research

**Status: research-infrastructure proposal / review branch (10 October 2026).** This is a public, offline, standard-library-only research metadata harness. It has **not** completed a systematic review, meta-analysis, independent replication, real market-data test, or Microsoft-Decision-1 hosted-model evaluation. No empirical significance is claimed.

## Purpose

Connect the existing NAAIL Microsoft-Decision-1 ICFR pilot to a controlled three-stage FT50 and Academic Journal Guide (AJG) accounting, auditing, finance and economics research process:

1. **Systematic literature review and (only when suitable) meta-analysis** — dated, reproducible search; inclusion/exclusion decisions; independent full-text checks, effect-size extraction, risk of bias, null results.
2. **Replication screening and reproduction** — verify author/journal code, data licenses, execution environment, numerical results and discrepancies, with separate human approval.
3. **Digital-twin and prospective hypothesis testing** — synthetic feasibility first, then real public data only following provenance, rights, measurement, holdout and adjudication gates.

The research problem is the market pricing of **independently corroborated, pre-disclosure ICFR/accounting risk information**; a specialized decision model is a candidate measurement tool, *not* an auditor and not an established return-forecasting result.

## Related existing projects

- [Existing synthetic Decision-1 ICFR pilot — draft PR #152](https://github.com/Saehon/Saeid-Homayoun/pull/152), developed independently and not merged by this change.
- [Authoritative Google Drive project folder](https://drive.google.com/drive/folders/1Y6NqwdwjBlYCqkGObTb9UeRNqiZin6iZ).
- [Controlled Drive master index](https://docs.google.com/document/d/1zugMqqio6LW1nhPrDknmjIYkddqin6dH12xrVqG3t5A/edit).
- NAAIL assurance workflow and LEMON-ICFR are separate governed systems; POMELO proprietary code, blind labels, unreleased patent claims, or confidential manuscripts **must not be copied here**.
- Kaggle/Hugging Face project-specific mirrors: **not yet verified or published**. The account-level links are in the repository profile; do not confuse them with an existing project dataset.

## What the scaffold actually runs

```bash
python -m unittest discover -s NAAIL/research-assurance-mcp/journal-coscientist/tests -p 'test_*.py' -v
python NAAIL/research-assurance-mcp/journal-coscientist/src/journal_task.py \
  --phase systematic-review \
  --journal-tier ALL \
  --registry NAAIL/research-assurance-mcp/journal-coscientist/registry/candidates.csv \
  --output-dir /tmp/naail-journal-report
```

The bundled registry contains **only column headers**; running it produces an explicit **no records yet** report and an audit manifest, **not invented articles or verified search hits**. The program does not access Scholar, Microsoft, Crossref, OpenAlex, EDGAR, private files, or hosted LLM APIs. Future ingestion requires review and documented licensing.

The GitHub Actions workflow validates this scaffold on pull requests. On the default branch **after human-reviewed merge**, a Monday UTC schedule can generate a metadata-only report and upload short-lived Actions artifacts. Neither workflow automatically promotes papers, moves confidential data, spends money nor rewrites hypotheses.

## Gates

- A repository registration is not evidence of a completed systematic search or PRISMA review.
- An accessible code package is not a successful numerical replication.
- Pseudo-data reproduces software behavior, not licensed-data estimates.
- Synthetic simulations demonstrate feasibility only, not predictive validity or causal inference.
- No gold-label leakage into model-visible data, no autonomous approval, and no results asserted without independent checking.
- Journal-tier membership, article bibliographies, DOI/citation data and licenses require human verification at the point of use.

See [review protocol](protocols/SYSTEMATIC_REVIEW.md), [replication gate](protocols/REPLICATION_GATE.md), and [prospective hypotheses](config/hypotheses.yml).