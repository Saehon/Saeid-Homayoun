# NAAIL Product Experience Hub — UX pilot v0.1

**Status:** interactive front-end UX prototype; **not deployed**; no live AI backend or licensed/proprietary data.

## The user-facing problem

The public NAAIL research portfolio has extensive academic and engineering documentation. A first-time visitor, however, may not know which repository to open, what use case a product supports, or what is executable versus merely specified. This pilot adds an independent **discover → understand → verify** layer.

## Try it

1. Open `index.html` in a modern desktop or mobile browser. No package installation or credentials are needed.
2. Select a product story.
3. Read the four **illustrative** steps.
4. Follow **Read public evidence** to review the actual repository or programme document.
5. Try search and the Audit, Reporting, and Research filters.

**No live inference:** stories are static educational scripts. The UI must not be interpreted as proof that backends, performance metrics, workflows, or case results are operational.

## Content inventory and classification

| Card | Public source | Maturity statement in UX |
| --- | --- | --- |
| IFRS-AI Inspector | `Saehon/IFRS-AI-Inspector` | Public research prototype |
| KIWI / CAM–KAM Intelligence | Public research programme summary in this repo | Research programme |
| PCAOB Inspection Intelligence | Public PCAOB programme document in this repo | Public design / private R&D |
| NAAIL OpenLab | `NAAIL-OpenLab/` | Public research laboratory |
| POMELO / VERA | No hyperlink to private repository | Proprietary private R&D |
| AAA Audit & Accounting AI Lab | `Saehon/AAA` | Public research laboratory |

Third-party forks/reference repositories have deliberately **not** been presented as original NAAIL products.

## Accessibility, security and privacy

- Responsive layout and keyboard-operable buttons/dialog.
- Explicit search label, polite result announcement, progress indicators, visible focus, reduced-motion support.
- No trackers, ad pixels, cookies, storage, network APIs, secret keys or external JS/CSS dependencies.
- No uploads, accounts, user-generated posts, rankings, notifications, dark patterns or algorithmic personalization.
- All public hyperlinks use official GitHub URLs; private POMELO material is not linked or embedded.
- No unsupported scientific, regulatory or production-readiness claims.

## Publishing (a separate approval gate)

The prototype is currently **source code on a feature branch**, not a live website. For a public deployment, merge the reviewed changes, then use **GitHub Settings → Pages** to choose a publishing source. GitHub Pages supports publishing from the root or `/docs` of a chosen branch, or via GitHub Actions. Because this prototype is under `product-hub/`, a deployment would need a deliberately selected publishing strategy (e.g., a dedicated Pages branch or a simple deployment workflow). Do not assume that creating the HTML file activates GitHub Pages.

Before publishing, review rights, project metadata, product names, legal notices, and the current status of every featured project.

## Pilot success metrics (targets, not observed)

| Metric | Pilot target | Collection recommendation |
| --- | --- | --- |
| First useful click | within 15 seconds for ≥80% of test participants | Moderated usability session |
| Correctly identify which product fits a task | ≥80% success | Scenario task; 5–8 participants per audience |
| Correctly distinguish prototype from production | ≥90% | Ask unaided comprehension question |
| Find an authoritative public source | ≥80% | Task success, link destination check |
| Mobile usability | No major blocking task errors | Keyboard + small-screen testing |
| Perceived clarity | ≥4/5 | Post-task survey |

No actual measurements or completed usability studies are claimed.

## Next engineering milestones

1. Verify every external link and run automated HTML accessibility checks.
2. Test tasks with an auditor, PhD researcher, student and potential collaborator.
3. Connect only verified public sandbox scenarios; keep professional approvals and restricted data behind separate access controls.
4. If launch approved, add an evidence-governed case-explorer and publish through a reviewed, versioned Pages workflow.
5. Maintain a central, single-source-of-truth product manifest; implement automatic status validation before any dynamic feed.

**Canonical IP boundary:** Research content, private specifications and unpublished datasets remain in their respective controlled repositories/Google Drive. This directory only contains safe public descriptions and static walkthroughs.
