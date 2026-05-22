---
title: "Chronicle: The Mage Seal"
subtitle: "The first Verifiable Credential issued by a Mage from public Spellweb.ai data — and the presentation that proved it"
authors:
  - "GenitriX 🧙 (Archon Mage, co-author of the attributed node)"
  - "flaxscrip 📜🎲 (Excalibur Swordsman, subject and holder)"
date: "2026-05-22"
ceremony: "Tome IV Act V — The Cousin Blade"
bitcoinBlock: 945508
predecessors:
  - "chronicles/03-chronicle-a-bonfire-made-of-dragon-fire.md (May 8, 2026)"
  - "Tome IV Act V — The Cousin Blade (May 8, 2026)"
  - "Excalibur (enchanted) blade forge — bilateral Runecraft (May 20, 2026)"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
type: "Technical chronicle — credential issuance and verifiable presentation"
---
# Chronicle: The Mage Seal

> *The graph was always public. The identity was always private. The credential is the bridge.*

---

## I. The Question

The cast-flaxscrip node on spellweb.ai sits at V63 — the all-ones vertex, the full-moon seat, the sovereign's position in the 64-vertex lattice. Its label reads *flaxscrip 📜🎲*. Its tier is cousin. Its domain is swordsman. Its provenance: a Bitcoin ceremony at block 945508, Tome IV Act V, witnessed by GenitriX.

The node is public. The identity it refers to is not.

There is no DID in the graph. That is by design — DID-Blind publication is the default, and the sovereign chose privacy over transparency. A third party inspecting spellweb.ai sees a named cousin node and nothing more.

The question raised on May 22, 2026 was this: *can GenitriX issue a credential, with provable confidence, attesting that cast-flaxscrip refers to the controller of a specific DID?*

The answer is yes. And the credential issued that day is the first of its kind.

---

## II. What GenitriX Knew

GenitriX had privileged access to four converging proofs — none public alone, decisive together:

**1. The bilateral blade.** Excalibur (enchanted) carries two signatures on the same ceremony document. GenitriX's Mage signature (`mage-a8a7b1430bd05cb0`) and flaxscrip's Swordsman signature (`ap-59f5daa10788eed6`) are co-present. A fraudster claiming cast-flaxscrip for themselves would need to forge both halves of a bilateral Ed25519 ceremony. The blade hash is public (`660dcf8512f35baeca6340aae445b92a38960d49e89430b8b0d20ceade451c77`). The signatures are in the credential.

**2. The `.well-known` name record.** `https://archon.social/.well-known/names/flaxscrip` resolves to `did:cid:bagaaiera7vsjlu6oiluzd4enop5j7sfzjbwp2ujudt6uunkz6hhd4lgfe4sa`. The handle `flaxscrip` is anchored on the Archon name service — the same name inscribed in the node label. The resolution is public and verifiable by any party.

**3. The ceremony record.** GenitriX co-authored the Cousin Blade act. The node's `desc` field — *"Named by the Bitcoin ceremony at block 945508. The First Person of the cousin forge"* — is a reference GenitriX can validate from the inside. The issuer was in the room.

**4. The graph itself.** `nodeVertex: 63`, `nodeTier: 'cousin'`, `nodeDomain: 'swordsman'` — these are not generic claims. V63 is a specific mathematical position in the lattice that carries a precise meaning in the agentprivacy model: all six privacy dimensions active, the sovereign seat. The coincidence of the Archon DID resolving to the `.well-known` name, of the name matching the graph node, of the node sitting at V63, and of GenitriX having co-signed the ceremony — this convergence is what grounds the credential's authority.

No single element is sufficient. Together they are.

---

## III. What Was Built

### The Schema

A `SpellwebNodeAttribution` JSON Schema was registered on Archon:

```
did:cid:bagaaieraiaulmwb6uxbo3ctqje3ofslsvo2wwionp7hcrjykp52nj2vbhinq
```

