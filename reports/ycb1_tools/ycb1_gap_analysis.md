# YCB1 gap analysis: notes, workshop, book (2026-11-24)

Read-only analysis. Nothing in the notes, deck or book was changed. Measuring scripts are in the session scratchpad (`gap.py`, `frames.py`); a permanent version becomes the coverage check (task A below).

## Findings

### 1. The book carries a small part of the notes

Word counts (words of text, rough):

| Layer | Words |
|---|---|
| Notes Material (all blocks) | about 30,000 |
| Notes Workshop slide content (folded deck layer) | about 22,000 |
| Notes Quiz, Exercises and FAQ | about 16,700 |
| Notes Worked examples | about 3,200 |
| Book, all content chapters together | about 12,000 |

- The book holds only blocks marked `Fact check: checked` (12 blocks): guiding principles, the Yoga Sutra, the Gita, Prasthanatrayi, hatha practices and health, mental well-being, bahiranga and antaranga, first aid and CPR, preparation for a class, factors influencing teaching, field experience, and the exam. Teaching, Hatha and mental-wellbeing blocks sit inside the "Teaching a Yoga Class" and "The Yoga Texts" chapters.
- All 40 pending blocks have no book text at all. They hold most of the volume and almost the whole practical syllabus: yogasana (the largest block, about 3,000 words of Material), the human body, stress, Hatha Pradipika, pranayama, sukshma and sthula vyayama, surya namaskara, cleansing, mudra, bandha, prayer, meditation, the remaining teaching blocks, diet, dinacharya and ritucharya, and the whole opening theory (definitions, history, schools, triguna and koshas).
- The book is therefore thinner than the deck, as the author saw: the deck has frames for these topics, the book has none.
- The cause is the fact-check gate plus the open decision in `TODO.md` (pending blocks: write unverified text, or leave a stub). Recommendation below.

### 2. Notes versus deck are mostly in step

- Almost every deck frame title is found in the notes (the notes' folded Workshop slide content layer, or later sync). A title check found about 25 live non-FAQ frame titles not in the notes, all frames added or renamed in the recent deck syncs (for example "On the Exam Day", "CPR: Doing It Well", "Functions of Circulatory System", "The Twelve Sutras in Order"). The 61 unmatched FAQ titles are the generic "Question N" frames.
- This is a title match only. A frame-by-frame content match (is every bullet of the frame in the notes?) has not been done and is part of task A.
- Reverse direction: the Material of the checked blocks holds points the deck does not (deck is shorter), which is fine; the unchecked deck-derived bullets are labelled "deck, not yet checked".

### 3. Images

- Deck: about 230 picture lines in the deck sources. The image register lists 118 original figures: 41 pose photos, 27 anatomy web diagrams, 12 illustrations, 11 concept diagrams, 10 table screenshots, 5 stick figures, 5 class photos, 5 vintage photos and a few others. All are status `planned` and all have a generated prompt (system prompt in `docs/image_system_prompt.md`).
- Book: no pictures at all (only a logo on the title page).
- Notes: only 21 blocks have a Figures list; other blocks say "none yet" even though the deck pictures belong to them (for example the yogasana block has the prompts, the sukshma vyayama block has them, but the Figures lines in every block must be checked against the register).
- Your rule asks: the same images in the book as in the workshop, with the prompt under each; only the prompt in the notes.
- Conflict to decide: 89 of the 118 originals are marked high risk in the register (web diagrams with publisher marks, third-party photos, exam screenshots), and the book is all rights reserved and meant to be sold. Original images cannot go into the book as they are. Options: (a) book carries the generated or redrawn replacement under the same register ID, with the prompt under it, and the original stays in the deck only; (b) book carries the original for the low and medium risk items and a placeholder box with the prompt for the high risk ones, until the replacement is generated.
- Table screenshots (10): retype as LaTeX tables rather than carry as pictures.

## Tasks (numbered for your confirmation)

A. Build the coverage check script and report in `reports/ycb1_tools/`: notes block to deck frames (by the folded layer and by the register's frame titles) to book chapter; word counts per layer; gaps in both directions; a figure check (register ID in notes Figures, in deck, in book). Read-only. Acceptance test for everything below.

B. Fix the notes first so they are the master: every block gets its Figures list from the register (prompt only, no picture, original file name as text), blocks with deck pictures but "none yet" are corrected, the 25 deck frames not in the notes are added, and the notes follow the Board syllabus order and topic names (check the Level 1 syllabus topic by topic).

C. Decide the pending-block policy for the book (see Decision 1) and fold the Workshop slide content and Open conflicts layers into proper Material, so a block is ready to be written out.

D. Write the book prose, chapter by chapter in syllabus order: each chapter carries all of its block's Material, Explanation, Worked examples, Exercises, Quiz and FAQ as full text, but compact (no repeating the same point in several layers; quick recall and check-yourself kept short). Order of work: the practical unit first (largest gap), then health, then the opening theory, then the remaining teaching blocks.

E. Figures in the book: for each register ID, a figure in the chapter with the prompt as a small italic line below; the notes keep only the prompt. Table screenshots retyped as tables.

F. Run the coverage check, compile the book and decks once, run `/verify-pdf`, refresh the ToPrint copies.

## Decisions for you (one at a time)

1. Pending blocks in the book: write the text from the pending Material, clearly labelled unverified in each chapter opening (recommended; it gives you the complete book now and the label comes off as each block is checked), or leave a stub until checked.
2. Images in the book: carry the register replacements with the prompt below (recommended), or originals where the risk is low and placeholders for the rest.
3. Which model: Sonnet is enough for tasks A, B, C and E (mechanical, script-driven). The prose in task D is the part that benefits from Opus (verbose but compact writing and the judgment on what to cut).

## Size estimate (for "not bulky")

The book at the notes' Material level would be about 30,000 words of core text plus worked examples and a trimmed question set, roughly 150 to 180 book pages with figures. The present 67 pages hold about 12,000 words. Keep the Quiz and FAQ to the items the Material answers, and fold the Open conflicts layer away (it is for the author, not the reader).
