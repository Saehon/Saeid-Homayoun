# Verified Anthropic upstream inventory — 2026-10-28

This document records verified repository existence and root LICENSE findings; it does **not** install or execute third-party code.

| Upstream | Root LICENSE result | State | Research use |
|---|---|---|---|
| [anthropics/financial-services](https://github.com/anthropics/financial-services) | Apache-2.0 | active | POMELO ICFR MACEI valuation |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | MIT | active | DARWIN JEV |
| [anthropics/skills](https://github.com/anthropics/skills) | review required | active | POMELO JEV |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Apache-2.0 | active | SME |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Apache-2.0 | active | agent workflows |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | review required | active | DARWIN development |
| [anthropics/courses](https://github.com/anthropics/courses) | CC-BY-NC-4.0 | archived | training only |
| [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) | MIT | active | CI pending credentials |
| [anthropics/claude-for-financial-advisors](https://github.com/anthropics/claude-for-financial-advisors) | Apache-2.0 | active | valuation |
| [anthropics/claude-code-playground](https://github.com/anthropics/claude-code-playground) | Apache-2.0 | active | experiments |

## Gates and exclusions
- `skills` and `claude-code`: root LICENSE unavailable; review repository-specific terms and per-skill licensing before reuse.
- `courses`: archived, CC BY-NC 4.0; no automatic commercial redistribution.
- No code imported, no secrets configured, no actions enabled, no runtime smoke tests performed.
- Pin exact upstream SHAs, perform SBOM/dependency scanning and license review, then import minimal code in separate PRs.
- Require reproducibility tests and a human review for financial/audit data access.
