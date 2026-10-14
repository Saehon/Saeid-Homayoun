# ANALYST ICOFR — code only

This repository contains reusable code only. Hugging Face and Kaggle calls authenticate and read; there are no dataset publishing, model upload, hosted inference, or remote analysis actions. Private source identifiers, rows, downloads, model files and results belong in a separate private directory. Nothing reads Google Drive or writes to it: move results to your private Drive through your approved workflow.

## Setup

Python 3.10+ is required. Create a virtual environment and install only what you need:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python connector.py status
python -m unittest discover -s tests -v
```

For local classification also install `requirements-local.txt`. Supported services need network access on your machine. Provider authorization has not been executed by simply adding this code.

Provide a read-only Hugging Face token through `HF_TOKEN`. For Kaggle use `KAGGLE_API_TOKEN` with a current Kaggle package, or the legacy pair `KAGGLE_USERNAME` and `KAGGLE_KEY`. Obtain tokens in your account settings. Store actual values in an OS secret manager, an untracked local environment, or GitHub repository secrets; never commit them, paste them into command arguments, or include them in a notebook. `.env.example` has empty variable names and is not automatically loaded. Account license/gated access terms must already be accepted where applicable.

```bash
python connector.py check --provider hf
python connector.py check --provider kaggle
```

Successful checks print a boolean status without account names. HF uses its authenticated identity endpoint. Kaggle makes an authenticated read of your dataset listing; it discards the returned metadata. Service failures print a fixed diagnostic so credentials, source IDs and response bodies do not enter logs.

## Local downloads

Choose a private root outside this repository and every Git working tree. On POSIX machines existing roots must have owner-only permissions (`chmod 700`); new roots are created that way. Replace uppercase placeholders yourself; do not commit filled-in commands that identify private sources. Each destination must be new. Downloads are inputs and never become GitHub artifacts.

```bash
python connector.py hf-download --kind model --repo-id NAMESPACE/MODEL \
  --revision FULL_COMMIT_SHA --accept-license LICENSE_IDENTIFIER \
  --local-root /absolute/private-work --destination models/classifier

python connector.py hf-download --kind dataset --repo-id NAMESPACE/DATASET \
  --revision FULL_COMMIT_SHA --accept-license LICENSE_IDENTIFIER \
  --local-root /absolute/private-work --destination inputs/hf-dataset

python connector.py kaggle-download --dataset OWNER/DATASET \
  --local-root /absolute/private-work --destination inputs/kaggle-dataset
```

HF requires the full immutable commit revision, matches it to server metadata, and requires the exact declared license identifier. Review actual license text and use restrictions before providing that identifier. Repositories with missing license metadata or `other` are rejected; request a documented standard license or review outside this tool. Model downloads include safetensors and tokenizer/config files only. Python code and pickle-based weights are excluded. A private metadata file records download provenance locally. HF dataset downloads require an explicit identifier and do not execute loading scripts. Kaggle downloads stay as unopened archives; review licenses and archive contents before extracting. Kaggle download calls retrieve the current dataset version; they are not pinned by this wrapper. Failed downloads can leave partial local directories: inspect or remove them locally and choose a new destination before retrying.

## Offline classification

Use a safetensors model compatible with Transformers' built-in sequence classification architecture. Use the checked, pinned HF download above, or independently verify the provenance and license of an existing local model. Classification does not certify an arbitrary local model's provenance or license. Models that need custom Python code or missing auxiliary files will fail. Local inputs do not need network permission. The CLI forces Hugging Face and Transformers offline mode, refuses remote custom code, and uses CPU inference.

```bash
python connector.py classify-local --local-root /absolute/private-work \
  --model-dir models/classifier --input-csv /absolute/private-work/inputs/text.csv \
  --text-column text --output outputs/classified.csv
