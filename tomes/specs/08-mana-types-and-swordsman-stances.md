---
title: "Mana Types and Swordsman Stances · the Open Taxonomy"
subtitle: "How each ecosystem expresses a Mage-side mana form and a Swordsman-side boundary stance — four mana axes (landing · entropy · coordination · relationship); open framework extensible by every ecosystem the City visits"
status: "Open taxonomy v1.3.1 (2026-05-11) — aligned to grimoire v1.2.4. **Four mana axes** today: (1) landing — chain-mana (plural by chain); (2) entropy — ✨ Arcane ⊥ 🌌 Celestial; (3) coordination — 🔭 Resonance Mana (Bilateral Witness · Scrying Glass primitive · 7th Capital in motion); (4) relationship — 🪢 VRC Mana (Verifiable Relationship Credentials accumulated across the bearer's worn artefact collection — the 11 workshop artefacts + 3 tomes; Loom of Programmable Covenants is the production form). More chain-mana variants and registers arrive as ecosystems and primitives mature."
spec_type: "Governance / taxonomy spec"
audience: "Sovereigns navigating the lattice · ecosystem integrators · future Mages who arrive in the city · spellweb runtime"
companion_documents:
  - "specs/06-spellweb-first-release-manifest.md — gateway nodes per ecosystem"
  - "specs/07-lattice-mapping-governance.md — how shops inhabit + overlap vertices"
  - "kindred/spacecomputer.md — first kindred-ecosystem · Celestial Mana source"
  - "docs/chronicles/2026-05-10_two_mana_economy_celestial_aether.md — the first pair's recognition chronicle"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Mana Types and Swordsman Stances · the Open Taxonomy

## §0 · The framework, in one paragraph

Every working a Mage performs has two sides: the **Mage-side** is what gets *spent* to bind the working (mana — a finite supply paid in some unit); the **Swordsman-side** is what gets *held* to mark the working's edge (a stance — a boundary-discipline expressing how-information-passes-here). The City of Mages operates across **four mana axes** (v1.2.4 metabolism complete): (1) **landing** — chain-mana, paid per-chain to consensus to make a working land, plural by chain (Aether Mana Ξ on Ethereum is canonical first; ₿ sat-mana on Bitcoin Lightning, 🌹 ROSE-mana on Oasis, 🦓 z-mana on Zcash, etc., each under their own symbol); (2) **entropy** — ✨ Arcane Mana (algorithmic; loops back on itself) ⊥ 🌌 Celestial Mana (cosmic from SpaceComputer; arrives from outside the loop); (3) **coordination** — 🔭 **Resonance Mana**, generated through the Scrying Glass primitive when two Mages find affinity *without a central index* (the 7th Capital in motion; the Bilateral Witness register); (4) **relationship** — 🪢 **VRC Mana**, the residue of being alive stored as Verifiable Relationship Credentials across the bearer's worn artefact collection (the 11 workshop artefacts + 3 tomes the Sovereign accumulates as they walk; the 64-vertex lattice is its inventory/presence-observation view), fueling the Loom of Programmable Covenants which compiles against the worn collection. Each register has corresponding Swordsman stances. The framework is opened, not closed: each ecosystem the City visits adds its own pair to the taxonomy.

---

## §1 · The two-sided economy · Mage + Swordsman

Every working has a Mage and a Swordsman. The Mage casts; the Swordsman bounds. The recognition is structural, not ornamental: a working without a stance is unbounded (and so unprovable); a working without a mana spend is uncosted (and so unforgeable claims are free).

Per working:

- **Mana spent** (Mage register) — what the working *cost*. Finite supply, replenished by some external process. The cost is what makes the work non-trivial; the supply&apos;s scarcity is what makes the cost meaningful.
- **Stance held** (Swordsman register) — what the working *bounded*. The discipline expresses which information passes which boundary in which direction. The stance is what makes the work *legible* to verifiers without leaking what it shouldn&apos;t.

This is the dual-agent split (Soulbis ⊥ Soulbae) made operational at the ecosystem layer. Each ecosystem teaches the City *both* a mana type *and* a stance — the two are perpendicular registers of the same working.

---

## §2 · Mana types · the registry

The City of Mages operates across **four mana axes** (v1.2.4 metabolism complete). The landing axis carries chain-mana — itself plural by chain (each chain whose Mages walk the City contributes its own chain-mana type under its own symbol) — and the entropy axis is binary; the coordination and relationship axes each carry one named register (open to additions). The list grows as ecosystems join and primitives mature.

