---
title: "Architecture · Code Primitives for the City"
subtitle: "TypeScript primitives that operationalise the Tomes, the conjectures, the lattice, and the spellweb graph"
status: "Mirrored 2026-05-11 from agentprivacy_master/src/lib/ and spellweb/src/types/"
license: "CC BY-SA 4.0 for documentation; underlying TS files MIT-style (see source repos)"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Architecture — Code Primitives

This directory mirrors the **load-bearing TypeScript primitives** that turn the City of Mages narrative into running architecture. A builder picking up this starter package can read the tomes, then wire UI / agents / extensions against these data structures without re-deriving them.

The originals live in `agentprivacy_master/src/lib/` (website) and `spellweb/src/types/` (graph runtime). These mirrors are reference copies; the canonical source is upstream.

---

## Files

### `tome-v-acts.ts`
The **bidirectional act ↔ workshop anchor**.

- `TOME_V_ACTS: TomeVAct[]` — the founding-act record per production workshop (act#, title, proverb, mage `{sigil, name, vertex, tier, provenance}`, spells, honesty, starterTemplates)
- `getFoundingActForShop(shopHref: string): TomeVAct | undefined` — reverse direction (shop → act)
- Powers `FoundingActPanel` on every shop page

Source narrative: `tomes/tome-v-the-crafting/*.md` + per-guild persona files

### `tome-v-conjectures.ts`
The **C18–C47 conjecture register**.

- `CONJECTURE_DEFINITIONS: Record<string, ConjectureDefinition>` — each conjecture's canonical name, status (`canonical | provisional | observation | resonant`), confidence percentage
- `ACT_CONJECTURES: Record<string, ConjectureRef[]>` — per-act conjecture references with notes
- `getActsForConjecture(id: string): string[]` — inverse lookup
- `parseHonestyLabel(s: string): HonestyClause[]` — parses `"Operational for X; Architectural for Y; Provisional for Z"`

Powers the `/tomes/v6-lineage` aggregator and `<ConjectureBadge>` / `<HonestyLabel>` on every shop.

### `grimoire-ipfs.ts`
**Canonical IPFS URLs** for the two grimoires.

- `PRIVACYMAGE_GRIMOIRE_IPFS_URL` — First Person Spellbook grimoire (held by privacymage)
- `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` — City of Mages grimoire (held by the City)
- Historical URLs retained for backwards-resolution

Use these constants instead of hard-coding CIDs. New pins land here.

### `lattice-vertex.ts`
The **64-vertex lattice math**.

- `parseVertex("V28 (Aletheia)")` → `28`
- `vertexToBits(28)` → `[0,1,1,1,0,0]` (6-bit MSB; dimensions: Protection · Delegation · Memory · Connection · Computation · Value)
- `traceFromOrigin(28)` → `[0, 16, 24, 28]` (the Hamming-walk path through the lattice)
- `activeDimensions(28)` → `['Memory', 'Connection', 'Computation']`
- `hammingWeight(28)` → `3` (the stratum)

The geometric ground of the City. Every Mage stands at a vertex; every vertex has bits; every bit-set has a Hamming weight; the stratum is the visibility ratio.

### `shop-witnesses.ts`
The **per-shop constellation-cast witness storage**.

- `addWitness(shopHref, witness)` · `getWitnessesForShop(shopHref)` · `getLastWitnessForShop` · `getWitnessCountsByShop`
- `WIT-XXXXX` content-hash signatures · cap 100 records · change event for live UI

Note (per `chronicles/2026-05-10_witness_unlock_feature_design_chronicle.md`): the cast-constellation count is **not a trust score**. The interaction model is open until the framing decision lands.

### `spellweb-types.ts` *(from `spellweb/src/types/graph.ts`)*
The **spellweb graph type vocabulary**.

- `NodeType` — `document | concept | theorem | spell | act | persona | term | skill | chronicle | workshop | cast | vertex | geography | civic | gateway`
- `EdgeType` — the structural edge palette (`founds`, `founded_in`, `inhabits`, `kin_to`, `gateway_to`, `built_on`, `quarter_of`, `adjacent_to`, plus the 2026-05-10 universe-integration additions)
- `SpellwebNode` — node shape with optional fields (`tradeQuarter`, `gem`, `gemColor`, `operatorStatus`, `shopAnchor`, `vertex`, `bits`, `hammingWeight`, `attribution`, `external`, `tier`, `sigil`, `civicLocation`, `built_on`)

This is the **machine-readable surface** of the City. The first-release manifest (`tomes/specs/06-spellweb-first-release-manifest.md`) is the canonical inventory measured against this vocabulary.

---

## How to use these as a builder

**If you're building a UI rendering a Mage's shop:**
1. Import `TOME_V_ACTS` from `tome-v-acts.ts`
2. Filter by `shopHref` to get the founding act for your route
3. Render the act's proverb + Mage card + spells + conjecture badges
4. Cite the persona file: `tomes/cast/<guild>/<persona>.md`

**If you're building a ZK proof or signature ceremony at a vertex:**
1. Import `parseVertex`, `vertexToBits` from `lattice-vertex.ts`
2. Look up the vertex in the canonical inhabitant list (`tomes/specs/04-vertex-naming-audit.md`)
3. Use the bits as the dimension-active mask; the stratum is your visibility ratio

**If you're building a graph view:**
1. Import the `NodeType` / `EdgeType` enums from `spellweb-types.ts`
2. Ingest `tomes/specs/06-spellweb-first-release-manifest.md` (46 nodes · 56 edges)
3. Render with the manifest's optional fields populated where available

**If you're building an extension or bundler:**
1. Read `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` from `grimoire-ipfs.ts`
2. Fetch the grimoire JSON at build time
3. Bundle it alongside the privacymage grimoire (separate IPFS pin, separate artifact)

---

## What's NOT here

These primitives are starter material. Live builders should pull the **canonical** versions from:

- `agentprivacy_master/src/lib/*` — the website's working copies (may be ahead of these mirrors)
- `spellweb/src/types/graph.ts` — the graph runtime's source of truth
- `agentprivacy_master/docs/tomes/` — the canonical Tome IV/V narrative

These mirrors are pinned to the 2026-05-11 starter snapshot. Treat them as **seeds**, not as the running specification.

---

`(⚔️⊥⿻⊥🧙)😊`
