#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="${1:-kaggle}"
CREATE_PUBLIC="${KAGGLE_CREATE_PUBLIC:-false}"
VERSION_MESSAGE="${KAGGLE_VERSION_MESSAGE:-GitHub sync ${GITHUB_SHA:-local}}"

if [[ -z "${KAGGLE_API_TOKEN:-}" ]]; then
  echo "KAGGLE_API_TOKEN is not set."
  exit 1
fi

echo "Validating Kaggle authentication..."
kaggle datasets list -m -p 1 >/dev/null
echo "Authenticated to Kaggle."

sync_datasets() {
  local base="${ROOT_DIR}/datasets"
  [[ -d "${base}" ]] || return 0
  local dataset_failures=0

  while IFS= read -r -d '' metadata; do
    local dir dataset_ref
    dir="$(dirname "${metadata}")"
    dataset_ref="$(python - "${metadata}" <<'PY'
import json
import sys

with open(sys.argv[1], "r", encoding="utf-8") as f:
    metadata = json.load(f)

dataset_id = metadata.get("id", "").strip()
if not dataset_id:
    raise SystemExit("dataset-metadata.json must contain a non-empty 'id' field.")
print(dataset_id)
PY
)"

    echo "Synchronizing Kaggle dataset ${dataset_ref} from ${dir}"

    if kaggle datasets files "${dataset_ref}" >/dev/null 2>&1; then
      if ! kaggle datasets version -p "${dir}" -m "${VERSION_MESSAGE}"; then
        echo "::error::Failed to version Kaggle dataset ${dataset_ref}"
        dataset_failures=$((dataset_failures + 1))
      fi
    else
      if [[ "${CREATE_PUBLIC}" == "true" ]]; then
        if ! kaggle datasets create -p "${dir}" --public; then
          echo "::error::Failed to create public Kaggle dataset ${dataset_ref}"
          dataset_failures=$((dataset_failures + 1))
        fi
      else
        if ! kaggle datasets create -p "${dir}"; then
          echo "::error::Failed to create private Kaggle dataset ${dataset_ref}"
          dataset_failures=$((dataset_failures + 1))
        fi
      fi
    fi
  done < <(find "${base}" -type f -name dataset-metadata.json -print0)

  if [[ "${dataset_failures}" -gt 0 ]]; then
    echo "Dataset synchronization completed with ${dataset_failures} failure(s)."
    return 1
  fi
}

sync_notebooks() {
  local base="${ROOT_DIR}/notebooks"
  [[ -d "${base}" ]] || return 0

  while IFS= read -r -d '' metadata; do
    local dir
    dir="$(dirname "${metadata}")"
    echo "Publishing Kaggle notebook from ${dir}"
    if ! kaggle kernels push -p "${dir}"; then
      echo "::warning::Kaggle notebook sync failed for ${dir}; dataset synchronization is unaffected."
    fi
  done < <(find "${base}" -type f -name kernel-metadata.json -print0)
}

# Datasets are the canonical publication target and must not be blocked by notebook issues.
sync_datasets
sync_notebooks

echo "Kaggle synchronization completed."
