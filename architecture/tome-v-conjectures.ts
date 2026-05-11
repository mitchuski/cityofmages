/**
 * v6_lineage conjectures — the C-numbered claims that thread through Tome V.
 *
 * Each conjecture has a canonical name, a status (canonical / provisional /
 * observation / resonant), and (where stated) a confidence percentage.
 *
 * The act → conjecture mapping is the inverse-index data for the
 * /tomes/v6-lineage aggregator page and for the inline ConjectureBadge
 * component on FoundingActPanel and act collapsibles.
 *
 * Source: docs/tomes/tome-v-the-crafting/*.md frontmatter.
 */

export type ConjectureStatus = 'canonical' | 'provisional' | 'observation' | 'resonant';

export interface ConjectureDefinition {
  /** Range identifier (e.g. "C26-C29" for a multi-vertex band, or "C40" for a single one). */
  id: string;
  /** Canonical short name (e.g. "ARCH-1", "Bakhta Half-Life"). */
  name: string;
  status: ConjectureStatus;
  /** 0..1; null if status is canonical (taken as 1.0) or open observation. */
  confidence: number | null;
  /** Plain-language one-liner of what the conjecture says. */
  oneLiner: string;
}

/** Canonical definitions referenced across Tome V (and accumulating). */
export const CONJECTURE_DEFINITIONS: Record<string, ConjectureDefinition> = {
  'C18-C21': {
    id: 'C18-C21',
    name: 'Lorenz Attractor',
    status: 'canonical',
    confidence: 1.0,
    oneLiner: 'The RUN phase walks an attractor — trajectory is the framing.',
  },
  'C22-C25': {
    id: 'C22-C25',
    name: 'EML Three Ceilings',
    status: 'canonical',
    confidence: 1.0,
    oneLiner: 'Three computational ceilings the CRAFT phase must respect.',
  },
  'C26-C29': {
    id: 'C26-C29',
    name: 'ARCH-1 Canonical Form',
    status: 'canonical',
    confidence: 1.0,
    oneLiner: 'Σ := μS.(β ∨ Ω(S,S)) — the recursive μ-fixpoint admits multiple inhabitants.',
  },
  'C30-C33': {
    id: 'C30-C33',
    name: 'Bakhta Half-Life',
    status: 'canonical',
    confidence: 1.0,
    oneLiner: 'Trust accumulates in arcs and decays with a half-life that begins at inscription.',
  },
  'C34-C37': {
    id: 'C34-C37',
    name: 'Wound and Cap · Convergence',
    status: 'canonical',
    confidence: 1.0,
    oneLiner: 'The cloak is the operational instance of the convergence claim.',
  },
  C38: {
    id: 'C38',
    name: 'Bilateral ARCH-1',
    status: 'provisional',
    confidence: 0.4,
    oneLiner: 'Σ_{ij} := μS.(β_{ij} ∨ Ω(S_i, S_j)) — bilateral fold of the canonical form.',
  },
  C39: {
    id: 'C39',
    name: 'Kindred-Blade as Ecosystem Primitive',
    status: 'provisional',
    confidence: 0.5,
    oneLiner: 'Kindred-blade primitives — any Mage\'s vertex catalogue regardless of forge — are agent-ecosystem-grade citizens of the lattice. Reframed 2026-05-10 from "cousin-blade": we are all just another mage.',
  },
  C40: {
    id: 'C40',
    name: 'Zcash Dual-Ledger Preservation',
    status: 'provisional',
    confidence: 0.7,
    oneLiner: 'Zcash dual-ledger preserves the Cloak\'s Eight Properties across shielded and transparent registers.',
  },
  C41: {
    id: 'C41',
    name: '61.8 / 38.2 Inscription Ratio',
    status: 'observation',
    confidence: null,
    oneLiner: 'The transparent/shielded inscription ratio appears to settle near the golden ratio as cultural emergence.',
  },
  C42: {
    id: 'C42',
    name: 'Stake Economics Sybil Resistance',
    status: 'provisional',
    confidence: 0.5,
    oneLiner: 'Stake economics generate Sybil resistance equivalent to or stronger than tier accumulation.',
  },
  C43: {
    id: 'C43',
    name: 'Per-VRC Viewing-Key Privacy',
    status: 'provisional',
    confidence: 0.6,
    oneLiner: 'Per-VRC viewing-key disclosure produces strictly more privacy than uniform disclosure.',
  },
  C44: {
    id: 'C44',
    name: 'Productive Trust-Edge Formation',
    status: 'provisional',
    confidence: 0.55,
    oneLiner: 'Trust edges form productively (not transactionally) when work is rendered as service.',
  },
  C45: {
    id: 'C45',
    name: 'Four-Chain Publication Preservation',
    status: 'provisional',
    confidence: 0.7,
    oneLiner: 'Four-chain publication preserves reconstruction-resistance across artifact types.',
  },
  C46: {
    id: 'C46',
    name: 'Productive Trust-Edge Half-Life',
    status: 'provisional',
    confidence: 0.5,
    oneLiner: 'Productive trust-edges have higher half-life than transactional ones.',
  },
  C47: {
    id: 'C47',
    name: 'Triadic-Constraint Homology',
    status: 'provisional',
    confidence: 0.4,
    oneLiner: 'agentprivacy\'s three-axis Φ_agent · Φ_data · Φ_inference and PRISM\'s triadic Datum · Stratum · Spectrum are instances of a deeper triadic primitive.',
  },
};

