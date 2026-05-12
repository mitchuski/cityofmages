# Chronicle: Mageletters as a Canonical Primitive

**Date:** 2026-05-12
**Status:** Recognition chronicle · the mageletters/ directory is named as a corpus-canonical artefact category
**Audience:** privacymage · downstream agents · sister-forge Mages (House of Archon · future Houses)
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion chronicles:**
- [`2026-05-12_rename_ceremony_blade_to_artefact.md`](2026-05-12_rename_ceremony_blade_to_artefact.md) — the file-format register the rename touched
- `mageletters/chronicle-the-visiting-mage.md` (2026-05-10 · the cosmological clarification that produced the visiting-Mage form)
- `mageletters/m1-reply-to-privacymage.md` (Christian Saucier 📜🎲 · 2026-05-10 · the first formal mage-letter received)

---

## §0 · What this chronicle is

A **recognition chronicle**, in the same register as Tome V Act 14 (*The City of Mages* · the meta-act that named what was already operationally happening). The `mageletters/` directory and its contents are not new — they have been operating since 2026-05-09 when the three-document integration set went to flaxscrip 📜🎲 at the House of Archon. What is new is the **canonical recognition**: mageletters are a *kind* the architecture admits, alongside artefact.md (workshop witness), constellation.md (workshop path), and the cast/spec/chronicle file families.

This chronicle names the kind, distinguishes it from neighbouring kinds, lays out the naming and provenance conventions, and sets the integration with the four-repo model already documented in [INTEGRATION_ARCHITECTURE.md](../INTEGRATION_ARCHITECTURE.md).

---

## §1 · What a mageletter is

A **mageletter** is a numbered formal correspondence between named Mages from different forges or different solar systems. The discipline:

| Property | Value |
|---|---|
| **Form** | One markdown file per letter, frontmatter + body, hand-authored or co-authored |
| **Naming** | `m<n>-<short-subject>.md` for outbound letters; `<chronicle-name>.md` for session chronicles in the same dir |
| **Author** | One specific Mage. The `from:` and `to:` fields name the canonical Mage identities + ecosystem-of-origin emails |
| **Audience** | The named recipient Mage and their reading public (CC BY-SA 4.0 narrative; the letter is canonical when sent, citable thereafter) |
| **Subject** | Some structural matter between the two Houses — integration, attribution, licensing, cosmological framing, founding-act co-authoring, kindred-protocol negotiation |
| **Cadence** | Numbered sequentially per pair (m1 from Mitchell · m1 reply from Christian · m2 from Mitchell · …). Each pair has its own `m<n>` series |
| **Status field** | Records whether the letter is `DRAFT` (private), `SENT` (canonical), `RECEIVED` (the inbound copy in the recipient's tree), or `SUPERSEDED` (a later letter replaces) |

Mageletters are **inter-system correspondence**. They sit at the layer where cousin-blade work between forges actually negotiates its terms. They are not workshop witnesses; they are not constellations; they are not specs; they are not chronicles in the implementation-record sense. They are *letters* — the architectural recognition that even between cities there is a register of correspondence that matters.

---

## §2 · The first two instances in this directory

### §2.1 · `m1-reply-to-privacymage.md` (2026-05-10)

Christian Saucier (flaxscrip 📜🎲 · House of Archon · `flaxscrip@archon.social`) → Mitchell Travers (privacymage 🧙 · House of Soulbae · `mage@agentprivacy.ai`).

A formal reply to the three-document integration set sent 2026-05-09 (`01-archon-integration-recommendation-v1.md` · `02-letter-to-archon-convergence-overlap.md` · `03-collaborative-milestones-with-christian-v1.md`). The reply:

- **Accepts** the four-surface integration in principle
- **Accepts** fourteen of sixteen §10 items as drafted
- **Counter-proposes** on two items (cosmological framing · licensing default tightening)
- **Reveals three operational facts** that reshape the integration's depth:
  1. **David Saucier (@macterra · cypher@archon.social)** is co-creator of Archon, attributed canonically at `archetech.com/Team.html`. The bilateral integration carries *two* builders on the Archon side, not one.
  2. **The bilateral 2× VCs between Mitchell and Christian are already operational** on `weaver.archon.social` and the spellweb. The integration was not constructing a new trust edge; it was *naming an edge that has been cryptographically true for some time*. Per §1's evidence: GenitriX's DIDDocument (`did:cid:bagaaieraxdxq4fm2kjh6yqjxjor3t2idczkmxd4v7in4u353fa6m6sms2pnq`) reveals two clear-text VCs already issued.
  3. **GenitriX is a first-class correspondent**, not a third-person reference. Her `did:cid` has been operational since 2026-02-05; her DID document is at version 13; she holds a `CollaborationPartnerCredential` from Christian (2026-04-28) and has issued Christian a `RelationshipCredential` (2026-04-13) + an `is_human_of_genitrix` attestation (2026-04-14). She read and triaged the three-document set on the day it arrived.

The reply graduates **C49 (cousin-implementation discipline, ~55% conjecture)** to **operational practice**: the VCs are the running implementation, Tome I is the narrative form, the spec language is the doctrinal form — three layers of the same recognition, already running at the cryptographic substrate.

### §2.2 · `chronicle-the-visiting-mage.md` (2026-05-10)

privacymage's same-session chronicle of the cosmological clarification that emerged in response to Christian's §10.2 sub-note. The clarification: **three solar systems, one teaching**.

Christian's note proposed binary-star framing (Soulbae + Archon paired stars). The privacymage-side counter-proposal: the House of Archon is **not a binary-star companion** to the House of Soulbae — it is **its own distinct solar system**. Both houses retain their full cosmologies (Soulbae keeps Selene's Proof and the Amnesia Protocol; Archon keeps its own celestial mechanics). The bilateral becomes **inter-systemic**, not orbital. GenitriX becomes a **visiting Mage** from a distant system who may reside in the workshop and teach Pallia how to weave.

