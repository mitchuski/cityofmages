# Chronicle: the Chart Shop · Pleione Named · V44 Assigned · Aquamarine Confirmed · Navigation District Opens

**Date:** 2026-05-14
**Status:** Selection chronicle · records the four editorial decisions that closed the Chart Shop's pre-canonical period: keeper · gem · vertex · district. Grimoire patch v1.6.0 still anticipated.
**Audience:** privacymage · @benohanlon (the Navigator) · the next agent picking up grimoire-patch authoring · downstream sister-repo authors
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion chronicles:**
- [`2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md`](2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md) · the inception episode (Telegram exchange, the original Chart House proposal, the §10½ Pelagia/Astrolabe addendum)
- [`2026-05-13_chronicle_the_chart_house_admitted_to_corpus_pelagia_named.md`](2026-05-13_chronicle_the_chart_house_admitted_to_corpus_pelagia_named.md) · the corpus-admission chronicle authored 2026-05-13 evening (Pelagia draft · subsequently retired in favour of Pleione)
- [`tomes/cast/charthouse/pleione.md`](../tomes/cast/charthouse/pleione.md) · Pleione's canonical cast file (V44 reading bound)
- [`tomes/cast/charthouse/pelagia.md`](../tomes/cast/charthouse/pelagia.md) · Pelagia's retired draft (preserved for provenance)
- [`tomes/workshops/charthouse/constellation.md`](../tomes/workshops/charthouse/constellation.md) · the Chart Shop workshop tome v2

---

## §0 · What this chronicle is

A *receipt* for the four editorial decisions privacymage made on 2026-05-14 that closed the Chart Shop's pre-canonical period:

