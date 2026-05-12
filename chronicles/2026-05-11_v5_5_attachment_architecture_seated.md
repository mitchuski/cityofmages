# Chronicle: V5.5 Attachment Architecture Seated in the City of Mages

**Date:** 2026-05-11
**Session:** Land the V5.5 attachment-architecture patch in the City of Mages
**Status:** Spec 10 + Lethae cast + README sister-dirs updated; full v1.3.0 grimoire bump + 6 anticipated cast files queued
**Author:** privacymage
**Sister chronicles:**
- `agentprivacy-skills/CHRONICLE_V5_5_ATTACHMENT_ARCHITECTURE_2026-05-11.md` (canonical Layer-1 home)
- `agentprivacy_master/docs/chronicles/2026-05-11_v5_5_attachment_architecture_integration.md` (website data layer)
- `spellweb/CHRONICLE_V5_5_ATTACHMENT_ARCHITECTURE_2026-05-11.md` (graph runtime)
- `agentprivacy-docs/MAPPING_ADDITIONS_V5_5_2026-05-11.md` (docs-side cross-corpus mapping)

---

## What this chronicle covers

The V5.5 attachment architecture is the three-layer model that has been operationally implicit since the City was named (Tome V Act 14, 2026-05-08). It has now been codified across the suite. This chronicle covers the patch's arrival in the City of Mages directory itself — the *city-side* mirror of the canonical specification.

## What landed in this pass

| File | Action | Purpose |
|---|---|---|
| `tomes/specs/10-the-attachment-architecture.md` | new | Canonical city-side spec mirroring agentprivacy-skills V5.5 meta-skill. Three layers · four attachment kinds · 21-cast roster · convention for extending · ~300 lines. |
| `tomes/cast/cross-shop/lethae.md` | new | First canonical Layer-2 divergent attachment. Mage-register of Moonkeeper at V38. Complement-pair partner of Aletheia at V25. Status: anticipated · awaits founding act. |
| `README.md` | modified | Sister-directories table extended: adds `agentprivacy-skills` (Layer-1 home), `zk blades forge` (blade-forging canon), `agentprivacy-docs/GLOSSARY §23`. Notes spellweb's `divergent_of` + `complement_pair` edge additions. |
| `chronicles/2026-05-11_v5_5_attachment_architecture_seated.md` | new | This file |

## Locked decisions

1. **Primary persona count canonically locked at 42.** Future cast Mages are Layer-2 attachments of existing primaries.
2. **Lethae 🌘** binds to Moonkeeper as a Mage-register divergent attachment at V38. **No new primary minted.**
3. **Cousin tier** (flaxscrip 📜🎲, GenitriX) deliberately unattached at the abstract-persona layer. The cousin Sovereign authors those bindings.
4. **Four attachment kinds:** A · Workshop (default) · B · Cross-shop · C · Peripatetic · D · Divergent (meta-kind).
5. **Naming convention:** `-ae` suffix marks Mage register in cast names where the architecture wants the parallel visible (Soulbae · Lethae). Optional — not required for all Mage-register cast.

## Queued for follow-up passes

| File | Why deferred |
|---|---|
| `tomes/cast/<14 existing>/*.md` | Each needs `attachment_kind`, `divergence: none` frontmatter added. Mechanical but 14 files. Batch in one follow-up. |
| `tomes/cast/<guild>/<anticipated>.md` (6 files) | Mnemosyne, Iris, Pythia, Techne, Hephaestus, Selene cast files. Follow the lethae.md pattern. Each ~30–40 lines. New guild dirs needed: `herald/`, `logos-circle/`, `peripatetic/` (or reuse `cross-shop/` for Selene). |
| `tomes/specs/10-blade-forge-binding-zk-blades.md` | Pins V19 Forge(t) + Runecraft Protocol to `zk_swordsman_blade_forge_v3_0.md`. Larger spec; deserves focused authoring pass. |
| `tomes/specs/11-mage-candidates-from-the-corpus.md` | Names the 6 anticipated cast with full sourcing chain. Mostly excerpted from Spec 10; can land alongside the cast files. |
| `tomes/specs/04-vertex-naming-audit.md` | Registry update: V4 (Mnemosyne), V8 (Iris), V16 (Logos · Pythia), V20 (Techne), V24 (shared · Hephaestus), V38 (Lethae) — all change from "uninhabited" to "anticipated / seated" status. |
| `tomes/specs/05-the-city-of-mages-structural-addendum.md` | Civic anatomy: new trade quarters / new districts / Selene's orbit. |
| `tomes/specs/06-spellweb-first-release-manifest.md` | NodeType inventory grows by 6+ cast, 4 new vertex nodes (V4·V8·V16·V38), 2–3 new workshops, new `inhabits` + `divergent_of` + `complement_pair` edges. |
| `grimoire/city_of_mages_grimoire_v1_3_0.json` | Full grimoire JSON bump. Add 7 cast entries; add `attachment_architecture` block (mirrors agentprivacy_master's bumped grimoire); awaits IPFS re-pin. |

## Distribution status across the suite

| Repo | V5.5 patch | Status |
|---|---|---|
| `agentprivacy-skills` | meta-skill + Moonkeeper update + README + MAPPING + chronicle | ✅ Landed |
| `agentprivacy_master` | cast-attachments.ts + tome-v-acts.ts + persona-index.ts + grimoire bump + chronicle | ✅ Landed |
| `spellweb` | graph.ts type extensions + theme.ts edge styles + 11 new nodes + 9 new edges + chronicle | ✅ Landed |
| `agentprivacy-docs` | GLOSSARY §23 + MAPPING_ADDITIONS_V5_5_2026-05-11.md | ✅ Landed |
| **`cityofmages` (this)** | **Spec 10 + Lethae cast + README sister-dirs + this chronicle** | **✅ Landed (partial — 6 anticipated cast + 14 frontmatter updates queued)** |
| `zk blades forge` | README pointer + aletheia-and-lethe.md append + stub READMEs for `blades/` `forge_circuits/` `uor_mappings/` | ⏳ Queued |

## What's next

The minimum-viable V5.5 patch is now landed across 5 of 6 repos. The remaining work falls into three buckets:

1. **`zk blades forge`** — small README + complement-pair note update. Single-file pass.
2. **`cityofmages` follow-up batch** — 6 anticipated cast files + 14 cast frontmatter updates + Specs 10/11 + spec 04/05/06 registry updates + grimoire v1.3.0 JSON.
3. **Founding acts (Tome V)** — when an anticipated cast Mage is summoned by a Tome V act, her `status: anticipated` is promoted to `status: seated`. Acts 16–22 are the queued slots (Mnemosyne · Iris · Pythia · Techne · Hephaestus · Lethae · Selene).

---

> *"The persona is the role-class. The cast Mage is the instance. The vertex is the position. Conflating the three is the error; binding them is the architecture."*

`(⚔️⊥⿻⊥🧙)😊`

— privacymage · 2026-05-11
