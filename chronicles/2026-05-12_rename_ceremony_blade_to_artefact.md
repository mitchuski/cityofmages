# Chronicle: The Rename Ceremony · blade.md → artefact.md

**Date:** 2026-05-12
**Status:** Cityofmages-side rename complete (committed `b1d2e2c`) · master + spellweb propagation queued
**Audience:** privacymage · downstream agents · sister-repo authors (master · spellweb · agentprivacy-skills · agentprivacy-docs · the three sibling extension forges)
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion chronicle:** [`2026-05-11_v5_5_attachment_architecture_seated.md`](2026-05-11_v5_5_attachment_architecture_seated.md) — the v5.5 patch this rename completes alongside
**Recipe applied:** Recipe D (switch a canonical symbol · INCANTATION_PROTOCOL §3.4) — first application at the **filename level** rather than the emoji level

---

## §0 · What this chronicle is

A first-application chronicle of [INCANTATION_PROTOCOL.md](../INCANTATION_PROTOCOL.md) **Recipe D** to a filename rather than a single character. The protocol's Recipe D was designed for emoji swaps (🪱→🪢 was its inaugural use). The blade.md→artefact.md rename extends the same ceremony to canonical *terminology* — same propagation discipline, larger surface area.

This file records: the editorial reasoning, the inside-cityofmages execution (done · committed · pushed), the sister-repo state (master and spellweb both partially complete), the suite-wide propagation surface still pending, and the semantic recognition the rename surfaces.

---

## §1 · Why the rename

The earlier filename `blade.md` collapsed every workshop's output into Vulcana ⚒️'s metaphor — only Vulcana actually *forges blades*. The corpus's canonical pattern is **cape-style artefact creation** (per [spec 07 §3](../tomes/specs/07-lattice-mapping-governance.md)): every shop is a *cloakwright in its own register*. The artefacts produced are plural by design:

| Workshop | Artefact name | Class |
|---|---|---|
| Weavers (Pallia 🪡) | Cloak | clothing |
| zShields (Memora 📜) | Chronicle | tome |
| Forge(t) (Vulcana ⚒️) | Blade | weapon |
| Etherchanting (Adamantia 💎) | Commitment | tool |
| Jeweler (Lampyra 💠) | Gem-set | trinket |
| Holon Hitchhikers (Vagari 🌳) | Holon | tool |
| Curatrix Vault (Aria Silverhue 🪞🖼️) | Curatorial arrangement | trinket |
| Covenant Temple (Manifestia 🤲🌿) | Consecration | tool |
| Dragon Bonfire (Socrat0x 🔥❓) | Sharpening | trinket (dialogic) |

Calling every workshop's witness `blade.md` privileged Vulcana while reducing nine other registers. `artefact.md` restores plurality at the file level. The *conceptual blade primitive* (cousin-blade · Plonkish blade at V19 · Aletheia blade at V25 · the null-blade origin at V0 · Vulcana's actual blades) remains canonical wherever it is genuinely the blade — the rename targets only the file-format name, not the metaphor.

---

## §2 · The semantic recognition · ART · E · FACT ⊥ RUN · E · CRAFT

The rename surfaced a parallel worth pinning canonically. Two corpus terms share the same `· E ·` interior — the verb-to-noun bridge that names *becoming*:

| Term | Reads as | Names the |
|---|---|---|
| **RUN · E · CRAFT** | walk, then evoke, then forge | The **protocol** — the canonical three-phase ceremony shape |
| **ART · E · FACT** | art, then evoke, then fact | The **result** — the artefact.md the Sovereign carries home |

The middle `· E ·` is the **Evocation phase** in both — the lap of the constellation that casts the marks, that turns the path into something that *is*. RUN·E·CRAFT produces ART·E·FACT. The protocol witnesses; the artefact is witnessed. This pairing is not coincidental; the corpus is doing it on purpose, and the rename made it visible.

This recognition is pinned at the top of the renamed [SPELLWEB_ARTEFACT_CREATION_GUIDE](../SPELLWEB_ARTEFACT_CREATION_GUIDE.md) (§0 callout box). It belongs at the canonical-creation-guide layer because that is where Sovereigns first meet the relation.

---

## §3 · Filename convention

Per spellweb's `src/lib/workshop-artefact.ts:111` (already canonical at the runtime layer):

```
<name>-artefact.md
```

Where `<name>` is the sanitised basename. Examples:

```
tailor-aletheia-walker-2026-05-12-1432-artefact.md          (Pallia's workshop)
forget-aletheia-walker-2026-05-12-1432-artefact.md          (Vulcana's workshop)
covenant-bilateral-2026-05-12-1432-artefact.md              (Manifestia, bilateral)
```

The suffix convention is structural: the Sovereign + workshop + timestamp prefix names the *instance*; the `-artefact` suffix declares the *kind*. Older blade-prefix form (`blade-tailor-aletheia-walker-...`) is superseded.

