# TODO: YCB Level 1 textbook

Parked as a 2027 project. Open actions only; rules live in `AUTHORING.md`, status in `README.md`. Work one task at a time; the author confirms before each.

## First: make notes, workshop and textbook one consistent body of content
Constraints: the fact-check gate applies (pending blocks are written as unverified, with a "Not yet fact-checked" box at the chapter opening); no cure claims; one chapter per syllabus unit or topic group, order only in `book/book_ycb1_content.tex`; compile once per batch, then `/verify-pdf`.
- [ ] Notes follow the Board syllabus order: every unit and topic has a block, nothing missing, nothing outside the syllabus; all deck and book content also lives in the notes.
- [ ] Workshop = notes, terse: every deck section maps to a block; no deck point absent from the notes.
- [ ] Textbook = notes, verbose: each chapter carries all of its block as full prose (explanation, examples, exercises, FAQ); fix chapters that are thinner than the deck.
- [ ] Re-run `../../../reports/ycb1_tools/ycb1_coverage.py` after each batch; its report is the acceptance test (keep it local).
- [ ] Author reads the re-synced chapters (`D:\Yogesh\GDrive\ToPrint\Main_Book_YCB1_interior.pdf`); certified teacher and qualified reviewer pass. Boxes now remain only where a block is pending.

## Close the open checks
- [ ] Download the Board's current Level 1 syllabus and replace the local copy in `docs/` (the current copy carries a private institute's footer); check for revisions to syllabus, marks and exam rules since guideline version 0.3.
- [ ] Decide which of the two identical guidebook copies to keep (the author removes the other). The two guidebook PDFs, `docs/Yoga_Booklet.pdf` and `docs/YCB Protocol Instructor.gdraw` stay out of the public repository (gitignore; untrack by hand if ever committed).
- [ ] Find a named source for each block marked gap; confirm the memorised sutra and sloka lists against the Board syllabus text. For application of knowledge and field experience, ask the Board or an accredited institute what is assessed (keep the honest wording until then: `../../../reports/ycb1_tools/open_sources_application.md`).
- [ ] Check two FAQ answers (Gita paths; kaivalya as asamprajnata samadhi) and the Sanskrit spellings of Yoga Sutra 1.23 to 1.29 and Gita 16.1 against a printed edition (`../../../reports/ycb1_tools/deck_fixes_*.md`).
- [ ] Ask one accredited training institute how many candidates sit Level 1 a year and what the trainees use to study.

## Notes blocks (author reviews each; a certified teacher reviews practical and health blocks)
- [ ] Write the methods for pranava and soham recitation, body and breath awareness, and yoga nidra from a named source (meditation chapter gap).
- [ ] Brevity pass: trim each written block to the main principle.
- [ ] Rewrite the question bank in `workshop/ycb1_theory_faqs.tex` into the Quiz and FAQ layers, in own words.
- [ ] Write the design authority file: audience, promises, tone, safety rules, image policy, syllabus-to-topic map.

## Figures (`docs/image_register.csv`)
- [ ] Trial three figures (one pose, one anatomy diagram, one vyayama pair) with the shared character sheet; fix the prompt wording; teacher check.
- [ ] Generate the remaining pictures per `docs/image_system_prompt.md` into `images/new/`; review side by side; comment out the original only after approval.
- [ ] Draw the diagrams (anatomy, kosha, chakra, prana, history, bandha, breathing, stick figures) in TikZ or Python.
- [ ] Retype the table screenshots as LaTeX tables in own words; retire the exam screenshots.
- [ ] For print, replace people figures with own photographs or commissioned line art; teacher reviews every pose.

## Derived outputs
- [ ] Re-author the deck frames from the notes (text that follows a web page or the guidebook closely must be rewritten); keep the deck compiling.
- [ ] Mock exam and answer key.
- [ ] Optional readability pass F3 from `docs/reviews/review_YCB1_2026-11-27.md` (turn "the guidebook says" narration into plain statements). The review's other findings are applied and the book is re-synced, rebuilt and in ToPrint (2026-11-27).
- [ ] Self-publish route (print-ready PDF under the author's control) after the person-only checks, the figures and the author's read.

## Records
- [ ] Keep `README.md` and `Publications/TODO.md` in step with each change.
