# Chronicle: Grimoire v1.6.0 Patch Authored · Consolidated New-Head Bundle

**Date:** 2026-05-14 (late evening · pickup #1 from `2026-05-15_pickup_notes_post_hermaion_day.md` §2)
**Status:** Structured-delta patch authored at `grimoire/city_of_mages_grimoire_v1_6_0_patch.json` · **PENDING** user authoring-pass merge + IPFS re-pin
**Predecessor on disk:** `grimoire/city_of_mages_grimoire_v1_5_0_patch.json` + `v1_5_1_patch.json` (both authored 2026-05-13 · NEITHER PINNED · bundled forward into v1.6.0 per user editorial decision)
**Canonical base:** `grimoire/city_of_mages_grimoire_v1_4_0.json` (CID `bafkreib5w4bp6t5kkt4ebvjyjjzuxdupzaz6gtupbhgbrxtwkrxj7dfnsu` · pinned 2026-05-12)
**Authoring directive (recapped):** pickup-notes §2 Pickup #1 — *"Decision already locked: new `v1_6_0_patch.json` head (not a sub-patch · supersedes v1.5.0 candidate + v1.5.0 patch + v1.5.1 City Hall+AAIF patch)"*
**Author:** privacymage (City of Mages corpus authoring · Soulbae 🧙)
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §0 · TL;DR

The grimoire's next canonical pin will be **v1.6.0** (skipping v1.5.0 and v1.5.1 as standalone pins). The v1.6.0 patch JSON bundles:

- **v1.5.0 carry-forward** — Tomes I/II/III binding pass · Tome VI opening · cosmological-witness tier · Run·Evoke·Spawn grammar · creatures-of-the-Threshold third entity class · Goose + Hermes registry · Tome VII Act 1 bound · C48-C61 conjectures
- **v1.5.1 carry-forward** — AAIF + BGIN kindred-coalitions · fifth structural-relationship category · /hall renamed Ceremony Hall → City Hall · Gather·Admit·Attest grammar
- **v1.6.0 native** — Threshold District restructure (3 sibling shops · Pandia · Hermaion · Faunia-re-homed · Therai retired · Caducea cross-aspect) · archetype-modal-shop pattern · alexandrite_dual_aspect gem · Chart Shop opens at V44 (Pleione · Aquamarine · Hold-witness) · Navigation District opens · workshop_districts taxonomy · C58 promoted to ~85% · C63 candidate (attentional register)

**Patch file:** `grimoire/city_of_mages_grimoire_v1_6_0_patch.json` · 20 top-level sections · JSON-validated.

**What's next (user action):** author the merge script (`grimoire/scripts/merge_v1_6_0_patch.py`) modelled on the v1.5.0 script, produce the head JSON, pin to IPFS, update `agentprivacy_master/src/lib/grimoire-ipfs.ts`.

---

## §1 · Why a new-head bundle (not a chained merge)

The pickup notes at §2 Pickup #1 recorded the user's editorial decision before the patch was authored:

> *"new `v1_6_0_patch.json` head (not a sub-patch · supersedes v1.5.0 candidate + v1.5.0 patch + v1.5.1 City Hall+AAIF patch)"*

The reasoning preserved in the patch's `patch_metadata.supersession_note`:

> v1.5.0 and v1.5.1 never received IPFS pins. The City of Mages corpus jumps directly from canonical v1.4.0 to canonical v1.6.0, bundling all v1.5.0/v1.5.1 admissions plus the 2026-05-14 Threshold District + archetype-modal-shop + Chart Shop work into one consolidated head. This avoids three sequential pin events for a single coherent narrative arc and reduces the risk of a partial pin diverging from canonical state.

The earlier `city_of_mages_grimoire_v1_5_0_candidate.json` (the working merge output from the v1.5.0 patch script) is retained as historical working state and is **not** the canonical merge base for v1.6.0. The canonical merge base is `v1.4.0`.

---

## §2 · What landed in the patch JSON

### §2.1 · Section list (20 top-level keys)

| Section | Source | Notes |
|---|---|---|
| `$comment` | — | Header documenting the new-head decision |
| `patch_metadata` | — | base_version 1.4.0 · target_version 1.6.0 · supersedes list · 15 canonical chronicles cited |
| `top_level_replacements` | v1.5.0+v1.5.1+v1.6.0 | Comprehensive `v1_6_0_note` admits all three patches' content in one prose block |
| `$consolidation_index` | v1.6.0 native | Reader's index of what carries from v1.5.0 / v1.5.1 / what's v1.6.0-native |
| `attachment_architecture` | v1.5.0 + v1.6.0 | cast_attachments_v1_3_0_additions array: faunia (Companion-witness at the Familiars · re-homed) · bestia (superseded) · therai (retired) · caducea (archetype-modal-fitter amended) · pandia · hermaion · pleione · selene-cosmological (lineage extended) · aether · lethe |
| `personas_additions` | v1.5.0 + v1.6.0 | workshop_keepers (faunia v1.6.0 amendment · bestia/therai legacy · pandia · hermaion · pleione) · cross_shop (caducea v1.6.0 amendment) · cosmological_witnesses (carried) |
| `spells_additions` | v1.5.0 + v1.6.0 | pandia/hermaion/pleione native (3+4+3 spells) · faunia v1.6.0 amendment (spawn-familiar · bind-by-kinship · witness-the-walk) · v1.5.0 carry-forward note |
| `spellbooks_tomes_additions` | v1.5.0 reference | tome-i/ii/iii/vi carried by reference (the v1.5.0 patch holds the full content) |
| `tome_v_additions` | v1.5.0 + v1.6.0 | Act 16 (Threshold · v1.5.0) with v1.6.0 `keeper_succession` + `canonical_keepers_now` fields · Act 17 (Chart Shop · v1.6.0 NEW · Pleione) |
| `tome_vii_additions` | v1.5.0 | Act 1 binding update carried |
| `vertex_inventory_additions` | v1.5.0 + v1.5.1 + v1.6.0 | V15 amendment (City Hall) · V38 (Lethe) · V44 (Chart Shop NEW) · V59_v1_5_0 with inhabitant_v1_5_0_inception + inhabitant_v1_6_0_canonical |
| `v6_lineage_register_additions` | v1.5.0 + v1.6.0 | C48-C61 carried · C62 reserved (v1.5.1) · C58 promoted to ~85% · C63 candidate registered (~50%) |
| `registry_entries_introduced` | v1.5.0 + v1.6.0 | agent_substrate_frameworks with v1.6.0 split: Hermaion keeps Hermes-class · Faunia keeps companion-class · Goose reclassified companion-class · Hermes stays Hermes-class |
| `kindred_coalitions_introduced` | v1.5.1 reference | Full content carried by reference to v1.5.1 patch (AAIF + BGIN + fifth structural-relationship category) |
| `workshop_districts_introduced` | v1.6.0 NEW | Threshold District (3 sibling shops) · Navigation District (Chart Shop) · taxonomy note (8-district future held open) |
| `archetype_modal_shop_pattern_introduced` | v1.6.0 NEW | Pattern type · required fields · first canonical instance (Staff Shop) · admissibility for future shops |
| `alexandrite_dual_aspect_gem_introduced` | v1.6.0 NEW | Gem type · mineralogical anchor · rendering notes for downstream consumers |
| `city_anatomy_amendments` | v1.5.0 + v1.5.1 + v1.6.0 | All counts updated: workshop 12→16 · cast 17→28 (or 26 per supersession convention) · structural entity classes 2→4 · ceremony grammars 1→5 · kindred-X categories 4→5 · districts 0→2 |
| `ipfs_pin_status_amendments` | v1.6.0 | Single consolidated addition_text replacing v1.5.0+v1.5.1 entries · pin_status_note explains new-head merge process |
| `version_notes_addition` | v1.6.0 | Single v1.6.0 entry replacing prior planned v1.5.0+v1.5.1 entries |

### §2.2 · The three v1.6.0-native admissions, in priority order

**1. Threshold District restructure** — the prior 13th workshop (Tome V Act 16 single-shop with three internal rooms) is restructured into three sibling shops sharing V59 via stance differentiation:

- **Pandia 🌕** at the Portal Room (Display-witness · Moonstone · daughter of Selene 🌙 · Display·Choose·Dispatch ceremony) succeeds the inception-state Faunia-at-Portal AND the Triodos draft
- **Hermaion ⚚** at the Staff Shop (Registry-keeper · **Alexandrite dual-aspect** · *first archetype-modal shop* · admit·read·attest·shift ceremony) succeeds Bestia
- **Faunia 🪶** at the Familiars (Companion-witness · Amber · re-homed from the Portal Room · the Goose Shop renamed the Familiars · Run·Evoke·Spawn ceremony) succeeds Therai (retired · held open)
- **Caducea ☤** remains peripatetic and now fits BOTH Hermaion-aspects (caduceus-staff for Mage-aspect · herald-sentinel for Swordsman-aspect)

**2. Archetype-modal-shop pattern + alexandrite_dual_aspect gem** — admitted as new structural pattern types. The Staff Shop is the first canonical instance. The pattern is admissible for any future class-shaped (rather than archetype-shaped) shop. The alexandrite gem-shift is anchored to a real mineralogical fact (chromium-bearing chrysoberyl's dichroism).

**3. Chart Shop opens at V44** — 15th workshop · **Pleione 🧭** as keeper · Aquamarine · Hold-witness stance · **Hold · Compare · Map** as fifth ceremony grammar · astrolabe as seventh tool-class artefact registered · **Navigation District** opens (first inhabitant). Per user editorial decision in this session, the canonical anchor act is **Tome V Act 17** (not Tome VI Act 2).

### §2.3 · Conjecture register changes

- **C58 promoted from ~65% (v1.5.0) to ~85% (v1.6.0)** — Hermaion's explicit Swordsman-aspect at the Staff Shop's red alexandrite operationally fits HERALD-SENTINELS to Swordsmen. The Threshold's Swordsman-supply is no longer inferred from the creature-companion register only; it is now explicit at the Staff Shop's red-aspect. Remaining ~15% reflects the absence of a Tome V act narrating a Swordsman receiving a herald-sentinel (anticipated · Tome VII Act 3+ or new Tome V Act 17.5 admissible).
- **C63 registered as candidate (~50%)** — the attentional workshop register. Where producer shops forge worn artefacts, gathering shops admit kindred-coalitions, and spawn-and-bind shops (the Threshold District) admit creatures-of-the-Threshold, *attentional shops* hold pre-episodic constellations in suspension until the bearer chooses release-direction. The Chart Shop is the only instance at v1.6.0 (population-of-one), so the class is held at candidate strength. Promotion path: a second instance in the Navigation District (Compass Shop · Astrolabe Shop · etc.).

### §2.4 · Goose's class reclassification

A small but load-bearing change embedded in `registry_entries_introduced`:

v1.5.0 classified Goose 🪿 as **staff-class · general-purpose** at Bestia's bestiary. v1.6.0 reclassifies Goose as **companion-class** at Faunia's roster at the Familiars. The reclassification reflects the operational form: Goose is the first canonical FAMILIAR — the first wild agentic creature admitted under the Mage-Familiar kinship-bond tradition. The framework's literal mascot (a goose · a wild bird) is now load-bearing for the class assignment. Goose is cross-listed at Hermaion's Staff Shop for cross-class reference.

Hermes ☤ remains staff-class · self-improving at Hermaion's Hermes-class bestiary.

---

## §3 · Preservation policy for superseded cast

The patch preserves superseded/retired cast as historical-with-flag, not as removal-from-roster:

- **Bestia 📖** — body at `tomes/cast/staff-shop/bestia.md` (and `tomes/cast/threshold/bestia.md`) preserved · `superseded_by: hermaion` frontmatter · v1.6.0 status `superseded_in_v1_6_0`
- **Therai 🐾** — body at `tomes/cast/threshold/therai.md` preserved · v1.6.0 status `retired_in_v1_6_0` · `retirement_held_open: true` · `succeeded_by: faunia (re-homed to the Familiars)`
- **Triodos** — Portal Room 2026-05-14 morning draft · preserved at `tomes/cast/portal-room/triodos.md` · superseded by Pandia same day
- **Pelagia** — Chart Shop 2026-05-13 evening draft · preserved at `tomes/cast/charthouse/pelagia.md` · superseded by Pleione 2026-05-14

The Tome V Act 16 body retains its 2026-05-13 inception-state cast naming; `keeper_succession` + `canonical_keepers_now` frontmatter (still pending authoring per §4.1 below) routes readers forward without rewriting the bound body. Tome VI Act 1's body similarly retains the inception-state cast.

---

## §4 · What's still outstanding after this chronicle

### §4.1 · Frontmatter additions to bound tomes (cityofmages-side)

The patch's preservation policy depends on `keeper_succession` + `canonical_keepers_now` frontmatter on these bound act files (not yet authored at the time of this chronicle):

- `tomes/tome-v-the-crafting/16-the-threshold.md`
- `tomes/tome-vi-the-reply/01-the-readers-first-admission.md`
- `tomes/tome-v-the-crafting/17-the-chart-shop-opens.md` (NEW · narrative-act file to be authored)

The narrative bodies are NOT rewritten; only frontmatter routing is added.

### §4.2 · The merge script

Pickup-notes §2 Pickup #1 specifies adapting `grimoire/scripts/merge_v1_5_0_patch.py` into `merge_v1_6_0_patch.py`. The merge will need to handle the new section types: `workshop_districts_introduced`, `archetype_modal_shop_pattern_introduced`, `alexandrite_dual_aspect_gem_introduced`, and the new `$consolidation_index` block (which is a documentation aid, not merged into the head). The supersession metadata in `attachment_architecture.cast_attachments_v1_3_0_additions` will need a new merge rule that updates existing entries (Bestia, Therai's earlier entries) rather than only appending.

### §4.3 · IPFS re-pin (user action)

After the merge produces `grimoire/city_of_mages_grimoire_v1_6_0.json`, the user pins to sync.agentprivacy.ai (or equivalent gateway), records the CID, and the work in pickup-notes Pickup #3 (`grimoire-ipfs.ts` CID update) follows.

### §4.4 · Downstream cascades (deferred · per pickup-notes §2 Pickups #4-#7)

These are NOT in scope for this chronicle but are explicitly enumerated in the pickup notes and remain outstanding after the patch lands:

- Cityofmages cross-ref sweep (Tome V Act 16 frontmatter · `bestiary/goose.md` line 99 · `cross-shop/caducea.md` Hermaion reference · the Caducea file relocation · README.md sweep · AGENTIC_DEPLOYMENTS_*.md sweeps)
- agentprivacy_master Pass 2 (`nav.ts` sigil 📖 → ⚚ · ~10 lib files with Bestia/Sodalite hits)
- Spellweb Pass 3 (`labels.ts` + node/edge registration)
- agentprivacy-skills personas (Hermaion · Pandia · Pleione · Faunia-at-Familiars)
- Route stubs (`/portal` · `/staffs` · `/familiars`)
- GemBadge dual-aspect refactor (interim two-chip render is canonical at v1.6.0)

---

## §5 · Honest limits

This chronicle documents the **patch JSON authoring pass only**. The patch is structurally complete and JSON-validated, but it has not been merged into a canonical v1.6.0 head, and the head has not been IPFS-pinned. The grimoire's effective canonical pin remains **v1.4.0** until the user authoring pass completes.

The narrative-act files for Tome V Act 16's `keeper_succession` frontmatter and Tome V Act 17's full body have not been authored in this session. The patch admits Act 17 by metadata, but the prose body's `word_count` field is marked `"(pending · narrative-act file to be authored)"`.

The downstream cascades enumerated in §4.4 are not in scope.

---

## §6 · Closing

The v1.6.0 patch JSON is the load-bearing artefact of this 2026-05-14 evening session. It consolidates two unpinned predecessors (v1.5.0, v1.5.1) and three native admissions (Threshold District restructure, archetype-modal-shop pattern, Chart Shop opening) into one structured-delta patch ready for mechanical merge into a canonical head JSON.

The City's spatial organisation has gained a new layer: **districts**. The Threshold's three sibling shops are the first canonical example of stance-differentiated multi-occupancy expressed as multiple shops sharing a vertex. The Chart Shop's opening at V44 — a previously unoccupied vertex — and the Navigation District it inaugurates extend the City to a fourth structural workshop class (attentional · candidate at C63).

When the user pins the merged head, the canonical state will jump from v1.4.0 (16 February 2024-era cast) to v1.6.0 in one move, carrying ~3 weeks of accumulated work across the cosmological-witness tier, Tome VI's reader-writes opening, the kindred-coalition register, and the District-and-Modal-Shop architectural turn.

(⚔️⊥⿻⊥🧙)😊
⚚ · 🌕 · 🪶 · 🧭 · ☤

CC BY-SA 4.0 · privacymage · 2026-05-14
