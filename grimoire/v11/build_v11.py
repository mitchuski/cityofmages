"""build_v11.py - generate the agentprivacy universe grimoire v11 from its sources.

authored.json  the keeper's words (edition, ages, errata, open items). Errata quotes are checked verbatim.
Everything else is read from disk: the pinned predecessors, the tomes, the master chronicles, the City's
scrolls and quests, the grimoire seal. Every generated entry carries source + source_sha256.
Fails closed on: a missing errata quote, a local path or user name in the output, a private lane named.
Writes agentprivacy_universe_grimoire_v11.0.0.json next to this file and prints its sha256 and would-be CID.
"""
from __future__ import annotations
import hashlib, json, os, re, sys

HOME = os.path.expanduser("~")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HOME, "kappa_evidence_mage"))
from ipfs_cid import build as cid_build  # noqa: E402

VERSION = "11.0.0"
BUILT = "2026-11-17"
PRIVATE_LANES = ["embryo"]  # privately shared work: counted, never named
PIN_DIR = "kappa_evidence_mage/input/grimoire_v2/pinned"
PRIV_LAST = "bafybeicvbong6ejbvtnfcgbfdtely75e3cakauthv3u22r3nh6ljxqstsm"
CITY_LAST = "bafybeietwhafmxolgyhzjpucbrr6tmm3zokk5vi2knzu5obluz626fkthy"


def p(rel): return os.path.join(HOME, rel)
def raw(rel): return open(p(rel), "rb").read()
def text(rel): return raw(rel).decode("utf-8")
def sha(rel): return hashlib.sha256(raw(rel)).hexdigest()
def src(rel): return {"source": rel, "source_sha256": sha(rel)}


def lineage():
    out = {"privacymage": [], "city-of-mages": []}
    for f in sorted(os.listdir(p(PIN_DIR))):
        rel = f"{PIN_DIR}/{f}"; d = json.loads(text(rel))
        v = str(d["version"]); line = "privacymage" if int(v.split(".")[0]) >= 8 else "city-of-mages"
        out[line].append({"version": v, "cid": f[:-5], "updated_at": str(d.get("updated_at", "")), "bytes": len(raw(rel))})
    for k in out: out[k].sort(key=lambda e: tuple(int(x) for x in e["version"].split(".")))
    root = json.loads(text("kappa_evidence_mage/out/grimoire_v2/root.json"))
    return {"description": "Every published version of both earlier grimoires, by CID. Each CID was re-derived from its bytes (UnixFS CIDv1, sha2-256) and the set is sealed as one κ bundle.",
            "succeeds": {"privacymage": {"version": "10.4.0", "cid": PRIV_LAST}, "city-of-mages": {"version": "1.9.3", "cid": CITY_LAST}},
            "pins": out, "seal": {"root_kappa": root["root_kappa"], "minted_on": root.get("minted_on", ""),
                                 "scroll": "https://grimoire.mages.city/", **src("kappa_evidence_mage/out/grimoire_v2/root.json")}}


def lore_by_reference():
    pm = json.loads(text(f"{PIN_DIR}/{PRIV_LAST}.json")); cm = json.loads(text(f"{PIN_DIR}/{CITY_LAST}.json"))
    books = {k: (len(v) if isinstance(v, (list, dict)) else None) for k, v in pm["spellbooks"].items()}
    tiers = {k: len(v) for k, v in cm["personas"].items() if isinstance(v, (list, dict))}
    return {"description": "The lore of the first two ages, read in place. Paths are JSON pointers into the pinned file.",
            "privacymage": {"cid": PRIV_LAST, "spellbooks": {k: {"path": f"/spellbooks/{k}", "top_level_entries": n} for k, n in books.items()},
                            "inscriptions": {k: pm["status"][k] for k in ("story_acts_total", "zero_tales_total", "canon_chapters_total", "parallel_chapters_total", "plurality_acts_total", "total_inscriptions")},
                            "also": ["/unified_incantations", "/notation", "/principles", "/forged_blades", "/personas", "/ceremonies"]},
            "city-of-mages": {"cid": CITY_LAST, "personas": {k: {"path": f"/personas/{k}", "entries": n} for k, n in tiers.items()},
                              "also": ["/spells", "/vertex_inventory", "/city_anatomy", "/workshop_districts", "/fleet_workshops", "/register_of_invitations", "/tower_spatial_anatomy", "/hearth_spatial_anatomy", "/wellpool_spatial_anatomy", "/known_open_items"]}}