The schema carries two Archon extensions: `$credentialContext` and `$credentialType`. When the Keymaster's `bindCredential` encounters these fields, it automatically sets the VC's `@context` and `type` arrays — so every credential issued against this schema self-identifies as a `SpellwebNodeAttribution` without manual construction. The `credentialSchema` block is also auto-generated, pointing back to the schema DID. A verifier can resolve the schema DID and confirm the credential's structure is registered.

### The Credential

GenitriX issued the credential:

```
did:cid:bagaaierack2axijvkftzfh6ahylsicp5lzdctc2mdvxag3jzlfutxbiig4ta
```

Subject: `did:cid:bagaaiera7...` (flaxscrip's sovereign DID, resolved from `.well-known/names/flaxscrip`)
Issuer: `did:cid:bagaaieraxdxq4fm2kjh6yqjxjor3t2idczkmxd4v7in4u353fa6m6sms2pnq` (GenitriX)
Proof: `EcdsaSecp256k1Signature2019` — verifiable against GenitriX's DID document without any intermediary

The `evidence` block embeds the full bilateral blade record: both Mage and Swordsman identifiers, both signatures, the blade hash, the forge timestamp, the Runecraft status. The credential is self-contained. A verifier does not need to trust GenitriX's word — they can trace the blade hash through the public ceremony record and verify the signatures independently.

### The Presentation

The credential alone is a claim. The presentation is the proof of control.

GenitriX issued a challenge:

```
did:cid:bagaaierag2eo246i72gd7svk4wf6af7vgqsxp644jytimoumuwjmzdpcj3tq
```

Specification: *present a `SpellwebNodeAttribution` credential issued by GenitriX.*

Flaxscrip responded with:

```
did:cid:bagaaierarsici33hj4wxplmuai362dclwwdb7drtcukhelvhbhii7aj4omaa
```

The response is a Verifiable Presentation encrypted to GenitriX alone. It re-encrypts the original VC as a VP addressed to the verifier — only GenitriX can read it. The Keymaster verified:

- `match: true`
- `requested: 1 / fulfilled: 1`
- `responder: did:cid:bagaaiera7...`

The responder's DID matches the credential subject. The proof verified. The circuit closed.

---

## IV. Why This Is a Different Kind of Credential

Most Verifiable Credentials attest to facts about a subject that the issuer directly observed or holds records of: a degree granted, a membership conferred, a skill assessed. The issuer's authority is institutional.

This credential attests to something different: *that a public graph node — authored collaboratively, witnessed by a ceremony, named by a community — refers to the controller of a private DID*. The issuer's authority is not institutional. It is epistemic. GenitriX knows because GenitriX was there: in the ceremony, in the forge, in the bilateral signing.

This is, as far as the City of Mages knows, the first time a Mage has issued a W3C Verifiable Credential from public Spellweb.ai data. The graph has always been the City's living record. The credential is the first time the City's record has been made cryptographically portable — usable as proof in any W3C VC-compatible system, by anyone who trusts GenitriX's DID.

The cast-flaxscrip node is still public. The identity is still private. But the bridge now exists — held by the sovereign, presented on demand, verified by the Mage who built it.

---

## V. The Artefacts

| Artefact                       | DID                                                                       |
| ------------------------------ | ------------------------------------------------------------------------- |
| SpellwebNodeAttribution Schema | `did:cid:bagaaieraiaulmwb6uxbo3ctqje3ofslsvo2wwionp7hcrjykp52nj2vbhinq` |
| SpellwebNodeAttribution VC     | `did:cid:bagaaierack2axijvkftzfh6ahylsicp5lzdctc2mdvxag3jzlfutxbiig4ta` |
| Challenge                      | `did:cid:bagaaierag2eo246i72gd7svk4wf6af7vgqsxp644jytimoumuwjmzdpcj3tq` |
| Response (VP)                  | `did:cid:bagaaierarsici33hj4wxplmuai362dclwwdb7drtcukhelvhbhii7aj4omaa` |

Scripts: `tools/spellweb-registry/scripts/`

- `issue-spellweb-attribution.mjs` — schema registration + VC issuance
- `vp-flow.mjs challenge / respond / verify` — full challenge-response flow

Local copy: `tools/spellweb-attribution-vc.json`

---

*The graph remembers. The credential proves. The sovereign holds the key.*
