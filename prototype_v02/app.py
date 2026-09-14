import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from econova.engine import EconovaEngine, HumanDecision, make_evidence_passport, passport_json
from econova.evidence import retrieve_evidence
from econova.data_sources import fetch_fama_french_5factor, climate_trace_instructions
from econova.empirical import EmpiricalSpec, run_six_tables, stata_do

load_dotenv()
st.set_page_config(page_title="ECONOVA-S v0.2", page_icon="📈", layout="wide")
st.title("ECONOVA-S™ v0.2")
st.subheader("GPT-5.6 Sol • Real Data • Evidence RAG • Econometrics • Human Gate")
st.caption("Stable Economic Meaning + Living Evidence + Replaceable Technology + Independent Scientific Verification")

with st.sidebar:
    st.header("Replaceable Technology Core™")
    model = st.text_input("Model", os.getenv("ECONOVA_MODEL","gpt-5.6-sol"))
    effort = st.selectbox("Reasoning",["medium","high","xhigh","max"],index=1)
    web = st.checkbox("Enable web search",False)
    vector_store = st.text_input("Optional licensed evidence vector-store ID", os.getenv("ECONOVA_VECTOR_STORE_ID",""))
    api_key = st.text_input("OpenAI API key", os.getenv("OPENAI_API_KEY",""), type="password")
    st.info("GPT-5.6 Sol is replaceable. It cannot alter the scientific gates.")

tab_design, tab_evidence, tab_data, tab_empirical = st.tabs([
    "1. Scientific Design","2. Evidence RAG","3. Real Data Lab","4. Six-Table Econometrics"
])

with tab_evidence:
    st.markdown("### Controlled Evidence Registry")
    q = st.text_input("Evidence query","data economy AI green innovation finance welfare")
    cards = retrieve_evidence(q, top_k=6)
    st.dataframe(pd.DataFrame(cards)[["year","authors","title","journal","doi","evidence_role"]], use_container_width=True)
    st.caption("Registry stores verified metadata and roles, not copyrighted article text.")

with tab_design:
    question = st.text_area("Research question",
        "When does firm data capability translate into green innovation, firm value, and social welfare?")
    context = st.text_area("Context / constructs / dataset notes")
    if st.button("Run governed GPT-5.6 Sol design", type="primary"):
        if not api_key:
            st.error("Provide OPENAI_API_KEY.")
        else:
            eng = EconovaEngine(api_key,model,effort,web,vector_store or None)
            with st.status("Running hypothesis → ERA → red team...", expanded=True):
                cards, stages = eng.run_design(question,context)
            st.session_state["design"] = (question,context,cards,stages)
    if "design" in st.session_state:
        question,context,cards,stages = st.session_state["design"]
        for stage in stages:
            with st.expander(stage.name, expanded=stage.name=="hypothesis_tournament"):
                st.markdown(stage.output)

with tab_data:
    st.markdown("### Real Data Lab")
    source = st.radio("Source",[
        "Fama–French 5 Factors (official live fetch)",
        "Upload firm-year / market CSV",
        "Climate TRACE export CSV"
    ])
    if source.startswith("Fama"):
        if st.button("Fetch official Fama–French data"):
            try:
                df = fetch_fama_french_5factor()
                st.session_state["data_df"] = df
                st.session_state["data_manifest"] = {
                    "real_data":True,
                    "source":"Kenneth French Data Library — Fama/French 5 Factors (2x3)",
                    "url":"https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html",
                    "rows":len(df),
                    "provenance_note":"Fetched at runtime from official Data Library."
                }
            except Exception as e:
                st.error(f"Fetch failed in this runtime: {e}")
                st.info("Upload an official export instead; the empirical engine is unchanged.")
    else:
        up = st.file_uploader("Upload CSV", type=["csv"])
        if up:
            df = pd.read_csv(up)
            st.session_state["data_df"] = df
            st.session_state["data_manifest"] = {
                "real_data":True,
                "source":"Climate TRACE user export" if "Climate" in source else "User-supplied verified CSV",
                "url":"https://climatetrace.org/data" if "Climate" in source else None,
                "rows":len(df),
                "provenance_note":"Preserve original source/download and license information."
            }
            if "Climate" in source:
                st.json(climate_trace_instructions())
    if "data_df" in st.session_state:
        st.dataframe(st.session_state["data_df"].head(20), use_container_width=True)
        st.json(st.session_state.get("data_manifest",{}))

with tab_empirical:
    st.markdown("### Six-Table Empirical Runner")
    if "data_df" not in st.session_state:
        st.info("Load data in the Real Data Lab first.")
    else:
        df = st.session_state["data_df"]
        cols = list(df.columns)
        numeric = list(df.select_dtypes(include="number").columns)
        outcome = st.selectbox("Outcome", numeric or cols)
        key_x = st.selectbox("Key X", [c for c in numeric if c != outcome] or cols)
        controls = st.multiselect("Controls",[c for c in numeric if c not in {outcome,key_x}])
        entity = st.selectbox("Entity FE",["(none)"]+cols)
        time = st.selectbox("Time FE / OOS field",["(none)"]+cols)
        cluster = st.selectbox("Cluster",["(none)"]+cols)
        if st.button("Run Tables 1–6"):
            spec = EmpiricalSpec(
                outcome,key_x,controls,
                None if entity=="(none)" else entity,
                None if time=="(none)" else time,
                None if cluster=="(none)" else cluster
            )
            try:
                tables = run_six_tables(df,spec,None if time=="(none)" else time)
                st.session_state["tables"] = tables
                st.session_state["spec"] = spec
                for name,t in tables.items():
                    st.markdown(f"#### {name}")
                    st.dataframe(t,use_container_width=True)
                    st.download_button(
                        f"Download {name}.csv",
                        t.to_csv(index=False),
                        f"{name}.csv",
                        "text/csv",
                        key=name
                    )
                st.download_button("Download Stata .do",stata_do(spec),"econova_analysis.do","text/plain")
            except Exception as e:
                st.exception(e)

st.divider()
st.markdown("### Evidence Passport™ + Human Gate")
if "design" in st.session_state:
    question,context,cards,stages = st.session_state["design"]
    decision = st.selectbox("Human decision",["REVISE","REJECT","APPROVE FOR NEXT STAGE"])
    reviewer = st.text_input("Reviewer","Saeid Homayoun")
    note = st.text_area("Review note","No discovery claim; proceed only after all scientific gates are evidenced.")
    empirical_manifest = {
        "construct_validation":False,
        "credible_identification":False,
        "replication_or_oos": bool("tables" in st.session_state),
        "economic_significance":False,
        "welfare_validation":False
    }
    passport = make_evidence_passport(
        question,context,cards,stages,HumanDecision(decision,reviewer,note),
        st.session_state.get("data_manifest",{}),empirical_manifest
    )
    st.json(passport)
    st.download_button(
        "Download Evidence Passport",
        passport_json(passport),
        "econova_evidence_passport_v02.json",
        "application/json"
    )
else:
    st.caption("Run the Scientific Design to activate the Human Gate.")
