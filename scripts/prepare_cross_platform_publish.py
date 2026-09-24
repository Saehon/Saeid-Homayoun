#!/usr/bin/env python3
"""Prepare a public Saehon GitHub project for publication on HF/Kaggle.
GitHub remains source of truth. Tokens are read only from environment variables.
"""
import os, re, subprocess, sys, tempfile
from pathlib import Path

project=sys.argv[1] if len(sys.argv)>1 else "Saeid-Homayoun"
if not re.fullmatch(r"[A-Za-z0-9._-]+",project):
    raise SystemExit("Invalid project name")
root=Path(tempfile.mkdtemp())/project
subprocess.run(["git","clone","--depth","1",f"https://github.com/Saehon/{project}.git",str(root)],check=True)
subprocess.run(["rm","-rf",str(root/".git")],check=True)
print(f"Prepared Saehon/{project} at {root}")
print("Target naming:")
print(f"  Hugging Face: SADHON/{project}")
print(f"  Kaggle title: {project}")
print("Publication requires HF_TOKEN and Kaggle credentials in GitHub Actions secrets.")