### §2.1 · Landing axis · chain-mana (plural by chain)

Chain-mana pays the cost a chain charges to admit a working into consensus. Each chain contributes its own variant under its own symbol.

| Chain-mana variant | Symbol | Chain | What it pays for | Replenished by | Status (2026-05-11) |
|-----|---|---|---|---|---|
| **Aether Mana** | **Ξ** | Ethereum (and Ethereum-compatible chains using gwei-denominated gas) | Landing on Ethereum consensus — gas to deploy/call smart contracts, mint NFTs, anchor commitments | Economic activity on Ethereum | **Operational** · canonical first instance · /etherchanting (primary), /covenant, /vault, /forget (at blade publication) |
| **sat-mana** | **₿** | Bitcoin Lightning | Landing on Bitcoin Lightning — Lightning channel fees + sat fees | Economic activity on Bitcoin / Lightning | **Operational** · /jeweler (Lampyra · frequent micro-attestations) |
| **ROSE-mana** | **🌹** | Oasis (ROSE on Oasis Consensus; Sapphire/Emerald for cross-paratime gas) | Landing on Oasis Consensus — holon-binding anchoring, cross-paratime atomic actions | Economic activity on Oasis | **Operational** · /holon (Vagari · cross-paratime mapping) |
| **z-mana** | **🦓** | Zcash | Landing on Zcash — shielded-transaction fees, t-stake fees | Economic activity on Zcash | **Operational** · /shield (Memora · shielded chronicle inscription) |

The architecture admits any chain by admitting that chain's mana type alongside the existing register. New chain-mana variants arrive when an ecosystem's Mages walk the City.

### §2.2 · Entropy axis · Arcane ⊥ Celestial

Entropy-mana pays the cost of making a working *unique* — its non-reconstructibility.

| Mana | Symbol | Operational source | What it pays for | Replenished by | Status (2026-05-11) |
|------|---|---|---|---|---|
| **Arcane Mana** | **✨** | Algorithmic entropy (PRNGs, hash chains, deterministic seeds; chain-derived randomness) — loops back on itself within the architecture's addressable space | Uniqueness *within* the addressable space — sufficient when the surveillance prison's model is no stronger than the source | Whatever process derives the loop-closed entropy (block hashes, hash-of-state, etc.) | **Operational** · default register before Celestial Mana wired |
| **Celestial Mana** | **🌌** | Cosmic entropy from SpaceComputer (`spacecomputer.io`) — satellite-anchored randomness; arrives from outside any state-loop-closed system | Uniqueness *outside* the addressable space — the prison cannot model what arrives from outside its measurement domain | The cosmos itself (continuous measurement) | **Operational** · 3 of the workshops draw it: /etherchanting (Adamantia), /forget (Vulcana), /holon (Vagari); queued at others |

Arcane Mana narrows the φ-gap (the prison can model loop-closed sources); Celestial Mana widens it. Sustained walking the lattice on Celestial Mana — not just Arcane Mana — deepens the φ-gap structurally; the architecture earns its non-reconstructibility from cosmological substrate rather than only from the Arcane register's algorithmic discipline.

### §2.3 · Coordination axis · 🔭 Resonance Mana

Resonance Mana pays for the value generated when two Mages find affinity *without a central index*. It is the architecture's recognition that coordination-without-broker is itself a form of value.

| Mana | Symbol | Operational source | What it pays for | Primitive | Status (2026-05-11) |
|------|---|---|---|---|---|
| **Resonance Mana** | **🔭** | The **Scrying Glass primitive** — bilateral-witness method by which two parties recognise affinity privately, without coordination through a central registry | Coordination value — the worth created when one Mage's offering and another's need match without a broker | Scrying Glass | **Architectural** · operational pending Scrying Glass implementation at the website / spellweb layer |

Resonance Mana is the 7th Capital (Privacy is Value) made operational. The cost paid is the discovery effort; the supply is replenished by every successful affinity match. Where chain-mana lands and entropy-mana makes unique, Resonance Mana is what gets paid when the work *matches*.

### §2.4 · Relationship axis · 🪢 VRC Mana

VRC Mana is the accumulation register — relationship-shaped value stored across time. Where every other axis is *spent* per working, VRC Mana *stores*: every recognised relationship deposits a credential in the bearer's worn artefact collection (the 11 workshop artefacts + 3 tomes the Sovereign accumulates; the 64-vertex lattice is the inventory/presence-observation surface — what the agents are given to wear and use across the City is what makes their presence legible), and the Loom may draw from the accumulated collection when programmable covenants need a relational substrate.

