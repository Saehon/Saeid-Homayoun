# GitLab Independent CI Mirror

This repository is designed to remain **GitHub-first**. GitLab is an independent CI validation surface.

## GitLab project name

Use the same repository name as GitHub:

`Saeid-Homayoun`

Recommended GitLab project path:

`<your-gitlab-username>/Saeid-Homayoun`

## Free setup

1. In GitLab choose **New project/repository → Import project → Repository by URL**.
2. Repository URL:
   `https://github.com/Saehon/Saeid-Homayoun.git`
3. Set project name to **Saeid-Homayoun**.
4. Keep the project public or private according to your preference.
5. Import the repository.
6. GitLab automatically detects the root `.gitlab-ci.yml` and runs the independent pipeline.

## Independent test layers

The GitLab pipeline intentionally does not depend on GitHub Actions. It checks:

- Python syntax for the scientific/governance and IBM integration code.
- Governance/orchestrator tests.
- Microsoft research-prototype 15-contract test suite.
- IBM Granite model registry integrity.

## Architecture

```text
GitHub: Saehon/Saeid-Homayoun
        |
        | source / periodic import
        v
GitLab: <user>/Saeid-Homayoun
        |
        v
Independent GitLab CI
        |
        +-- syntax
        +-- governance
        +-- research prototype contract
        +-- IBM Granite registry
```

GitHub remains the Source of Truth. GitLab is a second, independent CI surface rather than a competing development home.
