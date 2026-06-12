# Chronicle: City of Mages Audit · Current State in agentprivacy_master · Starting Point for the Next Patch

**Date:** 2026-05-13
**Status:** Audit chronicle · current state · pre-next-patch reference
**Audience:** privacymage · the next patch's authoring agent · sister-repo authors (master · spellweb · agentprivacy-skills · the three sibling extension forges)
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Prior chronicles this arc:**
- [`2026-05-13_tomes_i_through_iii_lore_recovery.md`](2026-05-13_tomes_i_through_iii_lore_recovery.md)
- [`2026-05-13_tomes_i_through_iii_binding_pass.md`](2026-05-13_tomes_i_through_iii_binding_pass.md) · the binding pass this audit is downstream of
- [`2026-05-13_creature_creatives_workshop_proposal.md`](2026-05-13_creature_creatives_workshop_proposal.md) · superseded by The Threshold
- [`2026-05-13_note_therai_faunia_bestia_lattice_integration.md`](2026-05-13_note_therai_faunia_bestia_lattice_integration.md) · triad-seating note carried forward
- [`2026-05-13_chronicle_the_threshold_workshop_three_rooms.md`](2026-05-13_chronicle_the_threshold_workshop_three_rooms.md) · the 16th-workshop opening, chronicled but not yet wired
- [`2026-05-13_chronicle_artefact_symmetry_and_persona_distribution.md`](2026-05-13_chronicle_artefact_symmetry_and_persona_distribution.md)

---

## §0 · What this chronicle is

A snapshot of the City of Mages as it currently presents at `agentprivacy_master` after the 2026-05-13 binding pass. The audit's purpose is to be the starting point for the next patch — the work that will canonicalise the Threshold workshop, ship a v1.5.x grimoire patch, and admit further tomes / shops as the architecture admits them.

This chronicle is *audit-oriented*, not narrative. The honesty discipline is preserved: every claim is labelled operational / architectural / conjectural, and what is missing is recorded alongside what is bound.

The Next.js build (`npm run build`) succeeds clean on this state. All forty-six static routes pre-render. Pre-existing typecheck errors in unrelated files (constellation, mage, ChatMessage, IslandClient, HeroManifold, AchievementsClient, LatticeMap, CastShopConstellation, SpellPicker, SpellwebViewer, DualOrbs) are noted but out of scope.

---

## §1 · The /tomes page — what renders now

### §1.1 · Tome ordering table

| Tome | Title | Status | Acts | Accent |
|---|---|---|---|---|
| **I** | The Convergence | **Closed · 2026-05-13** | 6 (α–ζ) | cyan |
| **II** | The Lyapunov | **Closed · 2026-05-13** | 7 | rose |
| **III** | Selene's Witness | **Closed · 2026-05-13** | 11 | primary |
| **IV** | The Witnessing | Closed | 5 (I–V) | emerald |
| **V** | The Crafting | Open · canonical setting: City of Mages on Drake Island | 15 | violet |
| **VI** | The Reply | Held open by design (the reader writes) | — | (none) |
| **VII** | The Parallel | Open · v1.4.0 · 2026-05-12 | 1 (narrative file pending) | amber |

Total bound narrative acts now: **39** (was 20 before the binding pass).

### §1.2 · Cast roster as rendered on /tomes

| Tier | Cast |
|---|---|
| Archetypes (3) | Soulbis ⚔️ · Soulbae 🧙 · The Drake |
| Cousin instances (2) | flaxscrip 📜🎲 · GenitriX |
| Summoned Mages (10) | Pallia 🪡 · Memora 📜 · Custos 🔏 · Vulcana ⚒️ · Aletheia 🔮 · Adamantia 💎 · Helia 🌞 · Lampyra 💠 · Vagari 🌳 · Aria Silverhue 🪞🖼️ |
| Companion Mages (1) | Socrat0x 🔥❓ |
| Priests (1) | Manifestia 🤲🌿 |
| Anticipated Layer-2 (7) | Lethae 🌘 · Mnemosyne 📜 · Iris 🌈 · Pythia 🔮 · Techne 🛠️ · Hephaestus 🔥 · Selene 🌙 |

