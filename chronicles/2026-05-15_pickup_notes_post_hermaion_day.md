# Pickup Notes · 2026-05-15 · After the 2026-05-14 Hermaion Day

**Authored:** 2026-05-14 late evening
**For:** the next session (2026-05-15+)
**Reading order:** start here, then the four chronicles in §5

---

## §0 · TL;DR (read first · 30 seconds)

Yesterday landed **three canonical moves at the Threshold District** in one day (morning: district restructure · afternoon: the-Familiars rename · evening: **Hermaion ⚚ + Alexandrite + archetype-modal-shop** architectural turn) AND **Pass 1 of agentprivacy_master integration** (`/tomes` page · `/runecraft` page · `cast-attachments.ts` · mirror district-restructure with 3 new subdirs + legacy README). The City's first archetype-modal shop is live in the site at `/tomes` and `/runecraft`.

**Tomorrow's single highest-priority pickup:** author `grimoire/city_of_mages_grimoire_v1_6_0_patch.json` (user's confirmed decision: v1.6.0 new-head patch bundling Hermaion + Pandia + Pleione + the-Familiars rename + archetype-modal-shop pattern + C58 canonisation). Everything else cascades from this — IPFS re-pin → `grimoire-ipfs.ts` CID update → fresh end-to-end build.

---

## §1 · What's in canonical state now (verify if uncertain)

**Threshold District @ V59** (post-2026-05-14 restructure):

| Shop | Keeper | Sigil | Gem | Stance | Canonical file |
|---|---|---|---|---|---|
| Portal Room | Pandia (daughter of Selene) | 🌕 | Moonstone `#c8d4e0` | Display-witness | `tomes/cast/portal-room/pandia.md` |
| **Staff Shop** ⚡ | **Hermaion** (ἕρμαιον · Hermes-gift) | **⚚** | **Alexandrite** (dual-aspect `#3d7c47` green-Mage ↔ `#a23a3a` red-Swordsman) | Registry-keeper · **archetype-modal** | `tomes/cast/staff-shop/hermaion.md` |
| the Familiars | Faunia (Roman Fauna) | 🪶 | Amber `#d97706` | Companion-witness | `tomes/cast/familiars/faunia.md` |
| (peripatetic) | Caducea | ☤ | — | Hermes-class fitter (fits both Hermaion aspects) | `tomes/cast/threshold/caducea.md` (relocation to `cross-shop/` pending) |

**Conjecture C58** (Vulcana's Forge(t) ∥ Threshold's Staff Shop sibling Swordsman-suppliers) promoted ~65% → ~85%.

**Workshop count:** 13 → 15 (Threshold-as-three sibling shops) → 16 (Chart Shop @ V44 · Navigation District opens).

**SUPERSEDED but preserved as historical** (do NOT edit bodies):
- `tomes/cast/staff-shop/bestia.md` (status_note + superseded_by frontmatter point to hermaion.md)
- `tomes/cast/portal-room/triodos.md` (superseded by Pandia, 2026-05-14 morning)
- `tomes/cast/charthouse/pelagia.md` (superseded by Pleione, 2026-05-14 morning)
- Legacy `tomes/cast/threshold/{bestia,faunia,therai,caducea}.md` (pre-district-restructure)
- `tomes/cast/goose-shop/faunia.md` (pre-the-Familiars-rename)
- Tome VI Act 1 body @ `tome-vi-the-reply/01-the-readers-first-admission.md` — bound; frontmatter has `keeper_succession` + `canonical_keepers_now`; body retains 2026-05-13 inception-state naming

---

## §2 · Where to start tomorrow · the priority queue

### Pickup #1 (HIGH · pre-everything-else) · Grimoire v1.6.0 patch JSON

**Decision already locked:** new `v1_6_0_patch.json` head (not a sub-patch · supersedes v1.5.0 candidate + v1.5.0 patch + v1.5.1 City Hall+AAIF patch).

What it admits:
- Hermaion ⚚ cast entry (replaces Bestia 📖); preserve Bestia as `superseded_in_v1_6_0` field
- Pandia 🌕 cast entry (replaces Triodos draft); preserve Triodos similarly
- Pleione 🧭 cast entry (replaces Pelagia draft, V44 Hold-witness)
- Faunia 🪶 re-homed to the Familiars (shop renamed Goose Shop → the Familiars)
- Therai retire (held open · could return)
- **New pattern type:** `archetype_modal_shop` (first instance: shop-staff-shop; fields: `gem_color_mage`, `gem_color_swordsman`, `archetype_modal: true`)
- **New gem type:** `alexandrite_dual_aspect` (color-shifting beryl; both color fields)
- Workshop count 13 → 16
- Threshold District + Navigation District as new top-level `workshop_districts` block (eight-district taxonomy from morning chronicle §6)
- Conjecture register: C58 promoted to ~85% (claim canonical close); C63 candidate (attentional workshop register) registered
- Tome V Act 16 references updated to point at successor cast (keeper_succession field)
- IPFS pin pointer (placeholder until re-pin)

