#!/usr/bin/env python3
"""
merge_v1_7_0_patch.py — Produce the canonical v1.7.0 grimoire head JSON.

The merge applies a single PURELY ADDITIVE patch over the v1.6.0 head:
    v1.6.0  (canonical IPFS pin: bafybeiap6kvy3tp2bndpk65ti57qngr7ill37gqgasp2sxmgder3akotru)
    + v1.7.0 patch  (the Tower as 8th spatial-anatomy element;
                     spirit-Mage as 7th cast tier;
                     the Archivist 📚 as first instance;
                     Tome VIII · The Library opens with Act 1 The Spiraling Tower;
                     C64 candidate; spec 05 §4.9 + spec 08 §3.6 amendments recorded)
    → city_of_mages_grimoire_v1_7_0.json   (self-contained head; ready for IPFS pin)

v1.7.0 is structurally simpler than v1.6.0 because the patch carries
`supersedes: []` — no cast removal, no workshop rename, no shop supersession.
All changes are appends or annotations. See chronicle:
    cityofmages/chronicles/2026-05-16_grimoire_v1_7_0_patch_authored.md §1

Run from repo root:
    python cityofmages/grimoire/scripts/merge_v1_7_0_patch.py
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[2]
GRIMOIRE_DIR = REPO_ROOT / "grimoire"
BASE_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_6_0.json"
PATCH_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_7_0_patch.json"
OUT_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_7_0.json"


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
# v1.7.0 apply functions
# ----------------------------------------------------------------------

def apply_top_level_replacements(base: dict, patch: dict, log: list[str]) -> None:
    repls = patch.get("top_level_replacements", {})
    for k, v in repls.items():
        if k.startswith("$"):
            continue
        prior = base.get(k, "<absent>")
        base[k] = v
        log.append(f"top_level: {k} := (len={len(str(v))}; was len={len(str(prior))})")


def apply_spirit_mage_tier(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("spirit_mage_tier_introduced")
    if not isinstance(block, dict):
        return
    block_clean = strip_meta_keys(block)
    base["spirit_mage_tier"] = block_clean
    log.append("spirit_mage_tier: add NEW top-level block (7th cast tier · tutelary register)")


def apply_tower_spatial_anatomy(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("tower_spatial_anatomy_introduced")
    if not isinstance(block, dict):
        return
    block_clean = strip_meta_keys(block)
    base["tower_spatial_anatomy"] = block_clean
    log.append("tower_spatial_anatomy: add NEW top-level block (8th spatial-anatomy element · monument-form)")


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
            log.append(f"cast_attachments: SKIP duplicate id={eid!r} (v1.7.0 is additive — no overwrites)")
            continue
        target.append(entry)
        appended += 1
    log.append(f"cast_attachments_v1_3_0: appended {appended} (the Archivist · B_cross_shop · tower-bound)")


def apply_persona_additions(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("personas_additions", {})
    personas = base.setdefault("personas", {})

    # spirit_mages sub-block (NEW · parallel to cosmological_witnesses)
    sm = strip_meta_keys(additions.get("spirit_mages", {}))
    if sm:
        sm_target = personas.setdefault("spirit_mages", {})
        for key, val in sm.items():
            if key == "tier_note":
                continue
            if key in sm_target:
                log.append(f"personas.spirit_mages: SKIP existing {key!r}")
                continue
            sm_target[key] = val
            log.append(f"personas.spirit_mages: add {key!r}")
        tn = additions.get("spirit_mages", {}).get("tier_note")
        if tn and "tier_note" not in sm_target:
            sm_target["tier_note"] = tn

        # Extend tier_taxonomy with spirit_mages note
        tt = personas.get("tier_taxonomy")
        if isinstance(tt, dict) and "spirit_mages" not in tt:
            tt["spirit_mages"] = (
                "Tutelary figures recognized rather than summoned. The cast entry "
                "comes later than the inhabiting; the monument is honor-built by the "
                "cast collectively. the Archivist 📚 (Tower-resident · v1.7.0)."
            )
            log.append("personas.tier_taxonomy: extended with spirit_mages note")

    # soulbae_amendment_v1_7_0 — annotation only (find soulbae nested in personas.archetypes)
    amend = additions.get("soulbae_amendment_v1_7_0")
    if isinstance(amend, dict):
        added_fields = amend.get("added_fields", {})
        archetypes = personas.get("archetypes", {})
        soulbae = archetypes.get("soulbae")
        if isinstance(soulbae, dict):
            for k, v in added_fields.items():
                if k in soulbae:
                    log.append(f"personas.archetypes.soulbae: SKIP existing field {k!r}")
                    continue
                soulbae[k] = v
                log.append(f"personas.archetypes.soulbae: annotate {k!r}")
        else:
            log.append("personas.archetypes.soulbae: NOT FOUND — soulbae annotation skipped")


def apply_spell_additions(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("spells_additions", {})
    by_persona = base.setdefault("spells", {}).setdefault("by_persona", {})
    for persona_id, spells in additions.items():
        if persona_id.startswith("$"):
            continue
        if not isinstance(spells, list):
            continue
        # Normalise patch's `<persona>-spells` key to canonical `<persona>` (matches v1.6.0 convention)
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


def apply_tome_additions(base: dict, patch: dict, log: list[str]) -> None:
    tomes_root = (
        base.setdefault("spellbooks", {}).setdefault("tomes", {}).setdefault("tomes", {})
    )
    tomes_additions = strip_meta_keys(patch.get("spellbooks_tomes_additions", {}))
    for key, val in tomes_additions.items():
        if not isinstance(val, dict):
            continue
        if key in tomes_root:
            log.append(f"tomes.{key}: SKIP existing")
            continue
        tomes_root[key] = val
        log.append(f"tomes: add {key!r} (Tome VIII · The Library opens · Act 1 bound)")


def apply_v6_lineage(base: dict, patch: dict, log: list[str]) -> None:
    additions = strip_meta_keys(patch.get("v6_lineage_register_additions", {}))
    register = base.setdefault("v6_lineage_register", {}).setdefault("register", {})
    for ckey, centry in additions.items():
        if ckey in register:
            log.append(f"v6_lineage_register.{ckey}: SKIP existing (v1.7.0 is additive)")
            continue
        register[ckey] = centry
        log.append(f"v6_lineage_register: add {ckey} ({centry.get('title','?')})")


def apply_spec_amendments(base: dict, patch: dict, log: list[str]) -> None:
    """Record spec amendments as audit trail (not merged into operational structures)."""
    block = patch.get("spec_amendments_recorded")
    if not isinstance(block, dict):
        return
    audit = base.setdefault("spec_amendments_history", {})
    v17_entry = strip_meta_keys(block)
    audit["v1_7_0"] = v17_entry
    log.append("spec_amendments_history.v1_7_0: recorded (spec 05 §4.9 · spec 08 §3.6)")


def apply_city_anatomy(base: dict, patch: dict, log: list[str]) -> None:
    amendments = strip_meta_keys(patch.get("city_anatomy_amendments", {}))
    if not amendments:
        return
    ca = base.setdefault("city_anatomy", {})
    annex = ca.setdefault("v1_7_0_amendments", {})
    for k, v in amendments.items():
        annex[k] = v
    log.append("city_anatomy.v1_7_0_amendments: stored amendments block (anatomy 7→8 · tiers 6→7 · cast +1 · workshops UNCHANGED · tomes 7→8)")


def apply_ipfs_pin_status(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("ipfs_pin_status_amendments", {})
    if not block:
        return
    target = base.setdefault("ipfs_pin_status_history", {})
    v16 = block.get("v1_6_0_pin_recorded")
    if v16:
        target["v1_6_0"] = v16
        log.append("ipfs_pin_status_history.v1_6_0: recorded (CID + sync.agentprivacy.ai)")
    v17 = block.get("v1_7_0_pin_pending")
    if v17:
        target["v1_7_0"] = v17
        base["ipfs_pin_status_v1_7_0_note"] = v17.get("pin_status_note", "")
        log.append("ipfs_pin_status_history.v1_7_0: recorded pending")


def apply_version_notes(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("version_notes_addition", {})
    entry = block.get("version_notes_entry")
    if not isinstance(entry, dict):
        return
    vn = base.setdefault("version_notes", {})
    canonical_key = "v" + str(entry.get("version", "1.7.0"))
    if canonical_key in vn:
        log.append(f"version_notes: SKIP existing {canonical_key!r}")
        return
    sample = next(iter(vn.values())) if vn else None
    if isinstance(sample, dict) and "date" in sample and "changes" in sample:
        changes = entry.get("additions", [])
        if entry.get("title"):
            changes = [entry["title"] + " — " + entry.get("summary", "")] + list(changes)
        vn[canonical_key] = {
            "date": entry.get("date", "2026-05-16"),
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

    log.append("=== applying v1.7.0 patch (additive · no supersessions) ===")
    apply_top_level_replacements(base, patch, log)
    apply_spirit_mage_tier(base, patch, log)
    apply_tower_spatial_anatomy(base, patch, log)
    apply_cast_attachment_additions(base, patch, log)
    apply_persona_additions(base, patch, log)
    apply_spell_additions(base, patch, log)
    apply_tome_additions(base, patch, log)
    apply_v6_lineage(base, patch, log)
    apply_spec_amendments(base, patch, log)
    apply_city_anatomy(base, patch, log)
    apply_ipfs_pin_status(base, patch, log)
    apply_version_notes(base, patch, log)

    # Strip prior v1.6.0 merge_provenance and tag the head with v1.7.0 provenance.
    base.pop("$merge_provenance", None)
    base["$merge_provenance"] = {
        "produced_by": "cityofmages/grimoire/scripts/merge_v1_7_0_patch.py",
        "merged_at": datetime.now(timezone.utc).isoformat(),
        "base": "city_of_mages_grimoire_v1_6_0.json (pin: bafybeiap6kvy3tp2bndpk65ti57qngr7ill37gqgasp2sxmgder3akotru)",
        "patches_applied_in_order": [
            "city_of_mages_grimoire_v1_7_0_patch.json (2026-05-16 · additive · no supersessions)",
        ],
        "head_status": "pinnable · canonical v1.7.0 head",
        "head_signature": "(⚔️⊥⿻⊥🧙)😊",
        "additive_patch_note": (
            "v1.7.0 is the City of Mages' first purely-additive patch. "
            "No v1.6.0 cast member retired, no workshop renamed, no shop superseded. "
            "Workshop count UNCHANGED at 16."
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
