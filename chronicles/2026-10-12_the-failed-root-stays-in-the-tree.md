# The failed root stays in the tree

> This is a local reflection of a City chronicle. The framework master is the narrative source of truth; this copy adds only this provenance and runtime-trace header. Signed by the First Person: **not yet**. It is a local draft, with no publication or binding recorded.
>
> Master: [The failed root stays in the tree](../../agentprivacy_master/docs/chronicles/2026-10-12_the-failed-root-stays-in-the-tree.md). Follows [The hash learns to sing](../../agentprivacy_master/docs/chronicles/2026-10-11_the-hash-learns-to-sing.md), which is told in the City only as the proposed Tome IX Act 14, because its run results stay behind the veil.
>
> Runtime traces live in the hashsmash_mage and blake3-mage lanes (the frontier race file, the prefilter packages and their submission notes, the kappa bundles pf2 to pf4 with roots 4332e53a, 862252fa, 6e5587c2 and 75847312) and on the public board (submissions fc11d939, b026078f, 673fd629, 3961c316). The evidence trees are served by blake3.mages.city, sha256.mages.city and sha3.mages.city, where every leaf re-derives in the browser. Scores named below are the board's own public record on 12 October; a board check beats them.

Private master chronicle draft · 12 October 2026 · harness lane: blake3_mage with hashsmash_mage (HashSmash blake3-r2, the frontier race), kappa_evidence_mage, and the three hash sites of the Mages City.

Scope: one long day in which the lane stopped listening to the frontier and joined it. Four submissions went to the blake3-r2 board, one failed, two passed, one is still validating. Two levers were tried and shut. Every step was minted as a κ bundle, each root naming the one it revises, and by the night the bundles were on a public site where a browser rebuilds every Merkle tree and re-derives every leaf, the failures included. blake3.mages.city, sha256.mages.city and sha3.mages.city went to production, fully revealed, and the First Person tweeted. Follows [[2026-10-11_the-hash-learns-to-sing]].

## 1. The inversion

A failed submission is normally erased. The package is fixed, the next attempt goes up, and the record of the miss lives only in a closed pull request nobody reads.

The inversion is that the failure is a node the winner points at. Our first entry failed intake for being 708 bytes over the judge's budget. Its κ root, 4332e53a, was not discarded: the entry that passed review an hour later names it in its `revises` field, so the passing root cannot be read without walking through the failed one. The same holds for the levers that did not work. Their records and files are leaves under the 57.4123 root, re-hashed from their bytes in a stranger's browser. Proof of work stops being "here is what won" and becomes "here is everything we did, and you can check none of it was edited afterwards".

## 2. Joining the race

The First Person's ask was plain: a blake3-r2 solve on the board, even if not the crown. The frontier was read as a lineage before anything was built: twenty-four accepted steps, one lever each, the big jumps named (the joint screen, the re-chosen outcome set, typed member lists) and everything else small counted-program trims.

The lever we brought was the Y9 prefilter. Every candidate that passes the frontier's test (1) projects onto seven bits of Y9 as exactly 0x004 or 0x3c4. That was first sampled, then proven: of all 1,024 low-ten-bit prefixes through the test's automaton, 14 survive, all on those two projections (Lemma PF, exact by enumeration). A packed check of about 8 units lets most words skip the expensive lane work. The budget for kept words needed a premise, and it was measured rather than assumed: 200,000 contexts, kept share 0.10463 against a budget of 1/8, written as H_PF with its margin.

Why this is interesting:
- The lever was found by reading what the frontier's own proof already implied, then made exact before it was made fast.
- Its premise is a measured number with a stated margin, and the measurement is itself a record in the bundle.

## 3. Four submissions, one failure, in order

- **Refused before it was sent:** the note was under the 5 KiB floor.
- **fc11d939, failed intake:** the judge's evidence budget is 512 KiB over the proof, the intake report and the experiment report, and we were at 524,996 bytes because the previous entry's whole section was stacked on top of ours instead of replaced. Our local check does not run that step. From then on the organizer's own intake is measured before every submit. Root 4332e53a.
- **b026078f, passed review, 57.4702:** the base section cut to a pointer, the typed-list values restated (a fresh-agent check caught that the trim had dropped them). Root 862252fa, which names 4332e53a as the root it revises. The note carried the harness name twice; Yukon already prints it from the flags.
- **673fd629, passed review, 57.4377:** the 2-unit word test charged only to words that are kept. Root 6e5587c2. Its note said what we would try next, which pointed the field at a lever while the race was live.
- Then the field moved on our work, with credit: 0xshikhar and Th0rgal both posted 57.4454 built on the prefilter, without the word-test change.
- **3961c316, 57.4123, validating:** their trims plus our word-test split. Judge evidence 520,650 bytes, 3,638 under. Fresh review clear. Root 75847312 (BLAKE3 label 13fbac90, Merkle root a95c1aca over 114 leaves), revising 6e5587c2. Its note still carried a next-steps line; the rule is now none at all.

