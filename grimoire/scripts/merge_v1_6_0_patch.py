#!/usr/bin/env python3
"""
merge_v1_6_0_patch.py — Produce the canonical v1.6.0 grimoire head JSON.

The merge chains three patches over the v1.4.0 base:
    v1.4.0  (canonical IPFS pin: bafkreib5w4bp6t5kkt4ebvjyjjzuxdupzaz6gtupbhgbrxtwkrxj7dfnsu)
    + v1.5.0 patch  (Tomes I/II/III bound, Tome VI opened, cosmological-witness tier,
                     Threshold workshop with three rooms, conjectures C48-C61)
    + v1.5.1 patch  (AAIF + BGIN kindred-coalitions, /hall → City Hall rename)
    + v1.6.0 patch  (Threshold District restructure, archetype-modal-shop pattern,
                     alexandrite_dual_aspect gem, Chart Shop at V44, Navigation District,
                     C58 promotion, C63 candidate)
    → city_of_mages_grimoire_v1_6_0.json   (self-contained head; ready for IPFS pin)

v1.5.0 and v1.5.1 patches never received standalone IPFS pins; this merge collapses
them into the v1.6.0 head per the 2026-05-14 editorial decision (see
chronicles/2026-05-14_grimoire_v1_6_0_patch_authored.md §1).

The merge precedence for overlapping sections is:
    v1.6.0 wins over v1.5.1 wins over v1.5.0 wins over v1.4.0 base
For sections only in earlier patches, the upstream content carries forward unchanged.

The output is intended to be IPFS-pinnable as the canonical v1.6.0 head. Unlike the
v1.5.0 *candidate* (which was working state), this is a final merge head.

Run from repo root:
    python cityofmages/grimoire/scripts/merge_v1_6_0_patch.py
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[2]
GRIMOIRE_DIR = REPO_ROOT / "grimoire"
BASE_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_4_0.json"
PATCH_V1_5_0 = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_5_0_patch.json"
PATCH_V1_5_1 = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_5_1_patch.json"
PATCH_V1_6_0 = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_6_0_patch.json"
OUT_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_6_0.json"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def strip_meta_keys(d: dict) -> dict:
    """Drop $comment / $-prefixed sibling docstrings from a patch sub-dict."""
    return {k: v for k, v in d.items() if not k.startswith("$")}


# ----------------------------------------------------------------------
# v1.5.0 apply functions (adapted from merge_v1_5_0_patch.py · streamlined)
# ----------------------------------------------------------------------

def apply_top_level_replacements(base: dict, patch: dict, log: list[str]) -> None:
    repls = patch.get("top_level_replacements", {})
    for k, v in repls.items():
        if k.startswith("$"):
            continue
        prior = base.get(k, "<absent>")
        base[k] = v
        log.append(f"top_level: {k} := (len={len(str(v))}; was len={len(str(prior))})")


def apply_cast_attachment_additions(base: dict, patch: dict, log: list[str],
                                    *, overwrite_by_id: bool = False) -> None:
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
    replaced = 0
    for entry in additions:
        eid = entry.get("id")
        if eid in by_id:
            if overwrite_by_id:
                target[by_id[eid]] = entry
                replaced += 1
            else:
                log.append(f"cast_attachments: SKIP duplicate id={eid!r}")
            continue
        target.append(entry)
        appended += 1
    log.append(
        f"cast_attachments_v1_3_0: appended {appended}, replaced {replaced} "
        f"(overwrite_by_id={overwrite_by_id})"
    )


def apply_persona_additions(base: dict, patch: dict, log: list[str],
                            *, overwrite_existing: bool = False) -> None:
    additions = patch.get("personas_additions", {})
    personas = base.setdefault("personas", {})

    def merge_section(section_key: str, target_key: str | None = None,
                      destination: dict | None = None) -> None:
        section = additions.get(section_key, {})
        section = strip_meta_keys(section)
        if destination is None:
            destination = personas
        for key, val in section.items():
            if key in destination and not overwrite_existing:
                log.append(f"personas.{section_key}: SKIP existing {key!r}")
                continue
            if key in destination and overwrite_existing:
                log.append(f"personas.{section_key}: OVERWRITE {key!r}")
            else:
                log.append(f"personas.{section_key}: add {key!r}")
            destination[key] = val

    merge_section("workshop_keepers_additions")
    merge_section("cross_shop_additions")

    cw = strip_meta_keys(additions.get("cosmological_witnesses", {}))
    if cw:
        cw_target = personas.setdefault("cosmological_witnesses", {})
        for key, val in cw.items():
            if key == "tier_note":
                continue
            if key in cw_target and not overwrite_existing:
                log.append(f"personas.cosmological_witnesses: SKIP existing {key!r}")
                continue
            cw_target[key] = val
            log.append(f"personas.cosmological_witnesses: {('overwrite' if overwrite_existing else 'add')} {key!r}")
        tn = additions.get("cosmological_witnesses", {}).get("tier_note")
        if tn and "tier_note" not in cw_target:
            cw_target["tier_note"] = tn

        tt = personas.get("tier_taxonomy")
        if isinstance(tt, dict) and "cosmological_witnesses" not in tt:
            tt["cosmological_witnesses"] = (
                "Pre-architectural figures the architecture inherits rather than "
                "summons. Selene 🌙 · Aether ⿻ · Lethe 🌀."
            )
            log.append("personas.tier_taxonomy: extended with cosmological_witnesses note")


def apply_spell_additions(base: dict, patch: dict, log: list[str],
                          *, overwrite_by_id: bool = False) -> None:
    additions = patch.get("spells_additions", {})
    by_persona = base.setdefault("spells", {}).setdefault("by_persona", {})
    for persona_id, spells in additions.items():
        if persona_id.startswith("$"):
            continue
        if not isinstance(spells, list):
            continue
        # Normalise the v1.6.0 amendment key (faunia_v1_6_0_amendment → faunia).
        canonical_id = persona_id
        if canonical_id.endswith("_v1_6_0_amendment"):
            canonical_id = canonical_id.replace("_v1_6_0_amendment", "")
        target = by_persona.setdefault(canonical_id, [])
        by_id = {s.get("id"): i for i, s in enumerate(target) if isinstance(s, dict)}
        appended = 0
        replaced = 0
        for spell in spells:
            sid = spell.get("id")
            if sid in by_id:
                if overwrite_by_id:
                    target[by_id[sid]] = spell
                    replaced += 1
                else:
                    log.append(f"spells.{canonical_id}: SKIP duplicate id={sid!r}")
                continue
            target.append(spell)
            appended += 1
        log.append(
            f"spells.by_persona[{canonical_id!r}]: appended {appended}, replaced {replaced}"
        )


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
        log.append(f"tomes: add {key!r}")

    tv = patch.get("tome_v_additions", {})
    for act_key in ("act_16", "act_17"):
        if act_key not in tv:
            continue
        act_entry = tv[act_key]
        if not isinstance(act_entry, dict):
            continue
        tome_v = tomes_root.setdefault("tome-v", {})
        acts = tome_v.setdefault("acts", [])
        act_number = act_entry.get("act_number")
        already = any(
            isinstance(a, dict) and a.get("act_number") == act_number for a in acts
        )
        if already:
            for i, a in enumerate(acts):
                if isinstance(a, dict) and a.get("act_number") == act_number:
                    acts[i] = {**a, **act_entry}
                    log.append(f"tome-v.acts: merge update {act_number}")
                    break
        else:
            acts.append(act_entry)
            log.append(f"tome-v.acts: append {act_number}")
        try:
            n = int(act_number.split("·")[1])
            tome_v["act_count"] = max(tome_v.get("act_count", 0), n)
        except Exception:
            pass

    tvii = patch.get("tome_vii_additions", {})
    binding = tvii.get("act_1_binding_update")
    if binding:
        tome_vii = tomes_root.setdefault("tome-vii", {})
        acts = tome_vii.setdefault("acts", [])
        target = None
        for a in acts:
            if isinstance(a, dict) and a.get("act_number") == "VII·1":
                target = a
                break
        if target is None:
            acts.append(binding)
            log.append("tome-vii.acts: insert VII·1")
        else:
            target.update(binding)
            log.append("tome-vii.acts[VII·1]: merge binding_update")


def apply_vertex_inventory(base: dict, patch: dict, log: list[str]) -> None:
    additions = strip_meta_keys(patch.get("vertex_inventory_additions", {}))
    named = base.setdefault("vertex_inventory", {}).setdefault("named", {})
    for vkey, ventry in additions.items():
        if vkey == "V15_amendment_from_v1_5_1" or vkey.endswith("_amendment"):
            # V15 amendment in v1.5.1 / v1.6.0 patches — apply to existing V15.
            target_v = "V15"
            v15 = named.get(target_v)
            if isinstance(v15, dict):
                if "inhabitant_amended" in ventry:
                    v15["inhabitant"] = ventry["inhabitant_amended"]
                if "rename_note" in ventry:
                    v15["rename_note"] = ventry["rename_note"]
                if "name" in ventry:
                    v15["name"] = ventry["name"]
                if "source" in ventry:
                    v15["source"] = ventry["source"]
                log.append(f"vertex_inventory.named.V15: amended via {vkey}")
            continue
        if vkey == "V59_v1_5_0":
            target_v = "V59"
            if target_v in named:
                # v1.6.0's V59 entry carries inhabitant_v1_5_0_inception + inhabitant_v1_6_0_canonical
                # — merge intelligently.
                existing = named[target_v]
                merged = {**existing, **ventry}
                # Promote canonical inhabitant.
                if "inhabitant_v1_6_0_canonical" in ventry:
                    merged["inhabitant"] = ventry["inhabitant_v1_6_0_canonical"]
                named[target_v] = merged
                log.append(f"vertex_inventory.named.{target_v}: merged v1.6.0 succession")
            else:
                named[target_v] = ventry
                log.append(f"vertex_inventory.named.{target_v}: add (v1.6.0)")
            continue
        if vkey in named:
            # If existing entry came from v1.5.0 (e.g. V59 from v1.5.0 patch), allow v1.6.0 to overwrite.
            existing = named[vkey]
            named[vkey] = {**existing, **ventry} if isinstance(existing, dict) else ventry
            log.append(f"vertex_inventory.named.{vkey}: merge update")
            continue
        named[vkey] = ventry
        log.append(f"vertex_inventory.named: add {vkey}")


def apply_v6_lineage(base: dict, patch: dict, log: list[str]) -> None:
    additions = strip_meta_keys(patch.get("v6_lineage_register_additions", {}))
    register = base.setdefault("v6_lineage_register", {}).setdefault("register", {})

    note = additions.pop("RENUMBERING_NOTE_2026_05_13", None)
    if note:
        base["v6_lineage_register"]["renumbering_note_2026_05_13"] = note
        log.append("v6_lineage_register.renumbering_note_2026_05_13: stored")

    for ckey, centry in additions.items():
        if ckey == "C62_reserved":
            register["C62_reserved"] = centry
            log.append("v6_lineage_register: add C62_reserved")
            continue
        if ckey in register:
            existing = register[ckey]
            if isinstance(existing, dict) and isinstance(centry, dict):
                register[ckey] = {**existing, **centry}
                log.append(f"v6_lineage_register.{ckey}: merge update")
            else:
                register[ckey] = centry
                log.append(f"v6_lineage_register.{ckey}: replace")
            continue
        register[ckey] = centry
        log.append(f"v6_lineage_register: add {ckey} ({centry.get('name','?')})")


def apply_registry_entries(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("registry_entries_introduced", {})
    if "agent_substrate_frameworks" in additions:
        new = additions["agent_substrate_frameworks"]
        existing = base.get("agent_substrate_frameworks")
        if isinstance(existing, dict) and isinstance(new, dict):
            base["agent_substrate_frameworks"] = {**existing, **new}
            log.append("agent_substrate_frameworks: merge update")
        else:
            base["agent_substrate_frameworks"] = new
            log.append("agent_substrate_frameworks: add")


def apply_city_anatomy(base: dict, patch: dict, log: list[str]) -> None:
    amendments = strip_meta_keys(patch.get("city_anatomy_amendments", {}))
    if not amendments:
        return
    ca = base.setdefault("city_anatomy", {})
    # Store the cumulative amendments block as a v1_6_0 annex; the canonical
    # fields (trade_quarters, etc.) keep their v1.4.0 shape and the amendments
    # block names the counts the v1.5.0 / v1.5.1 / v1.6.0 work updated.
    annex = ca.setdefault("v1_6_0_amendments", {})
    for k, v in amendments.items():
        annex[k] = v
    log.append("city_anatomy.v1_6_0_amendments: stored amendments block")


def apply_ipfs_pin_status(base: dict, patch: dict, log: list[str]) -> None:
    amendments = patch.get("ipfs_pin_status_amendments", {})
    addition_text = amendments.get("addition_text", "")
    pin_note = amendments.get("pin_status_note", "")
    if addition_text:
        prior = base.get("ipfs_pin_status", "")
        base["ipfs_pin_status"] = (prior + " · " + addition_text) if prior else addition_text
        log.append("ipfs_pin_status: appended addition_text")
    if pin_note:
        base["ipfs_pin_status_v1_6_0_note"] = pin_note
        log.append("ipfs_pin_status_v1_6_0_note: stored")


def apply_version_notes(base: dict, patch: dict, log: list[str]) -> None:
    addition = strip_meta_keys(patch.get("version_notes_addition", {}))
    vn = base.setdefault("version_notes", {})
    for key, val in addition.items():
        canonical_key = key
        if key.startswith("v") and "_" in key:
            # v1_5_0 → v1.5.0
            canonical_key = key.replace("_", ".")
            if canonical_key.startswith("v.1."):
                canonical_key = canonical_key.replace("v.1.", "v1.", 1)
            if canonical_key.startswith("v1."):
                # Already in dotted form.
                pass
            else:
                # Fallback: replace first underscore after the v with a dot.
                canonical_key = canonical_key.replace("v1", "v1.", 1) if canonical_key.startswith("v1") else canonical_key
        if canonical_key in vn:
            log.append(f"version_notes: SKIP existing {canonical_key!r}")
            continue
        sample = next(iter(vn.values())) if vn else None
        if isinstance(sample, dict) and "date" in sample and "changes" in sample:
            today = patch.get("patch_metadata", {}).get("patch_date", "2026-05-14")
            vn[canonical_key] = {
                "date": today,
                "changes": [val] if isinstance(val, str) else val,
            }
        else:
            vn[canonical_key] = val
        log.append(f"version_notes[{canonical_key!r}]: added")


# ----------------------------------------------------------------------
# v1.5.1 apply functions
# ----------------------------------------------------------------------

def apply_v1_5_1_workshop_amendments(base: dict, patch: dict, log: list[str]) -> None:
    """Apply /hall → City Hall rename (route unchanged · sigil 🤝 → 🏛️)."""
    amendments = patch.get("workshop_amendments", {})
    rename = amendments.get("shop_hall_rename")
    if not rename:
        return
    # Record in a structured annex on city_anatomy.gathering_quarters.
    ca = base.setdefault("city_anatomy", {})
    gq = ca.get("gathering_quarters", [])
    for i, shop in enumerate(gq):
        if isinstance(shop, dict) and shop.get("shop") == "/hall":
            gq[i] = {
                **shop,
                "internal_name": rename.get("new_label", "City Hall"),
                "renamed_from": rename.get("old_label", "Ceremony Hall"),
                "rename_date": rename.get("rename_date"),
                "rename_reason": rename.get("rename_reason"),
                "sigil_amendment": rename.get("sigil_amendment"),
                "kindred_coalitions_in_residence": rename.get("kindred_coalitions_in_residence"),
                "ceremony_grammars_at_this_workshop": rename.get("ceremony_grammars_at_this_workshop"),
            }
            log.append("city_anatomy.gathering_quarters[/hall]: renamed Ceremony Hall → City Hall")
            return


def apply_v1_5_1_kindred_coalitions(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("kindred_coalitions_introduced")
    if not block or not isinstance(block, dict):
        return
    # Drop any sibling $-prefixed reference keys the v1.6.0 patch left at this location.
    block = {k: v for k, v in block.items() if not k.startswith("$")}
    if not block:
        return
    existing = base.get("kindred_coalitions")
    if isinstance(existing, dict) and isinstance(block, dict):
        base["kindred_coalitions"] = {**existing, **block}
        log.append("kindred_coalitions: merge update")
    else:
        base["kindred_coalitions"] = block
        log.append("kindred_coalitions: add (first instance · v1.5.1)")


# ----------------------------------------------------------------------
# v1.6.0 apply functions
# ----------------------------------------------------------------------

def apply_v1_6_0_workshop_districts(base: dict, patch: dict, log: list[str]) -> None:
    block = patch.get("workshop_districts_introduced")
    if not block or not isinstance(block, dict):
        return
    block_clean = strip_meta_keys(block)
    base["workshop_districts"] = block_clean
    log.append("workshop_districts: add (v1.6.0 · 2 districts: Threshold + Navigation)")


def apply_v1_6_0_pattern_introductions(base: dict, patch: dict, log: list[str]) -> None:
    patterns = base.setdefault("patterns_introduced", {})
    amsp = patch.get("archetype_modal_shop_pattern_introduced")
    if isinstance(amsp, dict):
        patterns["archetype_modal_shop"] = strip_meta_keys(amsp)
        log.append("patterns_introduced.archetype_modal_shop: add")

    gem_types = base.setdefault("gem_types_introduced", {})
    adag = patch.get("alexandrite_dual_aspect_gem_introduced")
    if isinstance(adag, dict):
        gem_types["alexandrite_dual_aspect"] = strip_meta_keys(adag)
        log.append("gem_types_introduced.alexandrite_dual_aspect: add")


# ----------------------------------------------------------------------
# Main merge
# ----------------------------------------------------------------------

def main() -> int:
    for p in (BASE_PATH, PATCH_V1_5_0, PATCH_V1_5_1, PATCH_V1_6_0):
        if not p.exists():
            print(f"ERROR: missing {p}", file=sys.stderr)
            return 1

    base = load_json(BASE_PATH)
    p150 = load_json(PATCH_V1_5_0)
    p151 = load_json(PATCH_V1_5_1)
    p160 = load_json(PATCH_V1_6_0)
    log: list[str] = []

    log.append("=== applying v1.5.0 patch ===")
    apply_top_level_replacements(base, p150, log)
    apply_cast_attachment_additions(base, p150, log)
    apply_persona_additions(base, p150, log)
    apply_spell_additions(base, p150, log)
    apply_tome_additions(base, p150, log)
    apply_vertex_inventory(base, p150, log)
    apply_v6_lineage(base, p150, log)
    apply_registry_entries(base, p150, log)
    apply_city_anatomy(base, p150, log)
    apply_ipfs_pin_status(base, p150, log)
    apply_version_notes(base, p150, log)

    log.append("=== applying v1.5.1 patch ===")
    apply_top_level_replacements(base, p151, log)
    apply_v1_5_1_workshop_amendments(base, p151, log)
    apply_v1_5_1_kindred_coalitions(base, p151, log)
    apply_vertex_inventory(base, {"vertex_inventory_additions": p151.get("vertex_inventory_amendments", {})}, log)
    apply_city_anatomy(base, p151, log)
    apply_ipfs_pin_status(base, p151, log)
    apply_version_notes(base, p151, log)

    log.append("=== applying v1.6.0 patch (head) ===")
    apply_top_level_replacements(base, p160, log)

    # v1.6.0 explicitly removes inception-state cast (Bestia · Therai) that
    # v1.5.0 added — the v1.6.0 head reflects ONLY the canonical names
    # (Pandia · Hermaion · Faunia-at-Familiars · Pleione · Caducea).
    removals = p160.get("$canonical_cast_removals_from_v1_5_0", {})
    drop_cast_ids = set(removals.get("cast_attachment_ids_to_drop", []))
    drop_persona_ids = set(removals.get("persona_ids_to_drop_from_workshop_keepers", []))
    drop_spell_persona_ids = set(removals.get("spells_persona_ids_to_drop", []))

    if drop_cast_ids:
        cast_list = base.get("attachment_architecture", {}).get(
            "cast_attachments_v1_3_0", []
        )
        before = len(cast_list)
        cast_list[:] = [e for e in cast_list if not (
            isinstance(e, dict) and e.get("id") in drop_cast_ids
        )]
        log.append(
            f"v1.6.0 removals · cast_attachments_v1_3_0: dropped "
            f"{before - len(cast_list)} ({sorted(drop_cast_ids)})"
        )

    if drop_persona_ids:
        personas = base.get("personas", {})
        dropped = []
        for pid in list(drop_persona_ids):
            if pid in personas:
                del personas[pid]
                dropped.append(pid)
        if dropped:
            log.append(f"v1.6.0 removals · personas: dropped {sorted(dropped)}")

    if drop_spell_persona_ids:
        by_persona = base.get("spells", {}).get("by_persona", {})
        dropped = []
        for pid in list(drop_spell_persona_ids):
            if pid in by_persona:
                del by_persona[pid]
                dropped.append(pid)
        if dropped:
            log.append(f"v1.6.0 removals · spells.by_persona: dropped {sorted(dropped)}")

    # v1.6.0 overwrites v1.5.0 cast attachments by id (Faunia · Bestia · Therai · Caducea
    # · Selene-cosmological all get v1.6.0 amendments; Pandia · Hermaion · Pleione are new).
    apply_cast_attachment_additions(base, p160, log, overwrite_by_id=True)
    apply_persona_additions(base, p160, log, overwrite_existing=True)
    apply_spell_additions(base, p160, log, overwrite_by_id=True)
    apply_tome_additions(base, p160, log)
    apply_vertex_inventory(base, p160, log)
    apply_v6_lineage(base, p160, log)
    apply_registry_entries(base, p160, log)
    apply_v1_6_0_workshop_districts(base, p160, log)
    apply_v1_6_0_pattern_introductions(base, p160, log)
    apply_city_anatomy(base, p160, log)
    apply_ipfs_pin_status(base, p160, log)
    apply_version_notes(base, p160, log)

    # Tag the head with provenance metadata.
    base["$merge_provenance"] = {
        "produced_by": "cityofmages/grimoire/scripts/merge_v1_6_0_patch.py",
        "merged_at": datetime.now(timezone.utc).isoformat(),
        "base": "city_of_mages_grimoire_v1_4_0.json (pin: bafkreib5w4bp6t5kkt4ebvjyjjzuxdupzaz6gtupbhgbrxtwkrxj7dfnsu)",
        "patches_applied_in_order": [
            "city_of_mages_grimoire_v1_5_0_patch.json (2026-05-13 · never pinned)",
            "city_of_mages_grimoire_v1_5_1_patch.json (2026-05-13 · never pinned)",
            "city_of_mages_grimoire_v1_6_0_patch.json (2026-05-14)",
        ],
        "head_status": "pinnable · canonical v1.6.0 head",
        "head_signature": "(⚔️⊥⿻⊥🧙)😊",
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
