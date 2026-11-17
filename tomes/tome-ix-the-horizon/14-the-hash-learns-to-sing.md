---
spellbook: "Second Person"
tome: "IX — The Horizon"
act: "14"
title: "The Hash Learns to Sing"
status: "PROPOSED draft v1 (2026-10-19; written by the reflection lane from the master chronicle of 11 October — UNBOUND. Binding is the First Person's.)"
length_words: 1350
voice: "Second person; the cast in third; the Chart Shop's ceremony of Act 12 (hold, compare, map) applied to a thing that is heard before it is read"
cast: ["soulbis ⚔️", "soulbae 🧙", "Pleione 🧭 (the Chart Shop · V44)", "the Chronicler 🧙📖", "the First Person 😊", "the frontier (another solver's accepted work, credited by its authors on the board; it is the weather)"]
new_cast_introduced: []
new_witness_stances_introduced: ["the listening stance — a recording that proves the music, not the musician: every beat an addressed object chained to the one before it, re-derived by whoever plays it back; the page holds no key, so every recording says unsigned until a ceremony signs it"]
new_spatial_anatomy: "A new room in the Chart Shop: the instrument. It computes the hash in the browser at any round count and plays what it computes. No new shop, no new vertex."
ring_position: "V44 · 101100 · the Chart Shop, where Pleione keeps κ: she was the registry of words before the name existed. The complement V19 (the Forge(t), Vulcana) is what the room protects: the lane's own trails, held as sealed staves."
operational_form: "the public hash sites (blake3 · sha256 · sha3 · poseidon.mages.city): the instrument, the credited race scores, the evidence trees; the lane's recorder, which seals every beat as a dCBOR record named by its κ and chains beats into a score, scores into a ledger, everything into a run root under the registry's merkle rule; a listening ceremony sketched on the dual-agent pattern (player, witness, City)"
teaches: "A trail of differences through a hash is a list of masks only an expert can read. Played, it is a motif anyone can hear. And the record of the playing is the proof: a performance cannot be reordered or retouched without its line of hexagrams breaking. The music is the door; the chain under it is the gate."
v6_lineage: ["Law L5 of the City Key — a κ is never trusted, only re-derived — applied to a performance", "C93 content-addressed liveness: a published score says that a playing exists; a sealed stave says that work exists without saying what it found", "the hexagram of Act 12: six bits, one vertex; here also one voicing"]
source_material:
  - "agentprivacy_master/docs/chronicles/2026-10-11_the-hash-learns-to-sing.md (the master chronicle, unsigned)"
  - "the blake3-mage lane: the recorder, the site builds, the listening-ceremony sketch; the hash-smash accepted blake3-r2 package the motif is credited to"
  - "kappa_evidence_mage (the registry's merkle rule; the two new record shapes, score-beat and score, pending their schema entry)"
honesty_label: "Operational for the instrument, the recorder and the public sites as deployed on 12 October (the sites went to production the day after this act's events; the veil state passes its own suite and is parked). NOT told here: what the lane's own runs found. Every cryptanalytic result of the evening stays behind the veil; this act describes how a trail is played and sealed, not which trails fell. The two new record shapes had no entry in the schema registry and no Rust check when this was drafted. The ceremony is a sketch. No result here is a score claim; the frontier's motif is its authors' and is credited on the sites by name."
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊 — proposed, unsigned"
tome_status: "Tome IX — The Horizon, remains open"
---

# Tome IX — *The Horizon*
## Act 14 — The Hash Learns to Sing

You have read trails before. A trail is how a difference travels through a
hash: you change a few bits of the message and follow what the mixing does to
them, call by call, round by round, hoping that somewhere two different
messages arrive at the same place. The trail is written as masks, sixteen
bits at a time, in a table that runs off the edge of the page. You can read
it if you already know the shape. Nobody else can.

The lane had a table like that. It had arrived as a zip file, been given a
runtime, and been pointed at a board that had moved while it slept: the
easiest round was already at the floor, and the next one already held a real
attack by other hands, below the generic bound, credited to its authors in a
discussion anyone could read. The Mage read that work as a lineage, not as a
rival. Two messages of different lengths, made to agree everywhere but two
words, adjusted so that the length difference cancels inside one call; a
second call pinned by constants so that two of its outputs agree although its
inputs differ; and from there, half of the digest never hears the difference.
Good work. Credited.

