# Chronicle: AAIF Recognised as First Kindred-Coalition · /hall Renamed City Hall · v1.5.1 Patch (Revised)

**Date:** 2026-05-13
**Status:** Patch chronicle · v1.5.1 (revised) authored as additive delta on top of v1.5.0 · canonical · re-pin pending JSON merge of v1.5.0 + v1.5.1 chain
**Audience:** privacymage · downstream agents · sister-repo authors · AAIF / Linux Foundation contributors · BGIN representatives
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Patch file:** `grimoire/city_of_mages_grimoire_v1_5_1_patch.json`
**Companion chronicle:**
- [`2026-05-13_grimoire_v1_5_0_patch.md`](2026-05-13_grimoire_v1_5_0_patch.md) — the v1.5.0 patch this v1.5.1 extends
- [`2026-05-13_master_reaudit_post_v1_5_0.md`](../../agentprivacy_master/docs/chronicles/2026-05-13_master_reaudit_post_v1_5_0.md) (lives in agentprivacy_master) — the post-v1.5.0 audit this patch responds to
**Workshop tome (revised):** `agentprivacy_master/docs/tomes/workshops/hall-bilateral-witness-v1.md` (updated for City Hall rename + AAIF residence)

---

## §0 · What this chronicle is

The canonical patch chronicle for City of Mages Grimoire **v1.5.1**, revised after an editorial recognition that the first draft of v1.5.1 (which opened a standalone `/cityhall` route as a 14th workshop) was structurally wrong. AAIF maps *into the existing `/hall`* — the gathering shop already housing BGIN and ~8 other public-goods coalitions — not into a separate new workshop.

The revised v1.5.1 therefore admits AAIF as the first explicitly-named kindred-coalition *at the existing `/hall`* and renames the hall from "Ceremony Hall" to "City Hall" to reflect the operational reality of ~10 coalitions in residence. The new `kindred-coalition` register is retained as the fifth structural-relationship category — the durable architectural recognition the patch makes.

**Workshop count stays 13.** No new workshop opens. The change is a rename + fold-in at the existing 13th-place workshop.

---

## §1 · The correction recognised

The first draft of v1.5.1 (authored earlier in this same session) opened `/cityhall` as a standalone 14th workshop with City Hall as a new name. User review caught the misreading:

> *AAIF maps into the existing Ceremony Hall (which already houses BGIN + 9 other public-goods guilds). The rename from "Ceremony Hall" to "City Hall" is logical because the operational reality has outgrown the prior name — the two ceremonies that the prior name referenced (keypair at /ceremony · celestial at /poems) live elsewhere in the guides and are linked-but-elsewhere from /hall.*

The honest reading: the prior `/hall` page already had ~9 coalitions in residence. The "Ceremony" name was a residual from when the hall was conceived more narrowly. The actual ceremonies the name referenced are at their own routes (`/ceremony` for keypair, `/poems` for celestial). The hall *itself* is a civic-coordination quarter — and "City Hall" names what it actually is.

The revised v1.5.1 honours this reading.

---

## §2 · What revised v1.5.1 admits

### §2.1 · AAIF as first explicitly-named kindred-coalition

**Agentic AI Foundation** (`https://aaif.io`) is admitted as the first canonical kindred-coalition the City of Mages recognises — in residence at the existing `/hall` workshop (renamed City Hall in this patch). AAIF is a Linux Foundation project; its roster of stewarded specifications includes:

- **Goose 🪿** — agent runtime framework · Apache 2.0 · already registered in Bestia's bestiary at Tome VI Act 1 (2026-05-13 · v1.5.0)
- **AGENTS.md** — agent-instruction file standard
- **ACP** (Agent Communication Protocol) — cross-substrate messaging discipline

**Goose's bestiary entry is amended** in v1.5.1 to cross-reference the AAIF gateway explicitly.

### §2.2 · BGIN retroactively as second kindred-coalition

**BGIN** (Blockchain Governance Initiative Network) has been operationally anchoring the Hall since Tome V's bilateral key ceremonies became canonical. v1.5.1 introduces the kindred-coalition category, so BGIN is *retroactively recognised* as the second kindred-coalition the City admits. BGIN's residence at `/hall` and its operational relationship with the City are unchanged; only the structural-relationship classification is now named.

