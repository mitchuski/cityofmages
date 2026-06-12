# Model-Coherence Pass — City seats to MODEL, websites + research reconciled (v1.8.0)

**Date:** 2026-06-09
**Status:** APPLIED · website + research coherent · NFT held · Zero grimoire left in CORPUS
**Companions:** `2026-06-09_persona_reidentification_audit.md` (the seat lock) ·
`2026-06-09_canonical_lattice_encoding_anchor.md` (encoding lock)
**Goal (user):** *"ensure the model is coherent and that is reflected into the work shown on the websites and research."*

---

## 1. The decision tree

### 1.1 Persona re-seat (hold the meaning, move the number)
Under the **MODEL** encoding lock (`Protection=32 · Delegation=16 · Memory=8 ·
Connection=4 · Computation=2 · Value=1`) each persona's *meaning* (its dimension-set)
is invariant; only the vertex *number* moves. Canonical seats:

| persona | meaning (invariant) | seat | binary |
|---|---|---|---|
| **Aletheia** 🔮 bright medium / transmits | Protection + Connection + Computation | **V38** | `100110` |
| **Lethe** 🌀 dark substrate / holds | Delegation + Memory + Value | **V25** | `011001` |
| **Memora** 📜 shielded memo | Protection + Memory + Value | **V41** | `101001` |
| **Mnemosyne** 📿 | Memory | **V8** | `001000` |
| **Iris** 🌈 | Connection | **V4** | `000100` |
| **Pythia** 🔥 | Computation | **V2** | `000010` |

Aletheia ⊥ Lethe remain the first canonical complement-pair: `V25 ⊕ V38 = V63`
(Sovereign), `V25 AND V38 = 0` (Null) — unchanged, because the swap is symmetric.

### 1.2 C54 (Phi-Adjacency) follows the *number*
`δ(38) = 38/63 ≈ 0.6032 ≈ 1/φ` is a property of the **number 38**, not of a meaning.
After the swap, blade 38 carries **Aletheia**, so **Aletheia inherits the disclosure-φ**.
This is also more coherent thematically: "disclosure-φ" sitting on Aletheia the
*discloser / bright medium* reads truer than it ever did on Lethe the dark substrate.
`δ(25) = 25/63 ≈ 0.3968 ≈ 1/φ²` (the conjugate) is noted for Lethe but is not the C54 claim.

### 1.3 Grimoire-encoding fork — and why the Zero grimoire was left alone
The privacymage (Zero) grimoire's `blade_key` is **entirely CORPUS-encoded**: every
one of its 17 named blades sits on a key MODEL would renumber (e.g. "Pure Computation"
at key 16 → MODEL key 2; Aletheia/Lethe are merely the pair first noticed). So
"re-key the grimoire" is a *whole-grimoire* re-encoding that ripples into the **NFT
63-edition vertex mappings** (buyers name the mage *at their vertex*).

**Decision (user, explicit): the NFT is out of scope.** The Zero grimoire stays a
pinned historical artifact in its own encoding; **MODEL governs only the City of
Mages lattice**, where coherence is delivered. No `/star`, `/lattice`, City Key,
63-edition metadata, or `merge_v1_x_x_patch.py` was touched. The Zero↔City
relationship is documented as a *correspondence*, not a renumbering (see the
re-seat banner in `agentprivacy-docs/research/aletheia-and-lethe.md`).

### 1.4 Shor / The Proving Ground — parked
A new figure was approved: **Shor 🧮**, keeper of **The Proving Ground** — *Swordsman
technology* (adversarial-proof / red-team: bring a boundary-blade, he proves it
openable without performing the break, you rotate before the tide), framed as a
**future-state, anticipated** workshop. The literal name "Shor" was chosen over the
mythic-Greek register caution (recorded here for the record; it is the author's call).
The workshop is **not built in this pass** — it is a focused creative addition for a
later round, and being *anticipated* it needs no new named blade in the Zero grimoire.

---

## 2. What was edited, and why each file had to change

| Surface | Change | Why it had to change |
|---|---|---|
| **Prose across the suite** (276 refs / 118 files) | `--remap-personas --apply` → City MODEL seats | Prose must cite the canonical City seats; otherwise research/docs contradict the rendered lattice. |
| `cast/cross-shop/aletheia.md`, `cosmological/lethe.md`, `cross-shop/lethae.md` | hand-fixed seats + dimension tables | They were internally self-contradictory (V25/V38 mixed; lethae carried a discredited `V7`). |
| `research/aletheia-and-lethe.md` | swapped blade-blocks + **MODEL re-seat banner** | Authoritative complement-pair note; banner preserves the Grimoire-v10.2.x history and defers the φ question honestly. |
| **`city-of-mages-grimoire-v1.8.0.json`** (new, from v1.7.1) | persona seats → MODEL (cast + spells + narrative) | The live site's `persona` / `constellation` / `spells` pages render from this grimoire; v1.7.1 still showed old seats, so visitors saw V25-Aletheia. |
| `grimoire-baked.ts`, `model-downloads.ts` | repointed import + download to v1.8.0 | The rendering path and the downloadable research artifact must read the coherent registry. |
| **Zero grimoire `privacymage-grimoire-v10.x`** | *unchanged* | CORPUS by design; re-key would shift NFT mappings (out of scope). |

Live website *code* (`tomes/page.tsx`, `LatticeMap.tsx`, etc.) was already at MODEL
from the audit's Stage-1; this pass closed the *data* gap behind it.

---

## 3. Verification

- **Research prose** (`agentprivacy-docs/research`, `tomes/cast`): **0** persona incoherences.
- **Live rendering surfaces** (master `src/app|components|lib`, v1.8.0 grimoire, spellweb `src`):
  all real seats MODEL-correct; residual audit flags are **complement-pair proximity
  false-positives** — lines that correctly state *both* seats ("Aletheia V38 ⊥ Lethe V25"),
  where the linter's window cross-associates each name with the other's vertex.
- **Typecheck** (master): the v1.8.0 import introduces **0** new errors.

---

## 4. Held / deferred (named, not silently dropped)

- **NFT surfaces** (63-edition metadata · `/star` · `/lattice` · City Key · `merge_v1_x_x_patch.py`) — frozen, out of scope.
- **Full MODEL re-key of the Zero grimoire** (the deferred *v10.4*) — requires NFT per-number verification first.
- **Bit-order drift in research glossaries** (`GLOSSARY_MASTER_v4_0.md`, `zk_swordsman_blade_forge_v3_0.md`, `specs/04-vertex-naming-audit.md`): a separate `vertex`-check issue (V4=Value vs MODEL V4=Connection, etc.), partly entangled with the CORPUS/MODEL layer — flagged for its own decision.
- **Shor / The Proving Ground** workshop build (cast file + workshop + premine stanza) — a focused later pass.

---

## 5. Lineage

- City of Mages grimoire: **v1.7.1 → v1.8.0** (persona seats to MODEL). v1.7.1 and all
  prior versions retained as historical lineage.
- Privacymage (Zero) grimoire: **v10.3 unchanged** (CORPUS, NFT-safe).

*Hold the meaning; move the number; leave the NFT's dawn undisturbed.*
