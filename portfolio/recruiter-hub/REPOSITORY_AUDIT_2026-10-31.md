# GitHub Portfolio Improvement Audit

**As of:** 2026-10-31  
**Account:** [Saehon](https://github.com/Saehon)  
**Inventory:** 48 repositories visible to the connected account (41 public, 7 private).

## Concrete findings

| Priority | Observation | Consequence | Intervention |
|---|---|---|---|
| P0 | NAAIL canonical README has approximately 630 lines and repeated, overlapping umbrella sections | Valuable evidence is buried below long explanations | Add a concise recruiter-first navigation above the existing material; preserve original research text for subsequent editorial review |
| P0 | No special `Saehon/Saehon` profile repository appears in the current repository inventory | Personal GitHub profile does not surface a curated user-profile README | Prepared [PROFILE_README_READY.md](PROFILE_README_READY.md) for the dedicated profile repository; publication requires account action to create `Saehon/Saehon` |
| P0 | Mixed original projects and third-party reference repositories | Potential mistaken inference of code authorship | Apply explicit `Original contribution`, `Upstream fork`, `Reference`, or `Unverified provenance` labels |
| P1 | Nine position-specific career demonstrations reside in open PRs, several private | Recruiter cannot assume code is merged or accessible | Provide [evidence matrix](PROJECT_EVIDENCE_MATRIX.md), public entry points and visibility notes |
| P1 | Passing synthetic cases can be mistaken for model accuracy | Scientific/reputational risk | Explicitly label tests and disclose unknown external-validity metrics |
| P1 | `Riks-Index` has no root README found during this audit | Poor discoverability; purpose not documented | Add an accurate minimal README only after verifying its content and intended ownership |
| P1 | Imported/reference repos may contain README text describing upstream maintainers as authors | Possible false authorship claims | Do not rewrite original licenses or remove upstream credit; add an account-level classification |
| P2 | Repository default branches differ (`main`, `master`, `dev`) | Not intrinsically a defect | Leave upstream repositories unchanged; check each canonical development policy |
| P2 | Actual repository security setting state is not fully checked | Dependabot/secret scanning/branch rules cannot be asserted as enabled | Owner should review security settings and code scan results; follow GitHub guidance |

## Verified attribution examples

- **Original/canonical academic portfolio:** `Saehon/Saeid-Homayoun` (NAAIL OpenLab), alongside original role-specific contributions visible in their exact PR diffs.
- **Research prototype with investigator attribution:** `Saehon/IFRS-AI-Inspector`; only claim personally authored changes that can be traced.
- **Externally sourced reference examples:** `Saehon/financebench` (Patronus AI upstream materials), `Saehon/inspect_ai` (UK AI Security Institute), `Saehon/timesfm` (Google Research), `Saehon/AuditData-API` (AICPA/XBRL ecosystem). Never claim upstream code as original work.
- **Private proprietary project:** `Saehon/pomelo-core`; keep confidential and do not mirror patent-sensitive algorithms into a public portfolio.

## Recommended profile pin strategy

GitHub profile pins are a user-controlled account setting and **not configured by this audit**. Select six with an honest balance of original code, research and working demonstrations, prioritizing:
1. `Saeid-Homayoun`
2. `IFRS-AI-Inspector`
3. `Saeid-Homayoun-Test`, if the education/assurance demo is useful and clearly labeled
4. `AAA`, after ownership and reproducibility inspection
5. `Google-Antigravity-using-a-multi-agent-BERT-architecture`, only after third-party provenance review
6. another verified original research project rather than an unchanged upstream fork

## Responsible security checklist

Check **Settings → Advanced Security** per repository for dependency alerts, secret scanning and push protection (where available). Keep credentials in environment/secret stores, never in README, commits or issues. A security badge, passing CI or a policy file is not proof that monitoring features are enabled.

Do not publish licensing-restricted datasets or private Google Drive/Claude/Codex records. Preserve research chronology, duplicate detection and no-leakage gates.

**Sources:** [GitHub repository best practices](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories) · [Security quickstart](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository).
