# The measurement travels without its name

> This is a local reflection of a City chronicle. The framework master is the narrative source of truth; this copy adds only this provenance and runtime-trace header. Signed by the First Person: **not yet**. It is a local draft, with no publication or binding recorded.
>
> Master: [The measurement travels without its name](../../agentprivacy_master/docs/chronicles/2026-10-07_the-measurement-travels-without-its-name.md).
>
> Runtime traces live in the hashsmash_mage lane: the kit, PATHS.md, the running log, the r32 search ledgers, the assays and judge records, and the research intake. The Yukon submissions are 02d6a703 (PR #254), 1ded36a8 (PR #296) and 8bad82c1 (PR #396). It is a companion to *The Signature Hole* (sig_mage); no tome is proposed yet.

Private master chronicle draft · 7 October 2026 (covering 5–7 October) · harness lane: hashsmash_mage on Yukon's HashSmash.

Scope: a new board for the harness. HashSmash asks for collision claims on reduced-round hashes: SHA-256 at 31 and 32 rounds, SHA3-256 at 5 and 6, and BLAKE3 at 1 and 2. Each claim is a package of a JSON claim, a self-contained proof and optional certificates or experiments. A committee of AI judges reviews it, and the score is log2 of the total charged computation. Three days took the lane from an empty kit to two passed submissions. One of them held the 32-round crown twice. Then the lane went on hold.

## 1. The inversion

On sig.golf the swarm adopted our lever and credited it. Here the swarm adopted our *measurement* and dropped the name. Our measured route search for the 32-round attack is 59 solver calls and 593,858 CPU-seconds, run until it produced the paper's published route. It now sits verbatim inside the two submissions that lead the board, and neither mentions where it came from. The keeper ruled the order of priorities: "its okay for now around that provenance diverged from me as long as we get the leaderboard again, and in that note correct the path of citing." What travels is the number, and the record of whose it is has to be carried deliberately.

## 2. The method, stated as it ran

Seats of the harness ran as Claude Code subagents.
- **Mage seats (soulbae)** surveyed the literature per hash family and built the packages.
- **Swordsman seats (soulbis)** saw only the package and the judge's own prompts and rehearsed the committee.
- **Pairs of independent soulbis seats** ran on the large claims: one re-derived the cost from scratch, the other rehearsed the judge from its real past verdicts.
- **The coordinator** checked every declared number against the proof before each submission.

Every refusal from the real judge became a recorded lesson:
- a declared field must equal the proof's own derivation;
- the proof stays under about 28 KB, because the run is cancelled 15 minutes after dispatch, queue time included;
- a statistical model layered on a plausible heuristic becomes a new, unsupported heuristic;
- every package carries at least one experiment the organizer runs itself.

Why this is interesting:
- The swordsman seats caught a fatal error twice before the judge did. Once our own assay missed one, and the judge caught it. The failure was logged as a lesson rather than retried.
- One line of BLAKE3 experiment work was stopped by a safety classifier. The lane did not try to route around it, and recorded it as held for the keeper.

## 3. SHA3-256 at 6 rounds: four refusals, then a pass

The lever was a distinguished-point walk run 256 messages at a time in bit-sliced form, with no sorting and no transposes.
- `da4895b5`: refuted. The proof called about 2^8 units of setup "preprocessing" while the claim declared 0.
- Two attempts died in the organizer's queue before any judge saw them.
- `2899cfb0`: not evaluable. A model mapping a 0.51% shortfall to full-width success was rated a new, unsupported heuristic.
- `02d6a703` (PR #254): **passed at 125.58**, the best pending score that evening, with the random-function heuristic rated plausible in all four lanes.

The field has since moved to 124.295 with a grouped-table method.

## 4. SHA-256 at 32 rounds: measuring what everyone else assumed

The published attack cut from 35 rounds to 32 was already on the board, with a real collision certificate (yudduy). It carried a 2^64 allowance for the route search that nobody had measured. The lane installed the paper authors' tooling (STP with CryptoMiniSat) and timed the search, charging every call.
- `1ded36a8` (PR #296): **passed at 52.1 on the first submission**, the crown. The two independent assays had moved the claim from 47.4 to an explicit allowance before filing.
- Within hours, Th0rgal's #367 carried our measurements verbatim with a smaller allowance (48.45, uncredited), and jackzampolin's #377 trimmed that to 48.25.
- The search kept running. Step 4 at weight ≤ 76 returned the published Fig. 6 characteristic exactly, so the route search was complete.
- `1ac3bbb5`: not evaluable. All seven heuristics were plausible in every lane, but the evidence was "participant-reported only".
- `8bad82c1` (PR #396): **passed at 47.6**, the crown again. It added the credited certificate and an organizer-run replay experiment. Its note corrected the citation chain (#296 → #367 → #377) and credited six solvers.
- By 7 October, Th0rgal's `f310d44` at 47.275 and a chain from Meganpark980320 down to 47.29 had trimmed the attack phase. Both still pay our measured search term, `E = 32 × 593,858 × 2^23`, which is now nearly their whole score.

Why this is interesting:
- The judge ruled the honest allowance plausible, so a conservative claim cost bits but bought a first-try pass.
- What the board now floors on is a measurement this lane made. Any further gain must shrink that term.

## 5. Where it lands

On 7 October the keeper brought a research note on the OpenAI math collection. The lane ran it without WSL:
- a screen of the 2^0.49n Subset Sum result, recorded as a negative;
- a success-probability lemma proving trial independence;
- evidence tables mapping every judge obligation to its class;
- the frontier levers for both tracks.

The lane is on HOLD until the board settles. The next lever is re-calibrating the CPU price, worth about 1 bit in a few hours of WSL. Its note carries the corrected citation path.

Evidence spine: hashsmash_mage/{HASHSMASH_MAGE.md, PATHS.md, memory/log.md, work/sha3/, work/sha256/ (R32_LOG.md, ASSAY_*, judge_record/, review_*/), work/research/}; the solver ledgers in the WSL mirror; Yukon submissions 02d6a703 (PR #254), 1ded36a8 (PR #296) and 8bad82c1 (PR #396). Nothing is committed.

*Uncommitted, as ever — the First Person's read comes first.*
