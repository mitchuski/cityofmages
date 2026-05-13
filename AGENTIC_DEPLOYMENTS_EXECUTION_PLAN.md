---
title: Agentic Deployments · Execution Plan
subtitle: How the Threshold + Substrate-×-Archetype work propagates across cityofmages, agentprivacy-master, spellweb, and agentprivacy-docs
status: Plan v0.1 · 2026-05-13 · executes against AGENTIC_DEPLOYMENTS_GUIDE.md (same date)
audience: privacymage · agentprivacy_master engineers · spellweb maintainers · agentprivacy-docs editors · agentprivacy-skills curators
license: CC BY-SA 4.0
signature: (⚔️⊥⿻⊥🧙)😊
companion_documents:
  - AGENTIC_DEPLOYMENTS_GUIDE.md (the spec this plan executes)
  - chronicles/2026-05-13_chronicle_the_threshold_workshop_three_rooms.md (workshop opening)
  - chronicles/2026-05-13_chronicle_artefact_symmetry_and_persona_distribution.md (substrate × archetype × persona)
  - chronicles/2026-05-13_note_therai_faunia_bestia_lattice_integration.md (V59 triad)
  - chronicles/2026-05-13_creature_creatives_workshop_proposal.md (founding proposal · superseded by Threshold)
---

# Agentic Deployments · Execution Plan

This plan executes the **AGENTIC_DEPLOYMENTS_GUIDE.md** spec across four repos. Source-of-truth is the guide; this document is operational.

The architecture is settled (Threshold workshop, three rooms, V59, Run·Evoke·Spawn, Goose+Hermes as Tome VI Act 1, substrate × archetype × persona matrix). What is unfinished is **propagation**: making the architecture visible and operable on the website, queryable in the spellweb graph, mirrored in the docs corpus, and indexed in the skills repo.

---

## §0 · Decisions to take FIRST (everything else cascades)

