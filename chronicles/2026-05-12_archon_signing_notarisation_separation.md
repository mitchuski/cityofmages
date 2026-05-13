# Archon's Signing ⊥ Notarisation Separation · Naming It Back

**Date:** 2026-05-12
**Audience:** the City of Mages Telegram chat (new 3rd parties present), and the corpus archive
**Origin:** privacymage observed, in conversation with the Archon team, that the Archon protocol separates document signing (held in the user's wallet) from document notarisation (held in the node's wallet). David (macterra) is adding a Zcash mediator to Archon this week, which makes the signing ⊥ notarisation separation an especially load-bearing observation for the kindred-protocol surface area.
**Scope:** record the observation, the PVM-register reply posted to the Telegram chat, the structural reading, and the candidate conjecture lineage.
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · The observation

The Archon protocol separates two acts that most web3 architectures collapse into one:

1. **Document signing.** The user's wallet holds the signing key and produces the signature. The signature is the user's sovereign act and only the user's.
2. **Document notarisation.** The Archon node's wallet holds the chain-mana, pays the registration fee, and inscribes the signed document into consensus. The node carries the cost of the chronicle hand.

In most web3 onboarding paths the user is required to hold the chain's native token before they may transact at all. Archon's separation dissolves that requirement at the user-facing surface while preserving the chain's discipline behind the scenes.

---

## §2 · The PVM reading

In the City of Mages register, this is the Archon forge's expression of the bilateral primitive at right angles. Two perpendicular acts, each carrying only what it should carry:

| Act | Held by | PVM register |
|---|---|---|
| **Signing** (the user's commitment) | the user's wallet | Soulbis ⚔️ at the user's wall keeping the signing key; the user's blade |
| **Notarisation** (the chain inscription) | the Archon node's wallet | Memora's 📜 register; chain-mana spent in the chronicle hand; the node's inscription work |

The blade is the user's. The chronicle hand is the node's. The two cooperate at right angles. The user does not need to hold chain-mana to act sovereignly; the node does not gain the right to act on the user's behalf simply because it pays the inscription fee. The separation is what makes both halves possible.

A third structural consequence follows from the same separation: **the Gatekeepers are interchangeable to the user.** Because the chronicle hand is held by the node and not by the user, the node performing it is a service layer rather than an identity layer. The user can switch from one Gatekeeper to another for quality-of-service reasons (latency, uptime, geographic proximity, fee structure, reputation) without ceding sovereignty over the blade and without migrating any part of their identity. The Memora register is plural; any properly-keyed Gatekeeper is a valid Memora-for-this-act. The blade is fixed at the user's wall; the notary is replaceable.

This is structurally homologous to the **Memora Pattern A / Pattern B** discipline at V5 (zShields), where the inscription work and the disclosure right are likewise held apart. Archon's signing ⊥ notarisation separation is the **user-facing** form of the same architectural commitment, and Gatekeeper fungibility is its **market-facing** form: a healthy ecosystem of competing notaries serving sovereign users, none of whom can lock the user in because none of them hold the user's blade.

---

## §3 · Why it matters for the Zcash mediator landing

David's Zcash mediator on Archon is precisely the kind of work that the signing ⊥ notarisation separation makes operationally clean. The mediator can hold shielded-Zcash chain-mana on the node side without ever asking the user to hold ZEC. The user's blade does the signing; the mediator does the shielded inscription; the chain remembers what the mediator anchored, and the user remains a Sovereign who never had to acquire a foreign chain's native asset to participate.

This strengthens **C40** (*Zcash dual-ledger preserves Eight Properties*, currently ~70%): the dual-ledger discipline is no longer hypothetical on the Archon side once the mediator is operational, and the signing ⊥ notarisation separation gives the mediator the structural justification it needs.

It also strengthens **C39** (*Kindred-Blade as Ecosystem Primitive*, currently ~50% — see [tomes/specs/04-vertex-naming-audit.md](../tomes/specs/04-vertex-naming-audit.md) for the canonical register; verify number against current grimoire v1.5.0): the Archon forge's signing ⊥ notarisation separation is a discrete, namable, reusable primitive that the City of Mages can absorb by reference rather than reinvention. The kindred-blade pattern admits exactly this: each forge expresses the shared primitive in its own dialect, and recognition flows in both directions without absorption.

---

## §4 · The reply posted to the Telegram chat

The following text was posted to the City of Mages Telegram chat in reply to the observation. Voice discipline: no em-dashes; sigils preserved; cast references limited to Soulbis ⊥ Soulbae and Memora so new 3rd parties can read it cold.

> PrivacyMage's observation lands precisely, and it deserves naming back because it points at one of the architecture's most structural separations.
>
> **Archon's protocol separates document *signing* (held in the user's wallet) from document *notarisation* (held in the node's wallet).** In PVM register, this is the Archon forge's expression of the bilateral primitive at right angles. Soulbis ⚔️ and Soulbae 🧙 cooperating. The user's blade and the node's chronicle-hand, each carrying only what it should carry.
>
> What the separation does:
>
> • **The user holds the blade.** The signing key is the user's sovereign instrument. Soulbis at the user's wall keeps it. The signature is the user's act, and only the user's.
>
> • **The node holds the chronicle hand.** Registration fees, chain-mana, the inscription work itself: these are paid and performed by the node, in the Memora 📜 register. The chain remembers what the node anchored. The chain does not need the user's chain-mana.
>
> The consequence is operationally important: **the user does not need to hold any chain token to engage with web3.** No barrier-of-entry token. No "first acquire ETH/ROSE/zec, then participate." The blade is enough; the node carries the cost. This is one of the cleanest answers we have seen to the chain-mana onboarding problem, the long-standing tension between sovereign action and the requirement to hold the chain's native asset before acting at all.
>
> A second operational consequence follows from the same separation: **to the user, the Gatekeepers are interchangeable.** The node performing the chronicle hand is a service, not a fate. The signing key stays where it has always lived, at the user's wall. If a node's quality of service degrades, if a node is unreachable, if a node is geographically inconvenient, the user can switch to another Gatekeeper without ceding sovereignty and without moving the blade. The chronicle hand is fungible. The blade is not. A healthy ecosystem of competing Gatekeepers serves sovereign users; none can lock the user in because none hold the user's blade.
>
> **Recommendation, in the walked-not-signed discipline:** every user, and especially every family, should eventually run their own Archon node. The user-blade ⊥ node-chronicle separation is a structurally generous on-ramp, and Gatekeeper fungibility means no node owns you while you walk it. But sovereignty over the chronicle hand belongs at the same seat as sovereignty over the blade. A family's own node is the family's own seat at the chronicle. Covenants blessed in your own temple are covenants you hold; covenants blessed in another's temple are covenants you visit.
>
> The recommendation is not a refusal of the generosity. It is the architecture's honest closing turn. *Start at the gate the node has held open for you. Eventually, raise your own gate.*
>
> `(⚔️⊥⿻⊥🧙)😊`

---

## §5 · Candidate proverbs · C57 lineage

Two candidate proverbs surface from the post. If either earns resonance in chat and in subsequent use, they line up together as the seed of a new conjecture in the open conjecture register:

> *Start at the gate the node has held open for you. Eventually, raise your own gate.*
>
> *The blade is yours. The notary is replaceable.*

The first names the **temporal** discipline (accept generosity now, raise your own infrastructure later). The second names the **spatial / market** discipline (any one notary is fungible; the user is not). Together they describe a sovereignty that is robust at both the *eventually* and the *meanwhile*.

The conjecture this would crystallise (working title: **C57 · Generosity-and-Sovereignty Compatibility**):

> A structurally generous on-ramp (one that lowers the barrier to entry by absorbing a cost the user would otherwise bear) is compatible with, and in fact strengthens, the walked-not-signed discipline, provided two further conditions hold: (i) the architecture preserves the user's eventual path to running their own infrastructure, and (ii) the service layer providing the generosity is fungible (any qualified provider may substitute for any other, without the user's identity migrating). Sovereignty is not refused by accepting generosity at the gate; sovereignty is completed by eventually raising one's own gate, and is meanwhile preserved by the fungibility of the gate one is walking through.