Why this is interesting:
- Each gate that caught us became a gate we run: the floor, the intake size, the header, the trim check, the no-hints rule. The routine is now patch, self-test, organizer check, intake size, Docker, fresh critic, κ mint, submit, each on the final bytes.
- The lineage is a conversation in public: a lever we posted was built on within the hour and credited, and we built on theirs the same way.

## 4. Two doors that are shut

The lever our own note had leaked was then worked honestly. Is there a cheap test on a lane's list entry, before the 39-unit fill, that predicts the prefilter? Over all 2^16 inputs in eight real live blocks, every input bit matters fully (sensitivity 0.96 to 1.01, random-function-like), and prefix classes stay mixed at the random rate. No. Can any of the fill's ten rotation masks be dropped? All 1,024 drop sets tested: none survive.

Both were minted into the 57.4123 bundle as records with their output files, not left in a terminal.

Why this is interesting:
- A negative result recorded under the same root as the win is cheap to trust and expensive to fake. Nobody pays for these two doors twice, and nobody can later claim we did not try them.

## 5. From sheet music to evidence chains

The sites built the night before were re-cut around the evidence. Every public submission on six tracks became a race score, one voice per solver, credited by name: blake3 r1 and r2, SHA-256 r37 and r38, SHA3-256 r5 and r6. Our own work became chains: the prefilter root by root, every record inside 57.4377, the r37 and r38 roots. The sample text became "just another mage sharing their spellbook" and "just another swordsman, privacy their blade", every story re-checked against the verifier (the SHA-256 pair still collides at 12 steps). One honesty fix: full BLAKE3 agreeing on 141 of 256 bits had been shown as if it meant something; anything within three sigma of two random digests now reads as nothing in common.

BLAKE3 now stands beside every κ: each beat, each score, the ledger, the run root, and a BLAKE3 Merkle root over all of it. The browser's BLAKE3 matches the reference at every length, multi-chunk included.

## 6. The tree

The First Person asked for the Merkle tree drawn, with the failed and winning levers marked, and then asked whether it worked correctly. It did not, quite, and saying so made it right:

- The chain of roots had been drawn in our order. Built from each root's own `revises` field, it shows the truth: 57.4702 revises the failed root directly, and the trimmed root was a side draft never submitted.
- The tree had hashed leaf κs without re-deriving them. Now every leaf is checked against its content in the page: 32 of 32 records re-derived from their fields, 59 of 59 links, 23 of 23 files named by a re-derived record, and the two negative-result files re-hashed from their bytes on the site. Every one of the seven trees ends on "the tree is exactly its evidence".
- A failure had coloured every mixed branch red. A branch now takes a colour only when everything under it is one lever.

The page says plainly what the tree is: leaves sit in κ order, so position means nothing; the tree proves inclusion, and the flow of evidence lives in the links, which are leaves too.

## 7. The veil, parked

A third state was built for the public site: every score plays, its κ and BLAKE3 visible, while the records behind each κ are held for members of the City. It passes its own suite. Then the First Person chose otherwise for now: push the fully revealed work, add the fog of war once it draws attention. The production sites are the open build. The veil is one line away.

## 8. Production

Three Workers with custom domains, deployed after the First Person's login. blake3.mages.city is serving the build byte for byte, an evidence file re-hashes to its own name from the live site, and the 57.4123 graph is served. sha256 and sha3 answer from Cloudflare with byte-identical pages while the local router still remembered the names as nonexistent. The tweet went out that night: the work is a dance, not the final stance.

## 9. What did not happen

3961c316 has not finished validating. Nothing in blake3-mage is committed (it is not a git repository); kappa_evidence_mage's score shapes still lack a Rust check. The members' gate the veil points at does not exist yet. The site roots change on every rebuild, because every build draws fresh salts, so only the deployed build's root verifies. The board was not polled.

Evidence spine: hashsmash_mage/work/b3r2_frontier/{RACE.md, apply_wt.py, fill_mask_search.py, prefill_probe.py, pkg_pf2…pkg_pf4, submission-note-pf2…pf4.md, site_inputs/}; hashsmash_mage/intake_measure.sh; kappa_evidence_mage/out/b3r2_pf2, pf2b, pf2c, pf2d, pf2e, pf3, pf4 (roots 62d963d4, 1be1a000, 4332e53a, side draft, 862252fa, 6e5587c2, 75847312); blake3-mage/levers/{race_scores.py, tree_scores.py, sites_build.py, pb3_core.js, pb3_page.html, pb3_test.mjs, pb3_reveal_test.mjs, pb3_smoke.mjs}; blake3-mage/deploy/{blake3,sha256,sha3}.mages.city (Worker versions 421c4110, 38113002, 11fee45d). Suites at close: 292/292 site, 994/994 veil, 17,908/17,908 sound, smoke pass on every build with all seven trees verified leaf by leaf.

*Uncommitted, as ever — the First Person's read comes first.*
