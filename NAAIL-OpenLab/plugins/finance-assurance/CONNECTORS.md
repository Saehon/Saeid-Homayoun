# Optional connectors (not installed)
This prototype runs **offline**. No default MCP endpoints or account tokens are bundled. Intended adapters: Google Drive (controlled document archive), GitHub (code and provenance), SEC EDGAR/XBRL (public company facts with SEC fair-access practices), spreadsheet workpapers, ERP general ledger (authorized read-only access), Kaggle/Hugging Face (rights-cleared teaching or benchmark datasets), optional LLM providers.

## Integration contract
1. The project owner approves data location, read scope, vendor, lawful purpose and retention before connecting.
2. Default to **read-only**, minimal privileges, redaction and per-dataset provenance. Never send client data into a model without permission.
3. Raw accounting evidence remains in the authorized Drive or data vault. GitHub stores only code and redacted/synthetic fixtures.
4. Provider output is a suggestion, not evidence or assurance. Preserve input hashes, source references, prompt/model versions and reviewer verdict.
5. Any ledger write, filing, disclosure, compliance classification or publication requires a separate explicit human action.
6. No automated cross-platform synchronization is claimed: this folder indexes platforms until dedicated integrations are reviewed and configured.