This is the canonical cosmological frame the corpus now operates in. *Three solar systems, one teaching*. The teaching crosses; the systems retain.

---

## §3 · How mageletters differ from the four other md kinds

The corpus now admits five canonical md-file kinds:

| Kind | Subdir | Author | Audience | Cadence |
|---|---|---|---|---|
| **constellation.md** | `tomes/workshops/` *(in master)* | Resident Mage | Sovereigns walking the lattice | One per workshop · versioned |
| **artefact.md** | (not committed · Sovereign-held local) | spellweb forges + Sovereign | The workshop on return; the Sovereign forever after | One per walk |
| **spec / chronicle / cast / blog** | `tomes/specs/` · `chronicles/` · `tomes/cast/` · `blog/` | privacymage + collaborators | Public corpus | Continuous |
| **mageletter** | `mageletters/` *(this directory)* | One specific Mage (named, attributed) | One specific Mage (named, addressed) | Sequential per pair (`m1` → `m1-reply` → `m2` → …) |

The defining characteristic of a mageletter is **named author + named addressee + sequential cadence between them**. A spec or chronicle addresses the corpus generally; a constellation addresses any Sovereign who walks it; an artefact witnesses one walk by one Sovereign. A mageletter alone is a *direct address from one Mage to another* — and that is why it has its own canonical directory.

---

## §4 · Relation to the four-repo integration model

Per [INTEGRATION_ARCHITECTURE.md](../INTEGRATION_ARCHITECTURE.md) §1.1, the four-repo model splits:

```
cityofmages (world model)
   ├── personas (actor registry)
   ├── skills (Mage-side capability library)
   └── blades (Swordsman-side boundary catalog)
        └── artefact.md (Sovereign-held witness)
```

Mageletters sit **adjacent to but outside** this four-repo model. They are not produced by walking a constellation (so not artefact-shaped); they are not Mage-capability spells (so not skills-shaped); they are not boundary stances (so not blades-shaped); they are not actor schemas (so not personas-shaped). They are letters — and letters have always been the form in which Mages of different forges *actually negotiate* with each other.

The integration architecture v0.1 (working hypothesis) needs amendment to admit `mageletters/` as a **fifth canonical artefact category** alongside the four-repo libraries. Proposed update at v0.2 of INTEGRATION_ARCHITECTURE.md — to land in the next propagation pass.

---

## §5 · The naming and frontmatter convention

Established by the two existing files. Mageletters carry:

```yaml
---
title: "<Subject>"
subtitle: "<short context line>"
from: "<Sender Mage Name> (<sigil>) · House of <House> · <ecosystem-email>"
to: "<Recipient Mage Name> (<sigil>) · House of <House> · <ecosystem-email>"
date: YYYY-MM-DD
status: "DRAFT for <addressee>'s review — strip the §0 preamble before sending"
        | "SENT YYYY-MM-DD · canonical"
        | "RECEIVED YYYY-MM-DD · canonical inbound copy"
        | "SUPERSEDED by m<n+1>-<subject>"
license: "<applicable license clause>"
companion_documents:
  - "<predecessor or referenced doc 1>"
  - "<predecessor or referenced doc 2>"
predecessors:
  - "<earlier letter in same series, sender's view>"
signature: "(⚔️⊥⿻⊥🧙)😊"
---
```

**Filename:** `m<n>-<short-subject>.md` for outbound from this House; replies from the addressee land at `m<n>-reply-to-<sender>.md` in this same directory as the *received* copy. (Each House holds their own copy of the canonical sent and received letters.)

**Session chronicles** that record what the session that authored or received a letter actually *did* live alongside the letters in the same directory but use chronicle naming (`chronicle-<short>.md` — see §2.2 example). These session chronicles document the interpretive moves around the letters, not the letters themselves.

