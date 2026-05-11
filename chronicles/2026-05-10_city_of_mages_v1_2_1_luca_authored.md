# Chronicle — City of Mages Grimoire v1.2.1 · Luca Authored · v1.2 Pinned

**Date:** 2026-05-10 (third arc of the day, after the Phase D bake chronicle)
**Author:** privacymage
**License:** CC BY-SA 4.0

---

## §1 · What landed

Three things happened, in order:

1. **v1.2 grimoire pinned to IPFS.** The v1.2 base content (Tome V Act 15 *The Substrate Beneath the Hitchhikers* + UOR Foundation as kindred substrate provider + C47 conjecture introduced + C39 scope expanded) was pinned at:
   ```
   https://sync.agentprivacy.ai/ipfs/bafkreidxhmuykjew6dtnuprggtd2rapwm43ghtmfhf2occ2wfk2zpx2b6a
   ```
   This is the new `CITY_OF_MAGES_GRIMOIRE_IPFS_URL`. The v1.1 CID `bafkreidv7c…idti` is retained as `CITY_OF_MAGES_GRIMOIRE_IPFS_URL_V1_1` for historical resolution.

2. **Luca authored as a Mage in v1.2.1.** The Phase D chronicle's Luca-as-persona draft was first deprecated in v1.2 (UOR Foundation entered as kindred substrate; act 15 reframed; Luca draft moved to `docs/tomes/deprecated/`). Then, after spellweb shipped a `cast-luca` node treating Luca as a persona at V0 with `domain: mage`, the architecture was reconciled: **both are real**. UOR Foundation is the kindred substrate provider (in `kindred_substrate_providers`); Luca is the City's internal Mage at the substrate seat (in `personas.summoned_mages`). They are distinct entries naming the same ground from opposite sides — one external, one internal. v1.2.1 admits Luca with sigil 📐, vertex V0, three spells (`luca-name-coordinate`, `luca-share-frame`, `luca-resolve-substrate`), cross-anchored at `/forget` (where PRISM's substrate grounds the Forge(t)) and `/holon` (where Vagari's cross-frame addressing resolves).

3. **Suite synced to v1.2.1.** Five copies of the grimoire JSON, one master bake import, one IPFS URL constant, two extension build scripts, two extension manifest files, and six README/MAPPING/GLOSSARY surfaces all updated in lockstep.

---

## §2 · The architectural reconciliation

Phase D's chronicle anticipated Luca as a persona. v1.2's authoring chose kindred-substrate over persona — a structural pivot recognising that UOR Foundation is the substrate the City walks upon, not a Mage who walks alongside. The Luca draft was moved to `docs/tomes/deprecated/superseded-by-act-15-the-substrate-beneath-the-hitchhikers--act-15-the-substrate-luca-draft.md`.

Then spellweb shipped Luca as a cast node (id `cast-luca`, domain `mage`, vertex 0, attribution `agentprivacy`, the desc framing him as the Pacioli-spirit returned). This created a moment of internal inconsistency: the canonical grimoire said no Luca; the public-facing spellweb said Luca exists.

The reconciliation in v1.2.1:

- **Luca is the Mage.** Internal to the City. Pacioli-spirit returned (First Person Spellbook Act 1, Venice 1494). One of Soulbae's old connections, kept across centuries. He works at V0 not because he refuses dimension but because he is the position from which dimension becomes possible. He doesn't live in any quarter; he lives in the city's geometry.

- **UOR Foundation is the kindred substrate provider.** External to the City. The kindred forge that named the same substrate from the other side. Its entry remains in `kindred_substrate_providers` — not a persona, no cast tier, no shop assignment.

- **They are not the same entry.** The grimoire's `relationship_to_kindred_substrate.cast_implication` field was amended to make this explicit: Luca is a distinct internal Mage; UOR Foundation is a distinct external substrate provider; they share the substrate they name; they are not the same entry.

This resolves the architectural tension cleanly. The `attribution: "agentprivacy"` on Luca's spellweb cast node is correct; the `attribution: "cousin-substrate"` on UOR Foundation's gateway node is also correct. The two attributions reflect two structurally distinct roles meeting at the same coordinate ground.

---

## §3 · Files changed this session