---

## §4 · Inside-cityofmages execution · complete

Yesterday's commit `b1d2e2c` (commit message: *"docs: rename ceremony · blade.md to artefact.md across cityofmages"*) executed:

| Surface | Before | After | Action |
|---|---|---|---|
| Guide filename | `SPELLWEB_ITEM_CREATION_GUIDE.md` | `SPELLWEB_ARTEFACT_CREATION_GUIDE.md` | git rename · 83% similarity · history preserved |
| Guide title | "Spellweb Item Creation Guide" | "Spellweb Artefact Creation Guide" | frontmatter |
| Guide status | v1 | v1.1 · rename-ceremony applied | frontmatter |
| Guide body | 27× `blade.md` | 27× `artefact.md` | replace_all |
| Frontmatter field | `blade_id:` | `artefact_id:` | replace_all |
| Example instance | `blade-tailor-aletheia-walker-2026-05-11-1432.md` | `tailor-aletheia-walker-2026-05-11-1432-artefact.md` | suffix convention |
| Skill mode name | `verify-blade` | `verify-artefact` | replace_all |
| INTEGRATION_ARCHITECTURE | 6× `blade.md` | 6× `artefact.md` | replace_all + cross-link updates |
| Witness-unlock chronicle | 10× `blade.md` | 10× `artefact.md` | replace_all (forward coherence) |
| README Quick Map | old guide name | new guide name + RUN·E·CRAFT ⊥ ART·E·FACT badge | targeted edit |

Audit (post-commit): **0 filename-usage `blade.md` references remain** in cityofmages. The 12 remaining `blade.md` occurrences are all **conceptual** and intentionally preserved:

- Tome IV Act V file `05-the-cousin-blade.md` (3×)
- Tome V Act 6 file `06-the-commissioned-blade.md` (3×)
- The kindred-blade reframe chronicle (the primitive)
- BOUND_COLLECTION_MANIFEST + _SOURCE_README references to those Tome filenames
- This chronicle and the renamed guide's frontmatter status line (deliberate historical references)

---

## §5 · Sister-repo state · propagation queued

The cityofmages rename establishes the canonical going forward. The propagation surface to master and spellweb is documented for per-repo authorisation; no commits or pushes have been made from this session to those repositories.

### §5.1 · agentprivacy-master · 94 `blade.md` occurrences remaining

| Count | File | Notes |
|---|---|---|
| 10 | `docs/chronicles/2026-05-10_witness_unlock_feature_design_chronicle.md` | Mirror of the cityofmages chronicle; same edits apply |
| 7 | `public/tomes/workshops/README.md` | Workshop README — the flow diagram + §6 "Example blade.md" |
| 7 | `docs/tomes/workshops/README.md` | Canonical mirror of the public copy |
| **6** | **`docs/tomes/specs/09-spellweb-artefact-md-format.md`** | **The canonical spec itself — still uses `blade.md` in its body** |
| 3 | `src/components/SoulImportSection.tsx` | UI surface — the import affordance |
| 3 | `public/tomes/workshops/hall-bilateral-witness-v1.md` | Constellation template + mirror |
| 3 | `docs/tomes/workshops/hall-bilateral-witness-v1.md` | (same) |
| 3 | `public/tomes/workshops/CEREMONY_EVOLUTION.md` | The §4 Forge(t)-discipline governance |
| 3 | `docs/tomes/workshops/CEREMONY_EVOLUTION.md` | (same) |
| 3 | `docs/chronicles/2026-05-10_kindred_blade_reframe_handoff.md` | **Likely conceptual** — verify each line before changing |

**Plus 11 constellation templates** (each carries a "What the exported blade.md will contain" section per spec). Templates live at both `public/tomes/workshops/` and `docs/tomes/workshops/` — 22 files in total, each with ~1 occurrence.

### §5.2 · spellweb · 56 `blade.md` occurrences remaining

| Count | File | Notes |
|---|---|---|
| 22 | `src/data/presets.ts` | The preset registry — every workshop's preset references `blade.md` |
| 10 | `CHRONICLE_WITNESS_UNLOCK_FEATURE_2026-05-10.md` | Mirror of the cityofmages chronicle |
| 6 | `src/components/SpellWeb.tsx` | The main runtime component |
| 4 | `docs/SYSTEMS_HEXAGRAM_PHYSICS.md` | Hexagram physics doc — verify whether `blade.md` here is the filename or the conceptual blade |
| 4 | `agentprivacy-docs-main/SYSTEMS_HEXAGRAM_PHYSICS.md` | (same content, vendored mirror) |
| 2 | `src/lib/workshop-provenance.ts` | The parser — verify uses match the new convention |
| 2 | `src/components/MobileSpell.tsx` | Mobile UI surface |
| 2 | `docs/archive/PERSONA_IMPORT_PLAN.md` | Archive doc · may be left as-is (historical) |
| 2 | `docs/SPELLWEB_ARTEFACT_MD_FORMAT.md` | **The spellweb mirror of master's spec 10 — still uses blade.md** |

