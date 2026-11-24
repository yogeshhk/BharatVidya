import re, os, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
P = "D:/Yogesh/GitHub/BharatVidya/LaTeX/books/YCB1/docs/Notes YCB1.md"
R = "C:/Users/yoges/AppData/Local/Temp/claude/0aaab9165883c071/5c21a7ff-6ef5-4017-920e-9bd3c24366f0/scratchpad/res/"

def clean(s):
    return s.replace("\u2014", ", ").replace("\u2013", "-").replace(" -- ", ", ").replace("--", "-")

def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

def parse(txt):
    secs = {}
    cur = None
    for line in txt.split("\n"):
        m = re.match(r"^\s*(CONFIRMED|CORRECTED|REJECTED|UNVERIFIED|RESOLUTIONS|CORE|VERDICT)\s*:\s*(.*)$", line)
        if m:
            cur = m.group(1); secs[cur] = []
            if m.group(2).strip(): secs[cur].append(m.group(2).strip())
            continue
        if cur and line.strip():
            secs[cur].append(line.rstrip())
    return secs

raw = open(P, encoding="utf-8", newline="").read()
eol = "\r\n" if "\r\n" in raw else "\n"
t = raw.replace("\r\n", "\n")
stats = []
for fp in sorted(glob.glob(R + "*.md")):
    slug = os.path.basename(fp)[:-3]
    bid = "ycb1-" + slug
    secs = parse(clean(open(fp, encoding="utf-8").read()))
    i = t.find("- **ID:** " + bid)
    if i < 0: print("no block", slug); continue
    j = t.find("\n- **ID:**", i + 5); j = len(t) if j == -1 else j
    b = t[i:j]
    if "Fact check log (pass 3)" in b:
        continue
    lines = b.split("\n")
    nconf = ncorr = nrej = nunv = 0

    def find_bullet(label):
        tl = norm(label)
        for idx, l in enumerate(lines):
            m = re.match(r"^  - \*\*(.+?) \((deck, not yet checked)\):\*\*", l)
            if m and (norm(m.group(1)) == tl or tl in norm(m.group(1)) or norm(m.group(1)) in tl):
                return idx
        return None

    for item in secs.get("CONFIRMED", []):
        item = item.lstrip("-* ").strip()
        label, _, src = item.partition("|")
        idx = find_bullet(label)
        if idx is not None:
            lines[idx] = lines[idx].replace("(deck, not yet checked)", "(checked: " + src.strip().rstrip(".") + ")", 1); nconf += 1
    for item in secs.get("CORRECTED", []):
        item = item.lstrip("-* ").strip() if not item.startswith("  - **") else item
        label, _, newtxt = item.partition("|")
        idx = find_bullet(label)
        newtxt = newtxt.strip("\n")
        if idx is not None and newtxt.strip().startswith("-") or (idx is not None and "**" in newtxt):
            nt = newtxt.strip()
            if not nt.startswith("-"): nt = "- " + nt
            nt = "  " + nt if not nt.startswith("  ") else nt
            k = idx + 1
            while k < len(lines) and re.match(r"^    ", lines[k]): k += 1
            lines[idx:k] = [nt]; ncorr += 1
    for item in secs.get("REJECTED", []):
        item = item.lstrip("-* ").strip()
        label, _, why = item.partition("|")
        idx = find_bullet(label)
        if idx is not None:
            lines[idx] = lines[idx].replace("(deck, not yet checked)", "(deck, rejected: " + why.strip().rstrip(".") + ")", 1); nrej += 1
    nunv = len([x for x in secs.get("UNVERIFIED", []) if x.strip()])
    # resolutions into conflicts layer
    res = [x.lstrip("-* ").strip() for x in secs.get("RESOLUTIONS", []) if x.strip()]
    if res:
        for idx, l in enumerate(lines):
            if l.startswith("- **Open conflicts"):
                k = idx + 1
                while k < len(lines) and lines[k].startswith("  "): k += 1
                ins = ["  - Resolution: " + r.replace("|", ":", 1) for r in res]
                lines[k:k] = ins
                break
    verdict = " ".join(secs.get("VERDICT", [])).upper()
    core_bad = len([x for x in secs.get("CORE", []) if "NOT CONFIRMED" in x.upper()])
    flip = ("ALL-CHECKED" in verdict) and nunv == 0 and core_bad == 0
    log = f"- **Fact check log (pass 3):** added points: {nconf} confirmed, {ncorr} corrected, {nrej} rejected, {nunv} unverified; hand-written points not confirmed: {core_bad}; conflicts resolved: {len(res)}."
    for idx, l in enumerate(lines):
        if l.startswith("- **Worked examples:**"):
            lines.insert(idx, log); break
    b = "\n".join(lines)
    if flip:
        b = b.replace("- **Fact check:** pending", "- **Fact check:** checked (pass 3: every point in the Material is confirmed or corrected against the sources named in its bullets and in References; a certified teacher or qualified reviewer must still review it)", 1)
    t = t[:i] + b + t[j:]
    stats.append((slug, nconf, ncorr, nrej, nunv, core_bad, len(res), "FLIP" if flip else "pending"))
open(P, "w", encoding="utf-8", newline="").write(t.replace("\n", eol))
for s in stats: print(s)
print("blocks", len(stats))
