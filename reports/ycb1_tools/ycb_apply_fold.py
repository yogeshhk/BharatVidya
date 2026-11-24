import re, os, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
P = "D:/Yogesh/GitHub/BharatVidya/LaTeX/books/YCB1/docs/Notes YCB1.md"
F = "C:/Users/yoges/AppData/Local/Temp/claude/0aaab9165883c071/5c21a7ff-6ef5-4017-920e-9bd3c24366f0/scratchpad/fold/"
OLD = "- **Workshop slide content (merged from the current deck as the starting point; to be structured into the layers above, checked, and trimmed):**"
NEW = "- **Workshop slide content (folded into the layers above on a first pass; kept here until the author confirms nothing is lost):**"

def clean(s):
    return s.replace("\u2014", ", ").replace("\u2013", "-").replace(" -- ", ", ").replace("--", "-")

raw = open(P, encoding="utf-8", newline="").read()
eol = "\r\n" if "\r\n" in raw else "\n"
t = raw.replace("\r\n", "\n")
done = []; missing = []
for fp in sorted(glob.glob(F + "*.md")):
    slug = os.path.basename(fp)[:-3]
    bid = "ycb1-" + slug
    txt = clean(open(fp, encoding="utf-8").read())
    m = re.split(r"^\s*CONFLICTS:\s*$", txt, maxsplit=1, flags=re.M)
    mat = m[0]
    conf = ""; faq = ""
    if len(m) > 1:
        m2 = re.split(r"^\s*FAQ-QUIZ:\s*$", m[1], maxsplit=1, flags=re.M)
        conf = m2[0].strip()
        faq = m2[1].strip() if len(m2) > 1 else ""
    else:
        m3 = re.split(r"^\s*FAQ-QUIZ:\s*$", mat, maxsplit=1, flags=re.M)
        mat = m3[0]; faq = m3[1].strip() if len(m3) > 1 else ""
    mat = "\n".join(l.rstrip() for l in mat.strip("\n").split("\n") if l.strip() != "")
    if not mat.strip():
        continue
    i = t.find("- **ID:** " + bid)
    if i < 0:
        missing.append(slug); continue
    j = t.find("\n- **ID:**", i + 5); j = len(t) if j == -1 else j
    b = t[i:j]
    if "(deck, not yet checked)" in b and "folded into the layers above" in b:
        continue
    # insert material before Explanation
    k = b.find("- **Explanation:**")
    if k < 0: k = b.index("- **Worked examples:**")
    b = b[:k] + mat + "\n" + b[k:]
    # conflicts layer before Worked examples
    if conf:
        lines = [("  - " + l.lstrip("-* ").strip()) for l in conf.split("\n") if l.strip()]
        k = b.index("- **Worked examples:**")
        b = b[:k] + "- **Open conflicts (deck versus notes; to be checked before the deck is rebuilt):**\n" + "\n".join(lines) + "\n" + b[k:]
    # quiz additions
    if faq:
        qs = []
        for l in faq.split("\n"):
            l = l.strip().lstrip("-* ").strip()
            if l.startswith("Q:"):
                qs.append("  - " + l)
        if qs:
            mq = re.search(r"- \*\*Quiz:\*\*[^\n]*\n((?:  [^\n]*\n)*)", b)
            if mq:
                b = b[:mq.end()] + "\n".join(qs) + "\n" + b[mq.end():]
    b = b.replace(OLD, NEW)
    t = t[:i] + b + t[j:]
    done.append(slug)
open(P, "w", encoding="utf-8", newline="").write(t.replace("\n", eol))
print("applied", len(done), "missing", missing)
