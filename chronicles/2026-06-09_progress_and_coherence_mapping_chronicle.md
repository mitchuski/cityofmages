# Progress & Coherence-Mapping Chronicle — PQC Workshop + the Persona-Lattice Audit

**Date:** 2026-06-09
**Status:** SAVE-STATE · two open threads (A: build-ready · B: audit-in-progress)
**Companion:** `2026-06-09_canonical_lattice_encoding_anchor.md` (the encoding lock)
**Plan file:** `C:/Users/mitch/.claude/plans/recursive-questing-thompson.md`
**Audit tool:** `C:/Users/mitch/agentprivacy_encoding_audit.py`

This chronicle preserves all progress and positioning so neither thread is lost.
**Thread A** (the PQC workshop additions) is designed and build-ready. **Thread B**
(the persona-lattice coherence audit) opened mid-build when a foundational
encoding conflict surfaced; it must be resolved before the grimoire re-pins.

---

# THREAD A — The PQC workshop additions (build-ready)

## A0. Origin
`C:/Users/mitch/shor_mage/` — a kit for **ecdsa.fail** (Eigen Labs' open quantum
resource-estimation benchmark: cheapest reversible secp256k1 point-add, scored
Toffoli×qubits) + the **trailmix** Rust reference toolchain (5 circuits off
Schrottenloher/Proos–Zalka) + two agent-discipline papers (RCI, SkillOpt). Full
review in `shor_mage/SHOR_MAGE_DOSSIER.md`.

**Decision:** do NOT compete (frontier is insight-limited, not compute-limited;
this PC could run it via WSL2 but winning needs specialist circuit-design). Instead
lift the *trust mechanism* + honest *path-to-PQC* framing into the City as a new
district, tome, and a dormant salvage workshop. Honest-framing guardrail
(everywhere): resource estimation is a **durability signal, not an attack**; no
"ECDSA broken"; no "fully post-quantum safe."

