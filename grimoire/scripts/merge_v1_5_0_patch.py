#!/usr/bin/env python3
"""
merge_v1_5_0_patch.py — Apply the structured-delta v1.5.0 patch to the
canonical v1.4.0 base grimoire and emit a CANDIDATE v1.5.0 JSON.

This is a draft merge. The output is NOT a re-pinnable canonical artefact;
the user must review the candidate, make any editorial choices that the
mechanical merge could not (renumberings, narrative-prose adjustments,
deduplication if the patch overlaps existing fields), and only then promote
the candidate to canonical v1.5.0 and re-pin to IPFS.

Run from repo root:
    python cityofmages/grimoire/scripts/merge_v1_5_0_patch.py

Output:
    cityofmages/grimoire/city_of_mages_grimoire_v1_5_0_candidate.json

The script applies each patch section by an explicit, named rule. See the
APPLY_RULES section below. Sections of the patch are NOT merged blindly —
each gets a documented decision.
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[2]
GRIMOIRE_DIR = REPO_ROOT / "grimoire"
BASE_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_4_0.json"
PATCH_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_5_0_patch.json"
OUT_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_5_0_candidate.json"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def apply_top_level_replacements(base: dict, patch: dict, log: list[str]) -> None:
    replacements = patch.get("top_level_replacements", {})
    for k, v in replacements.items():
        prior = base.get(k, "<absent>")
        base[k] = v
        log.append(f"top_level_replacements: set base['{k}'] (was: {str(prior)[:80]!r})")


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
    existing_ids = {e.get("id") for e in target if isinstance(e, dict)}
    appended = 0
    for entry in additions:
        if entry.get("id") in existing_ids:
            log.append(
                f"cast_attachments: SKIP duplicate id={entry.get('id')!r} (already in base)"
            )
            continue
        target.append(entry)
        appended += 1
    log.append(f"cast_attachments_v1_3_0: appended {appended} new entries")


def apply_persona_additions(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("personas_additions", {})
    personas = base.setdefault("personas", {})

    # workshop_keepers_additions → Faunia, Bestia, Therai → personas root (tier="summoned")
    wk_additions = additions.get("workshop_keepers_additions", {})
    for key, val in wk_additions.items():
        if key.startswith("$"):
            continue
        if key in personas:
            log.append(f"personas.workshop_keepers: SKIP existing key {key!r}")
            continue
        personas[key] = val
        log.append(f"personas: added {key!r} (workshop-keeper · tier=summoned)")

    # cross_shop_additions → Caducea → personas root (peripatetic)
    cs_additions = additions.get("cross_shop_additions", {})
    for key, val in cs_additions.items():
        if key.startswith("$"):
            continue
        if key in personas:
            log.append(f"personas.cross_shop: SKIP existing key {key!r}")
            continue
        personas[key] = val
        log.append(f"personas: added {key!r} (peripatetic)")

    # cosmological_witnesses → Selene, Aether, Lethe → new sub-tier
    cw_additions = additions.get("cosmological_witnesses", {})
    if cw_additions:
        # Place under personas as a new section that mirrors the existing structure.
        cw_target = personas.setdefault("cosmological_witnesses", {})
        for key, val in cw_additions.items():
            if key.startswith("$"):
                continue
            if key in cw_target:
                log.append(f"personas.cosmological_witnesses: SKIP existing {key!r}")
                continue
            cw_target[key] = val
            log.append(f"personas.cosmological_witnesses: added {key!r}")

        # Also update tier_taxonomy on personas root to mention the new tier.
        tt = personas.get("tier_taxonomy")
        if isinstance(tt, dict) and "cosmological_witnesses" not in tt:
            tt["cosmological_witnesses"] = (
                "Pre-architectural figures the architecture inherits rather than "
                "summons. Tome III binding pass (2026-05-13). Selene 🌙 (orbit) · "
                "Aether ⿻ (medium) · Lethe 🌀 (substrate)."
            )
            log.append("personas.tier_taxonomy: extended with cosmological_witnesses note")


def apply_spell_additions(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("spells_additions", {})
    by_persona = base.setdefault("spells", {}).setdefault("by_persona", {})
    for persona_id, spells in additions.items():
        if persona_id.startswith("$"):
            continue
        if not isinstance(spells, list):
            continue
        target = by_persona.setdefault(persona_id, [])
        existing_ids = {s.get("id") for s in target if isinstance(s, dict)}
        appended = 0
        for spell in spells:
            if spell.get("id") in existing_ids:
                log.append(
                    f"spells.{persona_id}: SKIP duplicate id={spell.get('id')!r}"
                )
                continue
            target.append(spell)
            appended += 1
        log.append(f"spells.by_persona[{persona_id!r}]: appended {appended} spells")


def apply_tome_additions(base: dict, patch: dict, log: list[str]) -> None:
    tomes_root = (
        base.setdefault("spellbooks", {}).setdefault("tomes", {}).setdefault("tomes", {})
    )

    # spellbooks_tomes_additions → tome-i / tome-ii / tome-iii / tome-vi added
    tomes_additions = patch.get("spellbooks_tomes_additions", {})
    for key, val in tomes_additions.items():
        if key.startswith("$"):
            continue
        if key in tomes_root:
            log.append(f"tomes.{key}: SKIP — already present in base")
            continue
        tomes_root[key] = val
        log.append(f"tomes: added new tome {key!r}")

    # tome_v_additions.act_16 → append to tome-v.acts
    tv = patch.get("tome_v_additions", {})
    if "act_16" in tv:
        tome_v = tomes_root.setdefault("tome-v", {})
        acts = tome_v.setdefault("acts", [])
        # Avoid duplicate insertion if a v15-equivalent run leaves act_16 around.
        already = any(
            isinstance(a, dict) and a.get("act_number") == "V·16" for a in acts
        )
        if already:
            log.append("tome-v.acts: SKIP — act V·16 already present")
        else:
            acts.append(tv["act_16"])
            tome_v["act_count"] = max(tome_v.get("act_count", 0), 16)
            log.append("tome-v.acts: appended act V·16 (The Threshold); act_count → 16")

    # tome_vii_additions.act_1_binding_update → mark act-1 as bound
    tvii = patch.get("tome_vii_additions", {})
    binding = tvii.get("act_1_binding_update")
    if binding:
        tome_vii = tomes_root.setdefault("tome-vii", {})
        acts = tome_vii.setdefault("acts", [])
        # Find or insert act 1.
        target = None
        for a in acts:
            if isinstance(a, dict) and a.get("act_number") == "VII·1":
                target = a
                break
        if target is None:
            acts.append(binding)
            log.append("tome-vii.acts: inserted bound act VII·1")
        else:
            target.update(binding)
            log.append("tome-vii.acts[VII·1]: merged binding_update fields")


def apply_vertex_inventory(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("vertex_inventory_additions", {})
    named = base.setdefault("vertex_inventory", {}).setdefault("named", {})
    for vkey, ventry in additions.items():
        if vkey.startswith("$"):
            continue
        if vkey in named:
            # Don't blindly overwrite — record both and let user resolve.
            log.append(
                f"vertex_inventory.named[{vkey}]: EXISTS in base; "
                "candidate keeps base, patch entry preserved in _patch_alt"
            )
            named.setdefault("_patch_alt", {})[vkey] = ventry
            continue
        named[vkey] = ventry
        log.append(f"vertex_inventory.named: added {vkey}")


def apply_v6_lineage(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("v6_lineage_register_additions", {})
    if not additions:
        return
    register = base.setdefault("v6_lineage_register", {}).setdefault("register", {})

    # Renumbering note → store as a top-level note field for the user.
    note = additions.get("RENUMBERING_NOTE_2026_05_13")
    if note:
        base["v6_lineage_register"]["renumbering_note_2026_05_13"] = note
        log.append("v6_lineage_register.renumbering_note_2026_05_13: stored")

    for ckey, centry in additions.items():
        if ckey.startswith("$") or ckey == "RENUMBERING_NOTE_2026_05_13":
            continue
        if ckey in register:
            # If keys collide, surface the conflict — do NOT silently overwrite.
            log.append(
                f"v6_lineage_register.{ckey}: EXISTS in base; "
                "candidate keeps base, patch entry stored in _patch_alt"
            )
            register.setdefault("_patch_alt", {})[ckey] = centry
            continue
        register[ckey] = centry
        log.append(f"v6_lineage_register: added {ckey} ({centry.get('name','?')})")


def apply_registry_entries(base: dict, patch: dict, log: list[str]) -> None:
    additions = patch.get("registry_entries_introduced", {})
    if "agent_substrate_frameworks" in additions:
        if "agent_substrate_frameworks" in base:
            log.append(
                "agent_substrate_frameworks: already present in base; "
                "patch entry stored at _patch_alt"
            )
            base.setdefault("_patch_alt", {})[
                "agent_substrate_frameworks"
            ] = additions["agent_substrate_frameworks"]
        else:
            base["agent_substrate_frameworks"] = additions["agent_substrate_frameworks"]
            log.append("agent_substrate_frameworks: added as top-level section")


def apply_city_anatomy(base: dict, patch: dict, log: list[str]) -> None:
    amendments = patch.get("city_anatomy_amendments", {})
    ca = base.setdefault("city_anatomy", {})
    # Store amendments under a structured `v1_5_0_amendments` block so the user
    # can choose how to fold them into the canonical fields (workshop_count is
    # implicit in trade_quarters length; cast_seated_count is implicit in cast
    # array length; etc.).
    ca["v1_5_0_amendments"] = {
        k: v for k, v in amendments.items() if not k.startswith("$")
    }
    log.append(
        "city_anatomy.v1_5_0_amendments: stored amendments block "
        "(workshop_count · cast_seated_count · structural_entity_classes · "
        "tome_count · cast_tiers · swordsman_stances · chain_mana_count) — "
        "user authoring pass folds into canonical fields"
    )


def apply_ipfs_pin_status(base: dict, patch: dict, log: list[str]) -> None:
    amendments = patch.get("ipfs_pin_status_amendments", {})
    addition_text = amendments.get("addition_text", "")
    pin_note = amendments.get("pin_status_note", "")
    if addition_text:
        base["ipfs_pin_status"] = (
            base.get("ipfs_pin_status", "") + " · " + addition_text
        )
        log.append("ipfs_pin_status: appended v1.5.0 addition_text")
    if pin_note:
        base["ipfs_pin_status_v1_5_0_note"] = pin_note
        log.append("ipfs_pin_status_v1_5_0_note: stored merge-pin note")


def apply_version_notes(base: dict, patch: dict, log: list[str]) -> None:
    addition = patch.get("version_notes_addition", {})
    vn = base.setdefault("version_notes", {})
    for key, val in addition.items():
        if key.startswith("$"):
            continue
        canonical_key = key.replace("_", ".") if key.startswith("v") and "_" in key else key
        # The base uses "v1.4.0" style keys with dots; patch uses "v1_5_0" with underscores.
        canonical_key = canonical_key if "." in canonical_key else canonical_key.replace("v1", "v1.")
        if canonical_key in vn:
            log.append(f"version_notes: SKIP existing {canonical_key!r}")
            continue
        # Wrap into a {date, changes} shape if the base uses that shape.
        sample = next(iter(vn.values())) if vn else None
        if isinstance(sample, dict) and "date" in sample and "changes" in sample:
            vn[canonical_key] = {
                "date": "2026-05-13",
                "changes": [val] if isinstance(val, str) else val,
            }
        else:
            vn[canonical_key] = val
        log.append(f"version_notes[{canonical_key!r}]: added v1.5.0 entry")


def main() -> int:
    if not BASE_PATH.exists():
        print(f"ERROR: base not found at {BASE_PATH}", file=sys.stderr)
        return 1
    if not PATCH_PATH.exists():
        print(f"ERROR: patch not found at {PATCH_PATH}", file=sys.stderr)
        return 1

    base = load_json(BASE_PATH)
    patch = load_json(PATCH_PATH)
    log: list[str] = []

    apply_top_level_replacements(base, patch, log)
    apply_cast_attachment_additions(base, patch, log)
    apply_persona_additions(base, patch, log)
    apply_spell_additions(base, patch, log)
    apply_tome_additions(base, patch, log)
    apply_vertex_inventory(base, patch, log)
    apply_v6_lineage(base, patch, log)
    apply_registry_entries(base, patch, log)
    apply_city_anatomy(base, patch, log)
    apply_ipfs_pin_status(base, patch, log)
    apply_version_notes(base, patch, log)

    # Prepend candidate-status flag at the top of the JSON object.
    candidate_note = {
        "$candidate_note": (
            "DRAFT CANDIDATE — NOT canonical. Mechanically merged from "
            "city_of_mages_grimoire_v1_4_0.json + city_of_mages_grimoire_v1_5_0_patch.json "
            "by grimoire/scripts/merge_v1_5_0_patch.py at "
            f"{datetime.now(timezone.utc).isoformat()}. Review every section before "
            "promoting to canonical v1.5.0 and re-pinning to IPFS. Conflicts surfaced "
            "into '_patch_alt' subfields where applicable. See merge log printed by "
            "the script for the full action list."
        ),
        "$candidate_status": "pending-user-review",
        "$canonical_base": "city_of_mages_grimoire_v1_4_0.json (CID bafkreib5w4bp6t5kkt4ebvjyjjzuxdupzaz6gtupbhgbrxtwkrxj7dfnsu)",
        "$patch_source": "city_of_mages_grimoire_v1_5_0_patch.json",
    }
    # Re-emit base with candidate_note keys first for visibility.
    out = {**candidate_note, **base}
    save_json(OUT_PATH, out)

    # Write the action log to a sidecar file (avoids cp1252 stdout crashes on Windows).
    log_path = OUT_PATH.with_suffix(".merge.log")
    with log_path.open("w", encoding="utf-8") as f:
        f.write(f"merge complete: {OUT_PATH}\n")
        f.write(f"timestamp: {datetime.now(timezone.utc).isoformat()}\n")
        f.write(f"actions: {len(log)}\n\n")
        for line in log:
            f.write(line + "\n")
    # Safe stdout summary — strip emoji/arrows.
    safe = lambda s: s.encode("ascii", "replace").decode("ascii")
    print(f"merge complete -> {safe(str(OUT_PATH))}")
    print(f"action log    -> {safe(str(log_path))}")
    print(f"total actions: {len(log)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
