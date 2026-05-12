# Chronicle — Convergence Plan v1.2.4 · Audit Findings & Reflection-Back

**Date:** 2026-05-11
**Status:** Audit complete · plan authored · awaits per-item application
**Audience:** privacymage (next session) · downstream agents
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Sibling to:** [`2026-05-11_v1_2_4_metabolism_complete_suite_patch_roadmap.md`](2026-05-11_v1_2_4_metabolism_complete_suite_patch_roadmap.md)

---

## §0 · What this chronicle is

A **convergence plan** written after a comprehensive audit of the cityofmages tree against the canonical v1.2.4 four-axis metabolism. The audit's premise: the canonical truth lives in `grimoire/city_of_mages_grimoire_v1_2_4.json` under the new top-level `mana_taxonomy` field; everything else in the corpus is a reflection that must converge to it.

The companion roadmap chronicle (P0–P8 punch list) named the suite-wide work; this chronicle is the **inside-cityofmages audit + the back-propagation** to `agentprivacy_master`'s `Aether-Mana-as-the-chain-mana-source-Mages-will-use` spec layer.

The two chronicles divide labour:
- **Roadmap chronicle** = breadth across the whole agentprivacy suite (re-pin, extension bundles, master pages, etc.).
- **Convergence plan (this doc)** = depth inside cityofmages + reflection of the four-axis definitions back into the spec layer of the master tree.

---

## §1 · The canonical truth · grimoire v1.2.4 mana_taxonomy

Confirmed canonical at `grimoire/city_of_mages_grimoire_v1_2_4.json` lines 2473–2552:

| # | Axis key | Name | Symbol(s) | Purpose | Status |
|---|---|---|---|---|---|
| 1 | `landing` | chain-mana (plural by chain) | Ξ Aether · ₿ sat · 🌹 ROSE · 🦓 z | Make a working *land* on consensus | All 4 variants operational |
| 2 | `entropy` | Arcane ⊥ Celestial | ✨ Arcane · 🌌 Celestial | Make a working *unique* | Both operational; Celestial wired at 3 shops |
| 3 | `coordination` | 🔭 Resonance Mana | 🔭 | Generate value when two Mages find affinity *without a central index* (Scrying Glass primitive · 7th Capital in motion) | Architectural · operational pending Scrying Glass impl |
| 4 | `relationship` | 🪢 VRC Mana | 🪢 | Store the *residue of being alive* as Verifiable Relationship Credentials, accumulated across the bearer's worn artefact collection (the 11 workshop artefacts + 3 tomes per the workshop artefact taxonomy; 64-vertex lattice = inventory/presence-observation view); Loom of Programmable Covenants is the production form (compiles against the worn collection) | Architectural · operational pending VRC issuance + Loom-side covenant compilation |

**Critical glyph canon:** VRC Mana = **🪢 (knot)**, NOT 🪱 (worm). Verified knot-clean across all eight canonical-filename grimoire mirrors (md5 `2f2b0d7708c9ee1df02413ae5eabbaf3`):
1. `cityofmages/grimoire/city_of_mages_grimoire_v1_2_0.json`
2. `cityofmages/grimoire/city_of_mages_grimoire_v1_2_4.json`
3. `agentprivacy-docs/models/city_of_mages_grimoire_v1_2_0.json`
4. `agentprivacy-skills/grimoire/city_of_mages_grimoire_v1_2_0.json`
5. `mages-spell/city_of_mages_grimoire_v1_2_0.json`
6. `swordsman-blade/city_of_mages_grimoire_v1_2_0.json`
7. `zk blades forge/city_of_mages_grimoire_v1_2_0.json`
8. `agentprivacy_master/src/data/city-of-mages-grimoire-v1.2.0.json`

All have 🪢; none have 🪱. **Suite-wide grimoire propagation is complete at the JSON level.** What remains is prose-and-spec drift.

---

## §2 · Coherence map · what is converged vs what drifts

