# NAAIL Product UX Architecture — v0.1 (1 November 2026)

## Product positioning

**Audience:** auditors, accounting scholars, research collaborators, doctoral students and prospective innovation partners.

**One-sentence promise:** Discover an accounting AI research product in seconds, learn its intended task through a short scenario, and independently inspect its evidence boundary.

**Design inspiration vs copying:** Inspired by visual discovery cards and brief sequential stories familiar from consumer platforms, but intentionally **not** copying Instagram or TikTok's branding, content, trade dress, opaque feed ranking, attention-maximizing mechanics or algorithmic data collection.

## Information architecture

```text
Discover
  ├── Quick stories (tap product)
  ├── Search (task language)
  ├── Subject filters (Audit / Reporting / Research)
  └── Product card
      ├── Task-oriented promise
      ├── Transparent maturity label
      ├── Four-step explanatory storyboard
      └── Official public evidence source (if available)
Trust and governance
  ├── No model execution on this page
  ├── No scientific or regulatory certification claim
  ├── No private IP or licensed data
  └── Human decision and evidence boundary
```

## Experience principles

1. **10-second value proposition:** explain the practical research task before architecture details.
2. **Progressive disclosure:** benefit → story → evidence → repository, rather than front-loading terminology.
3. **Task-first taxonomy:** users search for IFRS, CAM, audit evidence and inspection rather than tool/framework names.
4. **Evidence before persuasion:** status and source links remain visible alongside each product.
5. **No misleading demo:** all walkthroughs say illustrative and do not pretend to run a back end.
6. **Private-by-design:** public-facing features are hard-separated from the proprietary POMELO/VERA implementation.
7. **Responsible discovery:** search and category filtering are user-controlled; there is no engagement-driven recommendation algorithm.

## Product architecture in future releases

```text
Static public discovery shell (this pilot)
  -> Controlled product catalogue manifest (next)
     -> Public product case demonstrations (optional)
        -> Evidence Passport service (only authorized sources)
           -> Validation/falsification and Human Gate
              -> Export of reproducible, scoped research artifacts
Private / licensed data and proprietary services: separate authenticated boundary
```

**Do not** connect an unreviewed public front end directly to private Google Drive, GitHub private repositories, confidential CAM/Audit Analytics datasets, provider API keys, or a professional decision engine.

## Prioritized backlog

| Priority | User outcome | Feature / gate | Acceptance criteria |
| --- | --- | --- | --- |
| P0 | Find a relevant product | Search, mobile filter, recognizable cards | All cards keyboard reachable and filterable |
| P0 | Understand maturity | Standardized research status labels | No claim of production, certification or proven impact |
| P0 | Inspect a source | Official repo/programme links | Links manually checked before merge |
| P0 | Prevent confidential disclosure | Public-safe static catalogue | No private URLs, secrets or private data |
| P1 | See real reproducible value | A public synthetic scenario per flagship | Executable test + source + provenance + reviewed limits |
| P1 | User confidence | Evidence Passports / evaluation cards | Complete trace from claim to public evidence |
| P1 | Improve onboarding | Audience-based task entry | Task testing with at least four audience roles |
| P2 | Expand product adoption | API/demo sandbox with rate limits | Legal, security, model-risk and human-gate approval |
| P2 | Measure UX scientifically | Privacy-respecting opt-in analytics | Consent/privacy review; zero raw client data |

## Research-grade differentiation

Conventional visual discovery often maximizes engagement. NAAIL should optimize **informed, verifiable task completion**. Suggested north-star metric: **Evidence-grounded successful product discovery rate**, defined as visitors who (a) identify the appropriate research tool, (b) correctly describe its maturity and (c) access a credible source, divided by participants given a real task. Collect via structured usability testing initially, not silently tracked behavior.

## Review checklist

- [ ] Mobile viewport sizes at 320, 375, 768 and 1280 px
- [ ] Keyboard-only walkthrough and Escape dismissal
- [ ] Screen-reader labels and focus restoration
- [ ] Search and all three filters
- [ ] Verified official links
- [ ] Product-owner review of statuses and intended task framing
- [ ] Scientific/rights/IP approval
- [ ] Deployment setup separately approved

References: Nielsen Norman Group's progressive disclosure guidance and GitHub Pages publishing documentation. Preserve the portfolio's existing `NAAIL_PRODUCT_STANDARD.md` and scientific governance policies.
