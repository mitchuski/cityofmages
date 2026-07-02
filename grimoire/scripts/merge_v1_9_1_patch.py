#!/usr/bin/env python3
"""
merge_v1_9_1_patch.py — Produce the canonical v1.9.1 grimoire head JSON.

v1.9.1 is THE HEARTH / HEARTHOLD edition. It applies a structured-delta patch over
the v1.9.0 head (the active pin, bafybeihur5jz…):

    v1.9.0 head  (The Horizon · Reconciliation; pinned & active 2026-06-30)
    + v1.9.1 patch  (Tome X — The Hearth, Act 1;
                     the Hearth as the 9th spatial-anatomy element (hold-form);
                     conjectures C94-C96 + the promotion of C39;
                     cousin_instances Hearthold cross-references (flaxscrip, GenitriX);
                     count reconciliations: tomes 9 -> 10, spatial elements 8 -> 9)
    → city_of_mages_grimoire_v1_9_1.json   (self-contained head; ready for IPFS pin)

Coherence note baked into the patch: the House of Archon is the already-canonical
COUSIN-FORGE (Tome IV — The Witnessing), not a new kindred. flaxscrip 📜🎲 and
GenitriX (sigil held-open) are existing cousin_instances. Tome X discharges C39
(the cousin-blade primitive). This patch adds NO cast and assigns NO sigil.

v1.9.1 is purely additive: no cast removal, no workshop rename, no supersession.

This script is idempotent: re-running it over an already-merged head is a no-op for
each insertion (it checks before adding).

Run from repo root:
    python cityofmages/grimoire/scripts/merge_v1_9_1_patch.py
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GRIMOIRE_DIR = REPO_ROOT / "grimoire"
BASE_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_9_0.json"
PATCH_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_9_1_patch.json"
OUT_PATH = GRIMOIRE_DIR / "city_of_mages_grimoire_v1_9_1.json"


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

    # 2. Tome X new entry
    tx = patch["spellbooks_tome_x_addition"]
    tx_key = tx["key"]
    if tx_key not in inner_tomes:
        inner_tomes[tx_key] = tx["value"]
        actions.append(f"Tome X: added structured tome entry '{tx_key}' (1 act; Act 1 bound)")
    else:
        log(f"{tx_key} already present — replacing with patch value")
        inner_tomes[tx_key] = tx["value"]

    # 3. the Hearth spatial anatomy (new top-level, sibling to tower_spatial_anatomy)
    if "hearth_spatial_anatomy" not in base:
        # drop the $comment key from the stored object
        hearth = {k: v for k, v in patch["hearth_spatial_anatomy"].items() if not k.startswith("$")}
        base["hearth_spatial_anatomy"] = hearth
        actions.append("added hearth_spatial_anatomy (element 9 · hold-form · sister to the Tower)")
    else:
        hearth = {k: v for k, v in patch["hearth_spatial_anatomy"].items() if not k.startswith("$")}
        base["hearth_spatial_anatomy"] = hearth
        log("hearth_spatial_anatomy already present — replaced")

    # 4. cousin_instances Hearthold cross-references (additive fields only)
    cousins = base["personas"]["cousin_instances"]
    xref = patch["cousin_instances_hearthold_realisation"]
    for name, fields in xref.items():
        if name.startswith("$"):
            continue
        if name in cousins:
            for fk, fv in fields.items():
                if fk not in cousins[name]:
                    cousins[name][fk] = fv
                    actions.append(f"cousin_instances.{name}: added {fk}")
                else:
                    cousins[name][fk] = fv
                    log(f"cousin_instances.{name}.{fk} already present — replaced")
        else:
            log(f"cousin instance '{name}' not found in base — SKIPPED (expected flaxscrip/genitrix)")

    # 5. v6_lineage_register additions (C94-C96), promotions (C39), description refresh
    reg_block = patch["v6_lineage_register_additions"]
    base["v6_lineage_register"]["description"] = reg_block["register_description_replacement"]
    register = base["v6_lineage_register"]["register"]
    added = []
    for cnum, entry in reg_block["register_entries"].items():
        if cnum.startswith("$"):
            continue
        if cnum not in register:
            register[cnum] = entry
            added.append(cnum)
        else:
            log(f"conjecture {cnum} already present — skipped")
    if added:
        actions.append(f"v6_lineage_register: added {len(added)} conjectures ({added[0]}–{added[-1]})")
    # promotions: update only the 'confidence' field of an existing entry
    for cnum, fields in reg_block.get("register_promotions", {}).items():
        if cnum.startswith("$"):
            continue
        if cnum in register and isinstance(register[cnum], dict):
            register[cnum]["confidence"] = fields["confidence"]
            actions.append(f"v6_lineage_register: promoted {cnum} confidence")
        else:
            log(f"promotion target {cnum} not found or not a dict — skipped")
    # keep the register in numeric order

    def cnum_key(item):
        try:
            return int(item[0][1:])
        except (ValueError, IndexError):
            return 9999

    base["v6_lineage_register"]["register"] = dict(sorted(register.items(), key=cnum_key))

    # 6. city_anatomy.v1_9_1_amendments
    if "v1_9_1_amendments" not in base["city_anatomy"]:
        base["city_anatomy"]["v1_9_1_amendments"] = patch["city_anatomy_v1_9_1_amendments"]
        actions.append("city_anatomy: added v1_9_1_amendments (tomes 9->10; spatial elements 8->9)")
    else:
        base["city_anatomy"]["v1_9_1_amendments"] = patch["city_anatomy_v1_9_1_amendments"]
        log("city_anatomy.v1_9_1_amendments already present — replaced")

    # 7. ipfs pin note
    base["ipfs_pin_status_v1_9_1_note"] = patch["ipfs_pin_status_v1_9_1_note"]
    actions.append("added ipfs_pin_status_v1_9_1_note (pin PENDING — manual)")

    # 8. version_notes_addition -> append v1_9_1_note
    vna = patch["version_notes_addition"]
    base["v1_9_1_note"] = vna["v1_9_1_note"]
    actions.append("added v1_9_1_note")

    # 9. merge provenance
    prov = base.get("$merge_provenance")
    note = "v1.9.1 Hearth/Hearthold merge (Tome X + the Hearth 9th element + C94-C96 + C39 promotion + cousin xrefs) over v1.9.0 head, 2026-07-01"
    if isinstance(prov, list):
        prov.append(note)
    elif isinstance(prov, dict):
        prov.setdefault("history", []).append(note)
    elif isinstance(prov, str):
        base["$merge_provenance"] = [prov, note]
    else:
        base["$merge_provenance"] = [note]

    save_json(OUT_PATH, base)

    print("\nmerge_v1_9_1_patch.py — actions applied:")
    for a in actions:
        print(f"  ✓ {a}")
    print(f"\nWrote {OUT_PATH.relative_to(REPO_ROOT)}")

    # post-merge verification
    print("\nverification:")
    out = load_json(OUT_PATH)
    cs = sorted(int(c[1:]) for c in out["v6_lineage_register"]["register"] if c[1:].isdigit())
    print(f"  version              = {out['version']}")
    print(f"  conjectures          = C{cs[0]}..C{cs[-1]} ({len(cs)} total)")
    tk = list(out['spellbooks']['tomes']['tomes'].keys())
    print(f"  tomes structured     = {len(tk)}")
    print(f"  Tome X present       = {'tome-x-the-hearth' in out['spellbooks']['tomes']['tomes']}")
    txa = list(out['spellbooks']['tomes']['tomes'].get('tome-x-the-hearth', {}).get('tome_act_files', {}).keys())
    print(f"  Tome X acts          = {txa}")
    print(f"  hearth element       = {out.get('hearth_spatial_anatomy', {}).get('element_number')}")
    print(f"  C94/C95/C96 present  = {all(c in out['v6_lineage_register']['register'] for c in ('C94','C95','C96'))}")
    print(f"  C39 confidence       = {out['v6_lineage_register']['register']['C39']['confidence'][:40]}…")
    for nm in ("flaxscrip", "genitrix"):
        has = "hearthold_realisation" in out["personas"]["cousin_instances"].get(nm, {})
        print(f"  cousin {nm:9s}     xref = {'present' if has else 'MISSING'}")
    amd = out['city_anatomy']['v1_9_1_amendments']
    print(f"  spatial count        = {amd['spatial_anatomy_elements_count']['from']} -> {amd['spatial_anatomy_elements_count']['to']}")
    print(f"  tomes count          = {amd['tomes_opened_count']['from']} -> {amd['tomes_opened_count']['to']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