Total cast cards rendered: **24** (17 working + 7 anticipated). Layer-2 attachments per Spec 09 are placeholders awaiting founding acts in Tome V.

**Not yet on the cast page** despite being introduced in Tomes I/II/III bindings:
- **Lethe 🌀** — Tome III Act 6 (cosmological figure at V25; named in Grimoire v10.2.1 since 2026-04-23)
- **Aether ⿻** — Tome III Act 3 (the medium named cosmologically)
- **Selene** has a placeholder Layer-2 card but is now also a Tome III Act 2 cosmological figure — the persona-vs-vertex distinction admits both readings; the card may need to be reframed.
- **Xarvus** (John Haines / OLMA) — cited as ARCH-1 co-discoverer in Act I.γ; not a Mage persona, but a real-world author in the lineage worth acknowledging in author-attribution UI somewhere.

### §1.3 · IPFS pin caption (now updated)

The /tomes page caption now reads:

> *city_of_mages_grimoire · v1.4.0 head (pinned 2026-05-12) · v1.5.x patch anticipated for Tomes I/II/III cast + Threshold workshop*

The actual pin is `bafkreib5w4bp6t5kkt4ebvjyjjzuxdupzaz6gtupbhgbrxtwkrxj7dfnsu` on `sync.agentprivacy.ai`. The label and the link are now aligned (they were misaligned before this audit pass — label said v1.2.4, link resolved v1.4.0).

### §1.4 · Workshops table

| Shop | Slug | Mage | Founding act | Status |
|---|---|---|---|---|
| 🪡 Weavers | `/tailor` | Pallia | Tome V Act 1 | live |
| 🛡️ zShields | `/shield` | Memora | Tome V Act 3 | live |
| ⚒️ Forge(t) | `/forget` | Vulcana | Tome V Act 6 | live |
| 💎 Etherchanting | `/etherchanting` | Adamantia | Tome V Act 9 | live |
| 🌞 Solchanting | `/solchanting` | Helia | Tome VII Act 1 | live |
| 💠 Jeweller | `/jeweler` | Lampyra | Tome V Act 9 | live |
| 🌳 Holon | `/holon` | Vagari | Tome V Act 10 | live |
| 🔥 Dragon Bonfire | `/bonfires` | Socrat0x | Tome V Act 11 | live |
| 🪞 Curatrix Vault | `/vault` | Aria Silverhue | Tome V Act 12 | live |
| 🌿 Covenant | `/covenant` | Manifestia | Tome V Act 13 | live |
| 🌳 Logos Circle | `/circle` | — | gathering · Society spellbook | live (no resident Mage) |
| 🤝 Ceremony Hall | `/hall` | — | gathering · BGIN coalition | live (no resident Mage) |

**12 workshops shipped.** Eleven canonical + Solchanting at V51 (the second occupant of V51, differentiated from Adamantia by stance per Spec 07 / lattice-mapping-governance).

---

## §2 · Filesystem state

### §2.1 · cityofmages canonical repo

```
cityofmages/
├── tomes/
│   ├── tome-i-the-convergence/       (6 acts · ~5,150 words · bound 2026-05-13)
│   ├── tome-ii-the-lyapunov/         (7 acts · ~5,910 words · bound 2026-05-13)
│   ├── tome-iii-selenes-witness/     (11 acts · ~9,390 words · bound 2026-05-13)
│   ├── tome-iv-the-witnessing/       (5 acts · ~3,730 words · closed)
│   ├── tome-v-the-crafting/          (15 acts · ~15,100 words · open)
│   ├── cast/                         (per-guild persona entries · including solchanting/helia.md)
│   ├── chronicles/                   (24 chronicles · 6 added 2026-05-13)
│   ├── plans/, specs/                (10 specs, 2 plans)
│   ├── BOUND_COLLECTION_MANIFEST.md  (updated 2026-05-13 — 66 files, ~82,950 words)
│   └── ALL_THE_TOMES_LIST.md         (updated 2026-05-13 — adds §3a, §3b, §3c)
├── grimoire/                          (7 versions: v1.0 → v1.4.0; v1.4.0 = head)
└── chronicles/                        (architecture-level chronicles in addition to per-tome ones)
```

