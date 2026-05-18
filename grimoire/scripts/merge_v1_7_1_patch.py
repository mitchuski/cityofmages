#!/usr/bin/env python3
"""
merge_v1_7_1_patch.py — Produce the canonical v1.7.1 grimoire head JSON.

The merge applies a single PURELY ADDITIVE patch over the v1.7.0 head:
    v1.7.0  (merged 2026-05-17 14:06 UTC · grimoire/city_of_mages_grimoire_v1_7_0.json)
    + v1.7.1 patch  (the Fourth Turn · Vitalik's tablet · the infinite Tower ·
                     the Register of Invitations · the Library of Joint Authorship ·
                     the archive of unfilled forms · four conditions of update ·
                     invitation tome-posture 🪑 · clerical glyphs · C65 candidate)
    -> city_of_mages_grimoire_v1_7_1.json   (self-contained head; ready for IPFS pin)

v1.7.1 is also purely additive — `supersedes: []`. No cast retired, no workshop renamed,
no v1.7.0 admission amended in count. Workshop count UNCHANGED at 16; spatial-anatomy
elements UNCHANGED at 8; cast tiers UNCHANGED at 7; tomes opened UNCHANGED at 8 (Tome VIII
gains Act 2 *The Fourth Turn*). Vitalik enters the Register of Invitations as the City's
first invited visiting mage; he does NOT enter the seven cast tiers.

Run from repo root:
    python cityofmages/grimoire/scripts/merge_v1_7_1_patch.py
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[2]
GRIMOIRE_DIR = REPO_ROOT / "grimoire"
BASE_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_7_0.json"
PATCH_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_7_1_patch.json"
OUT_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_7_1.json"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def strip_meta_keys(d: dict) -> dict:
    return {k: v for k, v in d.items() if not k.startswith("$")}


# ----------------------------------------------------------------------
# v1.7.1 apply functions
# ----------------------------------------------------------------------

def apply_top_level_replacements(base: dict, patch: dict, log: list[str]) -> None:
    repls = patch.get("top_level_replacements", {})
    for k, v in repls.items():
        if k.startswith("$"):
            continue
        prior = base.get(k, "<absent>")
        base[k] = v
        log.append(f"top_level: {k} := (len={len(str(v))}; was len={len(str(prior))})")


def apply_simple_top_level(base: dict, patch: dict, key: str, target_key: str | None,
                           log: list[str], log_suffix: str = "") -> None:
    """Store a new top-level block from the patch under target_key (or key if None)."""
    block = patch.get(key)
    if not isinstance(block, dict):
        return
    block_clean = strip_meta_keys(block)
    tk = target_key or key
    base[tk] = block_clean
    log.append(f"{tk}: add NEW top-level block{(' · ' + log_suffix) if log_suffix else ''}")


def apply_tower_amendments(base: dict, patch: dict, log: list[str]) -> None:
    """Store tower_amendments_v1_7_1 alongside the v1.7.0 tower_spatial_anatomy block
    (without overwriting). The v1.7.0 admission is preserved per the patch's explicit
    `preserved_from_v1_7_0_unchanged` field."""
    block = patch.get("tower_amendments_v1_7_1")
    if not isinstance(block, dict):
        return
    block_clean = strip_meta_keys(block)
    base["tower_amendments_v1_7_1"] = block_clean
    log.append(
        "tower_amendments_v1_7_1: stored (Tower is infinite · instant recognition canonical · "
        "eastern face elaborated · 5 operational roles)"
    )


def apply_persona_additions(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("personas_additions", {})
    personas = base.setdefault("personas", {})

    # invited_visiting_mages — NEW persona sub-block (parallel to v1.7.0's spirit_mages).
    ivm = strip_meta_keys(additions.get("invited_visiting_mages", {}))
    if ivm:
        ivm_target = personas.setdefault("invited_visiting_mages", {})
        for key, val in ivm.items():
            if key == "tier_note":
                continue
            if key in ivm_target:
                log.append(f"personas.invited_visiting_mages: SKIP existing {key!r}")
                continue
            ivm_target[key] = val
            log.append(f"personas.invited_visiting_mages: add {key!r}")
        tn = additions.get("invited_visiting_mages", {}).get("tier_note")
        if tn and "tier_note" not in ivm_target:
            ivm_target["tier_note"] = tn

        tt = personas.get("tier_taxonomy")
        if isinstance(tt, dict) and "invited_visiting_mages" not in tt:
            tt["invited_visiting_mages"] = (
                "External to the cast roster's seven tiers. Admitted to the Register of "
                "Invitations by congruent geometry. Authority limited to the invited folio. "
                "Vitalik 🪑 (placeholder sigil · v1.7.1)."
            )
            log.append("personas.tier_taxonomy: extended with invited_visiting_mages note")


def apply_tome_additions(base: dict, patch: dict, log: list[str]) -> None:
    """Tome VIII Act 2 is admitted as a new entry under tome-viii-the-library.tome_act_files.
    Also updates tome_status and tome_future_act_candidates from the patch."""
    additions = strip_meta_keys(patch.get("spellbooks_tomes_additions", {}))
    if not additions:
        return
    tomes_root = (
        base.setdefault("spellbooks", {}).setdefault("tomes", {}).setdefault("tomes", {})
    )
    tv8 = tomes_root.get("tome-viii-the-library")
    if not isinstance(tv8, dict):
        log.append("tomes.tome-viii-the-library: NOT FOUND — v1.7.1 act-2 addition skipped")
        return

    # Act 2 entry — keyed as "tome-viii-the-library-act-2" in the patch.
    act_entry = additions.get("tome-viii-the-library-act-2")
    if isinstance(act_entry, dict):
        act_files = tv8.setdefault("tome_act_files", {})
        if "tome-viii-act-2" in act_files:
            log.append("tomes.tome-viii-the-library.tome_act_files['tome-viii-act-2']: SKIP existing")
        else:
            # Normalise the patch's flat-format act entry into the same shape as Act 1.
            normalised = {
                "act_number": act_entry.get("act_number", 2),
                "act_title": act_entry.get("act_title", "The Fourth Turn"),
                "act_file": act_entry.get("act_file"),
                "act_status": act_entry.get("act_status"),
                "act_length_words_estimate": act_entry.get("act_length_words_estimate"),
                "act_voice": act_entry.get("act_voice"),
                "act_cast_introduced": act_entry.get("act_cast_introduced"),
                "act_cast_tier_introduced": act_entry.get("act_cast_tier_introduced"),
                "act_v6_lineage_carries": act_entry.get("act_v6_lineage_carries"),
                "act_simultaneous_filing": act_entry.get("act_simultaneous_filing"),
                "act_teaches": act_entry.get("act_teaches"),
            }
            # Drop None values to keep the head clean.
            normalised = {k: v for k, v in normalised.items() if v is not None}
            act_files["tome-viii-act-2"] = normalised
            log.append("tomes.tome-viii-the-library.tome_act_files['tome-viii-act-2']: added")

    # tome_status update — string replacement.
    status_update = additions.get("tome_viii_status_updated_at_v1_7_1")
    if isinstance(status_update, str):
        tv8["tome_status"] = status_update
        log.append("tomes.tome-viii-the-library.tome_status: updated for v1.7.1")

    # tome_future_act_candidates extension.
    new_candidates = additions.get("tome_viii_future_act_candidates_v1_7_1_addition")
    if isinstance(new_candidates, list):
        candidates = tv8.setdefault("tome_future_act_candidates", [])
        appended = 0
        existing_set = set(str(c) for c in candidates)
        for c in new_candidates:
            if str(c) in existing_set:
                log.append("tomes.tome-viii-the-library.tome_future_act_candidates: SKIP duplicate")
                continue
            candidates.append(c)
            appended += 1
        if appended:
            log.append(f"tomes.tome-viii-the-library.tome_future_act_candidates: appended {appended}")


def apply_register_entries(base: dict, patch: dict, log: list[str]) -> None:
    """Store the register_entries_additions block under register_of_invitations.entries."""
    block = patch.get("register_entries_additions")
    if not isinstance(block, dict):
        return
    entries_src = block.get("register_of_invitations_entries", {})
    if not isinstance(entries_src, dict):
        return
    target = base.setdefault("register_of_invitations", {}).setdefault("entries", {})
    appended = 0
    for entry_id, entry in entries_src.items():
        if entry_id in target:
            log.append(f"register_of_invitations.entries.{entry_id}: SKIP existing")
            continue
        target[entry_id] = entry
        appended += 1
    log.append(f"register_of_invitations.entries: appended {appended}")


def apply_canonical_phrases(base: dict, patch: dict, log: list[str]) -> None:
    block = strip_meta_keys(patch.get("canonical_phrases_v1_7_1", {}))
    if not block:
        return
    target = base.setdefault("canonical_phrases", {})
    bucket = target.setdefault("v1_7_1", {})
    for k, v in block.items():
        bucket[k] = v
    log.append(f"canonical_phrases.v1_7_1: stored {len(block)} phrase entries")


def apply_v6_lineage(base: dict, patch: dict, log: list[str]) -> None:
    additions = strip_meta_keys(patch.get("v6_lineage_register_additions", {}))
    register = base.setdefault("v6_lineage_register", {}).setdefault("register", {})
    for ckey, centry in additions.items():
        if ckey in register:
            log.append(f"v6_lineage_register.{ckey}: SKIP existing (v1.7.1 is additive)")
            continue
        register[ckey] = centry
        title = centry.get("title", "?") if isinstance(centry, dict) else "?"
        log.append(f"v6_lineage_register: add {ckey} ({title})")


def apply_spec_amendments(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("spec_amendments_recorded")
    if not isinstance(block, dict):
        return
    audit = base.setdefault("spec_amendments_history", {})
    v171_entry = strip_meta_keys(block)
    audit["v1_7_1"] = v171_entry
    log.append("spec_amendments_history.v1_7_1: recorded (spec 05 §4.10 elaboration · invitation-protocol spec deferred)")


def apply_city_anatomy(base: dict, patch: dict, log: list[str]) -> None:
    amendments = strip_meta_keys(patch.get("city_anatomy_amendments", {}))
    if not amendments:
        return
    ca = base.setdefault("city_anatomy", {})
    annex = ca.setdefault("v1_7_1_amendments", {})
    for k, v in amendments.items():
        annex[k] = v
    log.append(
        "city_anatomy.v1_7_1_amendments: stored (workshops UNCHANGED · anatomy UNCHANGED · "
        "tiers UNCHANGED · tomes opened UNCHANGED · postures 3→4 · invited mages 0→1 · "
        "register entries 0→1 · Tome VIII bound acts 1→2)"
    )


def apply_ipfs_pin_status(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("ipfs_pin_status_amendments", {})
    if not block:
        return
    target = base.setdefault("ipfs_pin_status_history", {})
    v17_status = block.get("v1_7_0_pin_status_at_v1_7_1_authoring")
    if v17_status:
        # Annotate the existing v1_7_0 entry with the authoring-time pin status.
        existing = target.get("v1_7_0")
        if isinstance(existing, dict):
            existing["status_at_v1_7_1_authoring"] = v17_status.get("status", "")
        else:
            target["v1_7_0"] = v17_status
        log.append("ipfs_pin_status_history.v1_7_0: annotated with v1.7.1-authoring-time status")
    v171_pending = block.get("v1_7_1_pin_pending")
    if v171_pending:
        target["v1_7_1"] = v171_pending
        base["ipfs_pin_status_v1_7_1_note"] = v171_pending.get("pin_status_note", "")
        log.append("ipfs_pin_status_history.v1_7_1: recorded pending")


def apply_version_notes(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("version_notes_addition", {})
    entry = block.get("version_notes_entry")
    if not isinstance(entry, dict):
        return
    vn = base.setdefault("version_notes", {})
    canonical_key = "v" + str(entry.get("version", "1.7.1"))
    if canonical_key in vn:
        log.append(f"version_notes: SKIP existing {canonical_key!r}")
        return
    sample = next(iter(vn.values())) if vn else None
    if isinstance(sample, dict) and "date" in sample and "changes" in sample:
        changes = list(entry.get("additions", []) or [])
        if entry.get("title"):
            changes = [entry["title"] + " — " + entry.get("summary", "")] + changes
        vn[canonical_key] = {
            "date": entry.get("date", "2026-05-17"),
            "changes": changes,
        }
    else:
        vn[canonical_key] = entry
    log.append(f"version_notes[{canonical_key!r}]: added")


# ----------------------------------------------------------------------
# Main merge
# ----------------------------------------------------------------------

def main() -> int:
    for p in (BASE_PATH, PATCH_PATH):
        if not p.exists():
            print(f"ERROR: missing {p}", file=sys.stderr)
            return 1

    base = load_json(BASE_PATH)
    patch = load_json(PATCH_PATH)
    log: list[str] = []

    log.append("=== applying v1.7.1 patch (additive · no supersessions) ===")
    apply_top_level_replacements(base, patch, log)

    # NEW top-level structural blocks (each stored as-is, parallel to v1.7.0's
    # spirit_mage_tier / tower_spatial_anatomy pattern).
    apply_simple_top_level(base, patch, "register_of_invitations_introduced",
                           "register_of_invitations", log,
                           log_suffix="NEW structural register · sister to bound tomes")
    apply_simple_top_level(base, patch, "tome_postures_introduced",
                           "tome_postures", log,
                           log_suffix="4 postures · invitation 🪑 added · clerical glyphs bound")
    apply_simple_top_level(base, patch, "library_of_joint_authorship_introduced",
                           "library_of_joint_authorship", log,
                           log_suffix="NEW destination on acceptance · empty at v1.7.1")
    apply_simple_top_level(base, patch, "archive_of_unfilled_forms_introduced",
                           "archive_of_unfilled_forms", log,
                           log_suffix="NEW destination on expiry by silence · empty at v1.7.1")
    apply_simple_top_level(base, patch, "four_conditions_of_update_bound",
                           "four_conditions_of_update", log,
                           log_suffix="city-wide editorial protocol · 4 conditions bound")

    apply_tower_amendments(base, patch, log)
    apply_persona_additions(base, patch, log)
    apply_tome_additions(base, patch, log)
    apply_register_entries(base, patch, log)
    apply_canonical_phrases(base, patch, log)
    apply_v6_lineage(base, patch, log)
    apply_spec_amendments(base, patch, log)
    apply_city_anatomy(base, patch, log)
    apply_ipfs_pin_status(base, patch, log)
    apply_version_notes(base, patch, log)

    # Strip prior v1.7.0 merge_provenance and tag the head with v1.7.1 provenance.
    base.pop("$merge_provenance", None)
    base["$merge_provenance"] = {
        "produced_by": "cityofmages/grimoire/scripts/merge_v1_7_1_patch.py",
        "merged_at": datetime.now(timezone.utc).isoformat(),
        "base": "city_of_mages_grimoire_v1_7_0.json (merged 2026-05-17 14:06 UTC · pin in progress user-side per chronicles/2026-05-17_v1_7_0_pin_prep_handoff.md)",
        "patches_applied_in_order": [
            "city_of_mages_grimoire_v1_7_1_patch.json (2026-05-17 · additive · no supersessions)",
        ],
        "head_status": "pinnable · canonical v1.7.1 head",
        "head_signature": "(⚔️⊥⿻⊥🧙)😊",
        "additive_patch_note": (
            "v1.7.1 is the City of Mages' second purely-additive patch (after v1.7.0). "
            "No v1.7.0 cast retired, no workshop renamed, no spatial-anatomy element renumbered. "
            "Workshop count UNCHANGED at 16. Spatial-anatomy UNCHANGED at 8. Cast tiers UNCHANGED at 7. "
            "Tomes opened UNCHANGED at 8. Vitalik enters the Register of Invitations as the City's "
            "first invited visiting mage (external to the cast roster's seven tiers)."
        ),
    }

    save_json(OUT_PATH, base)

    log_path = OUT_PATH.with_suffix(".merge.log")
    with log_path.open("w", encoding="utf-8") as f:
        f.write(f"merge complete: {OUT_PATH}\n")
        f.write(f"timestamp: {datetime.now(timezone.utc).isoformat()}\n")
        f.write(f"actions: {len(log)}\n\n")
        for line in log:
            f.write(line + "\n")

    safe = lambda s: s.encode("ascii", "replace").decode("ascii")
    print(f"merge complete -> {safe(str(OUT_PATH))}")
    print(f"action log    -> {safe(str(log_path))}")
    print(f"total actions: {len(log)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
