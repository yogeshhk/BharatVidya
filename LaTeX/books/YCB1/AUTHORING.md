# AUTHORING: YCB Level 1 exam-guide booklet

Working rules for this folder. The BharatVidya `CLAUDE.md` applies as well (XeTeX, no git commands, no CI, no em dashes, compile once per batch).

## Main principle
An easy-to-use exam guide, a small booklet, not a second textbook. The official guidebook is long, formal and hard to study from; this is the opposite. Short notes in plain words, one idea per line, no padding. Complete to the dot against the Board's Level 1 syllabus: every syllabus topic is covered and nothing outside it is added. Exam first: what to know, remember and do; a student can revise a topic in a few minutes. The same short notes feed the deck, the cheat sheet and the booklet. If a block is too long for a page, cut it. The principle is also stated at the top of `docs/Notes YCB1.md`.

## Fact-check pass (a gate)
All content lives in the notes and flows down from them, so the notes must be right before anything flows. Every block has a `Fact check` line: `pending` or `checked`. Nothing is carried to the deck, cheat sheet or booklet from a block that is still pending.
- Check every claim that can be wrong: names and attributions, dates and periods, numbers, Sanskrit text and transliteration, definitions, steps and cautions of a practice, health statements, and every exam rule, mark and fee-related fact.
- Check against a primary or an authoritative source (the Board's own documents, the primary text in a standard edition, a government health source), and a second source where the first is a secondary one. The reference documents in `docs/` are useful but are not the only check, and the old-scheme guidebook never settles an exam rule.
- Where reliable sources differ and a student could be asked, record the variations in one short line (for example two common spellings, two accepted counts, two forms of a practice) and say which one the exam follows. Do not write a research survey: keep it to what a candidate must know.
- When a claim cannot be verified, remove it or mark it clearly as unverified; never leave it looking certain. Health and first-aid content also needs a qualified reviewer.
- A block flips to `checked` only after the pass. Re-check a block whenever its facts change. A time-sensitive fact is re-read before use.

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

## Workshop slide content in the notes
The notes are the universal golden source, so everything the current workshop deck says is also in the notes. Each block carries a layer called Workshop slide content, merged from the deck frames as the starting point, with the deck's own source lines kept. The deck's question bank is merged into the FAQ layers (and an unassigned bank at the end of the notes file). Work on these layers in order: structure the content into Material, Explanation and the other layers; check each fact against a named source; rewrite in own words wherever a slide follows a web page or the guidebook closely; then delete the merged layer from that block. Nothing in a merged layer flows down until its block is `checked`.

## Figures
- The register is `docs/image_register.csv`: current file, prompt or brief, planned final name and path, type, risk, uses. Keep it in step with the deck.
- Never delete an image or an `\includegraphics` line. When a replacement exists, comment out the old line with `%` and add the new line directly under it, and update the register status. Retired originals move to a backup folder only when the author says.
- Original and prompt together: the original picture stays as it is in the deck, with its prompt directly below it (a `% PROMPT` comment). The notes file holds no pictures, only the original file name and the prompt as text. The common system prompt is written once in `docs/image_system_prompt.md`; only the per-picture description changes. After generation, save the new file under `workshops/YCB1/images/new/`, uncomment the `% NEW-PIC` line so both pictures show together, review side by side, and only after approval comment out the original (never delete it).
- Every picture line in the deck has a comment above it: `% FIG <figure ID> | now: ... | final: ... | register: ...`. Keep it when editing.
- People figures: one shared character sheet in every prompt (it is written in the notes file). AI drafts are for the deck; for the printed book use own photographs with a release, or commissioned line art, because the copyright status of generated images is unsettled and poses are often anatomically wrong. Check every generated pose against the syllabus.
- Diagrams are drawn in TikZ or Python, simple, labelled, readable in grayscale, never by colour alone. Images go in the family `images/` folder, no spaces in file names.

## Style
No em dashes or long dashes in generated content. No hard-typed chapter, section, table or figure numbers or counts of chapters or sections: refer to a topic by name; in LaTeX use `\label` and `\ref`. Name files by topic only; the order lives in the content driver. No one-line paragraphs in prose. Every chapter opens with a plain italic, question-led paragraph. Learner-facing text: one term per concept, short imperative steps, about 20 words per bullet.

## Licence and publishing
The deck repository is CC BY-NC-SA for content. The book needs its own licence notice so it can be sold; the choice is open (see `TODO.md`). Do not send the book to a publisher, or any draft outside this machine, without the author. A publisher that is LaTeX native is preferred; ask before signing.

## Records
When this folder changes, update `README.md` and `TODO.md` in the same pass. The Publications entry is in `D:\Yogesh\GitHub\Publications\TODO.md` and `KEEP_NOTES.md`; the author copies the lines into Google Keep.