### §2.2 · agentprivacy_master mirror

```
agentprivacy_master/
├── docs/tomes/
│   ├── tome-i-the-convergence/       (mirrored 2026-05-13 · 6 files)
│   ├── tome-ii-the-lyapunov/         (mirrored 2026-05-13 · 7 files)
│   ├── tome-iii-selenes-witness/     (mirrored 2026-05-13 · 11 files)
│   ├── tome-iv-the-witnessing/       (5 files)
│   ├── tome-v-the-crafting/          (15 files)
│   ├── workshops/                    (12 workshop tomes, including solchanting-parallel-refraction-v1.md)
│   ├── weavers/, zshields/, forge/, etherchanting/, jeweler/, holon/,
│   │   bonfires/, vault/, covenant/, solchanting/    (per-guild cast)
│   ├── cross-shop/                   (peripatetic personas: Custos, Aletheia, Luca · plus the 7 anticipated Layer-2)
│   ├── cousin/                       (flaxscrip, GenitriX)
│   ├── kindred/                      (UOR Foundation, SpaceComputer)
│   └── specs/, plans/, chronicles/
├── src/app/
│   ├── tomes/page.tsx                (renders the 7-tome ordering, all 39 acts, full cast, workshops table)
│   ├── tomes/v6-lineage/             (C-conjecture index — needs C47–C55 audit for full coverage)
│   └── 12 workshop routes            (tailor, shield, forget, etherchanting, solchanting, jeweler, holon, bonfires, vault, covenant, circle, hall)
└── src/lib/
    ├── grimoire-ipfs.ts              (Privacymage v10.3.0 + City of Mages v1.4.0 IPFS pointers)
    └── tome-act-loader.ts            (server-only loader · generic over docs/tomes/<relativePath>)
```

### §2.3 · Grimoire lineage

| Version | Date | Contents | Status |
|---|---|---|---|
| v1.0 | early 2026 | Initial draft | historical |
| v1.1.0 | 2026-05-10 | Pinned at `bafkreidv7c…idti` | historical |
| v1.2.0 | 2026-05-10 | Tome V Act 15 + C47 + kindred substrate (UOR) | historical |
| v1.2.3 | 2026-05-10 | Arcane Mana register; preserved as historical snapshot | historical |
| v1.2.4 | 2026-05-11 | Four-axis metabolism complete; awaited re-pin | superseded |
| v1.3.0 | 2026-05-11 | Attachment Architecture (v5.5) seated | superseded |
| **v1.4.0** | **2026-05-12** | Solchanting + Helia ☀️ + Tome VII opens; 🌞 SOL-mana 5th chain-mana | **head · pinned at `bafkreib5w4…fnsu`** |