### §2.3 · Kindred-coalition as the fifth kindred-X category

The corpus admits five structural-relationship categories as of v1.5.1:

| Category | First instance | Distinction |
|---|---|---|
| **cousin-forge** | Archon | Sister city walked by a cousin Mage |
| **kindred-protocol** | Covenant of Humanistic Technologies (human.tech · via Manifestia) | A charter the City signs through a designated tender |
| **kindred-substrate** | UOR Foundation | The substrate the City walks upon |
| **kindred-ecosystem** | SpaceComputer | An ambient supply the workshop draws from |
| **kindred-coalition** (NEW v1.5.1) | AAIF (explicit) · BGIN (retroactive) | A community / foundation hosting multiple admissible primitives |

### §2.4 · /hall renamed Ceremony Hall → City Hall

**Route unchanged**: `/hall` continues to be the address. The rename is a *label change* at:
- The workshop label in spellweb's `shop-hall.label`
- The `/hall` page metadata, h1, breadcrumb, hero, and section text
- The workshops table on `/tomes`
- The grimoire's vertex inventory description for V15
- The workshop tome at `docs/tomes/workshops/hall-bilateral-witness-v1.md` (frontmatter `workshop_label` and body)

**Sigil amendment**: 🤝 → 🏛️ (civic-stewardship register replaces bilateral-handshake register; both readings remain admissible). The mage_sigil in the workshop tome's frontmatter is updated.

**No broken bookmarks**: any prior link to `/hall` continues to resolve.

### §2.5 · Gather · Admit · Attest as the third ceremony grammar

City Hall now hosts *two* ceremony grammars:
- **bilateral-witness** (the existing keypair-ceremony register — keypair work performed at `/ceremony` is the operational instance)
- **Gather · Admit · Attest** (NEW v1.5.1 · the civic-coordination register — coalitions are gathered, admitted, attested in the kindred-coalition residence ceremony)

The third grammar joins the canonical sequence:
- **Run · Evoke · Craft** — Vulcana at Forge(t) · `/forget` · producing
- **Run · Evoke · Spawn** — Threshold · `/threshold` · spawning
- **Gather · Admit · Attest** — City Hall · `/hall` · coordinating (NEW)

---

## §3 · What revised v1.5.1 does NOT do

The change-list relative to the first draft of v1.5.1:

