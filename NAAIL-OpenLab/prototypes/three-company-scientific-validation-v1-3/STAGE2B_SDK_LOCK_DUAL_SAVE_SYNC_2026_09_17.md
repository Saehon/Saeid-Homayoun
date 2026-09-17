# NAAIL OpenLab™ — Stage 2B SDK Lock Dual-Save Sync

**Date:** 2026-09-17  
**Scientific benchmark:** `REGISTERED_NOT_EXECUTED`  
**Cross-candidate input lock:** `EXECUTED_VALIDATED`  
**SDK provenance verification:** `EXECUTED_VALIDATED`  
**SDK runtime CI validation:** `BLOCKED_CI_RUN_NOT_OBSERVED`  
**Live provider calls:** `BLOCKED_PROVIDER_CREDENTIAL_AND_RUNTIME`  
**Stage 2C:** `LOCKED`

## Pinned SDK state

- `openai==3.14.1`
- `google-genai==2.23.0`
- `anthropic==1.6.0`

Wheel SHA-256 values are preserved in `stage2b_sdk_provenance.csv`.

## GitHub public state

Repository: `Saehon/Saeid-Homayoun`  
Branch: `main`

- pinned requirements: commit `5997d54513191b04aa3a35bb9234dcad999c9278`
- SDK provenance registry: commit `c3220c3b8b27e622ee47e5ae20191d997208ecf3`
- SDK-lock workflow creation: commit `c52d332c9fb527e41873017dafa62be51d1a204d`
- PR-trigger support: commit `2d87779bf7e502ac3a902ec2482cb6bc4ed461fa`
- controlled validation PR #26 merge/squash: `4bbc741e2d0a0bd9bcba87e10f19535ab7a3b290`
- SDK-lock status publication: commit `77b75c68c9b1c64770b53cff06b035e258823757`
- README synchronization: commit `e9447e14329fa3da8faa2a86cdcc9138065cdb58`

The public GitHub Actions query returned zero observable workflow runs after both PR-trigger and merge-trigger attempts. No CI success is claimed.

## Google Drive canonical mirror

Canonical V1.3 folder: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

- `STAGE2B_SDK_LOCK_STATUS_2026_09_17.md`: `1FmvPZT6kzOKPTBCbxJGorsfVto_VCEqC`
- `stage2b_sdk_provenance.csv`: `1jUm4EFlirLrRa-rgx23OfItLoO-f2BsF`
- `requirements-stage2b.txt`: `1ghGLB3WLam6Xfby64PXJ0gz1p3FX8hsd`
- `naail-stage2b-sdk-lock.yml`: `1rY9nrWiSPpMX27SPIjEuDJ8tQPlLnILq`

## Scientific boundary

No provider API call has been made. No candidate response exists. The private V1.3B prompts and gold key remain outside public GitHub. Stage 2C is not eligible to open.

## Next gate

First obtain a successful runtime lock in either GitHub Actions or another independent connected environment using the exact pinned SDKs. Then provision the private C01 credential and execute C01 against the already registered task/evidence hashes. Freeze/hash/verify C01 before executing C02 and C03 on the same hashes.
