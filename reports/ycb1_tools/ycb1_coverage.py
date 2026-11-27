"""YCB1 coverage check: notes block -> deck frames -> book chapter -> figures. Read-only.
Run: python -I reports/ycb1_tools/ycb1_coverage.py   (writes reports/ycb1_tools/ycb1_coverage_report.md)
Local tool, not for the public release. ASCII output only.
"""
import re, csv, os, glob, io

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.normpath(os.path.join(HERE, "..", "..", "LaTeX", "books", "YCB1")) + os.sep
OUT = os.path.join(HERE, "ycb1_coverage_report.md")

# book chapter file -> notes block ID fragments it is meant to carry (the only hand-kept map)
BOOK_MAP = {
    "ycb1_book_guiding-principles.tex": ["guiding-principles"],
    "ycb1_book_texts.tex": ["yoga-sutra", "bhagavad-gita", "prasthanatrayi", "hatha-practices", "mental-wellbeing", "bahiranga"],
    "ycb1_book_first-aid-cpr.tex": ["first-aid"],
    "ycb1_book_teaching-class.tex": ["preparation-for-a", "factors-influencing", "class-prep"],
    "ycb1_book_field-experience.tex": ["field-experience"],
    "ycb1_book_exam.tex": ["exam"],
    "ycb1_book_meaning-history.tex": ["etymology", "origin-history"],
    "ycb1_book_principles-schools.tex": ["principles-of-yoga", "major-schools"],
    "ycb1_book_practices-intro.tex": ["practices-for-health", "shatkarma-introduction", "vyayama-surya-namaskara-introduction", "yogasana-introduction", "pranayama-dhyana-introduction"],
    "ycb1_book_hatha-diet-living.tex": ["hatha-pradipika", "aahara-diet", "healthy-living-gita", "subjective-experience"],
    "ycb1_book_human-body.tex": ["human-body"],
    "ycb1_book_health-promotion.tex": ["health-promotion", "holistic-approach", "positive-attitudes", "bhavas", "personality-development"],
    "ycb1_book_lifestyle-stress.tex": ["dinacharya", "stress-management", "metabolic-respiratory"],
    "ycb1_book_prayer.tex": ["prayer"],
    "ycb1_book_cleansing.tex": ["cleansing-techniques"],
    "ycb1_book_vyayama.tex": ["sukshma-vyayama", "sthula-vyayama"],
    "ycb1_book_surya-namaskara.tex": ["pd-surya-namaskara"],
    "ycb1_book_asanas.tex": ["yogasana-practice"],
    "ycb1_book_breathing-pranayama.tex": ["preparatory-breathing", "pd-pranayama"],
    "ycb1_book_bandha-mudra.tex": ["pd-bandha", "pd-mudra"],
    "ycb1_book_meditation.tex": ["meditation-practices"],
    "ycb1_book_lessons.tex": ["lesson-plan", "teaching-groups", "class-management", "conducting-lessons", "ideal-instructor", "model-lesson-plans"],
    "ycb1_book_application.tex": ["application-of-knowledge"],
}

norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
words = lambda ls: sum(len(re.findall(r"\w+", l)) for l in ls)

def read(p):
    return io.open(p, encoding="utf-8").read()

# ---- notes blocks
blocks, cur, unit = [], None, ""
for ln in read(R + "docs/Notes YCB1.md").split("\n"):
    if ln.startswith("## "):
        unit = ln[3:].strip(); cur = None
    elif ln.startswith("### "):
        cur = {"title": ln[4:].strip(), "unit": unit, "lines": []}; blocks.append(cur)
    elif cur is not None:
        cur["lines"].append(ln)

def layers(lines):
    out, name = {}, None
    for ln in lines:
        if ln.startswith("- **"):
            m = re.match(r"- \*\*(.+?)\*\*", ln)
            name = (m.group(1).rstrip(":").split(" (")[0].strip()) if m else "?"
            out[name] = [ln]
        elif name:
            out[name].append(ln)
    return out

for b in blocks:
    L = layers(b["lines"]); b["L"] = L
    idl = next((l for l in b["lines"] if l.startswith("- **ID:**")), "")
    b["id"] = idl.split("**ID:**")[1].strip() if idl else ""
    fc = next((l for l in b["lines"] if l.startswith("- **Fact check:**")), "")
    b["status"] = "checked" if fc.split("**Fact check:**")[-1].strip().startswith("checked") else "pending"
    b["text"] = "\n".join(b["lines"])
    b["deck_titles"] = [re.sub(r"\*", "", re.match(r"  - \*\*(.+?)\*\*", l).group(1)) for l in L.get("Workshop slide content", []) if re.match(r"  - \*\*", l)]
    b["figids"] = set(re.findall(r"\*\*(ycb1-fig-[a-z0-9-]+)\*\*", "\n".join(L.get("Figures", []))))

# ---- deck frames
deck = []
for f in sorted(glob.glob(R + "workshop/ycb1_*.tex")):
    t = "\n".join(l for l in read(f).split("\n") if not l.lstrip().startswith("%"))
    # titles may hold nested braces (\textit{...}), so read each one to its matching brace
    for m in re.finditer(r"\\begin\{frame\}(?:\[[^\]]*\])?\{|\\frametitle\{", t):
        depth, j = 1, m.end()
        while j < len(t) and depth:
            depth += {"{": 1, "}": -1}.get(t[j], 0)
            j += 1
        deck.append((os.path.basename(f), t[m.end():j - 1]))