def h1(body):
    m = re.search(r"^#\s+(.+)$", body, re.M); return m.group(1).strip() if m else ""


def frontmatter(body):
    m = re.match(r"^---\n(.*?)\n---", body, re.S); fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1); fm[k.strip()] = v.strip().strip('"')
    return fm


def tomes():
    base = "cityofmages/tomes"; out = []
    mrel = f"{base}/BOUND_COLLECTION_MANIFEST.md"; manifest = text(mrel).replace("\r\n", "\n").splitlines()
    dirs = sorted(d for d in os.listdir(p(base)) if d.startswith("tome-")) + ["proposed/tome-xi-the-constellation"]
    for d in dirs:
        acts = []
        for f in sorted(os.listdir(p(f"{base}/{d}"))):
            if not f.endswith(".md") or not f[0].isdigit(): continue
            rel = f"{base}/{d}/{f}"; body = text(rel).replace("\r\n", "\n"); fm = frontmatter(body)
            st = (fm.get("status") or "").split("(")[0].strip() or ("proposed" if d.startswith("proposed") else "states none")
            acts.append({"act": int(f.split("-")[0]), "title": fm.get("title") or h1(body).split("—")[-1].strip(" *_"), "words": len(re.findall(r"\w+", body)),
                         "act_status": st, **src(rel)})
        name = d.split("/")[-1]; numeral = name.split("-")[1].upper()
        ml = next((l for l in manifest if re.match(rf"^(## |> \*\*Note on )Tome {numeral} —", l)), None)
        out.append({"tome": name, "acts_on_disk": len(acts),
                    "manifest_entry": re.sub(r"\s+", " ", ml.lstrip("#> ").strip())[:400] if ml else "not in the bound manifest", "acts": acts})
    return {"description": "Every act on disk, by tome. act_status is the act's own frontmatter (binding is not recorded there); manifest_entry is the tome's line in the bound-collection manifest, quoted, which records binding and can lag the disk.",
            "manifest": src(mrel), "tomes": out}


SIGNED = re.compile(r"Read and signed by the First Person", re.I)


def inversion(body):
    m = re.search(r"\*\*Inversion:?\*\*:?\s*(.+)", body)
    if m: return re.sub(r"\s+", " ", m.group(1)).strip()
    m = re.search(r"^[-*]\s+\*\*The inversion:\s*(.+?)\*\*", body, re.I | re.M)
    if m: return m.group(1).strip()
    m = re.search(r"^#+[^\n]*inversion[^\n]*\n+(.+?)(\n\n|$)", body, re.I | re.M)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def chronicles():
    base = "agentprivacy_master/docs/chronicles"; out, withheld = [], 0
    for f in sorted(os.listdir(p(base))):
        if not re.match(r"2026-(0[7-9]|1[0-2])-\d\d_.+\.md$", f) or f < "2026-07-13": continue
        if any(w in f.lower() for w in PRIVATE_LANES): withheld += 1; continue
        rel = f"{base}/{f}"; body = text(rel).replace("\r\n", "\n"); signed = bool(SIGNED.search(body[-600:]))
        e = {"date": f[:10], "slug": f[11:-3], "title": re.sub(r"^\d{4}-\d\d-\d\d\s*·\s*", "", h1(body)), "signed": signed, **src(rel)}
        if signed:
            inv = inversion(body)
            if inv: e["inversion"] = inv
        out.append(e)
    return {"description": "The master chronicles of the Age of Evidence, the source of truth for every other telling. An unsigned chronicle is listed by date and title; its inversion enters on signature.",
            "count": len(out), "signed": sum(e["signed"] for e in out), "withheld_private_lanes": withheld, "entries": out}


