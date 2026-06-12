---
title: "Workshop Constellations — Protocol and Template"
subtitle: "How seekers find their way to a workshop's door"
version: "v1.0 (2026-05-11)"
status: "Operational"
audience: "Workshop keepers · seekers · spellweb runtime"
companion_documents:
  - "CEREMONY_EVOLUTION.md — governance of constellation versioning"
  - "architecture/shop-witnesses.ts — witness record storage"
  - "chronicles/2026-05-10_witness_unlock_feature_design_chronicle.md — full unlock cascade design"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Workshop Constellations

> *The map is not the journey, but the stars we trace together become the path we own.*

## §1 · What a constellation is

Each workshop in the City of Mages has a **constellation** — a named set of lattice vertices that expresses the workshop's knowledge in geometric form. A constellation is not a tour or a curriculum. It is the shape of the workshop's work rendered on the 64-vertex lattice.

When a seeker traces a constellation on the spellweb, they walk the same vertices the workshop's Mage inhabits and works from. The tracing is the trust task. The blade that emerges is the proof.

The constellation is **not surveillance**. The seeker does not report to the workshop. The seeker brings the blade back voluntarily. The workshop cannot know who traced unless the seeker chooses to arrive.

---

## §2 · The flow

```
1. Seeker downloads constellation.md from the workshop's tomes/workshops/<guild>/ directory
2. Seeker opens spellweb.ai and enters Ceremony Mode
3. Seeker traces the constellation's named vertices in order
4. Spellweb exports a artefact.md (the workshop's artefact, signed with the seeker's archetype and stratum)
5. Seeker brings the artefact.md to the workshop's shopAnchor route (e.g. /tailor)
6. The shop imports the blade → trust unlocks → secret nodes reveal → services open
```

The seeker may complete step 3 at any stratum (Light · Heavy · Dragon). Higher stratum means deeper traversal; secret nodes gate progressively on stratum per the witness-unlock design.

---

## §3 · What a constellation.md file must contain

Each workshop's `constellation.md` is authored by the workshop's keeper and lives at:

```
tomes/workshops/<guild>/constellation.md
```

It must contain these sections, in order:

### Required frontmatter fields

| Field | Description |
|---|---|
| `title` | "Constellation — \<TradeQuarter\> · \<Gem\> · V\<n\>" |
| `version` | Semantic string, e.g. `cloak-weave-v1` |
| `shop` | Node id from the spellweb manifest |
| `shopAnchor` | The route the blade returns to, e.g. `/tailor` |
| `keeper` | Mage name + sigil |
| `vertex` | Primary vertex, e.g. `V28` |
| `gem` | Gem name for the shop's color |
| `gemColor` | Hex color, e.g. `#a78bfa` |
| `nodeCount` | Integer — how many vertices the constellation traces |
| `operationalServices` | List of service identifiers offered at this tier |
| `honesty` | `operational` / `architectural` / `conjectural` — highest tier offered |
| `license` | `CC BY-SA 4.0` |
| `signature` | `(⚔️⊥⿻⊥🧙)😊` |

### Required sections

**§1 · The Constellation** — the ordered list of vertices with a one-line description of what each vertex represents in the workshop's work. This is the path the seeker traces.

**§2 · The Ceremony** — step-by-step description of what the seeker does on the spellweb. What they encounter at each vertex. What the artefact.md contains when exported.

**§3 · What Unlocks** — what the seeker gains on bringing the blade to the shop. Secret nodes. Documentation. Service access. Stated per stratum if relevant.

**§4 · The Services** — description of each operational service the shop offers, with honesty labels. One subsection per service.

**§5 · The 7th Capital** — the tip mechanism. How the seeker may contribute value to the keeper for services rendered. Form is the keeper's choice; structure must be present.

---

## §4 · Proof of Presence — what it is and is not

**What it is:**
- A geometric trust task — the seeker demonstrates they have walked the workshop's lattice path
- A blade with a witness signature, verifiable by the shop
- A voluntary act; the shop cannot compel it

**What it is not:**
- A credential issued by the workshop to the seeker
- A record of the seeker's identity (the blade carries archetype and stratum, not a DID)
- A gate that blocks access to the city (workshops are open; the constellation deepens what's available)

The proof of presence is the **structure of arrival**. Two seekers who traced the same constellation bring structurally identical blades with different archetypes and strata. The shop recognises the shape; it does not need to know the seeker.

---

## §5 · Stratum and progressive unlock

The witness-unlock design specifies progressive disclosure by running stratum:

| Stratum | Tier | Secret-node opacity |
|---|---|---|
| 0 | Null | Hidden |
| 1–2 | Light | 17%–33% |
| 3–4 | Heavy | 50%–67% |
| 5–6 | Dragon | 83%–100% |

Workshop keepers MAY assign a `revealStratum` to each secret node (overriding the default of 6). A node with `revealStratum: 2` becomes substantially visible on a Light-tier walk. A node with `revealStratum: 6` only fully reveals at Dragon.

The blade's stratum becomes the seeker's **achieved tier** for that workshop, stored in localStorage. Re-evoking and reaching a higher stratum raises the floor.

---

## §6 · The 7th Capital — tips as sovereign transaction

Each workshop's constellation closes with a 7th Capital section: the mechanism by which a seeker who has received value from the workshop may return value to the keeper.

The tip is:
- **Voluntary** — the proof of presence is not conditional on a tip
- **Sovereign** — the keeper sets the form and the suggested amount
- **Embedded in the ritual** — it is named in the constellation, not added as an afterthought

The tip transforms "the residue of being alive" — the behavioural surplus created when the seeker and the shop create value together — into a named, optional, sovereign transaction.

Workshop keepers may specify any form: a sats address, a Z-address (shielded), a VRC promise, a credit in the workshop's own ledger. The form must be declared in the `constellation.md`.

---

## §7 · Versioning

Each constellation carries a version string (e.g. `cloak-weave-v1`). When a keeper updates the constellation (new nodes, new services, new ceremony steps), they increment the version.

Prior unlocks remain valid at the prior version's achieved tier. Walking the new version unlocks the new secret nodes on top of existing floor opacity. See `CEREMONY_EVOLUTION.md` for full governance.

---

## §8 · Workshop index

| Workshop | Guild | Keeper | Gem | Vertex | Constellation file |
|---|---|---|---|---|---|
| Weavers | weavers | Pallia 🪡 | Amethyst | V28 | [weavers/constellation.md](weavers/constellation.md) |
| zShields | zshields | Memora 📜 | Onyx | V41 | *(forthcoming)* |
| The Forge(t) | forge | Vulcana ⚒️ | Ruby | V19 | *(forthcoming)* |
| Etherchanting | etherchanting | Adamantia 💎 | Sapphire | V51 | *(forthcoming)* |
| The Jeweler | jeweler | Lampyra 💠 | Topaz | V49 | *(forthcoming)* |
| Holon Hitchhikers | holon | Vagari 🌳 | Emerald | V31 | *(forthcoming)* |
| The Dragon Bonfire | bonfires | Socrat0x 🔥❓ | Garnet | V24 | *(forthcoming)* |
| The Curatrix Vault | vault | Aria Silverhue 🪞🖼️ | Pearl | V57 | *(forthcoming)* |
| The Covenant | covenant | Manifestia 🤲🌿 | Diamond | V55 | *(forthcoming)* |
| The Logos Circle | circle | *(gathering)* | Jade | — | *(forthcoming)* |
| The Ceremony Hall | hall | *(gathering)* | Lapis | — | *(forthcoming)* |

---

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · the City of Mages · 2026-05-11
