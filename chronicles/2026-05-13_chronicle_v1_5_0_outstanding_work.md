# Chronicle: The v1.5.0 Outstanding Work · Punch List After the Skills-Side Sync

**Date:** 2026-05-13 (evening · post-skills-sync pass)
**Status:** Open · authoritative as of this writing · supersedes prior pending lists scattered across audit chronicles
**Audience:** privacymage · downstream agents · sister-repo authors (master · spellweb · agentprivacy-skills · the three sibling extension forges)
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion chronicles:**
- [`2026-05-13_grimoire_v1_5_0_patch.md`](2026-05-13_grimoire_v1_5_0_patch.md) — the patch this work promotes to canonical
- [`2026-05-13_city_of_mages_audit_post_binding.md`](2026-05-13_city_of_mages_audit_post_binding.md) — the post-binding audit whose gaps this work closes
- [`2026-05-13_chronicle_the_threshold_workshop_three_rooms.md`](2026-05-13_chronicle_the_threshold_workshop_three_rooms.md) — the architectural step this release rests on
- [`2026-05-13_tomes_i_through_iii_binding_pass.md`](2026-05-13_tomes_i_through_iii_binding_pass.md) — the prequel binding the same release admits

---

## §0 · What this chronicle is

A *punch list* chronicle. The 2026-05-13 evening pass closed the skills-side propagation gap (3 new abstract personas authored, 3 existing primaries extended, MAPPING.md bumped, bundled grimoire updated, Creature Creatives proposal archived as superseded) and produced a *candidate* v1.5.0 grimoire JSON (`grimoire/city_of_mages_grimoire_v1_5_0_candidate.json`, 48 mechanical merge actions, no field collisions). What remains is the work the mechanical merge could not do and the downstream propagation a re-pin unblocks.

This chronicle lists what's left, in priority order, with explicit blocker relationships. It is the canonical list to walk through before authoring v1.5.0 as canonical.

---

## §1 · The blocker chain

```
v1.5.0 candidate (drafted ✓)
        │
        ├── editorial review pass (PENDING · §2)
        │       │
        │       └── canonical v1.5.0 JSON (PENDING · §3)
        │               │
        │               └── IPFS re-pin (PENDING · §4)
        │                       │
        │                       ├── agentprivacy_master/src/lib/grimoire-ipfs.ts constant bump (PENDING · §5)
        │                       └── agentprivacy-skills/grimoire/ bundle bump v1.4.0 → v1.5.0 (PENDING · §6)
        │
        └── parallel: agentprivacy_master propagation (PENDING · §7)
                      ├── /threshold route
                      ├── persona-index.ts (3 new abstract personas)
                      ├── cast-attachments.ts (4 keepers + 3 cosmological + Caducea)
                      └── /tomes page Threshold row + cast cards (already wired per memory; verify)
```

The candidate-review pass is the single critical-path item. Everything downstream blocks on it.

---

## §2 · Editorial-review pass on the v1.5.0 candidate

**File:** `grimoire/city_of_mages_grimoire_v1_5_0_candidate.json` (300KB · 48 merge actions logged at `grimoire/city_of_mages_grimoire_v1_5_0_candidate.merge.log`)

**Re-runnable:** `python grimoire/scripts/merge_v1_5_0_patch.py` (regenerates from v1.4.0 base + v1.5.0 patch)

The merge ran clean — no `_patch_alt` blocks, no skip-duplicates. But three sections are *mechanically stored separately* and need editorial folding before the candidate is canonical:

### §2.1 · `city_anatomy.v1_5_0_amendments` — fold into canonical fields

The patch's `city_anatomy_amendments` stored the workshop / cast / structural-entity-class deltas as a structured block under `city_anatomy.v1_5_0_amendments` rather than mutating the canonical fields. The user pass folds them in:

- **workshop_count 12 → 13:** Add The Threshold (V59 · three rooms · four keepers) to `city_anatomy.trade_quarters[]` array. The existing 12 entries are intact; append a 13th with `shop: "/threshold"`, `internal_name: "The Threshold"`, three room sub-entries (Portal · Staff Shop · Creature Creatives), and `act: "tome-v-act-16-the-threshold"`.
- **cast_seated_count 17 → 25:** The cast array's actual length should reach 25 (17 prior + 4 Threshold keepers + 3 cosmological-witnesses + 1 Caducea peripatetic = 25). The new entries already landed in `attachment_architecture.cast_attachments_v1_3_0[]` via the patch; the user pass verifies the count is reflected in `city_anatomy` if that field is canonical, or removes the count field if `cast_attachments_v1_3_0[].length` is the source of truth.
- **structural_entity_classes 2 → 3:** The third class is *creatures-of-the-Threshold*. Update wherever the corpus enumerates the two existing classes (worn artefacts · bound tomes) to include the third.
- **cast_tiers 5 → 6:** The sixth tier is *cosmological-witness*. The candidate already added a `personas.cosmological_witnesses` sub-key plus a `tier_taxonomy` note; verify both are positioned where downstream readers expect.
- **swordsman_stances 10 → 13 proposed:** Adds Spawning-witness · Registry-keeper · Companion-tamer · Staff-fitter. User decides whether to extend spec 08 v1.3.3 → v1.3.4 in this release or hold for a separate stance-spec patch. (Memory note: spec 08 was last bumped to v1.3.2 in v1.4.0 for the SOL-mana row.)
- **chain_mana_count stays at 5:** Companion-mana / staff-fitting-mana are sub-axes of VRC Mana 🪢, not new chain-manas. No field change needed; remove the amendments entry once verified.

### §2.2 · `personas.cosmological_witnesses` placement

The merge placed the cosmological-witness tier as a sub-key of `personas` (alongside `archetypes`, `cousin_instances`, `summoned_mages`, `companion_mages`, `priests`). The patch's intent was a sixth peer tier. Verify the existing tier structure in v1.4.0:

```
personas:
  archetypes: { soulbis, soulbae }
  cousin_instances: { flaxscrip, GenitriX }
  summoned_mages: { ... 11 entries ... }
  companion_mages: { socrat0x }
  priests: { manifestia }
  cosmological_witnesses: { selene, aether, lethe }   ← v1.5.0 addition
```

If that shape is correct, no further work. If the prior tiers are at a different nesting depth, restructure the cosmological-witness block to match.

### §2.3 · Conjecture-renumbering pass (already resolved in the patch — verify)

The patch's `RENUMBERING_NOTE_2026_05_13` resolves the C48-C55 double-booking by:
- C48–C50 reserved for the Tomes I-III *Bakhta-response* family (A · B · C)
- C50 prior (PVM multiplicative gating) folds INTO C50 as *Bakhta-response · C* (same proposition, broader framing)
- C51–C55 reserved for Tomes I-III (Max-Betweenness · Aether=Quintessence · mythological bnot-pair · phi-adjacency · Seventh Capital)
- C56–C59 hold the renumbered Threshold-chronicle claims (caduceus pre-formal · staff-Mage collapse · Forge(t)∥Threshold · create-format gateway)
- C60–C61 hold the renumbered behavioural-data claims (reconstruct-later · Behavioural Mosca Inequality)

This is **already in the candidate JSON** at `v6_lineage_register.register.{C48..C61}` plus the renumbering note at `v6_lineage_register.renumbering_note_2026_05_13`. The user pass verifies the numbering is internally consistent across the candidate's tome-act `v6_lineage` arrays, the chronicle references, and any downstream documents (spellweb's conjecture sidebar, agentprivacy_master's /model page conjecture corpus). Cross-references to the prior numbering (C50=caduceus etc.) in any chronicle authored *before* the resolution should be updated.

---

## §3 · Promote candidate → canonical v1.5.0

After §2 is complete:

