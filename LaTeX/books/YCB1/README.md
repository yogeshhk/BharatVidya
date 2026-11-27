# YCB Level 1 yoga textbook (Yoga Protocol Instructor)

**Main principle:** an easy-to-use textbook for the exam. The official guidebook is long, formal and hard to study from; this is short, simple and plain, complete to the dot against the Board's Level 1 syllabus, with nothing outside it. Every fact is checked before it flows down (fact-check gate in `AUTHORING.md`).

Built notes first: one Markdown notes file is the master; the workshop deck, its cheat sheet and the textbook are derived from it by hand. Keep this README in step with the folder; update it in the same pass as any change.

## At a glance

| | |
|---|---|
| Stage | Closed 2026-11-27 as a complete draft: 44 of 52 notes blocks fact-checked; book (with mock exam appendix), deck and cheat sheet build clean and agree with the notes |
| Master and flow | `docs/Notes YCB1.md`, then `workshop/` (deck, cheat sheet) and `book/`; one way, by hand |
| Build | `book/make_book_ycb1.bat` (XeTeX) |
| Review | `docs/reviews/review_YCB1_2026-11-27.md` (MAJOR REVISION: re-sync the chapters from the checked notes) |
| Proposal | `docs/proposal/YCB1_Book_Proposal.md`, PDF via `docs/proposal/build_proposal.bat`; route is self publish first |
| Cover | `book/Main_Book_YCB1_covers.tex`, QCNP theme |

Cross-repo book standard: `Publications/Books/CONVENTIONS.md`, "All book projects". Rules: `AUTHORING.md`, `CLAUDE.md`.

## Status

Closed on 2026-11-27 as a complete draft (author's decision). Every notes block has textbook text and the LaTeX book builds (chapter files in `book/`, one `\input` line each), with a generated mock exam appendix. The workshop deck was re-authored from the notes the same day. Blocks not yet fact-checked (eight, listed in the coverage report) open with a "Not yet fact-checked" box in the book. There are no open actions; what reopening would need is listed below. The guidebook in `docs/` belongs to the older four-level scheme, so the Board's current Level 1 syllabus is the spine, not the guidebook.

Decisions: licence is all rights reserved (`LICENSE_BOOK.md`); a bounded project, a workshop companion more than a revenue project; English first; route is self publish first, with Sakal or a Marathi edition only after the English draft and a demand check; docx is fine (a Word export from the notes is allowed; the LaTeX project is the build that exists); people figures are AI drafts for the deck, own photographs or commissioned line art for print. Full analysis: `../../../reports/ycb1_textbook_analysis.md`.

## Folder map

| Path | What it is |
|---|---|
| `docs/Notes YCB1.md` | The master notes: one block per syllabus topic with a stable ID, review and fact-check status, figure links |
| `docs/DESIGN.md` | Design authority: decisions, reader contract, voice, safety and image rules, syllabus-to-block-to-chapter map |
| `docs/image_system_prompt.md` | Common system prompt for picture generation and the review steps |
| `docs/image_register.csv` | One row per picture: current file, brief, planned final path, risk, uses |
| `docs/Syllabus-YPI-Version-0.2-Board.pdf`, `docs/Guideline-for-YP-Version-0.3-Board.pdf` | The Board's syllabus and guideline for this level: the authority for exam rules and syllabus |
| `docs/*.pdf`, `docs/README.md` | Other reference PDFs (Board papers, Common Yoga Protocol, a mind map, two large instructor books). Not the author's work; the large books are copyrighted and not for the public repository (see `TODO.md`) |
| `docs/ycb1_exam*` | The deck's exam source and exam screenshots (screenshots retired; the mock exam draft is the last section of the notes) |
| `workshop/` | The workshop deck and cheat sheet (drivers, `ycb1_*` topic files, `make_ycb1.bat`) |
| `book/` | The textbook: `Main_Book_YCB1_interior.tex`, `Main_Book_YCB1_covers.tex`, `book_ycb1_content.tex` (the only place chapter order lives), `ycb1_book_*` chapter files, `template_book.tex`, `make_book_ycb1.bat` (XeTeX) |
| `images/` | All pictures for deck and book; replacements in `images/new/`, with the TikZ sources of the line diagrams and `make_figures.bat` in `images/new/src/` |
| `LICENSE_BOOK.md`, `README.md`, `TODO.md`, `AUTHORING.md`, `CLAUDE.md` | Licence notice, this guide, open actions, working rules, rules for Claude |

Every picture line in the deck carries a comment with its figure ID, current file and planned final path.

## Build

Run from the folder, XeTeX: `workshop/make_ycb1.bat` (deck and cheat sheet), `book/make_book_ycb1.bat` (textbook).

## Sync rule

Notes first. A fact, point, exercise or figure is fixed in the notes, then carried down to the deck and the textbook by hand; nothing propagates automatically. When this folder changes, update this README, `TODO.md` and the Publications entry (`D:\Yogesh\GitHub\Publications\TODO.md`; the author keeps Google Keep in step).

## If the book is reopened

Not needed for the closed draft; recorded so nothing is lost. Person-only or resource-bound, in rough order:
- Board: download the current Level 1 syllabus (the local copy carries a private institute's footer) and check for revisions to syllabus, marks and exam rules since guideline version 0.3; ask the Board or an accredited institute what application of knowledge and field experience assess (honest wording kept meanwhile: `../../../reports/ycb1_tools/open_sources_application.md`).
- Reviews: a certified teacher for every pose, breathing practice and kriya (text and figure); a qualified reviewer for first aid, CPR and the disorder content; the eight pending blocks (mudra, sukshma and sthula vyayama, yogasana, bhavas, teaching groups, conducting lessons, application of knowledge).
- Printed editions: Sanskrit spellings of Yoga Sutra 1.23 to 1.29 and Gita 16.1; two FAQ answers (Gita paths; kaivalya as asamprajnata samadhi) (`../../../reports/ycb1_tools/deck_fixes_*.md`).
- Files: keep one of the two identical guidebook copies; the guidebook PDFs, `docs/Yoga_Booklet.pdf` and `docs/YCB Protocol Instructor.gdraw` stay out of the public repository.
- Figures: trial and generate the pose pictures (`docs/image_system_prompt.md`); line art for the realistic anatomy pictures; own photographs or commissioned line art for print.
- Content polish: a brevity pass on the notes; point-level matching between deck frames and notes (titles already match both ways).
- Market: ask one accredited institute how many candidates sit Level 1 a year and what they study from.
- Route: self publish (print-ready PDF under the author's control) after the above.
