# Security, Licence & Data Rules

1. **Clone; do not silently vendor.** Keep upstream repositories separate so their licences, notices and history remain intact.
2. **Do not auto-run third-party code.** The bootstrap scripts only clone repositories.
3. **Inspect licences before redistribution.** A public GitHub repository is not automatically public-domain software.
4. **Data can have a different licence from code.** This is explicitly relevant for IBM AML-Data.
5. **Cloud runtime can cost money.** Microsoft Copilot Studio/Dynamics/Azure and IBM watsonx/Cloud examples may require accounts, subscriptions, or API credentials.
6. **Never commit secrets.** Store API keys/tokens only in GitHub Actions secrets, Codespaces secrets, environment variables, or approved secret managers.
7. **SEC EDGAR access must follow SEC fair-access guidance.** Use an identifying user-agent and rate-conscious retrieval.
8. **Use isolated environments.** Prefer venv/conda/container environments for research replication.
9. **Pin versions for papers.** Record commit SHA, package versions, data snapshot date, model version and prompts/configuration.
10. **Human review remains mandatory.** Open-source models and agents are research tools, not autonomous accounting/audit judgments.

## Research provenance fields to record

- upstream repository URL
- upstream commit SHA
- licence identifier
- retrieval date
- dataset source and licence
- model/provider/version
- environment lockfile
- experiment seed
- prompt/configuration hash
- output checksum
- reviewer/falsification result
- human approval
