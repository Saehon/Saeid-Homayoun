# DARA — Dual-Spine AI Research Architecture

**A GPT-coordinated research system with two complementary spines.**

- **Google Drive:** Knowledge & Data Spine; vertical project-specific archives and horizontal shared methods/taxonomies.
- **GitHub:** Technology & Code Spine; approved code, Colab notebooks, integration interfaces, PR review and version history.
- **GPT / ChatGPT:** Research intelligence & coordination through **separate existing connectors** to Google Drive and GitHub.
- **Google ecosystem:** Colab, Gemini in Colab, Gemini CLI in Cloud Shell, Google Cloud `third-serenity-428705-g2`, and optional BigQuery/Vertex AI. Service authorization remains separate.

**Do not automatically pool project datasets or route routine Drive access through GitHub.** Preserve existing research folders, permissions and project-specific GitHub write pauses.

## Open DARA

- [▶ **Run DARA setup in Google Colab**](https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/main/DARA/colab/DARA_Integration_Bootstrap.ipynb)
- [Full architecture](ARCHITECTURE.md)
- [Project master index](PROJECT_MASTER_INDEX.md)
- [Colab setup instructions](COLAB_INTEGRATION.md)
- [Canonical DARA Google Drive folder](https://drive.google.com/drive/folders/1OXZ6v1zB0G7wmlGezLCAvm8I4Egr2UPL)

**Important:** GitHub can provide the notebook; it cannot authorize Drive/Cloud on behalf of the user or start unattended Colab execution. `OPENAI_API_KEY` is optional unless Colab itself must call the paid OpenAI API.

**Version:** 1.0 · 2026-10-14.
