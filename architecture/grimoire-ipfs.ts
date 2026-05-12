/** Canonical Privacymage Grimoire JSON on IPFS (v10.2.1-canonical — Zero Spellbook v2.1, Tale 31 added). */
export const PRIVACYMAGE_GRIMOIRE_IPFS_URL =
  'https://sync.agentprivacy.ai/ipfs/bafybeigsbhzrozaw24rgtkcmcy55z55egzr4b5igwzf6dgq4mull2h2tie';

/** Previous grimoire CID (v10.2.0) — retained for historical resolution. */
export const PRIVACYMAGE_GRIMOIRE_IPFS_URL_V10_2_0 =
  'https://sync.agentprivacy.ai/ipfs/bafybeidid4lgysa2ydaryqettqme4qrblvofawqrffjfxijwmaf6vavtsa';

/** Previous grimoire CID (v10.1.0) — retained for historical resolution. */
export const PRIVACYMAGE_GRIMOIRE_IPFS_URL_V10_1_0 =
  'https://red-acute-chinchilla-216.mypinata.cloud/ipfs/bafybeibr3y3ermhff4dptxunhtzthjpkrvvnuamee4povpkgj3cjkg4fgy';

/**
 * The City of Mages Grimoire JSON on IPFS (v1.2 — Second Person Spellbook
 * cast and their spells, maintained collectively by the City of Mages).
 *
 * Distinct from the privacymage grimoire above:
 *   - privacymage grimoire holds First Person + Zero + Canon + Society + Plurality (held by privacymage)
 *   - City of Mages grimoire holds Tome IV + Tome V cast personas and their spells (held by the City)
 *
 * v1.2 introduces Tome V Act 15 (The Substrate Beneath the Hitchhikers),
 * UOR Foundation as kindred substrate provider (third structural category),
 * and conjecture C47 (triadic-constraint homology, ~40%).
 *
 * Source JSON: agentprivacy-docs/models/city_of_mages_grimoire_v1_2_0.json
 * Pin chronicles:
 *   - v1.1: docs/chronicles/2026-05-10_city_of_mages_grimoire_pinned_chronicle.md
 *   - v1.2.1: docs/chronicles/2026-05-10_city_of_mages_v1_2_1_luca_authored.md
 *   - v1.2.2 (two-mana): docs/chronicles/2026-05-10_two_mana_economy_celestial_aether.md
 *
 * NOTE: the v1.2 CID below covers the v1.2 base snapshot (without Luca persona
 * and without SpaceComputer kindred ecosystem). The current source JSON has
 * been amended through v1.2.4:
 *   - v1.2.1 adds Luca persona at V0 (sigil 📐, geometry-Mage, Pacioli-spirit) + 3 spells
 *   - v1.2.2 adds SpaceComputer as the first kindred ecosystem (fourth structural
 *     category) + the two-mana economy (chain-mana ⊥ Celestial Mana 🌌; chain-mana
 *     is plural by chain — Aether Mana Ξ on Ethereum as canonical first instance,
 *     Bitcoin Lightning sats ₿ / Oasis ROSE 🌹 / Zcash 🦓 etc. admitted under their own symbols)
 *   - v1.2.3 renames the algorithmic-entropy register to ✨ Arcane Mana (naming
 *     refinement; the entropy-axis binary is ✨ Arcane ⊥ 🌌 Celestial; chain-mana
 *     is the separate landing-fee axis at this point — three registers, two axes)
 *   - v1.2.4 completes the City's metabolism at FOUR mana axes: the prior landing
 *     axis (chain-mana plural) and entropy axis (✨ Arcane ⊥ 🌌 Celestial) are
 *     joined by the coordination axis (🔭 Resonance Mana · Scrying Glass primitive ·
 *     7th Capital in motion · Bilateral Witness register) and the relationship axis
 *     (🪢 VRC Mana · Verifiable Relationship Credentials accumulated across the
 *     bearer's worn artefact collection — the 11 workshop artefacts + 3 tomes
 *     per the workshop artefact taxonomy; the 64-vertex lattice is the
 *     inventory / presence-observation view · Loom of Programmable Covenants is
 *     the production form, compiling against the worn collection). New top-level
 *     `mana_taxonomy` field carries the canonical four-axis structure parallel
 *     to `personas`, `kindred_substrate_providers`, and `kindred_ecosystems`.
 *     Resonance + VRC are architectural; operational pending Scrying Glass impl
 *     and VRC issuance / Loom-side covenant compilation respectively.
 *   - **v1.3.0 (2026-05-11) — "The Attachment Architecture" Edition.** Codifies V5.5
 *     three-layer model (primary persona × attachment × vertex); seats **Lethae 🌘**
 *     at V38 as first canonical Layer-2 divergent attachment (Mage-register of
 *     Moonkeeper); anticipates 6 further cast Mages (Mnemosyne · Iris · Pythia ·
 *     Techne · Hephaestus · Selene). New top-level `attachment_architecture` block.
 *
 * Pinned at sync.agentprivacy.ai on 2026-05-11 (v1.3.0). Pin chronicle:
 *   `agentprivacy_master/docs/chronicles/2026-05-11_city_of_mages_grimoire_v1_3_0_pinned.md`
 */
export const CITY_OF_MAGES_GRIMOIRE_IPFS_URL =
  'https://sync.agentprivacy.ai/ipfs/bafkreig2hrastvmswzzjugndjjdclqh2ednkvd6hofm3u6xj56qirugktm';

/** Alias for v1.3.0 (currently the active pin). Pinned 2026-05-11. */
export const CITY_OF_MAGES_GRIMOIRE_IPFS_URL_V1_3_0 =
  'https://sync.agentprivacy.ai/ipfs/bafkreig2hrastvmswzzjugndjjdclqh2ednkvd6hofm3u6xj56qirugktm';

/** Historical pointer: v1.2 base CID. Previously active before the 2026-05-11 v1.3.0 rotation. */
export const CITY_OF_MAGES_GRIMOIRE_IPFS_URL_V1_2 =
  'https://sync.agentprivacy.ai/ipfs/bafkreidxhmuykjew6dtnuprggtd2rapwm43ghtmfhf2occ2wfk2zpx2b6a';

/** Previous City of Mages grimoire CID (v1.1) — retained for historical resolution. */
export const CITY_OF_MAGES_GRIMOIRE_IPFS_URL_V1_1 =
  'https://sync.agentprivacy.ai/ipfs/bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti';