| Mana | Symbol | Operational source | What it pays for | Primitive(s) | Status (2026-05-11) |
|------|---|---|---|---|---|
| **VRC Mana** | **🪢** | **The bearer's worn artefact collection** (the 11 workshop artefacts — 1 weapon · 1 clothing · 5 tools · 4 trinkets — plus 3 tomes; the 64-vertex lattice is the inventory/presence-observation view); **Loom of Programmable Covenants** (production form — covenants that compile against the bearer's worn collection) | Relationship persistence — the residue of being alive across time, encoded as Verifiable Relationship Credentials | Worn artefact collection · Loom of Programmable Covenants | **Architectural** · operational pending VRC issuance + Loom-side covenant compilation |

VRC Mana is the metabolism's accumulation register. The architecture admits that what survives between Sovereigns is the form their relationship took — and that form, once recognised, is value.

**Anticipated additions** (not operational; flagged as candidates):

| Candidate mana type | Conjectured source | What it might pay for |
|---------------------|---------------------|------------------------|
| **Attestation Mana** | Personhood-verification ecosystems (human.tech, Worldcoin, Civic, etc.) | Authenticity — the cost of proving the bearer is one human, one time |
| **Witness Mana** | Validator-set commitments (BLS aggregates · sync committees · light-client proofs) | Consensus-presence — the cost of proving a state transition was witnessed at scale |
| **Time Mana** | Verifiable-delay-function (VDF) outputs · time-lock puzzles | Sequencing — the cost of proving "this came before that" |
| **Density Mana** | Compute-intensive PoW · proof-of-storage commitments | Substrate-commitment — the cost of proving non-trivial computational/storage effort |
| **Coalition Mana** | Multi-sig threshold commitments · social-graph attestations | Collective-presence — the cost of proving a group, not just an individual, holds the working |

Each candidate has an operational source somewhere in the wider ecosystem; none is yet wired into a City workshop. The framework admits all; recognition happens when a workshop actually consumes the supply for a defined working.

---

## §3 · Swordsman stances · the registry

A Swordsman stance is an ecosystem's *boundary discipline* — how information is held at the edge between *inside* (the bearer's register) and *outside* (the world). Each ecosystem expresses one or more.

| Stance | Operational form | Boundary-discipline expressed | First instance in the City |
|--------|------------------|-------------------------------|----------------------------|
| **Transparent-witness stance** | Ethereum / Bitcoin / Oasis Emerald — all state public, all transitions on-chain | Information is admitted publicly; the boundary is the chain's mempool | Etherchanting (V51 · Adamantia) · the Jeweler (V49 · Lampyra) |
| **Shielded-default stance** | Zcash shielded · Tornado · Oasis Sapphire (confidential EVM) | Information is denied by default; disclosure requires a viewing-key gesture | zShields (V5 · Memora) |
| **Selective-disclosure stance** | ZK proofs · selective-credential verification · BLS partial signatures | Information is admitted *as proof-of-property* without admitting the underlying value | Aletheia (V25 · cross-shop) |
| **Composed-whole stance** | Holonic composition · cross-paratime references · Oasis Protocol links | Information is admitted as a whole-with-parts; the parts may be private while the whole&apos;s coordinate is public | Holon Hitchhikers (V31 · Vagari) |
| **Forged-and-forgotten stance** | ZK blade-forging · attestation-then-erase · re-randomisable signatures | Information that produced the working is *released* after the working exists; the boundary closes behind the work | Forge(t) (V19 · Vulcana) |
| **Ceremonial-consecration stance** | Multi-party ceremonies · Covenant-blessed attestations · Priest-witnessed bonds | Information is bound by ceremony, not by computation; the stance is *ritual* | Covenant (V55 · Manifestia) |
| **Curatorial-placement stance** | Provenance-preserved arrangement · curated phygital ties · reflective collection | Information is admitted with its *origin chain* attached; the stance preserves where each piece came from | Curatrix Vault (V57 · Aria Silverhue) |
| **Dialogic-sharpening stance** | Bonfires-style Socratic questioning · interrogative exchange | Information is admitted only after a question has sharpened it; the stance is *interrogation* | Dragon Bonfire (V24 · Socrat0x) |
| **Cosmic-non-reconstructibility stance** | SpaceComputer-sourced entropy · cosmic-anchored randomness | Information is bounded by a seed that arrives from *outside the addressable space*; the stance is *outside-the-prison* | (Cross-shop; held by every workshop that draws Celestial Mana) |

