# TODO: YCB Level 1 textbook

**Status: parked as a 2027 project (author, 2026-11-24).** All notes blocks have book text and the book builds; what remains is the author's read, the teacher and reviewer pass, clearing the flagged pictures and generating the complicated figures. Pick up from the list below.

Open actions only, terse. Rules live in `AUTHORING.md`, status in `README.md`. Work one task at a time, in this order; the author confirms before each.

## TOP PRIORITY (author, 2026-11-24): make the notes, the workshop and the book one consistent body of content

Raised by the author after reading all three side by side: they look like three distinct things. Do this first next session (the author suggests running it with Opus). Plan it before touching anything; one confirmation per step.

The rule to make true:
- [ ] **Notes are the master and follow the Board syllabus structure.** Every topic of the Board's Level 1 syllabus (each unit and each topic under it) has its block in `docs/Notes YCB1.md`, in syllabus order, with nothing missing and nothing outside the syllabus. Everything the workshop deck says is also in the notes, and everything the book says is also in the notes (no content lives only in the deck or only in the book).
- [ ] **Workshop = the notes, terse.** Each deck section maps to a notes block; the frames are the same points, short and point-wise. A candidate who studies the deck should find nothing the notes do not hold, and nothing the notes hold (Material, checked) missing without a reason.
- [ ] **Book = the same notes, verbose.** Each book chapter or section carries ALL of the content of its notes block, written out as full explanatory prose like a book (explanation, reasoning, examples, worked examples, exercises, FAQ), not a summary and not a shorter list than the deck. Today the chapters are thinner than the deck in places (for example they leave out whole deck-derived layers that are still unchecked) and read like a different document; that must be fixed so deck and book cover the same ground, the deck in short points and the book in full text.
- [ ] **Then prove it.** Build a coverage check (a script plus a report) that maps every syllabus topic to its notes block, its deck frames and its book section, and lists gaps in either direction (in notes but not deck, in notes but not book, in deck or book but not notes). The report is the acceptance test; re-run it after every batch of changes. Keep it local (not for the public release), for example in `reports/ycb1_tools/`.

Constraints to carry into that work: the fact-check gate still applies (a block flows to the deck and the book only when `Fact check: checked`; pending blocks are written as unverified, never presented as certain); no hard-typed numbering; no cure claims; the book stays one chapter per syllabus unit or topic group with the order only in `book/book_ycb1_content.tex`; compile once per batch and run `/verify-pdf` at the end.

Decided 2026-11-24: (a), pending blocks are written into the book with a "Not yet fact-checked" box at the chapter opening. Done the same day: every block now has book text (231-page interior), figures placed with their prompts, coverage script and report in `reports/ycb1_tools/` (`ycb1_coverage.py`). Still open: the author's read of the new chapters, the reviewer pass, and taking the box off each chapter as its blocks are checked.

