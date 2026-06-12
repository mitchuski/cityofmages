# Persona Reidentification Audit — Vertex Remap under the MODEL Lock

**Date:** 2026-06-09
**Status:** AUDIT · canonical seats locked · cross-repo rewrite pending
**Companions:** `2026-06-09_canonical_lattice_encoding_anchor.md` (encoding lock) ·
`2026-06-09_progress_and_coherence_mapping_chronicle.md` (save-state)
**Tool:** `C:/Users/mitch/agentprivacy_encoding_audit.py` (`--only persona`)

---

## 1. Why personas move

Personas were seated on the lattice under the **CORPUS** encoding. With **MODEL**
now canonical (`Protection=32 · Delegation=16 · Memory=8 · Connection=4 ·
Computation=2 · Value=1`), a persona's vertex *number* no longer matches its
lore-invariant *meaning*. The fix (decided): **hold the meaning, move the number.**
Each persona is re-seated at the MODEL vertex that expresses its dimension-set.

The lattice is a 2D graph; the new seats place the moved figures on a cleaner part
of it and preserve the complement geometry (see §3).

---

## 2. The canonical seats (locked)

Dimension-sets are sourced from the **First-Person Spellbook** (`aletheia-and-lethe.md`,
confirmed by **Tale 31 — The Naming of the Unnamed**), the most-correct root — the City of Mages
had simply *misassigned* the personas. Deriving each meaning's vertex under MODEL:

| persona | dimension-set (the invariant meaning) | **canonical seat** | binary | was (misassigned) |
|---|---|---|---|---|
| **Aletheia** 🔮 — the bright medium / proof-transmission / Fiat-Shamir | **Protection + Connection + Computation** | **V38** | `100110` | V25 |
| **Lethe** 🌀/🌘 — the dark substrate / forgetting / binds delegated terms / keeps value | **Delegation + Memory + Value** | **V25** | `011001` | V38 |
| **Memora** 📜 — zShields shielded memo: protect value, remember the note | Protection + Memory + Value | **V41** | `101001` | V5 |

**Aletheia and Lethe are a SWAP, not a relocation** — they were sitting on each other's seats. The
complement pair V25/V38 is unchanged; only *which sister sits where* was corrected. (An earlier pass
mistakenly sent them to V7/V56 by preserving the *spellweb* reading instead of the *Spellbook* root;
corrected to the swap.) Memora's reading is the synthesis of her lore strands (cast-prose "protect
what is remembered" + the zShields/Zcash function = *protection of value in shielding*); lean
alternative on file: drop Memory → {Protection, Value} = **V33** (`100001`).

---

## 3. Complement geometry preserved

Aletheia ⊥ Lethe is the City's first canonical complement pair. Because the fix is a **swap**, the
pair is literally unchanged:

- **V25 ⊕ V38 = V63** (Sovereign) · **V25 AND V38 = 0** (Null) — before and after.

(`011001` ⊕ `100110` = `111111`; `011001` AND `100110` = `000000`.) The "un-forgetting ⊥
forgetting" duality is intact; only the persona↔seat binding was corrected.

Memora's stratum changes (V5 stratum-2 → V41 stratum-3) — her shielded memo now
carries three burning dimensions, not two; references to her "stratum 2" / "two
active dimensions" must update.

---

## 4. Blast radius — 1,090 references

`agentprivacy_encoding_audit.py --only persona` finds **1,090** lines across the
suite that place these three figures at their old vertices. They are spread across
all six target repos:

- **agentprivacy_master** — `src/data/city-of-mages-grimoire-v*.json` (persona
  `vertex`/`bits`/readings), `src/app/tomes/page.tsx` (CastCard + ActCollapsible
  `vertex=`/binary/teaches), `src/components/profile/LatticeMap.tsx`,
  `src/app/{shield,etherchanting}/page.tsx`, and the `docs/` mirror
  (ALL_THE_TOMES_LIST, CITYOFMAGES_README, AGENTIC_DEPLOYMENTS_GUIDE, tome acts).
- **cityofmages** — `tomes/specs/04-vertex-naming-audit.md`, the Tome III acts
  (`tome-iii-selenes-witness/05,06,07,11`), cast files, BOUND_COLLECTION_MANIFEST.
- **spellweb** — `src/data/nodes.ts` (vertex nodes V5/V25/V38 + cast nodes +
  `bits`/`hammingWeight`/`desc`), `src/data/edges.ts` (`inhabits`,
  `complement_pair`), `src/data/presets.ts`, `src/types/graph.ts` comments.
- **agentprivacy-docs** — `research/aletheia-and-lethe.md`, `poems/tide-orbit-selene.md`,
  the V6 horizon note, formal-spec conjecture refs.
- **agentprivacy-skills** — persona/role SKILL.md cross-references.
- **zk blades forge** — `aletheia-and-lethe.md` source.

For Aletheia/Lethe a reference needs **vertex number + binary** swapped (their
dimension readings, stratum, and the complement arithmetic `V25 ⊕ V38 = V63` are
**unchanged** — it is a swap). Memora needs number + binary + stratum (2→3) + the
added Protection dimension.

