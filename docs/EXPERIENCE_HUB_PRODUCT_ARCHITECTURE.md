# NAAIL Experience Hub — Product Architecture and UX MVP

**Owner:** Saeid Homayoun / NAAIL OpenLab™  
**Stage:** UX research prototype, proposed for review (not a production release)  
**Scope:** Public, educational product-discovery frontend. Does not invoke private research engines.  
**Implementation:** [Interactive Discover prototype](../discover/index.html).

## 1. Evidence-based diagnostic

Review scope: the public root `README.md`, `index.html`, `PRODUCT_PORTFOLIO.md`, `NAAIL_PRODUCT_STANDARD.md`, and representative public/private repository README files.

Observed:
- The root GitHub README is comprehensive, but its first screen is primarily academic and technical navigation.
- The website's main entry actions are academic profile, Scholar and ORCID; core cards link visitors directly to repository pages.
- Technical products describe methodology, governance and research boundaries well, but most lack a short, role-specific first-use experience.
- Existing GitHub portfolio separates source code, private R&D and external intellectual property, a boundary that must not be weakened.

**Product problem (hypothesis, not tested user evidence):** A non-developer may not know what to click, what task a tool solves or whether a demonstration is safe to use. Actual user testing is needed to validate this hypothesis.

## 2. Product vision

**NAAIL OpenLab is the umbrella brand.** KIWI, IFRS-AI Inspector, POMELO / VERA, ICFR, MACEI / TDABC, AuditData-API and ISSB/ESG are product experiences or specialized modules, not competing parent platforms.

Experience loop:

`Discover by role → Guided example → Inspect evidence → Open method/code → Validate independently → Human decision`

Borrow from modern discovery products:
- Low-friction entry: no mandatory sign-in for public education.
- Relevant ordering: user chooses role; the first cards match the relevant job to be done.
- Short, interactive explanations instead of long documentation as the first experience.
- Persistent user-controlled bookmarks, local to the device.

**Do not copy** engagement-optimizing infinite scrolling, opaque ranking, deceptive social proof, synthetic user counts, fake likes or unverified claims of regulatory validation. The optimization target is *useful, evidence-verified task completion*, not raw watch time.

Relevant platform explanations:
- TikTok official recommendation guidance: https://support.tiktok.com/en/using-tiktok/exploring-videos/how-tiktok-recommends-content
- Meta's Instagram Feed system card: https://ai.meta.com/tools/system-cards/instagram-feed-ranking/

## 3. Primary user journeys

| Persona | Primary job to be done | First public experience | Genuine next step |
|---|---|---|---|
| External auditor | Assess how a CAM, ICFR weakness or evidence gap should be examined | KIWI or ICFR synthetic walkthrough | Inspect methods, datasets permitted for release and reproducibility gates |
| CFO / controller | Understand the information and cost consequences of a reporting or capacity decision | IFRS-AI Inspector or MACEI / TDABC walkthrough | Review assumptions and request a supervised pilot |
| Researcher | Trace measurement, controls and data lineage | AuditData-API or KIWI | Access the public code and documented validation methodology |
| Student | Understand evidence-based accounting AI without installing tools | IFRS or TDABC walkthrough | Move into teaching exercises and sample data |
| Investor | Understand how audit evidence and disclosure quality may affect decision relevance | KIWI and ISSB | Inspect uncertainties, reporting dates and supporting research |

These are proposed personas, **not** results of observed interviews or measured usage.

## 4. Information architecture

- **Layer 0: Discover experience** — public landing and curated catalogue; links to authoritative public project repositories.
- **Layer 1: Guided educational demo** — small synthetic scenarios, fully labelled and separated from live analysis.
- **Layer 2: Scientific evidence and method** — source authority, sample construction, provenance, reproducibility, uncertainty and validation state.
- **Layer 3: Professional workflow (future, authenticated)** — upload/access control, scoped AI analysis, evidence passports, user permissions, independent evaluation, human approval.
- **Layer 4: Knowledge & Technology Cores (private)** — retain the canonical two-core architecture and research governance; never expose private Google Drive data in the static frontend.

