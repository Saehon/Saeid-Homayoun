# ACK2007 provenance dossier — SIZE and RGROWTH

Status: `UNREVIEWED`, `DEVELOPMENT_ONLY`, `SCIENTIFIC_HOLD`  
Scope: ORQ-001 and ORQ-002 only  
Rule: this dossier records conflicts and the evidence needed to resolve them. It does not select a reading, reconstruct a variable, or authorize prediction.

## Evidence boundary

The inspected repository records the conflicts in `governance/OPEN_REPAIR_QUEUE.md` and `config/ack2007_variable_status.template.json`. It does not contain a verified copy of the ACK2007 primary publication or an incorporated primary appendix/supplement with a page, table, note, or equation locator for either variable. The full bibliographic identity and exact primary-source locators are therefore `UNKNOWN` in this dossier. PR #76 head `4db589fd9e7dd8968ea4f1f4ab7ba421276129bf` is provenance for the recorded conflict, not primary evidence resolving it.

## SIZE — ORQ-001

| Conflict element | Competing readings recorded in repository | Primary evidence required to resolve it | Exact locator currently available | Still unknown |
| --- | --- | --- | --- | --- |
| Transform and unit | natural logarithm of market value of equity; average market value of equity expressed in USD billions | ACK2007 primary publication, variable-definition table/note or equation that defines SIZE and its unit/transform | `UNKNOWN` — no verified page/table/equation locator is stored | Which reading is authoritative; whether any log or unit conversion is applied |
| Measurement basis | point-in-time market value; average market value | ACK2007 primary publication or incorporated primary appendix, construction rule specifying measurement dates and averaging | `UNKNOWN` | Point-in-time versus average; observation dates; numerator components |
| Averaging window | no verified window; an unspecified multi-period average is implied by one reading | ACK2007 primary publication or incorporated primary appendix, page/table/note defining the start and end dates and frequency | `UNKNOWN` | Window endpoints, annual/quarterly/monthly frequency, fiscal versus calendar alignment |
| Missing observations | no verified treatment | ACK2007 primary publication or incorporated primary appendix, sample-construction or missing-data rule | `UNKNOWN` | Minimum observations, imputation/exclusion rule, denominator, and whether missing years remove a firm from the eligible sample |
| Sample eligibility | no verified rule | ACK2007 primary publication or incorporated primary appendix, sample-selection table and related footnote/text | `UNKNOWN` | Eligibility population, exclusions, timing, and interaction with the missing-year rule |

Decision: no competing reading is selected. `SIZE` remains `QUARANTINED`, `PROVENANCE_CONFLICT`, and non-executable.

## RGROWTH — ORQ-002

| Conflict element | Competing readings recorded in repository | Primary evidence required to resolve it | Exact locator currently available | Still unknown |
| --- | --- | --- | --- | --- |
| Growth window | 2001–2003; 2002–2004 | ACK2007 primary publication, variable-definition table/note or incorporated primary appendix stating the exact observation window | `UNKNOWN` — no verified page/table/equation locator is stored | Which window is authoritative; whether endpoints are inclusive; fiscal versus calendar alignment |
| Raw growth construction | no verified formula is stored | ACK2007 primary publication or incorporated primary appendix, equation or construction note defining the raw growth measure | `UNKNOWN` | Numerator, denominator, compounding, treatment of zero/negative bases, and unit |
| Ranking population | no verified population is stored | ACK2007 primary publication or incorporated primary appendix, sample/ranking rule and related table footnote | `UNKNOWN` | Full sample versus industry/year or other peer group; date at which the ranking population is formed |
| Ranking direction | higher growth may map to higher or lower rank; direction is unresolved | ACK2007 primary publication, coding note/table footnote defining rank direction and endpoints | `UNKNOWN` | Ascending/descending direction, rank scale, tie handling, and boundary convention |
| Missing-data eligibility | no verified rule | ACK2007 primary publication or incorporated primary appendix, sample-construction or missing-data rule | `UNKNOWN` | Required years, imputation/exclusion rule, incomplete-window handling, and whether missing data remove a firm from the ranking population |

Decision: no competing reading is selected. `RGROWTH` remains `QUARANTINED`, `PROVENANCE_CONFLICT`, and non-executable.

## Resolution gate

Neither ORQ item can be closed until all of the following are present and independently reviewable:

1. A verified copy or stable authoritative record of the ACK2007 primary publication, including full bibliographic identity and a content hash or immutable source reference.
2. For each variable, an exact definition locator and an exact construction-rule locator (document plus page/table/note/equation).
3. The complete sample-eligibility and missing-data rule relevant to the variable.
4. A recorded reconciliation explaining why the selected reading prevails over every competing reading.
5. Gate-accepted human approval. A primary locator alone does not promote a variable.

Until that evidence exists, `VariableRegistry.executable("SIZE")` and `VariableRegistry.executable("RGROWTH")` must remain false, `ScientificModel("ACK2007", ...)` must remain `SCIENTIFIC_HOLD`, and prediction must raise `ScientificHoldError`.

## Provenance consulted

- `governance/OPEN_REPAIR_QUEUE.md`, ORQ-001 and ORQ-002.
- `config/ack2007_variable_status.template.json`, generated from the PR #76 ontology at head `4db589fd9e7dd8968ea4f1f4ab7ba421276129bf`.
- `src/lemon_icfr/assurance/science.py`, fail-closed promotion and prediction guard.
- `tests/assurance/test_assurance_core.py::T31_35_Science::test_35_no_bypass_around_scientific_hold`.

These repository records establish the conflict and the HOLD control; they do not resolve either scientific definition.
