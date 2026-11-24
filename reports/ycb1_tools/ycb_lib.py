import re
P = "D:/Yogesh/GitHub/BharatVidya/LaTeX/books/YCB1/docs/Notes YCB1.md"

def apply(blocks, log_extra=""):
    """blocks: dict id -> (material_md, explanation_md, sources_line_or_None)
    Replaces everything from '- **Material:**' up to '- **Worked examples:**' in that block."""
    raw = open(P, encoding="utf-8", newline="").read()
    eol = "\r\n" if "\r\n" in raw else "\n"
    t = raw.replace("\r\n", "\n")
    for bid, (mat, expl, log) in blocks.items():
        i = t.index("- **ID:** " + bid)
        j = t.find("\n- **ID:**", i + 5)
        j = len(t) if j == -1 else j
        blk = t[i:j]
        a = blk.index("- **Material:**")
        b = blk.index("- **Worked examples:**")
        new = mat.rstrip("\n") + "\n" + expl.rstrip("\n") + "\n" + "- **Fact check log (still pending):** " + log + "\n"
        blk = blk[:a] + new + blk[b:]
        t = t[:i] + blk + t[j:]
    open(P, "w", encoding="utf-8", newline="").write(t.replace("\n", eol))
    print("updated", len(blocks))
