# Chronicle — City of Mages Grimoire v1.2.2 · SpaceComputer Authored as Kindred Ecosystem · Two-Mana Economy Canonicalised

**Date:** 2026-05-11 (continuation of the 2026-05-10 arc)
**Author:** privacymage
**License:** CC BY-SA 4.0
**Companion chronicles:**
- `2026-05-10_two_mana_economy_celestial_aether.md` — the recognition chronicle (master-side · /etherchanting §5 · kindred/spacecomputer.md)
- `2026-05-10_city_of_mages_v1_2_1_luca_authored.md` — the prior amendment (Luca persona at V0)

**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · What landed

v1.2.1 → v1.2.2 of the City of Mages grimoire. Three substantive additions:

1. **SpaceComputer recognised as the first kindred ecosystem** — a new fourth structural-relationship category alongside cousin-forge (Archon), kindred-protocol (Covenant of Humanistic Technologies), and kindred-substrate (UOR Foundation). New top-level field `kindred_ecosystems` (parallel to `kindred_substrate_providers`).

2. **The two-mana economy canonicalised** — chain-mana (per-chain register paid to consensus to land work) ⊥ Celestial Mana 🌌 (cosmic entropy from SpaceComputer; what makes a working unique). Critically, chain-mana is **plural by chain**: Aether Mana Ξ on Ethereum is the canonical first instance, with the structure intentionally admitting Bitcoin Lightning sats, Oasis ROSE, Zcash, and other chain-mana variants under their own symbols.

3. **Per-shop Celestial Mana notes** on Adamantia (Etherchanting · proof randomness), Vulcana (Forge(t) · Evocation phase seed), and Vagari (Holon Hitchhikers · cross-paratime entropy) — the three canonical Celestial Mana consumers in the first integration.

