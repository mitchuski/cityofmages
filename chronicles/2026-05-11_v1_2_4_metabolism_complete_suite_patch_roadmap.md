# Chronicle — v1.2.4 Metabolism Complete · Suite Patch Roadmap

**Date:** 2026-05-11
**Status:** Authored canonical · awaits fresh IPFS re-pin and suite-wide propagation
**Audience:** privacymage (next session) · downstream agents · contributors
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §0 · What this chronicle is

A **working document** capturing the v1.2.4 grimoire state (metabolism completed at four mana axes) and the **prioritised patch list** for propagating this state across the agentprivacy suite. Pick this up cold next session and work from §2 onward — each item names files, line ranges, and edit-sized scope.

---

## §1 · What landed in v1.2.4

The City of Mages grimoire is at **v1.2.4** (canonical: `agentprivacy-docs/models/city_of_mages_grimoire_v1_2_0.json`; mirrored at `cityofmages/grimoire/city_of_mages_grimoire_v1_2_0.json` + `_v1_2_4.json` explicit-version; `_v1_2_3.json` preserved as historical snapshot).

### §1.1 · Four mana axes · the City's metabolism completed

The metabolism is now structurally explicit at **four axes** instead of two. New top-level field `mana_taxonomy` (parallel to `personas`, `kindred_substrate_providers`, `kindred_ecosystems`).

| # | Axis | Register(s) | Symbol(s) | Purpose | Status |
|---|---|---|---|---|---|
| 1 | **Landing** | chain-mana (plural by chain) | Ξ Aether (Ethereum) · ₿ sats (Bitcoin Lightning) · 🌹 ROSE (Oasis) · 🦓 z-mana (Zcash) | Make a working *land* on consensus | All 4 variants operational |
| 2 | **Entropy** | Arcane ⊥ Celestial | ✨ Arcane · 🌌 Celestial | Make a working *unique* | Both operational; Celestial wired at 3 shops |
| 3 | **Coordination** *(NEW)* | 🔭 Resonance Mana | 🔭 | Generate value when two Mages find affinity *without a central index* (Bilateral Witness; 7th Capital in motion; **Scrying Glass primitive**) | Architectural · awaits operational Scrying Glass impl |
| 4 | **Relationship** *(NEW)* | 🪢 VRC Mana | 🪢 | Store the *residue of being alive* as Verifiable Relationship Credentials (captured in **Fan Passport**; fuels **Loom of Programmable Covenants**) | Architectural · awaits VRC issuance + Fan Passport surface |

### §1.2 · Four structural-relationship categories (canonical since v1.2.2)

| # | Category | First instance | Grimoire field |
|---|---|---|---|
| 1 | Cousin-forge | Archon | `personas.cousin_instances` |
| 2 | Kindred-protocol | Covenant of Humanistic Technologies | `external_partner` on Manifestia |
| 3 | Kindred-substrate | UOR Foundation | `kindred_substrate_providers` |
| 4 | Kindred-ecosystem | SpaceComputer | `kindred_ecosystems` |

### §1.3 · Pin state

| Version | CID | Status |
|---|---|---|
| v1.1 | `bafkreidv7c…idti` | live · historical resolution |
| v1.2 (base) | `bafkreidxhmuyk…2b6a` | live · current `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` |
| v1.2.1 (Luca) | — | authored · awaits re-pin |
| v1.2.2 (SpaceComputer + two-mana) | — | authored · awaits re-pin |
| v1.2.3 (Arcane Mana rename) | — | authored · awaits re-pin |
| **v1.2.4 (metabolism complete · Resonance + VRC)** | — | **authored · awaits re-pin · CURRENT HEAD** |

---

## §2 · Suite patch roadmap · prioritised punch list

Items are ordered by **leverage** (cost to apply × impact on coherence). Each item names files, scope, and edit size.

### 🔴 P0 · Re-pin v1.2.4 and propagate the new CID