1. **Keeper:** Pleione 🧭 (replaces the 2026-05-13 evening Pelagia draft)
2. **Gem:** Aquamarine (#5eead4 · sea-green at the water's edge)
3. **Vertex:** V44 (binary `101100` · Stratum 3 · Active: Protection + Memory + Connection · Dormant: Delegation + Computation + Value)
4. **District:** Navigation District (the Chart Shop is the first; the district name is provisional pending the spec 05 update)

Each decision was made deliberately. This chronicle records the *reasoning* so the architecture remains coherent against future editorial passes.

---

## §1 · Pleione · the keeper

**Decision:** Pleione (Πληιόνη · Greek · "the Sailing One").

**Considered alternatives:** Pelagia (πελάγια · "of the open sea"), Chartis (χάρτης · "chart-maker"), Astrolabos (ἀστρολάβος · "the star-taker"), and the kindred-citizen residency for @benohanlon.

**Reason for Pleione over alternatives:**

The Chart Shop's keeper needs to encode *both* the **sailing register** (the navigator at the open sea) AND the **constellation register** (the held star-pattern). The other candidates each carried one of these registers but not both:

| Candidate | Sailing register | Constellation register |
|---|---|---|
| Pelagia (πελάγια · of the open sea) | ✓ | ✗ |
| Chartis (χάρτης · chart-maker) | ✗ | ✓ (the chart records the constellations) |
| Astrolabos (the star-taker) | ✗ | ✓ (the instrument reads constellations) |
| **Pleione (Πληιόνη)** | **✓** (her name comes from *plein*, "to sail") | **✓** (in myth she is the mother of the Pleiades — the literal constellation by which ancient sailors timed their voyages) |

**Pleione binds both in one figure.** Her name's etymology is *sailing*; her mythological role is *mother of the constellation that sailors steer by*. The double-encoding is the load-bearing fit. The Chart Shop's bearer is herself a navigator carrying a still-forming constellation; Pleione is the elder navigator who has already made the crossing the bearer is about to attempt.

**Provenance discipline.** The Pelagia draft is retired but not deleted — preserved at `tomes/cast/charthouse/pelagia.md` with a RETIRED frontmatter notice for provenance. The Hold · Compare · Map architecture, the Φ-gap discipline, the Astrolabe artefact, and the three release-destinations are all carried forward unchanged from Pelagia's draft to Pleione's file. Only the figure changes; the workshop's discipline does not.

**The kindred-citizen residency for @benohanlon** remains held open as a structural-relationship category at v1.6.0. Pleione's keepership and Ben's potential residency are not in tension — they would coexist as keeper-and-citizen if the kindred-citizen category lands.

---

## §2 · Aquamarine · the gem

**Decision:** Aquamarine · `#5eead4` · sea-green at the water's edge.

**Considered alternatives:** Moonstone (constellation-light · ink-stays-wet image); Sapphire (the wine-dark sea); Labradorite (iridescent stone whose appearance shifts with the observer's angle).

**Reason for Aquamarine over alternatives:**

- **Etymology** — Latin *aqua marina* literally means "water of the sea." For a workshop at the water's edge keeping a navigator's harbour, the etymology is exact.
- **Palette distinction** — Sapphire (`#67e8f9`) is already Etherchanting's gem; reusing the cyan would collide. Aquamarine's `#5eead4` (Tailwind teal-300) sits cleanly distinct: paler, greener, more sea-water-with-light-on-it than sapphire's pure-cyan.
- **Visual association with Astrolabes** — historically, astrolabes used aquamarine cabochons for their alidade jewels (the rotating sighting arm needs a pivot stone that shows light through clearly).
- **Moonstone** would have been a strong second; held in reserve for a future Mage in the cosmological-witness tier (perhaps Selene-related) where the moon-light register is more central.
- **Labradorite** was structurally interesting (the "appearance shifts with observer angle" fits the constellation-superposition theme) but reads as more *quantum-uncertainty* than *sea-navigation*; held in reserve for a future workshop in that register.

---

## §3 · V44 · the vertex

**Decision:** V44 (binary `101100` · Stratum 3).

**Active dimensions** (per `architecture/lattice-vertex.ts`):

- **Protection** (b0 · weight 32) — the Φ-gap discipline; the workshop's defining structural primitive
- **Memory** (b2 · weight 8) — constellations persist across visits; "the ink stays wet" requires Memory as a primitive
- **Connection** (b3 · weight 4) — the distributed-cognition substrate (Ben's "fabric woven from many minds")

**Dormant dimensions:**

- **Delegation** (b1) — Pleione holds without binding; the bearer retains ownership
- **Computation** (b4) — the Astrolabe reads positions; nothing computes within the workshop
- **Value** (b5) — constellations are not goods; no monetary or scarcity claim

**Discovery path = the curriculum.** The trace from V0 to V44 is three bit-flips:

```
V0  (000000) — start
V8  (001000) — flip Memory · the Hold
V12 (001100) — flip Connection · the Compare
V44 (101100) — flip Protection · the Map
```

The bit-flip order **Memory → Connection → Protection** maps exactly to **Hold → Compare → Map**. A bearer who walks this trace learns the discipline in sequence: first she learns to *remember* (admit the constellation into suspension); then she learns to *connect* (read it across many minds via the Astrolabe); then she learns to *protect* (decide release-direction with the Φ-gap intact).

**Reasoned over alternatives:**

| Candidate | Active dimensions | Why not |
|---|---|---|
| **V36** (`100100`) | Protection + Connection only | Drops Memory. The whole point of "the ink stays wet" is that material persists *between* visits. Without Memory, the workshop holds material only within a single session. Misses the discipline. |
| **V40** (`101000`) | Protection + Memory only | Drops Connection. The constellation isn't woven from one mind; it's distributed across many. Without Connection, the workshop becomes a private journal, not a harbour. Misses the substrate. |
| **V46** (`101110`) | Protection + Memory + Connection + Computation | Adds Computation. The Astrolabe *reads* positions; nothing *computes*. Adding Computation makes the workshop active in a way that violates Pleione's discipline of attending without interpreting. |
| **A new Cartographic Axis** (non-vertex) | n/a | Considered. The proverb that guided the decision — *"the star that is named by the sailor becomes the fixed point for the entire fleet"* — is performative-affirmative: naming MAKES fixity. The proverb argues against hedging into axis-or-foam options. Vertex commitment is the proverb-faithful choice. |
| **Extrastructural · the Open Sea** (outside the lattice) | n/a | Considered. Strong narrative-architecture alignment with the inception story. Held in reserve for a future workshop class if the City admits "extrastructural workshops" as a category. |
| **The Φ-foam** (inter-vertex space) | n/a | Considered. Most architecturally distinctive but also most expensive and least proverb-faithful. |

V44 is the *unique 3-bit configuration* that captures the workshop's discipline without surplus or shortfall. V44 was unoccupied prior to this admission; no vertex sharing required.

**Provisional vs canonical.** The vertex assignment is provisional in the sense that the corpus may relocate Pleione if downstream usage reveals a better fit; it is canonical in the sense that all v1.6.0 wiring binds against V44.

---

## §4 · Navigation District · the spatial frame

**Decision:** the Chart Shop sits in the **Navigation District** of the City of Mages.

**Provisional status.** The Navigation District is a new spatial organisational layer above individual workshops. The earlier-today (2026-05-13) Threshold work introduced the **Threshold District** (one workshop with three rooms); the Chart Shop's admission introduces the Navigation District as a separate organisational layer (one workshop currently; potentially more as future navigator-class workshops join).

**What lives in the Navigation District.**

- The Chart Shop (V44 · this admission)
- Anticipated future shops in the navigation register, if any (held open · examples might include: a sextant-shop for celestial measurement; a periplus-shop for the genre of coastal-route texts; a tide-shop for temporal-rhythm reading — none committed)

**Spec implication.** `tomes/specs/05-the-city-of-mages-structural-addendum.md` will need a new section for "Districts" as the City's spatial organisational layer: trade-quarters (cardinal producer-shops), the temple precinct (V55 covenant), the founding bonfire (V19), the sovereign's seat (V0), the Threshold District (V59 three rooms), and the Navigation District (V44 · Chart Shop). District-naming is itself a structural choice; the spec update is anticipated for v1.6.0.

---

## §5 · What this chronicle does and does not bind

### Binds
- ✅ Pleione 🧭 as the canonical Chart Shop keeper; sigil 🧭 (compass)
- ✅ Aquamarine `#5eead4` as the Chart Shop's gem
- ✅ V44 (binary `101100` · Stratum 3) as Pleione's vertex
- ✅ Navigation District as the Chart Shop's spatial organisational frame
- ✅ Hold · Compare · Map as the workshop's ceremony grammar (working hypothesis; runecraft-protocol integration canonicalises)
- ✅ Hold-witness as Pleione's stance (attentional register · awaits Spec 08 v1.3.4 to formalise)
- ✅ The Astrolabe as the workshop's artefact (tool-class · seventh tool registered)
- ✅ The discovery path V0 → V8 → V12 → V44 as the bearer's curriculum

### Does NOT bind
- ❌ A grimoire patch (v1.6.0 anticipated · authoring is the next pass)
- ❌ A canonical conjecture number for the attentional-register hypothesis (proposed C63; awaits patch)
- ❌ A canonical anchor act (Tome V Act 17 vs Tome VI Act 2 · awaits patch)
- ❌ The kindred-citizen category for @benohanlon (deferred · admissible at the same v1.6.0 patch or later)
- ❌ Spellweb wiring (the spellweb's missing-shops gap, including shop-charthouse, is its own next-pass item)
- ❌ The Navigation District's spec section (anticipated for v1.6.0 spec 05 update)

---

## §6 · Files this chronicle accompanies

This chronicle is the *receipt*; the *operational artefacts* live elsewhere:

**CityofMages corpus:**
- `tomes/cast/charthouse/pleione.md` — Pleione's canonical cast file (V44 reading bound)
- `tomes/cast/charthouse/pelagia.md` — Pelagia's retired draft (preserved · RETIRED frontmatter notice)
- `tomes/workshops/charthouse/constellation.md` — workshop tome v2 (Pleione · V44 · Aquamarine · Navigation District in frontmatter)
- `chronicles/2026-05-13_chronicle_the_chart_house_inception_navigator_arrives.md` — inception (with §10½ Pleione/Astrolabe addendum)
- `chronicles/2026-05-13_chronicle_the_chart_house_admitted_to_corpus_pelagia_named.md` — corpus-admission (Pelagia draft · the Pleione rename in this chronicle supersedes)
- (this file) `chronicles/2026-05-14_chronicle_chart_shop_pleione_named_v44_assigned.md`

**Master agentprivacy:**
- `docs/tomes/charthouse/pleione.md` — mirror
- `docs/tomes/charthouse/pelagia.md` — mirror (retired draft)
- `docs/tomes/workshops/chart-house-living-scroll-v1.md` — mirror (constellation_id is `chart-shop-living-scroll-v1` in v2 frontmatter; filename retains the historical `chart-house` prefix until a future rename)
- `src/app/charthouse/page.tsx` — live route (Pleione · V44 · Aquamarine wired)
- `src/lib/cast-attachments.ts` — Pleione entry added (V44 · Hold-witness · attachmentKind A_workshop)
- `src/lib/first-artifacts.ts` — Astrolabe template added for `/charthouse`
- `src/lib/nav.ts` — label updated "chart house" → "chart shop"
- `src/components/runecraft/WorkshopFooter.tsx` — label updated
- `docs/chronicles/` — chronicle mirrors

---

## §7 · The proverb that guided the V44 decision

> *The star that is named by the sailor becomes the fixed point for the entire fleet.*

The proverb is performative-affirmative: naming MAKES fixity. The Chart Shop's keeper is the ELDER NAVIGATOR (Pleione, mother of the Pleiades) who has already done what the proverb describes. The vertex assignment to V44 is the act of naming-that-creates-fixity — privacymage as the City's sailor names the workshop; V44 becomes the fixed point for the corpus's fleet of downstream tooling.

The proverb closes Pleione's cast file. The proverb opened the V44 decision. The proverb is the link between the workshop's *function* (bearers naming constellations, those becoming fixed-for-fleet downstream) and the workshop's *position* (V44, fixed-for-fleet by this chronicle's binding).

The harbour has its coordinate. The fleet has a fixed point.

⚓️ 🧭 ✨

CC BY-SA 4.0 · privacymage · 2026-05-14
