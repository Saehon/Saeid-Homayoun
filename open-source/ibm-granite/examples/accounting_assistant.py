"""Minimal IBM Granite accounting/auditing assistant example.

Loads IBM Granite from Hugging Face at runtime. No model weights are stored in this repository.
"""

from transformers import pipeline

MODEL_ID = "ibm-granite/granite-4.0-h-tiny"

pipe = pipeline(
    "text-generation",
    model=MODEL_ID,
    device_map="auto",
)

messages = [
    {
        "role": "system",
        "content": (
            "You are a research assistant for accounting and auditing. "
            "Separate extracted evidence from interpretation, cite the supplied evidence, "
            "state uncertainty, and never present model output as a final audit judgment."
        ),
    },
    {
        "role": "user",
        "content": (
            "Given an annual-report excerpt, identify potential audit-risk themes, "
            "map them to relevant evidence, and flag what requires human verification."
        ),
    },
]

result = pipe(messages, max_new_tokens=400)
print(result[0]["generated_text"])
