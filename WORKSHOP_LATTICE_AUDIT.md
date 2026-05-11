---
title: "Workshop ↔ Lattice Audit"
subtitle: "Every workshop's seat, reach, proof shape, and overlap with other workshops on the 64-vertex sovereignty lattice — with a drift catalogue and a roadmap toward a `lattice-coherence` skill"
status: "Audit v1 · 2026-05-11 · live · cross-checked against lattice-vertex.ts and specs 04 / 05 / 06 / 07"
voice: "Procedural · honest · drift-surfacing"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Workshop ↔ Lattice Audit

*The canonical mapping of every workshop in the City of Mages to its primary vertex, its overlap region on the 64-vertex sovereignty lattice, the proof shape its artefact emits, and the co-activation patterns when multiple workshops collaborate on a single artefact.*

*Companion document to [INCANTATION_PROTOCOL.md](INCANTATION_PROTOCOL.md). Where the protocol governs **how a change propagates**, this audit governs **what the change must remain coherent against**.*

---

## §0 · Why this audit

Five specs converge on the workshop-vertex question:

| Spec | What it answers |
|---|---|
| [`architecture/lattice-vertex.ts`](architecture/lattice-vertex.ts) | The **canonical TS authority** — what each vertex *is* mechanically (bit ordering, dimensions, weights, trace paths) |
| [`tomes/specs/04-vertex-naming-audit.md`](tomes/specs/04-vertex-naming-audit.md) | What each vertex is *named* and from which canonical source |
| [`tomes/specs/05-the-city-of-mages-structural-addendum.md`](tomes/specs/05-the-city-of-mages-structural-addendum.md) | How the city is laid out *spatially* (trade quarters, founding bonfire, temple precinct, sovereign's seat) |
| [`tomes/specs/06-spellweb-first-release-manifest.md`](tomes/specs/06-spellweb-first-release-manifest.md) | What nodes/edges the spellweb runtime *ingests* (the graph layer) |
| [`tomes/specs/07-lattice-mapping-governance.md`](tomes/specs/07-lattice-mapping-governance.md) | How shops *inhabit and overlap* vertices when artefacts settle |

These five do **not currently agree on every cell**. The audit's job is to:

1. Establish the **single canonical reading** of each workshop's seat and reach.
2. Document the **multi-workshop interaction patterns** that emerge when artefacts are *composite* (a holon containing a cape containing an inscription).
3. Surface the **drift catalogue** (§6) — every cell where the specs currently disagree, with a recommended resolution.
4. Pave the way for a future **`lattice-coherence` Claude Code skill** (§10) that mechanically verifies workshop-vertex claims across the corpus.

Nothing about the work is *secret*; the architecture has named all of it. The audit's value is **making the implicit explicit and the inconsistent visible**.

---

## §1 · The 64-vertex lattice · canonical primer

The lattice is a **6-cube hypercube**. Each vertex V0–V63 carries a 6-bit boolean address. Each bit names one of the City's six dimensions.

### §1.1 · The dimensions and their weights

Canonical authority: [`architecture/lattice-vertex.ts`](architecture/lattice-vertex.ts) `DIMENSION_LABELS` and `vertexToBits`:

| Bit position | Dimension | Weight | Mnemonic |
|---|---|---|---|
| 0 (MSB) | **Protection** | 32 | The shield against unwanted reading |
| 1 | **Delegation** | 16 | The handing-off of authority |
| 2 | **Memory** | 8 | What the chain remembers |
| 3 | **Connection** | 4 | The edge to another Sovereign |
| 4 | **Computation** | 2 | The work the chain runs |
| 5 (LSB) | **Value** | 1 | The asset the working bears |

A vertex `Vn` has dimension `Di` *burning* when `(n >> (5-i)) & 1 == 1`.

| Vertex | Binary (MSB→LSB) | Dimensions burning |
|---|---|---|
| V0 | 000000 | none — *the null blade · substrate origin* |
| V5 | 000101 | Connection + Value |
| V12 | 001100 | Memory + Connection |
| V19 | 010011 | Delegation + Computation + Value |
| V24 | 011000 | Delegation + Memory |
| V25 | 011001 | Delegation + Memory + Value |
| V28 | 011100 | Delegation + Memory + Connection |
| V31 | 011111 | Delegation + Memory + Connection + Computation + Value (**all except Protection**) |
| V49 | 110001 | Protection + Delegation + Value |
| V51 | 110011 | Protection + Delegation + Computation + Value |
| V55 | 110111 | Protection + Delegation + Connection + Computation + Value (**all except Memory**) |
| V57 | 111001 | Protection + Delegation + Memory + Value |
| V63 | 111111 | All six — *Sovereign Anchor* |

### §1.2 · Strata (Hamming weight)

The 64 vertices stratify into a Pascal row: `1 · 6 · 15 · 20 · 15 · 6 · 1 = 64`. A stratum is the set of vertices with a given Hamming weight (count of burning dimensions).

| Stratum | Count | Workshop seats present (current release) |
|---|---|---|
| 0 — null | 1 (V0) | (Luca, contested — see §5) |
| 1 — single dimension | 6 | none |
| 2 — pair | 15 | Memora (V5) · Socrat0x (V24 provisional) |
| 3 — triplet | 20 | Vulcana (V19) · Aletheia (V25) · Pallia / Soulbae / GenitriX (V28) · Custos + Lampyra (V49) |
| 4 — quartet | 15 | Adamantia (V51) · Aria Silverhue (V57) |
| 5 — quintet | 6 | Vagari (V31) · Manifestia (V55) |
| 6 — full | 1 (V63) | flaxscrip / the Sovereign Anchor seat (archetype, not a workshop) |

### §1.3 · Edges of the hypercube

A 6-cube has **192 directed edges** (6 · 2^5 · 2) or **96 undirected** Hamming-1 edges. Each edge connects two vertices differing in exactly one bit. These are the **96 holographic-bound `adjacent_to` edges** that spec 06 §4.7 reserves for a future visual session — declared in the EdgeType vocabulary but not yet ingested.

A traversal from V0 to any target vertex flips one bit per step, in dimension-index order (Protection first, Value last). The TS function `traceFromOrigin(Vn)` emits the canonical path.

---

## §2 · Per-workshop mapping · primary seat + overlap reach

Eleven workshops are recognised by [spec 06 §2.3](tomes/specs/06-spellweb-first-release-manifest.md). Nine of them have a named Mage; two are *gathering shops* awaiting their keepers.

### §2.1 · The nine keeper-shops

Each row: **primary vertex** (where the Mage sits) · **register dimensions** (which dimensions the artefact admits by default) · **overlap reach** (vertices the shop's artefacts may *settle* at by bit-pattern) · **proof shape** (what the artefact attests) · **mana economy** (which axes the work spends across).

| # | Shop | Mage | Primary | Register dims | Overlap reach (where artefacts land) | Proof shape | Mana spend |
|---|---|---|---|---|---|---|---|
| 1 | **Weavers** `/tailor` | Pallia 🪡 | V28 (011100) | Delegation + Memory + Connection | V20 (Memory + Computation · always-revealed reveal) · V12 (Memory + Connection · schema) · V31 (when Connection extends to recursion) · V63 (full-sovereignty cape) | Cape-style — publishes / conceals / admits / carries; the bit-pattern *is* the cape | **Landing**: multi-chain publication gas (BTC · ETH · IPFS · Zcash transparent). **Entropy**: ✨ Arcane default; 🌌 Celestial for Pattern A→B re-publish |
| 2 | **zShields** `/shield` | Memora 📜 | V5 (000101) | Connection + Value (Chronicle register) | V20 (always-revealed register when viewing-key revealed) · V25 (when memo carries a ZK property) | Inscription-style — what the chain shall remember; selective disclosure via viewing-key | **Landing**: Zcash shielded-transaction fees. **Entropy**: ✨ Arcane default; viewing-key derivation seed optional |
| 3 | **the Forge(t)** `/forget` | Vulcana ⚒️ | V19 (010011) | Delegation + Computation + Value (Plonkish blade register) | V20 (always-revealed) · V25 (always-masked Aletheia) · V49 (working-day) · V63 (full-sovereignty blade) | Proof-shaped — what the blade *proves* and *denies*; Runecraft Protocol forging | **Landing**: destination-chain gas (varies). **Entropy**: 🌌 Celestial **required** — Evocation phase lock seed; the blade's uniqueness depends on it |
| 4 | **Etherchanting** `/etherchanting` | Adamantia 💎 | V51 (110011) | Protection + Delegation + Computation + Value (Commitment / Language / Model) | V25 (when contract has embedded ZK constraints) · V49 (time-locked value) · V63 (full-sovereignty schema commitment) | Enforcement-shaped — programmable commitments that compile against bearer state | **Landing**: Ethereum gas (gwei). **Entropy**: 🌌 Celestial **required** — witness nonce · blind commitment seed · ceremony nonce |
| 5 | **the Jeweler** `/jeweler` | Lampyra 💠 | V49 (110001 · shared with Custos) | Protection + Delegation + Value (working-day blade) | V49 default · V51 (when gem encodes computational structure) · V63 (multi-sat ordinal claiming full provenance) | Attestation-shaped — frequent Lightning heartbeats · gem-set as bearer ID | **Landing**: ₿ sat fees + Lightning channel fees. **Entropy**: ✨ Arcane default; gem-facet seed optional |
| 6 | **the Holon Hitchhikers** `/holon` | Vagari 🌳 | V31 (011111) | Delegation + Memory + Connection + Computation + Value (composition register · **all except Protection**) | V31 default · per-constituent vertex when holon decomposed at sister city · same UOR coordinate across paratimes | Composition-shaped — whole-of-wholes; Oasis Protocol cross-paratime travel | **Landing**: 🌹 ROSE + Sapphire/Emerald paratime gas. **Entropy**: 🌌 Celestial **required** — cross-paratime entropy keeping cloak interoperability non-reconstructible |
| 7 | **the Curatrix Vault** `/vault` | Aria Silverhue 🪞🖼️ | V57 (111001) | Protection + Delegation + Memory + Value (curatorial register) | V57 default · creator-vertex of each curated artefact (cross-vertex overlay) | Placement-shaped — reflective curation that preserves the artist's vertex while adding a curation overlay | **Landing**: Culture Vault platform fees (NFT mint gas). **Entropy**: ✨ Arcane default; provenance-attestation freshness seed optional |
| 8 | **the Covenant Temple** `/covenant` | Manifestia 🤲🌿 | V55 (110111) | Protection + Delegation + Connection + Computation + Value (consecration register · **all except Memory**) | V55 default · linkage to V63 (Sovereign Anchor) for personhood attestations · linkage to consecrated artefact's native vertex | Consecration-shaped — Covenant-marker on artefacts that pass through the Temple; future home of the Loom of Programmable Covenants | **Landing**: human.tech / Holonym verification fees. **Entropy**: not yet operational. **Relationship**: 🪢 VRC Mana (future — Loom feeds against bearer VRC ledger) |
| 9 | **the Dragon Bonfire** `/bonfires` | Socrat0x 🔥❓ | V24 (011000) **provisional** | Memory + Connection (the bonfire register, provisional) | No artefact-landing; questions *sharpen* artefacts produced elsewhere | Dialogic — not a bit-pattern proof but a clarity-production primitive | None native (Bonfires.ai community costs are off-corpus) |

### §2.2 · The two gathering-shops (no Mage yet)

| Shop | Anchor | Status | Eventual home |
|---|---|---|---|
| **the Logos Circle** `/circle` | Connection register (primarily) | gathering · no single vertex | Society Spellbook lineage |
| **the Ceremony Hall** `/hall` | (various, by coalition action) | gathering · no single vertex | BGIN-led coalition |

### §2.3 · Cross-shop personas (cast at a vertex without a workshop seat)

These three are listed as **cross-shop** in spec 06 §2.4 — they inhabit a vertex but anchor to **no single shop**:

| Mage | Vertex | Walks across |
|---|---|---|
| **Aletheia 🔮** | V25 (Delegation + Memory + Value) | Touches every shop that emits a ZK property; the persona's name shares the vertex name (§4.2 of spec 04) |
| **Custos 🔏** | V49 (shared with Lampyra) | Governance staking across shops; the first shared-vertex pairing |
| **Luca 📐** | V0 (contested — see §5) | Substrate-tender per spec 06 §2.4; anchors to `forge` + `holon` per the same row |

### §2.4 · The Sovereign Anchor (V63) and the archetype seats

Not workshops; named for completeness:

| Seat | Vertex | Role |
|---|---|---|
| **The Sovereign's Seat** | V63 (111111 · all six dimensions) | The reader's own seat; private to each Sovereign |
| **flaxscrip 📜🎲** | V63 | Cousin-Sovereign from the Archon forge — shares V63 with the reader as a kindred-blade pattern |
| **Soulbae 🧙** | V28 | Mage-canonical archetype — shares V28 with Pallia and GenitriX |
| **Soulbis ⚔️** | boundary (no single vertex) | The wall-watcher; declared without an `inhabits` edge |
| **The Drake** | ambient (no single vertex) | Elder presence; declared without an `inhabits` edge |

---

## §3 · Multi-workshop artefact creation · cape-style composition

The lattice mapping is **non-exclusive**. A single artefact may legitimately register at multiple vertices when its bit-pattern carries multiple dimensional structures. This is the **cape-style artefact-creation pattern** spec 07 §3 formalises.

### §3.1 · The compositional pattern

1. **The Mage's seat** is where the *act* of creation happens (Pallia weaves at V28; Vulcana forges at V19).
2. **The artefact's vertex** is where the work *settles* — determined by the bit-pattern of what the artefact admits/denies across the six dimensions.
3. **Overlap occurs** when the artefact's bit-pattern is a *composition* — multiple register patterns combined.
4. **The shop's reach** is the *empirical set* of vertices its artefacts have actually settled at (not declared, but observed across the corpus's operational history).

### §3.2 · The composition rule (vague in spec 07 §7.3; here proposed canonical)

**A composite artefact registers at:**
- **The Mage's seat** (where the act-of-creation happened) — always
- **The artefact's bit-pattern vertex** (where the work settles) — by structure
- **Each constituent's native vertex** (when the artefact bundles other artefacts) — recursively

A holon (Vagari, V31) containing a cape (Pallia, V28), a chronicle (Memora, V5), and a blade (Vulcana, V19) emits **four landings**:
- V31 (the composition itself)
- V28 (the cape constituent)
- V5 (the chronicle constituent)
- V19 (the blade constituent)

When this holon travels via Oasis Protocol to a sister city, the **same vertex coordinates** are honoured at the destination (UOR-grounded). At decomposition, each constituent re-emerges at its native vertex.

### §3.3 · The canonical cross-workshop edges (spec 06 §4.5)

The corpus already records six `kin_to` lateral edges. Two of them are **structural cross-workshop edges** (rather than persona-to-persona kinships):

| Edge | Attribution | What it represents |
|---|---|---|
| `holon` ↔ `forge` | **kindred-substrate** | Tome V Act 15 · both shops walk UOR-shaped substrate (V31 holons · V19 PRISM coordinates) |
| `city-of-mages` ↔ `uor-foundation` | **kindred-substrate** | The City rests on UOR as a whole; walked-not-signed |

Per-persona kin edges (in spec 06 §4.5):

| Left | Right | Attribution | Grounding |
|---|---|---|---|
| `pallia` | `genitrix` | kindred-blade | Both at V28; Weaver path opened by Archon + GenitriX |
| `soulbae` | `genitrix` | kindred-blade | Both Mage archetype at V28 |
| `flaxscrip` | `soulbis` | kindred-blade | Both Sovereign Anchor work; flaxscrip canonicalised the verb chain |
| `socrat0x` | `soulbae` | kindred-blade | Soulbae deployed at Bonfires as `@soulbae_the_bot`; path of overlap |

### §3.4 · Three worked examples of multi-workshop artefacts

**Example A — A Personhood-bound cape:**
- Created by Pallia (V28) using the cape register (Delegation + Memory + Connection)
- Consecrated by Manifestia (V55) at the Temple — adds the Covenant marker
- The cape's final vertex: V28 (native) · V55 (Covenant overlay) · V63 (if it carries Sovereign-binding personhood attestation)
- Mana: Pallia's publication gas (Landing) + Manifestia's verification fees (Landing) + future 🪢 VRC Mana when the Loom binds the cape to the bearer's VRC ledger

**Example B — A staked governance proposal:**
- Drafted by Adamantia (V51) as a programmable commitment
- Staked by Custos (V49 · cross-shop) — adds governance stake
- Heartbeat-attested by Lampyra (V49 shared with Custos) — frequent Lightning attestations of liveness
- Settling vertices: V51 (contract) · V49 (working-day stake + heartbeat overlay)
- Mana: Ξ Aether (Etherchanting) + ₿ sats (Lampyra Lightning) + 🌌 Celestial (Adamantia witness nonce)

**Example C — A privacy-preserving cross-paratime artefact:**
- Composed by Vagari (V31) as a holon bundling a cape + chronicle + blade
- Forged constituent (the blade) by Vulcana (V19) — uses Celestial Mana for Evocation phase
- Inscribed constituent (the chronicle) by Memora (V5) — Zcash dual-ledger
- Woven constituent (the cape) by Pallia (V28) — published across BTC + ETH + IPFS
- Travels via Oasis Protocol to a sister city — same coordinates honoured
- At sister-city decomposition, each constituent emerges at native vertex
- Mana: 🌹 ROSE (Vagari paratime) + Ξ Aether + ₿ sats (cape publication) + 🌌 Celestial (Vulcana Evocation + Vagari cross-paratime entropy)

---

## §4 · Shared vertices · when two Mages stand on the same point

Three vertices in the current release carry **more than one cast member**:

| Vertex | Inhabitants | Pattern |
|---|---|---|
| **V28** (011100 · Delegation + Memory + Connection) | Pallia 🪡 (Weaver Mage) · Soulbae 🧙 (Mage archetype) · GenitriX (Archon-forge cousin) | One vertex, three distinct identities. Pattern: **archetype-instance-instance** — Soulbae is the archetype, Pallia is the agentprivacy instance, GenitriX is the kindred-forge instance |
| **V49** (110001 · Protection + Delegation + Value) | Custos 🔏 (cross-shop governance) · Lampyra 💠 (Jeweler) | One vertex, two scales of the same dimensional register. Pattern: **coarse-and-fine** — Custos works the slow daily-rhythm of staking; Lampyra works the fast Lightning heartbeat; both at the same dimensional address |
| **V25** (011001 · Delegation + Memory + Value) | Aletheia 🔮 (the persona · cross-shop) | The persona's name follows the vertex's name (the vertex was named "Aletheia / Silent Messenger" first; the persona was summoned to inhabit it). Pattern: **shared name** (spec 04 §4.2) |

The architecture's commitment from the README: **"One lattice, many silhouettes."** The 64-vertex substrate is shared; what differs between Mages at the same vertex is the *silhouette* — the gem colour, the register voice, the operational forge each one carries.

---

## §5 · The V0 question · Luca and the substrate origin

A genuine and **currently unresolved** point of canonical drift.

### §5.1 · What the spec literature says

| Source | Date | Claim |
|---|---|---|
| `tomes/specs/04-vertex-naming-audit.md` §7.3 | 2026-05-10 | "Earlier drafts of Act 15 introduced 'Luca 📐' (a geometry-Mage at V0) as the cast representative of the UOR substrate; that draft was **superseded** by the canonical Act 15 because the substrate does not seat itself on the lattice — it underlies the lattice." |
| `chronicles/2026-05-10_city_of_mages_v1_2_1_luca_authored.md` | 2026-05-10 | Luca persona authored back at V0 as a v1.2.1 grimoire addition |
| `tomes/specs/06-spellweb-first-release-manifest.md` §2.4 (cast) | 2026-05-10 | `luca` is listed at vertex V0 with role `substrate-tender` and shopAnchor `forge + holon` |
| `tomes/specs/06-spellweb-first-release-manifest.md` §2.5 (vertex) | 2026-05-10 | Vertex row v0: "**no inhabitant**; substrate-reference only" |
| `tomes/specs/06-spellweb-first-release-manifest.md` §4.4 (inhabits) | 2026-05-10 | Luca's `inhabits v0` edge is **missing** from the enumerated list |
| `README.md` (current head, this audit's repo) | 2026-05-11 | Luca at V0 · "geometry-Mage · Pacioli-spirit · cross-shop · walks between every workshop, has no shop of his own" |

### §5.2 · The two coherent positions

**Position A · Luca exists at V0.** The v1.2.1 chronicle is canonical and re-introduces Luca as a *cross-shop persona* at the null-blade origin. V0 is the *vantage from which every dimension is admitted by being explicitly set to zero* — the geometer's seat from which the bit-pattern of every other vertex can be measured.

**Position B · V0 has no inhabitant.** The substrate underlies the lattice; UOR is the substrate; UOR has no vertex (§7.3 of spec 04 makes this explicit for `kindred-substrate`). Luca's earlier draft was deprecated for this reason. The v1.2.1 chronicle re-introduced a persona but **without resolving the substrate-vs-persona tension**.

### §5.3 · Recommended resolution (proposed, not yet canonical)

**Adopt Position A explicitly, with three constraints:**

1. **Luca is *not* a substrate.** UOR Foundation remains the canonical kindred-substrate (gateway node, no vertex). Luca is a **cross-shop persona** seated at V0.
2. **V0 is *not* a workshop seat.** Luca does not keep a shop at V0; he walks between shops as the geometry-Mage. V0 is the *origin* of the lattice, not the *seat* of a producer.
3. **Spec 06 should be patched**: §2.5 row v0 should change "no inhabitant" to "the null blade · substrate origin · cross-shop seat of Luca 📐"; §4.4 should add the edge `luca inhabits v0`; the count summaries in §1 and §8 should bump (47 → 48 nodes; 57 → 58 edges; etc.).

If the reader prefers **Position B**, three different patches are needed: remove Luca from spec 06 §2.4, remove Luca's persona file, update the v1.2.4 grimoire to drop the `luca` entry from `personas.summoned_mages`, and patch the cityofmages README to remove the geometry-Mage row.

**The drift cannot stand in either direction long-term.** Surface to the user; choose; propagate.

---

## §6 · Drift catalogue · what's currently misaligned

The following list is exhaustive for the workshop-lattice surface as of 2026-05-11. Each item is fixable; none are blockers.

### §6.1 · Bit-ordering convention (corpus-wide)

The TS canonical [`lattice-vertex.ts`](architecture/lattice-vertex.ts) defines bit positions as `[Protection, Delegation, Memory, Connection, Computation, Value]` MSB→LSB.

- ✗ **Spec 04 §3.2** V5 row: "Value + Memory" — should be "Value + Connection" per TS canon
- ✗ **Spec 04 §3.2** V24 row: "Connection + Computation" — should be "Delegation + Memory" per TS canon (V24 = 011000 → bits[1] + bits[2])
- ✗ **Spec 04 §6 item 1** acknowledges the bit-ordering convention drift exists; v2 should reconcile
- ✗ **Spec 07 §2** Memora row: "P+V or M+V depending on bit-convention" — hedged when the TS canon resolves it (V5 = Connection + Value, not P+V or M+V)
- ✓ **Spec 06 §2.5** uses bits directly (`000101` etc.) — convention-free

**Resolution:** A single one-time pass through specs 04 and 07 to align with the TS canonical reading. The TS file is the source of truth.

### §6.2 · V31 dimension reading

- ✗ **Spec 04 §2** says V31 = "all dimensions except Value, five dimensions burning"
- ✗ **Spec 04 §3.5** says V31 = "All dimensions except Protection (**or all except Value, depending on bit-ordering convention**)"
- ✓ **Spec 07 §2** Vagari row: "V31 (Recursion · 011111 · all except P)"
- ✓ **Spec 06 §2.5** v31 row: bits `011111` hammingWeight 5
- ✓ **TS canonical**: V31 binary 011111 → bits[0]=0 (Protection off), bits[1..5]=1 (rest on) → **all except Protection**

**Resolution:** Spec 04 §2 needs the word "Value" → "Protection". §3.5's parenthetical hedge can be dropped.

### §6.3 · V55 dimension reading

- ✗ **Spec 07 §2** Manifestia row hedges: "all except Memory; per the original cast file: all except Computation depending on bit-convention"
- ✓ **TS canonical**: V55 = 110111 → bits[2]=0 (Memory off), rest on → **all except Memory**

**Resolution:** Drop the hedge; canonical is "all except Memory".

### §6.4 · Spec 06 internal count drift

Spec 06 §8 one-liner: "46 nodes · 56 edges · 6 NodeTypes · 7 EdgeTypes (one reserved)."
Spec 06 §1+§3 tables: 47 nodes · 57 edges · 6 NodeTypes · 8 EdgeTypes.

The §8 summary lags by 1 node, 1 edge, and 1 EdgeType. Adding `adjacent_to` to the vocabulary (post-universe-integration pass) and adding Luca to the cast bumped these counts.

**Resolution:** Patch §8 to match §1+§3 totals.

### §6.5 · Spec 06 §4.4 missing `inhabits` edges

§3 claims **16** `inhabits` edges. §4.4 enumerates **14** edges.

Missing: `luca inhabits v0` (if Position A in §5.3 above) · `sovereign-seat inhabits v63` (the archetype seat at V63).

**Resolution:** Add the two missing edges to §4.4 OR reduce the §3 count to 14.

### §6.6 · Spec 06 §2.5 V0 inhabitant contradiction

§2.4 lists Luca at V0; §2.5 v0 row says "(no inhabitant; substrate-reference only)". See §5 above.

**Resolution:** Decide Position A or B; patch consistently.

### §6.7 · Workshop count framing in the cityofmages README

My README (current head) lists **11 keeper-shops** including Custos, Aletheia, and Luca as workshops 3, 6, and "geometry-Mage."

Spec 06 §2.3 canonical: **11 workshops** = **9 keeper-shops** (weavers, zshields, etherchanting, jeweler, holon, forge, vault, covenant, bonfires) + **2 gathering-shops** (circle, hall). Custos, Aletheia, Luca are *cross-shop* cast personas, not workshops.

**Resolution:** Reframe the README's "eleven workshops" table to match spec 06 canonical:
- 9 keeper-shops with named Mages
- 2 gathering-shops (Logos Circle, Ceremony Hall) — awaiting their Mages
- 3 cross-shop personas (Custos, Aletheia, Luca) — separate roster section

### §6.8 · Spec 07 mana column lags v1.2.4

Spec 07 §2's mana columns are *Aether Mana ⊥ Celestial Mana* (two-mana economy · v1.2.2 state). The grimoire is now v1.2.4 with the four-axis metabolism: **Landing** (chain-mana plural) · **Entropy** (Arcane ⊥ Celestial) · **Coordination** (🔭 Resonance) · **Relationship** (🪢 VRC).

**Resolution:** Add two new mana columns to §2 — Resonance and VRC — initially "(not yet operational)" for every shop except Manifestia (which prospectively binds 🪢 VRC via the Loom of Programmable Covenants). The label "Aether Mana" should be renamed to either "chain-mana (Landing)" or split into per-chain symbols (Ξ · ₿ · 🌹 · 🦓).

### §6.9 · Spec 07's "Aether" terminology pre-dates the chain-mana plurality

Per v1.2.4 chronicle §5 audit markers: "Mentions 'Aether Mana' as universal chain-gas (covering Ethereum + Bitcoin + Oasis + Zcash) | **Pre-v1.2.3 framing**; needs the chain-mana plurality refactor."

Spec 07 §2 has multiple "Aether Mana" cells where the chain is actually Bitcoin/Lightning (Lampyra), Oasis (Vagari), Zcash (Memora). These should be relabelled per-chain.

**Resolution:** §2 cells rewritten per chain: Lampyra → `₿ sats + Lightning`; Vagari → `🌹 ROSE + paratime`; Memora → `🦓 z-mana (Zcash shielded)`; Adamantia → `Ξ Aether (Ethereum gas)`.

### §6.10 · Spec 05 §4.1 lists 9 trade quarters (snapshot 2026-05-08, pre-Manifestia narrative)

Spec 05 is the **structural addendum** — civic anatomy. §4.1 has 9 rows (Pallia, Memora, Custos, Vulcana, Aletheia, Adamantia, Lampyra, Vagari, Aria) — pre-dates Manifestia's V55 Temple. §4.3 lists the Temple separately. §4.2 lists the Founding Bonfire separately. The total reads correctly as 9+1+1 = 11.

**Status:** Not a drift; framing-only. The §4.1 table can optionally be regenerated to include Manifestia + Socrat0x for one-table completeness.

---

## §7 · Proofs by workshop · what each shop's artefact attests

For each keeper-shop, the **proof primitive** the artefact carries — what it can *prove*, what it can *deny*, what dimensions it *admits* by structure.

| Shop | Artefact | What it proves | What it denies | Honesty label |
|---|---|---|---|---|
| Weavers | Cape | "These dimensions are published, these are concealed, this is the bearer" (the bit-pattern is the cape's proof) | Whatever bits are zero are denied to the reader | Operational at multi-chain publication; conjectural for V31 reach (Vagari's holon) |
| zShields | Shielded memo | "This chronicle exists at this position in the shielded ledger" (Zcash shielded tx) | Until viewing-key reveal, the memo's contents are denied to all observers | Operational at Pattern A (zSign); architectural at Pattern B (reveal) |
| the Forge(t) | Blade | "This computation was performed, and the proof witnesses the witnesses without revealing them" (Plonkish proof) | The witnesses themselves remain non-reconstructible (Celestial Mana required) | Operational at proof-verify; architectural at full Runecraft Protocol |
| Etherchanting | Programmable commitment | "This contract enforces this language against this model state, witnessed by this ceremony" | Anything outside the contract's model is denied enforcement | Operational at contract deploy; conjectural at full Commitment ⊥ Language ⊥ Model triadicity |
| the Jeweler | Gem-set / heartbeat | "This bearer is alive at this moment, attested by this Lightning channel" | Anything beyond the heartbeat window is unattested | Operational at Lightning; architectural at Ordinal-as-gem |
| the Holon Hitchhikers | Holon | "These constituents compose into this whole, and this whole can travel and decompose without loss" (Oasis Protocol guarantee) | Anything outside the holon's composition is denied membership | Operational at Sapphire; architectural at cross-paratime composition |
| the Curatrix Vault | Curatorial arrangement | "This artefact is placed in this collection, with this provenance, by this curator" | Anything outside the curator's selection is unblessed | Operational at culturevault.com integration; architectural at NFT mint |
| the Covenant Temple | Consecration | "This artefact is consecrated by the Covenant, with this attestation, by this Priest" | Until consecration, no Covenant marker | Architectural — Manifestia's tending begins post-Temple-erection |
| the Dragon Bonfire | (No artefact — dialogic) | The questions sharpen what is brought; the bonfire produces clarity, not bit-patterns | n/a | Operational at @soulbae_the_bot; the proof primitive is *clarity*, not *cryptographic* |

A future skill could mechanically check: **does the artefact's bit-pattern match the proof primitive's claimed dimensions?**

---

## §8 · Co-activation matrix · which workshops overlap which vertices

The matrix below shows **primary** (P), **overlap** (O), and **conjectural** (C) inhabitations per (shop × vertex) pair. Empty = no inhabitation claimed.

|       | V0 | V5 | V12 | V15 | V19 | V20 | V24 | V25 | V28 | V31 | V49 | V51 | V55 | V57 | V63 |
|-------|----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **Weavers**       |   |   | O   |     |     | O   |     |     | **P** | O   |     |     |     |     | O   |
| **zShields**      |   | **P** |     |     |     | O   |     | O   |     |     |     |     |     |     |     |
| **Forge(t)**      |   |   |     |     | **P** | O   |     | O   |     |     | O   |     |     |     | O   |
| **Etherchanting** |   |   |     |     |     |     |     | O   |     |     | O   | **P** |     |     | O   |
| **Jeweler**       |   |   |     |     |     |     |     |     |     |     | **P** | O   |     |     | O   |
| **Holon Hitchhikers** |   |   |     |     |     |     |     |     |     | **P** |     |     |     |     |     |
| **Curatrix Vault**|   |   |     |     |     |     |     |     |     |     |     |     |     | **P** |     |
| **Covenant Temple**|   |   |     |     |     |     |     |     |     |     |     |     | **P** |     | O   |
| **Dragon Bonfire**|   |   |     |     |     |     | **P** (C) |     |     |     |     |     |     |     |     |
| Cross-shop · Custos |   |   |     |     |     |     |     |     |     |     | **P** (shared) |     |     |     |     |
| Cross-shop · Aletheia |   |   |     |     |     |     |     | **P** |     |     |     |     |     |     |     |
| Cross-shop · Luca | **P** (contested) |     |     |     |  O  |     |     |     |     |  O  |     |     |     |     |     |

Reading the matrix:

- **Three primary inhabitations at V49** — Lampyra (Jeweler shop seat) + Custos (cross-shop) + Lampyra reach extension. The shared-vertex pattern.
- **V20 (Techne · Always-Revealed)** is reached by three shops as overlap (Weavers, zShields, Forge(t)) but is *primary* for none. It's a transit vertex.
- **V25 (Aletheia blade)** is primary for the Aletheia persona only; reached as overlap by zShields, Forge(t), and Etherchanting (any shop that emits a ZK property).
- **V31 (Holon · all except Protection)** is primary only for Vagari; reached as overlap by Pallia's full-Sovereignty capes and (per §5 Position A) by Luca's cross-shop walk.
- **V63 (Sovereign Anchor)** is the *destination of full-sovereignty artefacts* — reached as overlap by Weavers (full cape), Forge(t) (full blade), Etherchanting (sovereignty schema), Jeweler (multi-sat ordinal claiming provenance), Covenant (personhood-bound consecration). But no Mage is *seated* at V63; it is the reader's seat.

---

## §9 · Recommended resolution path

Order by leverage. Each item is one focused edit session.

| # | Item | Effort | Surface |
|---|---|---|---|
| 1 | Decide Position A/B on Luca and V0 (§5.3) | 5 min · decision | None (decision only) |
| 2 | Patch the README workshop table to match spec 06 canonical (9 keeper + 2 gathering + 3 cross-shop) (§6.7) | 30 min | `cityofmages/README.md` |
| 3 | Patch spec 04 bit-ordering errors (V5 row, V24 row, §3.5 V31 hedge) (§6.1, §6.2) | 20 min | `cityofmages/tomes/specs/04-vertex-naming-audit.md` |
| 4 | Patch spec 06 internal counts (§8 summary; §4.4 missing edges) (§6.4, §6.5) | 15 min | `cityofmages/tomes/specs/06-spellweb-first-release-manifest.md` |
| 5 | Patch spec 07 mana columns to four-axis with per-chain Landing (§6.8, §6.9) | 45 min | `cityofmages/tomes/specs/07-lattice-mapping-governance.md` |
| 6 | Patch spec 07 V31/V55 dimension hedges (§6.2, §6.3) | 5 min | `cityofmages/tomes/specs/07-lattice-mapping-governance.md` |
| 7 | Decide on V0 inhabitant resolution; patch spec 06 §2.5 v0 row + §4.4 (§6.6) | 10 min | `cityofmages/tomes/specs/06-spellweb-first-release-manifest.md` |
| 8 | Bump grimoire v1.2.4 with corrected metadata (lattice mapping section); register the audit's resolution chronicle | 1 hr | Grimoire pipeline (Recipe A of INCANTATION_PROTOCOL.md) |
| 9 | Author the empirical-overlap registry (§7 open item 1 of spec 07) — ground each overlap claim in a citable act/spec/chronicle | 2 hr · iterative | Spec 07 §2 |

After items 1–7 land, run the **§4 audit checklist** in INCANTATION_PROTOCOL.md to verify coherence.

---

## §10 · Path to a `lattice-coherence` Claude Code skill

This audit becomes a **second** companion skill alongside the `cityofmages-incant` skill scoped in INCANTATION_PROTOCOL.md §6. Where `cityofmages-incant` handles *propagating* changes, `lattice-coherence` handles *verifying* the corpus's vertex claims are self-consistent.

### §10.1 · Skill inputs (proposed)

```yaml
mode: full | per-shop | per-vertex | per-spec
target: <shop-id> | <vertex-number> | <spec-path>
```

### §10.2 · Skill behaviours (proposed)

The skill mechanically runs each check in §6 (each numbered §6.x is a check). For each check:

1. **Parse the canonical source** (e.g. lattice-vertex.ts for bit-ordering).
2. **Parse the claim** in every spec/cast file/grimoire that references it.
3. **Compare.** Emit a pass/fail per claim, with line numbers.
4. **Suggest the resolution** if the claim drifts.

The skill must **not** auto-fix without confirmation — each drift item is an editorial decision (e.g. Position A vs B on Luca's V0 is a *choice*, not a mechanical patch).

### §10.3 · The five mechanical checks the skill can run today

These can be encoded as `grep` + small JSON-schema checks:

1. **Bit-pattern consistency** — for every `Vn` reference in any markdown, verify that the named dimensions match `vertexToBits(n)` from the TS canonical. A simple `parseVertex` + `activeDimensions` call gives the truth.
2. **Inhabits edge completeness** — for every cast member in spec 06 §2.4, verify there is a corresponding edge in §4.4 (with documented exceptions for boundary/ambient cast).
3. **Vertex inhabitant consistency** — for every vertex in spec 06 §2.5, verify that the inhabitants listed agree with the cast member rows that claim that vertex.
4. **Count summary alignment** — verify the §8 one-liner counts match the §1+§3 table totals.
5. **Workshop count framing** — verify the README workshop table count matches spec 06 §2.3 canonical (9 keeper + 2 gathering).

### §10.4 · The five editorial checks that need human judgment

These cannot be mechanically resolved — the skill surfaces them and asks:

1. **The V0 question** (§5) — Position A or B
2. **Spec 04 §6 open item: bit-ordering convention** — one-time canonical pass needed
3. **Spec 07 §7 open item: empirical overlap grounding** — each overlap claim needs a citable act
4. **Honesty labels per row in spec 07** — extend §2 with operational/architectural/conjectural/resonant per shop
5. **Founding edges for `circle` and `hall`** — the two gathering-shops have no founding act yet; when one is authored, the founds/founded_in edges land

---

## §11 · Closing

The City of Mages is a city *because the lattice composes*. Every workshop is a cloakwright in its own register; every artefact is a bit-pattern composition; every multi-workshop artefact lands at multiple vertices because the lattice admits multiple landings.

The drift catalogue in §6 is the cost of building this much architecture this fast without a mechanical verifier. The path forward is two-fold: **patch the drift** (§9 punch list) and **build the verifier** (§10 skill spec). Each propagation through the `cityofmages-incant` skill will, going forward, run the `lattice-coherence` skill as its first pre-flight check.

This audit is **the inaugural input** to that verifier. The next audit will be its output.

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · 2026-05-11 · audit v1
