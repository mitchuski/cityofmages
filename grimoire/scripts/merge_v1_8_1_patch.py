#!/usr/bin/env python3
"""
merge_v1_8_1_patch.py — Produce the canonical v1.8.1 grimoire head JSON.

The merge applies a single PURELY ADDITIVE patch over the v1.8.0 head:
    v1.8.0  (canonical IPFS pin: bafybeihx7zn3frj6gln4bw5k3pxqnxoyumj42x4ohsjrhmro6q5vndw3ei)
    + v1.8.1 patch  (the City's SECOND spirit-Mage — the Librarian 🗃️ — as the Layer-2
                     attachment of the Chronicler; the Wikis as a NEW LEVEL within the Tower
                     (not a ninth element); Tome VIII Act 6 The Wikis and the Librarian bound;
                     C64 advances from candidate toward class on the second instance;
                     spec 05 §4.11 amendment recorded)
    → city_of_mages_grimoire_v1_8_1.json   (self-contained head; ready for IPFS pin)

v1.8.1 is purely additive: no cast removal, no workshop rename, no shop supersession.
Counts UNCHANGED: workshops 16, spatial-anatomy elements 8 (the Wikis are a LEVEL within
the Tower, not a ninth element), primary personas 42 (the Librarian is a Layer-2 attachment).
See chronicle: cityofmages/chronicles/2026-06-21_librarian_admitted_the_wikis_open.md

Run from repo root:
    python cityofmages/grimoire/scripts/merge_v1_8_1_patch.py
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[2]
GRIMOIRE_DIR = REPO_ROOT / "grimoire"
BASE_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_8_0.json"
PATCH_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_8_1_patch.json"
OUT_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_8_1.json"


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
# v1.8.1 apply functions
# ----------------------------------------------------------------------

def apply_top_level_replacements(base: dict, patch: dict, log: list[str]) -> None:
    repls = patch.get("top_level_replacements", {})
    for k, v in repls.items():
        if k.startswith("$"):
            continue
        prior = base.get(k, "<absent>")
        base[k] = v
        log.append(f"top_level: {k} := (len={len(str(v))}; was len={len(str(prior))})")


def apply_cast_attachment_additions(base: dict, patch: dict, log: list[str]) -> None:
    additions = (
        patch.get("attachment_architecture", {})
        .get("cast_attachments_v1_3_0_additions", [])
    )
    if not additions:
        return
    target = base.setdefault("attachment_architecture", {}).setdefault(
        "cast_attachments_v1_3_0", []
    )
    by_id = {e.get("id"): i for i, e in enumerate(target) if isinstance(e, dict)}
    appended = 0
    for entry in additions:
        eid = entry.get("id")
        if eid in by_id:
            log.append(f"cast_attachments: SKIP duplicate id={eid!r} (v1.8.1 is additive — no overwrites)")
            continue
        target.append(entry)
        appended += 1
    log.append(f"cast_attachments_v1_3_0: appended {appended} (the Librarian · B_cross_shop · tower-bound · Chronicler attachment)")


def apply_persona_additions(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("personas_additions", {})
    personas = base.setdefault("personas", {})

    sm = additions.get("spirit_mages", {})
    if sm:
        sm_target = personas.setdefault("spirit_mages", {})
        for key, val in sm.items():
            if key.startswith("$") or key == "tier_taxonomy_update":
                continue
            if key in sm_target:
                log.append(f"personas.spirit_mages: SKIP existing {key!r}")
                continue
            sm_target[key] = val
            log.append(f"personas.spirit_mages: add {key!r} (the Librarian · second instance)")

        # tier_taxonomy update (replace the spirit_mages note to name both instances)
        tt_update = sm.get("tier_taxonomy_update", {})
        new_note = tt_update.get("spirit_mages")
        if new_note:
            tt = personas.get("tier_taxonomy")
            if isinstance(tt, dict):
                tt["spirit_mages"] = new_note
                log.append("personas.tier_taxonomy.spirit_mages: updated to name both instances (Archivist + Librarian)")


def apply_spell_additions(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("spells_additions", {})
    by_persona = base.setdefault("spells", {}).setdefault("by_persona", {})
    for persona_id, spells in additions.items():
        if persona_id.startswith("$"):
            continue
        if not isinstance(spells, list):
            continue
        canonical_id = persona_id[:-7] if persona_id.endswith("-spells") else persona_id
        target = by_persona.setdefault(canonical_id, [])
        by_id = {s.get("id") or s.get("spell_id"): i for i, s in enumerate(target) if isinstance(s, dict)}
        appended = 0
        for spell in spells:
            sid = spell.get("id") or spell.get("spell_id")
            if sid in by_id:
                log.append(f"spells.{persona_id}: SKIP duplicate id={sid!r}")
                continue
            target.append(spell)
            appended += 1
        log.append(f"spells.by_persona[{canonical_id!r}]: appended {appended}")


def apply_tower_wikis_level(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("tower_wikis_level_introduced")
    if not isinstance(block, dict):
        return
    block_clean = strip_meta_keys(block)
    tsa = base.setdefault("tower_spatial_anatomy", {})
    levels = tsa.setdefault("levels", {})
    if "the-wikis" in levels:
        log.append("tower_spatial_anatomy.levels.the-wikis: SKIP existing")
        return
    levels["the-wikis"] = block_clean
    log.append("tower_spatial_anatomy.levels: add the-wikis (NEW level within the Tower · not a ninth element)")


def apply_tome_act_additions(base: dict, patch: dict, log: list[str]) -> None:
    tomes_root = (
        base.setdefault("spellbooks", {}).setdefault("tomes", {}).setdefault("tomes", {})
    )
    additions = strip_meta_keys(patch.get("tome_act_additions", {}))
    for tome_key, block in additions.items():
        tome = tomes_root.get(tome_key)
        if not isinstance(tome, dict):
            log.append(f"tome_act_additions.{tome_key}: SKIP — tome not found in base")
            continue
        # status update
        status_update = block.get("tome_status_update")
        if status_update:
            tome["tome_status"] = status_update
            log.append(f"tomes.{tome_key}.tome_status: updated (6 bound acts)")
        # cast introduced additions
        for cast_id in block.get("tome_cast_introduced_additions", []):
            tci = tome.setdefault("tome_cast_introduced", [])
            if cast_id not in tci:
                tci.append(cast_id)
                log.append(f"tomes.{tome_key}.tome_cast_introduced: append {cast_id!r}")
        # act files additions
        act_files = tome.setdefault("tome_act_files", {})
        for act_key, act in block.get("tome_act_files_additions", {}).items():
            if act_key in act_files:
                log.append(f"tomes.{tome_key}.tome_act_files.{act_key}: SKIP existing")
                continue
            act_files[act_key] = act
            log.append(f"tomes.{tome_key}.tome_act_files: add {act_key!r} (Act 6 The Wikis and the Librarian)")


def apply_v6_lineage_advancement(base: dict, patch: dict, log: list[str]) -> None:
    additions = strip_meta_keys(patch.get("v6_lineage_advancement", {}))
    register = base.setdefault("v6_lineage_register", {}).setdefault("register", {})
    for ckey, annotation in additions.items():
        entry = register.get(ckey)
        if not isinstance(entry, dict):
            # If C64 isn't present as a dict, record the advance as a standalone note
            register[ckey] = annotation
            log.append(f"v6_lineage_register: {ckey} not found as dict — stored advance annotation directly")
            continue
        for ak, av in annotation.items():
            entry[ak] = av
            log.append(f"v6_lineage_register.{ckey}: annotate {ak!r} (second-instance advance)")


def apply_spec_amendments(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("spec_amendments_recorded")
    if not isinstance(block, dict):
        return
    audit = base.setdefault("spec_amendments_history", {})
    audit["v1_8_1"] = strip_meta_keys(block)
    log.append("spec_amendments_history.v1_8_1: recorded (spec 05 §4.11 the Wikis)")


def apply_city_anatomy(base: dict, patch: dict, log: list[str]) -> None:
    amendments = strip_meta_keys(patch.get("city_anatomy_amendments", {}))
    if not amendments:
        return
    ca = base.setdefault("city_anatomy", {})
    ca["v1_8_1_amendments"] = amendments
    log.append("city_anatomy.v1_8_1_amendments: stored (spirit-Mage instances 1→2 · cast +1 · spatial-anatomy UNCHANGED at 8 · workshops UNCHANGED at 16 · primaries UNCHANGED at 42)")


def apply_ipfs_pin_status(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("ipfs_pin_status_amendments", {})
    if not block:
        return
    target = base.setdefault("ipfs_pin_status_history", {})
    v180 = block.get("v1_8_0_pin_recorded")
    if v180:
        target["v1_8_0"] = v180
        log.append("ipfs_pin_status_history.v1_8_0: recorded (CID + sync.agentprivacy.ai)")
    v181 = block.get("v1_8_1_pin_pending")
    if v181:
        target["v1_8_1"] = v181
        base["ipfs_pin_status_v1_8_1_note"] = v181.get("pin_status_note", "")
        log.append("ipfs_pin_status_history.v1_8_1: recorded pending (re-pin is a MANUAL user step)")


def apply_version_notes(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("version_notes_addition", {})
    entry = block.get("version_notes_entry")
    if not isinstance(entry, dict):
        return
    vn = base.setdefault("version_notes", {})
    canonical_key = "v" + str(entry.get("version", "1.8.1"))
    if canonical_key in vn:
        log.append(f"version_notes: SKIP existing {canonical_key!r}")
        return
    sample = next(iter(vn.values())) if vn else None
    if isinstance(sample, dict) and "date" in sample and "changes" in sample:
        changes = entry.get("additions", [])
        if entry.get("title"):
            changes = [entry["title"] + " — " + entry.get("summary", "")] + list(changes)
        vn[canonical_key] = {
            "date": entry.get("date", "2026-06-21"),
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

    log.append("=== applying v1.8.1 patch (additive · no supersessions) ===")
    apply_top_level_replacements(base, patch, log)
    apply_cast_attachment_additions(base, patch, log)
    apply_persona_additions(base, patch, log)
    apply_spell_additions(base, patch, log)
    apply_tower_wikis_level(base, patch, log)
    apply_tome_act_additions(base, patch, log)
    apply_v6_lineage_advancement(base, patch, log)
    apply_spec_amendments(base, patch, log)
    apply_city_anatomy(base, patch, log)
    apply_ipfs_pin_status(base, patch, log)
    apply_version_notes(base, patch, log)

    base.pop("$merge_provenance", None)
    base["$merge_provenance"] = {
        "produced_by": "cityofmages/grimoire/scripts/merge_v1_8_1_patch.py",
        "merged_at": datetime.now(timezone.utc).isoformat(),
        "base": "city_of_mages_grimoire_v1_8_0.json (pin: bafybeihx7zn3frj6gln4bw5k3pxqnxoyumj42x4ohsjrhmro6q5vndw3ei)",
        "patches_applied_in_order": [
            "city_of_mages_grimoire_v1_8_1_patch.json (2026-06-21 · additive · no supersessions)",
        ],
        "head_status": "pinnable · canonical v1.8.1 head (IPFS re-pin is a MANUAL user step)",
        "head_signature": "(⚔️⊥⿻⊥🧙)😊",
        "additive_patch_note": (
            "v1.8.1 admits the second spirit-Mage (the Librarian 🗃️), the Wikis as a level "
            "within the Tower, and Tome VIII Act 6. Workshop count UNCHANGED at 16; "
            "spatial-anatomy elements UNCHANGED at 8; primary personas UNCHANGED at 42. "
            "C64 advances toward class on the tier's second instance."
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
