from __future__ import annotations

from pathlib import Path

APPROVED_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def embed_texts(texts: list[str], model_name: str = APPROVED_EMBEDDING_MODEL):
    """Optional local Hugging Face embedding adapter.

    This is never used as authoritative IFRS/PCAOB evidence. Model/license terms
    must be reviewed before changing the default or redistributing model files.
    """
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(model_name)
    return model.encode(texts)


def download_kaggle_dataset(handle: str, *, license_approved: bool, output_dir: str | None = None) -> Path:
    """Optional Kaggle dataset adapter with an explicit license gate.

    `handle` must be a dataset handle selected by the researcher. NAAIL does not
    ship a generic 'approved Kaggle dataset' because licenses and provenance are
    dataset-specific.
    """
    if not license_approved:
        raise PermissionError("Dataset-specific license/provenance approval is required before Kaggle download.")

    import kagglehub

    path = Path(kagglehub.dataset_download(handle))
    if output_dir is None:
        return path

    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)
    return path


def github_reference(repo_url: str, commit_sha: str, *, license_approved: bool) -> dict[str, str | bool]:
    """Record a GitHub dependency without pretending NAAIL owns upstream code."""
    if not repo_url.startswith("https://github.com/"):
        raise ValueError("repo_url must be a GitHub repository URL")
    if len(commit_sha) < 7:
        raise ValueError("pin a real commit SHA or stable release commit")
    return {
        "repo_url": repo_url,
        "commit_sha": commit_sha,
        "license_approved": license_approved,
        "ownership": "third_party_upstream",
    }