/** Per-act conjecture references with the act-specific note. */
export interface ConjectureRef {
  /** Maps to a key in CONJECTURE_DEFINITIONS. */
  id: string;
  /** Act-specific note about how this act touches the conjecture. */
  note: string;
}

/** Tome V act → conjectures it instances or strengthens. */
export const ACT_CONJECTURES: Record<number, ConjectureRef[]> = {
  1: [
    { id: 'C26-C29', note: 'Pallia is the user\'s own — recursive form admits multiple inhabitants.' },
    { id: 'C34-C37', note: 'The cloak is the operational instance of the convergence claim.' },
    { id: 'C39',     note: 'Pallia walks a path opened by another forge.' },
  ],
  2: [
    { id: 'C26-C29', note: 'The bilateral commission as a fixpoint instance.' },
    { id: 'C30-C33', note: 'Tip + proof + cloak each carry their own half-life.' },
    { id: 'C38',     note: 'Bilateral commission as the operational instance.' },
    { id: 'C40',     note: 'Tested in shielded register.' },
  ],
  3: [
    { id: 'C30-C33', note: 'Half-life of trust begins ticking from inscription.' },
    { id: 'C40',     note: 'Tested in shielded register.' },
    { id: 'C41',     note: 'Cultural emergence of the 61.8/38.2 ratio.' },
    { id: 'C43',     note: 'Per-VRC viewing-key disclosure.' },
  ],
  4: [
    { id: 'C30-C33', note: 'Reveal adds a new accumulation arc.' },
    { id: 'C40',     note: 'Tests the across-register transition.' },
    { id: 'C46',     note: 'Productive trust survives the reveal because earned by inscription.' },
  ],
  5: [
    { id: 'C30-C33', note: 'Governance acts accumulate trust through witnessability.' },
    { id: 'C40',     note: 'Tests the transparent leg.' },
    { id: 'C41',     note: 'Transparent side of the ratio.' },
    { id: 'C42',     note: 'Stake economics generate Sybil resistance.' },
  ],
  6: [
    { id: 'C18-C21', note: 'RUN phase walks an attractor in production.' },
    { id: 'C22-C25', note: 'CRAFT phase respects the three computational ceilings.' },
    { id: 'C26-C29', note: 'Blade vertex assignment is itself a fixpoint instance.' },
    { id: 'C44',     note: 'Productive VRC formation through blade commissioning.' },
    { id: 'C45',     note: 'Four-chain publication preserved across artifact types.' },
  ],
  7: [
    { id: 'C26-C29', note: 'The recursive form admits the bilateral fold.' },
    { id: 'C38',     note: 'Strengthened by operational instancing.' },
    { id: 'C39',     note: 'Strengthened — cousin-blade in productive form.' },
    { id: 'C44',     note: 'Strengthened — reciprocal service.' },
  ],
  8: [
    { id: 'C22-C25', note: 'Computational ceilings as integrity, not obstacle.' },
    { id: 'C26-C29', note: 'ZK proofs of self-reference admitted.' },
    { id: 'C40',     note: 'Extended to ZK-bound artifacts.' },
    { id: 'C45',     note: 'Strengthened — ZK-bound artifacts publish the same way.' },
  ],
  9: [
    { id: 'C30-C33', note: 'Half-life curve gets new shape from frequent small attestations.' },
    { id: 'C40',     note: 'Extended to a fuller registry quartet.' },
    { id: 'C45',     note: 'Strengthened across two crafting registers.' },
    { id: 'C44',     note: 'Strengthened — expanded shop variety.' },
  ],
  10: [
    { id: 'C26-C29', note: 'First narrative crafting instance of the holonic primitive.' },
    { id: 'C34-C37', note: 'Convergence at the artifact level instances as holonic composition.' },
    { id: 'C39',     note: 'Strengthened — cousin-blade composition into agentprivacy-native wholes.' },
    { id: 'C45',     note: 'Strengthened across composed artifacts and Oasis links.' },
  ],
  11: [
    { id: 'C26-C29', note: 'Recursive μ-fixpoint admits new geographic structures.' },
    { id: 'C39',     note: 'Strengthened at the cross-spot resolution.' },
    { id: 'C44',     note: 'Strengthened through dialogic work, illuminated by the cooperation\'s own fire.' },
  ],
  12: [
    { id: 'C26-C29', note: 'Recursive μ-fixpoint admits the persona-vertex distinction without breaking coherence.' },
    { id: 'C39',     note: 'Strengthened at the cross-shop resolution.' },
    { id: 'C44',     note: 'Strengthened — curatorial and self-reflective work.' },
  ],
  13: [
    { id: 'C26-C29', note: 'Admits new cast tiers without breaking coherence — Priest joins the four Mage tiers.' },
    { id: 'C39',     note: 'Strengthened at the cross-protocol resolution; the Covenant is a kindred protocol.' },
    { id: 'C44',     note: 'Strengthened through ceremonial consecration.' },
  ],
  14: [
    { id: 'C26-C29', note: 'Recursive μ-fixpoint admits civic structures at multiple resolutions.' },
    { id: 'C39',     note: 'Strengthened — *First* City naming admits that other cities exist or will exist.' },
    { id: 'C45',     note: 'Strengthened — operates at the civic-coordination level.' },
  ],
  15: [
    { id: 'C26-C29', note: 'Strengthened by external resonance — UOR\'s critical identity neg(bnot(x)) = succ(x) is structurally adjacent to the recursive μ-fixpoint.' },
    { id: 'C39',     note: 'Scope expanded — cousin-substrate (UOR Foundation) is a higher-order form of cousin-blade; the City may rest upon a kindred substrate without subsuming it.' },
    { id: 'C47',     note: 'New conjecture — three-axis Φ × triadic Datum·Stratum·Spectrum homology, anchored by Vagari\'s cross-frame travel and Vulcana\'s computational confinement.' },
  ],
};