**Effort:** ~10 min (after re-pin lands)
**Files (rotation pattern; established in v1.1 → v1.2 sync):**
1. `agentprivacy_master/src/lib/grimoire-ipfs.ts` — bump `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` to v1.2.4 CID; retain v1.2 CID as `_V1_2` historical constant; update header comment
2. `agentprivacy-docs/models/city_of_mages_grimoire_v1_2_0.json` — `ipfs_pin_status` field with new CID
3. Re-sync 6 mirror copies (the PowerShell script already exists pattern-wise; just copy from canonical)
4. README/MAPPING surfaces (6 files): `agentprivacy-skills/README.md` + `MAPPING.md` · `zk blades forge/README.md` · `swordsman-blade/README.md` · `mages-spell/README.md` · `agentprivacy-docs/GLOSSARY_MASTER_v4_0.md`

**Why P0:** The CID is the architecture's anchor. Until v1.2.4 is pinned, the entire suite operates on a content-ahead-of-pin state. Re-pin closes that drift.

### 🔴 P1 · Workshop pages · surface the four-axis taxonomy

**Effort:** ~30 min
**Files (master):**
- `src/app/etherchanting/page.tsx` §5 — current Aether ⊥ Celestial framing; extend to mention 🔭 Resonance Mana (queued; not yet wired) + 🪢 VRC Mana (relationship-shaped value; not yet wired). Or, simpler: add a brief "future mana axes" subsection.
- `src/app/forget/page.tsx` — similar light addition
- `src/app/holon/page.tsx` — similar
- All 7 workshop pages (etherchanting, forget, covenant, jeweler, holon, shield, vault) — could surface the four-axis model as a shared sidebar/footer cross-reference, OR a single canonical reference doc `/poems` or `/model` page

**Recommended approach:** Add a new section in `/model` (or another canonical-room page) titled **"The City's Metabolism · Four Mana Axes"** with a single table; cross-link from workshop pages instead of duplicating.

### 🟡 P2 · Spec docs · spec 08 already refactored for chain-mana + Arcane

**Effort:** ~15 min
**Files:**
- `cityofmages/tomes/specs/08-mana-types-and-swordsman-stances.md` — already refactored in this session for chain-mana pluralism + Arcane register; **still needs Resonance + VRC additions** (4 axes total). §0 framework paragraph + §2 mana registry table + §4 ecosystem pairing table need a third section.
- `agentprivacy_master/docs/tomes/specs/08-mana-types-and-swordsman-stances.md` (if present) — likely the source of truth that `cityofmages/` mirrors; update there too if so.

### 🟡 P3 · Formal canon chronicle update

**Effort:** ~20 min
**File:** `agentprivacy-docs/chronicles/2026-05-11_two_mana_economy_and_kindred_ecosystem_category_formalised.md`

Currently records the three-register/two-axis state (chain-mana + Arcane + Celestial). Needs to be either:
- (a) Renamed and extended to capture v1.2.4's four-axis state, OR
- (b) Sibling chronicle written at `2026-05-11_metabolism_complete_four_mana_axes_formalised.md` referencing the prior chronicle and capturing the v1.2.4 amendment

(b) preserves the historical record; (a) updates in place.

### 🟢 P4 · Master pages workshop mana annotations

**Effort:** ~15 min per workshop · 4 workshops have annotations to refresh
**Context:** When workshop pages were updated to use chain-specific emoji (Ξ, ₿, 🌹, 🦓), they did NOT mention Resonance or VRC. Light cross-references to `/model` or a canonical metabolism page would close that loop.

### 🟢 P5 · Cast files in cityofmages/tomes/cast/ — mana annotations

**Effort:** ~10 min per file · 14 named cast files
**Files:** `cityofmages/tomes/cast/<guild>/<persona>.md` — each cast file could carry a `mana_consumption` frontmatter or section: which chain-mana the cast member's primary work draws on, whether they wire Celestial Mana yet, whether they participate in Resonance Mana or VRC Mana flows.

Not blocking for v1.2.4 re-pin; defer to a focused cast-audit session.

### 🟢 P6 · Blog series cross-reference

**Effort:** ~5 min per post · 12 blog posts
**Files:** `cityofmages/blog/blog-post-08-adamantia-etherchanting.md` etc.

