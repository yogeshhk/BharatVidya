# TODO: YCB Level 1 textbook

Open actions only, terse. Rules live in `AUTHORING.md`, status in `README.md`. Work one task at a time, in this order; the author confirms before each.

## Close the open checks (before any chapter text)
- [ ] Download the Board's own current Level 1 syllabus from yogacertificationboard.nic.in and replace the local copy in `docs/` (the current copy carries a private institute's contact footer). Check whether the Board has revised the syllabus, the marks or the exam rules since version 0.3 of its guideline.
- [ ] Keep the two large instructor-book PDFs in `docs/` out of the public repository (decide: ignore pattern in `.gitignore`, or move them to the private Drive). The BharatVidya policy says third-party books are not hosted here.
- [x] Read the guidebook in `docs/` (two copies, identical text). Result: it belongs to the older four-level scheme, not to the current Yoga Protocol Instructor syllabus. It has no content for application of knowledge or field experience, and no dedicated section on the Gita, Prasthanatrayi, bhavas, dinacharya and ritucharya, or hrid gati. The notes carry a Local sources line per block with these gaps.
- [ ] Find a named source for each block marked gap in the notes, and confirm the memorised sutra and sloka lists against the Board syllabus text. For application of knowledge and field experience ask the Board or an accredited institute what is assessed.
- [ ] Decide which guidebook copy to keep (the two files have identical text); the author removes the other, I do not delete.
- [ ] Deck corrections found while checking the notes (fix in `workshops/YCB1/ycb1_theory_texts.tex` when the deck is rebuilt from the notes): the Devanagari of Gita 2.49, 2.50 and 2.70 on the Gita frames is wrong (it is not those verses; use the checked text in the notes); the Yoga Sutra overview frame calls the sahabhuvas "accomplishments" (they are the companions of distraction: unhappiness, despair, trembling, irregular breath); the deck lists eleven principal Upanishads where the traditional commentary has ten; the first-aid frame gives the CPR depth as at least 5 cm where the Indian manual says 5 to 6 cm.
- [x] The Param Yoga study notes PDF now lives on the author's Desktop, outside the repository (cited in the notes References as candidate study notes). The two large instructor-book PDFs and the `.gdraw` file are still in `docs/` and still need the same decision.
- [ ] A Google Drawings link file (`YCB Protocol Instructor.gdraw`) in `docs/` carries a Google account identifier and email. Keep it out of the public repository.
- [ ] Ask one accredited training institute how many candidates sit Level 1 a year and what the trainees use to study.

## Decisions still open
- [ ] Licence for this folder (separate from the CC BY-NC-SA of the deck repository, so the book can be sold) and a licence notice file.
- [ ] Route: self publish or Sakal. A Marathi edition only after an English draft and a demand check.
- [ ] Whether the book is LaTeX only or also exported from the notes (the Publications rule says LaTeX native publishers; ask the publisher before signing).

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
- [ ] Rewrite the question bank in `../../workshops/YCB1/ycb1_theory_faqs.tex` into the Quiz and FAQ layers, in own words.

## Figures (see `docs/image_register.csv`)
- [ ] Generate each picture with the common system prompt (`docs/image_system_prompt.md`) plus its description; save under `../../workshops/YCB1/images/new/`; uncomment the `% NEW-PIC` line in the deck so both show; review side by side; comment out the original only after approval.
- [ ] Trial: make three figures (one pose, one anatomy diagram, one vyayama pair) with the shared character sheet; fix the prompt wording; teacher check.
- [ ] Draw the diagrams in TikZ or Python (anatomy, kosha, chakra, prana, history, bandha, breathing, stick figures).
- [ ] Retype the table screenshots as LaTeX tables in own words; retire the exam screenshots.
- [ ] Generate the people figures in sets with one character sheet; teacher reviews every pose; for the printed book replace with own photographs or commissioned line art.
- [ ] Create `../../workshops/YCB1/images/new/`; in the deck comment out the old picture line (never delete) and add the new one under it; update the register status; later move retired originals to a backup folder only when the author says.

## Derived outputs
- [ ] Re-author the deck frames from the notes (text that follows a web page or the guidebook closely must be rewritten); keep the deck compiling after each batch.
- [ ] Draft the booklet from the checked notes blocks: short, plain, one idea per line, complete to the syllabus, with quick checks and exam-style questions. Cut anything that does not help a student pass.
- [ ] Mock exam and answer key.
- [ ] One compile batch, page review, `/verify-pdf`, then the publisher or self-publish route.

## Records
- [ ] Keep `README.md` and `Publications/TODO.md` in step with each change; the author copies the YCB lines into Google Keep.
