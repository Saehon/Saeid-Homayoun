# Gemini CLI: scoped research integration policy

You are operating inside `integrations/google-colab-five-service/` of the user's GitHub repository `Saehon/Saeid-Homayoun`.

## Intent

Support the Google side of the GPT–GitHub–Google research workflow:
- Review/configure Google Cloud Shell + Gemini CLI readiness.
- Explain Python notebook integration with Google Drive and project `third-serenity-428705-g2`.
- Propose small, reviewable changes to code and documentation; coordinate via GitHub pull requests after human approval.
- Keep Google Drive as canonical research archive.

## Limits and human-in-the-loop

- Treat this as a **public source repository**: no private data, tokens, access keys, `.env` files, OAuth artifacts, or datasets in commits.
- No `git push`, merges, API activation, billing changes, model invocation costs, or cloud resource provisioning without user approval.
- Never assume access to a Colab runtime just because Cloud Shell is authenticated.
- Never claim Google Cloud, Colab or Gemini connections are **PASS** unless verified through actual execution.
- Do not modify unrelated project folders or override project-specific instructions to pause GitHub writes.
- Gemini CLI should prefer non-destructive inspection and minimal, reversible changes.
- Maintain reproducibility, human approval gates, source provenance and Drive readback checks.

See [Gemini CLI in Cloud Shell](CLOUD_SHELL_GEMINI_CLI.md) and [Architecture](ARCHITECTURE.md).