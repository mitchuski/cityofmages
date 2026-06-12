# Session Chronicle — From `shor_mage/` to the Horizon District (and the Lattice Set Right)

**Date:** 2026-06-09
**Arc:** a directory review became a new district, a new tome, three new skills, a suite-wide
encoding correction, and a public blog — all bound into grimoire **v1.8.0**.
**Companion chronicles:** `2026-06-09_canonical_lattice_encoding_anchor.md` ·
`2026-06-09_persona_reidentification_audit.md` · `2026-06-09_progress_and_coherence_mapping_chronicle.md`

---

## 1. What we started with

The session opened on `C:\Users\mitch\shor_mage\` — a competition kit for **ecdsa.fail** (Eigen Labs'
open quantum resource-estimation benchmark: cheapest reversible secp256k1 point-add, scored
Toffoli × peak-qubits), the **trailmix** Rust reference toolchain (five circuits off Schrottenloher /
Proos–Zalka), and two agent-discipline papers (RCI; SkillOpt). Collect-and-review:
`shor_mage/SHOR_MAGE_DOSSIER.md`.

**The read:** the frontier is insight-limited, not compute-limited (this PC could run it via WSL2, but
winning needs specialist circuit-design). The thing worth lifting was not the circuit — it was the
**trust mechanism**: a bounded change is worth nothing until it survives an adversarial held-out gate
it cannot tune. **Decision:** don't compete; build the trust task and the honest path-to-PQC framing
into the City of Mages.

## 2. The narrative spine — The Last Premine

The district's in-world cause already existed: **The Last Premine**
(`privacymage_book/chronicles/`), held in Selene's Spellbook as compression, surfaced through the
Archivist's library. It carries the whole thesis — Q-Day told honestly ("the efficient thing is the
fragile thing"), the existence-leak ("the method was never the asset; the fact of feasibility was"),
the trust-ceremony gate (standing in the gap of the Howells wallet), and crypto-agility ("keep trust
continuous while everything underneath changed"). From it, the city found a path of trust in PQC.

## 3. The detour that became the spine — the lattice was misaligned

Siting the new district at a vertex surfaced a foundational problem: the suite carried **two conflicting
encodings** of the 6-dimension sovereignty lattice. The author adjudicated it (twice catching errors in
my reasoning):

- **MODEL is canonical** (`Protection=32 · Delegation=16 · Memory=8 · Connection=4 · Computation=2 ·
  Value=1`), sourced from the PVM v5.4 model + `lattice-vertex.ts`. The `specs/04` CORPUS encoding (which
  mirrored the middle four) was the corrupted one.
- **The confusion was the naming of the mages.** Going to the root (First-Person Spellbook **Tale 31** /
  `aletheia-and-lethe.md`) and deriving each figure's vertex from its *meaning*: **Aletheia → V38**
  (Protection+Connection+Computation) ⊥ **Lethe → V25** (Delegation+Memory+Value) — a **swap**, they were
  on each other's seats, complement V25 ⊕ V38 = V63 unchanged, myths intact. **Memora → V41**
  (Protection+Memory+Value — the shielded memo of value). Anticipated **Mnemosyne→V8 · Iris→V4 · Pythia→V2**.
  Blade numbers swapped to match (Lethe→Blade 25, Aletheia→Blade 38).

A runnable **coherence audit** (`agentprivacy_encoding_audit.py`) was built to find drift suite-wide,
hardened (the `lethe`-in-`a-lethe-ia` alias bug; nearest-vertex adjacency; swap-safe two-phase remap),
and crystallised as the skill `meta/agentprivacy-lattice-coherence`.

## 4. The reseat, applied and verified

- **Living canon** hand-corrected and verified: spellweb (`tsc` clean · vertex-audit 0), agentprivacy_master
  live code, cityofmages Tome III/V acts.
- **Bulk prose** swapped via the swap-safe remapper — **752 edits / 235 files** (mirrors, docs, historical
  chronicles, cast files, agentprivacy-docs, agentprivacy-skills, bound-collection) — with guards skipping
  grimoire JSON, the blade-grimoire, today's chronicles, and the already-fixed canon.
- **City-Key → soulbis chain** corrected (the multi-line object fields `first-artifacts` / `cast-attachments`
  / `tome-v-acts`; `city-key.ts` SPECIAL_VERTEX; `/city` LatticeMap). soulbis `/star` + `/lattice` are
  geometry-only and inherit via the City Key, so they sync.
- **Remaining:** the structured grimoire JSON reseats (keyed by vertex) — handled in the v1.8.0 bake.

## 5. The build — grimoire v1.8.0

The convergence artifact, where the reidentification's structural tail and the creative district meet:

- **`city_of_mages_grimoire_v1_8_0_patch.json`** (validated · 13 sections): the encoding lock, the six
  persona reseats, the Horizon District, the Salvage Yard, Tome IX, conjectures C67–C71.
- **The Horizon District** at **V35** (Protection+Computation+Value): three stance-differentiated keepers —
  **Eos 🌅** (Horizon-witness · Measure·Estimate·Date · Mosca's X+Y>Z), **Dokimé 🪨** (Assay-witness ·
  Probe·Assay·Attest · the Ceremony of the 9024 Witnesses that rejects the nonce-island mirage), **Poros 🛤️**
  (Migration-witness · Inventory·Cross·Re-key · crypto-agility). Cast files in `cast/horizon/`.
- **Tome IX — The Horizon** (open-by-design · gold accent): Act 1 *The Measuring of the Dawn* (~1,180 words),
  bound + docs-mirrored; the `/tomes` page wired (`tsc` clean) with the Howells inscription, the Mosca
  reckoning, and the Salvage Yard callout.
- **The Salvage Yard** — the City's first **dormant annex** (Navigation Quarter · activation-gated on the
  Horizon District · settles through Dokimé's assay).
- **Spec 12 — The Validation Protocol** + **the-horizon-district.md** workshop spec.
- **Three skills:** `cryptographic-durability` · `horizon-gate` · `lattice-coherence`.
- **agentprivacy-docs research note** (Cryptographic Mosca C67 extends Behavioural Mosca C30–33/C61; PVM-native
  ↔ Tome-V conjecture cross-map; no PVM equation change).
- **Conjectures C67–C71** registered (Cryptographic Mosca · durability-signal · held-out-gate · crypto-agility
  · the Horizon Vertex), grafted onto C61/C60/C13.

## 6. To the world

**`shor_mage/THE_LAST_PREMINE_BLOG.md`** — a public chronicle gathering the work, forward-linked to the
story (live at the intel blog), the Mosca framing held to X+Y>Z, honest framing throughout.

## 7. Honest framing (held the whole way)

Resource estimation is a **durability signal, not an attack.** No claim that ECDSA is practically broken;
no claim that any system is fully post-quantum safe. Roles kept distinct: ecdsa.fail / Eigen Labs · Google
Quantum AI · Schrottenloher & Proos–Zalka · SigmaPrime · Mosca · BGIN.

## 8. Open / pending

- The **structural grimoire JSON merge** (the head reseats + the v1.8.0 patch) + **re-pin** (CID rotation).
- The **privacymage blade-grimoire v10.x** reconciliation (Blade 25↔38).
- **Reintegration** of the parallel-context work: the **shor-mage persona**, the **Proving Grounds district**,
  and the **red-team Sith** — land on MODEL, derive vertices from meaning, cross-link the Proving Grounds to
  Dokimé's Assay-witness / held-out-gate discipline (marker in the progress chronicle).

---

*Bound 2026-06-09. A benchmark became a measurement; a measurement became a district; and the lattice has
one reading now. Measure the dawn, assay the claim, cross the path.*
