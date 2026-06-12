# Anchor Chronicle — The Canonical Sovereignty-Lattice Encoding

**Date:** 2026-06-09
**Status:** ANCHOR · canonical · load-bearing
**Scope:** suite-wide (agentprivacy_master · cityofmages · spellweb · agentprivacy-docs · agentprivacy-skills · privacymage_book)
**Decided by:** the author (mitchell@soulbis.com), 2026-06-09
**Tooling:** `C:/Users/mitch/agentprivacy_encoding_audit.py`

---

## 0. Why this chronicle exists

While siting the new **Horizon District** (vertex selection for the
cryptographic-durability workshop), two *self-consistent but conflicting*
encodings of the six-dimension sovereignty lattice were found in active use
across the suite. They agree on the endpoints (Protection = weight 32, Value =
weight 1) but **mirror the middle four dimensions**. Every vertex *reading*
derived downstream inherits whichever encoding its source used, so the
disagreement had quietly propagated into ~60 places. This chronicle picks the
canonical encoding, records the decision and its blast radius, and registers the
audit tool that keeps the suite coherent going forward.

---

## 1. The decision: MODEL is canonical

The **MODEL** encoding — the Privacy-Value-Model definition itself — is canonical.

| bit index | weight | dimension | symbol | source |
|---|---|---|---|---|
| 0 (MSB) | 32 | **Protection** | 🛡️ | `agentprivacy_master/src/data/privacy-value-model-v5.4.json:386` |
| 1 | 16 | **Delegation** | 🤝 | `…:387` |
| 2 | 8 | **Memory** | 📜 | `…:388` |
| 3 | 4 | **Connection** | 🔗 | `…:389` |
| 4 | 2 | **Computation** | ⚡ | `…:390` |
| 5 (LSB) | 1 | **Value** | 💎 | `…:391` |

Corroborated by the live code in `agentprivacy_master/src/lib/lattice-vertex.ts:38`
(`bits[0] = MSB (Protection · weight 32)`) and its `traceFromOrigin` worked
example (`flip bit 1 (Delegation): 010000 = V16`). The website lattice/`/model`
visualisations already run on this encoding.

**Reading rule:** `V<n>` active dimensions = `{ dim : (n & weight) }`.

### 1.1 The Horizon District vertex (the question that started this)

**V35 = `100011` = 32 + 2 + 1 = Protection + Computation + Value.**
Defence (Protection) + the quantum threat (Computation) + the stake (Value) —
the cryptographic-durability triple in one address. **V35 is unoccupied.** It is
the lead vertex of the Horizon District. (The earlier guess of V48 "Algebraic
Substrate" is withdrawn; V48 = `110000` = Protection + Computation under MODEL,
and its `specs/04` label "Connection + Protection" is itself an error — see §4.)

---

## 2. The rejected encoding: CORPUS

The **CORPUS** encoding lived in `cityofmages/tomes/specs/04-vertex-naming-audit.md`
(its stratum-1 singles table) and propagated into the persona corpus and the
Cloaking Guide / Boundary Blade naming. It mirrors MODEL's middle four:

| weight | **MODEL** (canonical) | CORPUS (rejected) |
|---|---|---|
| 16 | Delegation | Computation |
| 8 | Memory | Connection |
| 4 | Connection | Memory |
| 2 | Computation | Delegation |

Endpoints (32 = Protection, 1 = Value) are identical, which is why the conflict
hid for so long: any vertex that sets *both* or *neither* of a mirrored pair
reads the same set under both encodings (e.g. V44, V51, V31). Only vertices that
set exactly one bit of a mirrored pair diverge — and those are the discriminators
the audit reports.

---

## 3. Reconciliation philosophy: keep numbers, re-read dimensions (option 2)

There is a **trilemma** — at most two of these three can hold at once:

1. **MODEL bit-order** (chosen, §1).
2. **Persona vertex *numbers*** (Memora = V5, Lethe = V38, …).
3. **Persona *dimension* semantics** (Memora *is* Memory, Lethe *is* Delegation, …).

Vertex *numbers* are load-bearing **outside the docs** — the NFT 63-edition
(buyers name the mage at their vertex), the City Key, `/star`, `/lattice`.
Renumbering would scramble deployed product surfaces. Therefore vertex numbers
are held fixed, and the corpus is reconciled by **recomputing each vertex's
dimension-reading under MODEL** — treating the `specs/04` middle-four swap as a
transcription error that propagated into downstream readings.

