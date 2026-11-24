# YCB Level 1 textbook: analysis and proposal

Read-only analysis. Nothing in the deck, the images or any other repo was changed. Status of each claim is marked
as verified (read in a file or an official page), reported (a search summary, not opened) or open.

## Purpose and verdict in one paragraph

A self-authored textbook for the Yoga Certification Board Level 1 exam (Yoga Protocol Instructor), built from a
concept layer that feeds a slide deck and a book, the way the QCNP book is built. The syllabus is fixed by the
Board, the deck already covers every syllabus area, and the main work is turning a compiled deck into original,
copyright-clean prose and diagrams. As a revenue project the market evidence is thin. As a workshop companion
and a credibility piece it is sound and cheap, if the image and text rework is done properly. Recommendation:
go, but bounded, and only after two open checks (the current Board syllabus and the official guidebook).

## 1. What the syllabus asks for (verified, local copy and Board guideline)

- Level 1 is the entry level: Yoga Protocol Instructor. Total 200 marks: theory 60 (three units of 20) and
  practical 140 (demonstration 80, teaching skills 40, application of knowledge 10, field experience 10).
- Theory units: introduction to yoga and yogic practices; introduction to yoga texts; yoga for health promotion.
  Each has ten sub-topics.
- Practical: prayer; cleansing (dhauti, neti, kapalabhati); sukshma and sthula vyayama; surya namaskara; a list of
  asanas; sectional and deep breathing; pranayama; bandhas; mudras; meditation practices; plus a teaching-methods
  block (lesson plan, groups, class management, precautions, ideal instructor).
- Board guideline (version 0.3, read): pass needs 70 percent in theory and in practical separately; up to 5
  percent grace in one of them; certificate validity 5 years. The deck's exam frame matches this (it cites version 0.2).
- The syllabus copy kept in the repo carries a private institute's contact footer (a person's name and phone
  number on every page). It is not a clean Board file. Replace it with the Board's own download before anything
  is cited from it.

## 2. What is open on the syllabus (honest gaps)

- Current version: I found no dated Board notice of a revised Level 1 syllabus. The Board posted a January 2026
  circular on validity extensions for Level 1 holders (it is a list of named certificate holders; not syllabus).
  The syllabus text I could read is the older one. Open: confirm on the Board site before writing.
- The official application-of-knowledge and field-experience content is not in the Board guideline. The deck's own
  TODO already says the guidebook must be read for these. Open.
- The sutra and sloka memorisation list (Yoga Sutra opening verses, selected Gita verses) is re-checked against the
  syllabus only in the older text. Open.
- The Board's Special CYEP route lets Level 1 and Level 2 holders upgrade; a textbook should say levels 2 and 3 exist
  and are out of scope.

## 3. The current deck (verified)

- Workshop deck: Presentation about 380 pages, CheatSheet about 57 pages, each about 10 MB (image heavy).
- Content chain: overview, theory (intro, texts, health), practical (demonstration, asanas, teaching skills,
  application, field experience), exam, references. A large FAQ file (about 1,800 lines) is deliberately not
  included in the build; it is a question bank for practice.
- Strengths: full syllabus coverage, Devanagari text with transliteration, exam rules, a question bank.
- Weaknesses for a book: slide-sized fragments, many frames are summaries of web pages, no Predict/Check style
  practice, no worked teaching plans in prose, no consistent diagram language.

## 4. Text provenance (verified by grep of the Ref lines)

The deck cites its sources in small print. The main ones: the official Level 1 guidebook (the most cited, dozens of
frames), the Board guidebook again, several commercial and personal yoga-school web pages, a 30-day yoga blog
series, and a long tail of general anatomy and biology web pages (educational sites, encyclopaedias, a
university site). Consequences:

- Slide text that follows a web page or the guidebook closely cannot go into a book. Every section needs to be
  re-authored from the syllabus plus primary texts (Yoga Sutra, Gita, Hatha Pradipika, which are public domain
  as texts; modern translations are not), in own words.