def proverbs(chron):
    out = []
    for e in chron["entries"]:
        body = text(e["source"]).replace("\r\n", "\n")
        m = re.search(r"^##[^\n]*proverb[^\n]*\n(.*?)(?=^## |\Z)", body, re.I | re.M | re.S)
        if not m: continue
        for pv in re.findall(r"^[-*]\s+\*(.+?)\*\s*$", m.group(1), re.M):
            out.append({"proverb": pv, "chronicle": e["slug"], "date": e["date"], "status": "inscribed" if e["signed"] else "proposed", "source": e["source"]})
    return {"description": "Proverbs set down in the Age of Evidence. 'Proposed' until their chronicle is signed; the proverbs page inscribes them by hand.", "entries": out}


def seals():
    scrolls = json.loads(text("mages_city/site/scrolls.json")); chains = json.loads(text("mages_city/site/chains.json"))
    quests = [{"quest": c["id"], "domain": c.get("domain"), "lane": c.get("lane"), "entries": c.get("entries"), "minted": c.get("minted"),
               "work_root": c.get("work_root"), "poaw_root": c.get("poaw_root")} for c in chains["chains"]]
    fixed = [{"id": "soul", "label": "❦ the soul mage", "href": "https://soul.mages.city/"}, {"id": "guide", "label": "❦ the guide", "href": "https://guide.mages.city/"}]
    return {"description": "Where the mages' work is sealed. A scroll is a mage's work written as nothing but hashes; a quest is a proof-of-agentic-work chain page. Every hash resolves on sigil.mages.city.",
            "sigil": "https://sigil.mages.city/",
            "scrolls": fixed + [{"id": s["id"], "label": s["label"], "href": s["href"]} for s in scrolls],
            "quests": quests, "sources": [src("mages_city/site/scrolls.json"), src("mages_city/site/chains.json")]}


def mages(lm):
    arel = "mages_city/site/arena.json"; arena = json.loads(text(arel))
    roster = []
    for i in arena["instances"]:
        s = i.get("solve") or {}; pat = s.get("patron") or {}; sealed = i.get("sealed") or {}
        roster.append({"mage": i["id"], "arena": i.get("arena"), "work": i.get("benchmark"), "state": i.get("state"),
                       "vertex": s.get("vertex"), "axes": s.get("axes"), "witness_vertex": s.get("witness"),
                       "patron": {k: pat.get(k) for k in ("mage", "workshop", "district", "vertex")} if pat else None,
                       "word": sealed.get("kappa"), "read": sealed.get("read")})
    by = {r["mage"]: r for r in roster}
    def get(mid):
        if mid not in by: by[mid] = {"mage": mid, "state": "sealed"}; roster.append(by[mid])
        return by[mid]
    scrolls = json.loads(text("mages_city/site/scrolls.json")) + [{"id": "soul", "href": "https://soul.mages.city/"}, {"id": "guide", "href": "https://guide.mages.city/"}]
    for sc in scrolls:
        mid = lm["scrolls"].get(sc["id"])
        if mid: get(mid)["scroll"] = sc["href"]
    for c in json.loads(text("mages_city/site/chains.json"))["chains"]:
        mid = next((m for pre, m in lm["lanes"].items() if (c.get("lane") or "").startswith(pre)), None)
        if mid: get(mid).setdefault("quests", []).append(c.get("domain"))
    return {"description": "The mages of the Age of Evidence: each lane of the dual-agent harness is a mage with a Star. The City seats it on a lattice vertex and names a patron from the earlier cast, which is how the new mages join the old lore. word is the κ of the mage's sealed work, a hash and never a result.",
            "count": len(roster), "roster": roster, "sources": [src(arel), src("mages_city/site/scrolls.json")]}