deck_norm = lambda x: norm(re.sub(r"\\[a-zA-Z]+", "", x))
allnotes = norm("\n".join(b["text"] for b in blocks))
deck_not_in_notes = [(f, x) for f, x in deck if deck_norm(x) and deck_norm(x) not in allnotes and not re.match(r"Question \d+", x)]
faq_generic = [x for f, x in deck if re.match(r"Question \d+", x)]
block_titles = {b["id"]: {norm(t) for t in b["deck_titles"]} for b in blocks}
deck_norms = {deck_norm(x) for f, x in deck}
notes_frames_not_in_deck = [(b["title"], t) for b in blocks for t in b["deck_titles"] if norm(t) not in deck_norms]

# ---- register
reg = list(csv.DictReader(io.open(R + "docs/image_register.csv", encoding="utf-8")))
fig_missing_in_notes = [r["figure_id"] for r in reg if not any(r["figure_id"] in b["figids"] for b in blocks)]
fig_wrong_block = [(r["figure_id"], r["block_id"]) for r in reg if any(r["figure_id"] in b["figids"] for b in blocks)
                   and not any(r["figure_id"] in b["figids"] and b["id"] == r["block_id"] for b in blocks)]
book_text_all = {}
for f in glob.glob(R + "book/ycb1_book_*.tex"):
    t = read(f)
    book_text_all[os.path.basename(f)] = t
book_fig_ids = set(re.findall(r"\\ycbfig\{(ycb1-fig-[a-z0-9-]+)\}", "\n".join(v for k, v in book_text_all.items() if k != "ycb1_book_figures.tex")))
# retired figures (retyped as a table, or dropped) are not expected in the book
fig_missing_in_book = [r["figure_id"] for r in reg if r["figure_id"] not in book_fig_ids
                       and r["status"] not in ("retyped_table", "dropped")]

# ---- book coverage per block
def terms(text):
    return {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z-]{5,}", text)}
def book_for(bid):
    for f, frags in BOOK_MAP.items():
        if any(fr in bid for fr in frags) and f in book_text_all:
            return f
    return None

rows = []
for b in blocks:
    mat = "\n".join(b["L"].get("Material", []) + b["L"].get("Explanation", []))
    f = book_for(b["id"])
    cov = ""
    if f:
        bt = re.sub(r"\\[a-zA-Z]+", " ", re.sub(r"%.*", "", book_text_all[f]))
        mt = terms(mat)
        cov = "%d%%" % (100 * len(mt & terms(bt)) / max(1, len(mt)))
    qa = words(b["L"].get("Exercises", []) + b["L"].get("Quiz", []) + b["L"].get("FAQ", []))
    nfig = sum(1 for r in reg if r["block_id"] == b["id"])
    rows.append((b["unit"], b["title"], b["status"], words(b["L"].get("Material", [])), len(b["deck_titles"]), f or "-", cov or "-", qa, nfig, len(b["figids"])))

# ---- report
o = []
o.append("# YCB1 coverage report\n")
o.append("Generated by `ycb1_coverage.py`. Notes block -> deck frames -> book chapter -> figures. Local, not for the public release.\n")
o.append("## Totals\n")
o.append("- Notes blocks: %d (checked %d, pending %d)" % (len(blocks), sum(b["status"] == "checked" for b in blocks), sum(b["status"] == "pending" for b in blocks)))
o.append("- Blocks with book text: %d; without: %d" % (sum(1 for r in rows if r[5] != "-"), sum(1 for r in rows if r[5] == "-")))
o.append("- Deck frames (live): %d (generic FAQ question frames %d)" % (len(deck), len(faq_generic)))
o.append("- Deck frames whose title is not in the notes: %d" % len(deck_not_in_notes))
o.append("- Notes deck-layer frames whose title is no longer in the deck: %d" % len(notes_frames_not_in_deck))
o.append("- Register figures: %d; missing from the notes Figures lists: %d; filed under a different block in the notes: %d; not yet in the book: %d\n" % (len(reg), len(fig_missing_in_notes), len(fig_wrong_block), len(fig_missing_in_book)))
o.append("## Per block\n")
o.append("Book term cover = share of the block's distinctive Material and Explanation words that appear in the mapped book chapter (a coarse measure; low means the chapter is thinner than the notes).\n")
o.append("| Unit | Block | Fact check | Material words | Deck frames in notes | Book chapter | Book term cover | Quiz/FAQ words | Register figs | Notes figs |")
o.append("|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    o.append("| %s | %s | %s | %d | %d | %s | %s | %d | %d | %d |" % (r[0][:24], r[1][:55], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))
o.append("\n## Gaps: deck frame not in the notes\n")
for f, x in deck_not_in_notes: o.append("- `%s`: %s" % (f, x))
o.append("\n## Gaps: notes deck-layer frame no longer in the deck (renamed or removed)\n")
for t, x in notes_frames_not_in_deck: o.append("- %s: %s" % (t[:50], x))
o.append("\n## Gaps: register figures missing from the notes Figures lists\n")
for x in fig_missing_in_notes: o.append("- " + x)
o.append("\n## Gaps: register figures not in the book\n")
o.append("%d figures (all of them unless a chapter file names the ID)." % len(fig_missing_in_book))
io.open(OUT, "w", encoding="utf-8").write("\n".join(o) + "\n")
print("wrote", OUT)
print("\n".join(o[2:9]))
