# GitHub → Hugging Face → Kaggle publication plan

**Source of truth:** GitHub `Saehon`.

Target naming convention:
- GitHub: `Saehon/<PROJECT>`
- Hugging Face: `SADHON/<PROJECT>`
- Kaggle title: `<PROJECT>` (slug may be normalized by Kaggle)

## Publication gate
Only public repositories suitable for redistribution should be mirrored. Private repositories are excluded. Forked or third-party repositories require license/attribution review before republication.

## Credentials
Store credentials only as GitHub Actions secrets. Never commit or paste tokens into repository files.

Expected secrets:
- `HF_TOKEN`
- `KAGGLE_USERNAME`
- `KAGGLE_API_TOKEN`

## Initial research portfolio priority
1. Saeid-Homayoun / NAAIL-OpenLab
2. AAA
3. IFRS-AI-Inspector
4. AuditData-API
5. financial-services / GPT adapter work

The helper at `scripts/prepare_cross_platform_publish.py` validates the project name and prepares a clean public source tree. A GitHub Actions publisher can invoke it once Actions workflow creation is authorized.
