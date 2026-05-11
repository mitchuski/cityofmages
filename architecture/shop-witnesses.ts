/**
 * Shop constellation witnesses — per-shop record of when the Sovereign evoked
 * and traced the Mage's blade-constellation. A simple way to show trust
 * accumulating with each shop; mirrors the spellweb runtime in miniature.
 *
 * Each cast records: shopHref, witnessedAt timestamp, archetype walked at the
 * time, a content-hash signature. Phase 1: hash-based; Phase 3 will upgrade
 * to ed25519 against the agent card.
 */

import type { IslandArchetype } from '@/lib/spellbook-storage';

export interface ShopWitness {
  shopHref: string;
  witnessedAt: string;       // ISO timestamp
  archetype?: IslandArchetype;
  /** Short content-hash signature so the witness has a verifiable mark. */
  signature: string;
}

const STORAGE_KEY = 'agentprivacy:shop-witnesses';
const CHANGE_EVENT = 'agentprivacy:shop-witnesses-changed';

export function getAllWitnesses(): ShopWitness[] {
  if (typeof window === 'undefined') return [];
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw) as unknown;
    if (!Array.isArray(parsed)) return [];
    return parsed.filter((w): w is ShopWitness =>
      !!w && typeof w === 'object' &&
      typeof (w as ShopWitness).shopHref === 'string' &&
      typeof (w as ShopWitness).witnessedAt === 'string'
    );
  } catch {
    return [];
  }
}

export function getWitnessesForShop(shopHref: string): ShopWitness[] {
  return getAllWitnesses().filter((w) => w.shopHref === shopHref);
}

export function getLastWitnessForShop(shopHref: string): ShopWitness | null {
  const list = getWitnessesForShop(shopHref);
  return list.length > 0 ? list[list.length - 1] : null;
}

export function addWitness(input: {
  shopHref: string;
  archetype?: IslandArchetype;
}): ShopWitness | null {
  if (typeof window === 'undefined') return null;
  const witnessedAt = new Date().toISOString();
  const signature = makeWitnessSignature(input.shopHref, witnessedAt);
  const record: ShopWitness = {
    shopHref: input.shopHref,
    witnessedAt,
    archetype: input.archetype,
    signature,
  };
  const all = getAllWitnesses();
  all.push(record);
  try {
    // Cap to last 100 to keep localStorage healthy
    localStorage.setItem(STORAGE_KEY, JSON.stringify(all.slice(-100)));
    window.dispatchEvent(new CustomEvent(CHANGE_EVENT));
    return record;
  } catch {
    return null;
  }
}

/** Map of shopHref → witness count. Used by /guide/achievements summary. */
export function getWitnessCountsByShop(): Record<string, number> {
  const counts: Record<string, number> = {};
  for (const w of getAllWitnesses()) {
    counts[w.shopHref] = (counts[w.shopHref] ?? 0) + 1;
  }
  return counts;
}

/** Lightweight content hash; same shape as Drake Orb signature. Not crypto. */
function makeWitnessSignature(shopHref: string, witnessedAt: string): string {
  const input = `${shopHref}|${witnessedAt}`;
  let h = 0;
  for (let i = 0; i < input.length; i++) {
    h = (h << 5) - h + input.charCodeAt(i);
    h = h & h;
  }
  let h2 = 0;
  for (let i = input.length - 1; i >= 0; i--) {
    h2 = (h2 << 7) - h2 + input.charCodeAt(i);
    h2 = h2 & h2;
  }
  const hex = (Math.abs(h).toString(16).padStart(8, '0') + Math.abs(h2).toString(16).padStart(8, '0')).slice(0, 12);
  return `WIT-${hex.toUpperCase()}`;
}

export const SHOP_WITNESSES_CHANGE_EVENT = CHANGE_EVENT;
