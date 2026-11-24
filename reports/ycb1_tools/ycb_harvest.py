import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ycb_parse as p
sys.stdout.reconfigure(encoding="utf-8")
P = "D:/Yogesh/GitHub/BharatVidya/LaTeX/books/YCB1/docs/Notes YCB1.md"

TH = ["th-etymology-definitions-aim", "th-origin-history-development", "th-guiding-principles-practitioners", "th-principles-of-yoga", "th-major-schools", "th-practices-for-health", "th-shatkarma-introduction", "th-vyayama-surya-namaskara-introduction", "th-yogasana-introduction", "th-pranayama-dhyana-introduction"]
TX = ["tx-patanjala-yoga-sutra", "tx-bhagavad-gita", "tx-hatha-pradipika", "tx-prasthanatrayi", "tx-aahara-diet", "tx-hatha-practices-health", "tx-mental-wellbeing-patanjala", "tx-bahiranga-antaranga", "tx-healthy-living-gita", "tx-subjective-experience"]
HL = ["hl-human-body-introduction", "hl-health-promotion-role-of-yoga", "hl-positive-attitudes", "hl-bhavas", "hl-dinacharya-ritucharya", "hl-holistic-approach", "hl-first-aid-cpr", "hl-stress-management", "hl-metabolic-respiratory", "hl-personality-development"]

def num_block(div, table):
    m = re.match(r"(\d+)\.(\d+)\b", div)
    if m:
        k = int(m.group(2)) - 1
        if 0 <= k < len(table): return table[k]
    return None

def demo_div(div):
    d = div.lower()
    for key, b in [("prayer", "pd-prayer-pranava-hymns"), ("cleansing", "pd-cleansing-techniques"), ("sukshma", "pd-sukshma-vyayama"), ("surya", "pd-surya-namaskara"), ("yogasana", "pd-yogasana-practice"), ("preparatory", "pd-preparatory-breathing"), ("pranayama", "pd-pranayama"), ("mudra", "pd-mudra"), ("meditation", "pd-meditation-practices")]:
        if key in d: return b
    return None

def teach_div(div):
    d = div.lower()
    for key, b in [("introduction", "pt-lesson-plan"), ("lesson plan", "pt-lesson-plan"), ("principles of teaching", "pt-teaching-groups"), ("preparation", "pt-class-preparation"), ("conducting", "pt-conducting-lessons-precautions"), ("salient", "pt-ideal-instructor"), ("models", "pt-model-lesson-plans")]:
        if key in d: return b
    return None

def assign(fn, frames):
    cur = None
    res = []
    for title, lines in frames:
        is_div = (not title) and len(lines) <= 3
        text = " ".join(lines)
        if is_div:
            d = text
            if fn == "ycb1_theory_intro.tex": nb = num_block(d, TH)
            elif fn == "ycb1_theory_texts.tex": nb = num_block(d, TX)
            elif fn == "ycb1_theory_health.tex": nb = num_block(d, HL)
            elif fn == "ycb1_practical_demoskills.tex": nb = demo_div(d)
            elif fn == "ycb1_practical_teachingskills.tex": nb = teach_div(d)
            else: nb = None
            if nb: cur = nb
            continue
        b = cur
        tl = (title + " " + text[:200]).lower()
        if fn == "ycb1_practical_asanas.tex": b = "pd-yogasana-practice"
        elif fn == "ycb1_practical_application.tex": b = "pa-application-of-knowledge"
        elif fn == "ycb1_practical_fieldexperience.tex": b = "pf-field-experience"
        elif fn in ("ycb1_exam.tex", "ycb1_overview.tex"): b = "ex-exam-and-certification"
        elif fn == "ycb1_practical_demoskills.tex":
            if re.search(r"sthula|sarvanga|hrid|comparison of sukshma", tl): b = "pd-sthula-vyayama"
            elif re.search(r"bandha|jalandhar|uddiyan|mula ", title.lower()): b = "pd-bandha"
        elif fn == "ycb1_practical_teachingskills.tex":
            if "class management" in tl: b = "pt-class-management"
            elif "factors" in title.lower(): b = "pt-factors-influencing-teaching"
        if b is None: continue
        res.append((b, title, lines))
    return res

