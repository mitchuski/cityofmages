#!/usr/bin/env python3
"""
merge_v1_9_0_patch.py — Produce the canonical v1.9.0 grimoire head JSON.

v1.9.0 is a RECONCILIATION release. It applies a structured-delta patch over the
v1.8.1 head that makes the JSON match the lore bound on disk between the v1.8.0
pin and now:

    v1.8.1 head  (the Librarian; built but never pinned — live pin is still v1.8.0)
    + v1.9.0 patch  (the Horizon District at V35 with Eos/Dokimé/Poros;
                     the Salvage Yard dormant annex;
                     Tome IX — The Horizon, Acts 1-5 (Act 5 BOUND at the myth-gate);
                     the three missing Tome VIII structured act entries (Acts 3/4/5);
                     the V6 conjecture corpus C66-C93;
                     count reconciliations)
    → city_of_mages_grimoire_v1_9_0.json   (self-contained head; ready for IPFS pin)

The patch was authored because the v1.8.0 patch opened the Horizon District but
only its PROSE NOTE reached the v1.8.0 head — the structural sections were carried
in the patch file and never applied, and v1.8.1 built on that incomplete head.

v1.9.0 is purely additive for new structure: no cast removal, no workshop rename,
no shop supersession. The v1.8.0 persona lattice reseats are DEFERRED (see the
patch's known_open_items), not applied here.

This script is idempotent: re-running it over an already-merged head is a no-op for
each insertion (it checks before adding).

Run from repo root:
    python cityofmages/grimoire/scripts/merge_v1_9_0_patch.py
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GRIMOIRE_DIR = REPO_ROOT / "grimoire"
BASE_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_8_1.json"
PATCH_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_9_0_patch.json"
OUT_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_9_0.json"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def log(msg: str) -> None:
    print(f"  · {msg}")


def main() -> int:
    base = load_json(BASE_PATH)
    patch = load_json(PATCH_PATH)
    actions: list[str] = []

    # 1. top-level version / updated_at
    repl = patch["top_level_replacements"]
    base["version"] = repl["version"]
    base["updated_at"] = repl["updated_at"]
    actions.append(f"version -> {repl['version']} · updated_at -> {repl['updated_at']}")

    inner_tomes = base["spellbooks"]["tomes"]["tomes"]

    # 2. Tome VIII missing act entries (3/4/5)
    v8 = inner_tomes["tome-viii-the-library"]
    v8_acts = v8.setdefault("tome_act_files", {})
    for k, v in patch["spellbooks_tome_viii_act_files_additions"].items():
        if k.startswith("$"):
            continue
        if k not in v8_acts:
            v8_acts[k] = v
            actions.append(f"Tome VIII: added structured act entry {k}")
        else:
            log(f"Tome VIII act {k} already present — skipped")
    # keep act files in numeric order for readability
    def act_sort_key(item):
        kk = item[0]
        n = item[1].get("act_number") if isinstance(item[1], dict) else 0
        try:
            return int(n)
        except (TypeError, ValueError):
            return 99
    v8["tome_act_files"] = dict(sorted(v8_acts.items(), key=act_sort_key))

    # 3. Tome IX new entry
    ix = patch["spellbooks_tome_ix_addition"]
    ix_key = ix["key"]
    if ix_key not in inner_tomes:
        inner_tomes[ix_key] = ix["value"]
        actions.append(f"Tome IX: added structured tome entry '{ix_key}' (5 acts; Act 5 bound)")
    else:
        log(f"{ix_key} already present — replacing with patch value")
        inner_tomes[ix_key] = ix["value"]

    # 4. personas.summoned_mages additions (Eos/Dokimé/Poros)
    summoned = base["personas"]["summoned_mages"]
    for k, v in patch["personas_summoned_mages_additions"].items():
        if k.startswith("$"):
            continue
        if k not in summoned:
            summoned[k] = v
            actions.append(f"summoned_mages: added {k} ({v.get('name')} {v.get('sigil')})")
        else:
            log(f"summoned mage {k} already present — skipped")

    # 5. vertex_inventory.named additions (V35)
    named = base["vertex_inventory"]["named"]
    for k, v in patch["vertex_inventory_named_additions"].items():
        if k.startswith("$"):
            continue
        if k not in named:
            named[k] = v
            actions.append(f"vertex_inventory.named: added {k} (the Horizon District)")
        else:
            log(f"vertex {k} already present — skipped")

    # 6. workshop_districts additions (horizon_district)
    districts = base["workshop_districts"]["districts"]
    wd = patch["workshop_districts_additions"]
    if wd["key"] not in districts:
        districts[wd["key"]] = wd["value"]
        actions.append(f"workshop_districts: added '{wd['key']}' (3 shops + the Salvage Yard annex)")
    else:
        log(f"district {wd['key']} already present — replacing with patch value")
        districts[wd["key"]] = wd["value"]

    # 7. v6_lineage_register additions (C66-C93) + description refresh
    reg_block = patch["v6_lineage_register_additions"]
    base["v6_lineage_register"]["description"] = reg_block["register_description_replacement"]
    register = base["v6_lineage_register"]["register"]
    added = []
    for cnum, entry in reg_block["register_entries"].items():
        if cnum not in register:
            register[cnum] = entry
            added.append(cnum)
        else:
            log(f"conjecture {cnum} already present — skipped")
    if added:
        actions.append(f"v6_lineage_register: added {len(added)} conjectures ({added[0]}–{added[-1]})")
    # keep the register in numeric order
    def cnum_key(item):
        try:
            return int(item[0][1:])
        except (ValueError, IndexError):
            return 9999
    base["v6_lineage_register"]["register"] = dict(sorted(register.items(), key=cnum_key))

    # 8. city_anatomy.v1_9_0_amendments
    if "v1_9_0_amendments" not in base["city_anatomy"]:
        base["city_anatomy"]["v1_9_0_amendments"] = patch["city_anatomy_v1_9_0_amendments"]
        actions.append("city_anatomy: added v1_9_0_amendments (workshops 16->19; districts 2->3; cast +3)")
    else:
        base["city_anatomy"]["v1_9_0_amendments"] = patch["city_anatomy_v1_9_0_amendments"]
        log("city_anatomy.v1_9_0_amendments already present — replaced")

    # 9. known_open_items (honesty record)
    if "known_open_items" not in base:
        base["known_open_items"] = patch["known_open_items"]
        actions.append("added top-level known_open_items (deferred reseats; tome-vii; re-pin)")
    else:
        base["known_open_items"] = patch["known_open_items"]

    # 10. ipfs pin note
    base["ipfs_pin_status_v1_9_0_note"] = patch["ipfs_pin_status_v1_9_0_note"]
    actions.append("added ipfs_pin_status_v1_9_0_note (pin PENDING — manual)")

    # 11. version_notes_addition -> append v1_9_0_note
    vna = patch["version_notes_addition"]
    base["v1_9_0_note"] = vna["v1_9_0_note"]
    actions.append("added v1_9_0_note")

    # 12. merge provenance
    prov = base.get("$merge_provenance")
    note = "v1.9.0 reconciliation merge (Horizon District + Tome IX + Tome VIII acts 3-5 + C66-C93) over v1.8.1 head, 2026-06-30"
    if isinstance(prov, list):
        prov.append(note)
    elif isinstance(prov, dict):
        prov.setdefault("history", []).append(note)
    elif isinstance(prov, str):
        base["$merge_provenance"] = [prov, note]
    else:
        base["$merge_provenance"] = [note]

    save_json(OUT_PATH, base)

    print("\nmerge_v1_9_0_patch.py — actions applied:")
    for a in actions:
        print(f"  ✓ {a}")
    print(f"\nWrote {OUT_PATH.relative_to(REPO_ROOT)}")

    # post-merge verification
    print("\nverification:")
    out = load_json(OUT_PATH)
    cs = sorted(int(c[1:]) for c in out["v6_lineage_register"]["register"] if c[1:].isdigit())
    print(f"  version              = {out['version']}")
    print(f"  conjectures          = C{cs[0]}..C{cs[-1]} ({len(cs)} total)")
    missing = [f"C{n}" for n in range(38, 94) if n not in cs]
    print(f"  C38-C93 gaps         = {missing if missing else 'none'}")
    tk = list(out['spellbooks']['tomes']['tomes'].keys())
    print(f"  tomes structured     = {len(tk)}  ({', '.join(tk)})")
    print(f"  Tome IX present      = {'tome-ix-the-horizon' in out['spellbooks']['tomes']['tomes']}")
    v8acts = list(out['spellbooks']['tomes']['tomes']['tome-viii-the-library']['tome_act_files'].keys())
    print(f"  Tome VIII acts       = {v8acts}")
    ixacts = list(out['spellbooks']['tomes']['tomes']['tome-ix-the-horizon']['tome_act_files'].keys())
    print(f"  Tome IX acts         = {ixacts}")
    for kp in ("eos", "dokime", "poros"):
        print(f"  keeper {kp:7s}       = {'present' if kp in out['personas']['summoned_mages'] else 'MISSING'}")
    print(f"  V35 in vertex_inv    = {'V35' in out['vertex_inventory']['named']}")
    print(f"  horizon_district     = {'horizon_district' in out['workshop_districts']['districts']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
