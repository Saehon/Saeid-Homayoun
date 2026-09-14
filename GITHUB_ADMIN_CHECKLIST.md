# GitHub Admin Checklist for ECONOVA-S™

These settings require repository administration in the GitHub UI or an admin-capable API endpoint.

## About sidebar

**Description**

ECONOVA-S™ — governed scientific economic intelligence for AI, data economy, finance and sustainable welfare, integrating Co-Scientist-style reasoning, Computational Discovery, AlphaEvolve-inspired search, evidence RAG, econometrics, replication and scientific red-team validation.

**Topics**

- artificial-intelligence
- economics
- finance
- data-economy
- econometrics
- scientific-discovery
- multi-agent-systems
- rag
- causal-inference
- research-software
- sustainability
- replication
- llm
- gpt
- open-science

**Website**

Use the ECONOVA-S project page once GitHub Pages or a dedicated domain is enabled. Until then, leave the website field blank rather than pointing to an unrelated page.

## Repository settings

Recommended:
- keep `main` as the default branch;
- enable **Automatically delete head branches** after pull-request merge;
- prefer **Squash merging** for clean public history;
- enable **Allow auto-merge** only after required checks are configured;
- enable **Discussions** when you want a community Q&A channel;
- disable Wiki if documentation is maintained entirely in the repository;
- enable GitHub Pages from `/docs` when the project landing page is ready.

## Protect `main`

Current public branch should be protected with a ruleset or branch-protection rule requiring:
- pull request before merge;
- at least one approving review for external contributions;
- required status checks from ECONOVA-S test workflows;
- branch to be up to date before merge;
- conversation resolution before merge;
- no force pushes;
- no branch deletion;
- CODEOWNERS review for protected scientific/IP files where appropriate.

Consider requiring signed commits for release-critical changes. Existing historical commits do not need to be rewritten solely for presentation.

## Releases

Publish **v0.2.0 — Real Data + Evidence RAG** after final verification.

Use `RELEASE_NOTES_v0.2.0.md` as the release body, update `CITATION.cff` if needed, and create the release from a stable commit on `main`.

If Zenodo GitHub integration is enabled, verify the repository license metadata before publishing the release so the archived record does not silently receive an unintended license.

## Packages

Do not publish a GitHub Package merely to populate the Packages section. Add packaging only when ECONOVA-S has a stable installable Python package or container image with a defined support/version policy.

## Security

- Enable private vulnerability reporting when available.
- Keep secret scanning and dependency alerts enabled.
- Never store OpenAI/API credentials in repository files.
- Review Dependabot pull requests before merging because dependency changes can affect scientific reproducibility.

## Citation

Keep `CITATION.cff` synchronized with releases and add the Zenodo DOI once minted.

## Public/private boundary

Keep publication-safe architecture, reproducible demonstrations, metadata, tests and non-sensitive adapters public. Keep patent-sensitive, security-sensitive, proprietary orchestration, private benchmarks and commercial deployment logic outside the public repository until IP review is complete.
