---
title: "Hearthold — the 7th Capital, made liquid on Archon"
subtitle: "The cousin-forge edition: the Privacy Is Value Model, built in did:cid"
status: "Edition v2.1 (2026-07-07) · companion to Tome X — The Hearth (Acts 1–2) · tracks Flaxscrip/hearthold @ v0.11.0 (19/19 e2e): Recall, the Knowledge Portal, the step-up ladder made whole"
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
- **Narrative binding:** Tome X — *The Hearth* · [Act 1 · *The House of Archon Answers*](../tomes/tome-x-the-hearth/01-the-house-of-archon-answers.md) · [Act 2 · *The Mage Takes a Face*](../tomes/tome-x-the-hearth/02-the-mage-takes-a-face.md) (Recall · the Knowledge Portal · the ladder made whole)
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
- **Recall (R1)** — the Warden reads its own hold: private, on-device RAG over the sealed vault ("ask
  your vault"), retrieval + answer-generation over embeddings + metadata only, no plaintext exposure
  (`e2e:recall`).
- The **evidence step-up ladder, made whole** — A1 the Warden proves witnessed vault data → A2 the
  Sovereign co-signs on a direct Warden↔Sovereign channel → a registry-governed **factor-2** step-up
  out-of-band on a direct **Warden→Signet** channel, where the Signet prompts *"Approve action?"*
  (`e2e:evidence`, `-stepup`, `-direct`). Disclosure matured to **composite** (issued leaves beside
  witnessed), **selective** (SD-JWT-VC), and **ephemeral** single-use proofs (`e2e:evidence-composite`,
  `-selective`).
- The **demo consoles** — thin React surfaces over per-agent daemons: Warden Console (vault · delegations
  · classifier), Signet Approver (the PoH gate + Warden-authored disclosure view), and the Witness
  interface. The Witness is now a **composable agent** of capability modules (`docs/witness-modules.md`).
- The full **DTG** credential set (one of each VRC/VMC/VIC/VPC/VEC/VWC + RCard — `e2e:dtg-set`,
  `proto:vwc`) + a two-faced **TRQP** trust registry (authorizes issuers outward · grades a Witness's
  autonomy inward · cross-project interop against a foreign registry — `e2e:trust-registry`,
  `e2e:inward-registry`, `interop:registry`).
- The **Game-of-42 bridge**: the Drake Gamers Guild board sealed `VRC → κ → seal` with the City's own
  canon — **byte-matched** against game42 and soulbis — forged into a **City Key** that lights its
  manifold on `soulbis.com/star` and takes its place as a constellation node.

**Landing (built, just outside the 19/19 tested-live line):** the **Knowledge Portal** — a *public Mage
⊥ private Warden* surface that scales the Separation Principle from one person to a guild. The Warden
stays home and private holding a shared KB; only the Mage/Witness wears a public browser face (QR
challenge/response sign-in, no keys in the browser; identity unlock/create/recover; split-host deploy).
Two invariants guard it: *the KB never holds a member's 7th Capital*, and *the Warden reads a query in
memory only — it logs no one*. (`docs/knowledge-portal.md`.)

**Next milestones (upstream):** the higher proof-of-human rungs (biometric · face-liveness · FIDO2),
per-device Witnesses, a Recall GUI + vector store, and hardening the Knowledge Portal.

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
