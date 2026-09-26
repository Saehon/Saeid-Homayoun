# Hugging Face publishing

Target Space:

- https://huggingface.co/spaces/SADHON/ibm-granite-accounting-audit

The GitHub workflow `.github/workflows/sync-ibm-granite-hf.yml` publishes this folder to the user's Hugging Face account.

## One-time credential requirement

GitHub needs a repository secret named `HF_TOKEN` containing a Hugging Face token with **write** permission.

The current ChatGPT Hugging Face connection is read-only (`read-repos`) and therefore cannot create the Space directly.

After `HF_TOKEN` is configured, the workflow can be run manually and will also sync future changes from `main`.
