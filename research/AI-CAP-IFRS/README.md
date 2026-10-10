# AI-CAP-IFRS — AI Capital Expenditure and IFRS Equity Valuation

**Full title:** Artificial Intelligence Capital Expenditure, Earnings–Cash Flow Divergence, and Equity Valuation: Evidence from IFRS Firms

**Category:** Research / Corporate Finance / IFRS / AI Investment & Equity Valuation

**Status:** Academic working project; neither published nor submission-ready.

## Research objective
Examine how equity investors contemporaneously price verifiable AI capital expenditure, accounting earnings–cash-flow divergence, recognized impairments, and risk-specific audit disclosures in IFRS firms.

**IFRS coverage:** IAS 16 (PPE), IAS 38 (development), IAS 36 (impairment), IAS 7 (cash flows). IFRS 18 is a prospective extension effective 2027, not a historical treatment.

## Three testable hypotheses
1. **Cash coverage × AI investment:** Contemporaneous equity valuation of disclosed AI capital investment depends on operating cash-flow coverage, after controlling for fundamental risk and growth opportunities.
2. **Impairment disclosure specificity:** The market reaction around a recognized impairment announcement differs with the specificity of asset- and CGU-level accounting disclosures.
3. **KAM information increment:** Independently informative KAMs moderate how investors interpret the accounting information bundle when AI investment or valuation risk is salient.

Hypotheses are unestimated. No forecasts, fabricated test statistics or claims of causal findings.

## Canonical archive: Google Drive
Google Drive holds the master manuscript, source files, verified results and version history. **Do not replace or duplicate it as the source of truth.**

- [Google Drive project folder](https://drive.google.com/drive/folders/1UZR8Uaj0a9h6oX6vwXgCUVlUKtXOKFPu)
- [Word working manuscript v3](https://docs.google.com/document/d/1CoWOW5IVVWT0wu-ie-vOVjSiR_A9_1H3/edit) (subject to file permissions)
- [Project master index](https://drive.google.com/file/d/1uwr12ZLSH4My7Ts3L03GW3hgVtOl_XIX/view)

## Platform roles
| System | Responsibility | Status |
|---|---|---|
| Google Drive | Canonical data, drafts, evidence, decisions and provenance | Folder and Word confirmed |
| GitHub | Open methods, scripts and reproducibility metadata | This folder / PR |
| Kaggle | Free-data notebooks and nonrestricted benchmarks | [Publication staging](kaggle/README.md); external page not yet created |
| Hugging Face | Licensed NLP model/dataset cards and public-source derived data | [Publication staging](huggingface/README.md); external page not yet created |

## Data
Primary candidate sources: audited IFRS annual reports, [ESEF filings](https://filings.xbrl.org/), listed-company filings, issuer disclosure timestamps, [Kenneth French factors](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html), and [Damodaran industry data](https://pages.stern.nyu.edu/~adamodar/). SRAF/SEC datasets are useful comparisons but primarily relate to US-reporting samples. See [data rules](data/README.md).

**Accounting pilot:** Northern Data AG, audited IFRS financials 2023–2025. Accounting amounts are not market pricing estimates. Verified AI-related monetary amounts must be distinguished from generic corporate investment and AI-related text mentions.

## Research process and governance
- Date every information release and avoid look-ahead leakage.
- Do not infer AI investment from word counts alone.
- Do not upload confidential or nonredistributable datasets to public platforms.
- Replication archives from prior FT50/AJG research are methodological references unless actually executed and documented.
- Researcher approval required before economic interpretations and publication.
- Preserve previous versions and record change history in the Drive master index.

### Project subfolders
[Data](data/README.md) · [Code](code/README.md) · [Kaggle](kaggle/README.md) · [Hugging Face](huggingface/README.md)