- The official guidebook is the likely closest competitor and the likely source of the exam questions. Use it to
  check coverage, never to copy.
- Commercial yoga-school pages are the weakest sources. Replace them with textbooks and peer-reviewed or
  government sources.

## 5. Images (verified inventory; classification by eye from contact sheets)

91 files named with the YCB1 prefix, about 117 uses across the topic files, none credited. By type:

| Type | Typical examples | Risk | Replacement route |
|---|---|---|---|
| Asana and kriya photographs of models | most single-pose frames | High: stock or yoga-school photographs | New figures (see below) |
| Vintage black-and-white teacher photographs | sukshma and sthula frames | High: scanned from a book or site | New figures |
| Group and class photographs | teaching skills frames | High | Own photographs of own classes, or illustration |
| Anatomy and physiology diagrams | breathing, muscles, joints, body systems | Medium to high: copied from web and textbooks | Own diagrams (TikZ or Python); simple and labelled |
| Philosophy diagrams | kosha, chakra, prana, history timeline, hand mudras | Medium | Own diagrams; mudras need figures |
| Screenshots of tables and exam pages | asana benefit tables, exam screenshots | High and not needed | Retype as tables in own words; drop the exam screenshots |
| Icons and clip art | teaching icon | Low to medium | Own simple icons |

The three groups that do not need a person (anatomy, philosophy, tables) can become diagrams or typeset tables.
The people-in-pose figures cannot; see section 9.

## 6. Competing and adjacent material (reported by search, not opened)

- The Board's own official guidebook for Level 1, published by a commercial publisher in 2016 and listed again for
  2017. Probably the strongest competitor and the likely basis of the exam.
- At least one private paperback for the Level 1 exam (listed around 2021) and an Exotic India listing of a
  compiled study guide. Practice-test courses on Udemy. Many free video playlists (several already in the deck's
  reference frame).
- No data found on sales, Amazon ratings or the number of exam candidates. Market sizing is open.

## 7. Market (reported, mostly weak)

- The Board's public page, captured June 2025, reports about 43,563 certified yoga professionals (1,470 overseas),
  more than 100 accredited training institutions and 26 certification bodies. That is the best figure found. It
  counts certified people across levels, not exam candidates or likely book buyers.
- Market-research reports put the Indian yoga market in the billions of dollars, with growth around 10 to 12 percent,
  but the three firms disagree widely on scope. They say nothing about exam-guide books. An old industry-body claim of a
  shortage of about 300,000 instructors is a 2014-era figure.
- Honest read: a niche. Buyers are trainees on 200-hour courses and people sitting the exam, who also have free video
  and an official guidebook. Likely sales are modest. A language edition (Marathi through Sakal) may reach students
  the English guides do not; this is a hypothesis, not evidence. Open: ask one accredited institute how many
  candidates a year and what they use.

## 8. Fit with the author's plans (verified in local files)

- The 2027 career plan puts the yoga pillar third: read first, then build workshops, books last. The yoga
  certification workshop is the deck itself.
- Publications TODO says no new projects except AutoBio around 2033, with the 2027 quantum textbook as the one
  exception. A yoga textbook would be a second exception, so it needs the author's explicit decision.
- The Publications Keep file is a paste of the author's Google Keep and Keep wins; an entry belongs in Keep first,
  then is synced into `KEEP_NOTES.md` and `TODO.md`. Nothing was added there.
- BharatVidya repo rules: licence CC BY-NC-SA for content, third-party material excluded, personal items flag-only,
  no CI. A book for sale does not sit comfortably in a non-commercial licence; the licence for the book folder
  must be decided before it is created.
- Cheap path: the book reuses the deck's structure, and the deck is the workshop; the book adds prose, diagrams,
  practice questions and teaching plans.

## 9. Proposed arrangement, modelled on QCNP

Same one-way chain, adapted to a syllabus-driven book (the notes-first rule used for the quantum courses fits
better than the book-as-golden rule, because the Board syllabus is the external spec).

