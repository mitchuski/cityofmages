"""sign_pass.py - list the unsigned master chronicles of the Age of Evidence with their inversions, for the
First Person to read and sign in batches. Local reading aid only: it is never published (it names private lanes).
Writes sign_pass.md beside this file. A chronicle leaves this list when its footer reads
'Read and signed by the First Person, <date>.'; the next build_v11.py run then carries its inversion.
"""
import os, re
import build_v11 as b

base = "agentprivacy_master/docs/chronicles"
rows = []
for f in sorted(os.listdir(b.p(base))):
    if not re.match(r"2026-(0[7-9]|1[0-2])-\d\d_.+\.md$", f) or f < "2026-07-13": continue
    rel = f"{base}/{f}"; body = b.text(rel).replace("\r\n", "\n")
    if b.SIGNED.search(body[-600:]): continue
    private = any(w in f.lower() for w in b.PRIVATE_LANES)
    rows.append((f[:10], re.sub(r"^\d{4}-\d\d-\d\d\s*·\s*", "", b.h1(body)), rel, b.inversion(body), private))

out = ["# Sign pass: unsigned chronicles of the Age of Evidence", "",
       f"{len(rows)} master chronicles wait for the First Person's read. To sign one, replace its closing line with",
       "`*Read and signed by the First Person, <date>.*` and re-run `python build_v11.py`; its inversion then enters v11.",
       "Private-lane chronicles are marked 🔒: they can be signed, but v11 still counts them without naming them.", ""]
month = None
for date, title, rel, inv, private in rows:
    if date[:7] != month:
        month = date[:7]; out += ["", f"## {month}", ""]
    out.append(f"- [ ] **{date} · {title}**{' 🔒' if private else ''}  ")
    out.append(f"  `{rel}`  ")
    out.append(f"  {('*Inversion:* ' + inv) if inv else '*No inversion line found; the chronicle names none in a form the build reads.*'}")
open(os.path.join(b.HERE, "sign_pass.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("unsigned", len(rows), "with inversion", sum(1 for r in rows if r[3]), "private", sum(1 for r in rows if r[4]))
