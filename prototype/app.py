import os
import streamlit as st
from dotenv import load_dotenv

from econova.engine import EconovaEngine, HumanDecision, make_evidence_passport, passport_json

load_dotenv()

st.set_page_config(page_title="ECONOVA-S™ Prototype", page_icon="📈", layout="wide")

st.title("ECONOVA-S™")
st.subheader("Governed AI Scientific Discovery Prototype — GPT-5.6 Sol")
st.caption(
    "Two permanent cores. GPT-5.6 Sol is a replaceable technology backend; "
    "economic meaning and scientific gates remain fixed."
)

with st.sidebar:
    st.header("Replaceable Technology Core™")
    model = st.text_input("Model", os.getenv("ECONOVA_MODEL", "gpt-5.6-sol"))
    effort = st.selectbox("Reasoning effort", ["medium", "high", "xhigh", "max"], index=1)
    use_web = st.checkbox(
        "Enable OpenAI web search",
        value=False,
        help="Useful for current public literature. A curated FT50/AJG corpus is still preferable for publication.",
    )
    api_key = st.text_input(
        "OpenAI API key",
        value=os.getenv("OPENAI_API_KEY", ""),
        type="password",
        help="Stored only in this app process/session. Prefer environment variables for deployment.",
    )
    st.divider()
    st.markdown("**Stable scientific rule**")
    st.info("AI explores; economics constrains; evidence verifies; humans approve.")

question = st.text_area(
    "Economic / finance research question",
    value="When does firm data capability translate into green innovation, firm value, and social welfare?",
    height=100,
)
context = st.text_area(
    "Optional evidence context",
    placeholder="Paste literature notes, dataset description, construct definitions, or constraints.",
    height=130,
)

run = st.button("Run governed discovery workflow", type="primary", use_container_width=True)

if run:
    if not api_key:
        st.error("Add an OpenAI API key in the sidebar or set OPENAI_API_KEY.")
        st.stop()
    if not question.strip():
        st.error("Enter a research question.")
        st.stop()

    engine = EconovaEngine(
        api_key=api_key,
        model=model.strip(),
        reasoning_effort=effort,
        allow_web_search=use_web,
    )

    try:
        with st.status("Running ECONOVA-S scientific workflow...", expanded=True) as status:
            st.write("1/3 Systems map + Co-Scientist-style hypothesis tournament")
            discovery = engine.discovery(question, context)
            st.write("2/3 ERA-style empirical conversion")
            era = engine.empirical_design(question, discovery.output)
            st.write("3/3 Independent scientific red-team")
            red = engine.red_team(question, discovery.output, era.output)
            status.update(label="AI stages complete — Human Gate required", state="complete")

        st.session_state["econova_run"] = {
            "question": question,
            "context": context,
            "use_web": use_web,
            "stages": [discovery, era, red],
        }
    except Exception as exc:
        st.exception(exc)

if "econova_run" in st.session_state:
    run_data = st.session_state["econova_run"]
    d, e, r = run_data["stages"]

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Hypothesis Tournament", "ERA Empirical Design", "Scientific Red Team", "Human Gate"]
    )
    with tab1:
        st.markdown(d.output)
    with tab2:
        st.markdown(e.output)
    with tab3:
        st.markdown(r.output)
    with tab4:
        st.warning(
            "This prototype has not executed a real-data empirical test. "
            "No scientific-discovery or causal claim is permitted."
        )
        decision = st.selectbox(
            "Human decision",
            ["REVISE", "REJECT", "APPROVE FOR NEXT STAGE"],
            index=0,
        )
        reviewer = st.text_input("Reviewer", value="Saeid Homayoun")
        note = st.text_area("Human review note", value="Proceed only after real-data and identification review.")

        human = HumanDecision(decision=decision, reviewer=reviewer, note=note)
        passport = make_evidence_passport(
            question=run_data["question"],
            context=run_data["context"],
            stages=run_data["stages"],
            human=human,
            web_search_enabled=run_data["use_web"],
        )

        st.json(passport)
        st.download_button(
            "Download Evidence Passport.json",
            passport_json(passport),
            file_name="econova_evidence_passport.json",
            mime="application/json",
            use_container_width=True,
        )

        report = f"""# ECONOVA-S Research Run

## Research question
{run_data["question"]}

## Systems Map & Hypothesis Tournament
{d.output}

## ERA Empirical Design
{e.output}

## Independent Scientific Red Team
{r.output}

## Human Gate
Decision: {decision}
Reviewer: {reviewer}
Note: {note}

**Scientific status:** design-stage only. No empirical discovery claim.
"""
        st.download_button(
            "Download Research Dossier.md",
            report,
            file_name="econova_research_dossier.md",
            mime="text/markdown",
            use_container_width=True,
        )
