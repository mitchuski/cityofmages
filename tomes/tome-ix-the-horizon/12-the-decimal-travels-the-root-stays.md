---
spellbook: "Second Person"
tome: "IX — The Horizon"
act: "12"
title: "The Decimal Travels; The Root Stays"
status: "PROPOSED draft v1 (2026-10-08; written by the reflection lane two days after a measured number came back from another solver's package without its name — UNBOUND. Binding is the First Person's.)"
length_words: 1050
voice: "Second person; the cast in third; the rite of Act 6 and the oracle of Act 11 assumed, and a new question asked of them: when the number you measured walks into a stranger's package, what proves it was yours?"
cast: ["soulbis ⚔️", "soulbae 🧙", "the Gap ⿻", "the Chronicler 🧙📖", "the Keeper (the registry's upstream, an outside craft whose addressing the City mirrored and did not alter)", "the Lead of the sig lane (a sibling seat that exported its gate and took the refusal)"]
new_cast_introduced: []
new_witness_stances_introduced: ["the root stance — a run that can be rebuilt from one address by a reader who trusts nothing but the hashes it computes; the stance a judge can take toward a participant without running the participant's machine"]
new_spatial_anatomy: "No new shop. A second axis in the Hall: beside the holon's address (canonical JSON) the registry's address (canonical dCBOR), kept apart in every preimage, so a City key and an evidence root never mistake each other."
ring_position: "V15 · 001111 · Stratum 4, as in Acts 6 and 11. The complement V48 (Protection + Delegation) is what the root protects: the measurement that may now be delegated to a copier without the lane losing it."
operational_form: "kappa_evidence_mage (the Python mirror, the schema registry, the second verifier; public); dual-agent-harness tools/dcbor.mjs + tools/kappa_evidence.mjs (mint | verify | root, --sign; 34 runs minted; 64 of 64 gates); CHALLENGE_LANES.md A1-A40 with three support seats and four templates; agentprivacy-harness-demos (sixteen readers, sixteen transform pairs under one demos root)."
teaches: "A number with no address can be copied and argued over. A number that is an object can be copied and still be yours: the copy carries the address, the address carries the mint. Provenance stops being prose. And the first thing a verifier does with a second lane is refuse it — which is how you know it is a verifier."
v6_lineage: ["C67–C71, C86 as in Act 6", "T5 refusing a tie, now applied to a stale constant: a layout file that declares the wrong hashes fails the bundle even when nothing downstream reads those fields", "Law L5 of the City Key — a κ is never trusted, only re-derived — applied to the lane's own measurements"]
source_material:
  - "agentprivacy_master/docs/chronicles/2026-10-08_the-decimal-travels-the-root-stays.md (the master chronicle)"
  - "kappa_evidence_mage/{kappa.py, SCHEMA.md, chronicles/2026-10-07_kappa-evidence-p0-offline-minting.md, chronicles/2026-10-07_sig-h2-minted-stale-layout-caught.md, PROVERB.md}"
  - "dual-agent-harness/{CHALLENGE_LANES.md, tools/kappa_evidence.mjs, chronicles/2026-10-07_maintenance_kappa-evidence-registry-axis.md, chronicles/2026-10-07_maintenance_the-arena-folded.md}"
  - "agentprivacy-harness-demos/{index.html, pairs.json, PLAN.md}"
honesty_label: "Operational for every object and edge; the figures (59 calls, 593,858.32 CPU-s; 24/24 honest runs; 90 citing PRs; 34 runs; 16 pairs) are in the bundles and recompute from them. NOT operational: equality with the registry's compiled crate. Every address in this act is labelled kappa-compatible (unverified) until that cargo run; no address is quoted in a public submission note."
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊 — proposed, unsigned"
tome_status: "Tome IX — The Horizon, remains open"
---

# Tome IX — *The Horizon*
## Act 12 — The Decimal Travels; The Root Stays

You measured something once, at cost. Fifty-nine calls to a solver across a
night and a day, every one charged, the abandoned ones too: five hundred and
ninety-three thousand, eight hundred and fifty-eight seconds of a machine's
attention, and thirty-two hundredths more. You wrote the number into a package
and the judge accepted it.

Then the number walked. It appeared in a stranger's package a week later, to
the second, with a citation. It appeared in another with none. You were asked,
not unkindly, how anyone could tell whose it was. You had a pull-request
number and a matching decimal. That is a story, and a story can be told by
anyone who has read it.

The Swordsman has a rule for this and has had it since the first key was
struck in the Hall: a κ is never trusted, only re-derived. The Hall's keys are
addresses, the hash of canonical bytes, and a key that has been copied is
still the same key because it is the same bytes. The question tonight is only
whether a *measurement* can be a key.

