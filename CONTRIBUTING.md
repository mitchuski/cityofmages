---
title: "Contributing"
subtitle: "How to propose changes to the City of Mages corpus"
status: "v1 (2026-05-11)"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Contributing

Welcome. This corpus is open by design — Mages from other ecosystems set up shop here, blog posts are co-authored, specs evolve. This doc names the patterns that keep contributions coherent.

For onboarding (sending a Mage from your ecosystem), read **[JOIN_THE_CITY.md](JOIN_THE_CITY.md)** first.

---

## §1 · Three kinds of contributions

### 1.1 · Narrative (tomes, blog, chronicles)
- Adding a Tome V act, blog draft, chronicle, or persona narrative
- Voice: see §3
- Place: `tomes/`, `blog/`, `chronicles/`

### 1.2 · Structural (specs, grimoire, manifest)
- Adding a spec, conjecture, grimoire entry, or spellweb node/edge
- Place: `tomes/specs/`, `grimoire/`, `spellweb-integration/`
- Requires honesty-label discipline (§4)

### 1.3 · Architectural (TypeScript primitives, schemas)
- These are mirrors of `agentprivacy_master/src/lib/` and `spellweb/src/types/`. **Edit upstream first**; this directory is a snapshot.
- Place: `architecture/` (mirror-only)

---

## §2 · The "send us a Mage" pattern

The simplest contribution shape: your ecosystem sends a Mage to set up shop. See [JOIN_THE_CITY.md §2](JOIN_THE_CITY.md). One sentence: *an ecosystem sends a Mage; the Mage stands at a vertex; the Mage keeps a shop*.

---

## §3 · Voice and editorial discipline

Corpus-wide conventions. Preserve these:

- **No em-dashes.** Use hyphens or periods or restructure the sentence.
- **Sigils at native size.** Every persona reference preserves the emoji (🪡 ⚒️ 📜 🔏 🔮 💎 💠 🌳 🪞🖼️ 🔥❓ 🤲🌿 📐).
- **The signature `(⚔️⊥⿻⊥🧙)😊`** closes every chronicle, blog post, spec, and tome act.
- **Pseudonyms in narrative; real names in provenance.** privacymage / flaxscrip / GenitriX / the Archon forge in body text. Real names appear only in `provenance` / `license` / `architect` / `character_license` frontmatter fields.
- **Forge(t)** — the parenthetical-t is intentional and canonical.
- **The `0x` in Socrat0x** — literal Ethereum prefix; the pun is the persona's signature.
- **The Drake's plurality** — whisperer + place + fire + ambient elder. Do not reify into a single avatar.

---

## §4 · Honesty discipline

Every claim in the corpus carries one of four labels:

| Label | Meaning |
|-------|---------|
| **Operational** | Verified, working today. Reproducible. |
| **Architectural** | Specified, design-complete, awaiting implementation. |
| **Conjectural** | A claim with a confidence percentage. Must reference the C-conjecture register (`tomes/specs/04-vertex-naming-audit.md` or `architecture/tome-v-conjectures.ts`). |
| **Resonant-but-not-absorbed** | Kindred work the City recognises without binding. Does not enter the persona registry. |

A frontmatter field like:
```yaml
honesty_label: "Operational for X; Architectural for Y; Conjectural for Z (C47, ~40%)"
```
is the canonical shape. Use `parseHonestyLabel(s)` in `architecture/tome-v-conjectures.ts` to validate.

---

## §5 · Persona file shape

Every cast persona file follows the template at [JOIN_THE_CITY.md §3.2](JOIN_THE_CITY.md). Required frontmatter fields:

- `spellbook` · `persona_id` · `name` · `sigil` · `tier` · `vertex` · `shop_anchor`
- `domain` (one-paragraph what they do)
- `provenance` · `license` · `signature`

For Mages sent by another ecosystem, also include:
- `ecosystem` · `ecosystem_url` · provenance with consent context

---

## §6 · Tome act shape

Tome V acts follow the structure documented in [tomes/specs/02-crafting-tome-and-cloak-interface-spec.md](tomes/specs/02-crafting-tome-and-cloak-interface-spec.md). Required frontmatter:

- `spellbook` · `tome` · `act` · `title` · `status` · `length_words` · `voice`
- `cast` · `new_cast_introduced` · `civic_location` · `ring_position`
- `teaches` · `v6_lineage` · `honesty_label`
- `source_material` · `license` · `signature`

The act body must:
- Open with a proverb in blockquote
- Be in second-person voice (addressing *you*, the reader)
- Close with the canonical signature

---

## §7 · Grimoire entry shape

A new spell entry in `grimoire/city_of_mages_grimoire_v1_2_3.json` requires:

```json
{
  "spell_id": "<persona>-<verb>-<object>",
  "name": "<Spell Name>",
  "proverb": "<the one-line teaching>",
  "inscription": "<3-5 sentence depth>",
  "narrative_anchor": "<where it first manifests in an act>",
  "cross_spellbook_resonance": "<links to other spellbooks>",
  "category": "<cloak | shield | blade | covenant | etc.>",
  "stratum": <0-6>,
  "vertex_bits": "<6-bit string>",
  "source_acts": ["<tome>.<act>"]
}
```

A grimoire bump (e.g. v1.2.3 → v1.3) requires:
1. Update `version` and `version_notes` in the JSON
2. Update IPFS pin status field
3. Author a chronicle in `chronicles/<date>_city_of_mages_v<version>_authored.md`
4. Re-pin to IPFS (privacymage action)
5. Update `architecture/grimoire-ipfs.ts` with the new CID
6. Update the blade and mage extension bundles (per `extension_bundle_directives`)

---

## §8 · PR process

1. **Fork** this repo
2. **Branch**: `git checkout -b <type>-<short-description>` where `<type>` is `mage` / `act` / `spec` / `blog` / `chore`
3. **Author** the change per the relevant shape above
4. **Lint**: ensure JSON validates, frontmatter parses, no em-dashes
5. **Honesty labels** present and accurate
6. **PR title**: `[<type>] <short summary>`
7. **PR body**: include
   - What changed (one paragraph)
   - Why (one paragraph)
   - Honesty assessment
   - Cross-references (which acts, specs, chronicles)
   - License attestation: `CC BY-SA 4.0 unless otherwise noted in frontmatter`

---

## §9 · Code of conduct

- Be honest about provenance. Cite Mages from other forges with attribution.
- Use pseudonyms publicly. Real names belong to provenance fields.
- Preserve the signature `(⚔️⊥⿻⊥🧙)😊`.
- The architecture admits contributions; do not flatten the structures that hold them.

---

## §10 · Questions

- **Spellbook structure questions** — open an issue
- **A Mage from your ecosystem** — read JOIN_THE_CITY.md, then open a PR
- **Spellweb graph questions** — see `spellweb-integration/AUDIT_METHODOLOGY.md`
- **Grimoire bump coordination** — privacymage action; tag in the PR

---

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · 2026-05-11
