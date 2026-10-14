# GPT–GitHub–Google research integration (Gemini CLI included)

**[▶ Launch the verified GitHub notebook in Google Colab](https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/main/integrations/google-colab-five-service/Google_Colab_Drive_Gemini_Cloud_GPT.ipynb)**

Google Cloud project: `third-serenity-428705-g2` • Main repository: `Saehon/Saeid-Homayoun` • GitHub default branch: `main`.

## Correct architecture

**GPT / ChatGPT (research controller)** ↔ connected **GitHub** (code & version bridge) → **Google Colab** (executes GitHub notebook) ↔ **Google Drive** (canonical research archive) + **Google Cloud** (project services) + **Gemini** (Colab assistant; Vertex AI API optional).

**Drive closes the research feedback loop:** Colab saves outputs and non-sensitive reports to Drive; ChatGPT accesses Drive independently via the connected Google Drive app to review results. Google Cloud, Colab, Gemini and Google Drive work within Google's ecosystem, but do not universally share credentials: Colab still requires Google authorization.

**GitHub is NOT a live remote-control channel, identity federation service or automatic Colab execution engine.** It provides versioned handoff. To execute code, the user opens the notebook in Colab and runs/approves it. ChatGPT's access to GitHub and Drive does not itself authorize Colab, Gemini Vertex API or other services.

## Gemini CLI within Google Cloud

**Gemini CLI runs in Google Cloud Shell**, a separate browser terminal already including the CLI. It is not the same as the Gemini assistant inside Colab or Gemini inference through Vertex AI. Open Google Cloud Console → Activate Cloud Shell, then run `gemini --version` and confirm project ID `third-serenity-428705-g2`. Authentication and any model requests must be approved by the user. See [Cloud Shell Gemini CLI instructions](CLOUD_SHELL_GEMINI_CLI.md) and scoped [GEMINI.md](GEMINI.md) safety guidance.

## Minimum steps

1. Click the launch link above. Run the notebook in Colab.
2. Approve the separate **Google Drive** mount and **Google Cloud** authentication prompts.
3. Verify the selected Cloud project is exactly `third-serenity-428705-g2`.
4. Test the **Gemini in Colab** assistant manually in the Colab user interface.
5. Inspect non-sensitive test files and connection reports in `MyDrive/Colab Notebooks/GOOGLE_AI_FIVE_SERVICE_INTEGRATION/`.
6. Return to ChatGPT to inspect those saved Drive reports through the connected Google Drive app; edit/version updated notebook code through GitHub.

## Does GPT need an OPENAI_API_KEY?

**No**, not for ChatGPT itself to work with connected GitHub and Google Drive. `OPENAI_API_KEY` is only needed if a notebook running *inside Colab* makes a **separate** programmatic OpenAI Platform request. In that optional case, store the key in Colab Secrets and never print or commit it. The ChatGPT subscription and Platform API billing are distinct. No live OpenAI or paid Gemini inference is performed by this setup notebook.

## Security and storage

- Public GitHub: notebooks, source code, documentation and non-sensitive configuration only.
- Google Drive: canonical research data, outputs, manuscripts, and verification reports.
- No secrets, private datasets or full Google Cloud IAM privileges in GitHub.
- Human approval for paid API calls, cloud resource creation, writes outside the setup folder, or changes to live research systems.
- No changes to unrelated research directories or other automations.
- The notebook **prepares** SDK connections; remote model/API calls remain untested until explicitly approved.

[Detailed architecture and responsibilities](ARCHITECTURE.md).