For a future production system, use an authenticated backend-for-frontend (BFF) and scoped service APIs. Any retrieval of private Drive data must occur server-side, with permission checks, audit logs and explicit user authorization. Keep client-side scripts completely free of secrets, privileged paths, proprietary rule sets and licensed data.

## 5. Current implementation

`discover/index.html` is a dependency-free static HTML/CSS/JavaScript proof of concept:
- Mobile-first interface, semantic headings, visible keyboard focus, reduced-motion accommodation.
- Searchable research-experience cards and user-selected audience ordering (not algorithmic personalization).
- Seven guided synthetic previews with three explicit steps each.
- Source/overview links and maturity labels.
- Saved-card bookmarks using browser local storage; gracefully degrades if storage is blocked.
- No account requirement, network API, tracking pixel, advertising, automatic personalized profiling or private-data connector.

**Limits:** No actual model is run, no financial file is analyzed, no real consumer analytics have been gathered, no professional assurance is produced, and no site deployment is implied by the existence of the code. The POMELO and MACEI experiences are educational previews; underlying private code remains private.

## 6. Public release gates

Before merging or enabling GitHub Pages:
1. Check public disclosure and IP rights for project descriptions and links.
2. Confirm every visible product links to a readable public page for external visitors.
3. Run keyboard/screen-reader and WCAG 2.2 AA accessibility review.
4. Test breakpoints at 320, 375, 768 and 1280 px; inspect links, preview modal, search and saved-only.
5. Verify that illustrative figures are clearly marked synthetic and never promoted as empirical results.
6. Inspect all links and run a static scan for secrets, external calls and third-party content.
7. Obtain maintainer/Human Gate approval before public release.

## 7. Scientific and product metrics

Set baselines *after* a consent-respecting pilot, not from repository files or imagined usage.

| Metric | Definition | Why it matters |
|---|---|---|
| Time to first meaningful action | Median seconds from landing to relevant preview or method opened | Reduces discovery friction |
| Guided-preview completion | Completed previews / previews started | Measures clarity of the flow |
| Evidence-follow-through | Evidence/method link opens / completed previews | Measures scientific transparency |
| Task usefulness | User-rated usefulness after representative task | Measures value rather than amusement |
| Failed-search rate | Searches with no matching experiences / searches | Measures information architecture |
| Trial-to-validated-use | Pilots passing documented research gates / pilots started | Measures real research/professional readiness |

**North star (proposed):** evidence-verified successful task completions per consenting active user. Avoid default analytics collection on a research site.

## 8. Prioritized roadmap

**P0 — This pull request:** public-facing discover UI, accessible guided synthetic examples, documented boundaries, root-site navigation.

**P1 — User research:** 5–8 qualitative usability sessions covering auditors, controllers, academics, students and investors. Test task comprehension, navigation, trust and accessibility. Update design from evidence.

**P2 — Verified sandbox:** public/approved synthetic data only; demonstrable deterministic computations with published formulae, assertions, code and tests; optional secure demo API.

**P3 — Authenticated product trials:** organization-level tenancy, data rights, RBAC, human approvals, audit logs, GDPR/security review and pricing/ROI validation before commercialization.

## 9. Maintenance protocol

This document is the **canonical UX/product specification** for the experience-hub scope. Update in place rather than creating serial product-design plan copies. GitHub holds implementation, tests and public-safe architecture; Google Drive remains the canonical controlled repository for private working data, licensed materials and restricted studies.

## 10. Acceptance criteria

The MVP may be accepted when a new visitor can (a) select their professional role, (b) find a relevant research experience, (c) complete the synthetic three-stage walkthrough, (d) access a public research overview, and (e) understand why this example is not a live, certified accounting or audit engine.
