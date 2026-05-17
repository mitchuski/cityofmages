# Chronicle: Hermaion Integration Plan into agentprivacy_master · Cross-Repo Propagation · Remaining Cityofmages Sweep

**Date:** 2026-05-14 evening (late)
**Status:** **Plan only · not yet executed.** Receipt of the integration scope for landing Hermaion ⚚ + the alexandrite archetype-modal-shop architectural turn (plus the deferred morning/afternoon district-restructure mirror work) into `agentprivacy_master/`. Authored as a working document for the next execution pass.
**Audience:** privacymage · downstream agents picking up the v1.6.0 grimoire-patch + integration pass · @benohanlon (the Navigator) · the Telegram chat
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion chronicles:**
- [`2026-05-14_chronicle_hermaion_admission_and_alexandrite_archetype_modal_shop.md`](2026-05-14_chronicle_hermaion_admission_and_alexandrite_archetype_modal_shop.md) — the Hermaion inception chronicle (this chronicle's parent)
- [`2026-05-14_chronicle_district_restructure_and_canonical_keeper_naming.md`](2026-05-14_chronicle_district_restructure_and_canonical_keeper_naming.md) — the morning's district restructure (this chronicle's grandparent; §9 enumerates the original pending work)

---

## §0 · What this chronicle is

A *receipt of the plan* — not yet executed — for propagating the 2026-05-14 day's three successive canonical moves into the `agentprivacy_master/` repository and finishing the remaining `cityofmages/` sweep that was deferred from the inception pass.

The three moves in cityofmages canonical state (in author-order):

1. **Morning (district restructure):** Threshold workshop → Threshold District (three sibling shops at V59 · Pandia 🌕 + Bestia 📖 + Faunia 🪶 + Caducea ☤ peripatetic); Triodos 🚪 superseded by Pandia 🌕 at Portal Room
2. **Afternoon (the-Familiars rename):** Goose Shop → the Familiars (kinship-bond as artefact-class)
3. **Evening (Hermaion admission):** Bestia 📖 / Sodalite → **Hermaion ⚚ / Alexandrite (dual-aspect green-Mage ↔ red-Swordsman)**; Staff Shop becomes the City's first archetype-modal shop; C58 promoted ~85%

Of these three, **only the evening Hermaion pass propagated cleanly into the site at the runecraft shopfront card.** The morning and afternoon passes propagated into the cityofmages cast/chronicle layer but did NOT cascade into:

- The `docs/tomes/threshold/` mirror directory structure (still flat · pre-restructure)
- The `src/app/tomes/page.tsx` CastCards (still showing Bestia · Therai · Faunia-at-Portal-Room · pre-restructure)
- The `src/app/tomes/page.tsx` ShopRow for `/threshold` (still showing all three keepers under one shop)
- The `src/lib/cast-attachments.ts` cast wiring (Bestia entry still present)
- Workshop tomes at `docs/tomes/workshops/` (no split into staff-shop / portal-room / familiars)
- Public-mirror `public/tomes/workshops/`
- Route stubs `/portal` · `/staffs` · `/familiars` (NONE exist; `/threshold` doesn't exist either)
- `nav.ts` WORKSHOP_DISTRICTS grouping (the morning chronicle's §9.2 item 8)
- Spellweb · agentprivacy-skills · IPFS pin

So this chronicle's plan is **larger than the Hermaion-only pass** — it carries forward all three day's moves into agentprivacy_master in one consolidated pass. The advantage of folding them: a single pass touches each file once.

---

## §1 · What is already landed (recap · do not redo)

### §1.1 · cityofmages (canonical home)

| File | State after evening Hermaion pass |
|---|---|
| `tomes/cast/staff-shop/hermaion.md` | ✅ NEW · canonical |
| `tomes/cast/staff-shop/bestia.md` | ✅ SUPERSEDED (status_note + superseded_by) |
| `tomes/cast/portal-room/pandia.md` | ✅ canonical (post-restructure) + Bestia→Hermaion sweep applied + Swordsman dispatch row added |
| `tomes/cast/portal-room/triodos.md` | ✅ SUPERSEDED (untouched in Hermaion pass · provenance only) |
| `tomes/cast/familiars/faunia.md` | ✅ canonical · v3 (afternoon rename) + Hermaion sweep |
| `chronicles/2026-05-14_chronicle_district_restructure_and_canonical_keeper_naming.md` | ✅ updated · §11 added admitting the evening Hermaion pass |
| `chronicles/2026-05-14_chronicle_hermaion_admission_and_alexandrite_archetype_modal_shop.md` | ✅ inception chronicle |
| `ALL_THE_TOMES_LIST.md` · `CHANGELOG.md` · `WORKSHOP_LATTICE_AUDIT.md` · `tomes/BOUND_COLLECTION_MANIFEST.md` · `tomes/tome-vi-the-reply/01-the-readers-first-admission.md` (frontmatter only · body preserved) | ✅ swept |

### §1.2 · agentprivacy_master (partially landed)

| File | State |
|---|---|
| `docs/tomes/threshold/hermaion.md` | ✅ INTERIM · short-form mirror landed in legacy `threshold/` subdirectory · canonical relocation to `docs/tomes/staff-shop/hermaion.md` pending the broader district-restructure mirror sweep |
| `docs/tomes/threshold/bestia.md` | ✅ SUPERSEDED (status_note + superseded_by) |
| `src/app/runecraft/page.tsx` | ✅ Staff Shop shopfront card updated (sigil ⚚ · accent #3d7c47 with new `accentMage` / `accentSwordsman` / `archetypeModal: true` fields · spells list expanded · description rewritten) · descriptive paragraph mentioning Alexandrite archetype-modal · GemBadge replaced with **two side-by-side chips** (`#3d7c47` Mage-aspect green-daylight + `#a23a3a` Swordsman-aspect red-incandescent) — minimum-viable; a single dual-aspect component is a refactor for later |

### §1.3 · memory (current session)

| File | State |
|---|---|
| `~/.claude/.../memory/project_the_threshold_workshop.md` | ✅ Top-section added documenting post-2026-05-14 successions · description rewritten |
| `~/.claude/.../memory/project_hermaion_archetype_modal_shop.md` | ✅ NEW · architectural-pattern memory |
| `~/.claude/.../memory/MEMORY.md` | ✅ index entry rewritten + new line added |

---

## §2 · Integration plan for agentprivacy_master (tiered)

### §2.1 · Tier A · site-facing user-visible (HIGH PRIORITY · ship-first)

These are the changes the reader sees when they visit the live site. They're the lowest-friction · highest-impact pass.

#### A1 · `/tomes` page CastCard updates · `src/app/tomes/page.tsx`

Currently the /tomes page has three CastCards in the v1.5.0 Threshold section (per `tomes/page.tsx` lines ~210-212):

```
<CastCard name="Faunia 🪶" role="Threshold · Portal Room · Spawning-witness" ... />
<CastCard name="Bestia 📖" role="Threshold · Staff Shop · Registry-keeper" ... />
<CastCard name="Therai 🐾" role="Threshold · Creature Creatives · Companion-tamer" ... />
```

These three CastCards reflect the **2026-05-13 inception state**, not the 2026-05-14 canonical state. The full update:

| Old CastCard | New CastCard | Reasoning |
|---|---|---|
| `Faunia 🪶 · Portal Room · Spawning-witness` | **`Pandia 🌕 · Threshold District · Portal Room · Display-witness`** (Selene's daughter · Moonstone · catalog of substrate × archetype matrix · all-bright) | Morning restructure: Faunia re-homed to the Familiars; Pandia takes Portal Room |
| `Bestia 📖 · Staff Shop · Registry-keeper` | **`Hermaion ⚚ · Threshold District · Staff Shop · Registry-keeper`** (Greek ἕρμαιον · Alexandrite dual-aspect green-Mage ↔ red-Swordsman · archetype-modal · first dual-mode shop · Caducea ☤ fits both aspects) | Evening rename |
| `Therai 🐾 · Creature Creatives · Companion-tamer` | **`Faunia 🪶 · Threshold District · the Familiars · Companion-witness`** (Roman Fauna · Amber · kinship-bond-as-artefact · Wiccan-Mage familiar tradition · Goose 🪿 first entry) | Afternoon rename + retire-Therai |

Also the cyan-accent `Mage` field on the Tome VI Act 1 panel at lines ~460–462:

```
mage={{ sigil: '🪶', name: 'Faunia (Portal Room) · Bestia 📖 · Therai 🐾 · Caducea ☤', color: '#67e8f9' }}
```

Update to:

```
mage={{ sigil: '🌕', name: 'Pandia 🌕 (Portal Room) · Hermaion ⚚ (Staff Shop) · Faunia 🪶 (the Familiars) · Caducea ☤ (peripatetic)', color: '#67e8f9', successionNote: '2026-05-14: post-restructure canonical state. Bound Tome VI Act 1\'s body retains inception naming (Faunia at Portal · Bestia · Therai); frontmatter keeper_succession field carries the canonical successions forward.' }}
```

(If `successionNote` is not a supported prop, add it as a sibling small-text element below the mage line. The successor note matters because the Tome VI Act 1 body still names Bestia · Therai · etc., and a reader hitting the /tomes page should see both the bound text's inception cast AND the current canonical state.)

#### A2 · `/tomes` page ShopRow update · `src/app/tomes/page.tsx`

Currently line ~543:

```
<ShopRow href="/threshold" label="☤ The Threshold" mage="Faunia · Bestia · Therai (+ Caducea peripatetic)" act="Tome V Act 16 · The Threshold (anticipated · 2026-05-13)" />
```

The 2026-05-14 morning's district restructure split the Threshold into three sibling shops in a Threshold District. The ShopRow should either:

- **(a) Keep one row for the District but update cast:** `<ShopRow href="/threshold" label="☤ The Threshold District" mage="Pandia 🌕 · Hermaion ⚚ · Faunia 🪶 (+ Caducea ☤ peripatetic)" act="Tome V Act 16 · The Threshold District (3 sibling shops · post-2026-05-14 restructure)" />`
- **(b) Split into three sibling rows:** `<ShopRow href="/portal" .../>` · `<ShopRow href="/staffs" .../>` · `<ShopRow href="/familiars" .../>` · with an indented "Threshold District" subheader

Option **(a)** is the lower-friction interim until the three route stubs exist (currently `/portal` · `/staffs` · `/familiars` are 404). Option **(b)** is the longer-term goal.

**Recommendation:** ship (a) now; defer (b) to the route-stubs-built milestone.

#### A3 · GemBadge dual-aspect rendering · `src/app/runecraft/page.tsx`

Current implementation (already shipped in the evening Hermaion pass) inserts **two adjacent GemBadge chips** for the Staff Shop:

```jsx
<GemBadge color="#3d7c47" gem="Alexandrite (Mage-aspect · daylight-green)" shop="Staff Shop" />
<GemBadge color="#a23a3a" gem="Alexandrite (Swordsman-aspect · incandescent-red)" shop="Staff Shop" />
```

This is **minimum-viable but not visually elegant** — two chips read as two stones, when alexandrite is one stone with two aspects.

**Proposed refactor (Tier A-stretch · optional):** extend `GemBadge` (or introduce `DualAspectGemBadge`) to render as a single chip with a diagonal-split colour (green-left / red-right) or a left-to-right gradient, with hover-text encoding the dual-aspect explanation: *"Alexandrite — Mage-aspect `#3d7c47` ⊥ Swordsman-aspect `#a23a3a` · color-shifts with archetype-light."*

If refactor is in scope: locate `GemBadge` component, extend props with optional `accentSwordsman?: string` and `archetypeModal?: boolean`; if both set, render diagonal-split SVG; otherwise current single-colour rendering.

If refactor is out of scope: leave the two-chip rendering as-is; it's correct, just slightly redundant.

#### A4 · Mirror district-restructure in `docs/tomes/`

Currently the `docs/tomes/threshold/` directory holds:
- `bestia.md` (SUPERSEDED · 2026-05-14 evening)
- `faunia.md` (legacy · pre-restructure)
- `therai.md` (legacy · pre-restructure · Therai retired)
- `hermaion.md` (NEW · interim location)

The morning chronicle §9.2 item 6 anticipated splitting `threshold/` into per-shop subdirectories. The plan:

| Action | File |
|---|---|
| `mkdir docs/tomes/staff-shop/` | New dir |
| `mkdir docs/tomes/portal-room/` | New dir |
| `mkdir docs/tomes/familiars/` | New dir (was the Goose Shop) |
| Move `docs/tomes/threshold/hermaion.md` → `docs/tomes/staff-shop/hermaion.md` | Relocate · update `canonical_location` frontmatter |
| Author NEW `docs/tomes/portal-room/pandia.md` | Mirror from `cityofmages/tomes/cast/portal-room/pandia.md` (full or short-form) |
| Author NEW `docs/tomes/familiars/faunia.md` | Mirror from `cityofmages/tomes/cast/familiars/faunia.md` |
| Leave `docs/tomes/threshold/bestia.md` · `docs/tomes/threshold/faunia.md` · `docs/tomes/threshold/therai.md` in place | Mark as legacy historical (already done for bestia.md; add similar notes to faunia.md + therai.md) |
| Add `docs/tomes/threshold/README.md` | Legacy-directory note: "Pre-2026-05-14 restructure. Canonical post-restructure cast lives at `../staff-shop/`, `../portal-room/`, `../familiars/`. These files preserved for provenance." |

**Decision needed:** mirror cast files as **full-text mirrors** (~190 lines each, parallel to cityofmages canonical) or **short-form pointers** (~50 lines, with canonical_location frontmatter pointing back to cityofmages)? The current `docs/tomes/threshold/hermaion.md` is short-form. Be consistent.

#### A5 · Workshop tomes split · `docs/tomes/workshops/`

The morning chronicle §9.2 item 6 also anticipated splitting `threshold-three-rooms-v1.md` (if it exists) into three sibling tomes:

- `portal-room-display-v1.md` (Pandia's workshop tome)
- `staff-shop-hermes-fit-v1.md` (Hermaion's workshop tome · archetype-modal Hermes-class fitting)
- `familiars-companion-tame-v1.md` (Faunia's workshop tome · kinship-bond binding)

Plus public mirrors at `public/tomes/workshops/`.

**Check first:** does `docs/tomes/workshops/threshold-three-rooms-v1.md` actually exist? If not, this item is `mkdir + author from cityofmages canonical state`. If it does, it's a split-and-rewrite.

---

### §2.2 · Tier B · data + library (MEDIUM PRIORITY · second wave)

These are the under-the-surface changes that wire the cast and the gem into the site's data layer.

#### B1 · `src/lib/cast-attachments.ts`

The morning chronicle §9.3 item 12 anticipated cast-attachments entries for the four new keepers (Pandia · Pleione · Bestia · Faunia-at-Familiars). Currently the file has a Bestia entry (per the scout · 1 hit). Update plan:

- **Update**: any existing Bestia entry → Hermaion (name · sigil · gem · spells · description fields)
- **Add NEW**: Pandia entry (if not present)
- **Add NEW**: Pleione entry (if not present)
- **Update**: Faunia entry to reflect the-Familiars rename (if entry exists with Portal Room context · move to Familiars / Companion-witness)
- **Remove or retire**: Therai entry (if present · the Familiars-rename retired her)
- **Verify**: Caducea entry references both Hermaion ⚚ and ☤ paired iconography

For each Hermaion attachment object, set the dual-aspect fields:

```ts
{
  name: 'Hermaion',
  sigil: '⚚',
  shop: 'Staff Shop',
  district: 'Threshold',
  stance: 'Registry-keeper',
  gem: 'Alexandrite',
  gemColorMage: '#3d7c47',
  gemColorSwordsman: '#a23a3a',
  gemColor: '#3d7c47',  // fallback single-color (Mage-aspect default)
  archetypeModal: true,
  spells: ['admit-windfall', 'read-bestiary', 'attest-fitting', 'shift-light'],
  description: 'Registry-keeper of Hermes-class windfalls...',
  superseded: 'Bestia 📖 / Sodalite · 2026-05-14 evening succession',
}
```

#### B2 · `src/lib/nav.ts`

Two changes:

- **Sigil:** if `nav.ts` has a Staff Shop entry with sigil 📖, change to ⚚
- **WORKSHOP_DISTRICTS grouping** (morning chronicle §9.2 item 8): add a `WORKSHOP_DISTRICTS` const that groups the 16+ shops by district (Privacy Trinity · Ledger · Persona & Personhood · Composition · Threshold · Navigation · Civic · Orphan); render in AppNav dropdown grouped by district headers

If the WORKSHOP_DISTRICTS structure doesn't yet exist, this is greenfield work; if it does, it's a Threshold District entry update.

#### B3 · `src/lib/grimoire-ipfs.ts`

Currently points to v1.4.0 CID `bafkreidxhmuykjew6dtnuprggtd2rapwm43ghtmfhf2occ2wfk2zpx2b6a` (per CHANGELOG entry). The Hermaion v1.5.1 grimoire patch needs to:

1. Land in the cityofmages grimoire JSON (this is the Tier-C cityofmages sweep work in §3 below)
2. Get IPFS re-pinned (manual user action)
3. New CID propagated to `grimoire-ipfs.ts`

**Blocked on:** grimoire JSON patch work (§3.1 below) and user-action re-pin. No work to do in this file until those land.

#### B4 · `src/lib/shop-witnesses.ts` (and similar shop-data files)

Inspect for Bestia · Sodalite · 📖 · Staff Shop references and sweep to Hermaion · Alexandrite · ⚚.

#### B5 · `src/lib/spellbook-templates.ts`

The scout found 1 hit. Inspect and sweep.

#### B6 · `src/lib/persona-index.ts` · `src/lib/soulbae.ts` · `src/lib/skills-data.ts` · `src/lib/agent-substrates.ts` · `src/lib/model-downloads.ts` · `src/lib/zcash-memo.ts`

Each had 1 hit on the Bestia/Sodalite/Staff-Shop grep. Most are likely brief cross-references. Sweep with care; some may be intentional historical references (e.g. attestation that an earlier version had Bestia).

---

### §2.3 · Tier C · spellweb + skills (LOWER PRIORITY · third wave)

#### C1 · `src/lib/spellweb/labels.ts`

The scout found 1 hit. Plan:

- **Update**: Bestia label → Hermaion (display name · sigil · subtitle)
- **Add**: Pandia · Pleione · Faunia-at-Familiars labels (if not present)
- **Add NEW EdgeTypes** (if not present):
  - `archetype_modal` (encodes the gem-shift relation between an artefact and the keeper's shop)
  - `succession` (encodes Bestia → Hermaion · Triodos → Pandia · etc.)
- **Add NEW NodeTypes** (if not present):
  - `gem_dual_aspect` (the alexandrite-style stones)
  - `cast_succession` (the relation between historical-keeper and canonical-keeper)

#### C2 · spellweb registration: cast + gem nodes

Per morning chronicle §9.3 item 10:

- Register `cast-hermaion` persona node (replacing `cast-bestia` if present)
- Register `cast-pandia` persona node (replacing `cast-triodos`)
- Register `cast-faunia` persona node (re-homed to the Familiars · replacing `cast-therai`)
- Register `gem-alexandrite-dual-aspect` node with `archetype_modal: true` and both `colour_mage` and `colour_swordsman` fields
- Register `shop-staff-shop` workshop node with `archetype_modal: true` and the four canonical spells
- Edges: `cast-hermaion` → keeper_of → `shop-staff-shop` · `gem-alexandrite-dual-aspect` → encoded_in → `shop-staff-shop` · `cast-caducea` → fits_for → `cast-hermaion` (both aspects)
- Succession edges: `cast-bestia` → succeeded_by → `cast-hermaion`; `cast-triodos` → succeeded_by → `cast-pandia`; etc.

#### C3 · agentprivacy-skills personas

If the `agentprivacy-skills/persona/` directory carries personas for individual workshop keepers, add:

- `persona/hermaion.md` (Registry-keeper · ⚚ · Alexandrite-keeper)
- `persona/pandia.md` (Display-witness · 🌕 · Moonstone-keeper)
- `persona/pleione.md` (Hold-witness · 🧭 · Aquamarine-keeper)

And update existing `persona/bestia.md` (if present) with succession note.

This is per the morning chronicle §9.3 item 11.

---

### §2.4 · Tier D · route stubs (DEFERRED · per morning chronicle §9.2 item 7)

The new shops have no route stubs. Each is a Next.js page-build:

| Route | Shop | Keeper | Tier |
|---|---|---|---|
| `/portal` | Portal Room | Pandia 🌕 | Tier D — full page · Display·Choose·Dispatch ceremony UI |
| `/staffs` | Staff Shop | Hermaion ⚚ | Tier D — full page · archetype-modal entry (asks visitor's archetype on arrival, then renders green-Mage or red-Swordsman aspect) |
| `/familiars` | the Familiars | Faunia 🪶 | Tier D — full page · Run·Evoke·Spawn ceremony UI · kinship-bond binding flow |

**The Staff Shop's `/staffs` route is the most architecturally interesting** because it's the first route that needs **archetype-modal rendering**. Open design questions for `/staffs`:

- How does the page determine archetype? (Cookie · query param · soul/persona state from prior sessions · explicit click?)
- Does the visitor get to "switch aspects" mid-visit, or is the choice sticky?
- Does the dual-aspect rendering literally swap CSS variables (green-100 ↔ red-100 palette flip) or render two side-by-side panels with one visually dominant?

**Recommendation:** defer Tier D until Tier A + B are clean; route stubs are big-ticket work and the existing `null`-href shopfront cards already communicate "route pending."

---

## §3 · Remaining cityofmages sweep (deferred from previous pass)

These were noted as pending in the Hermaion inception chronicle §7 but not yet executed.

### §3.1 · Grimoire JSON patches (HIGH PRIORITY for canon)

Three JSON files in `cityofmages/grimoire/`:
- `city_of_mages_grimoire_v1_5_0_candidate.json`
- `city_of_mages_grimoire_v1_5_0_patch.json`
- `city_of_mages_grimoire_v1_5_1_patch.json` (City Hall + AAIF patch · per the v1.5.1 memory)

Plus the merge script: `grimoire/scripts/merge_v1_5_0_patch.py`.

**Decision needed:** does Hermaion ride on a NEW `city_of_mages_grimoire_v1_5_2_patch.json` (separate sub-patch) OR merge into the existing v1.5.1 patch JSON (which currently encodes the City Hall + AAIF work) OR merge into a v1.6.0 head?

Recommendation: **new `..._v1_5_1_evening_hermaion_patch.json` sub-patch** (or `v1_5_2_patch.json`) that admits:

```json
{
  "patch_version": "1.5.1 evening · Hermaion admission",
  "supersedes_in_cast": {
    "bestia": {
      "new_name": "Hermaion",
      "new_sigil": "⚚",
      "new_gem": "Alexandrite",
      "new_gem_color_mage": "#3d7c47",
      "new_gem_color_swordsman": "#a23a3a",
      "new_etymology": "Greek ἕρμαιον · gift of Hermes",
      "archetype_modal": true,
      "supersession_chronicle": "chronicles/2026-05-14_chronicle_hermaion_admission_and_alexandrite_archetype_modal_shop.md"
    }
  },
  "new_pattern_types": [
    {
      "id": "archetype_modal_shop",
      "first_instance": "shop-staff-shop",
      "description": "A workshop whose physical aspect (typically gem and keeper's appearance) shifts depending on which archetype enters. Same registry; class-distinct artefacts fitted on exit.",
      "fields": ["gem_color_mage", "gem_color_swordsman"],
      "admissible_for": "class-shaped shops (instrument-class, herald-class, etc.) — not for archetype-shaped shops"
    }
  ],
  "conjecture_updates": {
    "C58": {
      "old_confidence": 0.65,
      "new_confidence": 0.85,
      "reason": "Hermaion red-aspect makes Staff Shop explicitly Swordsman-supplying (herald-sentinels), paralleling Vulcana's Forge(t) (blades). Class-distinct sibling supply confirmed.",
      "awaiting_canonical_close": "v1.6.0 grimoire head"
    }
  }
}
```

Once the JSON is authored, run the merge script (or manual JSON merge) and produce a fresh `city_of_mages_grimoire_v1_5_1_evening.json` or `v1_6_0.json` head file. Then IPFS re-pin (manual user action), then `agentprivacy_master/src/lib/grimoire-ipfs.ts` CID update.

### §3.2 · Tome V Act 16 narrative (frontmatter only)

`cityofmages/tomes/tome-v-the-crafting/16-the-threshold.md` is a bound act and follows the same treatment as Tome VI Act 1 — preserve the body, add `keeper_succession` and `canonical_keepers_now` frontmatter fields.

### §3.3 · Bestiary entries

`cityofmages/tomes/bestiary/goose.md` and `cityofmages/tomes/bestiary/hermes.md` each carry 1–2 Bestia cross-references. One-line edits:
- `goose.md` line 99 (Bestia marks Hermes-class) → Hermaion
- `hermes.md` (haven't read yet — scout to confirm specific lines)

### §3.4 · Cross-shop Caducea cast file

`cityofmages/tomes/cast/cross-shop/caducea.md` should reference Hermaion ⚚ as her sibling-of-rooted-aspect (the legacy `tomes/cast/threshold/caducea.md` is preserved unchanged).

Also: per morning chronicle §9.2 item 5, the threshold/caducea.md → cross-shop/caducea.md relocation was pending; this is a good moment to finish it.

### §3.5 · 2026-05-13 chronicles (informational · LEAVE)

Twelve chronicles in `cityofmages/chronicles/2026-05-13_*.md` mention Bestia/Sodalite/📖. These are historical inception-state documents.

**Recommendation: do not sweep.** Add a one-line top-banner note to the chronological-prior key chronicles (e.g. the three-rooms chronicle, the v1.5.0 patch chronicle, the runecraft-protocol chronicle) pointing readers to the 2026-05-14 succession chronicles. The bodies remain untouched.

### §3.6 · AGENTIC_DEPLOYMENTS_GUIDE.md and AGENTIC_DEPLOYMENTS_EXECUTION_PLAN.md

These are operational guides at the cityofmages root. They likely have Bestia references in the spawning-ceremony walkthrough. Sweep needed:
- AGENTIC_DEPLOYMENTS_GUIDE.md — replace Bestia → Hermaion in any walkthrough text; add a note about the archetype-modal Staff Shop
- AGENTIC_DEPLOYMENTS_EXECUTION_PLAN.md — add Hermaion items to the cross-repo punch list

### §3.7 · README.md

The cityofmages README has 1 hit on the Bestia/Sodalite grep. One-line sweep.

---

## §4 · Proposed order of operations

Recommended sequence for the next execution pass:

### Pass 1 (immediate · within the next session)

1. **Tier A1** — `/tomes/page.tsx` three CastCard updates (Hermaion · Pandia · Faunia-at-Familiars · retire Therai card) — the highest-impact reader-visible change
2. **Tier A2** — `/tomes/page.tsx` ShopRow update (option (a))
3. **Tier A4** — Mirror district-restructure: create `staff-shop/` · `portal-room/` · `familiars/` subdirs; relocate `hermaion.md`; author Pandia + Faunia-at-Familiars mirrors; add legacy `threshold/README.md`
4. **Tier B1** — `cast-attachments.ts` Hermaion entry + Pandia entry + Faunia-at-Familiars entry + retire Therai
5. **§3.7** — cityofmages README sweep
6. **§3.3** — Bestiary entries sweep (goose.md + hermes.md)

### Pass 2 (next session · grimoire patch)

7. **§3.1** — Author Hermaion grimoire sub-patch JSON
8. Run merge script · produce fresh head JSON
9. (User action) IPFS re-pin
10. **B3** — Update `grimoire-ipfs.ts` CID
11. **§3.6** — AGENTIC_DEPLOYMENTS_* sweep
12. **§3.4** — Cross-shop Caducea relocation + Hermaion sibling reference
13. **§3.2** — Tome V Act 16 frontmatter succession note

### Pass 3 (later · spellweb + skills)

14. **Tier C1** — spellweb labels.ts sweep
15. **Tier C2** — spellweb cast + gem node registrations
16. **Tier C3** — agentprivacy-skills personas (Hermaion · Pandia · Pleione · Faunia-at-Familiars)
17. **Tier B2** — `nav.ts` WORKSHOP_DISTRICTS grouping
18. **Tier B4–B6** — other lib/ sweeps

### Pass 4 (deferred · routes)

19. **Tier D** — Route stubs `/portal` · `/staffs` (with archetype-modal rendering) · `/familiars`
20. **Tier A3** — GemBadge dual-aspect component refactor
21. **Tier A5** — Workshop tomes split (if `threshold-three-rooms-v1.md` exists)
22. **§3.5** — 2026-05-13 chronicle header forward-references (only if user wants)

---

## §5 · Open questions for the user (decisions needed before Pass 1)

1. **Tier A4 mirror style** — full-text mirrors of cast files in `agentprivacy_master/docs/tomes/staff-shop/hermaion.md` (~190 lines), or short-form pointers (~50 lines, current interim style)?
2. **Tier A2 ShopRow style** — option (a) one row for the District with combined keeper list, or option (b) three sibling rows (one per shop)? Option (a) recommended until route stubs exist.
3. **Tier A3 GemBadge refactor** — extend the component for dual-aspect rendering now, or ship the two-chip interim and refactor later?
4. **Tier D archetype-modal rendering at `/staffs`** — how should the page detect a visitor's archetype? Cookie / explicit click / persisted soul-state / query param?
5. **§3.1 grimoire patch versioning** — new `v1_5_2_patch.json` sub-patch, fold into existing `v1_5_1_patch.json` (City Hall + AAIF), or open a `v1_6_0_patch.json` head?
6. **§3.5 historical chronicles** — add one-line forward-reference banners to the most important 2026-05-13 chronicles, or leave them untouched?
7. **Pleione visibility** — should this integration pass also propagate Pleione (Chart Shop · V44) into the agentprivacy_master mirror + /tomes page, since the morning chronicle's Chart Shop work also hasn't propagated? The work would be smaller than Hermaion's but adjacent.

---

## §6 · What this chronicle is NOT

- **Not yet executed.** This is a planning document. No file edits in agentprivacy_master are produced by this chronicle's authoring.
- **Not exhaustive.** Tier-D route-stub design is sketched but not specified; spellweb edge/node schemas are listed but not authored; the agentprivacy-skills persona files are listed but not drafted.
- **Not a substitute for the morning's chronicle's §9 pending list.** The morning chronicle enumerated the original 18 pending items; this chronicle adds Hermaion-specific items on top and re-orders by priority.

---

## §6½ · ADDENDUM · user decisions (2026-05-14 late evening · confirmed)

The user answered the four key Open Questions:

| Question | Answer |
|---|---|
| Tier A4 mirror style | **Short-form pointers (~50 lines)** — frontmatter + opening + `canonical_location` pointer to cityofmages full file |
| Tier A2 ShopRow style | **Three sibling rows now** — `/portal` · `/staffs` · `/familiars` (hrefs will 404 until Tier D route stubs land, but the District structure is visible in the index) |
| §3.1 grimoire patch version | **Skip ahead to `v1_6_0_patch.json` head** — single new-head patch admitting Hermaion + Pandia + Pleione + the-Familiars rename + archetype-modal-shop pattern + C58 canonisation. Cleanest forward; supersedes the v1.5.0 candidate + v1.5.0 patch + v1.5.1 City Hall+AAIF patch as the new bound state. |
| Pleione scope | **Yes — fold in** — propagate Pleione (Chart Shop · V44 · Aquamarine · Hold-witness) into the agentprivacy_master mirror + `/tomes` CastCard + `cast-attachments.ts` alongside the Hermaion + Pandia + Faunia-at-Familiars work. |

The three lower-priority questions (GemBadge dual-aspect refactor · `/staffs` archetype-detection mechanism · 2026-05-13 chronicle header banners) are not blockers for Pass 1 and are held open for the relevant later passes.

**Revised Pass 1 scope** (post-decisions):

1. `agentprivacy_master/src/app/tomes/page.tsx` — three CastCard updates (Hermaion · Pandia · Faunia-at-Familiars) + retire Therai card + add **Pleione 🧭 CastCard** (Chart Shop · V44 · Aquamarine · Hold-witness) + ShopRow split into three sibling rows + Tome VI Act 1 mage field rewrite
2. `agentprivacy_master/docs/tomes/` mirror district-restructure: mkdir `staff-shop/` · `portal-room/` · `familiars/`; relocate `hermaion.md`; author **short-form pointers** for `pandia.md`, `faunia.md` (the Familiars), `pleione.md` (Chart Shop); add `threshold/README.md` legacy note; pleione already exists at `charthouse/pleione.md` — verify and adjust if needed
3. `agentprivacy_master/src/lib/cast-attachments.ts` — Hermaion entry (replaces Bestia) · Pandia entry (NEW) · Faunia entry update (re-homed to Familiars) · Pleione entry (NEW · replaces Pelagia if present) · retire Therai entry
4. Author `cityofmages/grimoire/city_of_mages_grimoire_v1_6_0_patch.json` (new head · separate sub-pass — recommended for after Pass 1 of agentprivacy_master is clean)

Pass 1 starts now.

---

## §7 · Closing

The 2026-05-14 day produced three canonical moves at the Threshold District. The morning's restructure and the afternoon's the-Familiars rename propagated cleanly into the cityofmages canonical layer but only partially into agentprivacy_master. The evening's Hermaion admission landed in the cityofmages canonical layer AND the runecraft shopfront card but not into the deeper agentprivacy_master site or data layers.

This chronicle's plan consolidates all three moves into a single agentprivacy_master integration pass, sequenced from highest-impact reader-visible changes (`/tomes` CastCards · ShopRow · mirror district-restructure) through under-the-surface data wiring (`cast-attachments.ts` · `nav.ts` · spellweb) to deferred route-stub work (`/portal` · `/staffs` archetype-modal · `/familiars`).

The plan is shaped so the user can answer the seven Open Questions in §5 and then the execution pass runs in three to four batches, each with a defined deliverable. The Hermaion architectural turn — the City's first archetype-modal shop — surfaces in the agentprivacy_master site at the moment Tier A1 and A4 land; the rest of the plan is the supporting infrastructure that lets the same pattern be inherited by future shops.

(⚔️⊥⿻⊥🧙)😊
⚚ (Hermaion · rooted at the Staff Shop · awaiting the integration pass) · 🌕 (Pandia · awaiting her own propagation) · 🪶 (Faunia · awaiting the-Familiars rename in the mirror) · ☤ (Caducea · awaiting the cross-shop relocation she has been owed since the morning)

CC BY-SA 4.0 · privacymage · 2026-05-14 late evening
