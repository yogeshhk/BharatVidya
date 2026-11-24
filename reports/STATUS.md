# Status log (resume point)

Read this first in a new session. Latest block is "Session 2026-11-24" directly below; the older log follows it.

## Session 2026-11-24 (latest, kept in step while working)

Author is away and asked for autonomous work; if a session stops, continue from the first unticked item.

Done:
- [x] LaTeX reorganised into `LaTeX/workshops/` (YCB1, YogaSutra with `seminars/`, YogaNidra, Sharada, YogaShastra retired), `LaTeX/onepagers/`, `LaTeX/_shared/` (templates, shared topic files, shared images), `LaTeX/_leftovers/` (unused, kept). Hash-checked; one deck per family compiled. Manifest: `reports/latex_reorg_manifest.csv`. Folder guide: `LaTeX/README.md`.
- [x] `Yoga/` renamed `Spirituality/`; its certification folder moved into the YCB1 book docs and later flattened there by the author.
- [x] YCB Level 1 textbook scaffold in `LaTeX/books/YCB1/`: `README.md`, `TODO.md`, `AUTHORING.md`, `docs/Notes YCB1.md` (master notes, one block per syllabus topic), `docs/image_register.csv` (one row per deck image: current name, prompt or brief, final name and path). Deck picture lines carry `% FIG` comments. Analysis and proposal: `reports/ycb1_textbook_analysis.md`.
- [x] Source review of `LaTeX/books/YCB1/docs/`: the guidebook there (two identical copies) is for the older four-level scheme; the notes have a Local sources line per block (covered, partial, gap).
- [x] Notes block written: the exam and certification block (from the Board guideline and the Level 1 syllabus).
- [x] Publications `KEEP_NOTES.md` and `TODO.md` synced to the author's Keep text plus the YCB1 lines (author copies them into Google Keep).

- [x] Root tidy done: `LICENSE_CONTENT.md` and `MOVED_MATERIAL.md` merged into `NOTICE.md` (now licences, third-party notice, what was removed); `CODE_OF_CONDUCT.md` folded into `CONTRIBUTING.md`; `CONTENTS.md` folded into `README.md` (a map section). The four merged files are removed; `LICENSE` (MIT text unchanged), `CITATION.cff`, `CLAUDE.md`, `TODO.md` stay. Root now holds README, LICENSE, NOTICE, CITATION.cff, CONTRIBUTING, CLAUDE, TODO.
- [x] Links fixed after the tidy and after the author's own reshuffles: `Samskrit/README.md` (flat layout, no Arthashastra list because the file does not exist anywhere in the repo), `YogaSutra/README.md` and `SOURCES.md` (texts now in `YogaSutra/refs/`), root `README.md`. Local Markdown link check: 0 broken (reports excluded).

In progress (this block is updated as each step finishes):
- [ ] Continue the YCB1 notes blocks one at a time, starting with the practical demonstration blocks or the covered theory blocks (the author chose the exam block first; it is done). See `LaTeX/books/YCB1/TODO.md`.

Open, for the author:
- The two large instructor-book PDFs and the `.gdraw` link file in `LaTeX/books/YCB1/docs/` must stay out of the public repository (decide: ignore pattern or move to the private Drive).
- `Samskrit/Awesome_arthashastra.md` is gone; the Arthashastra list is no longer mentioned in the READMEs. Restore the file and the mentions if it should stay.
- Book licence for `LaTeX/books/YCB1/` (separate from the deck licence) is undecided; `NOTICE.md` says a book project keeps its own licence.

## Earlier log

Updated 2026-11-14, end of the clean-up day. Plan: `upgrade_nontech_14112026.md`.

## Rules in force
No git commands. No CI or workflows. Personal items are flag-only. Nothing from `ImpDocs` unless the author has granted access to its `Yoga` folder. Compile once per batch with `texify --engine=xetex -cp`. No em dashes. Move, hash-check and list; do not delete without being told.

## Decisions made by the author
- Licence: CC BY-NC-SA 4.0 for content, MIT for code, third-party material excluded by a NOTICE.
- Own coursework, answer sheets and assignments go out. Only generic public material and complete, original material stays. "Partial some files here, some there does not make sense."
- Core-only repository: slides, Yoga Sutra and Yoga Nidra material, curated lists. Everything else moved out (kept privately in Google Drive).
- Unfinished decks are deleted, not kept: the Arthashastra workshop, the Bharat Vidya overview, the Zen Yoga workshop and the Shrimath seminar.
- Seminar titles: no hard-typed number, a comma instead of the dash. Em dashes in slide text: quotations and exact cited titles stay, everything else became a spaced hyphen.
- Git history is not needed: a fresh start, done last, by the author.

## State of the repository, measured 2026-11-14
413 files, 75.1 MB outside hidden folders (folders: `LaTeX`, `YogaSutra`, `YogaNidra`, `Yoga`, `Samskrit`, `reports`), of which 20 compiled PDFs (about 48 MB) are git-ignored. The `.git` folder is still about 4.9 GB until the fresh start. Local Markdown link check: 0 broken. No em dashes in Markdown.

