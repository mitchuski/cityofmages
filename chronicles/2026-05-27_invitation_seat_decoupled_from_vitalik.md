# Chronicle: The Invitation Seat, Decoupled from Vitalik

**Date:** 2026-05-27
**Status:** Editorial decoupling · narrative + graph surfaces updated · grimoire patch pending
**Scope:** spellweb (graph) + cityofmages (register narrative)
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §0 · Why

At v1.7.1 the invitation-mage **seat** (the fourth tome-posture · the Register of Invitations · the empty chair 🪑) was admitted at the same moment as its first occupant, **Vitalik**. The two fused: the institution and the man shared a glyph (🪑), the conjecture C65 was framed as resting on Vitalik specifically ("population-of-one"), and the gateway node read as *Vitalik = the seat*.

Editorial intent (privacymage, 2026-05-27): **tie the seat less to Vitalik.** The Register is a permanent institution — an empty chair that precedes and outlasts any occupant. Vitalik is *entry 01*, a worked example that illustrates the posture without defining it.

## §1 · Glyph discipline (the decoupling key)

A clean three-way split replaces the overloaded 🪑:

| Glyph | Means | Nodes |
|-------|-------|-------|
| 🪑 | **the seat / institution** (the empty chair) | `con-invitation-tome-posture` · the Register of Invitations |
| 🔷 | **the Fourth Turn** (Vitalik's offering) | `con-fourth-turn` · `act-tome-viii-2` |
| 🚪 | **the visitor at the gate** (sigil still pending his own choice) | `gateway-vitalik` |

The open-folio glyph 🪑 now belongs to the seat itself, never to an occupant.

## §2 · What changed

**spellweb (`src/data/nodes.ts`) — committed:**
- `gateway-vitalik`: emoji 🪑 → 🚪; relabelled in desc as "Entry 01 of the Register of Invitations — one invited visiting mage who illustrates the institution rather than defining it"; sigil note clarified (🚪 visitor-at-the-gate; 🪑 belongs to the seat).
- `con-fourth-turn` and `act-tome-viii-2`: emoji 🪑 → 🔷.
- `con-invitation-tome-posture`: added "the register is the institution; the seat outlasts and precedes any occupant… the first occupant illustrates the posture without defining it." Glyph stays 🪑.
- `conj-c65`: reframed — held at candidate strength because the lifecycle is *not yet operationally demonstrated*, NOT because it rests on one mage; first instance "illustrates but does not define"; promotion path generalised to "any second entry stabilises the posture as a class."
- (Separately, same session) the Archivist was bridged into the graph — see the spellweb commit.

**cityofmages (`tomes/register-of-invitations/README.md`) — committed:**
- `status` frontmatter: "awaiting Vitalik's stylus" → "a permanent register · 1 entry filed (the Fourth Turn)".
- Added a framing paragraph: "**The Register is the institution; its entries are instances.**… the current occupant a single worked example."

## §3 · Pending — grimoire patch (NOT hand-edited)

The pinned grimoire `v1.7.1` JSON still encodes the Vitalik-centric framing in two places:
- the **C65** block (`promotion_path` names "Vitalik's acceptance" as a path; "population-of-one at v1.7.1");
- the **`vitalik`** sub-block (`sigil: "🪑 (placeholder · open-folio glyph)"`).

Per the project's grimoire-update discipline, **the pinned JSON is not hand-edited.** These reconcile through the normal patch + re-pin flow as a small **v1.7.2 decoupling patch**:
1. C65 `promotion_path` / notes → generalise off Vitalik (mirror §1–§2 above).
2. `vitalik.sigil` → 🚪 (visitor-at-the-gate · pending); note 🪑 is the seat's glyph, not his.
3. Re-pin and update `agentprivacy_master/src/lib/grimoire-ipfs.ts`.

Until that patch lands, the narrative + graph lead the grimoire — the usual lag in this workflow.

## §4 · What did NOT need changing

`tomes/specs/11-the-invitation-protocol.md` is already person-agnostic — it defines the postures, the four conditions of update, the protocol of waiting, and the editor's entry without centering Vitalik (he appears only in `source_material` provenance). No edit required; it already reads as the standing protocol of an empty chair.

---

*The chair was always the point. The man is the first to be offered it.*
