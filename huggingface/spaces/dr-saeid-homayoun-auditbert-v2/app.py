"""Dr. Saeid Homayoun CAM/KAM AuditBERT research demonstration.

This interactive tool intentionally uses the transparent non-ML baseline.
Model fine-tuning and private datasets are NOT deployed.
"""
import gradio as gr
from topic_screening import JURISDICTIONS, screen

EXAMPLES = [
    "Revenue recognition for complex contracts required judgment about variable consideration and performance obligations.",
    "Goodwill impairment required forecasts of cash flows, a discount rate and long-term growth estimates.",
    "Going concern analysis considered liquidity risk, loan covenants, and refinancing options.",
]

def analyze(matter: str, jurisdiction: str):
    try:
        matches = screen(matter, jurisdiction)
    except (TypeError, ValueError) as exc:
        return [], f"**Input validation:** {exc}"
    if not matches:
        return [], ("No keywords matched this illustrative vocabulary. **This is not "
                    "evidence that the CAM/KAM is low risk or immaterial.**")
    data = [
        [x["topic"], x["keyword_hits"], ", ".join(x["matched_terms"]),
         x["illustrative_reference"]] for x in matches
    ]
    primary = matches[0]
    explanation = (
        f"**Highest keyword match:** {primary['topic']} — "
        f"{primary['keyword_hits']} distinct matching expressions. "
        "**This number is not a probability or model confidence.**\n\n"
        f"**Illustrative accounting reference:** {primary['illustrative_reference']}. "
        "Applicability depends on reporting framework, issuer facts and audit period.\n\n"
        "**Required before any research or professional inference:** confirm report year, "
        "issuer, jurisdiction, disclosure source, taxonomy annotation, and reviewer "
        "agreement. No audit procedures or outcomes are inferred by this tool."
    )
    return data, explanation

with gr.Blocks(title="Dr. Saeid Homayoun | AuditBERT CAM–KAM Lab") as demo:
    gr.Markdown(
        "# Dr. Saeid Homayoun — AuditBERT CAM–KAM Research Lab\n"
        "**Independent research software demonstration** | University of Gävle, Sweden\n\n"
        "Explore how an explainable accounting-topic screener maps wording in "
        "Critical Audit Matters (CAMs) and Key Audit Matters (KAMs) to illustrative "
        "accounting areas. **Current method: deterministic lexical matching only. "
        "No trained FinBERT or Llama model is used in this live demonstration.**"
    )
    with gr.Row():
        with gr.Column():
            jurisdiction = gr.Dropdown(
                choices=list(JURISDICTIONS),
                value=JURISDICTIONS[0],
                label="Reporting context (illustrative)"
            )
            matter = gr.Textbox(
                label="Audit matter disclosure",
                placeholder="Paste a public or synthetic CAM/KAM excerpt (no confidential data)",
                lines=7,
                value=EXAMPLES[0],
                max_lines=15,
            )
            submit = gr.Button("Analyze audit matter", variant="primary")
        with gr.Column():
            findings = gr.Dataframe(
                headers=["Accounting area", "Keyword hits", "Evidence terms", "Reference"],
                datatype=["str", "number", "str", "str"],
                label="Transparent topic screening",
                interactive=False,
            )
            interpretation = gr.Markdown(
                "Choose the disclosure and select **Analyze audit matter**."
            )
    submit.click(analyze, inputs=[matter, jurisdiction], outputs=[findings, interpretation])
    gr.Examples(examples=[[x] for x in EXAMPLES], inputs=[matter],
                label="Synthetic examples (for demonstration only)")
    gr.Markdown(
        "---\n**Status and limitations.** This Space is a reproducibility/teaching "
        "demonstrator, not an AI-trained audit model, audit opinion, or compliance "
        "determination. Topic keyword counts are neither validated model metrics "
        "nor audit-quality measures. Do not submit sensitive firm records or "
        "client data to a public demo.\n\n"
        "**Research extensions:** independently trained FinBERT topic classifier "
        "(pending validated data and GPU run); Llama 3.1 8B audit-response "
        "research adapter (pending training and independent auditor evaluation).\n\n"
        "**Code and governance:** "
        "[GitHub V2 project](https://github.com/Saehon/Saeid-Homayoun/tree/"
        "research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2) "
        "· [Code review PR #185](https://github.com/Saehon/Saeid-Homayoun/pull/185) "
        "· [Existing collaborative SSRN paper](https://ssrn.com/abstract=7272139). "
        "The prior paper and Maryam Khosravian's original model repositories "
        "remain separately attributed."
    )

if __name__ == "__main__":
    demo.launch()