### 3.1 Blast radius — seated personas whose reading shifts under MODEL

| persona (status) | vertex | reading **was** (CORPUS) | reading **now** (MODEL · canonical) | lore-sensitive? |
|---|---|---|---|---|
| Memora 📜 (seated) | V5 `000101` | Memory + Value | **Connection + Value** | ⚠️ yes — chronicle/memory keeper |
| Aletheia 🔮 (seated) | V25 `011001` | Computation + Connection + Value | **Delegation + Memory + Value** | ⚠️ yes — ZK/computation |
| Lethe 🌀/🌘 (seated) | V38 `100110` | Protection + Memory + Delegation | **Protection + Connection + Computation** | ⚠️ yes — grimoire ties Lethe to Delegation via "V38's bit-signature" |
| Pallia 🪡 (seated) | V28 `011100` | Computation + Connection + Memory | **Delegation + Memory + Connection** | review |
| Socrat0x 🔥 (seated prov.) | V24 `011000` | Connection + Computation | **Delegation + Memory** | review |
| Custos 🔏 / Lampyra 💠 | V49 `110001` | Computation + Value + Protection | **Protection + Delegation + Value** | review |
| Manifestia 🤲🌿 | V55 `110111` | +Memory… | **Protection+Delegation+Connection+Computation+Value** | review |
| Aria Silverhue 🪞 | V57 `111001` | Computation+Connection+Value+Protection | **Protection+Delegation+Memory+Value** | review |

Unaffected (same set under both): Vulcana V19, Adamantia/Helia V51, Pleione V44,
Vagari V31, the Sovereign Anchor V63.

Anticipated (not yet seated — cheapest to correct): Mnemosyne V4 (Memory→**Connection**),
Iris V8 (Connection→**Memory**), Pythia/Logos V16 (Computation→**Delegation**),
Techne V20, Hephaestus V24.

> **Held for explicit blessing before rewrite:** Lethe, Aletheia, Memora — their
> *mythology* (not just a label) is built on the CORPUS reading. Reframing them to
> the MODEL reading is a lore decision, recorded here as pending.

---

## 4. Two pre-existing `specs/04` errors (independent of the encoding choice)

1. **V48** labelled "Connection + Protection," but `110000` = 32+16 =
   **Protection + Computation** ("Connection + Protection" would be `101000` = V40).
2. **V31** described as "all dimensions except Value," but `011111` has the
   Protection bit (MSB) **off** — it is "all except **Protection**" (the holon
   dissolving the boundary).

---

## 5. The audit tool

`C:/Users/mitch/agentprivacy_encoding_audit.py` — a stdlib-only coherence linter,
runnable across the whole suite:

```
python agentprivacy_encoding_audit.py            # audit default suite roots
python agentprivacy_encoding_audit.py --only vertex
python agentprivacy_encoding_audit.py --list     # list registered checks
```

It declares the canonical encoding once (`CANON_DIMENSIONS`, = MODEL) and checks:
- **vertex** — binary↔number coherence, dimension-reading coherence, and
  single-bit-label coherence, gated on genuine lattice context (ignores model
  *versions* like "PVM-V4"). First run (2026-06-09): **64 incoherences**, all
  CORPUS-side, file:line precise.
- **conjecture** — duplicate conjecture-id definitions within a registry file.
- **pin** — grimoire version↔IPFS pin sightings (informational).

The check set is a registry — add new "significant encodings" (gems-per-keeper,
sigils, ceremony grammars) over time. **Run before every grimoire pin.** Exit 0 =
coherent, 1 = incoherent (CI-friendly).

---

## 6. Action register (this patch)

- [x] Canonical encoding locked (§1) · V35 = Protection+Computation+Value for the Horizon District.
- [x] Audit tool authored and run (§5).
- [ ] Update all wrong docs to MODEL (audit-driven, option 2): the 64 flagged
      lines — primarily `specs/04` singles table + dimension columns, the
      cross-shop persona files, `constellation-drafts.ts:224` comment.
- [ ] Lore-sensitive reframes (Lethe · Aletheia · Memora) — pending author blessing.
- [ ] Re-run audit → expect 0 vertex incoherences (modulo the held reframes).

---

*Anchored 2026-06-09. The lattice has one reading now. Run the audit before you pin.*