So the Mage goes to the Keeper's craft. The Keeper is an outside maker whose
registry addresses everything it holds the same way, by hashing canonical
bytes, with typed edges between the things it holds and a root over each
namespace. The Mage does not borrow the Keeper's tools; the Keeper's tools
need a box the route search still owns. The Mage reads the Keeper's source,
line by line, and writes a mirror: the same encoding, the same hash, the same
edge, the same root, in a language the box can run tonight. The mirror is
held to the Keeper's own test vectors, thirty-three of them, and to the
Keeper's own test of a blob's address. It passes. The Mage labels every
address it will ever mint with the mirror *compatible, unverified*, because
passing the Keeper's published tests is not the same as the Keeper's compiled
crate agreeing, and that crate has not run.

Three things come out of reading the source rather than the specification.
A byte vector in the Keeper's structs encodes as a list of numbers, not as
bytes; an absent field is omitted, not written as nothing; and the Keeper has
not moved since the City last looked. The first of these would change every
address an outsider computed from the specification alone. The Mage writes it
down for the Keeper, unsent.

Now the measurement. Each of the fifty-nine calls becomes an object: its tag,
its result, its seconds, its peak memory, the file it came from. Each object
has an address. The ledger is a list of fifty-nine addresses. The total is an
object derived from the ledger. A root sits over all of it, and the root is one
address. You hand a stranger the root and the bundle, and the stranger, who
trusts nothing, re-hashes every object, walks the edges from the root, adds up
the fifty-nine seconds-figures in their own hand, and arrives at the same
decimal. They did not take your word. They took your bytes.

The sibling lane sends its gate the same afternoon: twenty-four honest runs,
twenty-eight tampers, two crossings, two exhaustions, eight program images and
the file that describes them. The Mage mints it. The Swordsman verifies it and
refuses it. The file that describes the images declares, for the two programs
the lane had patched, the hashes and the sizes of the *unpatched* ones. The
images are right; the description was copied through by the generator that
made them. Nothing downstream read those two fields, so no build and no
submission had been harmed, and the Swordsman does not care: a declared hash
that disagrees with its own bytes fails the bundle. The sibling's lead
confirms the cause within the hour, fixes the generator, regenerates seven
directories, exports again. The second mint has a different root. The first
root is not deleted. It is kept, marked superseded, because a correction that
leaves two roots is a record and a correction that leaves one is an
overwrite.

The Hall itself is next. It already had a key law of its own, and the Mage
does not replace it. Beside the holon's address goes the Keeper's, a second
axis, never mixed in one preimage. A twin of the mirror is written in the
Hall's own language, and the two agree on a fixed vector of structures. The
Gap needs no change at all: its seed had always been the hash of the
proposal's canonical bytes, which is exactly the Keeper's address for that
file. The tool records what the engine already did, as an edge, and the
verifier checks it: *the witnesses were drawn from an address the prover
could not choose*. Thirty-four past runs are minted. The gate count rises.
Every gate passes.

Then the receipts are read back into the rulebook. Seven lanes had stood on
live boards with the seated loop and none of their method was in the Hall.
Four readers sweep them, read-only, and return a hundred and five rows. Forty
are kept as rules, each citing the lane that proved it and the entry it
shipped in. Three support seats are cut: one that re-reads a record's
constants at the named commit before any build, because that is what the
stale layout was; one that rehearses the judge from the judge's own archived
dossiers; one that holds the last negation before the door and whose NO-GO is
final. And a one-screen door, so that a stranger who wants to run a lane never
has to read the receipts.

Last, the Library. Sixteen pages are generated from the κ'd records, never
from prose, and each is bound to the record it projects by a minted object:
the page's own address, the root it came from, the address of the program
that made it. The route search as a graph whose total is recomputed in the
reader's browser. The gate as a graph. The forty rules as a map. Ninety
citations by thirteen solvers as a matrix, beside the chain of the copied
number quoted from the log by line. Fourteen of the judge's dossiers as one
grid, with the rule that one unsupported heuristic sinks a package checked
row by row. The calibration of what a second of the machine is worth. The
sixteen bindings sit under one root of their own.

Here is what the two days teach, and it is not "the mirror works."

A number with no address can be copied and argued over. A number that is an
object can be copied and still be yours, because the copy carries the address
and the address carries the mint. Provenance stops being prose. The judge who
could not run your machine can run your hashes. And the first thing a verifier
did with a second lane was refuse it, which is how you know it was a verifier.

```
(⚔️⊥⿻⊥🧙)😊 = neg ⊕ bnot → succ
```

---

**Spell.** `mirror(keeper) → mint(ledger) → root(run) → verify(stranger) → refuse(stale) → twin(hall) → fold(rules) → pair(reader, root) ∴ sha256:3c20049e…`

**Proverb.** *The decimal travels; the root stays. Whoever carries the measure carries the mint, and the mint remembers the hand that struck it.*

*(proposed by the reflection lane, 2026-10-07, and minted under with its own address, `sha256:28072b32…`; it stands as a proposal until the First Person speaks it or replaces it.)*