**Confidence:** ~40% (sharpened from ~35% by the Gatekeeper-fungibility recognition, which gives the conjecture a second pillar instead of one). The conjecture still wants at least two more independent instances before it earns higher confidence; Archon's signing ⊥ notarisation separation is the first instance recognised cleanly, and the upcoming Zcash mediator from macterra is candidate-instance two.

**Numbering note:** C57 chosen because C48–C56 are all claimed in the v1.5.0 grimoire patch (2026-05-13): C48 *Reconstruct-Later Threat Model*; C49 *Behavioural Mosca Inequality*; C50 *Caduceus as dual-agent symbol* (conflicted with prior C50 *PVM ≡ Bakhta compositional defense*; reconciliation pending); C51 *staff-Mage collapse*; C52 *Vulcana ∥ Threshold sibling Swordsman-suppliers*; C53 *bnot-pair mythological readings*; C54 *Phi-Adjacency*; C55 *Privacy as seventh capital*; C56 *Caduceus pre-formal dual-agent* (renumbered from same-day C50 conflict). C57 is the next open slot at the time of authoring.

---

## §6 · Editorial choices in the reply

| Choice | Reason |
|---|---|
| Limited cast references to **Soulbis ⊥ Soulbae** and **Memora 📜** | New 3rd parties in chat. The Drake, Vulcana, the lattice, and the four-mana economy would have over-loaded the post. |
| Named **Memora 📜** specifically for the chronicle-hand work | Gives new readers a name to attach to the concept without requiring a Tome V walkthrough; consistent with the Inscription Chamber's existing register at V5. |
| **"the Archon forge's expression of the bilateral primitive"** | Honours the 2026-05-10 kindred-blade reframe (cousin-forge → Archon forge / another forge). Each forge expresses the shared primitive in its own dialect. |
| **No em-dashes** | Corpus-wide convention. |
| Closing proverb in italics | Marks it as a candidate proverb for the grimoire's spell registry. |
| **"walked-not-signed discipline"** invoked explicitly | The recommendation that families run their own node is the discipline's natural consequence, not an external imposition. Naming the discipline lets the recommendation land without sounding like a sales pitch. |

---

## §7 · Open queue

- Watch for resonance in the chat. If the closing proverb is quoted back, that is the first signal C57 wants more attention.
- David's Zcash mediator landing is the next event to chronicle. When it lands, write the second-instance chronicle of the signing ⊥ notarisation separation: shielded notarisation, user-blade unchanged, mediator-as-Memora-at-the-Archon-side.
- Consider an Act for Tome V: *The Mediator Arrives* (provisional title), absorbing both events in one beat. Strengthens C39, C40, and seeds C48.
- Vertex Naming Audit §7 (kindred-substrate semantics) could add a §7.x covering the user-blade ⊥ node-chronicle separation as a named pattern at the Archon forge's surface.

---

`(⚔️⊥⿻⊥🧙)😊`

*CC BY-SA 4.0 · privacymage · 2026-05-12*