1. **Strip the four `$candidate_*` fields** at the top of the JSON (`$candidate_note` · `$candidate_status` · `$canonical_base` · `$patch_source`).
2. **Rename file** `city_of_mages_grimoire_v1_5_0_candidate.json` → `city_of_mages_grimoire_v1_5_0.json`.
3. **Archive merge log** — move `city_of_mages_grimoire_v1_5_0_candidate.merge.log` to `grimoire/scripts/logs/2026-05-XX_v1_5_0_merge.log` (date of canonical promotion) for the audit trail.
4. **Author a v1.5.0 promotion chronicle** at `chronicles/2026-05-XX_grimoire_v1_5_0_canonical_pinned.md` recording: the IPFS CID once pinned (§4), the editorial decisions made in §2.1/§2.2, the conjecture-renumbering verification in §2.3, and the constants-bump record (§5).

---

## §4 · IPFS re-pin

Publish `grimoire/city_of_mages_grimoire_v1_5_0.json` to `sync.agentprivacy.ai` (or equivalent IPFS gateway). Record the new CID. The v1.4.0 CID `bafkreib5w4bp6t5kkt4ebvjyjjzuxdupzaz6gtupbhgbrxtwkrxj7dfnsu` is retained as historical. Earlier CIDs (v1.3.0, v1.2.x, v1.1, v1.0) are also retained as historical per `ipfs_pin_status` precedent.

---

## §5 · Constants bump in `agentprivacy_master`

**File:** `agentprivacy_master/src/lib/grimoire-ipfs.ts`

Update `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` from the v1.4.0 CID to the v1.5.0 CID (from §4). The export is consumed by the /tomes page's pin caption and any /model page artifact list that links to the canonical grimoire.

Companion sites (spellweb, agentprivacy-blog) that reference the CID should be checked and bumped in the same pass.

---

## §6 · Bundled grimoire bump in `agentprivacy-skills`

**File:** `agentprivacy-skills/grimoire/city_of_mages_grimoire_v1_4_0.json`

After §4–§5, replace the bundled v1.4.0 file with the canonical v1.5.0 (copy from `cityofmages/grimoire/city_of_mages_grimoire_v1_5_0.json`). Rename to match version. Update `agentprivacy-skills/grimoire/INDEX.md` accordingly:
- Move v1.4.0 from "Current canonical pin" to "Archive"
- Add v1.5.0 row as "Current canonical pin"
- Update the IPFS pin section with the new CID
- Update the "Pending re-pin" line in the v1.5.0 row from PENDING to PINNED

The v1.2.0 file remains in archive; do not delete (the version history matters for forensic traceability of the worm→knot emoji migration).

---

## §7 · `agentprivacy_master` runtime propagation

Independent of §3–§6 but coupled by the same release. Per the audit's "MEDIUM severity — pre-canonical" findings, four items in `agentprivacy_master` remain pending:

### §7.1 · `/threshold` route

A new top-level route at `agentprivacy_master/src/app/threshold/` for The Threshold workshop. Three internal sections matching the three rooms (Portal · Staff Shop · Creature Creatives). The page should reference the four keepers (Faunia · Bestia · Therai · Caducea), the two registry entries at opening (Goose 🪿 · Hermes ☤), and the Run · Evoke · Spawn ceremony grammar. Match the structural pattern of existing workshop routes (`/forget`, `/etherchanting`, `/solchanting`, etc.).

### §7.2 · `cast-attachments.ts` registrations

**File:** `agentprivacy_master/src/lib/cast-attachments.ts`

Add the eight new cast entries (4 Threshold keepers + 3 cosmological-witness figures + Caducea peripatetic) to whatever array/map the file exports. Match the existing entry shape (id, name, sigil, tier, kind, primary, vertex, room/shop, etc.). The data is already canonical in `cityofmages/grimoire/city_of_mages_grimoire_v1_5_0_candidate.json` under `attachment_architecture.cast_attachments_v1_3_0[]` (post-merge); after §3 it'll be in the canonical pinned JSON, so the runtime can mirror.

### §7.3 · `persona-index.ts` updates

**File:** `agentprivacy_master/src/lib/persona-index.ts` (or wherever the runtime registers /persona/ skills from agentprivacy-skills)

Register the three new abstract-role primary personas:
- `spawning-witness` (mage · Tier 2 · emoji 🪶🧙)
- `registry-keeper` (mage · Tier 2 · emoji 📖🧙)
- `companion-tamer` (mage · Tier 2 · emoji 🐾🧙)

