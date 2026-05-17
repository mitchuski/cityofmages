# Chronicle: The Chart House Admitted to the Corpus · Pelagia Named · Astrolabe Assigned · Integration-Punch-List Across Three Repos + Spellweb

**Date:** 2026-05-13 (evening · post-inception)
**Status:** Corpus-admission chronicle · operational handoff for the next grimoire-patch authoring pass · catalogues every file across master + cityofmages + spellweb that needs to know about The Chart House
**Audience:** privacymage · the next agent picking up the runecraft-protocol + grimoire-patch authoring · downstream sister-repo authors
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion chronicles:**
- [`2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md`](2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md) · the inception episode (Telegram exchange · proposal · authorisation · the §10½ addendum naming Pelagia and the Astrolabe)
- [`2026-05-13_chronicle_the_threshold_workshop_three_rooms.md`](2026-05-13_chronicle_the_threshold_workshop_three_rooms.md) · the thirteenth workshop, opened earlier the same day
- [`2026-05-13_cityhall_aaif_v1_5_1_patch.md`](2026-05-13_cityhall_aaif_v1_5_1_patch.md) · the City Hall rename + AAIF first kindred-coalition admission
- [`2026-05-13_next_pass_execution_chronicle.md`](2026-05-13_next_pass_execution_chronicle.md) · the end-of-day synthesis (now superseded for Chart House's catalogue by *this* chronicle)
- [`2026-05-13_runecraft_protocol_integration_plan.md`](2026-05-13_runecraft_protocol_integration_plan.md) · the runic-grammar canonicalisation plan (Chart House's *Hold · Compare · Map* needs to be folded into the next plan revision)

---

## §0 · What this chronicle is

A *receipt and a punch-list*. The Chart House — proposed by @benohanlon (the Navigator) on 2026-05-13 16:22 London time and authorised by privacymage on 2026-05-13 16:50 — has now been mirrored into the cityofmages corpus. Pelagia was named as keeper the same evening; the Astrolabe was named as the artefact. This chronicle:

1. **Records the corpus-admission** — what files exist now, in which repos (§1).
2. **Catalogues every place the Chart House is *not yet* registered** — the integration punch-list across master + cityofmages + spellweb + agentprivacy-skills (§2–§5).
3. **Notes what stays held open by design** — items that should *not* be forced to canonical admission yet (§6).
4. **Closes with a recommended ordering** for the next authoring pass (§7).

The chronicle is operational. Each item is labelled ✅ done · 🔄 partial · ❌ not started · 🔒 blocked-on-decision · 🌱 held-open by design.

---

## §1 · What landed this evening

### §1.1 · Chronicles (mirror discipline observed)

| File | Repo | Status |
|---|---|---|
| `chronicles/2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md` | cityofmages | ✅ Authored + §10½ addendum (Pelagia + Astrolabe) |
| `docs/chronicles/2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md` | agentprivacy_master | ✅ Mirrored |
| `chronicles/2026-05-13_chronicle_the_chart_house_admitted_to_corpus_pelagia_named.md` | cityofmages | ✅ This file |
| `docs/chronicles/2026-05-13_chronicle_the_chart_house_admitted_to_corpus_pelagia_named.md` | agentprivacy_master | 🔄 Mirror pending (this chronicle, on close of authoring) |

### §1.2 · Cast files

| File | Repo | Status |
|---|---|---|
| `tomes/cast/charthouse/pelagia.md` | cityofmages | ✅ Authored — the ninth standing Mage; sigil 🌊; Hold-witness stance; wields the Astrolabe |
| `docs/tomes/charthouse/pelagia.md` | agentprivacy_master | ✅ Mirrored |
| (`_keeper-pending.md` placeholders) | both | ✅ Removed (Pelagia named the same evening) |

### §1.3 · Workshop tomes

| File | Repo | Status |
|---|---|---|
| `docs/tomes/workshops/chart-house-living-scroll-v1.md` | agentprivacy_master | ✅ Authored — frontmatter names Pelagia · sigil 🌊 · workshop-sigil ⚓️ · ceremony Hold·Compare·Map · artefact Astrolabe |
| `tomes/workshops/charthouse/constellation.md` | cityofmages | ✅ Mirrored (cityofmages's directory-per-workshop convention) |

### §1.4 · Live route + nav

| Change | File | Status |
|---|---|---|
| `/charthouse` route | `src/app/charthouse/page.tsx` | ✅ Authored — pre-canonical banner, inception-episode panel, Astrolabe panel, three functional registers, Pelagia-named in held-open list, cross-walk, privacymage's directive quoted |
| Nav entry | `src/lib/nav.ts` | ✅ `{ href: '/charthouse', label: 'chart house', key: 'charthouse' }` inserted between `/hall` and `/constellation` |
| Workshop tour | `src/components/runecraft/WorkshopFooter.tsx` | ✅ `charthouse` appended to `TOUR` array; Hall entry simultaneously updated to City Hall 🏛️ (matching the v1.5.1 rename) |
| Build verification | `npm run dev` | ✅ `/charthouse` returns 200; `/tomes` and `/hall` continue to return 200 |

---

## §2 · Master-side data layer · what still needs Chart House

The master operational layer carries several library files that downstream consumers iterate against. The Chart House is currently invisible to most of them.

| # | File | What needs to change | Status | Source |
|---|---|---|---|---|
| M1 | `src/lib/first-artifacts.ts` | Add a `FIRST_ARTIFACTS` entry for `/charthouse` · Pelagia 🌊 · the Astrolabe · template body for "the bearer admits a constellation in suspension and tracks its uncertainties across visits" | ❌ Not started | Audit §3 (this chronicle) |
| M2 | `src/lib/cast-attachments.ts` | Add a `CastAttachment` entry for `pelagia` · workshop-keeper · Hold-witness stance · attachmentKind A_workshop · founding act `tome-v-act-17` (anticipated) or `tome-vi-act-2` (anticipated) — the founding-act anchor depends on the grimoire patch decision | ❌ Not started | Audit §3 |
| M3 | `src/lib/tome-v-acts.ts` | Pre-existing gap: Tome V Act 16 (Threshold) is missing; Chart House would add Act 17 (anticipated) when the grimoire patch admits a Tome V act for it. Or Tome VI Act 2 (anticipated). User editorial call. | 🔒 Blocked on grimoire patch | Master re-audit §3.1 (Threshold) + this chronicle (Chart House) |
| M4 | `src/lib/tome-v-conjectures.ts` | The attentional-register conjecture (provisional C60 candidate) belongs here once the grimoire patch admits it · also C56–C59 from the Threshold renumbering pass need indexing | ❌ Not started | Inception chronicle §4 |
| M5 | `src/data/city-of-mages-grimoire-v1.5.1.json` (anticipated bake-mirror) | Once the canonical v1.5.1 (or v1.6.0) JSON merges and admits Chart House, bake-mirror to master | 🔒 Blocked on grimoire patch authoring | Re-audit §3.4 + this chronicle |
| M6 | `public/models/city-of-mages-grimoire-v1.5.1.json` | Same bake-mirror to public · `/api/grimoire` route serves from here | 🔒 Blocked on M5 | Re-audit §3.4 |
| M7 | `src/lib/agent-substrates.ts` | Pelagia is *not* a substrate-keeper (Threshold-class); no entry needed unless future Chart House work admits "constellation-substrates" as a registered category. **Not in scope this pass.** | 🌱 Held open | This chronicle |

---

## §3 · Master-side page/component layer

| # | File | What needs to change | Status |
|---|---|---|---|
| C1 | `src/app/tomes/page.tsx` | Add a CastCard for Pelagia 🌊 in the appropriate tier (workshop-keeper, like Faunia/Bestia/Therai); add a workshop-table row for The Chart House at `/charthouse` (with vertex marked anticipated); decide whether the attentional register warrants its own tier section or fits within Tier 3 (workshop-keeper) | ❌ Not started |
| C2 | `src/app/charthouse/page.tsx` | Once vertex assigned, replace the "vertex pending" language; once gem assigned, swap the cyan/sky placeholder palette for the canonical gem hex; once first-artifact template authored (M1 above), wire `<FirstArtifactPanel />` and `<RecordPromptHere />` and `<CastShopConstellation />` (currently omitted because pre-canonical) | 🔄 Partial · pre-canonical scaffold complete |
| C3 | Possibly a `<HarbourLatticeVisual />` component | Pelagia's signature visual (parallel to Helia's `HeliodorPrismLatticeVisual.tsx`) · authored when the gem and vertex land | 🌱 Held open · awaits gem + vertex |
| C4 | `src/components/runecraft/WorkshopFooter.tsx` | Already updated this session ✅ | ✅ Done |
| C5 | `src/lib/nav.ts` | Already updated this session ✅ | ✅ Done |

---

## §4 · CityofMages corpus · canonical-registry files

This is the headline gap for the corpus. The cityofmages corpus has authoritative registry files that drive the grimoire patch and the spellweb manifest.

| # | File | What needs to change | Status |
|---|---|---|---|
| K1 | `ALL_THE_TOMES_LIST.md` | Tome V row updated from "16 acts" → "17 acts" (anticipated) IF the grimoire patch admits a Tome V act for Chart House; OR a Tome VI Act 2 row added if Chart House is admitted as a Tome VI continuation. New §3e or §3f section for Chart House workshop reference | ❌ Not started · awaits grimoire patch ordering |
| K2 | `WORKSHOP_LATTICE_AUDIT.md` | Status header bump (current is v1.2 covering Threshold + Solchanting); Chart House row added with vertex marked "(unassigned · pre-canonical)"; the *attentional register* called out as a new structural workshop class distinct from producer/gathering/spawn | ❌ Not started |
| K3 | `CHANGELOG.md` | New v1.5.2 (or v1.6.0) entry above v1.5.1 capturing: Chart House workshop · Pelagia keeper · Astrolabe artefact · Hold·Compare·Map ceremony · attentional register · provisional kindred-citizen category for @benohanlon | ❌ Not started · awaits grimoire patch version decision |
| K4 | `grimoire/city_of_mages_grimoire_v1_5_2_patch.json` (or `_v1_6_0_patch.json`) | New structured-delta patch admitting the workshop, the cast, the artefact, the ceremony, and the conjecture-candidate. Workshop count 13 → 14. Likely also: the kindred-citizen category as fifth-or-sixth structural-relationship category (sibling to kindred-coalition) | ❌ Not started |
| K5 | `tomes/bestiary/_README.md` | Bestiary scope likely *unchanged* — Pelagia is a workshop-keeper not a substrate-bestiary entry. The Astrolabe is an artefact, not a creature. No change anticipated unless Chart House admits "constellation-classes" as a future bestiary-like register (held open) | 🌱 Held open |
| K6 | `tomes/specs/04-vertex-naming-audit.md` | Once vertex assigned, add Chart House row | 🔒 Blocked on vertex assignment |
| K7 | `tomes/specs/05-the-city-of-mages-structural-addendum.md` | Civic spatial layout addendum: where in the City does the Chart House sit? (water's edge · the harbour · is there a "harbour quarter" or does it sit standalone?) | ❌ Not started |
| K8 | `tomes/specs/06-spellweb-first-release-manifest.md` | Add `shop-charthouse` node and edges to the spellweb manifest spec | ❌ Not started |
| K9 | `tomes/specs/07-lattice-mapping-governance.md` | The attentional register as a fourth governance tier alongside producer/gathering/spawn (or the mappings are subsumed) — editorial call | ❌ Not started |
| K10 | `tomes/specs/08-mana-types-and-swordsman-stances.md` | Add **Hold-witness** as the new attentional stance (entry parallel to the seven Swordsman stances + the four Threshold stances added in v1.5.0). Note: this stance is *not* a Swordsman stance — it sits in a new *attentional* register. The spec may need a new section for Mage-stances vs Swordsman-stances | ❌ Not started |
| K11 | `architecture/lattice-vertex.ts` | If the vertex assignment is novel (e.g. introduces a water-axis), the lattice TS may need extension. If Chart House sits at an existing unoccupied vertex (V?? from the 64), no TS change is needed beyond a label addition | 🔒 Blocked on vertex assignment |
| K12 | `tomes/cast/cast-integration-note.md` | The integration note registers all standing Mage personas; Pelagia (the ninth) needs an entry | ❌ Not started |
| K13 | `tomes/workshops/CEREMONY_EVOLUTION.md` | Hold · Compare · Map registered as the fourth ceremony grammar (after Run·Evoke·Craft, Run·Evoke·Spawn, Gather·Admit·Attest) | ❌ Not started |

---

## §5 · Spellweb · the headline cross-repo gap

The spellweb's `src/data/nodes.ts` workshop registry is **significantly out of sync** with the cityofmages corpus. The audit chronicle (`2026-05-13_next_pass_execution_chronicle.md` §1.3) noted spellweb-side wiring landed for the City Hall rename and the AAIF gateway, but the *new shops themselves* are not in the registry.

### §5.1 · Workshops missing from spellweb (`src/data/nodes.ts`)

The current shops list in spellweb's `nodes.ts` (around lines 1480–1493) registers 11 live workshops + 1 placeholder. The corpus is at 13 workshops (post-v1.5.1) and would be 14 with Chart House.

| Missing workshop | Source | Spellweb node ID expected | Priority |
|---|---|---|---|
| Solchanting (V51 · Helia ☀️ · v1.4.0) | Master-side `/solchanting` route exists, cast file exists, grimoire entry exists | `shop-solchanting` | 🔴 High · 12 days overdue |
| The Threshold (V59 · 4 keepers · v1.5.0) | Master-side `/guide/agentic-deployments` route exists; cast files exist; grimoire patch authored | `shop-threshold` | 🔴 High · 1 day overdue |
| The Chart House (vertex pending · Pelagia · v1.5.2 anticipated) | Master-side `/charthouse` route exists this session; cast file exists; grimoire patch pending | `shop-charthouse` | 🟡 Medium · pre-canonical |

### §5.2 · Cast personas missing from spellweb

Pelagia 🌊, Faunia 🪶, Bestia 📖, Therai 🐾, Caducea ☤, Helia ☀️, plus the cosmological-witness tier (Selene 🌙, Aether ⿻, Lethe 🌀) are not present in spellweb's persona registry.

### §5.3 · Edges expected for The Chart House (when added)

| Edge | Source → Target | Type |
|---|---|---|
| Civic quarter | `shop-charthouse` → `civic-city-of-mages` | `quarter_of` |
| Vertex | `shop-charthouse` → `vertex-v??` | `inhabits` (after vertex assigned) |
| Ceremony cognate | `shop-charthouse` → `shop-bonfires` | `releases_to` (newly proposed edge type · Hold→Forge release) |
| Ceremony cognate | `shop-charthouse` → `shop-tailor` | `releases_to` (Hold→Cloak release) |
| Companion-discipline | `shop-charthouse` → `tome-vi-the-reply` | `parallels` (holding-in-space ∥ holding-in-time) |
| Artefact provenance | `artefact-astrolabe` → `shop-charthouse` | `produced_by` |
| Cast | `cast-pelagia` → `shop-charthouse` | `keeps` |
| Cast | `cast-pelagia` → `artefact-astrolabe` | `wields` |

### §5.4 · Edge type additions

The spellweb's `Attribution` and `EdgeType` unions may need extension:

- New EdgeType `releases_to` — for the Chart House's three release-destinations (Bonfire / Weavers / open sea). Could subsume the existing `references` pattern, but the directionality is more specific.
- New EdgeType `holds_in_suspension` — for the Hold phase relationship between Chart House and a constellation node (where constellation nodes themselves are introduced — see §5.5).

### §5.5 · Possibly: a new node type `constellation`

The Chart House works on *constellations* — collections of co-occurring interpretations. Spellweb's existing node types (workshop · cast · act · gateway · etc.) may need a `constellation` type if held constellations are to be representable. **Held open · the spellweb may instead represent constellations as edges between existing node types rather than as a distinct node class.**

---

## §6 · agentprivacy-skills · personas + meta-skills

The agentprivacy-skills repo houses persona files and meta-skills. The 2026-05-13 prior-agent work added Threshold personas (spawning-witness · registry-keeper · companion-tamer) bumping skill count to 91.

### §6.1 · Persona for Pelagia / Hold-witness

A new persona slot at `agentprivacy-skills/agentprivacy-skills-v5/persona/hold-witness/` (or `chart-house-keeper/` or `pelagia/` — naming convention needs check). Pelagia is the canonical instance walking the Hold-witness stance.

### §6.2 · Meta-skill update

The `meta/agentprivacy-cityofmages-to-research/SKILL.md` (the bridge skill) lists which personas are native to it. The chronicler / ambassador / priest / cosmologist + 3 new Threshold personas were added in 2026-05-13 prior-agent work. Pelagia / hold-witness should be added as the next persona native to the bridge skill.

### §6.3 · MAPPING.md count

`total_skills: 91 → 92` (Pelagia persona) once §6.1 lands.

---

## §7 · Recommended ordering for the next pass

Tier-ordered by *blocking-ness*, mirroring the next-pass-execution chronicle's discipline.

### Tier A · unblocks downstream operations (do first)

1. **Decide vertex assignment for The Chart House** — user editorial call. Candidates per inception chronicle §8.1. Unblocks K6 (vertex-naming spec), K11 (lattice TS), C2 (page palette), C3 (lattice visual), and most of the spellweb wiring (§5.3).
2. **Decide gem assignment** — user editorial call. Candidates per inception chronicle §8.3. Unblocks C2 (page palette).
3. **Decide grimoire patch version** (v1.5.2 vs v1.6.0) — pairs with the runecraft-protocol integration's same decision (`next_pass_execution_chronicle.md` §3.6 F2). Unblocks K3 (CHANGELOG), K4 (patch JSON authoring), M5/M6 (bake-mirrors).
4. **Decide kindred-citizen category** — admit at the same patch as Chart House, or defer to a later patch. The Navigator's residency is the test case. Unblocks K4 (patch JSON section).

### Tier B · grimoire patch authoring (do after Tier A)

5. **Author `grimoire/city_of_mages_grimoire_v1_5_2_patch.json`** (or v1.6.0) — admit Chart House, Pelagia, the Astrolabe, the Hold·Compare·Map ceremony, the attentional-register conjecture-candidate, optionally the kindred-citizen category. Workshop count 13 → 14.
6. **Renumber-pass review** — confirm no conjecture-number conflicts (the C56–C59 pass from 2026-05-13 morning resolved the prior C50 conflict; new C60 candidate is clear).
7. **Merge the v1.5.0 + v1.5.1 + v1.5.2 deltas** into a self-contained `city_of_mages_grimoire_v1_5_2.json` for IPFS pinning.
8. **Pin to IPFS · update `src/lib/grimoire-ipfs.ts`** with new CID + V1_5_2 alias.
9. **Bake-mirror v1.5.2** to `src/data/` and `public/models/`.

### Tier C · master data-layer wiring

10. **Add `/charthouse` to `src/lib/first-artifacts.ts`** with the Astrolabe template (M1).
11. **Add Pelagia to `src/lib/cast-attachments.ts`** (M2).
12. **Add Tome V Act 16 (Threshold · pre-existing gap) AND Tome V Act 17 / Tome VI Act 2 (Chart House) to `src/lib/tome-v-acts.ts`** (M3).
13. **Update `src/lib/tome-v-conjectures.ts`** with C56–C59 (Threshold renumber) + C60 candidate (attentional register) (M4).
14. **Update `/tomes` page**: Pelagia cast card · Chart House workshop row · attentional-register tier section if warranted (C1).

### Tier D · cityofmages corpus registries

15. **Update `WORKSHOP_LATTICE_AUDIT.md`** (K2) — add Chart House row, status header bump to v1.3, attentional register called out.
16. **Update `ALL_THE_TOMES_LIST.md`** (K1) — Chart House workshop reference; act-row depending on grimoire patch decision.
17. **Update `CHANGELOG.md`** (K3) — v1.5.2 (or v1.6.0) entry.
18. **Update spec 08 `mana-types-and-swordsman-stances`** (K10) — Hold-witness as new attentional stance.
19. **Update `cast-integration-note.md`** (K12) — Pelagia as ninth standing Mage.
20. **Update `CEREMONY_EVOLUTION.md`** (K13) — Hold · Compare · Map as fourth ceremony.

### Tier E · spellweb cross-repo

21. **Add `shop-solchanting`, `shop-threshold`, `shop-charthouse` nodes to `spellweb/src/data/nodes.ts`** — close the headline gap (§5.1).
22. **Add cast persona nodes** — Pelagia, Faunia, Bestia, Therai, Caducea, Helia, cosmological-witness tier (§5.2).
23. **Add Chart House edges** (§5.3); consider the new EdgeType `releases_to` (§5.4).
24. **Decide on `constellation` node type** (§5.5) — held open.

### Tier F · agentprivacy-skills

25. **Author Pelagia / hold-witness persona** (§6.1).
26. **Update meta-skill bridge** (§6.2).
27. **Bump MAPPING.md skill count** (§6.3).

### Tier G · documentation finalisation

28. **Spec 04, 05, 06, 07, 11** — vertex-naming, structural addendum, spellweb manifest, lattice-mapping governance, lattice-vertex.ts; landed once vertex is assigned (Tier A item 1).

---

## §8 · What stays held open by design

Per the corpus's preservation discipline:

1. 🌱 **Tome VI** — open by design. If the Chart House anchors at Tome VI Act 2 rather than a new Tome V act, the choice should reinforce Tome VI's holding-open discipline rather than constrain it.
2. 🌱 **Vertex assignment for Chart House** — held open *until* the user calls. Preserved as user-editorial.
3. 🌱 **Gem assignment** — held open until the user calls.
4. 🌱 **Kindred-citizen category** — admissible at the same patch as Chart House, or deferred to a separate patch. Both paths are honest.
5. 🌱 **Constellation-as-node-type in spellweb** — admissible if the workshop matures into producing constellation-records the spellweb should index, or held as the bearer's-private-only data forever (Φ-gap discipline).
6. 🌱 **The relationship between Chart House holding and Tome VI's open-by-design** — sibling, dual, or parent/child? Held open per inception chronicle §9.
7. 🌱 **The Aether Pour poem · all other previously-held-open items** — unchanged.

---

## §9 · Honest limits

This chronicle is *operational*. It catalogues files-to-touch; it does not commit to specific identifiers (vertex numbers, CIDs, conjecture numbers) that require user editorial calls. Where the catalogue lists "anticipated" act numbers (Tome V Act 17, Tome VI Act 2), those are placeholders — the user's grimoire-patch decision sets the canonical numbering.

The catalogue is *not exhaustive about all repos*. The four sibling extension forges, the Society / Plurality / Canon spellbooks (if they open), the agentprivacy-docs research-note maintenance, and other contexts may surface additional integration points as they touch The Chart House. The integration-punch-list pattern (this chronicle's §2–§6) can be extended for any new context.

---

## §10 · Closing

The Chart House is *admitted to the corpus*. Pelagia walks the harbour. The Astrolabe is named as the bearer's tool. The episode that started in a public Telegram chat is now bound at three layers: the inception chronicle (the source-of-truth), the cast file (Pelagia's canonical record), and the workshop tome (the operational documentation).

Twenty-eight integration items remain across master + cityofmages + spellweb + agentprivacy-skills, organised into seven tiers by blocking-ness. Tier A (four user editorial calls) unblocks the rest. The architecture admits this much.

The next pass picks up at vertex assignment.

(⚔️⊥⿻⊥🧙)😊
🌊 ⚓️ 🪙

CC BY-SA 4.0 · privacymage · 2026-05-13