```

The output preserves every original column, including any existing human label, and appends `predicted_label` and `model_confidence`. Blank/malformed text rows fail instead of being silently skipped. Every model label and confidence is checked, and only a completed CSV is committed to the private output path. Confidence is the model score, not a verified probability of correctness. Long inputs are truncated to the model limit; evaluate the model and truncation effect before acting on results. Do not open untrusted text CSVs in a spreadsheet without handling formula injection there.

## GitHub and notebook use

The repository workflow `.github/workflows/analyst-icofr-connections.yml` runs only when manually started and lets you choose Hugging Face, Kaggle or both. Add repository secrets `HF_TOKEN` and either `KAGGLE_API_TOKEN` or the legacy Kaggle pair. It checks connectivity only: no datasets, private CSVs, analysis, model downloads, or artifact upload step. Secrets belong in Settings → Secrets and variables → Actions, never in YAML. GitHub shows manual workflow controls once the workflow exists on the repository default branch. `starter.py` can be copied to a private notebook environment as a CLI entrypoint; no notebook output is shipped. Kaggle notebooks execute on Kaggle infrastructure, so run private analysis locally if it must stay off that platform.

## Optional matrix engine

`risk_matrix.py` provides an input-gated CAM/ICFR matrix function using independently supplied, dated risk scores and an explicitly verified eligible-account roster. It preserves unknown states, requires at least20 distinct valid firms for peer thresholds, and keeps incomplete competitor measures unknown. The module docstring defines the required DataFrame schema; no dataset or result is included. Run `python -m unittest -v test_risk_matrix` for its16 synthetic tests. These tests validate code behavior and make no empirical research claim.

To connect another source, add a separate read-only adapter that accepts an explicit identifier and obtains credentials from environment variables. Preserve the same private output boundary and fixed error messages. This repository does not create a general upload channel.

## Local CAM token-risk proxy

`token_risk_profile.py` uses the Hugging Face `tokenizers` library locally for
Unicode normalization and token segmentation. It applies a reviewable,
versioned phrase lexicon to `TITLE`, `DESCRIPTION`, and `RESPONSE`, while the
primary CAM narrative proxy uses `TITLE` plus `DESCRIPTION` only. Auditor
response language stays separate. No Hub upload, hosted inference, or
pretrained model inference occurs.

`darwin_token_risk.py` joins the private token profile to separately supplied
account and opinion-year crosswalks. It can assign provisional H/L/U levels
within current-SIC2 × account × fiscal-year groups using a linear 70th
percentile, ties high, and at least 20 distinct companies. Every source row is
already CAM-present, ICFR remains unknown, and the only possible descriptive
matrix cells are A3, C3, and U5. It creates no CAM-absent observations.

Both commands require a new private output directory outside every Git working
tree and an expected source SHA-256 supplied at run time. Use placeholders in
saved scripts and terminal documentation; keep actual paths and fingerprints
in private storage.

```bash
python token_risk_profile.py \
  --cam /ABSOLUTE/PRIVATE/CAM.csv \
  --crosswalk /ABSOLUTE/PRIVATE/topic_account_crosswalk.csv \
  --expected-cam-sha256 EXPECTED_64_HEX_SHA256 \
  --out /ABSOLUTE/PRIVATE/new-token-profile-output

python darwin_token_risk.py \
  --cam /ABSOLUTE/PRIVATE/CAM.csv \
  --profile /ABSOLUTE/PRIVATE/new-token-profile-output/CAM_token_risk_profile_rows_PRIVATE.csv \
  --opinion-year-crosswalk /ABSOLUTE/PRIVATE/opinion_year_crosswalk.csv \
  --expected-cam-sha256 EXPECTED_64_HEX_SHA256 \
  --out /ABSOLUTE/PRIVATE/new-darwin-output
```

The result is a `post_selection_descriptive_proxy`: disclosure-language
intensity after CAM selection. It is not independent account risk, a CAM
probability, ICFR evidence, a material-misstatement probability, or a causal
estimate. Do not pass it to `risk_matrix.evaluate_risk_matrix` as independent
`R_iat`. Competition fields cover observed mapped CAM accounts only and are
not canonical DARWIN competition measures.

Run the synthetic tests from this directory:

```bash
python -m unittest discover -s tests -v
python -m unittest -v test_risk_matrix
```