| Folder | Files | What it holds |
|---|---|---|
| `LaTeX/` | 365 | 24 deck and one-pager drivers: the Yoga Sutra workshop, five seminars, overview and one-pager; the Yoga Shastra and YCB1 workshops; the Yoga Nidra seminar; the Sharada seminar; the Darshana one-pager. Topic files, templates, images, build scripts. Every driver resolves all its inputs and images |
| `YogaSutra/` | 22 | `README.md` (folder guide and a long video list), the study notes, the Devanagari text and its headings, `SOURCES.md`, and `mindmaps/` (17 hand-drawn mind maps, PDF and SVG) |
| `YogaNidra/` | 4 | `README.md` (overview with references), notes, the detailed practice script, the research reading list |
| `Yoga/` | 2 | `README.md` (Awesome Yoga list) and the meditation note |
| `Samskrit/` | 4 | `README.md`, Awesome Samskrit, Awesome Arthashastra, the Sanskrit papers reading list |
| `reports/` | 5 | the plans and this file |
| root | 12 | README, CONTENTS, TODO, CLAUDE, `MOVED_MATERIAL.md`, NOTICE, CONTRIBUTING, licences, CITATION, CODE_OF_CONDUCT |

`.gitignore` ignores compiled decks (`LaTeX/Main_*.pdf`) and `.claude/settings.local.json`; the list of personal-file name patterns was removed because the files are gone.

## Done today, in short
- Moved out, hash-checked, in batches: third-party tiers A to D (books, saved web pages, papers, magazines), personal coursework (Dasbodh, Samskrita Bharati notes, Bhishma master's course, Yogalaya forms and others), formerly linked files, unused LaTeX images and files, and finally everything outside the core (the `Dasbodh`, most of `IKS`, `Admin`, `Code`, most of `Samskrit` and `YogaShastra`). Each batch has a `_moved_from_repo.txt` list.
- Deleted: four unfinished decks with their cheat sheets, 38 topic files used only by them, 13 images and 4 build scripts (about 65 distinct files). Nothing else uses them.
- Slides: seminar titles reworded; em dashes removed from 335 slide lines in 20 sources; the YogaNidra deck had a stray `\end{document}` that cut it off at frame 12 of 35 (the cheat sheet could not even build) and now has all frames; 24 decks rebuilt, exit 0, no leftovers.
- Documents rewritten to the new shape: README, CONTENTS, CLAUDE.md, TODO, LaTeX README, NOTICE; new `MOVED_MATERIAL.md` and `lists/YogaSutra_sources.md` (consolidated source links, including the upstream YogaSutraTrees project).
- Shape (author's choice, after two tries): siblings are themes, not data types. `LaTeX/` stays the mixed folder with all the slides; the other folders are `YogaSutra/`, `YogaNidra/`, `Yoga/` and `Samskrit/` (which also holds the Arthashastra list), each with its own `README.md` and notes, lists or mind maps. An earlier layout by data type (`notes/`, `mindmaps/`, `lists/`) was dropped. All references were updated; link check 0 broken.
- Two reading lists were kept with links read from the PDFs themselves (Sanskrit papers; Yoga Nidra research). Addresses that came out garbled or cut off were left out, not guessed.
- Correction to earlier notes: the tidy step had been recorded as moving `LaTeX/preamble.tex`, `shloka.sty` and `subantaruupaNi.tex` out; they were in fact still there, identical to the `Samskrit/LaTeX` copies. They left in the final clean-up.

## Left for the author
Nothing is tracked as open. The git fresh start is done. The GitHub Release, the reading of the new Yoga Nidra frames and READMEs, and the email in the deck footers (kept) are the author's own, untracked decisions. The exam frames of the YCB1 workshop stay public.

## Yoga theme work: finished
The Drive master (renamed `BharatVidya` by the author) was reorganised by theme on 2026-11-14 and the staged files were copied in; the Desktop staging, the duplicates holding folder and the move log are gone. Generic and own material was copied from the Drive into `Yoga/`, `YogaSutra/`, `YogaNidra/` and `Samskrit/`, each item after the author confirmed it. In `Yoga/` of this repository the meaning is: the asana and philosophy side of yoga, plus yoga material that is not specific to the Yoga Sutra or Yoga Nidra. Details are in `reports/yoga_theme_plan.md`.

Later the same day the Drive was tidied again at the author's direction: the master's course and the Arthashastra folder moved under `IKS`, certification under `Yoga`, Aurobindo and Sadhguru under `Spirituality/Philosophy`; the Desktop staging and the old tools folder were deleted. The slide leftovers (53 files: unused images, three draft topic files, `preamble.tex`, `shloka.sty` and `subantaruupaNi.tex`) were copied back into `LaTeX/` at the author's request, so the file count under `LaTeX/` is higher than in the table above; the two PowerPoint files went to the Drive `Yoga/Diagrams`. The unused images include the YCB1 exam screenshots, which ties in with the open question about the exam frames.

## Next after this repository
The Drive `ImpDocs/Yoga` folder is to be reorganised by theme and deduplicated, with an analysis report first. FreeFileSync copies the Drive `ImpDocs` (source) to the GitHub `ImpDocs` (destination). The plan is saved in the agent's memory (`impdocs-yoga-reorganisation-plan`).