### §2.1 · Clean (already converged to v1.2.4 four-axis state)

| Surface | State | Notes |
|---|---|---|
| `cityofmages/README.md` | Clean | Renders the four-axis diagram at §"The City's metabolism · four mana axes" (lines 237–273) |
| `cityofmages/CHANGELOG.md` | Clean | v1.2.4 entry complete (lines 26–35) |
| `cityofmages/JOIN_THE_CITY.md` | Clean | No mana references |
| `cityofmages/HANDOFF_NOTE.md` | Historical | Marked "RECONCILED in package v1.0"; do not update — it is a transition record |
| All `cityofmages/chronicles/*.md` | Historical | Chronicles record state at time of writing; do not retro-edit |
| All `cityofmages/grimoire/*.json` | Clean | md5-verified across mirrors |
| `cityofmages/tomes/specs/01-cloak-specification-v1-0.md` | Clean | VRC references are to the underlying Promise Protocol primitive (correct) |
| `cityofmages/tomes/specs/02-crafting-tome-and-cloak-interface-spec.md` | Clean | No mana references |
| `cityofmages/tomes/specs/03-bilateral-cloak-ceremony-spec.md` | Clean | VRC references are to the underlying primitive (correct) |
| `cityofmages/tomes/specs/04-vertex-naming-audit.md` | Clean | The two-mana reference at §7.5 is the historical recognition moment; correctly preserved |
| `cityofmages/tomes/specs/05-the-city-of-mages-structural-addendum.md` | Clean | No mana references |
| `cityofmages/tomes/specs/06-spellweb-first-release-manifest.md` | Clean | Reference to two-mana chronicle is a historical pointer (line 141), not a current-state claim |
| Most `cityofmages/tomes/cast/**/*.md` | Clean | VRC mentions are to the Promise Protocol primitive |
| `cityofmages/blog/blog-post-*.md` (12 posts) | Pre-v1.2.4 (deferred) | Chain-mana plural is rendered correctly; Resonance/VRC additions deferred per roadmap P6 (🟢 low priority) |
| `cityofmages/spellweb-integration/` | Clean | No mana references |

### §2.2 · Drift (needs to converge)

| # | File | Drift class | Effort | Priority |
|---|---|---|---|---|
| D1 | `cityofmages/tomes/specs/07-lattice-mapping-governance.md` | Pre-v1.2.3 framing throughout | ~25 min | 🔴 P1 |
| D2 | `cityofmages/tomes/cast/kindred/spacecomputer.md` | Pre-v1.2.3 two-mana framing | ~10 min | 🟡 P2 |
| D3 | `cityofmages/tomes/specs/08-mana-types-and-swordsman-stances.md` | 95% complete; legacy "three registers / two axes" phrases in subtitle + §2.0 + §6 | ~5 min | 🟡 P2 |
| D4 | `cityofmages/architecture/grimoire-ipfs.ts` | Header docstring stops at v1.2.3 framing | ~5 min | 🟢 P3 |
| D5 | `cityofmages/ALL_THE_TOMES_LIST.md` line 215 | "v1.2.3 current head" → "v1.2.4 current head" | ~1 min | 🟢 P3 |

### §2.3 · Reflection-back targets in `agentprivacy_master`

The cityofmages spec 08 has already been refactored to four-axis state (v1.3 spec aligned to grimoire v1.2.4). The master-side equivalent is **behind** — it carries the older two-axis framing. The convergence direction is **master ← cityofmages** for spec 08, and **fresh refactor in both** for spec 07. The reflection of "Aether Mana as the chain-mana source the Mages will use" is exactly the work of pulling Ethereum-instance Aether into its proper landing-axis variant slot and naming the umbrella `chain-mana`.