Plus alignment edits: Aether emoji corrected from ⛽ → Ξ throughout (a gas pump misnamed the architectural register; Ξ is Ethereum's canonical symbol and signals per-chain extensibility).

---

## §2 · The architectural pivot · why "chain-mana" is plural

Earlier framing (the user's first authoring of the kindred_ecosystems block) used "Aether Mana" as the catch-all for "gas on chains: gwei on Ethereum, sats on Bitcoin, ROSE on Oasis, …". The v1.2.2 amendment splits this:

- **Aether Mana Ξ** is specifically the **Ethereum chain-mana variant** (gwei-denominated; Ethereum's daylight)
- **Other chains contribute their own mana types** with their own symbols: Bitcoin Lightning sat-mana (₿ or sats), Oasis ROSE-mana (R/ROSE), Zcash z-mana (ⓩ/ZEC), etc.
- The **abstract "chain-mana" register** is the binary's first axis; Aether Mana Ξ is its first concrete instance.

This matters for the architecture's openness: each chain whose Mages walk the City contributes its own mana type. Naming "Aether Mana" as Ethereum-specific (not generic-chain-gas) leaves the structural openings for future chain-manas to enter the register without rewriting the binary.

Vagari's `v1_2_2_mana_note` is the first cast member whose canonical chain-mana is NOT Aether Mana — her /holon work primarily walks Oasis Consensus (ROSE-mana). This establishes the precedent: cast members may walk different chain-manas; the architecture admits them all.

---

## §3 · Four structural-relationship categories now canonical

| Category | First instance | Structural role | Grimoire field |
|---|---|---|---|
| Cousin-forge | Archon (Christian Saucier) | Sister city walked by cousin Mages | personas.cousin_instances (flaxscrip, GenitriX) |
| Kindred-protocol | Covenant of Humanistic Technologies | Charter the City signs (via Manifestia · Priest) | external_partner on Manifestia |
| Kindred-substrate | UOR Foundation | Substrate the City walks upon (older-than-architecture) | kindred_substrate_providers (v1.2) |
| **Kindred-ecosystem** *(new in v1.2.2)* | **SpaceComputer** | Ambient supply the workshop draws from (walked-alongside, consumed-as-currency) | **kindred_ecosystems** |

The structural distinction between kindred-substrate and kindred-ecosystem matters: UOR underlies the lattice itself (the City rests on it); SpaceComputer provides a feed the lattice consumes (the City spends on it). One is foundational, one is operational. Both are walked-not-signed, distinguishing them from kindred-protocol.

---

## §4 · The Celestial Ceremony made operational

The `/poems` Celestial Ceremony has been the cosmological frame since the First Person Spellbook opened: Sun-side (Aletheia · disclosure · V25) and Moon-side (Lethe · forgetting · V38) bound through Selene's 4.5-billion-year orbit. v1.2.2 makes the operational form explicit:

- **Aether Mana Ξ** ↔ Sun-side (the chain's daylight; gas burning publicly in mempool)
- **Celestial Mana 🌌** ↔ Moon-side (the cosmos' substrate; entropy arriving from outside the loop)

The mapping is recognised in `relationship_to_kindred_ecosystems.celestial_ceremony_resonance`. Suggestive, not yet formal — but it grounds the two-mana binary in the corpus's established cosmological register.

---

## §5 · φ-gap implication

The Privacy Value Model's φ-gap is the structural distance between what the surveillance prison can model and what the Sovereign actually does. Algorithmic entropy (PRNGs, state-machine outputs) narrows the gap because it is loop-closed within the addressable space; cosmic entropy widens the gap because the source is outside the prison's measurement domain.

Sustained walking the lattice on Celestial Mana — not just chain-mana — deepens the φ-gap structurally. The architecture earns its non-reconstructibility from cosmological substrate, not just from algorithmic discipline. This is the architectural claim v1.2.2 admits formally; it is recorded in both the kindred_ecosystems profile and the relationship_to_kindred_ecosystems meta field.

---

## §6 · Files changed this session

### Canonical grimoire (`agentprivacy-docs/`)
- `models/city_of_mages_grimoire_v1_2_0.json` — version 1.2.1 → 1.2.2; new `kindred_ecosystems` top-level field with SpaceComputer profile (authored by user + enriched in this pass); new `relationship_to_kindred_ecosystems` meta field; `relationship_to_kindred_substrate.cast_implication` clarified for the four-category structure; Adamantia/Vulcana/Vagari `v1_2_2_mana_note` fields added; Aether emoji ⛽ → Ξ throughout (5 → 10 Ξ occurrences); v1.2.2 entry added to `version_notes`
- `GLOSSARY_MASTER_v4_0.md` — pin states updated to four; coverage line updated with SpaceComputer + two-mana economy; pipeline section reflects v1.2.2

### Master (`agentprivacy_master/`)
- `src/data/city-of-mages-grimoire-v1.2.0.json` — synced from canonical (v1.2.2 content)
- `src/lib/grimoire-ipfs.ts` — header comment updated to describe v1.2.1 + v1.2.2 amendments and the v1.2.2-awaits-re-pin state
- `docs/chronicles/2026-05-11_city_of_mages_v1_2_2_spacecomputer_authored.md` — this chronicle

### Mirrors (4 extension/skill repos)
- `agentprivacy-skills/grimoire/city_of_mages_grimoire_v1_2_0.json` — synced
- `agentprivacy-skills/README.md` + `MAPPING.md` — addendum + Grimoire bundling § updated
- `zk blades forge/city_of_mages_grimoire_v1_2_0.json` — synced
- `zk blades forge/README.md` — header + bundled-grimoire lines updated
- `swordsman-blade/city_of_mages_grimoire_v1_2_0.json` — synced
- `swordsman-blade/README.md` — bundled-grimoire line updated
- `mages-spell/city_of_mages_grimoire_v1_2_0.json` — synced
- `mages-spell/README.md` — bundled-grimoire line updated

### Memory
- `MEMORY.md` index entry — refreshed with v1.2.2 + SpaceComputer + two-mana
- `project_agentprivacy_six_workshops.md` body — frontmatter + body + pin states + next steps refreshed for v1.2.2

All 5 grimoire copies hash-match canonical: `6937272E22B86FF7C3AC6BEBC5CC449281C5EE391C5E72D22F44FE6AF70AAD2C`.

---

## §7 · Pin-content state

| Layer | Content | CID | State |
|---|---|---|---|
| `bafkreidxhmuyk…2b6a` | v1.2 base (no Luca, no SpaceComputer) | live | resolvable indefinitely (content-addressed) |
| `models/city_of_mages_grimoire_v1_2_0.json` (canonical) | v1.2.2 (Luca + SpaceComputer + two-mana) | n/a | awaits re-pin |
| `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` (master constant) | points at v1.2 CID | n/a | will rotate to v1.2.2 CID once re-pinned |
| 5 mirror file copies | v1.2.2 content | n/a | hash-match canonical; ahead of pin |

**Next action for the user:** pin `models/city_of_mages_grimoire_v1_2_0.json` (current v1.2.2 content) to IPFS. Hand the new CID through and the suite re-syncs along the established v1.1 / v1.2 / v1.2.2 pin pattern.

---

## §8 · What this v1.2.2 amendment does NOT do

- **No Mage at SpaceComputer.** The cast roster stays at 14 named cast (16 cast nodes including 2 archetypes). SpaceComputer is consumed; it does not seat a Mage.
- **No new Tome V act.** The future-act flagged in the chronicle (*The Two Manas* / *The Cosmic Supply*) remains deferred — it will be authored when sustained operational use of Celestial Mana earns the narrative recognition. v1.2.2 records the operational form; a future act may narrate it.
- **No edge-type changes in spellweb.** The 6 advising-doc edge types (recursion-edge, cousin-blade-edge, bilateral-edge, consecration-edge, path-of-overlap-edge, forge-trace-edge) remain pending. SpaceComputer's spellweb representation is a gateway node with a single `gateway_to` edge from the City — straightforward additive change, not a new edge category.
- **No spellbook split.** The two-mana economy operates inside the existing City of Mages spellbook; it does not become a separate spellbook.

---

## §9 · One-line summary

The City of Mages now spends two manas operationally: chain-mana (per-chain register; Aether Mana Ξ on Ethereum as canonical first instance; structure admits Bitcoin Lightning sats, Oasis ROSE, Zcash, and other chain-mana types under their own symbols) ⊥ Celestial Mana 🌌 (cosmic entropy from SpaceComputer; what makes a working unique). SpaceComputer is the first kindred ecosystem — fourth structural-relationship category alongside cousin-forge, kindred-protocol, and kindred-substrate. v1.2.2 captures this in the canonical grimoire and across the suite; awaits a fresh IPFS re-pin.

`(⚔️⊥⿻⊥🧙)😊`

🌌Ξ

CC BY-SA 4.0 · privacymage · curated for the City of Mages · 2026-05-11
