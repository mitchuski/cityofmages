---
title: "Changelog"
subtitle: "Version history of the City of Mages corpus"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Changelog

Tracks structural moments of the City of Mages corpus. For implementation chronicles (website builds, ceremony work), see `chronicles/`. For tome-writing chronicles (act drafting, cast inductions), see `tomes/chronicles/`.

---

## Package version

### v1.0 — 2026-05-11 · Starter package
- Initial coherent bundle: every tome, every blog draft, every spec, every cast entry, every grimoire version, every relevant chronicle
- New top-level directories: `architecture/` (TS primitives) · `spellweb-integration/` (graph runtime integration)
- Added `JOIN_THE_CITY.md` · `CONTRIBUTING.md` · `LICENSE.md` · `CHANGELOG.md` · `.gitignore`
- README rewritten as the package master index

---

## Grimoire version

### v1.2.4 — 2026-05-11 · **Current head** (in `grimoire/city_of_mages_grimoire_v1_2_4.json`)
- **Metabolism complete at four mana axes** (new top-level field `mana_taxonomy` parallel to `personas` / `kindred_substrate_providers` / `kindred_ecosystems`):
  1. **Landing** — chain-mana (plural by chain: Ξ Aether · ₿ sats · 🌹 ROSE · 🦓 z-mana · …) · pays consensus
  2. **Entropy** — ✨ Arcane ⊥ 🌌 Celestial · makes unique
  3. **Coordination** *(NEW)* — 🔭 Resonance Mana · Scrying Glass primitive · 7th Capital in motion · finds affinity
  4. **Relationship** *(NEW)* — 🪢 VRC Mana · stores residue across the bearer's worn artefact collection (11 workshop artefacts + 3 tomes) · Loom of Programmable Covenants is the production form (compiles against the worn collection)