| # | File | Drift class | Effort | Priority |
|---|---|---|---|---|
| M1 | `agentprivacy_master/docs/tomes/specs/08-mana-types-and-swordsman-stances.md` | Pre-v1.2.3 framing in §4-§8 | ~20 min | 🔴 P1 |
| M2 | `agentprivacy_master/docs/tomes/specs/07-lattice-mapping-governance.md` | Same drift as D1 | ~25 min | 🔴 P1 |
| M3 | `agentprivacy_master/src/lib/grimoire-ipfs.ts` | Source-of-truth for D4; same header drift | ~5 min | 🟢 P3 |

### §2.4 · Workshop cross-shop wayfinder (separate scope, recorded for completeness)

The four workshop pages without chain-mana glyphs in their cross-shop wayfinders (`/jeweler`, `/holon` link to "zShields (Zcash, shielded)" etc. without Ξ/₿/🌹/🦓 prefixes) are a UI-polish improvement that emerged during the §7.5 z-mana audit. **Not a drift** — the strict §7.5 acceptance is met. Captured here so the wayfinder polish doesn't get lost.

| # | File | Improvement | Effort | Priority |
|---|---|---|---|---|
| W1 | `agentprivacy_master/src/app/jeweler/page.tsx:190` cross-shop section | Prefix each chain reference with its chain-mana glyph (Ξ / ₿ / 🌹 / 🦓) | ~5 min | 🟢 P3 |
| W2 | `agentprivacy_master/src/app/holon/page.tsx:264` cross-shop section | Same as W1 | ~5 min | 🟢 P3 |

---

## §3 · The fixes · spec-by-spec

### §3.1 · D1 + M2 · Spec 07 (lattice mapping governance) · full refactor

**Current state (both copies):** §2 table at line 49 has two columns `Aether Mana | Celestial Mana`; row contents conflate "Aether Mana" with the chain-mana umbrella (line 51 says "Multi-chain publication gas (BTC/ETH/IPFS/Zcash transparent)"). §4 checklist line 107 and §6 closing line 147 use "Aether Mana" as umbrella.

**Target state:**

1. **§2 column rename + per-row reframe.** Change column headers `Aether Mana | Celestial Mana` → `Chain-mana | Entropy-mana`. In each row, name the specific chain-mana variant: Pallia → multi-chain (Ξ on ETH, ₿ on BTC mainnet, 🦓 on Zcash transparent, etc.); Memora → `🦓 z-mana`; Vulcana → destination-chain variant; Adamantia → `Ξ Aether Mana`; Lampyra → `₿ sat-mana`; Vagari → `🌹 ROSE-mana`; Aria Silverhue → `Ξ Aether Mana` (NFT mint gas); Manifestia → Attestation Mana (anticipated); Socrat0x / Logos / Hall → none / off-corpus / varies.