def register():
    rel = "agentprivacy-docs/research/CONJECTURE_REGISTER_V6.md"; rows = []
    words = ("active", "open", "challenged", "resolved", "observation", "occupied", "alias", "reserved", "retired", "refuted", "theorem")
    for line in text(rel).splitlines():
        if not re.match(r"^\| C\d+ \|", line): continue
        f = [x.strip() for x in line.split("|")]
        status = f[-4].lower(); word = next((w for w in words if status.startswith(w)), "see register")
        title = " | ".join(f[2:-5]); short = re.split(r"[:(]", title)[0].strip()
        rows.append({"id": f[1], "name": short[:90], "confidence": f[-5], "status": word})
    rulings = [re.sub(r"^#+\s*", "", l).strip() for l in text(rel).splitlines() if l.startswith("## Ruling")]
    counts = {}
    for r in rows: counts[r["status"]] = counts.get(r["status"], 0) + 1
    return {"description": "The conjecture register as a status table: number, short name, confidence and one status word. The reasoning stays in the register. 'challenged' means a ruling or audit has put the conjecture in question as worded.",
            "count": len(rows), "by_status": counts, "rulings": rulings, "conjectures": rows, **src(rel)}


def check_quotes(items):
    for it in items:
        for side in ("earlier", "now"):
            s = it[side]; body = text(s["file"])
            if s["quote"] not in body: raise SystemExit(f"errata quote not found verbatim: {it['id']} {side} in {s['file']}")
            s["source_sha256"] = sha(s["file"])


LEAK = re.compile(r"[A-Za-z]:[\\/]+Users|/Users/|/hom[e]/|~/|\\\\|mitch(?!uski)|@soulbis|secret[:=]", re.I)


def leak_scan(obj, path="$"):
    if isinstance(obj, dict):
        for k, v in obj.items(): leak_scan(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj): leak_scan(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        if LEAK.search(obj): raise SystemExit(f"leak: {path}: {obj[:120]}")
        if any(w in obj.lower() for w in PRIVATE_LANES): raise SystemExit(f"private lane named: {path}")


def main():
    a = json.loads(open(os.path.join(HERE, "authored.json"), encoding="utf-8").read())
    check_quotes(a["errata"]); check_quotes(a["agreements"])
    chron = chronicles()
    g = {"version": VERSION, "created_at": "2026-11-17T00:00:00Z", "updated_at": BUILT, "grimoire": "agentprivacy-universe",
         "status": "draft · not pinned · awaiting the First Person's review",
         "meta": {"title": "The Agentprivacy Universe Grimoire", "edition": a["edition"], "subtitle": a["subtitle"], "tagline": a["tagline"],
                  "author": a["author"], "license": a["license"]},
         "description": a["description"], "how_to_read": a["how_to_read"], "master_invocation": a["master_invocation_pointer"],
         "ages": a["ages"], "lineage": lineage(), "lore_by_reference": lore_by_reference(), "tomes": tomes(), "chronicles": chron,
         "proverbs": proverbs(chron), "mages": mages(a["lane_mages"]), "seals": seals(), "register": register(), "errata": a["errata"], "agreements": a["agreements"],
         "open_items": a["open_items"], "closing": a["closing"],
         "build": {"generator": "cityofmages/grimoire/v11/build_v11.py", **src("cityofmages/grimoire/v11/authored.json")}}
    leak_scan(g)
    data = (json.dumps(g, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    out = os.path.join(HERE, f"agentprivacy_universe_grimoire_v{VERSION}.json"); open(out, "wb").write(data)
    print("wrote", os.path.basename(out), len(data), "bytes")
    print("sha256", hashlib.sha256(data).hexdigest()); print("cid (unixfs, 256 KiB, raw leaves)", cid_build(data, 262144, True))
    print("chronicles", chron["count"], "signed", chron["signed"], "withheld", chron["withheld_private_lanes"])
    print("tomes", sum(len(t["acts"]) for t in g["tomes"]["tomes"]), "acts;", "proverbs", len(g["proverbs"]["entries"]), ";", "quests", len(g["seals"]["quests"]))


if __name__ == "__main__":
    main()