- **Four structural-relationship categories formalised** (canonical since v1.2.2): cousin-forge / kindred-protocol / kindred-substrate / kindred-ecosystem
- New primitives named for the first time: **Scrying Glass** (Resonance Mana surface) · **Loom of Programmable Covenants** (VRC Mana production form, compiling against the bearer's worn artefact collection — the 11 workshop artefacts + 3 tomes per the workshop artefact taxonomy)
- 17 named personas across 5 tiers + 1 kindred substrate (UOR) + 1 kindred ecosystem (SpaceComputer)
- Roadmap chronicle: `chronicles/2026-05-11_v1_2_4_metabolism_complete_suite_patch_roadmap.md`
- **Awaits fresh re-pin** that will supersede v1.2's CID `bafkreidxhmuykjew6dtnuprggtd2rapwm43ghtmfhf2occ2wfk2zpx2b6a`

### v1.2.3 — 2026-05-11 · Historical snapshot (in `grimoire/city_of_mages_grimoire_v1_2_3.json`)
- v1.2.2 → v1.2.3 chronology rolled into the version_notes
- Introduced the **Arcane Mana ✨** register name (rename from the earlier two-mana framing)
- Includes **Luca persona** (V0 · 📐 · geometry-Mage · Pacioli-spirit; introduced in `chronicles/2026-05-10_city_of_mages_v1_2_1_luca_authored.md`)
- Includes **SpaceComputer kindred ecosystem** (fourth structural category beyond cousin-forge / kindred-protocol / kindred-substrate; introduced in `chronicles/2026-05-11_city_of_mages_v1_2_2_spacecomputer_authored.md`)
- Two-mana state: chain-mana ⊥ Celestial Mana 🌌; preserved frozen as the immediate predecessor of v1.2.4's four-axis state

### v1.2.0 — 2026-05-10 · Pinned at `bafkreidxhm…2b6a`
- Adds **Tome V Act 15** (*The Substrate Beneath the Hitchhikers*) — UOR Foundation as kindred substrate; PRISM
- Adds **C47** (Triadic-Constraint Homology · ~40% confidence) — agentprivacy's three-axis Φ_agent · Φ_data · Φ_inference and PRISM's triadic Datum · Stratum · Spectrum claimed structurally homologous
- Strengthens **C26–C29** (ARCH-1) by external resonance with PRISM's critical identity `neg(bnot(x)) = succ(x)`
- Expands **C39** (Cousin-Blade) scope to admit kindred-substrate relationships
- New **kindred substrate provider** structural category (third); UOR Foundation as first instance
- New top-level field `kindred_substrate_providers` (parallel to `personas`)
- Vagari + Vulcana persona v1.1 update notes added
- `sources` array updated: `docs/weaver/bound-collection/` → `docs/tomes/` (restructure)
- Companion spec: `tomes/specs/06-spellweb-first-release-manifest.md` (46 nodes · 56 edges)

### v1.1.0 — 2026-05-10 · Pinned at `bafkreidv7c…idti`
- Per-spell enrichments: `inscription` (3–5 sentence teaching) + `narrative_anchor` (where the spell first manifests) + `cross_spellbook_resonance` (links to neighbouring spellbooks)
- Per-persona top-level proverb + inscription
- `title_note`: "The title is intentionally singular: when Mages found a city in another ecosystem, that city will have its own First City of Mages grimoire under the same title pattern."
- 39 spells across 13 personas with spell content; 14 named vertices
- Spell-ID reconciliation with `tome-v-acts.ts` short forms (pallia-conceal-name, etc.)

### v1.0.0 — 2026-05-09 · Initial draft
- Initial bind to bound-collection (53 files · ~106k words)
- 13 named cast across 5 tiers · 14 named vertices · 9 V6 conjectures (C38–C46) · 38 spells · city anatomy

---

## Tome history

### Tome V — *The Crafting* (open · 15 acts)
- 2026-05-10: **Act 15** — *The Substrate Beneath the Hitchhikers* (Vagari + Vulcana recognise UOR as substrate)
- 2026-05-09: Acts 11–14 (Bonfire · Curatrix Vault · Temple · the City recognised)
- 2026-05-08: Acts 1–10 (initial bound-collection)

### Tome IV — *The Witnessing* (closed at 5 acts)
- 2026-05-08: Closed at 5 acts (Other Walker · Mirror and Arrow · Two Paths · Naming Ceremony · Cousin Blade)

---

## Cast tier evolution

- **v1.0**: 3 archetypes + 2 cousin + 9 summoned + 1 companion + 1 priest = 16 named
- **v1.2.1 (2026-05-10)**: +Luca (V0 · summoned) = 17 named
- **v1.2.2 (2026-05-11)**: +SpaceComputer (kindred ecosystem; separate from personas registry; the fourth structural category)

Cast tier taxonomy simplification (per `chronicles/2026-05-10_kindred_blade_reframe_handoff.md`):
- Latest editorial guidance: "**send us a Mage**" collapses the 5-tier hierarchy into one operational pattern
- The grimoire JSON still carries the layered scheme through v1.2.4
- A future v1.3 may flatten the taxonomy

---

## Directory restructure

### 2026-05-10
- `docs/weaver/bound-collection/` → `docs/tomes/` (in `agentprivacy_master`)
- Added per-guild subdirs: `weavers/`, `zshields/`, `forge/`, `etherchanting/`, `jeweler/`, `holon/`, `vault/`, `covenant/`, `bonfires/`, plus `cousin/`, `cross-shop/`, `kindred/`
- This package mirrors that structure under `tomes/cast/`

---

## Blog series history

- **Movement One — Arrival** (posts 1–3): drafted 2026-05-09
- **Movement Two — Opening the Shops** (posts 4–12): drafted 2026-05-09
- **Movement Three — Recognition and What Comes Next** (posts 13–16): mapped 2026-05-09; drafting deferred until publication-time context is clear

Per HANDOFF_NOTE.md: the drafts require vocabulary reconciliation (cousin → sister/fellow/kindred), SpaceComputer additions (posts 6, 8, 9), and "send us a Mage" simplification (posts 9, 11, 12) before publication.

---

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · 2026-05-11