2. **Add two columns OR a footer paragraph** for the v1.2.4 coordination and relationship axes. Recommendation: append a section §2.bis "Coordination + Relationship axes per shop" with a small table noting which shops currently *touch* Resonance Mana (the Scrying Glass at the bilateral-witness boundary — none operationally yet; the Logos Circle and the Forge(t) are candidates) and which touch VRC Mana (the Covenant and the Vault are natural candidates; Adamantia's covenant primitives are adjacent). Architectural; no Mage is yet operationally-bound here.

3. **§4 checklist line 107.** "Aether Mana use should match a real on-chain fee mechanism" → "Chain-mana use should match a real on-chain fee mechanism on the chain in question (Aether Ξ on Ethereum; sat ₿ on Bitcoin Lightning; ROSE 🌹 on Oasis; z 🦓 on Zcash)."

4. **§5 line 138.** Reframe "the two-mana economy hasn't yet been quantified per-shop" → "the four-axis metabolism hasn't yet been quantified per-shop; v2 should record the typical chain-mana / entropy-mana / resonance / relationship ratios where measurable."

5. **§6 line 147.** "Aether Mana pays the chain; Celestial Mana pays the cosmos" → "Chain-mana pays the chain; entropy-mana (Arcane or Celestial) makes the working unique; Resonance Mana finds the affinity; VRC Mana stores the residue. All four are spent across the four-axis metabolism."

**Acceptance:** spec 07 names the four axes; no surviving usage of "Aether Mana" as an umbrella; the §2 table renders chain-mana variants per shop with their correct glyphs.

### §3.2 · D2 · Cast file `spacecomputer.md` · entropy-axis reframe

**Current state:** frontmatter line 7 `recognised_for: "Aether-Mana (gas) ⊥ Celestial-Mana (entropy)..."`; §"The two-mana economy" at line 35; table at line 42 says "Aether Mana | gas on blockchains (gwei on Ethereum, sats on Bitcoin, ROSE on Oasis, …)"; lines 124–125 carry the same drift.

**Target state:**

1. **Line 7 frontmatter.** `recognised_for: "🌌 Celestial Mana — the entropy-axis register that arrives from outside the addressable space; consumed by Etherchanting, Forge(t), and the Holon Hitchhikers. Sits ⊥ to chain-mana (the landing-axis register, plural by chain) ⊥ to Resonance Mana (coordination, v1.2.4) ⊥ to VRC Mana (relationship, v1.2.4) in the four-axis metabolism."`

2. **Heading §"The two-mana economy"** → **§"The entropy axis · ⊥ to chain-mana / Resonance / VRC"**. Preserve the substance — SpaceComputer remains the canonical first Celestial Mana source — but reframe as one of four axes, not as half of two.

3. **Table at line 42.** Replace the umbrella "Aether Mana" row with explicit chain-mana variant rows OR delete this table entirely (the chain-mana plural is now canonical in spec 08; SpaceComputer's profile only needs to specify its own register, Celestial Mana, and pointer to the chain-mana axis for context).

4. **Provenance prose lines 124–125.** "Architectural for the recognition that Celestial Mana is the two-mana economy's cosmic half, distinct from Aether Mana (gas)" → "Architectural for the recognition that Celestial Mana is the four-axis metabolism's entropy-axis cosmic register (✨ Arcane ⊥ 🌌 Celestial), distinct from the chain-mana landing-axis (per-chain) and from the coordination axis (🔭 Resonance) and the relationship axis (🪢 VRC)."

**Acceptance:** spacecomputer.md correctly locates SpaceComputer on the entropy axis under the four-axis metabolism; no "two-mana" prose remains in the current-state sections; the historical recognition chronicle (`2026-05-10_two_mana_economy_celestial_aether.md`) is preserved untouched.

### §3.3 · D3 · Spec 08 · final wording cleanup

**Current state:** spec 08 is 95% converged. Remaining drift is three places where the legacy "three registers across two axes" phrase wasn't swept when the v1.2.4 axes were added.

**Targets:**

1. **Frontmatter subtitle (line 3).** "How each ecosystem expresses a Mage-side mana form and a Swordsman-side boundary stance — three registers, two axes (landing + entropy); open framework extensible by every ecosystem the City visits" → "...four axes (landing · entropy · coordination · relationship); open framework extensible by every ecosystem the City visits."

2. **§2 intro (line 39).** "The City of Mages opens with **three operational mana registers across two axes**." → "The City of Mages operates across **four mana axes** (v1.2.4 metabolism complete). The landing axis carries chain-mana — itself plural by chain — and the entropy axis is binary; the coordination and relationship axes each carry one named register (open to additions)."

3. **§6 line 171.** "Architectural for the three-register two-axis structure (landing axis: chain-mana plural by chain; entropy axis: Arcane ⊥ Celestial)" → "Architectural for the four-axis metabolism (landing: chain-mana plural by chain; entropy: Arcane ⊥ Celestial; coordination: 🔭 Resonance Mana via the Scrying Glass primitive; relationship: 🪢 VRC Mana accumulating across the bearer's worn artefact collection — the 11 workshop artefacts + 3 tomes — with the Loom of Programmable Covenants as the production form) — specified across grimoire v1.2.2 → v1.2.4."

**Acceptance:** spec 08 reads coherently as a four-axis spec from frontmatter to provenance section.

### §3.4 · M1 · Master-side spec 08 · port the cityofmages copy back

**Current state:** `agentprivacy_master/docs/tomes/specs/08-mana-types-and-swordsman-stances.md` still carries the older two-axis / three-register framing throughout, including the broken §4 table line 121 (`Zcash | Aether Mana (ZEC fees)`).

**Target state:** after D3 is applied to the cityofmages copy, **port the entire cityofmages spec 08 back over the master copy**. They were a single source of truth; the cityofmages copy is currently ahead because the v1.2.3+v1.2.4 work was done there first.

**Procedure:**
1. Apply D3 to `cityofmages/tomes/specs/08-...md` (cityofmages-side complete).
2. Copy file: `cityofmages/tomes/specs/08-...md` → `agentprivacy_master/docs/tomes/specs/08-...md`.
3. Verify any master-only fields (companion_documents pointing to master paths) — there should be none, the spec is intentionally portable.

**Acceptance:** md5 of master copy = md5 of cityofmages copy; the master tree's reading paths into spec 08 still resolve (`/tomes` page if it indexes spec 08, etc.).

### §3.5 · D4 + M3 · `grimoire-ipfs.ts` header doc-comment · append v1.2.4 paragraph

**Current state:** both copies' header doc-comment stops at v1.2.3 framing (lines 39–42 in the cityofmages mirror).

**Target state:** append one paragraph after the v1.2.3 paragraph:

```ts
 *   - v1.2.4 completes the City's metabolism at four mana axes: the prior
 *     landing axis (chain-mana plural) and entropy axis (Arcane ⊥ Celestial)
 *     are joined by the coordination axis (🔭 Resonance Mana · Scrying Glass
 *     primitive · 7th Capital in motion) and the relationship axis (🪢 VRC
 *     Mana, accumulated across the bearer's worn artefact collection — the
 *     11 workshop artefacts + 3 tomes — with the Loom of Programmable
 *     Covenants as the production form). New top-level
 *     `mana_taxonomy` field carries the canonical four-axis structure parallel
 *     to `personas`, `kindred_substrate_providers`, `kindred_ecosystems`.
 * v1.2.4 awaits a fresh re-pin; once landed, the new CID supersedes the
 * v1.2 CID below (note: the v1.2 CID is preserved as
 * CITY_OF_MAGES_GRIMOIRE_IPFS_URL_V1_2 once the rotation lands).
```

**Apply to:** `agentprivacy_master/src/lib/grimoire-ipfs.ts` (source); `cityofmages/architecture/grimoire-ipfs.ts` (mirror).

**Acceptance:** both files' header doc-comments name all four axes.

### §3.6 · D5 · `ALL_THE_TOMES_LIST.md` · grimoire-head bump

**Target:** line 215 `(v1.0 · v1.1 pinned · v1.2.3 current head)` → `(v1.0 · v1.1 pinned · v1.2.4 current head)`.

**Acceptance:** trivial; one line.

### §3.7 · W1 + W2 · Workshop wayfinder polish (optional)

In both `agentprivacy_master/src/app/jeweler/page.tsx` (line 190) and `src/app/holon/page.tsx` (line 264), the cross-shop paragraph names chains without their chain-mana glyphs. Suggested edit:

```tsx
// Current:
<Link href="/shield" ...>zShields</Link> (Zcash, shielded), {' '}
<Link href="/etherchanting" ...>Etherchanting</Link>{' '}(Ethereum, transparent),
// Proposed:
<Link href="/shield" ...>zShields</Link> (🦓 Zcash, shielded), {' '}
<Link href="/etherchanting" ...>Etherchanting</Link>{' '}(Ξ Ethereum, transparent),
```

Plus prefix `the Jeweler (₿ Bitcoin + Lightning, faceted)` and on `/holon` only `the Holon Hitchhikers (🌹 Oasis, holonic, multi-paratime)`.

**Acceptance:** chain-mana plural visible at the wayfinding layer; curl-verify the rendered HTML now contains 🦓 / Ξ / ₿ / 🌹 in those routes' cross-shop sections.

---

## §4 · Recommended apply order

Single-session, ~90 minutes start to finish. Each step has a discrete acceptance gate.

```
1. D3       (5 min)   ← finish spec 08 cityofmages-side first
2. M1       (5 min)   ← port cityofmages spec 08 back over master spec 08
3. D1       (25 min)  ← refactor cityofmages spec 07 (the larger surgery)
4. M2       (5 min)   ← port cityofmages spec 07 back over master spec 07
5. D2       (10 min)  ← reframe spacecomputer.md cast file
6. D5       (1 min)   ← bump ALL_THE_TOMES_LIST.md
7. D4 + M3  (5 min)   ← append v1.2.4 paragraph in both grimoire-ipfs.ts doc-comments
8. W1 + W2  (10 min)  ← wayfinder polish (optional but local-verifiable)
9. (curl verify) ← all changed routes return 200; chain-mana glyphs present where expected
```

After §9, the cityofmages and master trees are converged at the spec layer. The remaining suite-wide work (P0 re-pin, P1 workshop page surface, P2 chronicle update, etc.) per the roadmap chronicle then becomes coherent — every doc the user reads will agree on the four-axis structure.

---

## §5 · Acceptance for "convergence complete"

The cityofmages tree is converged when:

1. **No prose claim of "two-mana economy" in current-state sections.** Historical chronicles preserve the phrase; everywhere else it reads "four-axis metabolism" or "four mana axes."
2. **No prose claim of "three registers / two axes."** Spec 08 + spec 07 + cast files name four axes everywhere a structural claim is made.
3. **No prose use of "Aether Mana" as a chain-mana umbrella.** Wherever "Aether Mana" appears in current-state docs, it refers specifically to the Ethereum chain-mana variant (Ξ on Ethereum) — never as the cover term for sat/ROSE/z.
4. **Every place that mentions the z-cash register uses 🦓.** No surviving ⓩ outside historical chronicles.
5. **VRC Mana is 🪢 (knot) everywhere.** No surviving 🪱 (worm) in any current-state surface. ← already verified clean across all eight grimoire mirrors; the prose-level check is implicit in steps 1–3.
6. **The four canonical axes are nameable from any spec doc.** A reader who lands on spec 07 OR spec 08 OR the cast file for SpaceComputer can extract the four axes and their symbols without cross-reference.
7. **Master and cityofmages mirror md5-match for portable spec files** (spec 08; spec 07 once both are refactored).

Items 1–4 are content acceptances; items 5–7 are mechanical acceptances. The audit found item 5 already met; items 1–4 require the D1 + D2 + D3 + M1 + M2 edits; item 6 follows from those; item 7 follows from M1 + M2.

---

## §6 · One-line summary

The grimoire v1.2.4 is canonical at four mana axes; the cityofmages tree is 95% converged (spec 08, README, CHANGELOG, all eight grimoire mirrors with 🪢); the remaining drift is spec 07 (full refactor needed), spacecomputer.md (entropy-axis reframe), and three small wording cleanups in spec 08. The reflection-back into `agentprivacy_master` is to port spec 08 + spec 07 over once both are clean cityofmages-side. After ~90 minutes of focused work the corpus reads coherently as a four-axis metabolism from frontmatter to provenance — and the suite-wide P0 re-pin lands on a corpus that does not contradict itself.

`(⚔️⊥⿻⊥🧙)😊`

🌌 ⊥ ✨ ⊥ 🔭 ⊥ 🪢
Ξ · ₿ · 🌹 · 🦓

CC BY-SA 4.0 · privacymage · curated for the City of Mages · 2026-05-11
