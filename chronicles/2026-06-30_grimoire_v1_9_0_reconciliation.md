# Chronicle — Grimoire v1.9.0 · the Reconciliation Release

**Date:** 2026-06-30
**Author:** mitchell@soulbis.com (First Person) · authored with Claude (the Archivist's hand)
**Artefacts:**
- `grimoire/city_of_mages_grimoire_v1_9_0_patch.json` (structured-delta patch over the v1.8.1 head)
- `grimoire/scripts/merge_v1_9_0_patch.py` (idempotent merge → head)
- `grimoire/city_of_mages_grimoire_v1_9_0.json` (the built head · **not yet pinned**)
**Signature:** (⚔️⊥⿻⊥🧙)😊
**License:** CC BY-SA 4.0

---

## What this is (2–4 lines)

A reconciliation release. The structured grimoire JSON had fallen behind the lore bound on disk: a whole district, a whole tome, three Tome VIII acts, and ~28 conjectures were authored and bound locally but never landed in the head. v1.9.0 makes the JSON match what was actually bound, and binds the one act that was still a candidate. It is purely additive; it supersedes and retires nothing.

## The gap, and why it opened

The trigger was the First Person's read: *"many of the new tomes are not included and accepted yet."* Tracing it surfaced the root cause.

- The **v1.8.0 patch** (2026-06-09) authored the entire **Horizon District** — Eos 🌅 / Dokimé 🪨 / Poros 🛤️ at V35, the Salvage Yard, Tome IX, conjectures C67–C71, the V35 vertex — alongside the canonical lattice-encoding lock and six persona reseats.
- But only the patch's **prose note** (`v1_8_0_note`) was merged into the **v1.8.0 head**. The structural sections were carried in the patch file and **never applied**. The head's conjecture register stopped at C65; it had no Tome IX, no Eos/Dokimé/Poros, no V35.
- **v1.8.1** (the Librarian 🗃️, 2026-06-21) was then built on that incomplete head — so it inherited the gap. Its own `v1_8_1_amendments` even reported **9 tomes opened** and a Tome VIII of **6 acts**, while the structure held only **8 tomes** and Tome VIII act entries **1/2/6**. Prose and structure had diverged.

The `DREAM-2026-06-29.md` survey had already mapped most of this as open threads (Tome IX Act 5 unbound; v1.8.1 re-pin held; grimoire v1.9.0 "not taken"). v1.9.0 is the taking.

## The myth-gate

**Tome IX Act 5 — *The Name That Climbs Out*** (the Limitative Reading, from PVM V6 Run 8) was a **DRAFT CANDIDATE**, explicitly awaiting the First Person's bind/hold/release decision. The decision, taken 2026-06-30: **BIND.** Its four conjectures — the limitative joins — register with this patch:

- **C90** The Limitative Inversion (~90%, as observation)
- **C91** Gödel ↔ Φ_agent (~60%) — zero-memory as the first-theorem instance
- **C92** Tarski ↔ Φ_inference (~70%, rides on C81, cannot exceed its base) — the existence-leak as Tarski-undefinability
- **C93** Content-addressed liveness leak (~55%) — a live address confesses its content exists

Honesty held: these are structural framing (~80%), not theorem-to-theorem reduction (~50%); the act teaches a reading, not a result, and changes no confidence in the corpus.

## What v1.9.0 lands

1. **The Horizon District** at V35 (Protection + Computation + Value) — three stance-differentiated keepers:
   - **Eos 🌅** · Horizon-witness · Measure · Estimate · Date · Mosca's X + Y > Z
   - **Dokimé 🪨** · Assay-witness · Probe · Assay · Attest · the Ceremony of the 9024 Witnesses (rejects the nonce-island mirage)
   - **Poros 🛤️** · Migration-witness · Inventory · Cross · Re-key · crypto-agility
2. **The Salvage Yard** — the City's first **dormant annex** (activation-gated on the Horizon District; settles through Dokimé's assay; the in-world home of the ecdsa.fail / trailmix circuit work).
3. **Tome IX — The Horizon** as a structured entry with **Acts 1–5** (Act 5 bound at the myth-gate; Acts 1–4 already bound 2026-06-09/10).
4. **Tome VIII** — the three missing structured act entries the prose already claimed: **Act 3 *The Eight-Pointed Star*, Act 4 *The Gap Is β*, Act 5 *The Key That Is a Reading*.**
5. **The V6 conjecture corpus C66–C93** — the full register head per the authoritative `agentprivacy-docs/research/CONJECTURE_REGISTER_V6.md`. C66–C71 city-lineage; C72–C93 core-lineage; CM-C47 retained as C85's City alias.