1. **Design authority** (one Markdown file, like the QCNP Mental Model): audience, promises, the learner's
   exam journey, tone, the safety rules, the image policy, and the syllabus-to-book map by topic name.
2. **Notes** (Markdown, pure portable content, one block per syllabus topic with a stable ID): scope, explanation,
   checks, exercises, quiz questions, safety notes, references. No dates, no paths, no model names. Reviewed by
   the author and, ideally, a certified instructor.
3. **Deck stubs** derived from the notes (the current deck is the seed, not the authority).
4. **Book** derived from the notes: chapters per syllabus area, each opening with a question, with practice,
   teaching-plan examples and exam-style questions.
5. **Cheat sheet** inherits the deck.

Folder: a new books area next to the decks in BharatVidya, with its own README, TODO and authoring notes. The
decision on where it lives (BharatVidya or Publications) is open.

Safety rule that must be in the design authority: asana, pranayama and kriya instructions are health-adjacent.
Contraindications come from named sources and are reviewed by a certified teacher before print. Nothing implies
diagnosis or cure.

## 10. Image plan (nothing deleted)

Principle: every current `\includegraphics` stays in the file. When the replacement exists, comment the old line and
add the new one directly under it, with a marker such as `% IMG-REPLACED: old file, date`. Old files stay in
`images/`; they are later moved to a backup folder only when the author says.

1. Build an image register (CSV, one row per use: file, frame, type, apparent source, risk, replacement route, new
   file name, status). Dry run first; no edits.
2. Diagrams (anatomy, kosha, chakra, prana, history, tables): drawn in TikZ or Python, simple, labelled, readable in
   grayscale. These are the cheapest and fully owned.
3. People-in-pose figures: three routes.
   - Own photographs of a certified teacher or model, with a signed release: cleanest legally and best for form.
   - Line-art figures drawn by an illustrator.
   - AI-generated figures from a ChatGPT or Gemini prompt set. Cheapest, but: the copyright status of generated
     images differs by country and is unsettled; anatomical errors in poses (hands, joints, spine) are common and
     matter here; consistency across sixty poses is hard. If used, give each prompt the same character sheet,
     review every figure against the syllabus pose, and have a teacher check them. I would use AI figures for early
     drafts and the workshop deck, and photographs or commissioned line art for the printed book.
4. Table screenshots and exam screenshots: retype and drop.
5. Keep a source line for each new figure in the register.

## 11. Effort and phases (no dates; order only)

1. Close the open checks: Board syllabus current text, official guidebook read, candidate numbers from one institute.
2. Decide: go or no-go, location, licence, language plan.
3. Write the design authority and the topic map; register all images.
4. Notes for theory units; review; deck stubs; book chapters.
5. Notes for practical units; the figure set; review by a teacher.
6. Practice questions bank (the unused FAQ file is a seed, to be rewritten), mock exam.
7. One compile batch, page review, publisher or self-publish route.

## 12. Decisions needed from the author, one at a time

1. Go, no-go or wait until the two open checks are done.
2. Home of the project (BharatVidya or Publications) and its licence.
3. Notes-first (recommended) or book-first as the golden source.
4. Image route for the people figures (own photographs, commissioned line art or AI figures).
5. Language plan (English first, or Marathi through Sakal first).
6. Whether to add a Keep line, and the matching entry in the Publications TODO.

## Sources

- Board documents read: guideline for yoga professionals, version 0.3; a January 2026 validity circular.
  Official site: yogacertificationboard.nic.in.
- Search results, not opened in full: Board brochure and certified-professionals count; the Exotic India and Blackwell's
  listings of Level 1 guides; Grand View Research, Expert Market Research and Future Market Insights summaries of
  the Indian yoga market; a Gulf News report of the industry-body shortage claim; the Assam AYUSH and Ministry of
  Education IKS licence pages.
- No Ministry of AYUSH copyright page was found. Reuse terms for Board and Ministry material are open.
