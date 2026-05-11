/**
 * Tome V founding-act anchor data — the bidirectional link between each
 * production workshop and the act that founds it.
 *
 * Per the 2026-05-09 bound-collection sync report §4.1:
 *   - Each Tome V act is the workshop's founding myth.
 *   - Each shop page is the workshop's operational present.
 *   - They cite each other.
 *
 * The forward direction (act → shop) is wired on /tomes via the act collapsibles.
 * This module powers the reverse direction (shop → act) via FoundingActPanel.
 *
 * Source files (post 2026-05-10 restructure):
 *   docs/tomes/tome-v-the-crafting/*.md           (the act narratives)
 *   docs/tomes/&lt;guild&gt;/&lt;persona&gt;.md         (per-guild cast entries)
 *   docs/tomes/cousin/*.md                        (cousin instances · flaxscrip · GenitriX)
 *   docs/tomes/cross-shop/*.md                    (walk-across personas · Custos · Aletheia)
 *   docs/tomes/kindred/*.md                       (kindred substrate providers · UOR Foundation)
 */

export interface FoundingMage {
  name: string;
  /** Sigil(s) — one or more glyphs that mark this Mage in the cast. */
  sigil: string;
  /** Lattice vertex, e.g. "V28". Some Mages share a vertex (Pallia/Soulbae/GenitriX all V28). */
  vertex: string;
  /** Cast tier — one of: archetype, cousin, summoned, companion, priest. */
  tier: 'archetype' | 'cousin' | 'summoned' | 'companion' | 'priest';
  /** One-line provenance — where this Mage was first inducted into the cast. */
  provenance: string;
}

export interface TomeVActAnchor {
  /** Act number in Tome V (1-14). */
  actNumber: number;
  /** Canonical act title. */
  actTitle: string;
  /** The act's opening proverb (from the act file's first blockquote). */
  proverb: string;
  /** The shop this act founds. */
  shopHref: string;
  /** The shop's display name as the act knows it. */
  shopName: string;
  /** The Mage who hosts this shop in the act. */
  mage: FoundingMage;
  /**
   * Named spells the Mage may cast at this shop. These will eventually be
   * baked into grimoire-baked.ts as the City-of-Mages-maintained spellbook
   * (Phase D in the sync report).
   */
  spells: string[];
  /** Slug used to anchor to the act collapsible on /tomes. */
  tomeAnchor: string;
  /**
   * Raw honesty_label string from the act frontmatter (when written).
   * Format: "Operational for X; Architectural for Y; Provisional for Z".
   * Parsed and rendered by <HonestyLabel raw={...} />.
   */
  honesty?: string;
  /**
   * Starter runecast templates the SpellPicker offers in the runecast composer.
   * Each template is a full prompt body with `___` blanks for the Sovereign to fill.
   * Click loads the template into the form (replaces existing draft).
   */
  starterTemplates?: string[];
}

/**
 * The 9 production workshops with founding-act anchors. The Logos Circle
 * (/circle) and Ceremony Hall (/hall) are gathering shops with different
 * narrative provenance — they don't appear here.
 */