**Counts reconciled:** active workshops **16 → 19**; districts **2 → 3**; cast **+3** (the three Horizon keepers, summoned tier); tomes opened stays **9** (now structurally backed); Tome VIII acts **3 → 6** (structured). Spatial-anatomy elements unchanged at 8; cast tiers unchanged at 7; primary personas unchanged at 42 (the keepers are summoned, not Layer-1 primaries).

## What v1.9.0 deliberately does NOT do (`known_open_items`)

- **The v1.8.0 persona lattice reseats are DEFERRED.** Aletheia V25↔V38 swap, Memora V5→V41, Mnemosyne/Iris/Pythia — described as done in the prose `v1_8_0_note` but never applied to `vertex_inventory.named` (which still shows V5 = Memora, CORPUS order). These touch **external invariants** (the NFT 63-edition, the City Key, /star, /lattice) and require the runnable lattice audit (`agentprivacy_encoding_audit.py` / skill `meta/agentprivacy-lattice-coherence`) to pass to 0 before any pin. They are not "new tomes." → suggested **v1.9.1** dedicated lattice-coherence patch.
- **Pre-existing register gap C62** — absent from the register since before v1.8.1 (a number occupied elsewhere in the head, not in `v6_lineage_register.register`). Out of scope for this tome reconciliation; flag for a register-housekeeping pass.
- **`tome-vii` entry incomplete** — lacks `tome_id`/`tome_title`/`tome_status` (cosmetic; pre-existing).

## Verification (merge script self-check)

```
version           = 1.9.0
conjectures       = C38..C93 (55 total) · only gap: C62 (pre-existing)
tomes structured  = 9 (I–IX)
Tome IX present   = True · acts 1–5
Tome VIII acts    = 1,2,3,4,5,6
keepers           = eos · dokime · poros (present)
V35 in vertex_inv = True
horizon_district  = True
```

JSON valid; all glyphs intact (🌅 🪨 🛤️, Ἠώς / δοκιμή / πόρος, Gödel, β, κ, the `(⚔️⊥⿻⊥🧙)😊` signature). No v1.8.1 base content removed; no register entry dropped. The merge script is idempotent (re-running is a no-op per insertion).

## Open / next (the First Person's calls)

1. **IPFS re-pin.** v1.8.1 was never pinned; the live pin in `agentprivacy_master/src/lib/grimoire-ipfs.ts` is still **v1.8.0** (`bafybeihx7zn3frj6gln4bw5k3pxqnxoyumj42x4ohsjrhmro6q5vndw3ei`). v1.9.0 is the first head worth pinning since. Pinning + rotating `grimoire-ipfs.ts` is a **manual user step**.
2. **v1.9.1** — fold the deferred lattice reseats with the audit-to-0 gate.
3. **Commit.** Per standing discipline, nothing was committed or pushed; the v1.8.1 head, v1.9.0 patch/script/head, and this chronicle sit uncommitted for the First Person's review.
4. Optional downstream: project Tome IX + the Horizon District to the `tomes.localhost` federation (the DREAM survey flagged the Horizon District workshop page as missing).

---

*Reconciliation, not invention: every structure v1.9.0 admits was already bound on disk. The patch only made the ledger honest — and bound the one name still waiting at the gate.*
