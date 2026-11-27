# DESIGN.md: YCB Level 1 yoga textbook

The design authority for this book: who it is for, what it promises, how it sounds, the safety and image rules, and
which syllabus topic lives in which notes block and chapter. The working rules (notes first, fact-check gate, own
words) are in `../AUTHORING.md`; the content is in `Notes YCB1.md`. When this file and `AUTHORING.md` disagree,
`AUTHORING.md` wins and this file is corrected.

## Decisions (do not reopen without the author)

- **D1 Audience.** Candidates for the Yoga Certification Board's Level 1 certificate (Yoga Protocol Instructor):
  adults with a regular practice who want to teach the common protocol. No background in anatomy, Sanskrit or
  philosophy is assumed. A secondary reader is a workshop participant who uses the book after the author's workshop.
- **D2 Promise.** An easy-to-use textbook for the exam. The official guidebook is long, formal and hard to study
  from; this book is the opposite. It covers every topic of the Board's Level 1 syllabus and nothing outside it,
  and a student can revise any topic in a few minutes.
- **D3 Scope.** The Board's Level 1 syllabus is the spec: theory (introduction to yoga, yoga texts, yoga for health
  promotion), practical (demonstration skills, teaching skills, application of knowledge, field experience) and the
  exam. The guidebook for the older four-level scheme is a coverage check only and never settles an exam rule.
- **D4 Origin.** `Notes YCB1.md` is the master. Two things are derived from it by hand: the workshop (deck and cheat
  sheet in `../workshop/`) and the textbook (`../book/`). Nothing propagates automatically.
- **D5 Licence and route.** The textbook is all rights reserved (`../LICENSE_BOOK.md`); the deck repository is
  CC BY-NC-SA. English first; self publish first; Sakal or a Marathi edition only after the English draft and a
  demand check. A Word export is acceptable to a publisher.
- **D6 Name.** Folder `YCB1`; the book is called a textbook (not a guide or a manual).
- **D7 Status labels.** A chapter written from a block whose fact check is pending opens with a "Not yet
  fact-checked" box; only the author marks a block checked. The person-only checks (Board, MDNIY monograph,
  certified teacher, first-aid reviewer) are no longer tracked (author, 2026-11-27); their blocks keep the box.

## Reader contract

The reader can read plain English and has practised yoga. Every Sanskrit term is given in Roman letters with its
English meaning the first time it appears in a chapter. Devanagari appears only for the texts the syllabus asks the
candidate to recite (the selected sutras and slokas, the prayers). Anatomy is kept to what a teacher needs to explain
a posture, a breath or a caution.

## Voice and tone

- Plain, short and direct: one idea per line, about 20 words per bullet, short imperative steps for practices.
- State the point, not who said it. Name a source in the text only where sources differ, where a claim is a
  tradition, or where the exam follows one reading (review finding F3). Every chapter closes with a Sources
  paragraph.
- Every chapter opens with a plain italic, question-led paragraph.
- One term per concept across the book, deck and notes.
- No em dashes or long dashes. No hard-typed chapter, section, table or figure numbers; refer by name.
- Instructions to the writer never print as instructions to the student (review finding F4).

## Safety rules

- Say "prevention and well-being" or "supportive practice"; never diagnosis, treatment or cure.
- Traditional claims (for example from the Hatha Pradipika) are labelled as the text's own claim.
- Every asana, pranayama and kriya gives its form, cautions and contraindications from a named source.
- First aid and CPR follow the Indian First Aid Manual; a qualified reviewer checks them before print.
- A certified teacher reviews every pose, breathing practice and kriya, in text and in figure, before print.
- Third-party tables or pictures that make cure claims are dropped, not retyped (the asana-benefit screenshots,
  2026-11-27).

## Image policy

- The register `image_register.csv` holds one row per picture: current file, brief or prompt, planned final file,
  type, risk and status (`planned`, `drawn`, `retyped_table`, `dropped`).
- Diagrams are drawn in TikZ or Python, simple, labelled and readable in black and white; never mark meaning by
  colour alone.
- Pictures of people: AI drafts are for the deck only. The printed book uses own photographs with a release, or
  commissioned line art, with one shared character sheet (`image_system_prompt.md`).
- Screenshots of tables are retyped as LaTeX tables in own words from the checked notes, or dropped.
- Never delete an original picture or its `\includegraphics` line; comment it out under its replacement.

## Book anatomy

- **Front matter:** title pages, how to use the book, initial pages (`ycb1_book_initialpages.tex`).
- **Each chapter:** italic question-led opener; the "Not yet fact-checked" box where its blocks are pending; the
  content in short sections; a recall box; exercises and FAQ; a Sources paragraph.
- **Back matter:** references appendix. A mock exam with an answer key is drafted in the notes (end section) and is
  carried into the book only with the author's confirmation.

## Syllabus-to-topic map

Order follows the Board's syllabus; the chapter order itself lives only in `../book/book_ycb1_content.tex`.