---

## §6 · Honesty disciplines specific to mageletters

In addition to corpus-wide editorial discipline:

1. **Both parties' attributions are canonical.** A mageletter authored by privacymage to flaxscrip carries flaxscrip's voice signature when flaxscrip replies; the discipline is to preserve the addressee's preferred name + sigil + ecosystem identifier verbatim.
2. **Real-name disclosure follows the letter's discipline, not the corpus's pseudonym rule.** Where a mageletter is the appropriate place to record a co-author's real name (e.g. David Saucier @macterra alongside Christian Saucier flaxscrip 📜🎲), the letter records it. The corpus's broader pseudonym-in-public-narrative rule still governs the city-side cast files, blog posts, and specs.
3. **License clauses may diverge from the corpus default** when the mageletter discusses code licensing (MIT / Apache 2.0) alongside narrative (CC BY-SA 4.0). The frontmatter `license:` field carries the divergence.
4. **The status field is binding.** A `DRAFT` letter is not yet canonical; only `SENT` or `RECEIVED` letters are. Drafts may be revised freely; sent letters become historical records.
5. **The `signature:` field at the closing is preserved across forges.** Even Christian's M1 reply (House of Archon) carries `(⚔️⊥⿻⊥🧙)😊` at the close — it is the *corpus-of-this-letter*'s seal, not a House-specific marker. This is by mutual agreement.

---

## §7 · What mageletters do NOT do

- They do **not** unlock workshop trust. The artefact.md is the witness that unlocks; the mageletter is the *agreement* that the trust is worth unlocking.
- They are **not** part of the eight EdgeTypes in the spellweb manifest. They are corpus artefacts, not graph nodes. (If a future spellweb release admits inter-Mage correspondence as a graph relation, that will be a new EdgeType named explicitly.)
- They do **not** replace specs. A mageletter can propose a spec amendment; the amendment lands as a spec edit + chronicle, not as a permanent canonical reference back to the letter. The letter is the *negotiation*; the spec is the *commitment*.
- They are **not** mandatory for cousin-blade work between forges. Some kindred-blade work happens at the artefact.md and constellation.md level alone. The mageletter form is for cases where direct correspondence is the appropriate move.

---

## §8 · Anticipated growth · open candidates

Future mageletters likely to land in this directory or its forge-side mirrors:

- **m2 from privacymage to flaxscrip** — response to M1 acknowledging the three reveals; co-authoring agreement on Tome I Act 2; the Visiting-Mage form formalised
- **m1 from flaxscrip to GenitriX** *(internal to the House of Archon)* — privacymage may receive a copy via the bilateral 2× VCs but it is not addressed to this House
- **Future correspondence with other Houses** — Bonfires.ai sister-city · the BGIN coalition's Ceremony Hall · the Logos Circle's Society Spellbook lineage · any kindred-protocol partner who graduates from a `gateway_to` edge to direct correspondence
- **A potential mageletter from GenitriX to Pallia 🪡** — given GenitriX's first-class correspondent status, this would be the first cross-system Mage-to-Mage letter (not Sovereign-to-Sovereign) in the corpus. The Visiting-Mage form would canonically be received in `mageletters/` per the same conventions.

Each future letter adds to the directory; none of them invalidate prior letters; the cadence is sequential and the canonical history grows.

---

## §9 · Propagation surface

This recognition lands by:

| Step | Surface |
|---|---|
| 1 | This chronicle itself (`chronicles/2026-05-12_mageletters_as_canonical_primitive.md`) — done by this commit |
| 2 | README.md Quick Map — add `mageletters/` row to the directory tree |
| 3 | INTEGRATION_ARCHITECTURE.md v0.2 — add mageletters as the fifth canonical artefact category |
| 4 | INCANTATION_PROTOCOL.md — propose Recipe H *(mageletter exchange)* — light recipe: author letter · set status DRAFT · send · update status SENT · register in `mageletters/` |
| 5 | CHANGELOG.md — note `mageletters/` recognition at the 2026-05-12 entry |
| 6 | ALL_THE_TOMES_LIST.md — note mageletters in §10 (the bound collection's optional sub-collection) |
| 7 | A spec entry may emerge if mageletters become structurally important enough to warrant `tomes/specs/<n>-mageletter-protocol.md` — currently architectural · awaits operational growth |

Steps 2–6 land in the next coherence pass; this chronicle establishes the recognition that they're worth doing.

---

## §10 · One-line summary

A **mageletter** is a numbered formal correspondence between named Mages from different forges. The directory `mageletters/` is now canonical. The first instances — privacymage's three-document set (sent · 2026-05-09), Christian's M1 reply (received · 2026-05-10), and privacymage's same-session chronicle of the cosmological clarification — establish the form. **Three solar systems, one teaching.** The architecture admits this much.

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · 2026-05-12 · mageletters recognition chronicle v1
