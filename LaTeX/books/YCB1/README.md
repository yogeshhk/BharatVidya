# YCB Level 1 textbook (Yoga Protocol Instructor)

A planned textbook for the Yoga Certification Board Level 1 exam, built notes first: one Markdown notes file is the master, and the workshop deck, its cheat sheet and the book are derived from it. This README is kept in step with the real state of the folder; update it in the same pass as any change.

## Status

Planning. The notes file has a block for every syllabus topic, each with a Local sources line that says how well the reference documents in `docs/` cover it (covered, partial, gap). The teaching text is not written yet. Main finding so far: the guidebook in `docs/` is for the older four-level scheme, so it cannot be the spine of this book; the Board's current Level 1 syllabus is. No book chapter or book driver exists. The workshop deck is the seed, not the authority. The decisions made so far and the open ones are in `TODO.md`; the rules for authoring are in `AUTHORING.md`; the full analysis and proposal is in `../../../reports/ycb1_textbook_analysis.md`.

Decisions taken: go as a bounded project, a workshop companion more than a revenue project; notes first; English first; the book lives here with its own licence (not yet chosen); people figures are AI drafts for the deck and own photographs or commissioned line art for print.

## Folder map

| Path | What it is |
|---|---|
| `docs/Notes YCB1.md` | The master notes: one block per syllabus topic with a stable ID, review status, figure links |
| `docs/image_register.csv` | One row per picture used by the deck: current file, prompt or brief for the replacement, planned final name and path, risk, where it is used |
| `docs/*.pdf` and `docs/README.md` | Reference PDFs kept beside the notes: the Board's syllabi and guideline, the Common Yoga Protocol, a mind map, and two large official or published instructor books, with a README written for the Board papers. None of these is the author's work. The level syllabus copy carries a private institute's contact footer: replace it with the Board's own file before citing. The two large books are copyrighted and are not for the public repository (see `TODO.md`) |
| `docs/ycb1_exam*` | Copies of the deck's exam source and exam screenshots, placed here by the author |
| `README.md`, `TODO.md`, `AUTHORING.md` | This guide, the open actions, the working rules |

The workshop deck this book grows from is `../../workshops/YCB1/`. Its pictures are in `../../workshops/YCB1/images/`; replacements will go in `../../workshops/YCB1/images/new/` (not created yet). Every picture line in the deck carries a comment with its figure ID, current file and planned final path.

## Sync rule

Notes first. A fact, point, exercise or figure is fixed in the notes, then carried down to the deck and the book by hand. Nothing propagates automatically. When this folder changes, update this README, `TODO.md` and the Publications entry (`D:\Yogesh\GitHub\Publications\TODO.md`; the author keeps Google Keep in step).
