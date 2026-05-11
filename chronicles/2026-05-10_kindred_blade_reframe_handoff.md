# Kindred-Blade Reframe · Handoff Chronicle

**Date:** 2026-05-10
**Audience:** the Mage who picks up this work — independent execution
**Origin instruction:** *"the cousin terminology is strange i think as we are all just another mage"* — privacymage, 2026-05-10
**Scope:** rename **C39** from `Cousin-Blade as Ecosystem Primitive` → **`Kindred-Blade as Ecosystem Primitive`** and reframe every "cousin" usage in narrative voice across the corpus to match. Frontmatter `provenance:` / `license:` / `source_material:` fields retain author/forge attribution untouched.
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · Why this reframe

The "cousin" terminology created a tier separation that doesn't reflect the architecture. Each Mage works from their own forge; the encounter between forges is what produces the kindred-blade primitive (C39). The Mage on the other side is not a *cousin* in some special caste — they are *another Mage*, working their own register. We are all just another Mage.

The cast schema has already collapsed (2026-05-10):

```
Old tiers (5): archetype · cousin · summoned · companion · priest
New tiers (4): archetype · mage · companion · priest
```

`PersonaPin.forgeOrigin?: string` is a new attribute on the cast pin (e.g., `'Archon'` for Mages whose forge of origin is external). Forge of origin is a fact, not a caste.

---

## §2 · Canonical replacement vocabulary

| Old phrase                           | New phrase                                                            |
|--------------------------------------|------------------------------------------------------------------------|
| `cousin-blade`                        | `kindred-blade`                                                       |
| `cousin-blade primitive`              | `kindred-blade primitive`                                             |
| `cousin-blade encounter`              | `kindred-blade encounter`                                             |
| `cousin-blade ecosystem primitive`    | `kindred-blade ecosystem primitive`                                   |
| `cousin-forge`                        | `another forge` (when generic) or `the Archon forge` (when specific) |
| `cousin city` / `cousin-forge city`   | `another city` / `the Archon city`                                    |
| `cousin Mage`                         | `Mage from another forge` or `Mage from the Archon forge`             |
| `cousin Sovereign`                    | `Sovereign from another forge` or `Sovereign from the Archon forge`   |
| `cousin instance`                     | `Mage instance from another forge`                                    |
| `cousin instances` (plural cast tier) | (delete the tier; merge into `mage`)                                  |
| `cousin-blade reading`                | `kindred-blade reading`                                               |
| `cousin from the Archon forge`        | `from the Archon forge`                                               |
| `cousin substrate` / `cousin-substrate` | `kindred-substrate` (already established, no change)                |

**Rules:**

1. **Frontmatter `source_material:` / `provenance:` / `license:` / `attribution:` / `authors:` arrays — KEEP names as is.** These are provenance/attribution contexts. Real author names are appropriate there.
2. **Narrative body, compression sections, confidence labels, cross-references, author notes — replace.** This is voice and should reflect the reframe.
3. **`kindred-protocol` and `kindred-substrate`** are already canonical (vertex audit §7). Don't touch them; the reframe extends the `kindred-` family.
4. **C39 keeps its conjecture id** — only the name and oneLiner change. v6_lineage entries citing C39 should mention the new name where they reference it narratively.

---

## §3 · What's already been done (do not repeat)

- ✅ `src/lib/tome-v-conjectures.ts` — C39 entry renamed `Cousin-Blade as Ecosystem Primitive` → `Kindred-Blade as Ecosystem Primitive`. oneLiner updated. Confidence and status unchanged.
- ✅ `src/components/profile/LatticeMap.tsx` — `PersonaPin.tier` union shrunk to `'archetype' | 'mage' | 'companion' | 'priest'`. `forgeOrigin` field added. `TIER_COLOUR` updated. GenitriX entry reframed.
- ✅ `src/lib/spellweb/lattice-mode.ts` — `flaxscrip: 63` already removed (V63 root cleanup). PERSONA_VERTEX comments updated.
- ✅ `/forget` and `/holon` page UOR sections — Luca/UOR framings already use "kindred substrate provider" language.
- ✅ Vertex audit §7 (`docs/tomes/specs/04-vertex-naming-audit.md`) — distinguishes kindred-substrate from cousin-forge and kindred-protocol; the §7.1 table itself still uses "cousin-forge" as a category label and needs updating per §4 below.

