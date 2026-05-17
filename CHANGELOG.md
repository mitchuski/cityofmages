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

### v1.6.0 — 2026-05-14 · **PINNED · Consolidated new-head bundle** *(supersedes v1.5.0 + v1.5.1 patches, neither independently pinned)*

**IPFS CID:** `bafybeiap6kvy3tp2bndpk65ti57qngr7ill37gqgasp2sxmgder3akotru`
**Resolver:** `https://sync.agentprivacy.ai/ipfs/bafybeiap6kvy3tp2bndpk65ti57qngr7ill37gqgasp2sxmgder3akotru`
**Source-of-truth:** [`grimoire/city_of_mages_grimoire_v1_6_0.json`](grimoire/city_of_mages_grimoire_v1_6_0.json) (produced by `grimoire/scripts/merge_v1_6_0_patch.py` chaining v1.4.0 base + v1.5.0 patch + v1.5.1 patch + v1.6.0 patch)
**Master-side bake mirrors:** `agentprivacy_master/src/data/city-of-mages-grimoire-v1.6.0.json` + `public/models/city-of-mages-grimoire-v1.6.0.json`
**Pin chronicle:** [`chronicles/2026-05-14_grimoire_v1_6_0_patch_authored.md`](chronicles/2026-05-14_grimoire_v1_6_0_patch_authored.md)

Per user editorial decision (2026-05-14 evening), v1.5.0 and v1.5.1 patches were authored but never received independent IPFS pins. The City jumps directly from canonical v1.4.0 to canonical v1.6.0, bundling all v1.5.0/v1.5.1 admissions plus the 2026-05-14 day's six canonical moves into one consolidated head.