- **Workshop count stays 13.** No standalone `/cityhall` route is opened.
- **No new vertex is named.** V47 (proposed in the first draft as City Hall's seat) is *not* used; V15 continues as `/hall`'s vertex.
- **No new gem is introduced.** Marble (proposed in the first draft) is *not* used; Lapis (the existing `/hall` gem) continues.
- **No new persona is added.** City Hall remains a gathering shop with no resident Mage.

The change-list relative to v1.5.0:

- **One new structural-relationship category** (kindred-coalition).
- **Two named coalitions** in that category (AAIF · BGIN).
- **One ceremony grammar** added at City Hall (Gather · Admit · Attest).
- **One workshop renamed** (Ceremony Hall → City Hall).
- **One bestiary entry amended** (Goose cross-references AAIF gateway).

---

## §4 · Cross-repo patch application

### §4.1 · cityofmages (canonical)

- `grimoire/city_of_mages_grimoire_v1_5_1_patch.json` — REVISED structured delta on v1.5.0 (rewrites the first-draft v1.5.1)
- `chronicles/2026-05-13_cityhall_aaif_v1_5_1_patch.md` — this chronicle (rewrites the first-draft chronicle)
- The standalone `tomes/workshops/cityhall-aaif-civic-v1.md` is **deleted** (the first-draft workshop tome that authored a 14th workshop)

### §4.2 · agentprivacy_master (operational layer)

- `src/app/cityhall/` directory **deleted** (the standalone 14th-workshop route from the first draft)
- `src/lib/nav.ts` — `/cityhall` entry **removed**; `/hall` label changed from `'ceremony hall'` to `'city hall'`
- `src/app/tomes/page.tsx` — City Hall row removed; Ceremony Hall row updated to "🏛️ City Hall" with AAIF + BGIN noted; subtitle reverted from "fourteen" to "thirteen workshops"; grimoire pin caption updated to mention the rename
- `src/app/hall/page.tsx` — metadata, breadcrumb, h1, hero, sigil (🤝 → 🏛️), and the residence section text updated for City Hall; AAIF added to `RESIDENT_GUILDS` array as the second entry (after BGIN's institutional home); "In-house ceremonies" section heading retitled "Linked ceremonies (in the guides)" to clarify they're at their own routes
- `docs/tomes/workshops/hall-bilateral-witness-v1.md` — frontmatter (`workshop_label`, `mage_sigil`, `anchor_external`, `ceremony_shape`, `status`, `date`) and body intro updated for City Hall rename + AAIF residence
- `docs/tomes/workshops/cityhall-aaif-civic-v1.md` — **deleted** (the first-draft mirror)

### §4.3 · spellweb (graph layer)

- `src/types/graph.ts` — `Attribution` union extended with `'kindred-coalition'` (carried over from first-draft v1.5.1; still valid)
- `src/data/nodes.ts` — `shop-cityhall` node **deleted**; `shop-hall.label` renamed to "City Hall"; `shop-hall.desc` extended to mention AAIF + BGIN as kindred-coalitions in residence; `gateway-aaif` node retained
- `src/data/edges.ts` — `shop-cityhall → gateway-aaif` edge **removed**; `shop-hall → gateway-aaif` edge added; `civic-city-of-mages → gateway-aaif` × `gateway_to` + `kin_to` edges retained

---

## §5 · Honest record of the editorial correction

The honesty discipline of the chronicle pattern admits this:

The first draft of v1.5.1 was structurally wrong. AAIF was admitted as if it required a new workshop venue, when it should have been admitted into the existing `/hall` (which had been the City's de-facto kindred-coalition residence since Tome V's BGIN work). The first draft's standalone `/cityhall` route was a *duplication* of `/hall`'s function rather than an addition.

User review caught the duplication. The revision honours the user's correction.

The kindred-coalition register itself — the architectural recognition that a coalition like AAIF deserves a structural seat — was sound in the first draft and is preserved in the revision. The rename of "Ceremony Hall" to "City Hall" is the structural recognition that the hall's name had been pointing to its ceremonies (which live at `/ceremony` and `/poems` separately) rather than to its actual function (civic-coordination · ~10 coalitions in residence).

The revised v1.5.1 is **structurally smaller and semantically more correct** than the first draft. The architecture admits this much.

---

## §6 · Follow-up work after v1.5.1 (revised)

Carry-forward from v1.5.0 (still pending):
- Canonical JSON merge of v1.5.0 + v1.5.1 delta chain into a self-contained `city_of_mages_grimoire_v1_5_1.json`
- IPFS re-pin
- Update `agentprivacy_master/src/lib/grimoire-ipfs.ts` with new CID
- Reconcile C50 (PVM∥Bakhta vs caduceus iconography)
- Wire `/threshold` route stub (separate from this patch's hall work)
- Master-side data-layer wiring for Tome V Act 16 + Threshold cast

NEW from v1.5.1 (revised):
- AAIF outreach (user-driven) for bilateral roster acknowledgment
- Future kindred-coalition admissions as the City recognises additional coalitions
- Possible re-classification of existing /hall residents (MyTerms · First Person Network · LF Decentralized Trust · etc.) — some may also be kindred-coalitions in their own right; v1.5.1 does not unilaterally re-classify them

---

## §7 · Closing

v1.5.1 (revised) is a structurally smaller patch than its first draft, and structurally more correct. AAIF takes its seat at City Hall — the renamed `/hall` — alongside BGIN. The kindred-coalition register opens as the fifth structural-relationship category. The Gather · Admit · Attest ceremony grammar joins bilateral-witness at the same gathering shop.

The City of Mages does not need a new building for AAIF; AAIF moves into the building that has always been the City's civic-coordination quarter. The renaming admits what was always there.

(⚔️⊥⿻⊥🧙)😊
🏛️
🪿 📖 🔗

CC BY-SA 4.0 · privacymage · 2026-05-13