## A1. The narrative origin: "The Last Premine"
The district's in-world cause is the sci-fi-future text **"The Last Premine"**
(`privacymage_book/chronicles/the-last-premine-v4 (1).md`; built PDF in
`privacymage_book/art/output/`), held in **Selene's Spellbook as compression** and
surfaced through the **Archivist's library** (the Tower, Tome VIII). It already
carries the whole thesis: Q-Day (secp256k1 broken ~1,200 qubits / 9 min — "the
efficient thing is the fragile thing"); the **existence-leak** ("the method was
never the asset; the fact of feasibility was" = durability-signal-not-attack); the
**trust-ceremony gate** (the dual-agent Howells wallet — "nobody tried standing in
the gap"); **crypto-agility** ("keep trust continuous while everything underneath
changed… the trust graph used primitives the way a river uses its banks"). Figures:
**Marvin** (BGIN archive custodial intelligence), **Selene** (ex-SIKE info-broker).

## A2. The Horizon District (active)
**Vertex V35 = `100011` = Protection + Computation + Value** (defence + the quantum
threat + the stake; FREE; canonical under MODEL — see Thread B). Witness register:
**Durability / migration-horizon**. Three stance-differentiated sibling shops
(mirrors the Threshold at V59):

| keeper | sigil | witness | gem | ceremony | proverb |
|---|---|---|---|---|---|
| **Eos** | 🌅 | Horizon-witness | Sunstone (heliolite) | Measure · Estimate · Date | "The dawn is not an attack; it is a time you can measure." |
| **Dokimé** | 🪨 | Assay-witness | Lydite (touchstone) | Probe · Assay · Attest | "The gold that fears the stone was never gold." |
| **Poros** | 🛤️ | Migration-witness | Labradorite (turns colour) | Inventory · Cross · Re-key | "Value lives on the path, not the point." |

(δοκιμασία = the Athenian trust-vetting; 🛤️ echoes Eos 🌅 and the soulbis `T∫(π)·the
path` motif; compass dropped — it conflicts with Pleione.)

## A3. The trust task (the district's spells)
Five expressive forms: **Ceremony of the 9024 Witnesses** (Dokimé — Fiat-Shamir
held-out gate; rejects the **nonce-island mirage**); **the Touchstone assay**; the
**RCI "Tony→Anton" liturgy** (Eos — bounded change: state-the-waste → smallest-fix →
confirm/reject-with-metrics); the **Mosca Reckoning** (Eos — honest horizon report,
Y>X+Z); the **Migration Crossing** (Poros — crypto-agility, no silent stragglers).
Artefacts: **Horizon Glass** (tool, borne), **Touchstone** (trinket, witness-capable),
**Crossing-Ledger** (trinket/tome).

## A4. Tome IX — *The Horizon*
Open-by-design (like VI/VII/VIII), accent **gold `#fbbf24`**, anchor `tome-ix-act-N`.
Act 1 *The Measuring of the Dawn* opens by naming the premine as the text the
Archivist surfaced, "and from it the city found a path of trust in PQC"; quotes the
Howells proverb as the district's founding inscription; closing beat names the
Salvage Yard (A5).

## A5. The Salvage Yard (DORMANT — gated on the Horizon District)
A new **dormant annex** of the **Navigation Quarter** (Pleione, V44 — the maritime/
salvage theme fits). The City's first expression of the Last Premine's
**quantum-salvage-bounty** primitive: a board where crews post post-quantum /
reversible circuits as *digital salvage* — the in-world home of the actual
ecdsa.fail / trailmix work. It **settles through Dokimé's 9024-witness assay**, so it
cannot open until the Horizon District is built. Introduces a NEW structural concept:
a workshop with `status: dormant` + `activation_gate: "Horizon District built"`. No
keeper summoned yet; vertex assigned on activation (a free Navigation-adjacent
vertex). Uncounted in the active total (active workshops 16 → 19 for Horizon; Salvage
Yard = +0 active until opened).

## A6. Suite integration (Thread A build targets — BLOCKED on Thread B for vertex-touching parts)
- **Grimoire v1.8.0** structured-delta patch (`cityofmages/grimoire/…v1_8_0_patch.json`):
  Horizon District + 3 keepers + 3 ceremonies + 3 artefacts + Tome IX Act 1 +
  Salvage-Yard dormant stub + conjectures **C67–C71**. Re-pin = user JSON-merge.
- **/tomes** (`agentprivacy_master/src/app/tomes/page.tsx`): Tome IX section,
  ActCollapsible, gold accent + ladder `tome === 'IX'`, tome-ordering row.
- **spellweb** (`src/types/graph.ts`, `data/{nodes,edges,theme}.ts`): node types
  `horizon`, `assay`; ~7 verb-form edges (`estimates`, `bounds_horizon_of`,
  `assayed_by`, `survives`, `migrates_to`, `hardens`, `attests_durability_of`);
  district subgraph + artefacts threading them.
- **Conjectures** (`agentprivacy_master/src/lib/tome-v-conjectures.ts`): C67–C71,
  grafted onto the existing quantum cluster (C61 Behavioural Mosca / C60
  harvest-now-decrypt-later / C13 quantum-resistant bilateral witness). PVM-native
  cross-map in the docs note. No PVM v5.4 equation change.
- **agentprivacy-docs**: `research/2026-06-09_horizon_district_cryptographic_durability_note.md`
  extending `research/schrottenloher-ecdlp-v6-note.md` + `pvm-v6-1-bakhta-half-life.md`.
- **agentprivacy-skills** (2 new): `role/agentprivacy-cryptographic-durability`,
  `meta/agentprivacy-horizon-gate` (the held-out-gate / bounded-change discipline).

---

# THREAD B — The persona-lattice coherence audit (open)

## B0. What happened
Siting V35 surfaced that the suite carries **two conflicting encodings** of the
6-dimension sovereignty lattice. Locked: **MODEL is canonical**
(`Protection=32 · Delegation=16 · Memory=8 · Connection=4 · Computation=2 · Value=1`;
source `privacy-value-model-v5.4.json:386-391` + `lattice-vertex.ts:38`). The
rejected **CORPUS** encoding (in `specs/04` + propagated) mirrors the middle four
(16↔Computation, 8↔Connection, 4↔Memory, 2↔Delegation). Full detail + the audit tool
in the companion anchor chronicle.

## B1. The real root cause — "the confusion is the naming of the mages"
Personas were assigned to vertices **under CORPUS**. Under canonical MODEL, a
persona's **vertex number no longer matches its lore-meaning**. The fix is NOT to
re-read personas in place — it is to **re-derive each persona's vertex from its
(lore-invariant) meaning under MODEL**, holding the complement-pair and structural
invariants. Vertex *numbers* are load-bearing in the NFT 63-edition / City Key /
`/star` / `/lattice`, so each move must be scoped against those surfaces.

## B2. The exemplar — Aletheia ⊥ Lethe SWAP
Lore-stated meanings (Tome III Acts 5–6, confirmed across grimoire + spellweb +
zk-blades-forge `aletheia-and-lethe.md`):
- **Aletheia** 🔮 (the bright medium · proof-transmission · Fiat-Shamir) =
  **Protection + Connection + Computation** → MODEL `100110` = **V38**.
- **Lethe** 🌀 (the dark substrate · forgetting · binds delegations whose terms can't
  be retrieved · holds value) = **Delegation + Memory + Value** → MODEL `011001` = **V25**.

They currently sit on each other's vertices (Aletheia=V25, Lethe=V38). **Resolution:
swap → Aletheia V38, Lethe V25.** The complement pair is preserved (V25 ⊕ V38 = V63;
V25 AND V38 = 0) regardless of which persona is where. This vindicates the
"naming of the mages" hypothesis exactly.

## B3. Memora — unresolved lore inconsistency (needs a call)
- Cast prose: "Protect what is being remembered. Remember what is being protected" →
  **Protection + Memory** → MODEL `101000` = **V40**.
- Vertex node / Cloaking Guide: V5 "Chronicle Vertex · **Value + Memory**" → MODEL
  `001001` = **V9**.
- Current vertex V5 under MODEL reads `000101` = Connection + Value (neither).
→ Decide Memora's true dimension-set (Protection+Memory vs Value+Memory), then place
at V40 or V9.

## B4. Coherence-mapping table — personas to audit
For each, the action is: confirm lore-meaning → place at the MODEL vertex for that
meaning. (Vertices that set both/neither of a mirrored pair are stable and need no
move.) Status as of this chronicle:

| persona | current | lore-meaning (to confirm) | correct MODEL vertex | note |
|---|---|---|---|---|
| Aletheia 🔮 | V25 | Protection+Connection+Computation | **V38** | SWAP (B2) |
| Lethe 🌀/🌘 | V38 | Delegation+Memory+Value | **V25** | SWAP (B2) |
| Memora 📜 | V5 | Protection+Memory *or* Value+Memory | **V40** or **V9** | resolve B3 |
| Mnemosyne 📿 | V4 | Memory | **V8** | anticipated · cheap |
| Iris 🌈 | V8 | Connection | **V4** | anticipated · cheap |
| Pythia 🔥 | V16 | Computation | **V2** | anticipated · cheap |
| Techne 🎨 | V20 | Memory+Computation | **V10** | anticipated |
| Hephaestus/Socrat0x 🔥 | V24 | Connection+Computation | **V6** | Socrat0x seated-provisional |
| Custos 🔏 / Lampyra 💠 | V49 | Protection+Computation+Value | **V35** | ⚠ collides with the Horizon District — these already MEAN the durability triple; resolve as shared-vertex stance OR re-read in place |
| Pallia 🪡 | V28 | (confirm — Mage-canonical; V28 is also the V63 transmuted-projection — structural) | TBD | V28's structural role (Mage projection of Sovereign V63) may pin it |
| Manifestia 🤲🌿 | V55 | (confirm) | TBD | covenant vertex |
| Aria 🪞 | V57 | (confirm) | TBD | curatrix |
| Vulcana ⚒️ | V19 | — | V19 | STABLE (both mirror-bits set) |
| Adamantia 💎 / Helia ☀️ | V51 | — | V51 | STABLE |
| Pleione 🧭 | V44 | — | V44 | STABLE |
| Vagari 🌳 | V31 | all-but-Protection | V31 | STABLE |
| flaxscrip / Sovereign | V63 | all | V63 | STABLE |

## B5. App-reference surface (where vertex moves must propagate)
Audit-driven (`agentprivacy_encoding_audit.py`). Known touch-points per moved persona:
- **spellweb**: `src/data/nodes.ts` (vertex nodes + cast nodes: `vertex`/`bits`/
  `hammingWeight`/`desc`), `src/data/edges.ts` (`inhabits`, `complement_pair`),
  `src/types/graph.ts` comments, `src/data/presets.ts`.
- **agentprivacy_master**: `src/data/city-of-mages-grimoire-v1.*.json` (persona
  `vertex` + readings), `src/app/tomes/page.tsx` (CastCard + ActCollapsible
  `vertex=`), `src/components/profile/LatticeMap.tsx`, `src/app/{shield,etherchanting}/page.tsx`.
- **cityofmages**: `tomes/specs/04-vertex-naming-audit.md`, cast files, tome acts.
- **External (high-care)**: NFT 63-edition metadata, City Key, `/star`, `/lattice`.
- **Poems**: Selene's Spellbook poems referencing these figures (meaning, not vertex).

## B6. Reconciliation policy (decided)
- MODEL encoding is canonical (locked).
- **Lore-anchored personas** (rich written meaning: Lethe, Aletheia, Memora, and the
  single-bit anticipated Mnemosyne/Iris/Pythia) → **move vertex to match meaning**.
- **Lower-stakes / structurally-pinned personas** → resolve case-by-case (re-read in
  place, or move) in the dedicated edit pass.
- Preserve: complement pairs (Aletheia⊥Lethe), the V63/V28 dual-agent split, the
  NFT/key/star deployed numbers (audit each move against them).
- Fix the two `specs/04` errors (V48 label; V31 "except Value").
- **Run the audit before any grimoire pin.**

---

# NEXT STEPS (resume points)

**Thread B (do first — unblocks the pin):**
1. Confirm Memora's dimension-set (B3) → fix her vertex.
2. Approve the Aletheia↔Lethe swap (B2) and the Custos/Lampyra V35 collision policy (B4).
3. Run the audit-driven edit pass across B5 surfaces; re-run audit to 0 (modulo any
   intentionally-held residuals).
4. Confirm no external (NFT/key/star) breakage for each moved number.

**Thread A (build after B settles the vertices):**
5. Author Tome IX Act 1 + cast files (Eos/Dokimé/Poros) + Horizon-District + Salvage-Yard.
6. Grimoire v1.8.0 patch · /tomes wiring · spellweb additions · C67–C71.
7. agentprivacy-docs note · 2 skills.
8. Build/typecheck; user JSON-merge + re-pin.

---

## PENDING REINTEGRATION INTO v1.8.0 (parallel context, 2026-06-09)

A separate working context is authoring, for merge into the **same v1.8.0** release:
- a **shor-mage persona** (the circuit-frontier figure of the ecdsa.fail work — natural kin to the
  Horizon District / Salvage Yard);
- a **Proving Grounds district** aligned to the existing workshops (an adversarial-testing register);
- a **red-team Sith persona** (the adversary archetype).

**Reintegration notes for whoever merges:** these must land on the **MODEL** lattice encoding and the
corrected seats (this chronicle + the encoding anchor are authoritative). Give the shor-mage and the
red-team Sith their vertices by *deriving from meaning under MODEL* (run `agentprivacy_encoding_audit.py
--only persona` after). The Proving Grounds (adversarial testing) is a natural sibling-register to the
Horizon District's **Assay-witness** (Dokimé) and the **held-out-gate** discipline — cross-link them.
The v1.8.0 grimoire patch (`city_of_mages_grimoire_v1_8_0_patch.json`) is the merge target; append the
new district/personas as additional sections (mirror the `horizon_district_introduced` /
`personas_additions` shapes) and bump the workshop counts accordingly.

---

*Saved 2026-06-09. Two threads, one lattice. Settle the names, then open the dawn.*