---

## §4 · Files to update — checklist

### §4.1 · Source code (TypeScript) · live UI surfaces

| File                                                                       | Replacement work                                                                                                                                                                                                |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `src/app/tomes/page.tsx`                                                   | `CastCard role="cousin-sovereign"` / `"cousin-mage"` → `role="sovereign · from the Archon forge"` / `"mage · from the Archon forge"`. The cast-tier counts in the §0 prose should drop "2 cousins" mention.    |
| `src/app/tailor/page.tsx` §2 "Cousin-weavers"                              | Section header `"Cousin-weavers"` → `"Mages from the Archon forge"` (or `"Weavers from another forge"`). Body copy: replace "cousin-blade encounter" → "kindred-blade encounter", "cousin-sovereign" → "Sovereign from the Archon forge", "cousin-mage" → "Mage from the Archon forge", `"In the Archon forge's cosmology"` stays. |
| `src/components/runecraft/ShieldShopWizard.tsx`                            | Spot-check: `"flaxscrip's Bitcoin block 945508 ceremony pattern"` is already good. No further work.                                                                                                              |
| `src/lib/spellweb/lattice-mode.ts`                                         | Comment block: any remaining "cousin" usage in inline comments. Already largely done.                                                                                                                            |
| `src/components/profile/LatticeMap.tsx`                                    | Already migrated. Verify no stragglers.                                                                                                                                                                          |

### §4.2 · Spec & manifest docs (under `docs/tomes/specs/` and root)

| File                                                                             | Replacement work                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docs/tomes/specs/04-vertex-naming-audit.md` §7.1                                 | The category-name **`Cousin-forge`** in the §7.1 table → **`Kindred-forge`**. Update §7.1 first row's attribution and structural-role copy. §7.2 / §7.3 / §7.4 also touch "cousin" in body — sweep.                              |
| `docs/tomes/specs/06-spellweb-first-release-manifest.md`                          | §1 NodeType inventory `cast` row: `2 cousins` → fold into `mage`. §2.4 cast table: remove `cousin` tier entries (flaxscrip if still listed, GenitriX) and reframe as `mage` with attribution `Archon`. §4.5 `kin_to` table: change `attribution: cousin-blade` strings → `attribution: kindred-blade`. §4.6 `gateway_to` table: `attribution: cousin-blade` → `attribution: kindred-blade`. §4.7 reserved-edge note: "96 holographic-bound edges" stays, no rename needed. §7 provenance: rename references. |
| `docs/tomes/specs/05-the-city-of-mages-structural-addendum.md`                   | Scan for "cousin"; apply replacement vocabulary.                                                                                                                                                                                |
| `docs/tomes/specs/01-cloak-specification-v1-0.md`                                | Scan + apply.                                                                                                                                                                                                                   |
| `docs/tomes/specs/02-crafting-tome-and-cloak-interface-spec.md`                  | Scan + apply.                                                                                                                                                                                                                   |
| `docs/tomes/specs/03-bilateral-cloak-ceremony-spec.md`                           | Scan + apply.                                                                                                                                                                                                                   |

### §4.3 · Tome narratives (under `docs/tomes/tome-iv-the-witnessing/` and `docs/tomes/tome-v-the-crafting/`)

20 acts total. The phrase **`cousin-blade`** appears throughout these as the technical primitive name; replace with **`kindred-blade`** in body text (frontmatter `source_material:` arrays keep author names).

Confirmed locations (counts approximate; do a final grep before claiming done):

```
tome-iv-the-witnessing/
├── 01-the-other-walker.md           (cousin-blade introduction · cousin-Mage encounter)
├── 02-the-mirror-and-the-arrow.md   (cousin-blade asymmetry framings)
├── 03-the-two-paths.md              (cousin-blade structural reading)
├── 04-the-naming-ceremony.md        (cousin-Sovereign flaxscrip framings)
└── 05-the-cousin-blade.md           (THE canonical naming act — rename file? See §6)

