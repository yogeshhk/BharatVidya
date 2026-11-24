# YCB Level 1 exam-guide booklet (Yoga Protocol Instructor)

**Main principle:** an easy-to-use exam guide, a small booklet, not a second textbook. The official guidebook is long, formal and hard to study from; this is short, simple and plain, complete to the dot against the Board's Level 1 syllabus, with nothing outside it. Every fact is checked before it flows down (see the fact-check gate in `AUTHORING.md`).

A planned booklet for the Yoga Certification Board Level 1 exam, built notes first: one Markdown notes file is the master, and the workshop deck, its cheat sheet and the book are derived from it. This README is kept in step with the real state of the folder; update it in the same pass as any change.

## Status

Planning. The notes file has a block for every syllabus topic, each with a Local sources line that says how well the reference documents in `docs/` cover it (covered, partial, gap). Written so far, in own words and all pending review: the exam and certification block and the practical blocks that the Common Yoga Protocol covers (guiding principles, prayer, loosening practices, the protocol asanas, kapalabhati, nadi shodhana and bhramari, meditation, two mudras). The theory blocks and the rest of the syllabus are not written yet. Main finding so far: the guidebook in `docs/` is for the older four-level scheme, so it cannot be the spine of this book; the Board's current Level 1 syllabus is. The book driver, covers, make file and template exist in `book/` (compiles, front matter only); no chapter exists yet. The workshop deck is the seed, not the authority. The decisions made so far and the open ones are in `TODO.md`; the rules for authoring are in `AUTHORING.md`; the full analysis and proposal is in `../../../reports/ycb1_textbook_analysis.md`.

Decisions taken: licence for the book is all rights reserved (`LICENSE_BOOK.md`); go as a bounded project, a workshop companion more than a revenue project; notes first; English first; the book lives here with its own licence (all rights reserved); people figures are AI drafts for the deck and own photographs or commissioned line art for print.

## Folder map

| Path | What it is |
|---|---|
| `docs/Notes YCB1.md` | The master notes: one block per syllabus topic with a stable ID, review status, figure links |
| `docs/image_system_prompt.md` | The common system prompt for picture generation (people figures, diagrams), the prompt layout and the original-then-new review steps |
| `docs/image_register.csv` | One row per picture used by the deck: current file, prompt or brief for the replacement, planned final name and path, risk, where it is used |
| `docs/Syllabus-YPI-Version-0.2-Board.pdf`, `docs/Guideline-for-YP-Version-0.3-Board.pdf` | The Board's own syllabus and guideline for this level, downloaded from the Board site; these are the authority for the exam rules and the syllabus |
| `docs/*.pdf` and `docs/README.md` | Reference PDFs kept beside the notes: the Board's syllabi and guideline, the Common Yoga Protocol, a mind map, and two large official or published instructor books, with a README written for the Board papers. None of these is the author's work. The level syllabus copy carries a private institute's contact footer: replace it with the Board's own file before citing. The two large books are copyrighted and are not for the public repository (see `TODO.md`) |
| `docs/ycb1_exam*` | Copies of the deck's exam source and exam screenshots, placed here by the author |
| `workshop/` | The YCB1 workshop deck and cheat sheet (drivers, `ycb1_*` topic files, `images/`, `make_ycb1.bat`), clubbed here with the book as in QCNP and the Game Theory Workbook (`docs/`, `workshop/`, later `book/`) |
| `book/` | The book project: `Main_Book_YCB1_interior.tex`, `Main_Book_YCB1_covers.tex`, `book_ycb1_content.tex` (the only place chapter order lives), front matter, references, `template_book.tex`, `make_book_ycb1.bat` (XeTeX). Skeleton only, no chapters yet; a chapter is added as one `\input` line once its notes block is checked |
| `README.md`, `TODO.md`, `AUTHORING.md` | This guide, the open actions, the working rules |

The workshop deck this book grows from is `workshop/`. Its pictures are in `images/`; replacements will go in `images/new/` (not created yet). Every picture line in the deck carries a comment with its figure ID, current file and planned final path.

## Sync rule

Notes first. A fact, point, exercise or figure is fixed in the notes, then carried down to the deck and the book by hand. Nothing propagates automatically. When this folder changes, update this README, `TODO.md` and the Publications entry (`D:\Yogesh\GitHub\Publications\TODO.md`; the author keeps Google Keep in step).