The blog series was reconciled to v1.2.x state in the HANDOFF_NOTE.md flow but doesn't yet mention v1.2.4's Resonance/VRC. Light additions to relevant posts (probably blog-post-01, -08, -09, and one new post if you want to fully narrate the metabolism).

### 🟢 P7 · A new Tome V act narrating the metabolism (deferred)

**Effort:** open-ended · authoring
**Working titles flagged in grimoire v1.2.4 version_notes:**
- *The Scrying Glass* — narrates Resonance Mana recognition
- *The Loom of Programmable Covenants* / *The Fan Passport* — narrates VRC Mana recognition

Deferred per the user's own pattern: a Tome V act is authored when sustained operational use *earns* the recognition. Not yet; flagged for the future.

### 🟢 P8 · spellweb integration

**Effort:** ~20 min
**Files:**
- `cityofmages/spellweb-integration/` and `spellweb/src/data/` graph data may need new node/edge types for the new mana primitives (Scrying Glass, Fan Passport, Loom of Programmable Covenants). Likely best as a follow-up after the operational implementations land.

---

## §3 · Conceptual map · how the four axes relate to existing primitives

This is the framing you can use when explaining the metabolism to a downstream reader or another agent:

```
        ┌─────────────────────────────────────────────────────────┐
        │            The City's Metabolism (v1.2.4)               │
        ├─────────────────────────────────────────────────────────┤
        │                                                         │
        │  LANDING ──────────► chain-mana (plural by chain)       │
        │      ↓               Ξ · ₿ · 🌹 · 🦓 · ...              │
        │  pays consensus     paid to consensus per chain         │
        │                                                         │
        │  ENTROPY ──────────► ✨ Arcane ⊥ 🌌 Celestial            │
        │      ↓               loop-closed vs loop-open           │
        │  makes unique       depth of non-reconstructibility    │
        │                                                         │
        │  COORDINATION ────► 🔭 Resonance Mana                   │
        │      ↓               Scrying Glass primitive            │
        │  finds affinity     7th Capital in motion              │
        │                     Bilateral Witness register          │
        │                                                         │
        │  RELATIONSHIP ────► 🪢 VRC Mana                          │
        │      ↓               Fan Passport · VRCs                │
        │  stores residue     Loom of Programmable Covenants     │
        │                                                         │
        └─────────────────────────────────────────────────────────┘
```

Existing primitives the four axes connect to:

- **chain-mana** ← every transaction-shop pays here (Etherchanting, zShields, Forge(t), Etc.)
- **Arcane Mana** ← every shop's default randomness supply before Celestial wired
- **Celestial Mana** ← SpaceComputer; 3 shops operational (Etherchanting, Forge(t), Holon Hitchhikers)
- **Resonance Mana** ← Scrying Glass; not yet operational; framing: when two Sovereigns recognise each other without a central register, that recognition has value (the 7th Capital made operational)
- **VRC Mana** ← Fan Passport (the artifact that accumulates VRCs); Loom of Programmable Covenants (the production form — programmable covenants that compile against the bearer's VRC ledger)

The **Scrying Glass primitive** and the **Loom of Programmable Covenants** are named here for the first time. They may already have prior framings elsewhere in the corpus (Pallia's loom; bilateral witness ceremonies); this v1.2.4 grimoire amendment is the architectural commitment to recognise them as *mana primitives* rather than only as workings.

---

## §4 · Quick-reference file inventory

### Where the canonical lives
- `agentprivacy-docs/models/city_of_mages_grimoire_v1_2_0.json` — **v1.2.4 content**; hash `703720FD…`
- `agentprivacy-docs/chronicles/2026-05-11_two_mana_economy_and_kindred_ecosystem_category_formalised.md` — formal canon chronicle (needs v1.2.4 extension; see P3)

### Six canonical-filename mirrors (all hash-match canonical)
1. `agentprivacy_master/src/data/city-of-mages-grimoire-v1.2.0.json`
2. `agentprivacy-skills/grimoire/city_of_mages_grimoire_v1_2_0.json`
3. `zk blades forge/city_of_mages_grimoire_v1_2_0.json`
4. `swordsman-blade/city_of_mages_grimoire_v1_2_0.json`
5. `mages-spell/city_of_mages_grimoire_v1_2_0.json`
6. `cityofmages/grimoire/city_of_mages_grimoire_v1_2_0.json`

### Version-explicit files in cityofmages/grimoire/
- `city_of_mages_grimoire_v1_0.json` — v1.0 (initial; 59 KB)
- `city_of_mages_grimoire_v1_1_0.json` — v1.1 (pinned at `bafkreidv7c…idti`; 130 KB)
- `city_of_mages_grimoire_v1_2_3.json` — v1.2.3 historical snapshot (hash `CEC54AA6…`; 178 KB; preserved frozen at v1.2.3)
- `city_of_mages_grimoire_v1_2_4.json` — v1.2.4 explicit-version current head (hash `703720FD…`; ~189 KB)

### Master pipeline
- `agentprivacy_master/src/lib/grimoire-ipfs.ts` — `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` constant (current value: v1.2 CID; needs rotation to v1.2.4 once pinned)
- `agentprivacy_master/src/lib/grimoire-baked.ts` — imports `@/data/city-of-mages-grimoire-v1.2.0.json`; path unchanged through v1.2.x bumps

### Surface docs to update on each v1.2.x bump
1. `agentprivacy-skills/README.md` (Post-V5.4 addendum paragraph)
2. `agentprivacy-skills/MAPPING.md` (Grimoire bundling §)
3. `zk blades forge/README.md` (header + bundled-grimoire line)
4. `swordsman-blade/README.md` (bundled-grimoire line)
5. `mages-spell/README.md` (bundled-grimoire line)
6. `agentprivacy-docs/GLOSSARY_MASTER_v4_0.md` (Status / Coverage / Pipeline / IPFS pins)
7. `agentprivacy_master/src/lib/grimoire-ipfs.ts` (header comment + CITY_OF_MAGES_GRIMOIRE_IPFS_URL constant)
8. `cityofmages/CHANGELOG.md` (grimoire version section)
9. `cityofmages/ALL_THE_TOMES_LIST.md` (§9 grimoire reference)
10. `cityofmages/README.md` (Quick map · grimoire listing)

---

## §5 · Where v1.2.4 changed what

If you're auditing a doc to check whether it's v1.2.4-aware, look for these markers:

| Marker present? | What it tells you |
|---|---|
| Mentions "✨ Arcane Mana" or "Arcane register" | v1.2.3 or later |
| Mentions "🔭 Resonance Mana" or "Scrying Glass primitive" | **v1.2.4** specifically |
| Mentions "🪢 VRC Mana" or "Fan Passport" or "Loom of Programmable Covenants" | **v1.2.4** specifically |
| Mentions "two-mana economy" without Resonance/VRC mention | Pre-v1.2.4 (likely v1.2.2 or v1.2.3); needs extension |
| Mentions "Aether Mana" as universal chain-gas (covering Ethereum + Bitcoin + Oasis + Zcash) | Pre-v1.2.3 framing; needs the chain-mana plurality refactor |
| Mentions "13 named cast" or "36 spells" | Pre-v1.2.1 (before Luca); historical snapshot or stale |
| Mentions "14 Tome V acts" | Pre-v1.2 (before Act 15); historical snapshot |

Use this table when auditing any doc in the suite.

---

## §6 · One-line summary

The City's metabolism is complete at four mana axes: chain-mana lands the working, Arcane or Celestial makes it unique, 🔭 Resonance generates value when two Mages match, 🪢 VRC stores the residue as relationship credentials. Grimoire is at **v1.2.4** awaiting re-pin; six canonical-filename mirrors hash-match; suite-wide propagation pattern is the v1.1 → v1.2 template. Pick the punch list up from §2; next task is the re-pin (P0).

`(⚔️⊥⿻⊥🧙)😊`

🌌 ⊥ ✨ ⊥ 🔭 ⊥ 🪢
Ξ · ₿ · 🌹 · 🦓

CC BY-SA 4.0 · privacymage · curated for the City of Mages · 2026-05-11
