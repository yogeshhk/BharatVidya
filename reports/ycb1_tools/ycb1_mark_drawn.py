"""Mark register figures whose replacement picture now exists in images/new/ as status 'drawn' (drawn by us in TikZ,
picture only in the repo). Idempotent. Usage: python -I ycb1_mark_drawn.py"""
import csv, io, os
B = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "LaTeX", "books", "YCB1")) + os.sep
p = B + "docs/image_register.csv"
rows = list(csv.DictReader(io.open(p, encoding="utf-8")))
f = list(rows[0].keys()); n = 0
for r in rows:
    if r["final_name"] and os.path.exists(B + "images/new/" + r["final_name"]) and r["status"] != "drawn":
        r["status"] = "drawn"; n += 1
w = csv.DictWriter(io.open(p, "w", encoding="utf-8", newline=""), fieldnames=f, lineterminator="\n")
w.writeheader(); w.writerows(rows)
print("marked drawn:", n)
