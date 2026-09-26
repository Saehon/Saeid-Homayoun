import json
import streamlit as st

from icfr_engine import ControlInput, review_control, to_json

st.set_page_config(page_title="ICFR Evidence Review Agent", page_icon="🧾", layout="wide")

st.title("ICFR Evidence Review Agent — Prototype V0")
st.caption("Decision support for evidence review. Final ICFR/professional judgment remains human.")

with st.sidebar:
    st.header("Control")
    control_id = st.text_input("Control ID", "REV-01")
    period = st.text_input("Review period", "FY2026")
    objective = st.text_area(
        "Control objective",
        "Revenue reconciliations are prepared and independently reviewed each month."
    )

required = st.text_area(
    "Required evidence — one item per line",
    "reconciliation\nreviewer sign-off\nperiod",
    height=120,
)
evidence = st.text_area(
    "Evidence text",
    "Monthly revenue reconciliation for period FY2026. Reviewer sign-off completed.",
    height=220,
)

if st.button("Review evidence", type="primary"):
    control = ControlInput(
        control_id=control_id,
        objective=objective,
        required_evidence=[x.strip() for x in required.splitlines() if x.strip()],
        evidence_text=evidence,
        period=period,
    )
    result = review_control(control)

    c1, c2, c3 = st.columns(3)
    c1.metric("Coverage", f"{result['primary_review']['coverage']:.0%}")
    c2.metric("Risk triage", result["primary_review"]["risk_triage"])
    c3.metric("Human Gate", result["evidence_passport"]["human_gate"]["decision"])

    st.subheader("Missing evidence")
    missing = result["primary_review"]["missing_requirements"]
    st.write(missing if missing else "No deterministic requirement gap detected.")

    st.subheader("Independent challenge")
    flags = result["independent_challenge"]["flags"]
    st.write(flags if flags else "No deterministic challenge flag.")

    st.subheader("Evidence Passport")
    st.json(result["evidence_passport"])

    st.download_button(
        "Download review JSON",
        data=to_json(result),
        file_name=f"{control_id}_icfr_review.json",
        mime="application/json",
    )
