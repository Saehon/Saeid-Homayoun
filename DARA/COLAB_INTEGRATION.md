# DARA Colab Integration — Setup and Verification
## Objective
Verify the approved DARA **dual-spine** workflow without modifying existing project datasets, GitHub research repositories, or paying for cloud AI services.

**[Open Colab notebook](https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/main/DARA/colab/DARA_Integration_Bootstrap.ipynb)**

### Steps
1. Click the notebook link; sign into Google Colab if prompted.
2. Run the notebook from top to bottom and authorize Google Drive mount when required.
3. Authorize Google Cloud separately; verify `gcloud config get-value project` is `third-serenity-428705-g2`.
4. The notebook makes a uniquely named, non-destructive read/write test and report under `MyDrive/DARA_ResearchOS/`.
5. Use Gemini in the Colab sidebar manually; optional Gemini CLI runs in separate Google Cloud Shell (check `gemini --version` there).
6. Return to ChatGPT and ask it to inspect the saved DARA report using its **separately connected** Google Drive app.
7. For future code changes, use GitHub pull requests; open reviewed notebooks in Colab.

### Verification matrix
| Service | How verified |
|---|---|
| GitHub code bridge | Notebook URL loads and public GitHub metadata is reachable |
| Colab runtime | Python execution occurs |
| Google Drive | Drive mount and readback test succeed |
| Google Cloud | ADC authentication exists and project ID matches |
| Gemini in Colab | Manual UI prompt, not automatically verified by Python |
| Gemini CLI | Separate Cloud Shell check, not inherited from Colab |
| BigQuery / Vertex AI | Not enabled or invoked by setup |
| OpenAI API | Not needed; only optional if Colab invokes models |
| ChatGPT ↔ Drive/GitHub | Independent connected apps, not notebook credentials |

No unrelated data movement, service enablement, GitHub push or paid inference occurs. Report empirical success only after observed Colab execution. 
