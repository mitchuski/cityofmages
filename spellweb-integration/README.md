---
title: "Spellweb Integration · the City on the Knowledge Graph"
subtitle: "How the universe maps onto the spellweb's typed-node graph"
status: "Mirrored 2026-05-11 from spellweb/"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Spellweb Integration

This directory holds the **canonical record of how the City of Mages renders as a graph** on the spellweb knowledge runtime, plus the audit methodology that keeps the graph coherent against the master corpus.

The spellweb (`https://spellweb.ai`) is a separate runtime; this is the City's interface to it.

---

## Files

### [`CHRONICLE_UNIVERSE_INTEGRATION_2026-05-10.md`](CHRONICLE_UNIVERSE_INTEGRATION_2026-05-10.md)
The chronicle of the day the universe arrived on the spellweb. Three passes:
1. **Universe integration** — 67 new nodes + ~95 new edges; six new `NodeType` values; eight new `EdgeType` values; thirteen new optional fields on `SpellwebNode`
2. **Audit against spec 06** — +1 archetype (the-Drake), +15 conjectures (C18–C47), +9 document nodes, +~65 wiring edges, drift fixes
3. **Luca lineage retcon** — Luca rewritten as the Pacioli of First Person Spellbook Act 1 returning to the City as the geometry-Mage at V0

### [`AUDIT_METHODOLOGY.md`](AUDIT_METHODOLOGY.md)
How to keep the spellweb's graph canonical against the master corpus. The methodology a future audit session should follow when the corpus moves and the spellweb needs to catch up.

---

## The four-domain universe on the graph

```
Tome           ChronicleNode at ring_position vertex
                 + civic_location (Tome V acts)
                 + v6_lineage[] + honesty
                 + shop_anchor (reverse direction)

Workshop       CivicNode at the resident Mage's vertex
                 + resident_mage ref · founding_act ref
                 + trade_quarter · operator_status
                 + LiveConstellationNode slot

Cast           Node typed by tier (archetype/cousin/summoned/companion/priest)
                 + sigil · vertex · shop_anchor · spells · source_material

Vertex         VertexNode (64 total · 13 inhabited · 51 open)
                 + bits · hamming_weight · canonical_name · attribution chain

Drake Island   GeographyLayer underneath the lattice
                 the_drake plural: whisperer · place · fire · elder

City of Mages  CivicOverlay on top of geography + lattice
                 trade_quarters · founding_bonfire · temple_precinct
                 sovereigns_seat (V63) · street_plan (lattice)
                 walls (the "you" voice) · sister_cities[]

Sister cities  GatewayNode at the city map's edge
                 cousin-blade-edge / kindred-substrate-edge / kindred-ecosystem-edge
```

---

## The edge palette (current)

| EdgeType     | Semantics                                                                  |
|--------------|----------------------------------------------------------------------------|
| `founds`     | act → workshop · "this narrative founds this shop"                         |
| `founded_in` | workshop → act · reverse direction                                         |
| `inhabits`   | persona → vertex · "this Mage stands at this position"                     |
| `kin_to`     | mutual lateral · cousin-blade · kindred-substrate · etc.                   |
| `gateway_to` | city → external partner · sister cities · upstream forges                  |
| `built_on`   | civic → geography · "the City is built on Drake Island"                    |
| `quarter_of` | workshop → city · "this shop is a trade quarter of the City of Mages"      |
| `adjacent_to`| reserved for the 96 holographic-bound lattice edges (future visual pass)   |

Source of truth: [`../architecture/spellweb-types.ts`](../architecture/spellweb-types.ts).

---

## The first-release manifest

Canonical inventory: [`../tomes/specs/06-spellweb-first-release-manifest.md`](../tomes/specs/06-spellweb-first-release-manifest.md)

**46 nodes · 56 edges · 6 NodeTypes · 7 EdgeTypes (one reserved).**

| NodeType    | Count | Notes                                                                  |
|-------------|------:|------------------------------------------------------------------------|
| `civic`     |     1 | The City of Mages                                                       |
| `geography` |     1 | Drake Island                                                            |
| `workshop`  |    11 | Live shops on `/runecraft`                                              |
| `cast`      |    16 | 3 archetypes + 2 cousins + 9 summoned + 1 companion + 1 priest         |
| `vertex`    |    13 | Inhabited vertices                                                      |
| `gateway`   |     4 | Archon · Bonfires · human.tech · UOR Foundation                        |

This release is the **first** ingest. v1.2.3 adds Luca (V0) and SpaceComputer as kindred ecosystem; the audit methodology document tells you how to land those into a v2 manifest.

---

## How to use this directory

**If you're standing up your own spellweb instance:**
1. Read `AUDIT_METHODOLOGY.md` first — it defines what "canonical" means
2. Ingest `tomes/specs/06-spellweb-first-release-manifest.md` against the vocabulary in `architecture/spellweb-types.ts`
3. Layer on Luca (V0) and SpaceComputer (kindred ecosystem) per the May 10–11 chronicles in `chronicles/`
4. Run the audit methodology against your graph; drift-fixes go back upstream

**If you're querying the spellweb for City of Mages content:**
- Filter by `NodeType` = `workshop` for the 11 trade quarters
- Filter by `NodeType` = `cast` for the 17 named personas (16 in v1.1 + Luca in v1.2.1)
- Filter by `NodeType` = `gateway` for the sister-city / cousin-forge / kindred-substrate / kindred-ecosystem connections
- Follow `quarter_of` from any workshop to reach the civic node

---

`(⚔️⊥⿻⊥🧙)😊`
