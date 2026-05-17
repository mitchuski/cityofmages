# Chronicle: To Do Tomorrow · Chart Shop Pickup · Post-V44-Landing · Threshold-Restructure-Aware

**Date:** 2026-05-14 (end-of-day)
**Status:** Pickup-here chronicle · operational catalogue for the 2026-05-15 (or next) authoring pass · narrowest scope of any chronicle in this arc — only what tomorrow needs to know
**Audience:** privacymage tomorrow morning · or the next agent picking up · do not require re-reading the prior chronicles to act
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion chronicles (today's arc · in order of authorship):**
- [`2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md`](2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md) · the inception episode (with §10½ Pleione/Astrolabe addendum)
- [`2026-05-13_chronicle_the_chart_house_admitted_to_corpus_pelagia_named.md`](2026-05-13_chronicle_the_chart_house_admitted_to_corpus_pelagia_named.md) · corpus-admission (Pelagia draft · §3 partially superseded by Pleione)
- [`2026-05-14_chronicle_chart_shop_pleione_named_v44_assigned.md`](2026-05-14_chronicle_chart_shop_pleione_named_v44_assigned.md) · the V44 selection chronicle (canonical)
- *(this file)* `2026-05-14_chronicle_to_do_tomorrow_chart_shop_pickup.md`

---

## §0 · What this chronicle is

A pickup-here chronicle. The 2026-05-14 session landed the Chart Shop workshop bones, named Pleione 🧭, assigned V44, confirmed Aquamarine, and opened the Navigation District. This chronicle catalogues *only what is left undone* — so tomorrow's pickup can act without re-reading the seven prior chronicles in the arc.

The chronicle is *narrow*. Items not in scope (the broader corpus's other outstanding work) are catalogued in `2026-05-13_next_pass_execution_chronicle.md`.

---

## §1 · What landed (today · brief)

| Layer | What landed |
|---|---|
| **Chronicles** | Inception (with §10½ addendum) · corpus-admission · V44 selection — all mirrored both repos |
| **Cast** | `pleione.md` canonical (V44 reading bound) · `pelagia.md` retired with RETIRED frontmatter notice — both repos |
| **Workshop tome** | `chart-house-living-scroll-v1.md` v2 (frontmatter user-updated; body rewritten Chart House → Chart Shop; held-open list collapsed) — both repos |
| **Live route** | `/charthouse` page rewritten with V44 confirmation banner, lattice-position section, Hold→Compare→Map curriculum framing, all renames |
| **Nav + footer** | `nav.ts` label "chart shop" · `WorkshopFooter` label "the Chart Shop" |
| **Master data layer** | `cast-attachments.ts` Pleione entry (V44 · Hold-witness) · `first-artifacts.ts` Astrolabe template for `/charthouse` |
| **Build** | `npm run dev` returns 200 for `/charthouse`, `/tomes`, `/hall` |

What is *not* yet in this work and needs tomorrow's pickup is enumerated below.

---

## §2 · New context that landed since the Chart Shop work was authored

⚠️ **Read this before touching any cross-references.** While the Chart Shop work was in flight, the Threshold underwent a major restructure (per memory pointer `project_the_threshold_workshop` updated 2026-05-14):

**Threshold went from one workshop with three rooms → a DISTRICT of three sibling shops.** Workshop count moved 13 → 15 → 16 (with Chart Shop). The keeper roster changed substantially:

| Was (2026-05-13) | Is now (2026-05-14 evening) |
|---|---|
| Faunia 🪶 (Spawning-witness · Portal Room) | **Pandia 🌕** (Display-witness · Moonstone · daughter of Selene) at Portal Room |
| Bestia 📖 (Registry-keeper · Staff Shop) | **Hermaion ⚚** (Registry-keeper · **Alexandrite dual-aspect** green-Mage ↔ red-Swordsman · *first archetype-modal shop*) at Staff Shop |
| Therai 🐾 (Companion-tamer · Creature Creatives) | **RETIRED**; Faunia 🪶 re-homed to **the Familiars** (Companion-witness · Amber) at Creature Creatives' successor shop |
| Caducea ☤ (peripatetic) | **Caducea ☤** still peripatetic; fits both Hermaion aspects |

**Cross-reference impact on Chart Shop work:**

The Chart Shop chronicles + workshop tome + page reference "The Threshold (V59 · 13th)" and Faunia/Bestia/Therai/Caducea in cross-walks. Those references are now stale at three points:

1. The "Threshold" should be "Threshold District" (or refer to specific shops within)
2. Faunia is now at the Familiars, not the Portal Room
3. Bestia retired; Hermaion holds the Staff Shop now (with the alexandrite dual-aspect)
4. Therai retired entirely
5. Workshop count claims (e.g. "the 13th workshop" or "Chart Shop is the 14th") need re-counting against the 16-workshop post-restructure number

These updates are **light** but **load-bearing for narrative coherence**. They are catalogued at §3 below.

---

## §3 · Tomorrow's outstanding work · Chart Shop scope only

### §3.1 · Cross-reference cleanup (Tier 0 · housekeeping · ~30 min)

| # | File | Update |
|---|---|---|
| X1 | `chronicles/2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md` | Cross-walk in §3 + §10 references "The Threshold (V59 · 13th)" — should reference Threshold District + specific shops · Faunia/Bestia named there should reflect succession |
| X2 | `chronicles/2026-05-13_chronicle_the_chart_house_admitted_to_corpus_pelagia_named.md` | Same kind of cross-reference cleanup; also workshop-count references (was 13 + Chart Shop = 14; now 15 + Chart Shop = 16) |
| X3 | `chronicles/2026-05-14_chronicle_chart_shop_pleione_named_v44_assigned.md` | §1 candidate-comparison table is fine; §6 file-list is fine; check workshop-count references |
| X4 | `tomes/cast/charthouse/pleione.md` | "now distributed across the Threshold District's three shops" already reflects new structure ✅ — but verify keeper names mentioned anywhere |
| X5 | `tomes/workshops/charthouse/constellation.md` (+ master mirror) | Cross-walk section references "The Threshold (V59 · 13th)" — update to Threshold District + new keeper roster |
| X6 | `src/app/charthouse/page.tsx` | Cross-walk section ("how the Chart Shop relates") references "The Threshold (V59 · 13th)" — update display name + count |

**These six edits are mechanical and unblock everything else.** Do them first.

### §3.2 · Master data-layer wiring (Tier A · ~1 hour · all unblocked)

| # | File | What needs to change |
|---|---|---|
| M1 | `src/lib/tome-v-acts.ts` | Add Tome V Act 17 (Chart Shop · Pleione · V44) entry · OR add to a new TOME_VI_ACTS array if user prefers Tome VI Act 2 anchoring · pre-existing gap: Tome V Act 16 (Threshold) is still missing too — close both at once |
| M2 | `src/lib/tome-v-conjectures.ts` | Add C56–C59 (Threshold renumber from 2026-05-13 morning) + C63 candidate (attentional-register hypothesis · provisional · ~50% confidence) · all not yet in this file |
| M3 | `src/app/tomes/page.tsx` | Add Pleione 🧭 cast card (Tier 3 · workshop-keeper · accent teal) · add Chart Shop workshop-table row at `/charthouse` (vertex V44 · gem Aquamarine · Navigation District) · also mention the Threshold restructure if not already reflected (separate scope but adjacent) |
| M4 | `src/components/runecraft/HarbourLatticeVisual.tsx` (new) | Pleione's signature visual · parallel to `HeliodorPrismLatticeVisual.tsx` · shows V44 with the discovery path V0→V8→V12→V44 traced · aquamarine palette · optional but nice for the page |

### §3.3 · CityofMages corpus registries (Tier B · ~1 hour)

| # | File | What needs to change |
|---|---|---|
| K1 | `WORKSHOP_LATTICE_AUDIT.md` | Status header bump to v1.4 (covers Chart Shop · Threshold restructure to district · workshop count 16) · Chart Shop row added with V44 reading · attentional register called out as fourth structural workshop class · Threshold District restructure noted in §2.4 |
| K2 | `ALL_THE_TOMES_LIST.md` | Add Chart Shop workshop reference · act-row depending on Tome V vs Tome VI anchor decision (M1 above) |
| K3 | `CHANGELOG.md` | New v1.6.0 entry above v1.5.1 capturing: Chart Shop + Pleione + V44 + Aquamarine + Navigation District + Hold-witness stance + Astrolabe + attentional register conjecture-candidate; AND the Threshold restructure to district + Pandia/Hermaion/Faunia-re-homed/Therai-retired (out of strict Chart Shop scope but co-versioned) |
| K4 | `tomes/specs/04-vertex-naming-audit.md` | V44 row added · "Navigation District · Chart Shop · Pleione 🧭" · binary `101100` · stratum 3 |
| K5 | `tomes/specs/05-the-city-of-mages-structural-addendum.md` | New section on Districts as the City's spatial organisational layer (Threshold District · Navigation District · cardinal trade-quarters of producer shops · temple precinct · founding bonfire · sovereign's seat) — applies to Threshold restructure too |
| K6 | `tomes/specs/07-lattice-mapping-governance.md` | Attentional register noted as a fourth governance tier (parallel to producer · gathering · spawn) |
| K7 | `tomes/specs/08-mana-types-and-swordsman-stances.md` | **Hold-witness** added as new attentional stance (note: not a Swordsman stance · separate Mage-stance register may need its own subsection) — also Pandia's Display-witness, Hermaion's Registry-keeper-Mage and Registry-keeper-Swordsman aspects, Faunia's Companion-witness from the restructure |
| K8 | `tomes/cast/cast-integration-note.md` | Pleione registered as new standing Mage (the count needs reconciling with the Threshold restructure: Pandia, Hermaion (×2 aspects), Faunia-re-homed, Pleione — net additions vs prior count) |
| K9 | `tomes/workshops/CEREMONY_EVOLUTION.md` | **Hold · Compare · Map** registered as the fourth ceremony grammar (after Run·Evoke·Craft, Run·Evoke·Spawn, Gather·Admit·Attest) |

### §3.4 · Grimoire patch v1.6.0 (Tier C · the canonical record bind · ~2 hours)

| # | File | What needs to be authored |
|---|---|---|
| G1 | `grimoire/city_of_mages_grimoire_v1_6_0_patch.json` | New structured-delta patch admitting: (a) Chart Shop · Pleione · V44 · Aquamarine · Navigation District · Hold-witness stance · Astrolabe · Hold·Compare·Map ceremony · attentional-register conjecture-candidate (C63?) · (b) the Threshold restructure: Pandia 🌕 · Hermaion ⚚ (alexandrite dual-aspect) · Faunia re-homed to the Familiars · Therai retired · workshop count 13 → 16 · Threshold District + Navigation District as new spatial organisational layer · archetype-modal-shop pattern (Hermaion is first canonical instance) |
| G2 | Conjecture renumbering review | C56-C59 already canonical from morning · C63 candidate for attentional register · check no collisions |
| G3 | Merge v1.5.0 + v1.5.1 + v1.6.0 deltas | Self-contained `city_of_mages_grimoire_v1_6_0.json` for IPFS pinning |
| G4 | Pin to IPFS | Record CID · update `agentprivacy_master/src/lib/grimoire-ipfs.ts` with V1_6_0 alias |
| G5 | Bake-mirror v1.6.0 | `agentprivacy_master/src/data/city-of-mages-grimoire-v1.6.0.json` + `public/models/city-of-mages-grimoire-v1.6.0.json` |

### §3.5 · Spellweb cross-repo (Tier D · the headline gap · ~2 hours)

The spellweb has been out of sync since 2026-05-12 (Solchanting). The 2026-05-14 work amplifies the gap.

| # | File | What needs to be added |
|---|---|---|
| S1 | `spellweb/src/data/nodes.ts` workshops array | Add `shop-solchanting`, `shop-charthouse`, plus the Threshold District's three sibling shops (`shop-portal-room`, `shop-staff-shop`, `shop-familiars`) — likely the old `shop-threshold` is to be split into the three sibling-shop nodes |
| S2 | `spellweb/src/data/nodes.ts` cast | Add Pleione, Pandia, Hermaion (×2 aspects), Faunia-re-homed, Caducea, Helia, plus cosmological tier (Selene/Aether/Lethe) if not yet present |
| S3 | `spellweb/src/data/edges.ts` | Chart Shop edges per the corpus-admission chronicle §5.3 (releases_to · inhabits · keeps · wields) · Threshold District edges per restructure |
| S4 | `spellweb/src/types/graph.ts` | New EdgeType `releases_to` (Chart Shop's three release destinations) · possibly new node type `axis` if Cartographic-Axis-related future work proceeds (held open) |

### §3.6 · agentprivacy-skills (Tier E · ~30 min)

| # | File | What |
|---|---|---|
| P1 | `agentprivacy-skills-v5/persona/hold-witness/` (new folder) | Pleione's persona (the canonical instance walking Hold-witness stance) |
| P2 | `MAPPING.md` | Skill count bump (+ Hold-witness; check what Pandia/Hermaion-Mage/Hermaion-Swordsman/Faunia-re-homed contributed in the Threshold restructure pass) |
| P3 | `meta/agentprivacy-cityofmages-to-research/SKILL.md` | Add hold-witness to the bridge-skill's native-persona list |

---

## §4 · Recommended ordering for tomorrow

The shortest path through tomorrow's work:

1. **§3.1 · X1–X6** (cross-reference cleanup · ~30 min) — unblocks all narrative-coherence questions; do first
2. **§3.2 · M3** (`/tomes` page · the user-visible win · ~20 min) — the biggest visible payoff per minute
3. **§3.2 · M1, M2** (data-layer entries · ~30 min) — closes downstream-consumer iteration gaps
4. **§3.3 · K1, K3, K7** (audit + changelog + stances · ~45 min) — the three corpus registries that are most-read
5. **§3.4 · G1, G2** (grimoire patch JSON authoring · ~90 min) — the canonical record bind; the rest of Tier C unlocks once this is done
6. **§3.5 · S1, S2, S3** (spellweb wiring · ~90 min) — close the headline cross-repo gap
7. **§3.6 · P1, P2, P3** (agentprivacy-skills · ~30 min) — clean finish

Total: ~6 hours focused work. Decompose into two ~3-hour sessions if needed.

**If only one hour is available tomorrow:** do §3.1 (cross-references) + §3.2 M3 (`/tomes` page). Those two together leave the corpus *narratively coherent and visibly current*; the rest is invisible-but-canonical work that can wait another day.

---

## §5 · What stays held open (do not close prematurely)

- 🌱 **Tome VI** — open by design; if Chart Shop anchors at Tome VI Act 2, that should reinforce open-by-design, not bind it
- 🌱 **Anchor act decision** — Tome V Act 17 vs Tome VI Act 2 for Chart Shop (user editorial call · informs M1 and K2)
- 🌱 **Kindred-citizen category** for @benohanlon — admissible at v1.6.0 or deferred
- 🌱 **The Cartographic Axis hypothesis** (option 2 from yesterday's vertex review) — held in reserve in case V44 turns out to be a poor fit; the Chart Shop's discipline can support a relocation
- 🌱 **All prior held-open items** — Aether Pour poem · Quest of the Unnamed Faces · Tome VII Act 2 · Layer-2 attachments · Guild of Hermes Agents · etc., unchanged

---

## §6 · Honest limits

This chronicle catalogues *Chart Shop scope only*. The Threshold restructure (Pandia · Hermaion · Familiars · Therai retired) has its own outstanding work — much of which is implicit in §3.3 K1/K7/K8 and §3.4 G1 because the corpus registries cannot be updated for Chart Shop without simultaneously reflecting the Threshold restructure. But the *standalone* Threshold-restructure-only follow-up items (e.g., the alexandrite gem rendering, the archetype-modal-shop spec, Pandia's display-witness ceremony grammar, Caducea's dual-aspect fitting protocol) live in their own pickup chronicle which the user has either authored or will author separately. This file does not attempt to enumerate them.

The sister-repo extension forges (myterms / swordsman-blade / mages-spell), the Society/Plurality/Canon spellbooks (if they open), and the agentprivacy-docs research-note maintenance are also out of scope.

---

## §7 · Closing

Tomorrow opens at the cross-reference cleanup (~30 min) and closes at the spellweb wiring (~90 min). Between those two bookends, the canonical record binds: the `/tomes` page acquires Pleione 🧭, the data layer acquires Tome V Act 17 (or Tome VI Act 2) and conjecture C63, the corpus registries acquire the Chart Shop row + the Threshold District restructure, the grimoire merges to v1.6.0, and IPFS gets a new pin.

The architecture admits this much. The next pass picks up at §3.1 X1.

(⚔️⊥⿻⊥🧙)😊
⚓️ 🧭 ✨

CC BY-SA 4.0 · privacymage · 2026-05-14