| Syllabus unit | Notes block ID | Chapter file |
|---|---|---|
| Introduction to yoga and yogic practices | `ycb1-th-etymology-definitions-aim` | `ycb1_book_meaning-history.tex` |
| | `ycb1-th-origin-history-development` | `ycb1_book_meaning-history.tex` |
| | `ycb1-th-guiding-principles-practitioners` | `ycb1_book_guiding-principles.tex` |
| | `ycb1-th-principles-of-yoga` | `ycb1_book_principles-schools.tex` |
| | `ycb1-th-major-schools` | `ycb1_book_principles-schools.tex` |
| | `ycb1-th-practices-for-health` | `ycb1_book_practices-intro.tex` |
| | `ycb1-th-shatkarma-introduction` | `ycb1_book_practices-intro.tex` |
| | `ycb1-th-vyayama-surya-namaskara-introduction` | `ycb1_book_practices-intro.tex` |
| | `ycb1-th-yogasana-introduction` | `ycb1_book_practices-intro.tex` |
| | `ycb1-th-pranayama-dhyana-introduction` | `ycb1_book_practices-intro.tex` |
| Introduction to yoga texts | `ycb1-tx-patanjala-yoga-sutra` | `ycb1_book_texts.tex` |
| | `ycb1-tx-bhagavad-gita` | `ycb1_book_texts.tex` |
| | `ycb1-tx-hatha-pradipika` | `ycb1_book_hatha-diet-living.tex` |
| | `ycb1-tx-prasthanatrayi` | `ycb1_book_texts.tex` |
| | `ycb1-tx-aahara-diet` | `ycb1_book_hatha-diet-living.tex` |
| | `ycb1-tx-hatha-practices-health` | `ycb1_book_texts.tex` |
| | `ycb1-tx-mental-wellbeing-patanjala` | `ycb1_book_texts.tex` |
| | `ycb1-tx-bahiranga-antaranga` | `ycb1_book_texts.tex` |
| | `ycb1-tx-healthy-living-gita` | `ycb1_book_hatha-diet-living.tex` |
| | `ycb1-tx-subjective-experience` | `ycb1_book_hatha-diet-living.tex` |
| Yoga for health promotion | `ycb1-hl-human-body-introduction` | `ycb1_book_human-body.tex` |
| | `ycb1-hl-health-promotion-role-of-yoga` | `ycb1_book_health-promotion.tex` |
| | `ycb1-hl-positive-attitudes` | `ycb1_book_health-promotion.tex` |
| | `ycb1-hl-bhavas` | `ycb1_book_health-promotion.tex` |
| | `ycb1-hl-dinacharya-ritucharya` | `ycb1_book_lifestyle-stress.tex` |
| | `ycb1-hl-holistic-approach` | `ycb1_book_health-promotion.tex` |
| | `ycb1-hl-first-aid-cpr` | `ycb1_book_first-aid-cpr.tex` |
| | `ycb1-hl-stress-management` | `ycb1_book_lifestyle-stress.tex` |
| | `ycb1-hl-metabolic-respiratory` | `ycb1_book_lifestyle-stress.tex` |
| | `ycb1-hl-personality-development` | `ycb1_book_health-promotion.tex` |
| Practical: demonstration skills | `ycb1-pd-prayer-pranava-hymns` | `ycb1_book_prayer.tex` |
| | `ycb1-pd-cleansing-techniques` | `ycb1_book_cleansing.tex` |
| | `ycb1-pd-sukshma-vyayama` | `ycb1_book_vyayama.tex` |
| | `ycb1-pd-sthula-vyayama` | `ycb1_book_vyayama.tex` |
| | `ycb1-pd-surya-namaskara` | `ycb1_book_surya-namaskara.tex` |
| | `ycb1-pd-yogasana-practice` | `ycb1_book_asanas.tex` |
| | `ycb1-pd-preparatory-breathing` | `ycb1_book_breathing-pranayama.tex` |
| | `ycb1-pd-pranayama` | `ycb1_book_breathing-pranayama.tex` |
| | `ycb1-pd-bandha` | `ycb1_book_bandha-mudra.tex` |
| | `ycb1-pd-mudra` | `ycb1_book_bandha-mudra.tex` |
| | `ycb1-pd-meditation-practices` | `ycb1_book_meditation.tex` |
| Practical: teaching skills | `ycb1-pt-lesson-plan` | `ycb1_book_lessons.tex` |
| | `ycb1-pt-teaching-groups` | `ycb1_book_lessons.tex` |
| | `ycb1-pt-class-preparation` | `ycb1_book_teaching-class.tex` |
| | `ycb1-pt-factors-influencing-teaching` | `ycb1_book_teaching-class.tex` |
| | `ycb1-pt-class-management` | `ycb1_book_lessons.tex` |
| | `ycb1-pt-conducting-lessons-precautions` | `ycb1_book_lessons.tex` |
| | `ycb1-pt-ideal-instructor` | `ycb1_book_lessons.tex` |
| | `ycb1-pt-model-lesson-plans` | `ycb1_book_lessons.tex` |
| Practical: application of knowledge | `ycb1-pa-application-of-knowledge` | `ycb1_book_application.tex` |
| Practical: field experience | `ycb1-pf-field-experience` | `ycb1_book_field-experience.tex` |
| Exam and certification | `ycb1-ex-exam-and-certification` | `ycb1_book_exam.tex` |

The same map drives the coverage check (`BOOK_MAP` in `reports/ycb1_tools/ycb1_coverage.py`); change both together.