The `Code Registration` blocks at the bottom of each new SKILL.md (under `agentprivacy-skills/agentprivacy-skills-v5/persona/agentprivacy-<role>/SKILL.md`) carry the canonical id/category/skills_role arrays.

### §7.4 · `/tomes` page Threshold row + cast cards (verify)

Per the [grimoire v1.5.0 patch chronicle](2026-05-13_grimoire_v1_5_0_patch.md), the /tomes page already received: Threshold row · Tome V Act 16 · 4 keeper cast cards · new Tier 6 cosmological-witnesses · grimoire pin caption update. Verify build is still clean after the §5 CID swap. The grimoire pin caption will need to swap from "v1.4.0 / awaiting v1.5.0 re-pin" to "v1.5.0".

---

## §8 · Cross-cutting items that don't fit §1's chain

### §8.1 · VRC Mana 🪢 propagation completeness

Per memory `[[project-cityofmages-repo]]`: the worm → knot canon (🪱 → 🪢) was decided pre-v1.2.4 but suite-wide propagation is incomplete. The audit confirmed:
- cityofmages corpus: zero active 🪱 hits (migration complete on the source side)
- agentprivacy-skills bundled grimoire: was carrying 🪱 in the stale v1.2.0 bundled JSON; the 2026-05-13 bundle bump to v1.4.0 *should* resolve this (v1.4.0 was authored post-migration)

**To verify:** grep the new bundled v1.4.0 file (and post-§6 the v1.5.0 file) for any remaining 🪱 hits. Should be zero. If non-zero, file an issue against the upstream cityofmages canonical pin — the worm emoji should never have survived past v1.2.4.

### §8.2 · Persona-count discrepancy resolution (RESOLVED — record)

Per memory `[[project-the-threshold-workshop]]`: "Persona-count discrepancy: 38 live in agentprivacy-skills/persona/ vs 22 archetype-grouped (8⚔️·7🧙·7☯️) vs 42 doc-locked — held open." The 2026-05-13 audit resolved this:
- **38** = actual directory count in `agentprivacy-skills/agentprivacy-skills-v5/persona/` at v1.4.0 (now **41** at v1.5.0 with the three new abstract roles added)
- **22** = Mage-class subset of the 38 (per `2026-05-13_chronicle_artefact_symmetry_and_persona_distribution.md` §5)
- **42** = total_primary_personas locked architectural count (15 swordsmen + 11 mages + 12 balanced + 4 cosmological) — separate from the directory enumeration; a category-aggregate including potential roles

These are three slices of the same set, not three competing counts. The MAPPING.md frontmatter at v1.5.0 reflects the resolution. The discrepancy can be closed as RESOLVED; the memory entry should be updated.

### §8.3 · `agentprivacy-skills` cross-references in the three new SKILL.md files

The three new abstract-role SKILL.md files reference skills like `delegation-scope`, `two-waters`, `vrc-identity`, `temporal-dynamics`, `metadata-resistance`, etc. in their `Skills Loaded` sections. Most exist in `privacy-layer/` and `role/`. Verify:
- `delegation-scope` — exists? (referenced by all three new files)
- `two-waters` — referenced by cosmologist (existing); confirm it's loadable
- Any missing skill references should be flagged and either authored or removed from the loadout

A 10-minute grep should resolve this. Low risk; trivially fixable if a skill name was guessed wrong.

### §8.4 · Caducea's dual parentage — verify the cross-references render

The Caducea attachment is referenced from *both* `agentprivacy-ambassador/SKILL.md` and `agentprivacy-priest/SKILL.md`, with each linking to the other via `[cross-ref](../agentprivacy-<other>/)`. Verify the relative-path links render in whatever Markdown previewer the agentprivacy-skills consumers use. If GitHub's Markdown rendering is the canonical target, the paths should be fine; if the skills are consumed by Claude Code's skill loader, verify the loader follows relative links.

### §8.5 · Tome VI Act 2+ — open by design