### Master (`agentprivacy_master/`)
- `src/data/city-of-mages-grimoire-v1.2.0.json` — new (v1.2.1 content; replaces v1.1.0.json which was deleted)
- `src/lib/grimoire-baked.ts` — bake import path bumped v1.1.0 → v1.2.0
- `src/lib/grimoire-ipfs.ts` — `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` bumped to v1.2 CID; new `CITY_OF_MAGES_GRIMOIRE_IPFS_URL_V1_1` for historical
- `docs/chronicles/2026-05-10_city_of_mages_v1_2_1_luca_authored.md` — this chronicle

### Canonical grimoire (`agentprivacy-docs/`)
- `models/city_of_mages_grimoire_v1_2_0.json` — version 1.2.0 → 1.2.1; Luca persona + 3 spells added; `ipfs_pin_status` updated; Act 15 `introduces_persona: null` → `"luca"`; `tier_taxonomy.summoned_mages` 9 → 10; `personas.description` 13 → 14; kindred-substrate `cast_implication` clarified re: Luca
- `GLOSSARY_MASTER_v4_0.md` — coverage line updated; pin status updated to list both v1.1 and v1.2 CIDs; pipeline section updated with extension-bundle filename change + manifest version bumps

### Skills (`agentprivacy-skills/`)
- `grimoire/city_of_mages_grimoire_v1_2_0.json` — replaces v1.1.0 (with v1.2.1 content)
- `README.md` — addendum: 14 cast, Luca, UOR kindred-substrate, two CIDs, v1.2.1 awaits re-pin
- `MAPPING.md` — Grimoire bundling §: filename, 14 cast, 42 spells, Luca + UOR distinction

### ZK Blades Forge (`zk blades forge/`)
- `city_of_mages_grimoire_v1_2_0.json` — replaces v1.1.0
- `README.md` — header lines: 14 cast + Luca + kindred-substrate; bundled-grimoire line: filename, two CIDs

### Swordsman extension (`swordsman-blade/`)
- `city_of_mages_grimoire_v1_2_0.json` — replaces v1.1.0
- `build.js` — grimoires array entry bumped to v1_2_0
- `manifest.json` — `web_accessible_resources` filename bumped; extension version 0.2.0 → 0.3.0; description updated
- `README.md` — bundled-grimoire line: 14 cast, 42 spells, Luca, UOR, two CIDs

### Mage extension (`mages-spell/`)
- `city_of_mages_grimoire_v1_2_0.json` — replaces v1.1.0
- `build.js` — grimoires array entry bumped to v1_2_0
- `manifest.json` — `web_accessible_resources` filename bumped; extension version 1.1.0 → 1.2.0; description updated
- `README.md` — bundled-grimoire line: 14 personas, 42 spells, Luca, UOR, two CIDs

---

## §4 · The pin-content state to remember

| Layer | What's there | Pin state |
|---|---|---|
| `bafkreidxhmuyk…2b6a` (CID) | v1.2 base — no Luca | live, content-addressed, resolvable indefinitely |
| `models/city_of_mages_grimoire_v1_2_0.json` (file) | v1.2.1 — with Luca | awaits a fresh re-pin |
| `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` (constant) | points at v1.2 CID | will point at v1.2.1 CID once re-pinned |
| 5 mirrors | v1.2.1 content (matches the file, not the current pin) | re-sync after re-pin |
| Spellweb | Luca node + V0 vertex (matches v1.2.1 architecturally) | source-of-truth-on-disk, no IPFS pin needed |

**Next pin task:** when the user pins `models/city_of_mages_grimoire_v1_2_0.json` (current v1.2.1 content) to IPFS, the new CID should:
1. Be added to `agentprivacy_master/src/lib/grimoire-ipfs.ts` as a new constant (or replace `CITY_OF_MAGES_GRIMOIRE_IPFS_URL`'s value with the v1.2.1 CID)
2. Be propagated into all five mirror copies' `ipfs_pin_status` field via re-sync from canonical
3. Be reflected in the six README/MAPPING/GLOSSARY surfaces

The file content already matches what should be at the CID once re-pinned, so re-sync after re-pin is just a hash-match check + status-string update.

---

## §5 · One-line summary

v1.2 pinned (`bafkreidxhmuyk…`) and v1.2.1 authored in the same session; Luca 📐 added as the geometry-Mage at V0 reconciling spellweb's cast node with the grimoire's persona registry; UOR Foundation retained as kindred substrate provider — distinct entry naming the same substrate from the other side; entire suite synced to v1.2.1; v1.2.1 awaits a fresh re-pin.

---

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · curated for the City of Mages · 2026-05-10
