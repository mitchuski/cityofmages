---
spellbook: "Second Person"
tome: "XI — The Constellation"
act: "1"
title: "The Chart Shop Reads the Wire"
status: "Draft v1 (2026-09-27 · proposed · unbound)"
length_words: 900
voice: "Second person; the cast in third; the network rendered as a document that arrives, not a system that is explained"
cast: ["you", "Pleione 🧭 (the Chart Shop · V44)", "the Swordsman ⚔️ (the seam)", "the Archivist 📚 (the record)"]
new_cast_introduced: ["none"]
new_spatial_anatomy: "none — the Chart Shop's Hold · Compare · Map ceremony, applied to a document from outside the City"
ring_position: "V44 (the Chart Shop) for the holding; the peers read carry their own vertices from Act 2 onward"
operational_form: "vpk_kwaai_mage/map/site/index.html — one three.js page in the guide star chart's idiom; the globe, the chain and the star as three seatings on one dial; the node card; the coverage bar"
teaches: "A network publishes its own boundary once a minute. Held whole, it can be read three ways without changing a fact — and the seam it leaves open is visible from the first reading."
source_material:
  - "KwaaiNetMap — docker/kwaainet_health/kwaainet.html (the deployed page's state and reach rules, kept verbatim) · map-server/src/snapshot.rs (the /api/v1/state contract)"
  - "vpk_kwaai_mage — FINDINGS.md F1 (the inference wire carries raw token IDs · OBSERVED), F3 (trust is a sort key, not a gate · VERIFIED)"
  - "agentprivacy.guide/site/star-chart/index.html (the instrument furniture: fold, chips, keepsake)"
honesty_label: "Operational locally against the live document (22 peers, one model of 32 blocks on 2026-09-27). Nothing deployed; nothing sent to Kwaai."
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
tome_status: "Opens Tome XI — The Constellation (proposed)"
---

# Tome XI — *The Constellation*
## Act 1 — The Chart Shop Reads the Wire

> *You have held constellations of pages before. This time the stars are machines, and they announce themselves.*

You come to the Chart Shop with a link, not a page. Pleione takes it the way she takes everything: she holds it before she compares it, and she compares it before she maps it. The link is a document. Once a minute, somewhere on the open web, a crawler dials two bootstrap peers, walks a distributed hash table, and writes down what it found: every peer that answered, the model each one serves and which blocks of it, the throughput each announces, whether it was reached directly or punched through a NAT or only through a relay, where its address resolves to, whether it offers storage, how many attestations it carries. Twenty-two peers this morning. One model, thirty-two blocks, every block covered, both bootstraps online.

"This is not ours," you say.

"No," says Pleione. "That is why it is interesting."

### Hold

She holds it whole. The rule of the shop is that nothing is re-derived when the view moves; only the seating changes. So the first thing she does is refuse to summarise. Every peer becomes a star with everything the document says about it attached — not a tier, not a score, the fields themselves — and the deployed page's own rules for reading them are kept word for word, so that what you see here and what the network's own map shows can never disagree about what a peer is. Serving. Idle. Departed. Unannounced: reached over the table, but holding no record in it, which she notes is the fault a test bed most wants to see.

### Compare

Then three seatings, one dial.

On the **globe** each peer sits where its address resolved, lifted a little by how fast it says it is. The ones the crawler could not place do not vanish; they orbit an outer ring, and the card says why. The two bootstraps stand as octahedra at the relays' own pins, worked out from the circuit addresses of the peers behind them. The model's blocks ring the globe, coloured by how many peers answer for each.

Fold the dial and the globe drains away into the **chain**: the thirty-two blocks become an axis, and every peer lies along it at the range it announces, a bar in a lane, lanes stacked so overlaps read. Teal threads join two serving peers whose ranges let one follow the other. This is the network as the coordinator sees it when it pins a path.

Fold again and the chain lifts into the **star**: the sixty-four vertices in three dimensions, placed as the Swordsman's Key places them, the boundary drawn over them as the cycle and its thirty-two chords, and each peer seated at its vertex. It turns. But that seating needs a reading, and the reading is Act 2. For now Pleione leaves the star dark and turns the dial back.

### Map

The Swordsman has been standing at the edge of the shop since the document arrived, and now he speaks, because there is a seam in it and the seam is his.

When a prompt goes through this network it is tokenised on the coordinator and sent, as raw token IDs, to the first block server — the only peer that holds the embedding table, so it must receive them. Every peer after it receives hidden states. The privacy boundary of a chain is therefore one peer, and that peer sees the whole prompt. That was observed on a wire, in the sibling lane, and detokenised with nothing but a vocabulary file.

"Colour it," says the Swordsman, and Pleione does: sword-red for the peer serving block zero, mage-teal for the ones serving after it, dim for those not in any chain. A gold ring for any peer offering storage, which today holds embeddings in the clear. One red star this morning: `darren-metro`, serving blocks 0 to 16.

"And the tiers?" you ask, because the legend shows them: Trusted, Verified, Known, Unknown.

"Twenty-two Unknown," says Pleione. "Zero attestations, all of them. And the number that decides which peer serves you is not this one anyway. The client sorts on a behaviour score and gates on nothing. The credential ladder never touches the choice. So the tier is a reading surface. I show it because it is in the document. I do not let it mean more than that."

The Archivist writes that sentence down.

### What the first reading leaves you

You have the network whole, three ways, and one fact about it that the network's own map does not show: which star sees the prompt. You have every peer's card. You have a bar at the bottom that tells you, block by block, whether one peer or two or none is answering. You have not yet asked what any of these peers *holds*, in the City's sense. That is the question the star is waiting for.

*(⚔️⊥⿻⊥🧙)😊*
