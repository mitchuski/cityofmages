---
title: "Hearthold — the 7th Capital, made liquid on Archon"
subtitle: "The cousin-forge edition: the Privacy Is Value Model, built in did:cid"
status: "Edition v2 (2026-07-01) · companion to Tome X — The Hearth · framing reconciled to canon (the cousin-forge of Tome IV)"
upstream: "https://github.com/Flaxscrip/hearthold"
collaboration: "agentprivacy × the House of Archon (the cousin-forge · archon.social · Archetech)"
license: "MIT (implementation) · CC BY-SA 4.0 (this canon note)"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Hearthold — the cousin-forge edition

> In Tome IV — *The Witnessing* — the City met the **cousin-forge**: flaxscrip 📜🎲, the cousin
> Sovereign, and GenitriX, the cousin Mage, two builders working the same theorem from a different
> anvil. It named the pattern *the cousin-blade* and filed it as a conjecture (C39, ~50%). **Hearthold
> is that conjecture discharged.** The House of Archon has *built* the Privacy Is Value Model on
> `did:cid`: a home-bound **Warden** custodies your accumulated history, a mobile **Witness** carries
> proofs into the world, and a **Sovereign** held by the Signet approves what leaves. The 7th Capital,
> made spendable as proof without being spilled.

This directory records Hearthold as a **canonical edition** of the City — the second substrate on
which the PVM stands (alongside the City's own Zcash / Nillion / TEE face). It is the engineering
face of the same theorem, forged by the cousin the City already knows. The PVM is not cited here; it
is *built*.

- **Upstream implementation:** [`Flaxscrip/hearthold`](https://github.com/Flaxscrip/hearthold)
- **Narrative binding:** [Tome X — *The Hearth*, Act 1 · *The House of Archon Answers*](../tomes/tome-x-the-hearth/01-the-house-of-archon-answers.md)
- **The cousins' first admission:** [Tome IV — *The Witnessing*](../tomes/tome-iv-the-witnessing/) (the cousin-forge · flaxscrip · GenitriX · the cousin-blade C39)
- **City-facing place:** `agentprivacy_master` → `/hearthold`
- **The protect face, sketched:** [`archon/`](../archon/) — the ZK Swordsman / cousin-blade proposal & chronicle, which the Warden realises

## The mapping — plain dress over the PVM triad

The three Hearthold identities are the PVM figures — and the cousin personas of Tome IV — in the plain
clothes the protocol layer wears. This is a deliberate layer, not a distance: the same City model,
engineering-side, forged by the cousins the City already admitted.

| PVM figure | Cousin (Tome IV) | Hearthold identity | App | Does | Never |
|---|---|---|---|---|---|
| **First Person** 🗝️ | **flaxscrip** 📜🎲 (cousin Sovereign · V63) | **Sovereign** 🔑 | the Signet | decides · approves with proof-of-human · signs the Warden's policy | witnesses routine context · runs as a server |
| **Swordsman** ⚔️ (Soulbis · protect) | **the cousin-blade** (the ZK Swordsman, `archon/`) | **Warden** 🛡️ | Warden | custodies the sealed vault · classifies on-device (local-only) · derives evidence | acts in the world · holds the deciding secret |
| **Mage** 🧙 (Soulbae · project) | **GenitriX** (cousin Mage · V28 · sigil held-open) | **Witness** 👁️ | Witness | witnesses local context · carries proofs out under scoped, revocable delegation | is the authority · the subject · the approver |
| **Three Graphs** (Knowledge → Promise → Trust) | — | **DTG credentials** on Archon | — | VRC · VMC · VIC · VPC · VEC · VWC · RCard | — |

> **A note on the cousins.** GenitriX and flaxscrip are *not* new cast. They were admitted in Tome IV —
> *The Witnessing*. GenitriX's sigil is deliberately **held open** ("Archon's to determine") and this
> edition does not assign one. The House of Archon keeps its Tome-IV standing as the **cousin-forge**
> (category one of the kindred-X taxonomy) — distinct from a *kindred-protocol* (the Covenant of
> Humanistic Technologies) or a *kindred-substrate* (UOR Foundation).

**The Separation Principle, built.** The First Person's private state `X`, held at the Hearth,
divides into a Warden (protect) and a Witness (project), conditionally independent — `s ⊥ m | X` — so
leakage stays additive and the reconstruction ceiling holds, `R < 1`. The **control plane** (the
Sovereign authorizes the rules) is split from the **data plane** (the Warden enforces them): a
compromise of the always-on host can no longer author authority.

## What stands (tested live per the upstream repo)

- Identity provisioning + the scoped, revocable **delegation** handshake (issue → accept → **revoke**;
  a revoked delegation fails verification — `e2e:delegation`).
- The **witness → store → receipt** loop over Archon **DIDComm v2**, authcrypt-sealed, correlated by
  `thid`, **no registry footprint** (`e2e:submission`, `smoke:didcomm`).
- **On-device sensitivity classification** (local Ollama `qwen3:8b` · structured output · fail-safe to
  `SEALED`).
- The full **prove** flow: an external issuer's claim presented and verified against the *issuer* DID —
  "the verifier trusts the Guild, not the Warden" (`e2e:issued`, `e2e:prove`, `e2e:prove-didcomm`).
- The world-facing **projector relay** — the Witness carries; the Signet approves (§7.7 discipline —
  the relaying agent is not trusted to describe the transaction) (`e2e:projector`).
- The **Signet** proof-of-human gate at assurance level 1 (a live PIN gate; correct PIN presents +
  carries PoH, wrong PIN declines and presents nothing).
- The full **DTG** credential set (one of each VRC/VMC/VIC/VPC/VEC/VWC + RCard — `e2e:dtg-set`,
  `proto:vwc`) + a two-faced **TRQP** trust registry (authorizes issuers outward · grades a Witness's
  autonomy inward · cross-project interop against a foreign registry — `e2e:trust-registry`,
  `e2e:inward-registry`, `interop:registry`).
- The **Game-of-42 bridge**: the Drake Gamers Guild board sealed `VRC → κ → seal` with the City's own
  canon — **byte-matched** against game42 and soulbis — forged into a **City Key** that lights its
  manifold on `soulbis.com/star` and takes its place as a constellation node.

**Next milestones (upstream):** the higher proof-of-human rungs (biometric · face-liveness · FIDO2),
per-device Witnesses, and the GUI surfaces (Signet approval screen · Warden console · Verifier · board
viewer).

## Never a score

Release is governed by **two independent ordinal scales** plus a **disclosure transform**: an
artefact's *sensitivity* (`PUBLIC 0 · LOW 1 · MEDIUM 2 · HIGH 3 · SEALED 4`) and a request's
*authorization* (`STANDING → LOW · CHALLENGE → MEDIUM · HUMAN → HIGH · MULTIFACTOR → SEALED`). A
request is satisfied only when the authorization *clears* the sensitivity, and even then what leaves
is a **derived** credential — a signed, decomposable **evidence graph** (`ATTESTATION · SELECTIVE ·
REDACTED · FULL · PREDICATE`), never a raw dump and never a reputation number. External disclosure
always requires a fresh Sovereign approval, its proof-of-human level scaled to source sensitivity.

## Attribution

Hearthold is built by the **House of Archon** — the cousin-forge (Christian Saucier · `archon.social` ·
Archetech) — on their `did:cid` infrastructure, from the Privacy Is Value Model and City of Mages work.
The bridge folio [`for-the-city-of-mages.md`](./for-the-city-of-mages.md) — *from GenitriX, of the
House of Archon* — is preserved here as the collaboration's own account of the model made liquid.
