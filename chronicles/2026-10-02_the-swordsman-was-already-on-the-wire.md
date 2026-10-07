# The Swordsman was already on the wire

> Local City chronicle reflection. The framework master is the narrative source of truth; this copy adds only this provenance and runtime-trace header. Signed by the First Person: **not yet**. Local draft; no publication or binding is recorded.
>
> Master: [The Swordsman was already on the wire](../../agentprivacy_master/docs/chronicles/2026-10-02_the-swordsman-was-already-on-the-wire.md).
>
> Runtime traces live in the openanonymity_mage lane (the mechanism brief and eight upstream clones at pinned commits) and in agentprivacy-docs (the V7 note, dispositions, source manifest and integration plan). No City tome is proposed for this chronicle yet.

Private master chronicle draft · 2 October 2026 · research lane: the Open Anonymity Project, read into agentprivacy as its own V7 strand.

Scope: one afternoon, from a link to an organisation on GitHub to a neutral lane, a mechanism brief, an integration plan and a V7 research strand. Started from "lets find the overlap and integrate this into the agentprivacy work"; ended with the rulings that OA is a strand of its own, that agentprivacy means to contribute to OA as an early adopter and be seen as a partner, and that the Kwaai work is not touched yet.

## 1. The inversion

The programme came to OA expecting to bring the model to a project. It found that the project had already built the part the model mostly draws. Open Anonymity ships unlinkable inference: a person buys blind-signed tickets, each session swaps tickets for a fresh provider key, and nobody but the person holds the join between who paid and what was asked. That is the Swordsman, on the inference wire, in a chat app ordinary people use. The contribution therefore turns around. It is not "here is our model"; it is "here are the pieces your design names as future work, and here is the model that says why they matter."

## 2. The read, measured

All eight repositories were cloned shallow into `~/openanonymity_mage/upstream/` and read without running anything. Two readers worked apart: one went through OA's mechanism, the other through the agentprivacy tree for places it touches. The second found no mention of OpenAnonymity, nanomem, Tinfoil or Privacy Pass anywhere in the home directory. The overlap is real but unnamed.

The mechanism, as read: RSA blind signatures (RFC 9474) in Privacy Pass form (RFC 9578); one fixed challenge for every client so tokens cannot be tagged; stations that mint short-lived keys double-signed by station and org; a verifier in an AMD SEV-SNP confidential container that checks each station's privacy settings and key ownership and bans on failure; an optional zkAPI path that funds leases from a private ETH note; and nanomem, a person's memory in readable markdown with a fact lifecycle and a step that writes a minimized, tagged prompt the person approves before it leaves. Three of the brief's claims were checked by hand against source: the fixed challenge, that the client displays the verifier's attestation without verifying it, and the prompt-crafter's minimization rules.

OA states its own limits plainly: "unlinkable, not invisible." The provider still reads every prompt.

Why this is interesting:
- The project keeps a "Wrong-Conclusion Traps" table in its own privacy model. It anticipates the reader most likely to overclaim, and the reading here kept to it.
- Licences divide the org: the app, memory, station and verifier are MIT; the SDK, Android wrapper and an earlier snapshot are AGPL. That decides what can be built on directly.

## 3. The overlap, sorted

Nine rows, each with a tier. The four that carry the strand:

- **Linkage, not content.** C82 places the adversary's growth in the linkage corpus building up over time. Unlinkable inference refuses the provider that corpus. What is left is whatever the content of a prompt can re-link, and that is measurable and has not been measured.
- **Two separations at once.** The blind signature is amnesia-enforced: the issuer cannot join issuance to redemption. The verifier's settings checks are policy-enforced, made attestable. One shipping system is a worked instance of C17 and C83.
- **The minimized prompt is a lease.** nanomem's step is the same act as the harness's single human door, VPK's scoped slice and verifyvasp's purpose-bound projection. OA's is the one already in front of users.
- **One key is the anonymity set.** Everyone must blind against the same issuer key. OA lists a transparency log as future work. The MTC strand's cosigned tree, with the City as one cosigner, is the shape of an answer.

Gaps were recorded as readings, not findings: the client shows the verifier's attestation without checking it; the list of verified stations is unsigned; the outer signature comes from a closed service; global key rotation sits beside per-invitation issuance counts. None goes upstream without the keeper's word.

## 4. The rulings

The keeper ruled three things. OA is its own V7 strand, not a sub-strand of the Hold. The aim is to contribute to OA's project as an early adopter, bringing our knowledge where it overlaps, so that agentprivacy is seen as an OA partner. And the Kwaai lane stays as it is for now: OA is not written into `PATHWAY.md`.

The first ruling became files the same afternoon: a V7 research note (`2026-10-02_v7_unlinkable_inference_and_the_swordsman.md`), a dispositions file touching ten register rows with no status change, a source manifest that pins all eight commits and hashes the nine documents read, and a row in the V7 index. Seven unnumbered candidates, OA-H1 to OA-H7. The central experiment is OA-H1: under fresh keys per session, how much can a provider re-link from content alone, and how much do minimization and scrubbing lower it?

Why this is interesting:
- The partner offer was written down before the first line of contact. The order runs from reading to running locally to measuring to the offer, so what reaches OA is what has been checked.
- The strongest single offer, a cosigned log of the issuer key, answers an item OA already lists as its own future work.

## 5. What did not happen

No ticket was bought, no key minted, no ETH deposited, no issue or pull request opened, no one contacted. Nothing was written into the Kwaai repository. The plan's spending, contact and push doors stay with the keeper.

Evidence spine: openanonymity_mage/{README.md, MECHANISM_BRIEF_2026-10-02.md, upstream/ ×8 at pinned commits}; agentprivacy-docs/plans/OPENANONYMITY_INTEGRATION_PLAN_2026-10-02.md; agentprivacy-docs/research/{2026-10-02_v7_unlinkable_inference_and_the_swordsman.md, oa-v7-conjecture-dispositions.json, oa-v7-source-manifest.json, V7_RESEARCH_INDEX.md}. All uncommitted.

*Uncommitted, as ever — the First Person's read comes first.*
