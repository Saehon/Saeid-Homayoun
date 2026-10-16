"""Publish only the permission-cleared synthetic Risk-CAM starter to Kaggle.
Requires KAGGLE_USERNAME and KAGGLE_KEY. Never reads Google Drive or private data.
"""
import json, os, pathlib, shutil, subprocess, tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
os.environ["KAGGLE_USERNAME"]
os.environ["KAGGLE_KEY"]
with tempfile.TemporaryDirectory(prefix="riskcam_kaggle_") as td:
    out=pathlib.Path(td)
    shutil.copy2(ROOT/"data"/"SYNTHETIC_demo.csv",out/"SYNTHETIC_demo.csv")
    shutil.copy2(ROOT/"distribution"/"kaggle"/"dataset-metadata.json",out/"dataset-metadata.json")
    shutil.copy2(ROOT/"distribution"/"kaggle"/"README.md",out/"README.md")
    subprocess.run(["kaggle","datasets","create","-p",str(out)],check=True)
print("Kaggle synthetic-only dataset publication command completed.")
