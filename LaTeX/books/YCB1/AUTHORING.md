# AUTHORING: YCB Level 1 textbook

Working rules for this folder. The BharatVidya `CLAUDE.md` applies as well (XeTeX, no git commands, no CI, no em dashes, compile once per batch).

## The chain
Notes first, then deck, cheat sheet and book. The master is `docs/Notes YCB1.md`. A fact, point, exercise, figure or quiz item is fixed in the notes first and carried down by hand with the author's confirmation. Presentation-only choices (layout, a diagram style, audience wording) stay in the deck. The deck is a seed for the notes, never an authority: where they disagree, the notes win.

## Notes block format
Each block has a stable ID (`ycb1-` and a topic slug; never renamed), a Review status and an Additions status, then Scope, Material, Explanation, Worked examples, Figures, Exercises, Quiz, FAQ, References and Videos. `Review: pending` is the normal state; do not mark a block reviewed yourself. A new factual point added while authoring sets `Additions: pending`. Match on the ID, never on the heading text. A layer that is not yet written says "to be written".

Unlike the quantum course notes, this notes file lists figure paths in the Figures layer, because the author wants each picture traceable from the notes to the deck. Keep that line in the form: figure ID, now (current path), final (planned path).

## Sources and own words
- Write every section in own words from named sources. Do not copy a web page, a slide, a screenshot or the official guidebook. The syllabus topic list is the spec; the Board's wording is not reproduced beyond short topic names.
- Source order: the Board's own documents, primary texts (Yoga Sutra, Gita, Hatha Pradipika; modern translations are copyrighted, cite and paraphrase), textbooks, then government health sources for health content. Never a commercial yoga-school page as the only source.
- Prefer a dateless, qualitative claim over a specific number unless the number is the point. Re-read time-sensitive facts (exam fees, validity, rules) before use; do not stamp them with a read date in the notes.

## Safety
Asana, pranayama, kriya and health content is health-adjacent. Give the form, cautions and contraindications from a named source. A certified teacher reviews every pose, breathing practice and kriya, in text and in figure, before print, and a qualified reviewer checks first aid, CPR and disorder content. Say "prevention and well-being", never diagnosis or cure.

## Figures
- The register is `docs/image_register.csv`: current file, prompt or brief, planned final name and path, type, risk, uses. Keep it in step with the deck.
- Never delete an image or an `\includegraphics` line. When a replacement exists, comment out the old line with `%` and add the new line directly under it, and update the register status. Retired originals move to a backup folder only when the author says.
- Every picture line in the deck has a comment above it: `% FIG <figure ID> | now: ... | final: ... | register: ...`. Keep it when editing.
- People figures: one shared character sheet in every prompt (it is written in the notes file). AI drafts are for the deck; for the printed book use own photographs with a release, or commissioned line art, because the copyright status of generated images is unsettled and poses are often anatomically wrong. Check every generated pose against the syllabus.
- Diagrams are drawn in TikZ or Python, simple, labelled, readable in grayscale, never by colour alone. Images go in the family `images/` folder, no spaces in file names.

## Style
No em dashes or long dashes in generated content. No hard-typed chapter, section, table or figure numbers or counts of chapters or sections: refer to a topic by name; in LaTeX use `\label` and `\ref`. Name files by topic only; the order lives in the content driver. No one-line paragraphs in prose. Every chapter opens with a plain italic, question-led paragraph. Learner-facing text: one term per concept, short imperative steps, about 20 words per bullet.

## Licence and publishing
The deck repository is CC BY-NC-SA for content. The book needs its own licence notice so it can be sold; the choice is open (see `TODO.md`). Do not send the book to a publisher, or any draft outside this machine, without the author. A publisher that is LaTeX native is preferred; ask before signing.

## Records
When this folder changes, update `README.md` and `TODO.md` in the same pass. The Publications entry is in `D:\Yogesh\GitHub\Publications\TODO.md` and `KEEP_NOTES.md`; the author copies the lines into Google Keep.