FAQ_RULES = [
 (r"sthul|sarvanga", "pd-sthula-vyayama"), (r"suryanamaskar|surya namaskar", "pd-surya-namaskara"),
 (r"pranayama|puraka|kumbhak|sheetali|sitali|bhramari|bhastrika|heating|hunger and thirst", "pd-pranayama"),
 (r"kapalabhati|kapalbhati|dhauti|\bneti\b|shatkarma|nauli|basti|trataka|shudhkarma", "th-shatkarma-introduction"),
 (r"gheranda|hatha|hyp\b|swatmaram|ghat|matsyendra|acharya", "tx-hatha-pradipika"),
 (r"patanjali|sutra|antaray|vibhuti|klesha|chitta|yogabhasya|ishwar", "tx-patanjala-yoga-sutra"),
 (r"gita|karmasu|samalam", "tx-bhagavad-gita"), (r"prasthan|smriti", "tx-prasthanatrayi"),
 (r"mitahara|mita |diet|\bfood|aahara|ahara|stomach|taste|rasa", "tx-aahara-diet"),
 (r"adhija|anadhija|vyadhi|psychosomatic|stress|frustrat|upset|prayer|mental illness", "hl-stress-management"),
 (r"season|ritu|hemant|grishma|sharad|shishira|achamana|abhyanga|adana|dosha|ayurved|nidra|sattu|langhana|hydropathy|heliotherapy|trayopastambha|charaka|sushruta|sarangdhara|bottle|nature cure|frawley|kuhne", "hl-dinacharya-ritucharya"),
 (r"kosha|dhatu|triguna|sattvic|rajasic|tamasic|purusha|prakriti|sankhya|chakra|mandukya|taittiriya", "th-principles-of-yoga"),
 (r"lesson plan|teach|student|group discussion|dress|session|limitations of a practice|technique", "pt-teaching-groups"),
 (r"homeostasis|kwashiorkor|protein|nervous|scurvy|pellagra|blood", "hl-human-body-introduction"),
 (r"jnana|bhakti|bhakta|kirtana|smarana|sravana|raja yoga|karma yoga|laya", "th-major-schools"),
 (r"asana|dhanurasana|back pain|immediately after food|throat", "th-yogasana-introduction"),
 (r"gayatri|mantra|pranav|pranava|aham brahm", "pd-prayer-pranava-hymns"),
 (r"etymology|yuj|root|definition of yoga|means\b.*unite|sanskrit, yoga", "th-etymology-definitions-aim"),
 (r"veda|upanishad|international day|kaivalya|kuvalay|vedas|purushartha|wealth|jaimini|nastik|nastika", "th-origin-history-development"),
 (r"sukshma", "pd-sukshma-vyayama"),
]

def faq_assign(title, lines):
    s = (title + " " + " ".join(lines)).lower()
    for rx, b in FAQ_RULES:
        if re.search(rx, s): return b
    return None

def fix(s):
    s = s.replace("\u2014", " - ").replace("--", "-").replace("\u2013", "-")
    s = re.sub(r"\s+-\s+-\s+", " - ", s)
    return re.sub(r"[ \t]+", " ", s)

def render_frame(title, lines, ind="    "):
    out = []
    head = fix(title).strip() if title else ""
    body = [fix(l) for l in lines]
    if head:
        out.append(f"{ind}- **{head}**")
        sub = ind + "  "
    else:
        sub = ind
    for l in body:
        l = l[2:] if l.startswith("- ") else l
        out.append(f"{sub}- {l}")
    return out

def main():
    per = {}
    faqs = {}
    general = []
    seen = set()
    for fn in sorted(os.listdir(p.D)):
        if not (fn.startswith("ycb1_") and fn.endswith(".tex")): continue
        if fn in ("ycb1_refs.tex", "ycb1_backcover.tex", "ycb1_frontcover.tex"): continue
        frames = p.parse(fn)
        if fn == "ycb1_theory_faqs.tex":
            for title, lines in frames:
                if not lines or (not title and len(lines) <= 1 and lines[0] == "FAQs"): continue
                key = (title, tuple(lines))
                if key in seen: continue
                seen.add(key)
                b = faq_assign(title, lines)
                if b: faqs.setdefault(b, []).append((title, lines))
                else: general.append((title, lines))
            continue
        for b, title, lines in assign(fn, frames):
            if not lines: continue
            if all(l.startswith("|") or len(l) < 2 for l in lines): continue
            key = (title, tuple(lines))
            if key in seen: continue
            seen.add(key)
            per.setdefault(b, []).append((title, lines))

    raw = open(P, encoding="utf-8", newline="").read()
    eol = "\r\n" if "\r\n" in raw else "\n"
    t = raw.replace("\r\n", "\n")
    n_fr = 0; n_faq = 0
    for b, frs in per.items():
        i = t.find("- **ID:** ycb1-" + b)
        if i < 0:
            print("no block", b); continue
        j = t.find("\n- **ID:**", i + 5); j = len(t) if j == -1 else j
        blk = t[i:j]
        if "Workshop slide content" in blk: continue
        lines = ["- **Workshop slide content (merged from the current deck as the starting point; to be structured into the layers above, checked, and trimmed):**"]
        for title, ls in frs:
            lines += render_frame(title, ls, "  ")
            n_fr += 1
        k = blk.index("- **Worked examples:**")
        blk = blk[:k] + "\n".join(lines) + "\n" + blk[k:]
        t = t[:i] + blk + t[j:]
    for b, frs in faqs.items():
        i = t.find("- **ID:** ycb1-" + b)
        if i < 0: print("no faq block", b); continue
        j = t.find("\n- **ID:**", i + 5); j = len(t) if j == -1 else j
        blk = t[i:j]
        m = re.search(r"- \*\*FAQ:\*\*[^\n]*\n", blk)
        if not m: print("no FAQ layer", b); continue
        lines = ["- **FAQ (from the deck's question bank; answers not yet checked against sources):**"]
        for title, ls in frs:
            lines += render_frame("", ls, "  ")
            n_faq += 1
        blk = blk[:m.start()] + "\n".join(lines) + "\n" + blk[m.end():]
        t = t[:i] + blk + t[j:]
    if general and "## Question bank from the workshop deck" not in t:
        sec = ["", "## Question bank from the workshop deck (not yet assigned to a block)", "", "Questions with their answers as the deck has them; to be checked, assigned to blocks and merged into the Quiz layers.", ""]
        for title, ls in general:
            sec += render_frame("", ls, "")
        t = t.rstrip("\n") + "\n" + "\n".join(sec) + "\n"
    open(P, "w", encoding="utf-8", newline="").write(t.replace("\n", eol))
    print("frames merged", n_fr, "faq entries", n_faq, "general", len(general), "blocks", len(per), "faq blocks", len(faqs))

main()
