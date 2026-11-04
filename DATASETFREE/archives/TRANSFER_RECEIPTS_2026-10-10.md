# Verified transfer receipts — 10 October 2026

**Canonical source of truth:** [Google Drive archive](https://drive.google.com/drive/folders/19m030UxkJeu36nij7IbRV-OnxcXt33vj)

**Full provenance receipt:** [Google Doc](https://docs.google.com/document/d/1-E1lpCmTAfoI9l1EnNAgHQ-3eK5Fj2J1Trom2qiyAnU/edit)

| Artifact | Actual Google Drive file | Bytes | Archive SHA-256 |
|---|---|---:|---|
| MacAma MIT + Twin-2K-500 Apache selected code-only subset | [CLEAN code archive](https://drive.google.com/file/d/1_UOuWnG1ve1dx3Ts2XE2OFzwVlrBXA5s/view) | 151,204 | c41150a520068fdc3bd5d3f0f4dc7ed1f2d829c3dde5d955aa59c789f45990c0 |
| Synthetic candidate-matching MIT-labelled benchmark (3 small Parquet files) | [Synthetic dataset archive](https://drive.google.com/file/d/1NcVqUcWSvoQwhvbq1TdTyKOolyIQeIZT/view) | 451,159 | 89cc30bc48aedc7438ddf17425e7041cd1a3ff90ebf917b16f69c32e06efd04b |

## Code source revisions

- [MacAma](https://github.com/YilinYuan/MacAma) MIT commit `5873f38d85e29712b83a1689ddcc6ee6f574c0c5`.
- [Twin-2K-500](https://github.com/tianyipeng-lab/Digital-Twin-Simulation) Apache-2.0 commit `f1eed510c9a4fb47aaa9bb46e178aaa2d9224623`.
- Hugging Face candidate matching source: [michaelozon](https://huggingface.co/datasets/michaelozon/candidate-matching-synthetic). Licence label MIT; all rows are **synthetic**.

Upstream GitHub Actions were successful and transferred through authenticated file references to private Google Drive. The **original first code snapshot was updated in place** with the clean, dependency-free selected code snapshot; inspect Drive revision history if needed.

**Not completed:** downloading all 47 studies' original microdata and scripts, reproducing published coefficients, pushing a user-owned dataset to Hugging Face (current @SADHON connector read only), or publishing on Kaggle (account not connected). Public code without a verified licence stays linked, not mirrored. The code and dataset above are first approved examples only.
