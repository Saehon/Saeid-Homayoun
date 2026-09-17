# NAAIL OpenLab™ — Stage 2B GitHub / Google Drive Sync Manifest

**Date:** 2026-09-17  
**Stage:** `2B — Independent Blind Model Runs`  
**Scientific execution status:** `REGISTERED_NOT_EXECUTED`  
**Control-package status:** `EXECUTED_VALIDATED` as infrastructure only  
**Phase 2:** open / not promoted

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## GitHub publication verification

Repository: `Saehon/Saeid-Homayoun`  
Visibility: public  
Default branch: `main`  
Directory: `NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

| Artifact | Git blob SHA | Publishing commit |
|---|---|---|
| `STAGE2A_PUBLICATION_MANIFEST_2026_09_17.md` | `d3209c0b780d9197d358dc3da7947775699088d5` | `544e752e64b4a47f8356503f35bc9aad1b087e44` |
| `STAGE2B_INDEPENDENT_MODEL_RUN_GATE_V1_3B.md` | `714b69f8adf2cc5a272e3addec7a7421c3c8f49a` | `5e87c088b71ed7f7e8737177c0731ac7d46f4822` |
| `stage2b_candidate_roster_v1_3b.csv` | `63bd517201f3dce3def7f3bd28fe06625ef7f524` | `3645f0360d897cdb9d534f8bcca4d25174677992` |
| `stage2b_response_freeze_ledger_template_v1_3b.csv` | `5bd3849bdc8d0b90bf50b9356d510783bd4cb4b4` | `9e61d8579d55c6ddf623901a0fb2b005be706c55` |
| synchronized V1.3 `README.md` | `b92952618e8248d84d151d4181c72c69c7c0e44e` | `2424f13b94fdd54adffeb296364c3490d38c6253` |

## Google Drive verification

Canonical V1.3 folder:
`https://drive.google.com/drive/folders/1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

| Drive artifact | File ID | Verified state |
|---|---|---|
| `NAAIL V1.3 — Stage 2A Publication & Dual-Save Manifest` | `1fJdnvpPs9qpUIW5pcCeOU9GwCIUocT3xVXVKUqTf6Hw` | present in canonical V1.3 folder |
| `NAAIL V1.3B — Stage 2B Independent Model Run Gate` | `1rcoGEIo6rmZC6JJ4my1aEpJMzqppYOFcd2OlGi2dusA` | present in canonical V1.3 folder |
| `Prototype V1.3B — Stage 2B Candidate Roster` | `1lkRoWU_-nu5pwn8WFJs-DK43HU3dQIcZaK87WXp1dHY` | readback verified: C01–C03 = `BLOCKED_PROVIDER_ACCESS` |
| `Prototype V1.3B — Stage 2B Response Freeze Ledger` | `1g5DIxLy0ZcNmVIt1KPCDc3HLfTUhpah0QcUYawh_QnY` | readback verified: `NOT_FROZEN` / `REGISTERED_NOT_EXECUTED` |

Private V1.3B prompts and gold key remain isolated in the restricted Drive folder and are not published to GitHub before response freeze.

## Current Stage 2B result

The execution controls are built, published and mirrored. **No independent candidate model has been run.** The registered candidate slots C01–C03 remain unassigned because no separate connected model-inference route is currently available in the active environment.

This condition is recorded as blocked evidence rather than bypassed or replaced by same-session assistant outputs.

## Downstream lock

Until real independent candidate runs are frozen:

- Stage 2B scientific execution remains `REGISTERED_NOT_EXECUTED`;
- Stage 2C blinded scoring must not open the private gold key;
- Stage 2D numeric CVPO remains `NOT_EXECUTED`;
- Stage 2E Phase 2 closure cannot promote benchmark performance;
- WMT/JPM Human Gate remains unchanged;
- Step 20 independent replication remains `REGISTERED_NOT_EXECUTED` for all three companies;
- Phase 3 and Phase 4 are not promoted.

## Next permitted action

Assign at least three genuinely independent candidate model/provider runs, execute the same frozen V1.3B packet under comparable conditions, freeze every raw output/failure record plus SHA-256 and telemetry, and only then open Stage 2C scoring.