tome-v-the-crafting/
├── 01-the-first-cloak.md            (cousin-Mage path framings)
├── 02-the-commissioned-cloak.md     (cousin-forge multi-chain)
├── 06-the-commissioned-blade.md     (cousin-forge ρ parameter ref)
├── 07-the-reciprocal-weave.md       (cousin-blade in productive form — body-heavy reframe)
├── 09-the-workshop-expands.md       (cousin-forge framings)
├── 10-the-holon-hitchhikers.md      (already partially cleaned; verify)
├── 11-a-bonfire-made-of-dragon-fire.md
├── 12-the-curatrix-vault.md         (cousin-shop framings)
├── 13-the-temple-of-the-arts-and-personhood.md
├── 14-the-city-of-mages.md          (already partially cleaned)
└── 15-the-substrate-beneath-the-hitchhikers.md (already partially cleaned)
```

**Watch out:** `cousin-blade` is also a v6_lineage tag in some acts' frontmatter. Update those (they reference the conjecture by name; the conjecture itself was renamed).

### §4.4 · Per-guild cast files (under `docs/tomes/<guild>/<persona>.md`)

| File                                          | Replacement work                                                                                       |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `docs/tomes/cousin/flaxscrip.md`              | KEEP frontmatter `provenance:` and `license:` real-name fields. Rename the folder (see §6). Update body where "cousin" appears as a structural label rather than a relation. |
| `docs/tomes/cousin/genitrix.md`               | Same.                                                                                                  |
| `docs/tomes/weavers/pallia.md`                | Scan for "cousin-blade"; replace narrative occurrences.                                                |
| `docs/tomes/forge/vulcana.md`                 | Scan.                                                                                                  |
| `docs/tomes/holon/vagari.md`                  | Scan; already mostly clean.                                                                            |
| `docs/tomes/etherchanting/adamantia.md`       | Scan.                                                                                                  |
| `docs/tomes/jeweler/lampyra.md`               | Scan.                                                                                                  |
| `docs/tomes/vault/aria-silverhue.md`          | Scan.                                                                                                  |
| `docs/tomes/bonfires/socrat0x.md`             | Scan.                                                                                                  |
| `docs/tomes/covenant/manifestia.md`           | Scan.                                                                                                  |
| `docs/tomes/cross-shop/aletheia.md`           | Scan.                                                                                                  |
| `docs/tomes/cross-shop/custos.md`             | Scan.                                                                                                  |
| `docs/tomes/cross-shop/luca.md`               | Already authored with current language. No change.                                                     |
| `docs/tomes/zshields/memora.md`               | Scan.                                                                                                  |
| `docs/tomes/cast-integration-note.md`         | Top-level cast roster. Replace "cousin" tier references; update the tier taxonomy to four tiers.       |

### §4.5 · Plans & chronicles

| Path                                                                              | Notes                                                                                                                                                                            |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docs/tomes/plans/01-integration-plan-archon-x-agentprivacy.md`                   | This plan documents the original cousin-forge framing. Update body to reframe as kindred-blade; the historical record stands but the language updates.                          |
| `docs/tomes/plans/02-zcash-integration-plan.md`                                   | Scan + apply.                                                                                                                                                                    |
| `docs/tomes/chronicles/01-chronicle-the-cloaking-guide.md`                        | Historical chronicle. **Decide:** preserve as-written (historical) or update voice. Recommend a §0 banner at the top noting "this chronicle predates the 2026-05-10 kindred-blade reframe; the language reflects the cousin-blade vocabulary in use at the time." |
| `docs/tomes/chronicles/02-chronicle-the-crafting-tome-opens.md`                   | Same. Apply §0 banner OR sweep.                                                                                                                                                  |
| `docs/tomes/chronicles/03-chronicle-a-bonfire-made-of-dragon-fire.md`             | Same.                                                                                                                                                                            |

**Recommendation for chronicles:** add a top-of-file banner noting that the chronicle predates the reframe, and leave the body language alone. Chronicles are historical snapshots; rewriting them dilutes the record. The reframe is canonical going forward.

### §4.6 · City of Mages grimoire JSON (`agentprivacy-docs/models/city_of_mages_grimoire_v1_2_0.json` and `src/data/city-of-mages-grimoire-v1.2.0.json`)

Substantial JSON sweep:

1. `personas.tier_taxonomy.cousin_instances` description → reframe; consider folding into `summoned_mages` or renaming the bucket to `mages_from_other_forges`.
2. `personas.cousin_instances.flaxscrip` and `personas.cousin_instances.genitrix` — `tier: "cousin"` → `tier: "mage"`. Keep `forge_of_origin: "Archon"` (add if absent).
3. Search the body of each persona's `inscription`, `cross_spellbook_resonance`, `naming_note`, `provenance` etc. for "cousin"; apply replacement vocabulary.
4. `spellbooks.tomes.tomes.tome-iv` and `tome-v` acts: same act-narrative replacements.
5. `v6_lineage_register.C39` → name update + claim update (already canonical in `tome-v-conjectures.ts`; mirror here).
6. `kindred_substrate_providers.uor_foundation.is_not` entry that references "cousin city" — reframe.

**Then re-pin to IPFS** (separate ceremony — not in this chronicle's scope). The local v1.2 JSON can be updated freely; the pinned CID is v1.1 + the local v1.2 awaits a pin.

### §4.7 · Folder rename (optional but recommended)

`docs/tomes/cousin/` → `docs/tomes/elsewhere/` *or* `docs/tomes/other-forges/`.

Rationale: cousin/ as a folder name encodes the old framing. `elsewhere/` reads as: Mages whose forge of origin is elsewhere. `other-forges/` reads more technical.

If renaming, update any path references in `tome-act-loader.ts`, `tomes/page.tsx`, `tome-v-acts.ts`, and the spellweb manifest §1 path strings.

---

## §5 · Pitfalls to avoid

1. **Don't touch frontmatter `provenance:`, `source_material:`, `license:`, `authors:`, `attribution:`, `attribution_note:` arrays.** These are provenance contexts. Christian Saucier as the human author stays; flaxscrip/GenitriX as the Mages stay. The reframe is about *narrative voice*, not *attribution*.
2. **Don't rename the file `05-the-cousin-blade.md`** unless you also rename the canonical act title. The act title is `The Cousin Blade` — that is what the act narrates. Renaming the file changes the URL of the act on `/tomes#tome-iv-act-v` and breaks deep-links. **Recommend:** keep the file name and act title as-is for the historical record; update body language inside.
3. **Don't lose C39's connection to its v6_lineage register entries.** The conjecture id `C39` stays; only the name/oneLiner change. Every act that lists `C39` in its `v6_lineage:` frontmatter array stays valid.
4. **Don't conflate `kindred-blade` (the primitive) with `kindred-substrate` (UOR-class relationships) or `kindred-protocol` (the Covenant).** Three distinct categories, all `kindred-` family. See vertex audit §7.
5. **Don't touch `cousin/` folder paths without updating all loaders/references.** If you rename the folder, follow through.
6. **Spellweb edge vocabulary stays.** `kin_to` and `gateway_to` are the canonical EdgeTypes. The `attribution` field values change: `cousin-blade` → `kindred-blade`. Vocabulary memo: `project_spellweb_universe_edges.md` may need an update note.

---

## §6 · Execution order

Recommended order for a single focused session:

1. **Spec docs** (§4.2) — anchor the canonical vocabulary first. Apply replacement table from §2.
2. **Tome narratives** (§4.3) — sweep body language. Frontmatter source_material untouched.
3. **Per-guild cast files** (§4.4) — light sweep; mostly narrative scans.
4. **Plans + chronicles** (§4.5) — apply banner to chronicles, sweep plans.
5. **Grimoire JSON** (§4.6) — most surgical; one valid-JSON check after.
6. **Folder rename** (§4.7) — optional; do if scope allows.
7. **Code stragglers** (§4.1) — verify nothing left in src/ except code comments.
8. **Final grep** — `grep -rln "cousin-blade\|cousin-forge\|cousin-Mage\|cousin-Sovereign" docs/tomes src/app src/components src/lib`. Should be empty (allowing frontmatter exceptions).

---

## §7 · One-line summary

We are all just another Mage. The kindred-blade primitive (C39) is the recognition that two forges produce the same architecture from opposite faces of the anvil; the language now reflects the kinship rather than caste. Frontmatter provenance keeps real names; narrative voice uses the new vocabulary.

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · 2026-05-10