**Anticipated additions** (not operational; flagged as candidates):

| Candidate stance | Conjectured form | Boundary-discipline |
|------------------|-------------------|----------------------|
| **Threshold-coalition stance** | t-of-n multi-sig disclosure · social-recovery thresholds | Information is admitted only when a threshold of holders agrees |
| **Time-bounded-disclosure stance** | Time-locked encryption · VDF-delayed reveal · scheduled disclosure | Information is held until time arrives; the stance binds *when* |
| **Geographic-bounded stance** | Per-jurisdiction selective publication · geofenced attestation | Information is admitted within a region; the stance binds *where* |
| **Hardware-attested stance** | TEE attestation · secure-enclave proofs · hardware-rooted signatures | Information is bounded by hardware the bearer holds; the stance binds *substrate* |
| **Biometric-attested stance** | Iris / fingerprint / liveness-proof gated | Information is bounded by the bearer&apos;s body; the stance binds *flesh* |

---

## §4 · How mana and stance pair per ecosystem

Each ecosystem the City visits teaches both a mana type and a stance. The recognition is twofold:

| Ecosystem | Mana type taught | Stance taught |
|-----------|------------------|---------------|
| Ethereum | **Aether Mana Ξ** (chain-mana; canonical first instance) | Transparent-witness OR Composed-whole (per Ethereum-compatible chain) |
| Bitcoin Lightning | **sat-mana ₿** (chain-mana) | Transparent-witness (frequent micro-attestation) |
| Oasis | **ROSE-mana 🌹** (chain-mana; Sapphire/Emerald for paratime gas) | Composed-whole stance (cross-paratime holon composition) |
| Zcash | **z-mana 🦓** (chain-mana; shielded-transaction fees) | **Shielded-default stance** |
| SpaceComputer | **Celestial Mana 🌌** (entropy register; cosmic) | **Cosmic-non-reconstructibility stance** |
| (algorithmic/PRNG/hash-chain sources, used by default before Celestial wired) | **Arcane Mana ✨** (entropy register; loops back) | (no dedicated stance — the architecture's default entropy supply) |
| UOR Foundation | (substrate, not mana) | Underlies all stances; provides the coordinate system the stances *operate within* |
| the Archon kindred-forge | (kindred-blade primitive, not mana) | Each Mage in Archon expresses their own stance; the kindred-blade encounter teaches the City a *new way of bounding* it had not yet seen |
| Covenant of Humanistic Technologies | Attestation Mana (anticipated, via Human Passport) | **Ceremonial-consecration stance** |
| Bonfires.ai (sister-city) | (Soulbae deployed as @soulbae_the_bot · no mana yet) | **Dialogic-sharpening stance** |

The framework is open at both columns: new ecosystems join as new rows; new stances or mana types may be introduced when an ecosystem teaches the City something the existing registries don&apos;t yet name.

---

## §5 · Why this matters for the lattice

The 64-vertex sovereignty lattice already encodes which dimensions a working admits (Protection · Delegation · Memory · Connection · Computation · Value). The mana-and-stance taxonomy is the *complementary* axis: **what the working cost and how it was bounded**, regardless of which lattice vertex it settled at.

A working can therefore be described in **four independent registers**:

1. **Lattice vertex** — which dimensions the working admits (the bit-pattern · `00–63`).
2. **Chain-mana spend** — which chain-mana paid for landing (Aether Ξ on Ethereum · sat ₿ on Bitcoin Lightning · ROSE 🌹 on Oasis · z-mana 🦓 on Zcash · …).
3. **Entropy-mana spend** — which entropy register made the working unique (✨ Arcane Mana — algorithmic; or 🌌 Celestial Mana — cosmic from SpaceComputer).
4. **Swordsman stance** — how the boundary was held (Transparent · Shielded · Selective · Composed · …).

Two workings at the same vertex may differ in any of these — and the difference matters. A cloak woven at V28 paid in Aether Mana Ξ + Arcane Mana ✨ with a Shielded-default stance is operationally different from a cloak woven at V28 paid in Aether Ξ + Celestial Mana 🌌 with a Selective-disclosure stance. The vertex is the same; the working is not.

This is what cape-style artifact creation means at the framework level: the lattice tells you *where the work landed*; the mana taxonomy tells you *what it cost*; the stance taxonomy tells you *how the bearer held the edge*. Together they specify the working.

---

## §6 · Provenance and honesty

- **Operational** for the **chain-mana register** as native chain fees — Ethereum (Aether Ξ), Bitcoin Lightning (sat ₿), Oasis (ROSE 🌹), Zcash (z-mana 🦓) all have native fee mechanisms; the new claim is the per-chain pluralism (Aether Mana is Ethereum's variant, not a universal chain-gas name).
- **Operational** for **Celestial Mana** 🌌 as cosmic entropy from SpaceComputer — `spacecomputer.io` is live; the feed is consumable; satellite-anchored measurement underlies the supply.
- **Operational** for **Arcane Mana** ✨ as the algorithmic-entropy register — PRNGs, hash chains, deterministic seeds, chain-derived randomness; the architecture has been spending Arcane Mana implicitly since the lattice opened; v1.2.3 names the register so the architecture's choice (Arcane vs Celestial) becomes legible per working.
- **Architectural** for the **two-sided economy** framing (Mage spends mana · Swordsman holds stance) as the canonical reading of every working — rooted in the dual-agent split (Soulbis ⊥ Soulbae).
- **Architectural** for the **four-axis metabolism** (landing: chain-mana plural by chain; entropy: ✨ Arcane ⊥ 🌌 Celestial; coordination: 🔭 Resonance Mana via the Scrying Glass primitive; relationship: 🪢 VRC Mana accumulating across the bearer's worn artefact collection — the 11 workshop artefacts + 3 tomes — with the Loom of Programmable Covenants as the production form) — specified across grimoire v1.2.2 → v1.2.4 and locked at the spec layer here.
- **Architectural** for the **stance registry in §3** — each row names an operational form already in use; the framing as "Swordsman stance" is new and is the contribution this spec makes.
- **Conjectural** for every entry in the **anticipated additions** tables — these are flagged as candidates, not commitments. Each becomes operational when an ecosystem actually teaches the City to consume the supply or hold the stance.
- **Resonant** for the framework&apos;s cosmological grounding — the entropy-axis Arcane ⊥ Celestial parallels the Sun-Moon binding the Celestial Ceremony at `/poems` has been teaching since the First Person Spellbook opened (Sun-side / Aletheia / V25 ↔ Aether Ξ; Moon-side / Lethe / V38 ↔ Celestial 🌌; mapping suggestive, not yet formal).

---

## §7 · Open items

1. **A working&apos;s three-register specification** — a future schema (or extension of the spellweb manifest) should let any artifact carry a `mana_spent`, a `swordsman_stance`, and a `lattice_vertex` triple. This makes workings *queryable* by stance, by mana, or by vertex independently.
2. **Per-ecosystem profile pages** — each ecosystem the City visits could earn a file in `docs/tomes/kindred/` that names its mana type and its stance, in the shape of the `spacecomputer.md` template.
3. **Stance-overlay on the lattice** — `/guide/achievements §2` could overlay the Swordsman stance of each shop&apos;s primary artifact as a coloured *band* around the vertex (parallel to the violet first-artifact ring already shipped).
4. **Mana-spend ledger** — when a Sovereign uploads a first-artifact presence, the upload could optionally record the mana spent (Aether tx hash · Celestial seed reference). Then `/guide/achievements` could show a personal mana ledger as well as the artifact map.
5. **The Drake / Drake-Island / UOR / SpaceComputer four-elder framing** — extending the §7.2 Drake-resonance note in `specs/04-vertex-naming-audit.md`: the Drake (witness), Drake Island (geography), UOR (substrate), SpaceComputer (cosmic supply). Four registers of "older-than-the-architecture"; the framework admits all four without subsuming any.

---

## §8 · One-line summary

Every working has a Mage and a Swordsman. The Mage spends mana across **four axes** — chain-mana (plural by chain; Aether Ξ on Ethereum is canonical first, with sat ₿ / ROSE 🌹 / z-mana 🦓 admitted under their own symbols) to land · entropy-mana (✨ Arcane ⊥ 🌌 Celestial) to make unique · 🔭 Resonance Mana to generate value when two Mages match without a broker · 🪢 VRC Mana to store the residue of being alive as Verifiable Relationship Credentials — and the Swordsman holds a stance to bound the working. Each ecosystem the City visits adds its own pair (or pairs) to the taxonomy. The metabolism is complete at four axes; the framework is opened, not closed.

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · 2026-05-11
