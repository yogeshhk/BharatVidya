"""Move LaTeX/books/YCB1/workshop/images/* to LaTeX/books/YCB1/images/ (hash-checked) and fix path strings.
Idempotent. The old folder is removed only if empty. Run: python -I ycb1_move_images.py
"""
import os, io, hashlib, shutil, glob
B = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "LaTeX", "books", "YCB1"))
SRC, DST = os.path.join(B, "workshop", "images"), os.path.join(B, "images")
def h(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
os.makedirs(DST, exist_ok=True)
moved = 0
if os.path.isdir(SRC):
    for n in sorted(os.listdir(SRC)):
        s, d = os.path.join(SRC, n), os.path.join(DST, n)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True); continue
        if os.path.exists(d):
            raise SystemExit("destination exists: " + n)
        hs = h(s); shutil.copy2(s, d)
        if h(d) != hs: raise SystemExit("hash mismatch: " + n)
        os.remove(s); moved += 1
    try: os.rmdir(SRC)
    except OSError: print("old folder not empty, left in place")
print("moved", moved, "files; now in images:", len([x for x in os.listdir(DST) if os.path.isfile(os.path.join(DST, x))]))
# path strings in text files (comments, register, docs)
files = glob.glob(B + "/workshop/ycb1_*.tex") + glob.glob(B + "/docs/*.md") + glob.glob(B + "/docs/*.csv") + [B + "/AUTHORING.md", B + "/README.md", B + "/TODO.md"]
n = 0
for f in files:
    t = io.open(f, encoding="utf-8").read()
    u = t.replace("books/YCB1/workshop/images/", "books/YCB1/images/").replace("`workshop/images/new/`", "`images/new/`").replace("`workshop/images/`", "`images/`")
    if u != t:
        io.open(f, "w", encoding="utf-8", newline="\n").write(u); n += 1
print("text files updated:", n)
