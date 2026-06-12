# IPFS Pin Note — City of Mages grimoire v1.8.0 (final pass)

> **STATUS: COMPLETED 2026-06-10.** Both pins are live and wired in.
> - City of Mages **v1.8.0** → `bafybeihx7zn3frj6gln4bw5k3pxqnxoyumj42x4ohsjrhmro6q5vndw3ei` (byte-identical to local v1.8.0; verified).
> - Privacymage **v10.4.0** (Lattice-Coherence; Aletheia↔Lethe reseated, C54 follows the number) → `bafybeicvbong6ejbvtnfcgbfdtely75e3cakauthv3u22r3nh6ljxqstsm`.
> - Wired: `model-downloads.ts` (both local + ipfs), `grimoire-ipfs.ts` (active → v10.4), `grimoire-baked.ts` (bakes v1.8.0 + v10.4). App, pins, research, and City now coherent. NFT surfaces untouched.

**Date:** 2026-06-09
**What to pin:** the new **City of Mages grimoire v1.8.0** (persona seats re-seated to MODEL).
**What NOT to pin / NOT touch:** the Zero grimoire (`privacymage-grimoire-v10.x`, unchanged)
and all NFT surfaces (63-edition metadata · `/star` · `/lattice` · City Key).

---

## 1. The file to pin

Canonical, identical in three locations (pin any one — they are byte-identical):

```
agentprivacy_master/src/data/city-of-mages-grimoire-v1.8.0.json     ← source of truth
agentprivacy_master/public/models/city-of-mages-grimoire-v1.8.0.json ← web mirror
cityofmages/grimoire/city_of_mages_grimoire_v1_8_0.json              ← repo copy
```

## 2. Pin it (your gateway — needs your auth, run in this session with `!`)

```
# example via the agentprivacy sync gateway / ipfs CLI
ipfs add --cid-version=1 agentprivacy_master/public/models/city-of-mages-grimoire-v1.8.0.json
# → copy the returned bafybei… CID
```

## 3. After you have the CID — wire it in (two edits)

1. `agentprivacy_master/src/lib/model-downloads.ts` — the `city-of-mages-grimoire-ipfs`
   entry (currently the v1.7.1 pin `bafybeibr35x…ivy4`): add a v1.8.0 entry (or bump it),
   setting `version: 'v1.8.0'` and `...ipfs('<new CID>')`. Keep the v1.7.1 entry as lineage.
2. `agentprivacy_master/src/lib/grimoire-ipfs.ts` — update the City grimoire pin reference
   to the new CID (the bake-mirror comment block).

## 4. Check-in workflow

```
# review what this pass changed (NFT files should NOT appear)
git -C cityofmages status --short
git -C agentprivacy_master status --short
git -C agentprivacy-docs status --short
git -C spellweb status --short

# sanity: confirm no NFT/external surfaces were touched
git -C agentprivacy_master status --short | grep -iE "star|lattice|city-key|63|edition|merge_v1" || echo "clean: no NFT surfaces in diff"

# commit per repo (branch first if you prefer)
#   cityofmages:        chronicle + v1_8_0 grimoire copy + cast fixes
#   agentprivacy_master: v1.8.0 grimoire + repointed imports
#   agentprivacy-docs:  research prose + source-note banner
#   agentprivacy-skills / spellweb: prose re-key
# (agentprivacy_tomes is NOT a git repo — snapshot at _snapshots/agentprivacy_tomes_pre_remap)
```

## 5. Explicitly held (do not pin / do not edit this pass)

- `privacymage-grimoire-v10.x` (Zero spellbook) — CORPUS-encoded, NFT-linked, **unchanged**.
- 63-edition NFT metadata · `/star` · `/lattice` · City Key · `merge_v1_x_x_patch.py` — **frozen**.

*Pin the City. Leave the Zero spellbook on its old shelf. The NFT keeps its vertices.*
