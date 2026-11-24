"""Record deck frame titles added by the 2026-11-24 syncs in the notes block that owns them (idempotent)."""
import io, os
P = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "LaTeX", "books", "YCB1", "docs", "Notes YCB1.md"))
MAP = {
 "ycb1-ex-exam-and-certification": ["Who Can Sit, and Pass Marks", "After the Result", "On the Exam Day", "References for Level 1 Exam"],
 "ycb1-pf-field-experience": ["The Board's Two Forms"],
 "ycb1-pt-factors-influencing-teaching": ["Factors Influencing Yoga Teaching"],
 "ycb1-pt-class-preparation": ["Preparing the Room, the Student and the Opening"],
 "ycb1-hl-human-body-introduction": ["Functions of Circulatory System", "Functions of Respiratory System", "Functions of Excretory System"],
 "ycb1-hl-holistic-approach": ["Yoga, Care and Well-being"],
 "ycb1-hl-first-aid-cpr": ["Moving a Casualty, Food and Drink", "CPR: Doing It Well", "Stopping CPR and the Instructor's Role"],
 "ycb1-hl-metabolic-respiratory": ["Respiratory \\& Metabolic Health: Yogic Prevention"],
 "ycb1-th-guiding-principles-practitioners": ["Practice: Before, During and After", "When Not to Practise, and Food"],
 "ycb1-tx-patanjala-yoga-sutra": ["The Twelve Sutras in Order"],
 "ycb1-tx-bhagavad-gita": ["Sense of the Five Shlokas"],
 "ycb1-tx-hatha-pradipika": ["Hatha Yoga Pradipika: Laya Yoga and Nadanusandhana", "Hatha Yoga Pradipika: Samadhi as the Aim", "Middle Path and General Rules for Asana Practice"],
 "ycb1-tx-hatha-practices-health": ["What Each Hatha Practice Adds"],
 "ycb1-tx-prasthanatrayi": ["Prasthanatrayee: Heard, Remembered, Reasoned"],
 "ycb1-tx-mental-wellbeing-patanjala": ["Nine Obstacles and Four Companions", "A Clear and Steady Mind: Means and Remedy"],
 "ycb1-tx-bahiranga-antaranga": ["Five Yamas and Five Niyamas"],
}
MARK = "- **Deck frames added by the sync (titles only; the content is in the Material above):**"
lines = io.open(P, encoding="utf-8").read().split("\n")
out, cur, done, start = [], None, 0, 0
for ln in lines:
    if ln.startswith("- **ID:** "):
        cur = ln.split("**ID:**")[1].strip(); start = len(out)
    if ln.startswith("- **References:**") and cur in MAP:
        if not any(l.startswith(MARK) for l in out[start:]):
            out.append(MARK + " " + "; ".join(MAP[cur])); done += 1
        cur = None
    out.append(ln)
io.open(P, "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("blocks updated:", done)