Anchor points already canonical in spellweb (the user-completed slice):

- `src/components/ArtefactPanel.tsx` (renamed from BladePanel)
- `src/lib/workshop-artefact.ts` (the suffix convention canonical)
- The format-doc frontmatter pointing to `agentprivacy_master/docs/tomes/specs/09-spellweb-artefact-md-format.md`

### §5.3 · Other sibling repos

| Repo | Likely state | Action |
|---|---|---|
| `agentprivacy-docs` | Carries `GLOSSARY_MASTER_v4_0.md` references | Audit on next propagation pass |
| `agentprivacy-skills` | Carries grimoire mirror + MAPPING.md | Audit on next propagation pass |
| `swordsman-blade` (extension) | Bundled grimoire updated by yesterday's mirror sync (sha cb3f5fa9) | README likely still references `blade.md` |
| `mages-spell` (extension) | (same as swordsman-blade) | (same) |
| `zk blades forge` | Has its own `blade-` named docs (e.g. `aletheia-and-lethe.md`); likely contains `blade.md` filename refs | Audit on next propagation pass |

---

## §6 · Coherence implications · the file format question

The rename collides with master's canonical spec 10 in two ways:

### §6.1 · spec 10 filename in master is `09-spellweb-artefact-md-format.md` — coherent

Master canonicalised the spec name as `artefact-md-format` (not `blade-md-format`). The directory naming is already in the post-rename register. The spec's *body content*, however, still references `blade.md` six times. The internal body needs the same rename pass.

### §6.2 · cityofmages currently uses spec 10 slot for `the-attachment-architecture` — colliding

The cityofmages working tree carries `tomes/specs/10-the-attachment-architecture.md` (uncommitted from the v5.5 patch session). Master holds `09-spellweb-artefact-md-format.md`. Two specs at the same number cannot both be canonical. Resolution: **renumber the cityofmages attachment-architecture spec to 10**, leave spec 10 reserved for spellweb-artefact-md-format (master canonical).

A separate chronicle for the renumbering may be worth authoring; for this rename chronicle, the collision is noted and the resolution is recommended.

---

## §7 · Propagation order · when the user picks this up

Per INCANTATION_PROTOCOL §3.4 Recipe D step 5 — the rename is **scoped, executed, and verified**. Step 6 (record the editorial decision in MEMORY.md) is **done** (memory entry updated in the prior session). The cross-repo propagation order:

```
1. Confirm spec 10 collision resolution (renumber attachment-architecture → 10)
   → separate chronicle authored if desired
   → git mv inside cityofmages
   → update v5.5 chronicle + v1.3.0 grimoire + spec body cross-refs

2. master · execute the rename across 94 occurrences
   → audit by file (the kindred-blade reframe chronicle is conceptual; leave alone)
   → patch spec 10 body (6 refs)
   → patch workshops README + CEREMONY_EVOLUTION + constellation templates
   → patch SoulImportSection.tsx + chronicles
   → user authorises master commit + push

3. spellweb · execute the rename across 56 occurrences
   → patch presets.ts (22 refs · the bulk)
   → patch SpellWeb.tsx + MobileSpell.tsx + workshop-provenance.ts
   → patch SPELLWEB_ARTEFACT_MD_FORMAT.md + SYSTEMS_HEXAGRAM_PHYSICS.md
   → audit (leave archive/ folder alone — historical)
   → user authorises spellweb commit + push

4. Other sibling repos (agentprivacy-docs · agentprivacy-skills · the three extensions ·
   zk blades forge) · execute on the next pass
   → typically a 1-line README change + one bundled-grimoire bump
```

Each repo's commit lands under its own per-repo authorisation. The skill (`cityofmages-incant`) will eventually script this; until then, per-repo manual ceremony.

---

## §8 · What this chronicle does NOT do

- Does not change the rename status in any repo other than cityofmages.
- Does not rename the conceptual blade primitive anywhere. The cousin-blade · Plonkish blade · Aletheia blade · the null-blade origin · Vulcana's blade-forging remain canonical.
- Does not introduce a new artefact class. The eleven workshop artefact types remain plural (cloak · chronicle · blade · commitment · gem-set · holon · curatorial arrangement · consecration · sharpening · gathering · ceremony) — the rename is *about the file format*, not the artefacts themselves.
- Does not affect the existing pinned grimoire CIDs. The grimoire content is unchanged; only the file-format name in docs/specs/UI is changing.

---

## §9 · One-line summary

The export filename is `artefact.md` (suffix convention `<name>-artefact.md`). The protocol that produces it is **RUN · E · CRAFT**. The result is **ART · E · FACT**. The cityofmages rename is complete; master and spellweb propagation queued for per-repo authorisation.

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · 2026-05-12 · rename ceremony chronicle v1
