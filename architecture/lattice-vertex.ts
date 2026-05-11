/**
 * Lattice vertex utilities. The 64-vertex sovereignty lattice is a 6-cube
 * hypercube; each vertex maps to a 6-bit binary. The bits read top-to-bottom
 * as: Protection · Delegation · Memory · Connection · Computation · Value.
 *
 * Used by CastShopConstellation to:
 *   - parse a "V28" string from tome-v-acts data into a vertex number 0-63
 *   - compute the binary representation
 *   - generate a trace path from V0 to the Mage's vertex (one bit-flip per step)
 */

export const DIMENSION_LABELS = [
  'Protection',
  'Delegation',
  'Memory',
  'Connection',
  'Computation',
  'Value',
] as const;

export type DimensionIndex = 0 | 1 | 2 | 3 | 4 | 5;

/**
 * Parse a vertex string like "V28", "V25 (Aletheia)", "V25 · V63 (anchor)".
 * Returns the first valid vertex number it finds, or null.
 */
export function parseVertex(raw: string | undefined): number | null {
  if (!raw) return null;
  const m = raw.match(/V(\d{1,2})/i);
  if (!m) return null;
  const n = parseInt(m[1], 10);
  if (Number.isNaN(n) || n < 0 || n > 63) return null;
  return n;
}

/**
 * Convert a vertex number 0-63 into a 6-bit array.
 * bits[0] = MSB (Protection · weight 32). bits[5] = LSB (Value · weight 1).
 */
export function vertexToBits(vertex: number): number[] {
  return [
    (vertex >> 5) & 1,
    (vertex >> 4) & 1,
    (vertex >> 3) & 1,
    (vertex >> 2) & 1,
    (vertex >> 1) & 1,
    vertex & 1,
  ];
}

/** Inverse: 6-bit array → vertex number. */
export function bitsToVertex(bits: number[]): number {
  return bits.reduce((acc, b, i) => acc | ((b ? 1 : 0) << (5 - i)), 0);
}

/**
 * Trace path from V0 to the target vertex. One bit-flip per step.
 * Returns an ordered list of vertex states, starting at V0 and ending at target.
 *
 * Example: V0 → V28 (011100) flips Memory → Connection → Computation in order.
 *   states: [0, 8, 12, 14] · NOTE: above is wrong, let me redo
 *
 * Actually for V28 = 011100 (bits[0..5] = [0,1,1,1,0,0]):
 *   V0  = 000000
 *   flip bit 1 (Delegation): 010000 = V16
 *   flip bit 2 (Memory):     011000 = V24
 *   flip bit 3 (Connection): 011100 = V28
 *   states: [0, 16, 24, 28]
 *
 * The order of flipping matches dimension index order (Protection first, Value last)
 * so the trace reads canonically.
 */
export function traceFromOrigin(targetVertex: number): number[] {
  const bits = vertexToBits(targetVertex);
  const states: number[] = [0];
  let current = 0;
  for (let i = 0; i < 6; i++) {
    if (bits[i]) {
      current |= 1 << (5 - i);
      states.push(current);
    }
  }
  return states;
}

/**
 * Returns the dimensions (in order) that are active in the target vertex.
 * Used by the constellation animation to label each step.
 */
export function activeDimensions(vertex: number): { index: DimensionIndex; label: string }[] {
  const bits = vertexToBits(vertex);
  const out: { index: DimensionIndex; label: string }[] = [];
  for (let i = 0; i < 6; i++) {
    if (bits[i]) out.push({ index: i as DimensionIndex, label: DIMENSION_LABELS[i] });
  }
  return out;
}