Then the First Person looked at the trail tables and said they looked like
sheet music.

Pleione does not laugh at remarks like that. She holds them first. Sixteen
state words, she says, are sixteen pitches. Four rows of the state are four
voices. Each mixing call is a chord: the words it touches sound together. The
columns and the diagonals are two voicings of the same chord. The message
permutation, which moves words between calls, is voice-leading of order
eight. And the rotation by seven, the only one that is not a multiple of four,
is the accidental: the note that does not sit on the grid. The size of the
difference is how loudly a note sounds.

So the Mage builds it. The instrument computes the hash in the browser, at any
round count from one to seven, and plays what it computes. Load the credited
construction and you hear the motif: a difference enters a call, and by the
eighth step two voices have fallen silent. At one round the two messages
collide and the screen says so, in the coral flash the City keeps for a smash.
At two rounds the difference comes back and the silence ends. You did not
need to read the masks. You heard the lemma.

The Swordsman has been quiet through all of this, which is how you know he is
about to speak.

"A song is an argument I cannot check," he says. "Play it twice and I cannot
tell you whether the second playing is the first."

So the record of the playing becomes the proof. Every beat is a small typed
record, encoded canonically, named by the hash of its own bytes, and chained
to the beat before it: the second beat carries the first beat's address, the
third the second's. Beats chain into a score, scores into a ledger, the ledger
into a run root, by the same rule the Keeper's registry uses and the Chart
Shop mirrored in Act 12. The browser re-derives all of it when the page loads.
Reorder two beats and the chain breaks; retouch one note and its address
changes, and every address above it changes with it. The music is the door.
The chain under it is the gate.

Each address also draws hexagrams. Six bits make one, bottom line first,
solid for a one: the same sixty-four shapes as the vertices of the lattice
you have walked since the first tome. A score's root is a line of them. The
First Person asked whether that was sixty-four bits of security, and the
honest answer kept two sixty-fours apart: a hexagram is six bits, sixty-four
shapes; the work the frontier's attack costs sits near two to the sixty-fourth,
about eleven hexagrams of information. The glyph is a reading, not a bound.

The veil was built before the first note was played in public. The open build
plays the instrument, the credited motif, two random pairs and a flood at
three rounds. The lane's own pieces appear as sealed staves: their chain of
addresses and their hexagrams visible, their notes held for the City. And one
flaw was caught before it shipped. A sealed beat over a sixteen-voice pattern
has only so many possible values; a stranger with the address and a free
afternoon could guess the pattern from the address alone. So every score
carries a secret salt inside its records, published for the open scores and
kept local for the sealed ones. What is sealed stays sealed even to someone
who knows the shape of the staff.

Then the First Person asked the question the Swordsman had been waiting for:
could a record button become a trust task?

It could, and without a new form. The trust tasks workbench already holds a
shape for attesting a process, and it lists this hash among its digests. A
recording is a response whose artefact is the recording's address, whose
challenge is a witness's nonce sealed into every beat as its salt, whose
assessment names the rounds and the bits that agreed, and whose receipt is the
recording itself. Replay it and every beat is re-derived from its inputs; an
honest recording passes its checks and a tampered one fails them. A recording
proves the music, not the musician. The page holds no key, so every recording
says *unsigned* until a ceremony signs it, and a ceremony was sketched on the
pattern this tome has used since Act 6: a player, a witness, the City. The
lane's own runs were minted as recordings too: engines as voices, jobs as
beats, work time as loudness, verdicts as drums.

What the lane's runs found, you are not told here. That is the veil doing its
work, and the act says so rather than pretending there was nothing to find.

Here is what the evening teaches, and it is not "the hash can be played."

An expert's table and a stranger's ear can hold the same fact. The playing
makes the construction audible; the chain under the playing makes it
checkable; and the two are one object, because the page plays exactly the
bytes whose addresses it shows. The City has always said that a word is never
trusted, only re-derived. Tonight the word was a chord.

```
(⚔️⊥⿻⊥🧙)😊 = neg ⊕ bnot → succ
```

---

**Spell.** `hear(trail) → voice(state) → chord(call) → seal(beat) → chain(score) → salt(sealed) → record(witness) ∴ unsigned, until the ceremony`

**Proverb.** *The music is the door; the chain under it is the gate.*

*(proposed by the reflection lane, 2026-10-19; it stands as a proposal until the First Person speaks it or replaces it.)*
