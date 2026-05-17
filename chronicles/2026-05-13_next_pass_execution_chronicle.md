# Chronicle: What Needs To Be Done · Next-Pass Execution Chronicle · Post-v1.5.1 Cleanup · Pre-Integration-Pass

**Date:** 2026-05-13 (end-of-day synthesis)
**Status:** Strategic chronicle · consolidates outstanding work across cityofmages + agentprivacy_master + spellweb · the working document for the next authoring pass
**Audience:** privacymage · the next agent who picks up where this chronicle closes · downstream sister-repo authors
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion chronicles (today's arc · in order of authorship):**
1. `2026-05-13_tomes_i_through_iii_lore_recovery.md` — the binding-pass premise
2. `2026-05-13_tomes_i_through_iii_binding_pass.md` — 24 narrative-act files bound
3. `2026-05-13_tome_vi_review_and_binding.md` — Tome VI Act 1 bound
4. `2026-05-13_chronicle_the_threshold_workshop_three_rooms.md` (prior agent · canonical)
5. `2026-05-13_note_therai_faunia_bestia_lattice_integration.md` (prior agent · V59 triad)
6. `2026-05-13_chronicle_artefact_symmetry_and_persona_distribution.md` (prior agent · substrate × archetype matrix)
7. `2026-05-13_grimoire_v1_5_0_patch.md` — the v1.5.0 patch (Threshold + cosmological cast + Goose/Hermes)
8. `2026-05-13_city_of_mages_audit_post_binding.md` — corpus audit
9. *(in master)* `agentprivacy_master/docs/chronicles/2026-05-13_master_reaudit_post_v1_5_0.md` — master-side re-audit
10. `2026-05-13_cityhall_aaif_v1_5_1_patch.md` (revised) — /hall renamed City Hall · AAIF folded in
11. `2026-05-13_runecraft_protocol_integration_plan.md` — the runecraft-protocol integration plan
12. *(this file)* `2026-05-13_next_pass_execution_chronicle.md` — what needs to be done

---

## §0 · What this chronicle is

A consolidation chronicle synthesising the day's arc into a *single working document* for the next authoring pass. The day produced a substantial amount of work across three repositories; the consolidation chronicle's job is to make the *outstanding* work visible in priority order so the next agent (or the same agent on a future session) can pick up without re-reading the eleven prior chronicles.

The chronicle is *operational* and *honest about decisions still pending*. Each item is labelled by status: ✅ done · 🔄 partial · ❌ not started · 🔒 blocked-on-decision · 🌱 held-open by design.

---

## §1 · What has been resolved (the day's closing position)

### §1.1 · Three substantial patches landed at the cityofmages corpus

| Patch | What it admitted | Status |
|---|---|---|
| **Tomes I/II/III binding pass** | 24 narrative-act files (6+7+11) translating the 2026-05-09 act-index into the Tome IV/V tradition · 11 cast tier · cosmological-witness register | ✅ Bound · pushed to github at commit 223ae57 |
| **v1.5.0 patch** (delta JSON · re-pin pending) | Tome VI Act 1 opens · The Threshold at V59 · 4 new cast (Faunia · Bestia · Therai · Caducea) · Goose 🪿 + Hermes ☤ as first registry entries · 8 new conjectures (later renumbered) | ✅ Delta authored · canonical JSON merge pending |
| **v1.5.1 patch (revised)** | /hall renamed Ceremony Hall → 🏛️ City Hall · AAIF first kindred-coalition · BGIN retroactive second · kindred-coalition fifth structural-relationship category · Gather · Admit · Attest third ceremony grammar | ✅ Delta authored · canonical JSON merge pending |

### §1.2 · Master-side wiring landed

| Wiring | Status |
|---|---|
| Cast files for the four Threshold keepers (Faunia · Bestia · Therai · Caducea) mirrored to `docs/tomes/threshold/` and `docs/tomes/cross-shop/` | ✅ Done |
| Cast files for the three cosmological-witness figures (Selene 🌙 · Aether ⿻ · Lethe 🌀) mirrored to `docs/tomes/cosmological/` | ✅ Done |
| All 24 Tomes I/II/III narrative-act files mirrored to `docs/tomes/tome-i-the-convergence/`, `tome-ii-the-lyapunov/`, `tome-iii-selenes-witness/` | ✅ Done |
| Tome V Act 16 + Tome VI Act 1 + Tome VII Act 1 narrative files mirrored | ✅ Done |
| `/tomes` page patched · workshops table + cast tier 6 cosmological-witnesses + grimoire pin caption | ✅ Done |
| `/hall` page renamed City Hall · AAIF added to RESIDENT_GUILDS array · breadcrumb/h1/hero updated | ✅ Done |
| `src/lib/nav.ts` updated · `/hall` label changed to 'city hall' · standalone `/cityhall` removed · `/guide/agentic-deployments` added (user authored) | ✅ Done |
| Threshold workshop tome `docs/tomes/workshops/threshold-three-rooms-v1.md` authored | ✅ Done |
| `npm run build` passes clean · 46 static routes prerender | ✅ Verified |

### §1.3 · Spellweb-side wiring landed

| Wiring | Status |
|---|---|
| `shop-cityhall` node deleted (standalone /cityhall reverted) | ✅ Done |
| `shop-hall.label` renamed "City Hall" · desc extended with AAIF + BGIN residence | ✅ Done |
| `gateway-aaif` gateway node added · `attribution: 'kindred-coalition'` | ✅ Done |
| `Attribution` type union extended with `'kindred-coalition'` in `src/types/graph.ts` | ✅ Done |
| Edges: `civic → gateway-aaif` × gateway_to + kin_to · `shop-hall → gateway-aaif` × references | ✅ Done |

### §1.4 · The C50 reconciliation is resolved (conjecture renumbering pass)

The v1.5.0 grimoire patch chronicle flagged a C50 conflict (prior C50 "PVM ∥ Bakhta compositional defense" colliding with the new C50 "caduceus as pre-formal dual-agent symbol" from the Threshold chronicle). The user-driven renumbering pass on `tome-vi-the-reply/01-the-readers-first-admission.md` (visible in the file's frontmatter `v6_lineage`) resolves the conflict by moving the Threshold-introduced conjectures into the **C56–C59** range, preserving the prior C49–C55 assignments:

| Conjecture ID | Statement | Status pre-renumber | Status now |
|---|---|---|---|
| C49 | Behavioural Mosca Inequality (Bakhta-response · X_b + Y_b > Z_b) | ✅ Bound in Tome II Act 7 | ✅ Preserved at C49 |
| C50 | PVM multiplicative gating ≡ Bakhta compositional defense | ✅ Bound (Tome II Act 6/7) | ✅ Preserved at C50 |
| C51 | The ⿻ remains max-betweenness (Brandes) | ✅ Bound in Tome III Act 1 | ✅ Preserved at C51 |
| C52 | Aether = Quintessence = the Gap | ✅ Bound in Tome III Act 3 | ✅ Preserved at C52 |
| C53 | Every bnot-pair has a mythological reading | ✅ Bound in Tome III Act 7 | ✅ Preserved at C53 |
| C54 | Phi-Adjacency (δ ≈ 1/φ) | ✅ Bound (Tome III Acts 7-8) | ✅ Preserved at C54 |
| C55 | Privacy is a seventh kind of capital, foundationally | ✅ Bound in Tome III Act 9 | ✅ Preserved at C55 |
| **C56** | Caduceus as pre-formal dual-agent symbol (~60%) | ❌ Was conflict-C50 | ✅ Now C56 (NEW) |
| **C57** | Staff-Mage collapse (held open · what a Mage carries can itself be a Mage) | ❌ Was conflict-C51 | ✅ Now C57 (NEW · held open) |
| **C58** | Vulcana's Forge(t) (V19) ∥ The Threshold (V59) are sibling Swordsman-supplying workshops (~65%) | ❌ Was conflict-C52 | ✅ Now C58 (NEW) |
| **C59** | Create-format as gateway to Mage-tier — Hermes is the first observable case carrying Mage-grade properties at adoption (~70%) | ❌ Was conflict-C49 | ✅ Now C59 (NEW) |

The renumbering is *clean* — no other conjecture references need updating beyond the grimoire patch JSONs and the Threshold-related cast files.

### §1.5 · The runecraft-protocol integration plan is authored

`chronicles/2026-05-13_runecraft_protocol_integration_plan.md` documents the canonical runic-grammar (creat-ur-e · run-e-craft · run-e-create · art-e-fact) and the substrate × archetype matrix (Goose-in-Mage = companion · Hermes-in-Mage = caduceus staff · stance-flipped renderings for Swordsman / Balanced). The plan inventories what to update across all three repositories and proposes a six-phase execution order. **The plan is not executed.** It is the starting point for the next pass.

---

## §2 · New context surfaced this session

### §2.1 · The Creature Creatives proposal has been formally superseded

`chronicles/2026-05-13_creature_creatives_workshop_proposal.md` now carries a SUPERSEDED banner at the top declaring The Threshold (V59 · three rooms · four keepers) as the canonical structure. Creature Creatives is one of the three rooms within The Threshold (Therai's room). The proposal is preserved for historical context; no future authoring should reference it as canonical.

### §2.2 · The `/guide/agentic-deployments` nav link is live

`src/lib/nav.ts` now includes `{ href: '/guide/agentic-deployments', label: 'agentic deployments', key: 'agentic-deployments' }`. This was added by the user and is operational in the nav. The corresponding sub-route under `/guide` is anticipated (or already authored — outside this chronicle's scope). The cityofmages root has `AGENTIC_DEPLOYMENTS_GUIDE.md` and `AGENTIC_DEPLOYMENTS_EXECUTION_PLAN.md` files that may be the source documents.

### §2.3 · The substrate × archetype matrix is canonical

`chronicles/2026-05-13_chronicle_artefact_symmetry_and_persona_distribution.md` (prior agent · canonical) introduces the matrix: substrate-iconographic-affinity × archetype-stance determines artefact configuration. Goose-in-Mage is companion-class · Goose-in-Swordsman is watch-goose · Hermes-in-Mage is caduceus staff · Hermes-in-Swordsman is herald-sentinel · etc. This refines the v1.5.0 first-pass Threshold classification of Goose and Hermes as flatly "staff-class" — they're more accurately stance-rendering matrices.

### §2.4 · Conjecture C59 (create-format gateway) replaces the prior C49 ambiguity

Per the renumbering pass, the "create-format as gateway to Mage-tier" conjecture is now C59 (was a conflict-C49). Hermes is the first observable case carrying Mage-grade properties at adoption. The conjecture is ~70% architectural; it informs whether a Hermes-class staff can graduate to Mage-tier (the staff-Mage collapse · C57 held open) and the design of future framework admissions.

---

## §3 · The outstanding work catalogue (consolidated · all-source)

The following items are outstanding as of end-of-day 2026-05-13. They are grouped by the smallest unit of change and tagged with their source (which prior chronicle / audit flagged each one).

### §3.1 · Tier A · unblocks downstream operations

| # | Item | Status | Source |
|---|---|---|---|
| A1 | **Merge `v1_5_0_patch.json` + `v1_5_1_patch.json` into a canonical `city_of_mages_grimoire_v1_5_1.json`** | ❌ Not started | v1.5.0 patch chronicle §5; master re-audit §2.2 |
| A2 | **Pin v1.5.1 to IPFS** at sync.agentprivacy.ai · record new CID | 🔒 Blocked on A1 | v1.5.0 patch chronicle §5 |
| A3 | **Update `agentprivacy_master/src/lib/grimoire-ipfs.ts`** · bump `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` to v1.5.1 CID · add `V1_5_1` alias constant · v1.4.0 demoted to historical pointer | 🔒 Blocked on A2 | v1.5.0 patch chronicle §5 |
| A4 | **Update grimoire patches with renumbered conjectures** (C56–C59 in v1.5.0 patch · all references in the canonical v1.5.1 JSON) | ❌ Not started | This chronicle §1.4 |
| A5 | **Bake-mirror v1.5.1 grimoire** at `src/data/city-of-mages-grimoire-v1.5.1.json` and `public/models/city-of-mages-grimoire-v1.5.1.json` | 🔒 Blocked on A1 | Master re-audit §3.4 |

### §3.2 · Tier B · master-side data layer wiring

| # | Item | Status | Source |
|---|---|---|---|
| B1 | **Add Tome V Act 16 to `src/lib/tome-v-acts.ts`** · downstream consumers (CastShopConstellation · AchievementsClient · FoundingActPanel) need this to discover The Threshold | ❌ Not started | Master re-audit §3.1 |
| B2 | **Add Faunia · Bestia · Therai · Caducea to `src/lib/cast-attachments.ts`** · four entries · V59 (shared by three) and V0-peripatetic (Caducea) | ❌ Not started | Master re-audit §3.2 |
| B3 | **Stub `src/app/threshold/page.tsx`** · the /tomes Threshold workshop row links to /threshold which currently 404s · should mirror the /cityhall stub pattern with three sub-room cards (Portal Room · Staff Shop · Creature Creatives) | ❌ Not started | Master re-audit §3.3 · audit chronicle §8 item 7 |
| B4 | **Add `/threshold` to `src/lib/nav.ts`** | 🔄 Partial · `/cityhall` was removed correctly · `/threshold` not yet added | This chronicle |

### §3.3 · Tier C · runecraft-protocol integration (the planned six phases)

| # | Item | Status | Source |
|---|---|---|---|
| C1 | **Phase 1 · Terminology audit** · audit every workshop tome's `ceremony_shape` frontmatter · canonicalise "artefact" → "art-e-fact" where structural · audit "creature"/"spawn"/"agent" → "creat-ur-e"/"run-e-create" in narrative-act files | ❌ Not started | Runecraft-protocol integration plan §4 |
| C2 | **Phase 2 · Cast file updates** · update Faunia/Bestia/Therai/Caducea for canonical runic grammar · update Therai's bestiary scope (Goose moves to her keeping per Mage-stance) · update Bestia's bestiary scope (staff-class-by-iconographic-affinity) | ❌ Not started | Integration plan §4 phase 2 |
| C3 | **Phase 3 · Tome narrative updates** · Tome V Act 16 replace "Run · Evoke · Spawn" with Run-e-craft + Run-e-create · Tome VI Act 1 Goose admission moves to Therai's keeping (companion-class Mage-stance default) | ❌ Not started | Integration plan §4 phase 3 |
| C4 | **Phase 4 · Master data layer** · also in Tier B above; the runecraft-protocol alignment applies to the `starterTemplates` and `provenance` strings in B1/B2 | ❌ Not started | Integration plan §4 phase 4 |
| C5 | **Phase 5 · Grimoire patch** · new patch (v1.5.2 or v1.6.0 · user's call) admitting the runic-grammar canonicalisation + substrate × archetype matrix + the stance-rendering refinement of Goose/Hermes · introduces provisional C60 candidate (substrate × archetype matrix as architectural pattern) | ❌ Not started | Integration plan §4 phase 5 |
| C6 | **Phase 6 · Specs + spellweb** · spec 07 §4 substrate-stance multi-occupancy · spec 08 §5 substrate × archetype matrix · spellweb workshop nodes' ceremony_shape strings updated · stance-rendering edges (open design call) | ❌ Not started | Integration plan §4 phase 6 |

### §3.4 · Tier D · documentation finalisation

| # | Item | Status | Source |
|---|---|---|---|
| D1 | **Update `/tomes/v6-lineage` page** · add C48–C59 entries with confidence levels · the v6-lineage index is currently outdated (was at C46 before the day's work) | ❌ Not started | Audit chronicle §8 item 10 · Master re-audit §3.5 |
| D2 | **Update `ALL_THE_TOMES_LIST.md` workshops table reference** (cityofmages housekeeping post-v1.5.1) | 🔄 Partial · §3-§3d done · workshops reference may need a sentence | Master re-audit §2 |
| D3 | **Update `WORKSHOP_LATTICE_AUDIT.md`** · the rename Ceremony Hall → City Hall and AAIF residence note · the Threshold V59 three-keeper-shared case as second canonical multi-occupancy after V51 | ❌ Not started | This chronicle |
| D4 | **Spec 08 v1.3.4** · add Spawning-witness · Registry-keeper · Companion-tamer · Staff-fitter stances to the Swordsman stance registry · confirm SOL-mana row added | ❌ Not started · partial check: SOL-mana row may already be in spec 08 v1.3.x | v1.5.0 patch chronicle §5; Master re-audit §3 |
| D5 | **Spec 07 v1.3.x** · register V59 three-keeper precedent as second canonical multi-occupancy case study (after V51) | ❌ Not started | v1.5.0 patch chronicle §5; Master re-audit §3 |

### §3.5 · Tier E · cross-repo work

| # | Item | Status | Source |
|---|---|---|---|
| E1 | **AAIF outreach** · the bilateral civic-attestation is uni-laterally complete from the City's side · AAIF's reciprocal acknowledgment is user-driven | ❌ Not started · user-driven | v1.5.1 chronicle §5 |
| E2 | **Tome VII Act 2 narrative** (Helia's first program deployment) · anticipated when the parallel-program-deployment ceremony is walked end-to-end | 🌱 Held open · arrives when walked | v1.5.0 patch chronicle §5 |
| E3 | **The 7 anticipated Layer-2 attachments** (Lethae · Mnemosyne · Iris · Pythia · Techne · Hephaestus · Selene-Layer-2) · placeholder files exist · founding acts in Tome V anticipated | 🌱 Held open | v1.5.0 patch chronicle |
| E4 | **The Aether Pour poem** (Tome III Act 4 audio slot) · held open as invitation | 🌱 Held open · do not substitute | Tome III Act 4 itself |
| E5 | **C56–C59 in `/tomes/v6-lineage`** · partial overlap with D1 above | ❌ Not started | This chronicle §1.4 |
| E6 | **Master commit + push** · 74+ uncommitted files in master · user-deferred per prior direction | 🔒 Blocked on user direction | Master re-audit §7 |
| E7 | **Spellweb commit** · uncommitted changes for /hall rename + gateway-aaif + Attribution union · separate repo from master · user may push spellweb independently | 🔒 Blocked on user direction | This chronicle |

### §3.6 · Tier F · open design questions

| # | Item | Status |
|---|---|---|
| F1 | **Sub-routes for /threshold** (`/threshold/portal`, `/threshold/staffs`, `/threshold/creatures`) vs flat /threshold with anchors — both admissible | 🔒 User decides |
| F2 | **v1.5.2 vs v1.6.0 numbering** for the runecraft-protocol canonicalisation — patch-grade vs minor-version-grade | 🔒 User decides |
| F3 | **Stance-rendering edge type** in spellweb (for substrate × archetype matrix) — whether to add or rely on existing `references` | 🔒 User decides |
| F4 | **Re-classification of existing /hall residents** (MyTerms · LFDT · etc.) as kindred-coalitions — some may qualify; v1.5.1 didn't unilaterally re-classify | 🔒 Held open · per-coalition editorial call |
| F5 | **Future kindred-coalition admissions** (e.g. ToIP · IEEE 7012 · Hitchhikers) — the category is open; user-driven | 🌱 Held open by design |
| F6 | **Guild-of-Hermes-Agents** Mage-class — held open per Threshold chronicle §9 | 🌱 Held open by design |

---

## §4 · Priority order for the next pass

If the user picks up tomorrow (or the next agent picks up), the recommended order is:

### First session · Tier A unblock (mechanical · ~1 session)

1. **A1**: Merge the v1.5.0 + v1.5.1 deltas into a self-contained `city_of_mages_grimoire_v1_5_1.json` (apply renumbered C56–C59 in the same merge)
2. **A4**: Update v1.5.0 patch JSON to use C56–C59 (consistency)
3. **A2**: Pin to IPFS · record CID
4. **A3**: Update `src/lib/grimoire-ipfs.ts`
5. **A5**: Bake-mirror to master's `src/data/` and `public/models/`
6. *(Verify)* `npm run build` succeeds with the new pin

### Second session · Tier B master data wiring (~1 session)

7. **B1**: Add Tome V Act 16 to `tome-v-acts.ts` (in canonical runic grammar — *or use plain English now and runic later in Tier C* depending on user preference)
8. **B2**: Add 4 Threshold cast entries to `cast-attachments.ts`
9. **B3**: Stub `/threshold` route (with 3 sub-room cards or flat with anchors · per F1 decision)
10. **B4**: Add `/threshold` to nav.ts
11. **D1**: Update `/tomes/v6-lineage` with C48–C59 (canonical lineage index up-to-date)
12. *(Verify)* `npm run build` clean · `/threshold` renders · v6-lineage page renders

### Third+ session · Tier C runecraft-protocol integration (~3+ sessions)

13. **C1**: Terminology audit pass across workshop tomes + narrative acts (could be tooled · could be by-hand)
14. **C2**: Cast file updates with canonical runic grammar + substrate × archetype matrix
15. **C3**: Tome narrative updates (Tome V Act 16 grammar revision · Tome VI Act 1 Goose-to-Therai classification update)
16. **C5**: Grimoire patch v1.5.2 (or v1.6.0 per F2) admitting runic canonicalisation + matrix + Goose/Hermes stance-rendering · introduces C60 candidate
17. **C6**: Specs + spellweb alignment

### Fourth session · Documentation + outreach

18. **D3 · D4 · D5**: spec updates · WORKSHOP_LATTICE_AUDIT update
19. **E1**: AAIF outreach (user-driven)
20. **E6 / E7**: master commit (and possibly spellweb commit) per user direction

---

## §5 · What is held open by design (preserve · do not close)

These items should *stay* held open in the next pass, not closed prematurely:

- 🌱 **Tome VI** — open by design · each future framework admission is a future Act
- 🌱 **The Aether Pour poem** (Tome III Act 4) — held open as invitation · do not substitute
- 🌱 **The Quest of the Unnamed Faces** — 49 lattice positions await naming
- 🌱 **C51 (max-betweenness)** — open conjecture; admit new bnot-pair namings as they arrive
- 🌱 **C57 (staff-Mage collapse)** — held open per Threshold chronicle §9
- 🌱 **C60 candidate (substrate × archetype matrix)** — provisional · awaits a worked operational example
- 🌱 **Tome VII Act 2** — anticipated when Helia's first program deployment is walked
- 🌱 **Future kindred-coalitions** — the category is open
- 🌱 **The 7 anticipated Layer-2 attachments** — Lethae through Selene-Layer-2 · founding acts await

---

## §6 · Honest limits

This chronicle is *operational*, not narrative. It catalogues outstanding work; it does not claim completeness about *all* outstanding work in the corpus. Items not catalogued here may exist in other contexts (the agentprivacy-skills repo · the spellweb's broader open work · the agentprivacy-docs research-note maintenance · the four sibling extension forges' integration · the Society/Plurality/Canon spellbooks if/when they open).

The Tier ordering is *recommended*, not prescriptive. The user may choose to prioritise Tier C (runecraft-protocol integration) first as the most architecturally consequential pass, accepting that the IPFS re-pin (Tier A) lands later. Or the user may choose to land a v1.5.2 patch that bundles Tier A + Tier B without yet touching Tier C, keeping the runic-grammar canonicalisation as a future v1.6.0. Both are admissible.

The Tier F open design questions are *not* blockers for Tier A · Tier B execution — they can be deferred. They become blockers only when Tier C lands at the grimoire patch authoring (item 16).

---

## §7 · Closing

The day produced eleven prior chronicles, three substantial patches across the cityofmages corpus, master-side wiring of the Threshold + cosmological tier + Tomes I/II/III, spellweb-side wiring of City Hall + AAIF, the conjecture renumbering pass that resolved the C50 conflict, and a runecraft-protocol integration plan whose execution is the next session's natural starting point.

This chronicle's job is to make sure nothing falls through the cracks. Tier A (IPFS re-pin + grimoire-ipfs.ts bump) unblocks downstream master operations. Tier B (data-layer wiring) makes The Threshold operationally visible in the Next.js app. Tier C (runecraft-protocol integration) is the largest single architectural alignment pass; it is also the most semantically consequential. Tier D (specs + v6-lineage) finalises the corpus's reference layer. Tier E covers cross-repo outreach and held-open items.

The architecture admits this much. The next pass picks up at Tier A item 1.

(⚔️⊥⿻⊥🧙)😊
ᚢ ᛖ
🏛️ ☤ 🪿

CC BY-SA 4.0 · privacymage · 2026-05-13
