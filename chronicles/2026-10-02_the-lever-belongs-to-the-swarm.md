# The lever belongs to the swarm

> Local City chronicle reflection. The framework master is the narrative source of truth; this copy adds only this provenance and runtime-trace header. Signed by the First Person: **not yet**. Local draft; no publication or binding is recorded.
>
> Master: [The lever belongs to the swarm](../../agentprivacy_master/docs/chronicles/2026-10-02_the-lever-belongs-to-the-swarm.md).
>
> Runtime traces live in the sig_mage lane (kit, fleet run 01, running log, submission notes), in Yukon submissions 62479bf4 (PR 212) and 35cff6dc (PR #301), and in the soul_mage knowledge base that renders the lab's /harness/ tables. The proposed companion tome is [The Signature Hole](../tomes/proposed/the-signature-hole.md).

Private master chronicle draft · 2 October 2026 (covering 30 September – 2 October) · harness lane: sig_mage on Yukon's sig.golf.

Scope: the dual-agent harness's newest outcome. sig.golf asks for a hash-based signature scheme with a Lean certificate, scored as signature bytes times worst-case RISC-V verify cycles, lower is better. Three days took the lane from a research kit to two promoted submissions, each holding the crown when it landed, and to a third line of work that ports both of its levers onto the scheme that took the crown from it.

## 1. The inversion

A benchmark looks like a race for a place. sig.golf behaves like a commons. Every promoted submission is public and every solver composes on top of the last. The lever the harness found on 1 October was adopted by the swarm within minutes and carried someone else to the crown, crediting ours as ancestry. The outcome to record is not standing. It is that the lever is now part of the floor everyone builds on, and that the keeper ruled this good: "there is also the ability to quote others in the swarm and join as collaborators on the board so not as much of an issue if our lever is adopted."

## 2. The method, stated as it ran

The kit (`sig_mage/sigmage/SIG_MAGE.md` §7) names the separation: the Mage proposes, the Swordsman disposes, and the proposer never grades its own work. The Mage owns cost-model sweeps, emulator experiments, RISC-V generation and Lean proof scripts. The Swordsman owns the contract reading, the security argument, the worst-case cycle bound, admission and termination, malleability review of every format change, and the only key to the local verifier.

Fleet run 01 (30 September) records how it actually ran: one Claude session played every role in sequence, Mage-alpha, Mage-beta and Swordsman, with the separation enforced by process. Every Mage claim was re-derived by a separate Swordsman check before it was logged; no parallel agents ran. Three dreams went in. One was confirmed (a triple dispatch for the one-time-signature chain heads, −665 cycles worst case, derived exactly rather than sampled). Two were killed, one of them because the Swordsman showed a 2-bit pin in the digest decoding was load-bearing for the 2^-128 bound.

Why this is interesting:
- The kill was the security argument doing its work: a cycle saving the Mage wanted would have broken the bound the certificate proves.
- The gate before every submission was a full local Lean build plus the comparator replay, the same check the official validator runs. Nothing was submitted on a model's say-so.

## 3. E8, and what the swarm did with it

On 1 October the lane found lever E8: the upper one-time signatures sign the two children of the lower tree's root, so the verifier skips four hashes (−40 cycles). It passed the local gate and was submitted. At 18:31Z Yukon promoted it: submission `62479bf4`, score 62,612,160 (S 6,032 × C 10,380), the crown at that moment.

The same evening E8 was ported onto a rival's pending tree and passed the local gate again, at C 10,334. It was not submitted. Frodan's PR 217 was already queued with the same composition at the same score, crediting "mitchuski's PR212" as promoted ancestry, and was promoted at 20:12Z. The crown moved, built on our lever. The gated port was kept in reserve in case 217 failed. It did not.

## 4. C1, and the scheme that moved the floor

On 2 October the lane found lever C1: an arithmetic poly-MAC over the signer's cache (three key hashes) plus cached top leaves, which cut 835 compressions from signing and let the verifier's targets drop. The Mage seat designed the change and wrote the Lean proofs; separate agents built and checked the machine-code images in an emulator. The local Lean build covered the security proof, the reference equivalence, the budgets and the machine proofs. It was submitted with the comparator replay still running, and the replay passed while Yukon validated ("Lean default kernel accepts the solution"). Yukon promoted it: submission `35cff6dc` (PR #301), C 10,255, score 61,858,160, the crown again.

That afternoon another solver's PR #308 merged a different scheme, T3 (four layers, a new few-time signature shape, in-place witness): 54,722,304, 11.5% under ours. The crown is theirs. The lane's answer was to carry C1, and later E8, onto T3. By evening the T3+C1 keygen and sign machine proofs were green and a full build was running. That work belongs to the lane's live session and is not told here.

Why this is interesting:
- Two promotions in two days, each holding the crown when it landed, and each overtaken by composition, not by refutation.
- Some of the lane's work closed things off rather than gaining: the encoding is at its floor, and a few-time signature shape that looked cheaper fails the certificate's own variance term by 1.1–2.45 bits. A NO-GO measured in the proof's own formulas is a result.

## 5. Where it lands

The keeper asked that sig_mage be shown as an outcome of the harness on the lab side and be given a tome in the City. Its recorded numbers go into the soul_mage knowledge base, where every number must trace to a quote in a file on disk. The lab's `/harness/` tables are rendered from that knowledge base, never typed by hand. The City's telling is proposed as **The Signature Hole**, a companion to *The Proof Links*: unnumbered and unbound.

Evidence spine: sig_mage/sigmage/{SIG_MAGE.md §7, memory/fleet-run-01.md, memory/log.md (2026-10-01, 2026-10-02 entries), submissions/}; Yukon submissions 62479bf4 (PR 212, merged 3b7d98a) and 35cff6dc (PR #301, merged 33ce004); soul_mage kb + exports; agentprivacy_labs site/harness/. The KB record, lab render, City reflection and tome are uncommitted.

*Uncommitted, as ever — the First Person's read comes first.*
