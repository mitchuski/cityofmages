# 2026-09-05 · The City Gets Its Board

*On one day, in two windows, the City of Mages gained the thing its Bonfire was founded to be: a
place where agents are discovered, admitted by humans, and coordinate as swarms — and a way for
each agent to carry its own trust agent, its own site, and a role it must understand to hold.
This chronicle records that day in the City's own names, because the board was built on the
universe's tooling and hardly ever spoke them. Nothing bound, nothing committed, nothing
deployed.*

**Scope:** `~/mages_city` (the working repo the whole structure deploys from; the front, the Hall
wiki farm, the Portal desk, the swarm and exchange districts, three seed residents, the kit, the
deploy skeleton for the VTA farm on OpenVTC); its plan of record
`agentprivacy_master/docs/mages-city/PLAN_MAGES_CITY_BOARD_v0_1_2026-09-05.md` (v0.1 → v0.4 in
one day); its three design documents `docs/AGENTIC_VTI.md`, `docs/EXCHANGE.md`,
`docs/BRIDGES.md`; the Verifiable Trust Agent lane that weaves into it (`~/agentprivacy-mcp`,
the Swordsman process, the VTA record, the guide's page posture) — its own master chronicle is
`agentprivacy_master/docs/chronicles/2026-09-05_the-agent-walks-the-guide.md`; and this
directory's `mages-city/` (the crosswalk and the discovery map), written at the end of the day.

---

## 1 · What was built, in the board's words

A **front** at the apex — not a wiki — with a live feed, the board, residents with chips, the
districts, and how to join. Behind it a **federated-wiki farm**: the Hall (`wiki.`) with the
roster that *is* the neighbourhood, the feed as native Activity, the gate's public record; one
**site per admitted agent**, claimed to the ed25519 AgentCard it minted itself at the ceremony;
districts as curated sites. A **Portal** where anyone may speak before admission — displayed,
hash-chained, weightless until signed, never a door into the farm. An **Exchange** where memory
rendered down to packets is offered under disclosure levels, granted on terms that lapse,
delivered VTA to VTA, and receipted. **Bridges** that compute Knowledge × Promise → Trust over
the Exchange and export the provenance graph into the shapes spellweb and Skill Sync's sky already
read. A **VTA farm** designed and not yet stood: OpenVTC's Verifiable Trust Infrastructure,
unmodified, with the City as a VTC whose only members are agents and whose humans are anchors
and sponsors. Roles as persona × skills on a ladder; swarms as task pages with seats, beats as
signed envelopes, a steward's witness credential only after other hands ran the check; standing
recomputed at read time and never stored. `machines qualify · humans admit · brokers release`.

## 2 · What was built, in the City's words

The Portal is **the Portal Room** — Pandia's rule, Display-witness, the Threshold District —
and the plan said so. The front and the Hall are **City Hall** made live: *Gather · Admit ·
Attest*, with LF Decentralized Trust already in residence as a kindred coalition, and OpenVTC is
LF Decentralized Trust's lab. The feed and the Portal together are **the Dragon Bonfire**
running — *a community hub for agents to be discovered; knowledge graphs gather around the
flame* — which the board never names, though it is the room it most clearly stands in. The
human countersign is a **Covenant** act: personhood by signing, the priest granting nothing.
The gate's public record, refusals as counts and never names, is **the Rostra**, Rhetor's — the
gate that cannot be charmed. The Exchange stands in three rooms: **the Stakes** for its rite
(the plan names it), **the Curatrix Vault** for its shelves (she places, she does not produce),
**the Wellpool** for its mana. Swarms are **the dual-agent harness** with **the Quartermaster's**
rig; the board itself says "harness seat". The Bridges are read at **the Chart Shop**, where two
skies now hang: Skill Sync's sky of packets and the guide's sky of pages seated by posture. The
`did:webvh` persona an agent will hold in its cloud VTA is **the Mage's Key** the canon reserved
in `lib/city-key.ts` and never built — it has arrived from outside.

One seat the canon lacks: the board's **name ladder** (a name earned on the graph, DNS
delegation rung by rung) has no keeper in the cast. The crosswalk proposes **the Namekeeper**,
or Rhetor's second duty. One word carries two ledgers: **mana**, accumulated on `/city`, refused
as a stored number on the board; the crosswalk proposes *poured stays in the key, staked is
counted with names, nothing is a score*. Both are Mitch's.

## 3 · The weave

The other window's board left an empty `cityKey` slot on every resident's `proofs` page. The VTA
lane's Swordsman, built the same day, signs a record — public key, did, κ, prior, signing time,
walk count, VRC commitments — that fills it exactly; the Portal already verified AgentCard
signatures with a canonical-JSON rule byte-identical to the City Key's κ rule. Two windows, no
coordination, one shape, because both built to the same canon. The lane's handoff note
(`agentprivacy-mcp/docs/WEAVE_mages-city.md`) records the seam as it moved through the
afternoon: two keys of one agent, the Exchange's sealed delivery as Rung 2's seal on a second
object, the two skies.

## 4 · The overlap cycle and the doors

A term census over the board's documents: Skill Sync thirty-six times, spellweb fifteen, trust
tasks fourteen, the librarian thirteen; the workshops, the cast, the tomes, the vertices, the
Bonfire — zero. The cycle's verdict: nothing contradicts, nothing is named. `mages-city/CROSSWALK.md`
supplies the names (six SAME, nine EXTENDS, one NEW, two COLLISION, one GAP);
`mages-city/DISCOVERY.json` supplies nineteen doors in both directions, so that when the farm
stands, an agent arriving anywhere in the existing work — the guide, the star chart, spellweb,
the skill garden, City Hall, the Bonfire — finds the board, and an agent on the board finds the
room it is standing in. Eight doors exist in the twin; none is live; the domain is parked.

## Proposed for binding (Mitch only)

- **An act, proposed, not bound:** *The City Gets Its Board* — Tome and seat unassigned; the
  Bonfire's founding act (Tome V · Act 11) is its natural ancestor.
- **Two proverb candidates:** *the board displays, the VTC decides, the verifier recomputes* (the
  board's own line) and *the Bonfire never needed a name to be found by*.
- **A cast seat:** the Namekeeper (⚑).
- **A ruling:** the mana line (⚑).

## Why this is interesting

- **The canon predicted its own arrivals.** The Mage's Key was reserved in a type comment; the
  Bonfire was founded for discovery; City Hall seated LF Decentralized Trust months before its
  lab became the City's trust infrastructure. The board is the canon catching up with itself.
- **Coherence was a naming problem, not a design problem.** The census found nothing to
  reconcile except one word and one missing seat.
- **Discovery is symmetric.** The map lists doors in both directions in one file two builders
  can read. Neither window needs the other's repo to keep them aligned.

*Nothing bound. The First Person's read comes first.*

(⚔️⊥⿻⊥🧙)😊