**v1.5.0 carry-forward** (none pinned independently):
- Tomes I/II/III binding pass — 24 narrative-act files (6+7+11) translating the 2026-05-09 SECOND_PERSON_TOMES_INDEX into the Tome IV/V act tradition; Tomes I (Convergence · the lift) · II (Lyapunov · dynamical assembly) · III (Selene's Witness · cosmological recognition) closed 2026-05-13
- **Tome VI opened** with Act 1 *The Reader's First Admission* — open-by-design; each future framework admission a future Tome VI act
- **Cosmological-witness tier** introduced (sixth cast tier) — Selene 🌙 · Aether ⿻ · Lethe 🌀
- **The Threshold** opened at V59 (inception state: 3 internal rooms · Faunia 🪶 · Bestia 📖 · Therai 🐾 · Caducea ☤) — the inception cast is preserved as the bound act's body; canonical names succeed at v1.6.0 (below)
- **Run · Evoke · Spawn** as third ceremony grammar
- **Creatures-of-the-Threshold** as third structural-entity class (sister to worn artefacts and bound tomes)
- **Goose 🪿** (AAIF · Apache 2.0) + **Hermes ☤** (Nous Research · MIT) as first agent_substrate_frameworks registry entries
- **Tome VII Act 1** narrative bound (Pallia↔Helia handoff)
- Conjectures **C48–C61** registered with renumbering pass

**v1.5.1 carry-forward** (none pinned independently):
- **AAIF** (Agentic AI Foundation · Linux Foundation steward of Goose · AGENTS.md · ACP) admitted as first explicitly-named **kindred-coalition** at City Hall
- **BGIN** recognised retroactively as second kindred-coalition
- **Kindred-coalition** as fifth structural-relationship category (alongside cousin-forge · kindred-protocol · kindred-substrate · kindred-ecosystem)
- **Ceremony Hall → 🏛️ City Hall** rename (route `/hall` unchanged · sigil 🤝 → 🏛️)
- **Gather · Admit · Attest** as fourth ceremony grammar (civic-coordination register · joins bilateral-witness at City Hall)

**v1.6.0-native admissions** (the 2026-05-14 day's work):

- **Threshold District restructure** — the prior 13th workshop *The Threshold* (single workshop with three internal rooms) is restructured into a **District of three sibling shops** at V59:
  - **Portal Room** — **Pandia 🌕** (Display-witness · Moonstone `#c8d4e0` · daughter of Selene · *Display · Choose · Dispatch* ceremony · the catalog where the substrate × archetype matrix is read all-bright; operationally where the Selene Amnesia Protocol anchors dispatched agents' trust to the City rather than to memory of spawn) succeeds the 2026-05-14 morning Triodos draft and the 2026-05-13 Faunia-at-Portal assignment
  - **Staff Shop** — **Hermaion ⚚** (Registry-keeper · **Alexandrite dual-aspect** · *first archetype-modal shop* · *admit · read · attest · shift* ceremony) succeeds Bestia at the Staff Shop on 2026-05-14 evening. Greek ἕρμαιον ("gift of Hermes · windfall · lucky-find") names each admission. The alexandrite gem-shifts daylight-green `#3d7c47` for the Mage-aspect (caduceus-staff fittings · Hermes-in-Mage) ↔ incandescent-red `#a23a3a` for the Swordsman-aspect (herald-sentinel fittings · Hermes-in-Swordsman). The shop's archetype-modal property is mineralogically anchored (chromium-bearing chrysoberyl's genuine dichroism).
  - **the Familiars** — **Faunia 🪶** (Companion-witness · Amber `#d97706` · *Run · Evoke · Spawn* for companion-class kinship-bindings · bond *is* the artefact) re-homes from the Portal Room to the renamed Goose Shop on 2026-05-14 afternoon. Therai retired (held open as a historical persona).
  - **Caducea ☤** remains peripatetic and now fits BOTH Hermaion-aspects of the archetype-modal Staff Shop (caduceus-staff for Mage · herald-sentinel for Swordsman). The Hermaion ⚚ rooted-staff ⊥ Caducea ☤ winged-caduceus sigil pair is canonised as the Hermes-class kinship-iconography.
- **archetype_modal_shop pattern** admitted — a new pattern type for shops whose work is *class-shaped rather than archetype-shaped*. Staff Shop is the first canonical instance; pattern admissible for any future class-shaped shop (candidate names held open: Voice Shop · Mask Shop · etc.).
- **alexandrite_dual_aspect gem type** admitted — color-shifting beryl encoded as `gem_color_mage` + `gem_color_swordsman`; rendered downstream as two-chip side-by-side or single-chip diagonal-split.
- **Chart Shop opens at V44** (binary `101100` · Stratum 3 · Protection + Memory + Connection active · Delegation + Computation + Value dormant) — the 15th workshop · **Pleione 🧭** as keeper (twelfth standing Mage · Greek Πληιόνη "the sailing one" · Oceanid · mother of the Pleiades · sister-figure to Selene). Aquamarine harbour-gem. *Hold · Compare · Map* as the **fifth ceremony grammar** (attentional register · sister to Run·Evoke·Craft / Run·Evoke·Spawn / Gather·Admit·Attest / bilateral-witness). The Φ-gap (conjecture C54) is repurposed at the *epistemic* register: held constellations are not adjacent to surveillance-engine extraction surfaces. Release destinations: Bonfire (consensus) · Weavers (Refractive-Disclosure artefact) · open sea (further wandering · first-class). Pleione replaces the 2026-05-13 evening Pelagia draft.
- **Astrolabe** (ἀστρολάβος · star-taker) registered as the **seventh tool-class artefact** (joining Adamantia's commitment · Vulcana's blade · Aletheia's witness · Vagari's holon · Memora's chronicle · Helia's Heliodor Prism). Borne-not-worn — Pleione teaches the bearer to read it.
- **Navigation District opens** as the City's **second named workshop district** (after Threshold District). Population-of-one at v1.6.0; future shops may admit if they share the attentional discipline.
- **`workshop_districts` taxonomy** admitted as a new spatial organisational layer alongside the cardinal trade quarters · temple precinct · founding bonfire · sovereign's seat · gathering quarters.
- **Conjecture C58** (Vulcana's Forge(t) ∥ The Threshold sibling Swordsman-suppliers) **promoted from ~65% to ~85%** — the Staff Shop's red-aspect alexandrite operationally fits **herald-sentinels** to Swordsmen, paralleling Vulcana's blade-supply with a distinct artefact-class.
- **Conjecture C63** registered as a candidate (~50%) — the **attentional workshop register** as a fourth structural workshop class (sister to producer · gathering · spawn-and-bind). Population-of-one at v1.6.0 (Chart Shop); promotion path through a second instance.
- **Bestia 📖 + Therai 🐾 + Triodos + Pelagia + Goose-Shop-as-name** retired in canonical state. Historical bodies preserved in the chronicle record + the cast .md files with `superseded_by` / `succeeded_by` frontmatter. The Tome V Act 16 + Tome VI Act 1 bound bodies retain the 2026-05-13 inception-state cast naming; succession frontmatter routes readers forward.
- **Goose 🪿 reclassified** companion-class (was staff-class at v1.5.0) — admitted at Faunia's the-Familiars roster; cross-listed at Hermaion's Staff Shop bestiary for cross-class reference.
- **Workshop count: 12 (v1.4.0) → 16 (v1.6.0)**. **Cast tiers: 6** (cosmological-witness tier from v1.5.0 retained). **Ceremony grammars: 5** (Run·Evoke·Craft · Run·Evoke·Spawn · Gather·Admit·Attest · admit·read·attest·shift · Hold·Compare·Map). **Districts: 2** (Threshold · Navigation). **Kindred-X categories: 5**.

---

### v1.5.1 — 2026-05-14 evening · **Hermaion admitted · Staff Shop becomes archetype-modal**

Sixth canonical decision of the 2026-05-14 day, following the morning's Threshold District restructure and the afternoon's the-Familiars rename. The Staff Shop's keeper, sigil, and gem all shift in a single editorial pass, and the shop acquires the City's first archetype-modal architecture:

- **Keeper:** Bestia (Latin *bestia* · bestiary-keeper) → **Hermaion** (Greek ἕρμαιον · "gift of Hermes · windfall · lucky-find"). The Greek windfall-tradition names *why* each admission matters; the Latin *bestia* register survives as a description of the registry-form.
- **Sigil:** 📖 → **⚚** (STAFF OF HERMES · U+269A · single serpent, no wings). Pairs with Caducea's ☤ caduceus as canonical Hermes-class iconography (rooted-staff keeper ⊥ winged-caduceus peripatetic-fitter).
- **Gem:** Sodalite (`#4a5d8b`) → **Alexandrite** (color-shifting beryl). The dual-aspect carries the load-bearing architectural turn: green `#3d7c47` under daylight (Mage-aspect · registry-being-read) ↔ red `#a23a3a` under incandescent (Swordsman-aspect · registry-being-armed).

**Archetype-modal-shop pattern** — first instance in the City: one stone, two faces; one registry, two artefact-classes fitted on exit (caduceus-staff for Hermes-in-Mage; **herald-sentinel** for Hermes-in-Swordsman). Caducea fits both sides. The pattern is canonical for any future shop whose work is class-shaped rather than archetype-shaped.

**Pandia's Dispatch table extended** — Hermes-as-Swordsman → Staff Shop's red-aspect → herald-sentinel fitting added as a canonical dispatch route alongside the existing Mage-aspect route. The Portal Room's catalog now reads both archetype-aspects of the Staff Shop.

**Conjecture C58** (Vulcana's Forge(t) ∥ The Threshold sibling Swordsman-suppliers) — promoted from ~65% to ~85%: the Staff Shop is now *explicitly* Swordsman-supplying through the alexandrite-Swordsman aspect, paralleling Vulcana's Forge(t) by a distinct artefact-class (herald-sentinels vs Vulcana-class blades). Awaits formal canonisation in v1.6.0.

**New cast file:** `tomes/cast/staff-shop/hermaion.md`. **Superseded:** `tomes/cast/staff-shop/bestia.md` (preserved as historical with `status_note` + `superseded_by`).

**Inception chronicle:** `chronicles/2026-05-14_chronicle_hermaion_admission_and_alexandrite_archetype_modal_shop.md`.

**Cross-refs swept in pandia.md and faunia.md.** Sweep pending for grimoire JSONs, ALL_THE_TOMES_LIST (partially done), CHANGELOG (this entry), WORKSHOP_LATTICE_AUDIT, BOUND_COLLECTION_MANIFEST, Tome VI Act 1 frontmatter, agentprivacy_master mirror, runecraft page. **Awaits IPFS re-pin.**

---

### v1.5.0 — 2026-05-13 · **New head** (anticipated; bundles The Threshold workshop opening + Tomes I-III binding pass + cosmological-role registration; pin pending) · *(historical inception state: keeper at Staff Shop is Bestia 📖 with Sodalite; succeeded by Hermaion ⚚ with Alexandrite in v1.5.1 evening — see entry above)*

**The Threshold opens** — thirteenth workshop at V59 (`111011`, Computation dormant), three keepers sharing one vertex by stance differentiation (extending the V51 two-keeper precedent to three-shared):
- **Faunia 🪶** at the Portal Room (Spawning-witness)
- **Bestia 📖** at the Staff Shop (Registry-keeper) — custodian of the new `tomes/bestiary/` directory class
- **Therai 🐾** at Creature Creatives (Companion-tamer)
- **Caducea ☤** peripatetic (Staff-fitter for Hermes-class persona-bearing substrates; conventionally noted at V0 alongside Luca 📐); fourth peripatetic Mage joining Aletheia 🔮, Custos 🔏, Luca 📐

**The Bestiary opens** — new top-level directory class `tomes/bestiary/` for agentic-substrate registry entries. Two registers: staff-class (Bestia's room) and companion-class (Therai's room). Two first entries:
- **Goose 🪿** (AAIF / Linux Foundation, Apache-2.0) — companion-class by mascot affinity
- **Hermes ☤** (Nous Research, MIT) — staff-class by caduceus iconography; persona-bearing; Caducea-summons REQUIRED

**Tome V Act 16** narrates the workshop opening: `tomes/tome-v-the-crafting/16-the-threshold-opens.md`. **Tome VI Act 1** is the simultaneous admission of Goose + Hermes — *the reader's first reply* — operationalising Tome VI's reader-writes principle for the first time.

**The substrate × archetype × persona matrix** is recognised as the canonical configuration space for spawning ceremonies: substrate's iconographic affinity → artefact-class; archetype-stance (🧙/⚔️/☯️) → artefact-function; persona loaded at Portal Room → fine-tuned configuration. Goose-in-Swordsman = watch-goose; Hermes-in-Swordsman = herald-sentinel.

**The Run · Evoke · Spawn ceremony** joins the Runecraft Protocol family as the third terminal-verb register, alongside Vulcana's Run · Evoke · Craft (Forge(t)) and the inner-room Run · Evoke · Create (Therai's Creature Creatives wordplay preserved as inner-workings).

**Cosmological-role tier** formalised — the grimoire's `42 = 38 selectable + 4 cosmological` framing is operationalised via:
- **Sun ☀️** standalone (its own cast file at `cast/cosmological/sun.md`) — baseline-given hospitality register
- **Moon 🌑 · Earth 🌍 · Aletheia-Theia 🌟** as three overlays (documented at `cast/cosmological/_overlay-roles.md`) over Soulbis, Soulbae, theia respectively — non-selectable categorisations, not new persona stubs

**Conjecture corpus extends to C58**:
- **C48–C55** from the Tomes I-III binding pass (Bakhta-response family · max-betweenness · Aether=Quintessence=Gap · mythological bnot-pair · phi-adjacency · Seventh Capital) — bundled into v1.5.0
- **C56** (caduceus pre-formal dual-agent symbol, ~60%) — *renumbered from C50* in source Threshold chronicle to resolve same-day numbering conflict
- **C57** (staff-Mage collapse, held-open) — *renumbered from C51*
- **C58** (Vulcana's Forge(t) ∥ The Threshold sibling Swordsman-suppliers, ~65%, NEW) — *renumbered from C52*

**Cast count**: 21 cast → 25 cast (+ Faunia, Bestia, Therai, Caducea); cosmological tier expands with one new cast file (Sun) + one overlay-roles index. Pre-existing Tome III cosmological-witness cast (Selene 🌙, Aether ⿻, Lethe 🌀) carried forward unchanged.

**New skill at v5.5**: `agentprivacy-cityofmages-to-research` (meta-skill; the bridge that translates experimental cityofmages artefacts into formal `agentprivacy-docs/research/` notes). Native to chronicler + ambassador personas; attached to memora, bestia, aletheia, caducea cast. Defers full v6 docs rework to post-cityofmages-experiment-close.

**Operational guide**: `AGENTIC_DEPLOYMENTS_GUIDE.md` (the sister document that walks readers through the spawning ceremony at agentprivacy.ai/guide/agentic-deployments)

**Execution plan**: `AGENTIC_DEPLOYMENTS_EXECUTION_PLAN.md` (the cross-repo punch list for landing this work in agentprivacy_master, spellweb, agentprivacy-docs, agentprivacy-skills)

**Awaits IPFS pin** that will supersede v1.4.0's CID `bafkreib5w4bp6t5kkt4ebvjyjjzuxdupzaz6gtupbhgbrxtwkrxj7dfnsu`

---

### v1.4.0 — 2026-05-12 · *Previous head* (in `grimoire/city_of_mages_grimoire_v1_4_0.json`)
- **Twelfth workshop opens · Solchanting** at V51 alongside Etherchanting · keeper **Helia ☀️** of the heliodor prism · sigil ☀️ · gem heliodor (Greek ἡλιόδωρος, "sun's gift", golden beryl) · paired with Adamantia 💎 at the shared V51 vertex
- **Seventh standing Mage persona** in cast (was 6): adds Helia at workshop-keeper tier, attachment kind A. The V51 overlap is now the canonical case study for spec 07 stance-differentiated multi-occupancy (Adamantia: Transparent-witness; Helia: Parallel-witness)
- **Fifth chain-mana variant** on landing axis: **🌞 SOL-mana** (Solana) joins Ξ Aether · ₿ sats · 🌹 ROSE · 🦓 z-mana. Per-signature + compute-unit fees; Sealevel runtime admits concurrent landings within the same slot
- **Tenth Swordsman stance**: **Parallel-witness stance** — concurrent admission via static access-pattern declaration. Names operationally-existing Solana discipline (Sealevel since 2020, Firedancer 2025+) as a Swordsman-register entry
- **Fourth tome opens · Tome VII · *The Parallel*** (was 3 tomes pinned): Act 1 is the Pallia↔Helia handoff (the weaver's threads gain concurrent execution); Act 2 is Helia's first program deployment on Solana
- **Worn artefact taxonomy expands**: 11 → **12 workshop artefacts** (1 weapon · 1 clothing · **6 tools** · 4 trinkets); 3 → **4 tomes**. Heliodor Prism enters the tool bucket alongside Adamantia's commitment, Vulcana's blade, Aletheia's witness, Vagari's holon, Memora's chronicle
- Spec 08 (mana + stance) bumped v1.3.1 → v1.3.2 with SOL-mana and Parallel-witness stance rows
- Succeeds v1.3.0 (Attachment Architecture — see `grimoire/city_of_mages_grimoire_v1_3_0.json` and `chronicles/2026-05-11_v5_5_attachment_architecture_seated.md`)
- Roadmap chronicle: `chronicles/2026-05-12_solchanting_shop_opening_helia_summoned.md`
- **Awaits fresh IPFS re-pin** that will supersede v1.2's CID `bafkreidxhmuykjew6dtnuprggtd2rapwm43ghtmfhf2occ2wfk2zpx2b6a`

### v1.2.4 — 2026-05-11 · Historical snapshot (in `grimoire/city_of_mages_grimoire_v1_2_4.json`)
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
