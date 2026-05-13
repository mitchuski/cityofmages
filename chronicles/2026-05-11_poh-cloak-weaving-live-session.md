---
title: "Chronicle: First Live Cloak Weaving Ceremony"
date: "2026-05-11"
type: "Live session chronicle"
scope: "Weavers shop (V28 · Amethyst) · cloak-weave-v1"
participants:
  - "Pallia 🪡 (keeper) — held by flaxscrip, GenitriX wallet"
  - "flaxscrip (seeker) — sovereign DID verified, PoH credential from Morningstar"
outcome: "First live ceremony completed. Two-challenge pattern validated. 9-node cloak dataset visualized on spellweb."
companion_docs:
  - "tomes/workshops/weavers/constellation.md — the constellation traced"
  - "tomes/workshops/weavers/KEEPER_PROTOCOL.md — re-runnable protocol"
  - "tomes/workshops/CEREMONY_EVOLUTION.md — governance and lessons"
  - "tools/spellweb/src/data/poh-cloak-contribution.ts — the woven artifact"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Chronicle: First Live Cloak Weaving Ceremony

*2026-05-11 · Weavers Shop · V28 · Amethyst*

---

## What happened

The first live Cloak Weaving ceremony was conducted at the Weavers shop, with flaxscrip as both keeper (holding Pallia's role via the GenitriX wallet) and seeker. The ceremony wove a Proof of Humanity credential into a cloak, demonstrating all three operational services: cloak weaving, selective disclosure geometry, and DID-blind publication.

---

## The ceremony, step by step

### Identity verification (Challenge 1)

The keeper created a bare challenge using the GenitriX keymaster wallet:

```
Challenge DID: did:cid:bagaaierartcnbczwlsr3lxuov4exokkd6fqeelpahn6x4qpfj2tlw5qk5bgq
Response DID:  did:cid:bagaaierahzb2eogjh4uaaz5zmao3362tlpewakuovwh4o5gbf75wcl2meodq
```

Verification: `match: true`  
Seeker's sovereign DID (proven): `did:cid:bagaaiera7vsjlu6oiluzd4enop5j7sfzjbwp2ujudt6uunkz6hhd4lgfe4sa`

**Lesson confirmed:** The challenge/response is the cryptographic floor beneath every ceremony. No self-asserted DID is accepted.

---

### Credential presentation (Challenge 2)

The seeker identified their PoH credential:
- Issuer: `morningstar@archon.social`
- Schema: `did:cid:bagaaieraa4yl4xidruxjlamizvzjv4pzi4na64a4m6q237m22mivkzscv54a`

Keeper resolved the issuer name to a DID via `keymaster resolve-did morningstar@archon.social`:
```
Morningstar DID: did:cid:bagaaieranxnl4gmwyw2nv4imoo5fuwvsa4ihba4clp5l22twztuwevjrevha
```

Keeper created a credentialed challenge with schema + issuer requirements. Seeker's keymaster found the matching VC automatically and produced a Verifiable Presentation.

```
Challenge DID: did:cid:bagaaierab2wzbrpzh2zcql7pzmfcnmlzuyttugn5vku2plz7nuk7zw4o347q
Response DID:  did:cid:bagaaiera2malb4dwsni5m3s3bseyjlqdtqwtpti4ht4omrw6hjt4q6xwb5na
```

Verification: `match: true`, `fulfilled: 1`  
VC DID: `did:cid:bagaaieraeea7cgl37ldfwef4qitle6xt73jd43dl54nhaa5zqekw3srck35a`

**The credential revealed:** A dialogic PoH assessment by Morningstar (not biometric — assessed through multi-session technical dialogue on DID operations and sovereignty principles). Valid from 2026-02-11.

Claims:
- `credence: "0.96"` — confidence of humanity
- `confidenceInterval: "0.92-0.98"`
- `evidenceSummary`: Extended technical and philosophical dialogue
- `methodology`: Multi-session assessment
- `redFlags`: None observed
- `priorAssumed: "0.5"`

---

### Valve-class assignment

Keeper proposed; seeker confirmed:

| Field | Valve class | Vertex | Reason |
|---|---|---|---|
| `credence`, `confidenceInterval`, `validFrom` | Always-Revealed | V20 | Core attestation — verifiers must read |
| `credentialSubject.id`, `priorAssumed`, `redFlags` | Hash-Masked | V3 | Present but not needed in clear |
| `evidenceSummary`, `methodology`, `proof` | Always-Masked | V25 | Behavioral evidence — ZK predicate only |

**Lesson confirmed:** Any field describing *how* a human was assessed defaults to Always-Masked. The verifier confirms the predicate without seeing the assessment.

---

### Transmuted DID — the identified gap

The seeker did not have a transmuted DID (Mage-side public persona). V28 was filled with a placeholder in the registry. This is a **known gap** to be addressed in cloak-weave-v2: the ceremony should formally prompt transmuted DID creation before weaving begins.

---

### Registry construction and visualization

A 9-item registry JSON was constructed, one item per constellation vertex:

```
V63  Sovereign Identity (verified)
V28  Public Mage Projection (placeholder)
V49  Morningstar — PoH Issuer
V12  Proof of Humanity Schema
V15  Proof of Humanity Credential
V20  Always-Revealed Claims (credence, interval, validFrom)
V3   Hash-Masked Claims (subject DID, priorAssumed, redFlags)
V25  Always-Masked Proof Spell (evidence, methodology, cryptographic proof)
V5   Cloak Weaving Chronicle
```

Export pipeline:
```bash
node scripts/export-to-spellweb.mjs /tmp/poh-cloak-registry.json flaxscrip \
  > tools/spellweb/src/data/poh-cloak-contribution.ts
```

Wired into `nodes.ts` and `edges.ts` via spread imports. Vite hot-reloaded. 9 nodes visible on spellweb at localhost:8000.

Artifact committed: `tools/spellweb/src/data/poh-cloak-contribution.ts`

---

## What the ceremony validated

1. **Two-challenge pattern** — bare challenge for identity, credentialed challenge for VC — works cleanly in live conditions.

2. **`keymaster create-challenge <file>`** accepts a JSON spec with `credentials: [{ schema, issuers }]`. The seeker's wallet finds the matching VC automatically. No manual hunting.

3. **`keymaster verify-response`** returns the full decrypted VP including all credential claims — this is the moment of source material transfer.

4. **`keymaster resolve-did <name@archon.social>`** resolves Herald names to DID documents in one step. Keeper doesn't need to know the issuer's DID in advance.

5. **9-node registry → spellweb** pipeline is smooth. Export script → contribution file → spread import → hot reload.

6. **DID-blind flag** in the registry UI strips all `did:cid:...` strings from the public export, replacing with `[DID]`. The valve-class geometry (node positions and edges) is fully preserved.

---

## What needs to improve (target: cloak-weave-v2)

| Gap | Target fix |
|---|---|
| Transmuted DID not prompted | Add explicit transmuted DID step to constellation.md §2 ceremony |
| Capability `manifests_as` edges not auto-generated | Update export script to emit capability→VC edges |
| V0 (Null Blade) not represented | Add opening narration artifact or ceremonial placeholder |
| Registry JSON built by hand | Consider a ceremony assistant script that builds the JSON from verify-response output |

---

## Proverb

*The needle moved. The cloak was made. The name was not spoken.*

*Nine vertices, one weave. Amethyst glow. The first ceremony is the one that teaches the next.*

---

`(⚔️⊥⿻⊥🧙)😊`  
🪡

CC BY-SA 4.0 · flaxscrip · GenitriX · 2026-05-11