## Close the open checks (before any chapter text)
- [ ] Download the Board's own current Level 1 syllabus from yogacertificationboard.nic.in and replace the local copy in `docs/` (the current copy carries a private institute's contact footer). Check whether the Board has revised the syllabus, the marks or the exam rules since version 0.3 of its guideline.
- [x] Keep the two large instructor-book PDFs in `docs/` out of the public repository (decide: ignore pattern in `.gitignore`, or move them to the private Drive). The BharatVidya policy says third-party books are not hosted here. Done 2026-11-24: the two guidebook copies are in the repo `.gitignore`; if they were ever committed, untrack them by hand.
- [x] Read the guidebook in `docs/` (two copies, identical text). Result: it belongs to the older four-level scheme, not to the current Yoga Protocol Instructor syllabus. It has no content for application of knowledge or field experience, and no dedicated section on the Gita, Prasthanatrayi, bhavas, dinacharya and ritucharya, or hrid gati. The notes carry a Local sources line per block with these gaps.
- [ ] Find a named source for each block marked gap in the notes, and confirm the memorised sutra and sloka lists against the Board syllabus text. For application of knowledge and field experience ask the Board or an accredited institute what is assessed.
- [ ] Decide which guidebook copy to keep (the two files have identical text); the author removes the other, I do not delete.
- [ ] Deck corrections found while checking the notes (fix in `books/YCB1/workshop/ycb1_theory_texts.tex` when the deck is rebuilt from the notes): the Devanagari of Gita 2.49, 2.50 and 2.70 on the Gita frames is wrong (it is not those verses; use the checked text in the notes); the Yoga Sutra overview frame calls the sahabhuvas "accomplishments" (they are the companions of distraction: unhappiness, despair, trembling, irregular breath); the deck lists eleven principal Upanishads where the traditional commentary has ten; the first-aid frame gives the CPR depth as at least 5 cm where the Indian manual says 5 to 6 cm.
- [x] The Param Yoga study notes PDF now lives on the author's Desktop, outside the repository (cited in the notes References as candidate study notes). The two large instructor-book PDFs and the `.gdraw` file are still in `docs/` and still need the same decision.
- [x] A Google Drawings link file (`YCB Protocol Instructor.gdraw`) in `docs/` carries a Google account identifier and email. Keep it out of the public repository.
- [x] `docs/Yoga_Booklet.pdf` (the Board's 2019 booklet, third-party) joins the two guidebook PDFs: keep out of the public repository.
- [ ] Read the MDNIY monographs named in that booklet (sukshma vyayama, shatkarma, yogasana, pranayama) for the eight asanas still without a Board source, the sarvanga pushti and hrid gati rounds and cautions, and the hasta mudra forms. Findings so far: `../../../reports/ycb1_tools/open_sources_practical.md`.
- [x] Application of knowledge: no source describes what is assessed (only its 10 marks and one-hour limit). Ask the Board or an accredited institute. Findings: `../../../reports/ycb1_tools/open_sources_application.md`. Decided 2026-11-24: keep the honest wording (the Board names it and gives 10 marks, nothing more); revisit only if a Board or institute answer turns up.
- [ ] Check two FAQ answers set from an agent's own knowledge (Gita paths; kaivalya as asamprajnata samadhi) and the Sanskrit spellings of Yoga Sutra 1.23 to 1.29 and Gita 16.1 against a printed edition. Deck fix logs with their Needs source lists: `../../../reports/ycb1_tools/deck_fixes_*.md`.
- [ ] Ask one accredited training institute how many candidates sit Level 1 a year and what the trainees use to study.

## Decisions still open
- [x] Licence for this folder (separate from the CC BY-NC-SA of the deck repository, so the book can be sold) and a licence notice file. Done 2026-11-24: all rights reserved for the book, see `LICENSE_BOOK.md`; the copyright page is updated.
- [x] Route: self publish or Sakal. A Marathi edition only after an English draft and a demand check. Decided 2026-11-24: self publish first (print-ready PDF kept under the author's control); a publisher or a Marathi edition can follow the finished English draft.
- [x] Whether the book is LaTeX only or also exported from the notes (the Publications rule says LaTeX native publishers; ask the publisher before signing). Settled 2026-11-24 by the self-publish route: LaTeX only, no export from the notes.

## Foundations
- [ ] Write the design authority file: audience, promises, tone, safety rules, image policy, the syllabus-to-topic map.
- [ ] Map the deck frames to the notes blocks, frame by frame (the notes list only the seed topic file for now).
- [ ] Decide the book's folder layout (driver, chapter files named by topic, shared template) once the first chapter is about to be written; compile with XeTeX.

## Notes blocks (author reviews each; a certified teacher reviews the practical and health blocks)
- [ ] Theory: introduction to yoga and yogic practices.
- [ ] Theory: yoga texts (sutra and sloka lists confirmed against the Board syllabus first).
- [ ] Theory: yoga for health promotion (first aid, CPR, disorders: named current sources and a qualified reviewer).
- [ ] Practical: demonstration skills (cleansing, vyayama, surya namaskara, asanas, breathing, pranayama, bandha, mudra, meditation).
- [ ] Practical: teaching skills, application of knowledge, field experience.
- [ ] Exam and certification block checked against the Board guideline.
- [ ] Fact-check pass over every notes block (a gate: nothing flows to the deck or booklet from a block whose Fact check line is pending). Verify names, periods, numbers, Sanskrit text, steps, cautions, health statements and exam rules against primary or authoritative sources; note short variations where good sources differ. Rules in `AUTHORING.md`.
- [ ] Brevity pass: check every written block against the main principle (short, plain, complete to the syllabus, nothing outside it) and trim.
- [ ] Rewrite the question bank in `workshop/ycb1_theory_faqs.tex` into the Quiz and FAQ layers, in own words.

## Figures (see `docs/image_register.csv`)
- [ ] Generate each picture with the common system prompt (`docs/image_system_prompt.md`) plus its description; save under `images/new/`; uncomment the `% NEW-PIC` line in the deck so both show; review side by side; comment out the original only after approval.
- [ ] Trial: make three figures (one pose, one anatomy diagram, one vyayama pair) with the shared character sheet; fix the prompt wording; teacher check.
- [ ] Draw the diagrams in TikZ or Python (anatomy, kosha, chakra, prana, history, bandha, breathing, stick figures).
- [ ] Retype the table screenshots as LaTeX tables in own words; retire the exam screenshots.
- [ ] Generate the people figures in sets with one character sheet; teacher reviews every pose; for the printed book replace with own photographs or commissioned line art.
- [ ] Create `images/new/`; in the deck comment out the old picture line (never delete) and add the new one under it; update the register status; later move retired originals to a backup folder only when the author says.

## Derived outputs
- [ ] Re-author the deck frames from the notes (text that follows a web page or the guidebook closely must be rewritten); keep the deck compiling after each batch.
- [ ] Draft the booklet from the checked notes blocks: short, plain, one idea per line, complete to the syllabus, with quick checks and exam-style questions. Cut anything that does not help a student pass.
- [ ] Mock exam and answer key.
- [ ] One compile batch, page review, `/verify-pdf`, then the publisher or self-publish route.

## Records
- [ ] Keep `README.md` and `Publications/TODO.md` in step with each change; the author copies the YCB lines into Google Keep.