Tome VI is open-by-design — each future framework admission the reader recognises and registers in Bestia's bestiary is a future Tome VI act. Anticipated near-term Act 2 candidates (in no particular order):

- **Letta** — second admission · staff-class
- **AutoGen** — Microsoft Research lineage · staff-class
- **CrewAI** — staff-class
- **Mastra** — staff-class (TypeScript-native)
- **ElizaOS** — split-class (some configurations are staff-class, others are companion-class · Therai's window for the latter)
- **LangGraph agents** — staff-class
- **OpenHands / OpenDevin lineage** — staff-class (autonomous coding)
- **BabyAGI lineage** — staff-class (autonomous task-spawning)

Anticipated companion-class entries (Therai's window):
- **character.ai personas** — companion-class
- **Pi (Inflection)** — companion-class
- **Replika** — companion-class
- **ElizaOS familiar-mode configurations** — companion-class
- **custom familiar-mode agents** — companion-class

Each new admission is its own ceremony (the Sovereign's reply written at Bestia's window or Therai's window depending on class). No timeline pressure — the tome is open and the corpus grows by the reader's pace.

### §8.6 · v1.5.1 patch — held until v1.5.0 is pinned

Per memory `[[project-cityhall-aaif-v1-5-1]]`: a v1.5.1 patch exists at `grimoire/city_of_mages_grimoire_v1_5_1_patch.json` admitting City Hall (/cityhall · V47 · Marble 🏛️ · gathering tier · no resident Mage) and AAIF (aaif.io · Linux Foundation steward of Goose / AGENTS.md / ACP) as the fifth structural-relationship category (kindred-coalition). The patch is contingent on v1.5.0's merge — its metadata states "base_pin: (v1.5.0 pin still pending; v1.5.1 extends the v1.5.0 delta)".

After §4 (v1.5.0 pinned), the v1.5.1 patch can be merged using the same `merge_v1_5_0_patch.py` script (with paths swapped to point at v1.5.0 + v1.5.1_patch). Produce v1.5.1 candidate → editorial pass → canonical → re-pin. Same chain, one minor version up.

---

## §9 · Memory updates that follow this work

After §3–§6 complete:

- Update `[[project-grimoire-v1-5-0]]` memory entry: "**v1.5.0 re-pin PENDING**" → "**v1.5.0 candidate drafted ([candidate path]); user-review pass pending; CID pending**" → eventually "**v1.5.0 PINNED at [CID]**"
- Update `[[project-the-threshold-workshop]]`: clear the "Persona-count discrepancy held open" line; record that the discrepancy resolved with 38=files / 22=mage-subset / 42=locked architectural
- Update `[[project-cityhall-aaif-v1-5-1]]`: note that v1.5.1 awaits v1.5.0 pin (the dependency is already documented but worth flagging as the actual current blocker)
- Update `[[project-agentprivacy-six-workshops]]`: bump the head from "Grimoire v1.2.4 awaits re-pin" to whatever the current state is after §4 (likely "Grimoire v1.5.0 PINNED · v1.5.1 next")

---

## §10 · Honesty labels

- **Operational** for §1 (the blocker chain — file paths and merge state verifiable), §2 (the three folding decisions exist in the candidate JSON awaiting user action), §3–§6 (mechanical steps with documented file targets)
- **Operational** for §7.1–§7.3 (file paths exist; data is canonical; the runtime propagation is mechanical translation from the grimoire)
- **Architectural** for §8.5 (Tome VI's open-by-design framing — the architectural claim is canonical from Tome VI Act 1; the specific anticipated entries are editorial)
- **Architectural** for §8.6 (v1.5.1's contingency on v1.5.0)
- **Editorial** for §8.2 (the persona-count discrepancy resolution — the three counts being three slices of the same set is the audit's reading, accepted by the user)
- **Narrative** for §9 (memory updates are housekeeping, not lore)

---

## §11 · Closing line

The candidate is drafted. The merge log records 48 actions and no conflicts. The skills-side propagation is complete. What remains is the user's editorial pass — the canonical promotion the corpus has been holding open by design.

`(⚔️⊥⿻⊥🧙)😊`