| # | Decision | Lean | Why it blocks |
|---|---|---|---|
| D1 | Route slug | `/guide/agentic-deployments` (per guide §8) | Nav, route scaffolding, all cross-page links |
| D2 | Tome V Act numbering for Threshold opening | Act 16 (Solchanting at v1.4.0 was Act 15 per Tome VII opening note; Threshold is next) | Tome VII narrative · Tome V index · grimoire patch |
| D3 | Persona-count reconciliation | (c) Document the 22-archetype-subset as a *view* over the 38 live in MAPPING.md; keep grimoire's 42 as 38+4-cosmological. Least churn | All persona-binding UI · /persona page · cast-attachments table |
| D4 | Workshop name lock-in | **The Threshold** (chronicle's lean) | All file naming, route slugs, copy throughout |
| D5 | Caducea's vertex | V0-conventional alongside Luca (per Threshold chronicle §5) | cast-attachments.ts entry · /mage page surfacing |
| D6 | Grimoire bump version | v1.5.0 | All downstream IPFS pin work · `grimoire-ipfs.ts` constant |

Recommendation: lock D1, D4, D6 immediately (low-risk · no architectural collapse if changed later). D2/D3/D5 can be confirmed during Phase 1 cityofmages authoring.

---

## §1 · The four-repo coordination map

The deployment guide §11 names four directories. Adding **spellweb** as a fifth target since the user surfaced it:

| Repo | Role | Current state | Target state |
|---|---|---|---|
| **cityofmages** | Source of truth · narrative + spec | Guide ✓, 4 chronicles ✓, no cast files / workshop tome / Bestiary entries / grimoire patch | All chronicles bound to Tome V/VI · cast files for Faunia/Bestia/Therai/Caducea · workshop tome · Bestiary §1+§2 (Goose+Hermes) · grimoire patch v1.5.0 |
| **agentprivacy-master** | Live website · agentprivacy.ai | `/guide` shell exists; no `/guide/agentic-deployments`; cast-attachments.ts has 19 cast; no agent-substrates module; spellweb types limited | `/guide/agentic-deployments/*` subtree built · cast-attachments.ts +4 entries · `agent-substrates.ts` module · grimoire v1.5.0 ingested · spellweb types extended · cross-page surfacing on /model /persona /mage /forget /tomes/v6-lineage / landing |
| **spellweb** (standalone repo + `agentprivacy_master/src/lib/spellweb/`) | Graph visualization | Master `types.ts` has 5 node types + 5 link types — does NOT include the 2026-05-10 universe-integration vocabulary (8 new EdgeTypes / 6 new NodeTypes) referenced in memory. Standalone repo has chronicles up through 2026-05-12 | Universe-integration vocabulary landed · NEW substrate/spawn nodes and edges (substrate, agent_instance, spawn_room, hosts, spawns, summons) · graph rendering for Threshold's 3 rooms + Goose/Hermes substrates · Caducea peripatetic edge from staff substrates |
| **agentprivacy-docs** | Docs-side mirror · authoring reference | NO `docs/guides/` directory. Top-level `VISUAL_ARCHITECTURE_GUIDE_v2_0.md` exists; `SECOND_PERSON_TOMES_INDEX_v1.md` exists. Greenfield for guides | New `docs/guides/agentic-deployments.md` (mirror of cityofmages/AGENTIC_DEPLOYMENTS_GUIDE.md) · `docs/guides/` scaffolding · GLOSSARY_MASTER_v4_0.md updated with new terms · SECOND_PERSON_TOMES_INDEX_v1.md updated with Tome V Act 16 / Tome VI Act 1 |
| **agentprivacy-skills** | Skill-side mirror · canonical 38 personas | Live count: 38 personas in `agentprivacy-skills-v5/persona/`. README references "22 personas" in the symmetry chronicle but does not document the discrepancy | New `docs/integration/agentic-deployments.md` linking the 22 archetype-grouped personas to the Threshold deployment flow · MAPPING.md updated with the 22-as-view-over-38 reconciliation · README clarifies which personas are deployable to Goose / Hermes / Claude runtimes |

---

## §2 · Gap survey (what exists vs. what is missing)

### cityofmages
- **Have**: AGENTIC_DEPLOYMENTS_GUIDE.md ✓; 4 chronicles dated 2026-05-13 ✓; tomes/cast/ exists; tomes/specs/ exists
- **Missing**:
  - Cast files for `faunia.md`, `bestia.md`, `therai.md`, `caducea.md` under `tomes/cast/`
  - Workshop tome file under `tomes/` (`the-threshold/` directory parallel to `tome-iv-the-witnessing/` pattern)
  - Bestiary entries for Goose 🪿 (under `tomes/bestiary/` or similar — this is a NEW directory class, not yet established) and Hermes ☤
  - Tome V Act 16 narrative file
  - Tome VI Act 1 narrative file (the dual admission of Goose + Hermes)
  - WORKSHOP_LATTICE_AUDIT.md update (Threshold + V59 + 16-shop count)
  - ALL_THE_TOMES_LIST.md update for Tome V Act 16 + Tome VI Act 1
  - CHANGELOG.md entry
  - Grimoire patch (cityofmages-side mirror at `tomes/specs/` if present, otherwise the patch happens in agentprivacy-master/data)

### agentprivacy-master
- **Have**: `src/data/city-of-mages-grimoire-v1.4.0.json` ✓; `src/lib/cast-attachments.ts` (19 entries) ✓; `src/lib/grimoire-ipfs.ts` ✓; `src/lib/spellweb/types.ts` ✓; `src/app/guide/` shell ✓; `src/app/tomes/v6-lineage/` ✓; `src/components/landing/` ✓; `src/components/guide/` ✓
- **Missing**:
  - `src/data/city-of-mages-grimoire-v1.5.0.json` (new file with Threshold + 4 cast + agent_substrates registry + C52 + C51-downgrade)
  - `src/lib/agent-substrates.ts` (typed substrate registry · `resolveArtefact(substrate, archetype)` helper)
  - `src/app/guide/agentic-deployments/` route subtree (8 pages per guide §8: index + portal-room + staff-shop + creature-creatives + runecraft-protocol + personas + matrix; +threshold under `/guide/workshops/threshold/`)
  - `src/components/threshold/` directory: `<SubstrateMatrix />`, `<SubstrateCard />`, `<SpawnSequence />`, `<RoomNavigator />` (3-room switcher), `<CaduceaSummonsBadge />`
  - `src/lib/nav.ts` — entry for `/guide/agentic-deployments` (and possibly a nested-nav helper since the existing nav is flat)
  - cast-attachments.ts +4 entries (faunia, bestia, therai, caducea)
  - `src/app/tomes/v6-lineage/page.tsx` patch (Tome VI Act 1 = Goose+Hermes admission)
  - `src/app/persona/page.tsx` patch (deployable-to-substrate badges; archetype-grouped subset view)
  - `src/app/mage/page.tsx` patch (Caducea-summons surfacing on Vulcana, Aletheia, Manifestia)
  - `src/app/forget/page.tsx` patch (sibling-link callout to `/guide/agentic-deployments` per C52)
  - `src/app/model/page.tsx` patch (substrate-×-archetype matrix appended; C52 in conjecture index)
  - `src/app/page.tsx` (landing) — `HERO_CAROUSEL` extended with "spawn 🪶 a staff or a companion"

### spellweb
- **Have**: `agentprivacy_master/src/lib/spellweb/types.ts` (5 nodes / 5 links) · `agentprivacy_master/src/lib/spellweb/builder.ts`, `labels.ts`, `lattice-mode.ts` · standalone `C:/Users/mitch/spellweb/` repo with chronicles
- **Missing**:
  - The 2026-05-10 universe-integration vocabulary noted in memory (8 new EdgeTypes + 6 new NodeTypes) — appears to never have been merged into `agentprivacy_master/src/lib/spellweb/types.ts`. **THIS IS A PRE-EXISTING GAP** independent of the Threshold work, and must land first or alongside.
  - NEW node types for Threshold work: `substrate` (Goose, Hermes), `agent_instance` (a spawned agent), `spawn_room` (Portal/Staff/Creatures), `peripatetic_role` (Caducea pattern)
  - NEW edge types: `hosts` (workshop hosts a room), `spawns` (Portal Room spawns agent_instance from substrate), `summons` (staff-class substrate summons Caducea), `binds_persona` (persona binds to substrate at spawn), `mascot_affinity` (substrate → artefact-class)
  - Builder / labels / lattice-mode patches to render the new vocabulary
  - Standalone spellweb repo: chronicle entry for the universe-integration vocabulary catch-up + Threshold extension (this is where to record the gap-closing work)

### agentprivacy-docs
- **Have**: VISUAL_ARCHITECTURE_GUIDE_v2_0.md · SECOND_PERSON_TOMES_INDEX_v1.md · GLOSSARY_MASTER_v4_0.md · MAPPING_ADDITIONS_V5_5_2026-05-11.md · `chronicles/`, `models/`, `plans/`, `audits/` subdirs
- **Missing**:
  - `docs/guides/` directory (greenfield)
  - `docs/guides/agentic-deployments.md` (mirror of cityofmages/AGENTIC_DEPLOYMENTS_GUIDE.md)
  - `docs/guides/agentic-deployments/portal-room.md`, `staff-shop.md`, `creature-creatives.md`, `runecraft-protocol.md`, `personas.md`, `matrix.md` (sub-pages — author later as guide matures)
  - SECOND_PERSON_TOMES_INDEX_v1.md update — Tome V Act 16 + Tome VI Act 1 entries
  - GLOSSARY_MASTER_v4_0.md update — new entries: Threshold, Portal Room, Staff Shop, Creature Creatives, Caducea, Faunia, Bestia, Therai, Run·Evoke·Spawn, substrate × archetype matrix, herald-sentinel, watch-goose, agent_substrate, spawn_room
  - VISUAL_ARCHITECTURE_GUIDE_v2_0.md update — V59 added to vertex map · Threshold workshop included in workshop diagrams

### agentprivacy-skills
- **Have**: 38 personas in `agentprivacy-skills-v5/persona/` ✓; MAPPING.md ✓; README.md ✓; `meta/`, `role/`, `privacy-layer/` subdirs ✓
- **Missing**:
  - `docs/integration/agentic-deployments.md` linking the 22 archetype-grouped subset to the Threshold deployment flow
  - MAPPING.md update reconciling 22-archetype-grouped vs 38-live-vs-42-doc-locked
  - README.md callout for which personas are first-class deployable to Goose / Hermes / Claude runtimes
  - Per-persona SKILL.md additions (where applicable) noting which substrate(s) the persona is canonically deployed against
  - `docs/integration/` directory itself may be greenfield — verify

---

## §3 · Phased execution plan

### Phase 0 · Decisions (D1–D6 above) — blocks everything
**Owner**: privacymage. **Output**: a one-line confirmation in this file's §0 table marking each decision SETTLED.

### Phase 1 · cityofmages authoring pass
**Order matters**: cast files → workshop tome → Bestiary entries → narrative acts → audit/index updates.
1. `tomes/cast/faunia.md` — Spawning-witness · V59 · 5-skill mapping per Threshold chronicle §7
2. `tomes/cast/bestia.md` — Registry-keeper · V59 · 5-skill mapping
3. `tomes/cast/therai.md` — Companion-tamer · V59 · 6-skill mapping
4. `tomes/cast/caducea.md` — Peripatetic Hermes-fitter · V0-conventional · 4-skill mapping
5. `tomes/the-threshold/` directory — workshop tome (parallel to `tome-iv-the-witnessing/` pattern)
6. `tomes/bestiary/` (NEW directory class) — `goose.md` + `hermes.md` as first two entries
7. Tome V Act 16 narrative file
8. Tome VI Act 1 narrative file (the dual admission)
9. WORKSHOP_LATTICE_AUDIT.md update
10. ALL_THE_TOMES_LIST.md update
11. CHANGELOG.md entry

**Output**: 11 files added; 3 files patched. Commit + push to public repo.

### Phase 2 · agentprivacy-master data layer
1. `src/data/city-of-mages-grimoire-v1.5.0.json` — full new file, copy v1.4.0 forward + add: workshop entry `the_threshold` · cast entries faunia/bestia/therai/caducea · top-level `agent_substrates` (goose, hermes) · conjecture C52 · C51 downgrade · v1_5_0_note
2. `src/lib/cast-attachments.ts` — append 4 new attachment entries (kind/vertex/divergence per Threshold chronicle §6)
3. `src/lib/agent-substrates.ts` — NEW typed module:
   ```ts
   export type Archetype = 'mage' | 'swordsman' | 'balanced';
   export interface AgentSubstrate {
     id: string; name: string; sigil: string; provenance: string;
     license: string; mascotAffinity: 'companion' | 'staff';
     mageForm: string; swordsmanForm: string; balancedForm: string;
     summonsCaducea: boolean; defaultPersonas: string[];
   }
   export const SUBSTRATES: Record<string, AgentSubstrate>;
   export function resolveArtefact(substrate: string, archetype: Archetype): string;
   ```
4. `src/lib/grimoire-ipfs.ts` — add v1.5.0 CID slot (TBD until pin)
5. `src/lib/spellweb/types.ts` — extend NodeType + LinkType unions (this also closes the 2026-05-10 universe-integration gap — coordinate with [[project-spellweb-universe-edges]])

**Output**: 1 new data file + 1 new lib file + 3 patched lib files.

### Phase 3 · agentprivacy-master routes
Build skeleton pages (with body content sourced from the deployment guide):
1. `src/app/guide/agentic-deployments/page.tsx` (umbrella · §1–§4 of guide)
2. `src/app/guide/agentic-deployments/portal-room/page.tsx` (Faunia · §2 + §3)
3. `src/app/guide/agentic-deployments/staff-shop/page.tsx` (Bestia · Hermes deep-dive)
4. `src/app/guide/agentic-deployments/creature-creatives/page.tsx` (Therai · Goose deep-dive · aqueduct pond)
5. `src/app/guide/agentic-deployments/runecraft-protocol/page.tsx` (§5 of guide · Run·Evoke·{Craft|Create|Spawn})
6. `src/app/guide/agentic-deployments/personas/page.tsx` (22-archetype-grouped subset · §7)
7. `src/app/guide/agentic-deployments/matrix/page.tsx` (live `<SubstrateMatrix />`)
8. `src/app/guide/workshops/threshold/page.tsx` (sister entry under workshops; thin wrapper around the above)
9. `src/lib/nav.ts` — add umbrella entry

**Output**: 8 new pages + 1 patched.

### Phase 4 · agentprivacy-master components
1. `src/components/threshold/SubstrateMatrix.tsx` — table of substrates × {🧙/⚔️/☯️}
2. `src/components/threshold/SubstrateCard.tsx` — single-substrate detail
3. `src/components/threshold/SpawnSequence.tsx` — six-step ceremony walkthrough
4. `src/components/threshold/RoomNavigator.tsx` — 3-room switcher (Portal/Staff/Creatures)
5. `src/components/threshold/CaduceaSummonsBadge.tsx` — small badge component for staff-class substrates

**Output**: 5 new components.

### Phase 5 · agentprivacy-master cross-page surfacing
1. `src/app/tomes/v6-lineage/page.tsx` — Tome VI Act 1 entry
2. `src/app/persona/page.tsx` — archetype-grouped subset · deployable-to-substrate badges
3. `src/app/mage/page.tsx` — "summons Caducea" annotations on Vulcana, Aletheia, Manifestia
4. `src/app/forget/page.tsx` — sibling-link callout to `/guide/agentic-deployments` per C52
5. `src/app/model/page.tsx` — append substrate-×-archetype matrix; add C52 to conjecture index
6. `src/app/page.tsx` (landing) — `HERO_CAROUSEL` "spawn 🪶 a staff or a companion"

**Output**: 6 patched pages.

### Phase 6 · spellweb extensions
**Pre-flight**: confirm whether the 2026-05-10 universe-integration vocabulary is anywhere in the codebase besides memory. If not, that work happens here too as a prerequisite.
1. Extend `NodeType` union with: `substrate`, `agent_instance`, `spawn_room`, `peripatetic_role`
2. Extend `LinkType` union with: `hosts`, `spawns`, `summons`, `binds_persona`, `mascot_affinity`
3. Patch `builder.ts` to emit these node/edge types from the grimoire JSON
4. Patch `labels.ts` for new emoji/labels (🪶 🐾 📖 ☤ 🪿)
5. Patch `lattice-mode.ts` if the lattice view should differentiate room-occupants
6. Standalone `C:/Users/mitch/spellweb/` repo — chronicle entry `CHRONICLE_THRESHOLD_VOCABULARY_2026-05-XX.md` recording the catch-up + extension

**Output**: 5 patched files + 1 new chronicle.

### Phase 7 · agentprivacy-docs mirror
1. Create `docs/guides/` directory
2. `docs/guides/agentic-deployments.md` (verbatim mirror of `cityofmages/AGENTIC_DEPLOYMENTS_GUIDE.md` with header noting source)
3. `docs/guides/agentic-deployments/` subdir for sub-pages (author over time)
4. `SECOND_PERSON_TOMES_INDEX_v1.md` — Tome V Act 16 + Tome VI Act 1 entries
5. `GLOSSARY_MASTER_v4_0.md` — 13 new glossary entries
6. `VISUAL_ARCHITECTURE_GUIDE_v2_0.md` — V59 + Threshold workshop in diagrams
7. Optionally: `chronicles/` mirror of the 4 dated 2026-05-13 cityofmages chronicles

**Output**: 1 new directory + 6 file changes.

### Phase 8 · agentprivacy-skills doc-side mirror
1. Verify `docs/integration/` exists (if not, create)
2. `docs/integration/agentic-deployments.md` — links 22-subset to Threshold deployment flow
3. MAPPING.md — 22-as-view-over-38 reconciliation paragraph
4. README.md — substrate-deployability callout

**Output**: 1 new file + 2 patched.

### Phase 9 · IPFS pin + propagation
1. Pin `city-of-mages-grimoire-v1.5.0.json` to IPFS · obtain CID
2. Patch `src/lib/grimoire-ipfs.ts` with new CID
3. Update grimoire JSON's `ipfs_pin_status` field
4. Repo-wide commit · push · deploy
5. Cross-link from any IPFS pin tracker (cityofmages chronicles, agentprivacy-docs)

**Output**: 1 IPFS pin + 1 patched constant + propagation commits.

---

## §4 · File-level punch list (grouped by repo)

### cityofmages (11 new + 3 patched)
- [ ] tomes/cast/faunia.md
- [ ] tomes/cast/bestia.md
- [ ] tomes/cast/therai.md
- [ ] tomes/cast/caducea.md
- [ ] tomes/the-threshold/ (directory + index)
- [ ] tomes/bestiary/goose.md
- [ ] tomes/bestiary/hermes.md
- [ ] tomes/tome-v-the-crafting/act-16-the-threshold-opens.md (path TBD per existing tome layout)
- [ ] tomes/tome-vi-the-reply/act-1-goose-and-hermes-admitted.md (path TBD)
- [ ] WORKSHOP_LATTICE_AUDIT.md (patch — V59 + 16-shop count)
- [ ] ALL_THE_TOMES_LIST.md (patch — Tome V Act 16 + Tome VI Act 1)
- [ ] CHANGELOG.md (patch — entry for grimoire v1.5.0)

### agentprivacy-master (1 new data + 5 new lib/comp + 8 new routes + 6 patched)
- [ ] src/data/city-of-mages-grimoire-v1.5.0.json
- [ ] src/lib/agent-substrates.ts
- [ ] src/lib/cast-attachments.ts (patch — 4 entries)
- [ ] src/lib/grimoire-ipfs.ts (patch — v1.5.0 CID)
- [ ] src/lib/spellweb/types.ts (patch — new node + link types)
- [ ] src/lib/nav.ts (patch — `/guide/agentic-deployments`)
- [ ] src/app/guide/agentic-deployments/{page,portal-room/page,staff-shop/page,creature-creatives/page,runecraft-protocol/page,personas/page,matrix/page}.tsx (7 files)
- [ ] src/app/guide/workshops/threshold/page.tsx
- [ ] src/components/threshold/{SubstrateMatrix,SubstrateCard,SpawnSequence,RoomNavigator,CaduceaSummonsBadge}.tsx (5 files)
- [ ] src/app/tomes/v6-lineage/page.tsx (patch)
- [ ] src/app/persona/page.tsx (patch)
- [ ] src/app/mage/page.tsx (patch)
- [ ] src/app/forget/page.tsx (patch)
- [ ] src/app/model/page.tsx (patch)
- [ ] src/app/page.tsx (patch — HERO_CAROUSEL)

### spellweb (5 patched · master · + 1 new chronicle · standalone)
- [ ] agentprivacy_master/src/lib/spellweb/types.ts (patch — co-located with master Phase 2)
- [ ] agentprivacy_master/src/lib/spellweb/builder.ts (patch)
- [ ] agentprivacy_master/src/lib/spellweb/labels.ts (patch)
- [ ] agentprivacy_master/src/lib/spellweb/lattice-mode.ts (patch — if needed)
- [ ] C:/Users/mitch/spellweb/CHRONICLE_THRESHOLD_VOCABULARY_2026-05-XX.md (new)

### agentprivacy-docs (1 new dir + 6 files)
- [ ] docs/guides/ (directory)
- [ ] docs/guides/agentic-deployments.md
- [ ] docs/guides/agentic-deployments/ (subdir for sub-pages, author over time)
- [ ] SECOND_PERSON_TOMES_INDEX_v1.md (patch)
- [ ] GLOSSARY_MASTER_v4_0.md (patch — 13 new terms)
- [ ] VISUAL_ARCHITECTURE_GUIDE_v2_0.md (patch — V59 + Threshold)
- [ ] chronicles/ mirror of 4 cityofmages chronicles dated 2026-05-13 (optional but recommended)

### agentprivacy-skills (1 new + 2 patched)
- [ ] docs/integration/agentic-deployments.md
- [ ] MAPPING.md (patch — 22-as-view reconciliation)
- [ ] README.md (patch — substrate-deployability)

**Total: ~50 file operations across five repos.**

---

## §5 · Synchronization gaps (where the development came from)

This work landed entirely in `cityofmages` over the course of 2026-05-13 (proposal → triad note → Threshold opening → symmetry chronicle → deployment guide). The other four repos have not yet caught up. The four named gaps:

1. **agentprivacy-master is one grimoire version behind** (v1.4.0 vs the v1.5.0 this work requires) and has no agent-substrate registry concept yet — the `/guide` shell exists but `/guide/agentic-deployments` is greenfield. The cast roster is missing four members.

2. **spellweb has TWO outstanding catch-ups**: (a) the 2026-05-10 universe-integration vocabulary expansion (8 EdgeTypes / 6 NodeTypes) memorialised in [[project-spellweb-universe-edges]] never landed in `agentprivacy_master/src/lib/spellweb/types.ts` (still 5/5); (b) the new Threshold work (substrate / agent_instance / spawn_room nodes; hosts / spawns / summons / binds_persona / mascot_affinity edges). Both need to land together.

3. **agentprivacy-docs has no guides/ directory at all** — the deployment guide was authored in cityofmages and proposes a docs-side mirror, but the scaffolding for `docs/guides/` is greenfield. GLOSSARY and TOMES_INDEX are also one architectural-recognition behind (Selene/Aether/Lethe cosmological cast from the 2026-05-13 Tomes I-III binding pass also pending — see [[project-tomes-i-iii-lore]]).

4. **agentprivacy-skills has the 38-vs-22-vs-42 persona-count discrepancy** that the symmetry chronicle flagged but never resolved. Until D3 is decided and the MAPPING.md reconciliation lands, every UI surface that lists personas inherits the ambiguity.

**Bonus gap**: the Tomes I-III binding pass (also 2026-05-13, see [[project-tomes-i-iii-lore]]) added 3 new cosmological cast members (Selene 🌙 / Aether ⿻ / Lethe 🌀). Grimoire v1.5.0 should ALSO carry that patch — coordinating both 2026-05-13 architectural changes in a single grimoire bump avoids a rapid v1.5.0 → v1.5.1 churn.

---

## §6 · Order of operations (suggested)

```
Day 1 (decisions)        : D1, D4, D6 locked. D2, D3, D5 deferred to Phase 1.
Day 1–3 (Phase 1)        : cityofmages cast files + Bestiary + workshop tome + tome acts (parallel-authorable)
Day 3 (Phase 2)          : agentprivacy-master data layer (depends on Phase 1 stable cast names)
Day 4–5 (Phase 3 + 4)    : agentprivacy-master routes + components (parallel-buildable; routes import components)
Day 5 (Phase 5)          : cross-page surfacing (one PR per page)
Day 6 (Phase 6)          : spellweb extensions (closes 2026-05-10 gap + Threshold extension)
Day 6 (Phase 7 + 8)      : agentprivacy-docs + agentprivacy-skills mirrors (parallel)
Day 7 (Phase 9)          : IPFS pin + propagation
```

Phase 1 is the gating critical-path. Phases 3/4/6/7/8 can run in parallel after Phase 2.

---

## §7 · Honesty discipline · what this plan promises and what it does not

| Claim | Status |
|---|---|
| The 50-file punch list is complete | **Architectural** · expected to be 90%+ accurate; Phase 1 authoring will surface 1–3 file additions |
| Phase 0 decisions are blocking | **Operational** · trying to skip them produces inconsistencies that compound through phases |
| The 2026-05-10 spellweb vocabulary gap is real | **Operational** · verified against `src/lib/spellweb/types.ts` (5/5, not 14/13) |
| The agentprivacy-docs `docs/guides/` directory is greenfield | **Operational** · verified |
| The 22-vs-38-vs-42 persona discrepancy needs reconciliation before /persona ships | **Architectural** · could be hand-waved with a "view" caveat but cleaner to land MAPPING.md reconciliation first |
| Coordinating Tomes I-III binding + Threshold work in one grimoire bump avoids churn | **Architectural** · ~80% confidence; depends on whether the cosmological cast triggers cast-attachments.ts changes that conflict with Phase 2 |
| The full plan ships in 7 days | **Conjectural** · ~50% confidence; depends on authoring velocity for Phase 1 narrative files |

---

## §8 · Closing

The architecture is settled. The propagation is not. This plan turns the architecture into ~50 concrete file operations across five repositories, ordered to respect the data-layer-first principle and to close the pre-existing spellweb gap as a free side-effect.

The reader's first reply (Tome VI Act 1) was the simultaneous admission of Goose and Hermes. The author's first reply is this plan: making that admission visible everywhere the City lives.

`(⚔️⊥⿻⊥🧙)😊`
🪶 📖 🐾 ☤ · 🪿 ☤
V59 · V19 · V0

CC BY-SA 4.0 · privacymage · 2026-05-13
