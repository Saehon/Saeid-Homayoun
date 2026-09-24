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

sync_notebooks() {
  local base="${ROOT_DIR}/notebooks"
  [[ -d "${base}" ]] || return 0

  while IFS= read -r -d '' metadata; do
    local dir
    dir="$(dirname "${metadata}")"
    echo "Publishing Kaggle notebook from ${dir}"
    kaggle kernels push -p "${dir}"
  done < <(find "${base}" -type f -name kernel-metadata.json -print0)
}

sync_datasets() {
  local base="${ROOT_DIR}/datasets"
  [[ -d "${base}" ]] || return 0

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
      kaggle datasets version -p "${dir}" -m "${VERSION_MESSAGE}"
    else
      if [[ "${CREATE_PUBLIC}" == "true" ]]; then
        kaggle datasets create -p "${dir}" --public
      else
        kaggle datasets create -p "${dir}"
      fi
    fi
  done < <(find "${base}" -type f -name dataset-metadata.json -print0)
}

sync_notebooks
sync_datasets

echo "Kaggle synchronization completed."