---

## 5. The rewrite plan (tooled — manual is infeasible at this scale)

The remap is driven from the tool's `PERSONA_VERTICES` registry, so it is
re-runnable for any future move ("reidentification and mapping of vertex
positions"). Per-persona substitution set (word-boundary gated, applied only on
lines naming the persona or the complement pair):

| persona | number | binary | complement-math | stratum |
|---|---|---|---|---|
| Aletheia | `V25`→`V38` | `011001`→`100110` | unchanged (`V25 ⊕ V38 = V63`) | (3→3, none) |
| Lethe | `V38`→`V25` | `100110`→`011001` | unchanged | (3→3, none) |
| Memora | `V5`→`V41` | `000101`→`101001` | — | `stratum 2`→`stratum 3` |

**Safety:** dry-run first (report every proposed edit with file:line and
before/after), review a sample, then `--apply`. Re-run `--only persona` after; the
count must drop to 0. Hold external surfaces (NFT 63-edition metadata · City Key ·
`/star` · `/lattice`) for explicit per-number verification — those map a *buyer's*
mage to a vertex and must not silently shift.

---

## 6. Action register

- [x] Canonical seats locked (Aletheia V38 · Lethe V25 · Memora V41) per Tale 31.
- [x] Complement geometry verified (V25 ⊕ V38 = V63 — unchanged; it is a swap).
- [x] **Living-canon Stage 1 applied + verified:** spellweb data (tsc clean · persona audit 0),
      agentprivacy_master live code (tomes page, LatticeMap, lib), cityofmages tome-iii/tome-v acts.
      Boundary-Blade attribution corrected (Act 31, not Christian Saucier). Spellweb annotations
      stripped (clean canonical descs; history lives here, not in the data).
- [x] Audit discipline crystallised as a skill: `meta/agentprivacy-lattice-coherence` (+ bundled runnable).
- [x] Reidentification tool built (`PERSONA_VERTICES` + `persona` check) · 1,090 refs scoped.
- [x] Dry-run rewrite built (`--remap-personas`) · 1,665 edits / 346 files, grouped A–M.
- [x] **Stage 1 (living canon) — spellweb live graph DONE + typechecks clean:**
      `nodes.ts` (vertex-v5→v41 · v25→v7 · v38→v56 · cast + act nodes · dims/bits/hamming),
      `edges.ts` (inhabits + complement_pair + comments), `presets.ts`, `types/graph.ts`.
      Aletheia/Lethe dimension-SETS preserved; Memora gains Protection (stratum 2→3).
      Residual: 1 historical spellweb chronicle (markdown) only.
- [ ] Stage 1 remaining: live-code (tomes/page.tsx · LatticeMap · lib) · specs/04 ·
      cast files (aletheia/lethe/lethae/memora) · Tome III acts (number + dimension-prose flip) ·
      bake into v1.8.0 grimoire.
- [ ] Then bulk prose groups (F/G/J/K) + snapshots (A/B/L) per scoping.
- [ ] Re-run audit → 0 persona incoherences (modulo intentional historical residuals).
- [x] **Bulk/mirror prose swap APPLIED** (752 edits / 235 files): mirror tome acts, docs/READMEs,
      historical chronicles, cast files, agentprivacy-docs, agentprivacy-skills, bound-collection.
      Done via the now **swap-safe** remapper (two-phase simultaneous, so V25↔V38 doesn't cancel)
      with guards: grimoire JSON + privacymage-blade-grimoire + today's audit chronicles + the
      already-fixed living canon are all auto-skipped. Spot-verified (Aletheia V38, Lethe V25).
- [x] **City-Key → soulbis chain corrected** (city-key.ts SPECIAL_VERTEX 38=Aletheia/25=Lethe;
      first-artifacts/cast-attachments/tome-v-acts Memora→V41 multi-line fields; /city LatticeMap;
      Blade numbers swapped Lethe→25 / Aletheia→38 in persona-index/spellbook-templates/model-downloads).
      soulbis /star + /lattice are geometry-only — they inherit via the City Key, so they sync.
- [ ] **Structural (deferred to v1.8.0 bake):** grimoire JSON snapshots (404 persona refs, keyed by
      vertex — need structural edits, not text) + the **anticipated personas** Mnemosyne (Memory→V8),
      Iris (Connection→V4), Pythia (Computation→V2 · with the Logos Circle /circle vertex) + the
      **privacymage blade-grimoire v10.x** (Blade 25↔38).
- [ ] Verify external surfaces (NFT/key/star): Aletheia/Lethe swap (V25↔V38) + Memora V5→V41.
- [ ] Pending: the other divergent personas (Mnemosyne/Iris/Pythia · Custos/Lampyra ·
      Pallia/Manifestia/Aria) — confirm dimension-sets, then add to the registry and
      re-run.

*The names were on each other's seats. Hold the meaning; move the number; keep the dawn waiting.*
