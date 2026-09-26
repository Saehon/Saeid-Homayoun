import gradio as gr

MODEL_ID = "ibm-granite/granite-4.0-h-tiny"
MODEL_URL = f"https://huggingface.co/{MODEL_ID}"
GITHUB_URL = "https://github.com/Saehon/Saeid-Homayoun/tree/main/open-source/ibm-granite"

DESCRIPTION = f"""
# IBM Granite Accounting & Audit Lab

This research Space connects **Saeid Homayoun's GitHub research environment** to the official
IBM Granite open-source model **{MODEL_ID}**.

- Official model: [{MODEL_ID}]({MODEL_URL})
- GitHub integration: [Saehon/Saeid-Homayoun]({GITHUB_URL})
- License: Apache-2.0

The model weights remain hosted by IBM. This Space is an integration and research interface,
not a republished IBM model.

### Example research workflow
SEC / XBRL / IFRS / CAM-KAM / ICFR evidence → Granite → reviewer/falsification → human approval
"""

with gr.Blocks() as demo:
    gr.Markdown(DESCRIPTION)
    task = gr.Dropdown(
        [
            "CAM/KAM analysis",
            "ICFR risk narrative",
            "IFRS evidence-grounded RAG",
            "Financial report extraction",
            "Audit-agent prototyping",
        ],
        value="CAM/KAM analysis",
        label="Research use case",
    )
    text = gr.Textbox(label="Evidence / report excerpt", lines=10)
    gr.Markdown(
        "This lightweight public Space documents the integration. "
        "Run inference from the official IBM model page, Colab/Kaggle, or the GitHub example."
    )
    gr.Button("Open official IBM model", link=MODEL_URL)
    gr.Button("Open GitHub integration", link=GITHUB_URL)

demo.launch()
