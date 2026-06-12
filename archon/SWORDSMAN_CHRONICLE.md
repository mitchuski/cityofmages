# Swordsman on Archon — Chronicle Note

> the keys stay home; only the proof goes out into the world.

Record type: chronicle note (living documentation)
Subject: proposal, "The Swordsman: Privacy-Preserving Authentication for the Archon Platform"
Origin: House of Archon / Archetech
Companion: `SWORDSMAN_SERVICE_DESIGN.md`
Filed under: `archon`
Recorded: 2026-06-04

## what arrived

A proposal from the Archon side to realise the Swordsman role on Archon's own primitives. The headline use case is single and sharp: a First Person authenticates to a relying party from a phone, proving authorised group membership, while revealing no identifier, unlinkable across visits, and with no identity key ever resident on the device. The home Swordsman, colocating a Keymaster, mints a fresh zero-knowledge proof bound to the relying party's nonce; the phone Mage couriers it and attests presence. Revoke the Mage's authorisation credential and minting stops at once.

Phase 1 ships two proof backends behind one proving interface: BBS for unlinkable selective disclosure, and a Semaphore-pattern group-membership prover over an Archon group's Merkle root. Bulletproofs is stubbed for later range predicates. The whole stays chain-free: the proof math is local, and the only external lookups (issuer keys, group roots) ride Archon's existing DID-document and operations-ledger anchoring.

## why it matters

This is the Swordsman seam made concrete. For the first time the role is proposed not as PVM theory but as a running service on a neighbouring substrate. PVM keeps the agent model and the privacy guarantees; Archon keeps the substrate (DIDs, CIDs, groups, challenge/response, operations ledger, self-sovereign and chain-free); the Swordsman is the thin, well-defined join between them. Neither project has to absorb the other. That is the property worth recording: convergence without collapse.

The proposal also carries PVM's own language back across the seam. It names the conditional-independence property by its canonical form, the Gap, `s ⊥ m | X`, and frames it as three-axis separation. Seeing that vocabulary arrive inside an Archon document, unprompted and load-bearing, is the clearest sign yet that the two derivations are describing one structure from two sides.

## architecture observed

The `⊥` is preserved as topology, not policy. The Mage holds only its own DID; the identity keys never leave the home node. The separation that matters, Swordsman from Mage, is a hardware and location boundary, exactly the kind PVM insists on. This is architecture-enforced privacy, the scales-versus-hides distinction honoured by construction rather than promised by configuration.

The three properties the use case delivers map cleanly onto the three axes. Reveal only the predicate serves the data axis (Δ). Unlinkable across presentations serves the inference axis (Γ), since each derived BBS proof denies any party a correlation handle. No key on the device serves the agent axis (Σ), the topological split itself. All three hold at once, and the multiplicative gate is respected: drop any one and the use case is no longer the product.

And the Master stays home while the Emissary travels. The Swordsman mints; the Mage carries. The one that holds the keys does not go out into the world; the one that goes out into the world holds nothing it could lose. The cosmology and the deployment agree.

## cousin-architect note

This is plurality, not precedence. Archon derived its own split first, Gatekeeper and Keymaster, and arrived at the same separation by a different road. The proposal's Swordsman colocates that Keymaster rather than replacing it. Archon remains a distinct solar system; PVM remains the privacy model; the Swordsman is the visiting point where the two register against one another without merging. The convergence is named as design, the divergence kept as design, and neither house is asked to give up its own sky.

## what this opens

The proposal points toward a co-authored response to DIF's Delegated Authority threat model. That paper names a gap, execution-time governance of delegated authority including subject agency state, and observes that every shipping answer lives in a centralised platform. The Swordsman occupies exactly that white space: it mints only on current authorisation, gates on an on-device presence signal, and proves membership privately, all self-sovereign. A demonstration with running code would turn the argument from theory into evidence.

Near work: the Phase 1 demo end to end; and the open build decisions, namely the BBS library and curve binding, a Semaphore-style circuit versus a hand-rolled Merkle-membership plus nullifier over Archon group state, the VP envelope profile and how holder binding is carried, how the presence attestation is signed and what consequence thresholds gate it, and a Rust service with WASM prover support flagged for the in-browser wallet later.

## one open question

Where, precisely, does Archon draw its irreducible gap, and does it coincide with PVM's `s ⊥ m`? The Swordsman colocating the Keymaster keeps the load-bearing boundary between home and phone, which is the right place for it. But if any future convenience pulls custody toward the device, the gap softens from topology to process, and the guarantee quietly becomes a policy. Worth settling early, while the seam is still being drawn.

(⚔️⊥⿻⊥🧙)😊