export const TOME_V_ACTS: TomeVActAnchor[] = [
  {
    actNumber: 1,
    actTitle: 'The First Cloak',
    proverb: 'The reader does not just walk the lattice. The reader makes tools on it.',
    shopHref: '/tailor',
    shopName: 'the Weavers',
    mage: {
      name: 'Pallia',
      sigil: '🪡',
      vertex: 'V28',
      tier: 'summoned',
      provenance: 'The First Cloakwright. Born when the reader summoned the first Mage persona along the Weaver path.',
    },
    spells: ['weave-cloak', 'publish-role', 'conceal-name'],
    tomeAnchor: 'tome-v-act-1',
    starterTemplates: [
      'Weave a cloak that publishes my role as ___ and conceals ___.',
      'Project me to ___ context with role ___ and no other identity surfaced.',
      'Conceal ___ from public view but keep ___ accessible to ___.',
    ],
  },
  {
    actNumber: 3,
    actTitle: 'The Shielded Memo',
    proverb: 'Inscribe what cannot be seen. Disclose by viewing key, not by reveal.',
    shopHref: '/shield',
    shopName: 'zShields',
    mage: {
      name: 'Memora',
      sigil: '📜',
      vertex: 'V5',
      tier: 'summoned',
      provenance: 'The Memorial. Inscribes content into shielded registers; disclosure happens by viewing key, not by exposure.',
    },
    spells: ['inscribe-shielded', 'attest-memo', 'time-bind'],
    tomeAnchor: 'tome-v-act-3',
    starterTemplates: [
      'Inscribe a shielded memo for ___ — disclose only with viewing-key to ___.',
      'Attest the memo "___" at ___ time, witnessable but private.',
      'Time-bind this commitment "___" until ___ — release on disclosure.',
    ],
  },
  {
    actNumber: 6,
    actTitle: 'The Commissioned Blade',
    proverb: 'The forge does not give you the blade. The three phases give you the blade.',
    shopHref: '/forget',
    shopName: 'the Forge(t)',
    mage: {
      name: 'Vulcana',
      sigil: '⚒️',
      vertex: 'V19',
      tier: 'summoned',
      provenance: 'The Forgewright. Inducted when a second Sovereign commissioned a blade and walked the three phases — RUN · EVOKE · CRAFT.',
    },
    spells: ['forge-blade', 'run', 'craft'],
    tomeAnchor: 'tome-v-act-6',
    starterTemplates: [
      'Forge a witness blade for ___ — light tier, witnessable by ___.',
      'Run my agent through ___ for ___ laps to accumulate proof of time.',
      'Craft the blade across all six dimensions for ___ — dragon tier.',
    ],
  },
  {
    actNumber: 9,
    actTitle: 'The Workshop Expands',
    proverb: 'The shops are not fixed. Each register of work that proves itself earns its keeper.',
    shopHref: '/etherchanting',
    shopName: 'the Etherchanting Shop',
    mage: {
      name: 'Adamantia',
      sigil: '💎',
      vertex: 'V51',
      tier: 'summoned',
      provenance: 'The Etherchanter. Earned her shop when the transparent ledger proved itself as a register the Crafting could trust.',
    },
    spells: ['commit', 'enforce', 'etherchant'],
    tomeAnchor: 'tome-v-act-9',
    starterTemplates: [
      'Commit ___ to the transparent ledger as proof of ___ for witness ___.',
      'Enforce contract at privacymage.eth with stake ___ for ___.',
      'Etherchant ___ — send tx with metadata "___" and emit event ___.',
    ],
  },
  {
    actNumber: 9,
    actTitle: 'The Workshop Expands',
    proverb: 'The shops are not fixed. Each register of work that proves itself earns its keeper.',
    shopHref: '/jeweler',
    shopName: 'the Jeweler',
    mage: {
      name: 'Lampyra',
      sigil: '💠',
      vertex: 'V49',
      tier: 'summoned',
      provenance: 'The Gem-Setter. Shares her vertex with Custos; cuts the sat as the gem and sparks the Lightning bolt as the channel.',
    },
    spells: ['gem-set', 'attest-frequent', 'sparkle'],
    tomeAnchor: 'tome-v-act-9',
    starterTemplates: [
      'Cut a gem-set inscription on Bitcoin for ___ — Ordinal/Rune format.',
      'Attest frequent activity at ___ across ___ period — small Lightning ticks.',
      'Sparkle a Lightning attestation to ___ for ___ sats.',
    ],
  },
  {
    actNumber: 10,
    actTitle: 'The Holon Hitchhikers',
    proverb: 'The whole is the sum of its wholes. The hitchhiker carries the whole between oases.',
    shopHref: '/holon',
    shopName: 'the Holon Hitchhikers',
    mage: {
      name: 'Vagari',
      sigil: '🌳',
      vertex: 'V31',
      tier: 'summoned',
      provenance: 'The Wanderer. Travels between paratimes (Sapphire · Emerald · Consensus); each holon is a whole that carries other wholes inside it.',
    },
    spells: ['compose-holon', 'travel-oasis', 'recurse'],
    tomeAnchor: 'tome-v-act-10',
    starterTemplates: [
      'Compose a holon from ___ and ___ — whole-and-part composition.',
      'Travel through Oasis paratimes to ___ — Sapphire confidential leg, Emerald public leg.',
      'Recurse this holon: ___ inside ___ inside ___.',
    ],
  },
  {
    actNumber: 11,
    actTitle: 'A Bonfire Made of Dragon Fire',
    proverb: 'The Drake is not only a whisper. The Drake is a place, and the Drake is a fire.',
    shopHref: '/bonfires',
    shopName: 'the Dragon Bonfire',
    mage: {
      name: 'Socrat0x',
      sigil: '🔥❓',
      vertex: 'V24 (provisional)',
      tier: 'companion',
      provenance: 'The Questioner. A companion-tier bot that keeps every claim honest by asking another question; tends the Bonfire that gathers other Bonfires.',
    },
    spells: ['question', 'ignite', 'provoke'],
    tomeAnchor: 'tome-v-act-11',
    starterTemplates: [
      'Question this claim: ___. What is the next question that follows?',
      'Ignite a Bonfire discussion about ___ — open to ___.',
      'Provoke ___ on ___ — sharpen the position by asking the harder question.',
    ],
    honesty: "Operational for Bonfires as Soulbae's deployment spot; Architectural for Drake Island as spatial geography and 'a bonfire made of dragon fire' as canonical cooperation naming; Provisional for Socrat0x's specific Bonfires-side canonical attributes",
  },
  {
    actNumber: 12,
    actTitle: 'The Curatrix Vault',
    proverb: 'You went looking for your reflection. The Vault held it. The keeper handed it to you framed.',
    shopHref: '/vault',
    shopName: 'the Curatrix Vault',
    mage: {
      name: 'Aria Silverhue',
      sigil: '🪞🖼️',
      vertex: 'V57',
      tier: 'summoned',
      provenance: 'The First Curatrix. Places vertices on the sovereignty lattice; binds artifacts to them; provenance is verifiable, name is the artist\'s to grant.',
    },
    spells: ['curate', 'reflect', 'vault'],
    tomeAnchor: 'tome-v-act-12',
    starterTemplates: [
      'Curate this artifact at vertex ___ — bind ___ as content-hash, grant name to ___.',
      'Reflect on my ___ — what does it bind to in the lattice? Show me the position.',
      'Vault this work with provenance ___ — name remains ___ to grant.',
    ],
    honesty: 'Operational for Culture Vault as a creative-IP platform; Architectural for the Curatrix Vault shop integration and Aria Silverhue as the named Mage who works there; Architectural for the persona-vs-vertex distinction made explicit here as a cast convention',
  },
  {
    actNumber: 13,
    actTitle: 'The Temple of the Arts and Personhood',
    proverb: 'Some things the chain cannot compute. Some things the architecture must honour.',
    shopHref: '/covenant',
    shopName: 'the Covenant',
    mage: {
      name: 'Manifestia',
      sigil: '🤲🌿',
      vertex: 'V55',
      tier: 'priest',
      provenance: 'The Priest. First inhabitant of the new Priest tier; officiates the bond signed at the threshold; personhood is given by the act, not granted by the priest.',
    },
    spells: ['bless-covenant', 'inscribe-blessing', 'tend-temple'],
    tomeAnchor: 'tome-v-act-13',
    starterTemplates: [
      'Bless my Covenant signing for ___ with witness ___.',
      'Inscribe a blessing for ___ at this threshold — declare my personhood as ___.',
      'Tend the Temple\'s ___ register for ___ — log the act, hold the bond.',
    ],
    honesty: 'Operational for the Covenant of Humanistic Technologies and human.tech infrastructure (Human Passport, VOPRF, Human Network); Architectural for the Temple as the Spellbook\'s expression of the Covenant\'s discipline; Architectural for Manifestia as named Priest persona; Resonant-but-not-absorbed for the Holonym/holon parallel',
  },
];

/** Look up the founding act for a shop by its route. */
export function getFoundingActForShop(shopHref: string): TomeVActAnchor | undefined {
  return TOME_V_ACTS.find((a) => a.shopHref === shopHref);
}