**Scripts/files involved:**
- `grimoire/scripts/merge_v1_5_0_patch.py` — adapt or write `merge_v1_6_0_patch.py`
- `grimoire/city_of_mages_grimoire_v1_5_0_candidate.json` — read for structural template
- `grimoire/city_of_mages_grimoire_v1_5_1_patch.json` — read for structural template

Output: `grimoire/city_of_mages_grimoire_v1_6_0_patch.json` + (after merge) `grimoire/city_of_mages_grimoire_v1_6_0.json` head.

### Pickup #2 (HIGH · user action) · IPFS re-pin

Manual step. After Pickup #1, the user pins the v1.6.0 head JSON to IPFS and returns the new CID. Then Pickup #3 lands.

### Pickup #3 (MEDIUM · post-IPFS) · `agentprivacy_master/src/lib/grimoire-ipfs.ts`

Update the CID constant to the new v1.6.0 pin. Currently points at v1.4.0 `bafkreidxhmuykjew6dtnuprggtd2rapwm43ghtmfhf2occ2wfk2zpx2b6a`.

### Pickup #4 (MEDIUM · cityofmages cross-ref sweep)

- `tomes/tome-v-the-crafting/16-the-threshold.md` — add `keeper_succession` + `canonical_keepers_now` frontmatter (parallel to Tome VI Act 1 treatment); body preserved
- `tomes/bestiary/goose.md` line 99 — "Bestia to mark the substrate-instance Hermes-class" → "Hermaion to mark..."
- `tomes/bestiary/hermes.md` — sweep Bestia/📖 references (haven't scouted yet)
- `tomes/cast/cross-shop/caducea.md` — add Hermaion ⚚ sister-of-rooted-aspect reference (currently file exists per scout but content unknown)
- `tomes/cast/threshold/caducea.md` → `tomes/cast/cross-shop/caducea.md` relocation (was pending from morning chronicle §9.2 item 5)
- `README.md` (cityofmages root) — 1 hit; one-line sweep
- `AGENTIC_DEPLOYMENTS_GUIDE.md` + `AGENTIC_DEPLOYMENTS_EXECUTION_PLAN.md` — sweep + add Hermaion items

### Pickup #5 (MEDIUM · agentprivacy_master Pass 2 · `src/lib/` sweep)

Files that had Bestia/Sodalite hits in the earlier grep (verify each · most are 1-line refs):
- `nav.ts` — Staff Shop sigil 📖 → ⚚; optional `WORKSHOP_DISTRICTS` grouping
- `shop-witnesses.ts`
- `spellbook-templates.ts`
- `agent-substrates.ts`
- `model-downloads.ts`
- `soulbae.ts`
- `skills-data.ts`
- `zcash-memo.ts`
- `ceremony/types.ts`
- `ceremony/constellation.ts`

### Pickup #6 (LOWER · spellweb + skills · Pass 3)

- `src/lib/spellweb/labels.ts` — Hermaion label + dual-aspect gem node + succession edges
- spellweb node registration (cast-hermaion · cast-pandia · cast-pleione · gem-alexandrite-dual-aspect · shop-staff-shop with archetype_modal: true)
- spellweb edge registration (cast-bestia → succeeded_by → cast-hermaion · cast-caducea → fits_for → cast-hermaion both aspects · gem-alexandrite-dual-aspect → encoded_in → shop-staff-shop · etc.)
- `agentprivacy-skills/persona/` — author Hermaion, Pandia, Pleione, Faunia-at-Familiars personas (separate repo)

### Pickup #7 (DEFERRED · route stubs · Pass 4)

- `/portal` route stub (Pandia · Display-witness · Display·Choose·Dispatch UI)
- `/staffs` route stub (Hermaion · **archetype-modal rendering** — see Open Question §3.2)
- `/familiars` route stub (Faunia · Run·Evoke·Spawn UI)

### Pickup #8 (DEFERRED · GemBadge dual-aspect refactor · Pass 4)

Currently two side-by-side chips (`#3d7c47` + `#a23a3a`). Refactor option: single chip with diagonal-split or gradient encoding the dual-aspect.

---

## §3 · Open questions still held (no decision yet)

### §3.1 · GemBadge refactor scope

Single-chip dual-aspect rendering (Pickup #8) or keep the two-chip interim? **Recommendation:** keep interim until `/staffs` route is built · refactor as part of that work.

### §3.2 · Archetype detection at `/staffs`

How does the page know the visitor is a Mage vs Swordsman? Options: cookie · explicit click · persisted soul-state · query param · browser fingerprint of visitor's persona-state from prior sessions. **No decision yet.** Influences `/staffs` route work in Pickup #7.

### §3.3 · 2026-05-13 historical chronicle banners

Should the 12 chronicles in `chronicles/2026-05-13_*.md` get a 1-line header banner pointing to the 2026-05-14 successions, or remain pristine historical records? **Recommendation:** leave as-is (the chronicle dates self-identify the inception-state). Override only if the user disagrees.

---

## §4 · Build / verify checklist (if you want to test)

Before/during/after Pickup #5:

```
cd /c/Users/mitch/agentprivacy_master
npm run typecheck       # verify cast-attachments.ts + tomes/page.tsx + runecraft/page.tsx all compile
npm run build           # full Next.js build to catch route issues
npm run dev             # spot-check /tomes and /runecraft visually
```

Anticipated TypeScript-clean from yesterday's edits (no schema changes were introduced beyond optional new fields on existing interfaces). If TS errors surface, the most likely culprits:
- `accentMage` / `accentSwordsman` / `archetypeModal` new props on the runecraft shopfront object — check the shopfront type definition for `additionalProperties: false` style strictness
- `Pleione` CastCard's `vertex` string format — should match existing format conventions
- `successionNote` prop on Tome VI Act 1 mage field — I added this in the chronicle plan but didn't end up wiring it; the mage prop is fine without it

If type errors: easiest fix is to extend the relevant interfaces with the new optional fields.

---

## §5 · Chronicle trail (reading order if you need to reconstruct context)

The four chronicles from yesterday, in order:

1. `chronicles/2026-05-14_chronicle_district_restructure_and_canonical_keeper_naming.md` — **the big one** · morning district restructure + afternoon the-Familiars rename + §11 added documenting evening Hermaion pass
2. `chronicles/2026-05-14_chronicle_hermaion_admission_and_alexandrite_archetype_modal_shop.md` — Hermaion inception chronicle (sigil + gem + archetype-modal-shop pattern explained in depth)
3. `chronicles/2026-05-14_chronicle_hermaion_integration_plan_for_agentprivacy_master.md` — the agentprivacy_master integration plan (Tiers A/B/C/D · seven open questions · user's four answers in §6½ addendum)
4. `chronicles/2026-05-15_pickup_notes_post_hermaion_day.md` — this file

If you only have time for one chronicle to get oriented, read **#1** (it's the load-bearing structural document); the others elaborate.

---

## §6 · Key file pointers (where things live now)

### Cityofmages canonical cast
- `tomes/cast/portal-room/pandia.md` · `triodos.md` (superseded)
- `tomes/cast/staff-shop/hermaion.md` · `bestia.md` (superseded)
- `tomes/cast/familiars/faunia.md`
- `tomes/cast/charthouse/pleione.md` · `pelagia.md` (superseded)
- `tomes/cast/threshold/*.md` — legacy historical
- `tomes/cast/goose-shop/faunia.md` — pre-rename historical
- `tomes/cast/cross-shop/caducea.md` — Caducea canonical

### Agentprivacy_master mirror cast (short-form pointers)
- `docs/tomes/portal-room/pandia.md` · `docs/tomes/staff-shop/hermaion.md` · `docs/tomes/familiars/faunia.md` — NEW from yesterday Pass 1
- `docs/tomes/charthouse/pleione.md` — already existed
- `docs/tomes/threshold/README.md` — NEW · legacy-directory note
- `docs/tomes/threshold/{bestia,faunia,therai}.md` — legacy

### Agentprivacy_master site
- `src/app/runecraft/page.tsx` — Staff Shop shopfront card live
- `src/app/tomes/page.tsx` — 3 District CastCards + Pleione CastCard + Tome VI Act 1 panel + 4 sibling ShopRows live
- `src/lib/cast-attachments.ts` — Pandia + Hermaion + Faunia-at-Familiars seated · Pleione already seated · Bestia/Therai retired

### Memory
- `~/.claude/projects/C--Users-mitch/memory/project_the_threshold_workshop.md` (updated top-section)
- `~/.claude/projects/C--Users-mitch/memory/project_hermaion_archetype_modal_shop.md` (NEW)
- `~/.claude/projects/C--Users-mitch/memory/MEMORY.md` (index)

---

## §7 · One-line orienting note

The City got its first archetype-modal shop yesterday — Hermaion ⚚ at the Staff Shop, alexandrite green-Mage ↔ red-Swordsman. The site reads canonical state. The grimoire JSON head is the last big rock; everything else is sweep work.

(⚔️⊥⿻⊥🧙)😊
⚚ · 🌕 · 🪶 · 🧭 · ☤
