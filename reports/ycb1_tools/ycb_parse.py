import re, glob, sys, os
sys.stdout.reconfigure(encoding="utf-8")
D = "D:/Yogesh/GitHub/BharatVidya/LaTeX/books/YCB1/workshop/"

def strip_comments(src):
    out = []
    for l in src.split("\n"):
        s = l.strip()
        if s.startswith("%"):
            continue
        # drop trailing comments (unescaped %)
        l = re.sub(r"(?<!\\)%.*$", "", l)
        out.append(l)
    return "\n".join(out)

def brace_arg(s, i):
    """s[i] == '{' ; return (content, index after closing)"""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{": depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
    return s[i + 1:], len(s)

def clean(s):
    s = re.sub(r"\\includegraphics(\[[^\]]*\])?\{[^}]*\}", "", s)
    s = re.sub(r"\\(begin|end)\{(itemize|enumerate|columns|column|center|frame|tabular|table|block|alertblock|exampleblock|description|minipage|figure|adjustbox|tcolorbox)\}(\[[^\]]*\])?(\{[^}]*\})?", "\n", s)
    s = re.sub(r"\\(hline|pause|centering|vfill|vspace\*?\{[^}]*\}|hspace\*?\{[^}]*\}|newline|noindent|small|tiny|footnotesize|scriptsize|large|Large|LARGE|Huge|huge|bfseries|itshape|normalsize)\b", "", s)
    s = re.sub(r"\\item\s*(\[[^\]]*\])?", "\n- ", s)
    for _ in range(6):
        s = re.sub(r"\\(textbf|textit|emph|underline|texttt|textsc|textcolor\{[^}]*\}|colorbox\{[^}]*\}|alert|text|mbox|resizebox\{[^}]*\}\{[^}]*\})\{([^{}]*)\}", r"\2", s)
    s = s.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_").replace("\\#", "#").replace("\\$", "$")
    s = s.replace("\\\\", "\n").replace("&", " | ")
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", "", s)
    s = s.replace("{", "").replace("}", "").replace("~", " ")
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in s.split("\n")]
    return [l for l in lines if l]

def parse(fn):
    src = open(D + fn, encoding="utf-8").read()
    src = strip_comments(src)
    frames = []
    for m in re.finditer(r"\\begin\{frame\}(\[[^\]]*\])?(.*?)\\end\{frame\}", src, flags=re.S):
        body = m.group(2)
        title = ""
        k = body.find("\\frametitle")
        if k >= 0:
            j = body.index("{", k)
            title, _ = brace_arg(body, j)
            body = body[:k] + body[_:]
        lines = clean(body)
        frames.append((" ".join(clean(title)) if title else "", lines))
    return frames

if __name__ == "__main__":
    tot = 0
    for fn in sorted(os.listdir(D)):
        if fn.startswith("ycb1_") and fn.endswith(".tex"):
            fr = parse(fn)
            tot += len(fr)
            print("##", fn, len(fr), "frames")
            for t, l in fr:
                if not t and len(l) <= 3:
                    print("   DIVIDER:", " / ".join(l)[:100])
    print("total", tot)