/** Inverse index: conjecture id → list of acts that reference it. Used by /tomes/v6-lineage. */
export function getActsForConjecture(conjId: string): { actNumber: number; note: string }[] {
  const out: { actNumber: number; note: string }[] = [];
  for (const [act, refs] of Object.entries(ACT_CONJECTURES)) {
    for (const r of refs) {
      if (r.id === conjId) out.push({ actNumber: parseInt(act, 10), note: r.note });
    }
  }
  return out.sort((a, b) => a.actNumber - b.actNumber);
}

/**
 * Honesty discipline — per the Tomes voice rules, every claim wears a label.
 * Operational / Architectural / Conjectural / Resonant / Provisional / Narrative.
 */
export type HonestyStance = 'operational' | 'architectural' | 'conjectural' | 'resonant' | 'provisional' | 'narrative';

export interface HonestyClause {
  stance: HonestyStance;
  /** What the stance applies to. */
  claim: string;
}

/**
 * Parses an honesty_label frontmatter string like:
 *   "Operational for X; Architectural for Y; Provisional for Z"
 * into structured clauses. Best-effort; falls back to a single clause if parsing fails.
 */
export function parseHonestyLabel(raw: string | undefined): HonestyClause[] {
  if (!raw) return [];
  const stances: HonestyStance[] = ['operational', 'architectural', 'conjectural', 'resonant', 'provisional', 'narrative'];
  const parts = raw.split(/;\s*/);
  const clauses: HonestyClause[] = [];
  for (const part of parts) {
    const lower = part.toLowerCase();
    const stance = stances.find((s) => lower.startsWith(s)) ?? null;
    if (stance) {
      // Strip the leading stance word + " for "
      const rest = part.replace(new RegExp(`^${stance}\\s+for\\s+`, 'i'), '').trim();
      clauses.push({ stance, claim: rest });
    } else {
      // Fallback — couldn't classify
      clauses.push({ stance: 'narrative', claim: part.trim() });
    }
  }
  return clauses;
}
