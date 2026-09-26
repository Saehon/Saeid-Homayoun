# Prototype V0

Run locally:

```bash
cd ICFR-Evidence-Review-Agent/prototype
python -m venv .venv
# activate the environment
pip install -r requirements.txt
streamlit run app.py
```

Run tests:

```bash
pytest -q
```

V0 is deliberately deterministic and auditable. The next increment adds a GPT provider behind the same review contract; the deterministic layer remains mandatory.