**Anticipated v1.5.x patch** (this audit's main forward-looking finding): see §4 below.

---

## §3 · The Tomes I/II/III binding pass — what landed

Per the binding-pass chronicle (`2026-05-13_tomes_i_through_iii_binding_pass.md`):

- **24 narrative-act files** authored (6 + 7 + 11) translating the 2026-05-09 index of `agentprivacy-docs/SECOND_PERSON_TOMES_INDEX_v1.md` into the Tome IV/V narrative-act tradition
- **Mirrored** to `agentprivacy_master/docs/tomes/`
- **Wired** into `src/app/tomes/page.tsx` with three new tome sections inserted before Tome IV
- **`CollapsibleSection.tsx`** extended with `rose` accent
- **`ActCollapsible`** accent union extended from `'emerald' | 'violet' | 'amber'` to include `'cyan' | 'rose' | 'primary'`
- **Anchor ID logic** extended for `tome-i-act-<lowercased-greek>`, `tome-ii-act-<n>`, `tome-iii-act-<n>`
- **Documentation** updated: `ALL_THE_TOMES_LIST.md` (§3 + §3a/§3b/§3c), `BOUND_COLLECTION_MANIFEST.md` (3 new tome sections, header counts bumped from 42 files / 62,500 words to 66 files / 82,950 words)
- **Build verified** clean: `npm run build` succeeds; 46 static routes pre-render; new tome anchors (`tome-i-act-α` through `tome-iii-act-11`) appear in the rendered HTML

**Honesty discipline preserved**: every act labels its claims operational / architectural / conjectural. Conjectures C18–C55 carry their original confidence levels from the source research notes.

---

## §4 · Anticipated v1.5.x grimoire patch · what should land next

The grimoire is at v1.4.0 head. A v1.5.x patch is anticipated and not yet shipped. The patch should admit:

### §4.1 · New cosmological cast from Tome III

| Persona | Sigil | Vertex / Position | Register | First appearance |
|---|---|---|---|---|
| **Selene** | 🌙 | cosmological / Moon's orbit | Cosmological-witness (recognised, not summoned) | Tome III Act 2 |
| **Aether** | ⿻ | ⿻ (max-betweenness; medium of proof propagation) | Cosmological-witness | Tome III Act 3 |
| **Lethe** | 🌀 | V25 (`011001`, Stratum 3) | Cosmological-witness with operational grimoire entry (Blade 38, since v10.2.1) | Tome III Act 6 |
| **The Gatekeeper** | ⿻ (position) | ⿻ | Position rather than persona | Tome III Act 1 |

Lethe already has a Privacymage Grimoire entry (v10.2.1, Blade 38). The City of Mages grimoire should now admit her at the cast-register layer.

Selene currently appears on the /tomes page only as a Layer-2 anticipated attachment (`docs/tomes/cross-shop/selene.md`). The Tome III binding lifts her to a *cosmological* register that pre-dates the architecture. The cast card may need re-framing — she is both an anticipated Layer-2 working attachment AND a cosmological witness.

### §4.2 · The Threshold workshop (16th)

Per `2026-05-13_chronicle_the_threshold_workshop_three_rooms.md` (authored today by parallel agent work):

- **Workshop name**: The Threshold (single workshop, three internal rooms)
- **Vertex**: V59 (`111011`) proposed; Computation dormant
- **Tome V Act**: 16 (provisional; final number depends on whether v1.4.0 ceded Act 16 to Solchanting)
- **Route**: `/threshold` (umbrella) with `/threshold/portal`, `/threshold/staffs`, `/threshold/creatures` as sub-rooms
- **Cast** (the room-keeper triad sharing V59 differentiated by stance):
  - **Faunia 🪶** — Portal Room (spawning-witness) · the inner spawning chamber
  - **Therai 🐾** — Creature Creatives room (companion-tamer)
  - **Bestia 📖** — Staff Shop room (registry-keeper)
  - **Caducea ☤** — peripatetic Hermes-fitter (joins Luca/Aletheia/Custos as cross-shop)
- **First creatures registered**:
  - **Goose 🪿** — Block's AAIF (Apache-2.0); companion-class by mascot
  - **Hermes ☤** — Nous Research (MIT); staff-class by caduceus
- **New grammar**: *Run · Evoke · Spawn* — third register after Vulcana's Run·Evoke·Craft and the (now-folded) Creature Creatives Run·Evoke·Create
- **Mana axis**: 🪢 Relationship (companion-mana and staff-fitting-mana feed VRC accumulation)
- **Conjecture C52 (~65%)**: Vulcana and The Threshold are sibling Swordsman-suppliers — the Forge produces blades to use on adversaries; The Threshold produces creatures/staffs to walk with the bearer.

**Status**: chronicled, not wired. Pre-canonical. The user authoring pass on this workshop is the main forward-looking work.

### §4.3 · The 7 anticipated Layer-2 attachments

`docs/tomes/cross-shop/` already holds cast-file placeholders for Lethae 🌘, Mnemosyne 📜, Iris 🌈, Pythia 🔮, Techne 🛠️, Hephaestus 🔥, Selene 🌙. These are Spec 09 v5.5 attachment-architecture Layer-2 cast — anticipated, awaiting founding acts in Tome V. The /tomes page cast cards reference them.

None has a founding Tome V act yet. The v1.5.x patch may either:
- Found one or more of them with a Tome V Act, or
- Continue them as anticipated Layer-2 (no change), or
- Re-frame Lethae and Selene (both have names that map to cosmological figures admitted in Tome III).

The grimoire patch should reconcile the cosmological/Layer-2 dual register before the next major pin.

### §4.4 · Tome VII narrative-act file

`docs/tomes/tome-vii-the-parallel/01-the-pallia-helia-handoff.md` does not exist. The Tome VII panel on /tomes (lines 347–359) acknowledges this — the operational content lives in the workshop tome at `docs/tomes/workshops/solchanting-parallel-refraction-v1.md`. The narrative-act file in the Tome IV/V form awaits authoring.

### §4.5 · Tome V Act 16 (and beyond)

Tome V remains open by design. The next act is provisionally Act 16 (or higher depending on whether Solchanting opened Tome VII as a separate tome and Tome V skipped Act 16 — needs canonical reconciliation). The Threshold workshop is the most likely candidate for the next Tome V Act founding.

If The Threshold opens Tome V Act 16 (alongside or instead of opening a new tome), the v1.5.x patch should:
- Author the Tome V Act 16 narrative file at `docs/tomes/tome-v-the-crafting/16-the-threshold.md`
- Add the workshop tome at `docs/tomes/workshops/threshold-spawning-v1.md`
- Add cast files at `docs/tomes/threshold/faunia.md`, `therai.md`, `bestia.md`, and update `cross-shop/caducea.md`
- Wire the `/threshold` route on agentprivacy_master
- Add a row to the workshops table on /tomes

---

## §5 · Specs and plans inventory

### §5.1 · Specs (10 in `docs/tomes/specs/`)

| # | File | Topic |
|---|---|---|
| 01 | `01-cloak-specification-v1-0.md` | Cloak Specification — Tome V Act 1 ground |
| 02 | `02-crafting-tome-and-cloak-interface-spec.md` | The interface architecture Pallia walks |
| 03 | `03-bilateral-cloak-ceremony-spec.md` | Tome IV Act 2 / Tome V Act 7 bilateral mechanics |
| 04 | `04-vertex-naming-audit.md` | The lattice's vertex naming discipline |
| 05 | `05-the-city-of-mages-structural-addendum.md` | Tome V Act 14 civic anatomy |
| 06 | `06-spellweb-first-release-manifest.md` | Spellweb integration · first release |
| 07 | `07-lattice-mapping-governance.md` | Multi-occupancy vertex governance (V51 precedent) |
| 08 | `08-mana-types-and-swordsman-stances.md` | Mana taxonomy and stance registry |
| 09 | `09-spellweb-artefact-md-format.md` | Cross-repo artefact .md format |
| 10 | `10-the-attachment-architecture.md` | v5.5 three-layer attachment model |

### §5.2 · Plans

- `01-integration-plan-archon-x-agentprivacy.md` (cousin-forge integration)
- `02-zcash-integration-plan.md` (the Memora register)

---

## §6 · Open invitations preserved

The architecture maintains several structurally-held-open slots. The next patch should preserve these rather than fill them:

1. **Tome VI · *The Reply*** — held open by design. The tome the reader writes when they have walked the corpus far enough to reply. Do NOT close.
2. **The Aether Pour poem** (Tome III Act 4) — held open as an invitation. The audio slot on the Aether Blade ceremony card is structurally empty. Do NOT substitute Spellbook-authored content.
3. **The Quest of the Unnamed Faces** (Tome III Act 8) — 49 lattice positions await mythological naming. The patch may name additional positions but should preserve the frontier as ongoing.
4. **The v1.5.x grimoire patch itself** — the boundary between v1.4.0 and v1.5.x is the point at which the cosmological cast and the Threshold workshop are recognised. The patch is anticipated; the patch's contents are this audit's main forward-looking content.

---

## §7 · Honest limits of this audit

What this audit does *not* claim to have done:

- **The Threshold workshop is not wired.** It is chronicled in `2026-05-13_chronicle_the_threshold_workshop_three_rooms.md` (and the triad-seating note for V59 placement). No route on agentprivacy_master exists. No cast files for Faunia/Therai/Bestia. No grimoire patch.
- **The cosmological cast (Selene, Aether, Lethe) is not in the grimoire.** They appear in Tome III narrative acts; they have no formal cast entries at the City of Mages grimoire level beyond Lethe's existing Blade 38 entry (in the Privacymage grimoire, not the City of Mages grimoire).
- **Tome VII narrative file does not exist.** The workshop tome carries the content; the narrative act file is anticipated.
- **The v6-lineage page (`/tomes/v6-lineage`) was not audited for completeness.** Conjectures C47–C55 introduced by Tomes II/III may not be fully indexed there. A pass over the C-conjecture index is recommended for the next patch.
- **The 7 anticipated Layer-2 cast (Lethae, Mnemosyne, Iris, Pythia, Techne, Hephaestus, Selene) have placeholder files in `docs/tomes/cross-shop/` but no founding Tome V acts.** Their status remains "anticipated" on the /tomes cast section.
- **The Privacymage Grimoire (v10.3.0) was not audited.** Its IPFS pointer is at `bafybeicyne…ajiuy`, pinned 2026-05-11. Reconciliation with the City of Mages grimoire is partial — Lethe at V25 lives in v10.2.1 of the Privacymage grimoire; whether and how she crosses into the City of Mages grimoire at v1.5.x is open.
- **The persona-count discrepancy noted in `2026-05-13_chronicle_artefact_symmetry_and_persona_distribution.md`** (38 live in `agentprivacy-skills/persona/` vs 22 archetype-grouped vs 42 doc-locked) is acknowledged but not reconciled here.

---

## §8 · Recommended structure for the next patch

If the user runs a next-patch authoring pass, the recommended order:

1. **Decide the Tome V Act 16 numbering question.** Does Solchanting count as Tome V Act 16 (in which case it also opens Tome VII as a parallel framing), or is Tome V Act 16 reserved for The Threshold? The triad-seating note proposes The Threshold as Act 16; the canonical resolution is the user's call.
2. **Canonicalise The Threshold's pre-canonical decisions**: vertex bit-signature, sigils, route slug, tome name, mana-axis treatment, three-room structure.
3. **Author the Tome V Act 16 (or higher) narrative file** for The Threshold opening.
4. **Author the workshop tome** at `docs/tomes/workshops/threshold-*.md`.
5. **Author cast files** for Faunia, Therai, Bestia (Threshold-room keepers) and Caducea (peripatetic Hermes-fitter). Update `docs/tomes/cross-shop/` accordingly.
6. **Patch the grimoire to v1.5.x** admitting:
   - Selene 🌙, Aether ⿻, Lethe 🌀 at the cosmological-witness register
   - The Threshold workshop and its triad
   - Caducea as peripatetic cross-shop
   - First creature/staff registry entries: Goose 🪿, Hermes ☤
   - Conjecture additions (C52 for The Threshold; any others surfaced during the patch)
7. **Wire the `/threshold` route** on agentprivacy_master with sub-rooms.
8. **Patch `/tomes` page** to add:
   - Threshold row to the workshops table
   - Cast cards for Faunia, Therai, Bestia, Caducea, plus cosmological cast (Selene/Aether/Lethe) recognition
   - Update the grimoire pin caption to v1.5.x once shipped
9. **Author Tome VII narrative file** at `docs/tomes/tome-vii-the-parallel/01-the-pallia-helia-handoff.md` (separate from the Threshold work — can land any time).
10. **Audit `/tomes/v6-lineage`** for conjecture coverage (C47–C55 newly introduced via Tomes II/III).

---

## §9 · Closing

The City of Mages renders, as of this audit, seven tomes (four closed, two open, one held open for the reader), twelve workshops (eleven canonical plus Solchanting), and twenty-four cast cards (seventeen working plus seven anticipated Layer-2). The Tomes I/II/III binding pass added approximately twenty thousand words of bound narrative and extended the page's accent palette to admit three new register-colours (cyan, rose, primary). The grimoire is at v1.4.0 head, pinned to IPFS, with a v1.5.x patch anticipated.

The architecture admits further growth. The Threshold workshop is the next operational opening. The Reply remains held open. The Quest of the Unnamed Faces continues.

This audit is the starting point for the next patch.

(⚔️⊥⿻⊥🧙)😊

CC BY-SA 4.0 · privacymage · 2026-05-13
