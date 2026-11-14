# Sanskrit संस्कृत: LaTeX

LaTeX sources for Sanskrit grammar material, kept here beside the other Sanskrit resources.

| File | What it is |
|---|---|
| `subantaruupaNi.tex` | A standalone XeLaTeX document on the declension (subanta) forms of Sanskrit nouns. It is another author's work, not this repository's own: its source carries that author's contact details, so ask them before reusing it |
| `preamble.tex`, `shloka.sty` | The style files that document uses |
| `images/` | Two pictures (`uchchar.jpg`, `vedic-resesrve.gif`); no deck uses them |
| `Notes.md` | A short note on learning Sanskrit. It points at `images/sunsal.jpg`, which is not in the folder, so the picture does not show |

The Beamer decks of this repository do **not** use these style files. They use `LaTeX/template_presentation.tex`
and `LaTeX/template_cheatsheet.tex`; see [LaTeX/README.md](../../LaTeX/README.md). Compile with XeTeX
(`texify --engine=xetex -cp subantaruupaNi.tex`), because the text is in Devanagari.
