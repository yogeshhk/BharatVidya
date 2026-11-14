# Status log (resume point)

Updated 2026-11-14, end of the clean-up day. Plan: `upgrade_nontech_14112026.md`. Read this first in a new session.

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

## Staged on the Desktop, waiting for the Drive `Yoga` folder
`C:\Users\yoges\Desktop\BharatVidya_Moved\` holds seven batch folders (380 files, 378 MB), each with its own list file: `Dasbodh` (118), `IKS_Bhishma` (31), `IKS_rest` (26), `LaTeX_unused` (55), `Rest_other` (62), `Samskrit` (13) and `YogaShastra_rest` (75). The author asked for them to be moved into the Drive `Yoga` folder. That is blocked until access to that folder is granted. Earlier batches were already moved by the author. Do not delete the Desktop copy until the Drive copy is hash-checked.

## Left for the author
- Start the git history fresh, last (the agent never runs git). Back up the `.git` folder first (about 4.9 GB, so to C: or Drive), then delete it, `git init -b master`, `git add -A`, check `git status`, commit, add the remote `https://github.com/yogeshhk/BharatVidya.git` and `git push --force origin master`. Only `master` is visible locally; check the GitHub branches and tags pages for others. GitHub keeps old commits reachable by address until it collects them, and existing forks and clones keep the old history.
- Publish the compiled PDFs as a GitHub Release (they are git-ignored now); build them from `LaTeX/` with the scripts.
- Read the Yoga Nidra instruction frames that were newly included (the deck grew from 92 to 234 pages); some have draft-looking titles such as "Preparation - 0".
- Decide whether the exam frames in the YCB1 workshop (`LaTeX/ycb1_exam.tex`) may stay public.
- Contact email: it prints in every deck footer; confirm you want it published.
- Empty the Windows Recycle Bin after the Drive copy is confirmed.
- Commit all of this.

## Yoga theme work: the Drive is reorganised, the repository is next
The Drive master (renamed `BharatVidya` by the author) was reorganised by theme on 2026-11-14 and the staged files were copied in; details, what is still open and the to-do entries are in `reports/yoga_theme_plan.md` and `TODO.md`. The staged material on the Desktop was copied, not moved, so `C:\Users\yoges\Desktop\BharatVidya_Moved` now duplicates the Drive: delete it only after the author agrees. A holding folder of 80 exact-duplicate copies is at `C:\Users\yoges\Desktop\BharatVidya_Duplicates`, and every action is in `Desktop\BharatVidya_Drive_move_log.csv`. In `Yoga/` of this repository the meaning is: the asana and philosophy side of yoga, plus yoga material that is not specific to the Yoga Sutra or Yoga Nidra. Copying generic Drive material into it comes next, one item at a time with the author's say.

Later the same day the Drive was tidied again at the author's direction: the master's course and the Arthashastra folder moved under `IKS`, certification under `Yoga`, Aurobindo and Sadhguru under `Spirituality/Philosophy`; the Desktop staging and the old tools folder were deleted. The slide leftovers (53 files: unused images, three draft topic files, `preamble.tex`, `shloka.sty` and `subantaruupaNi.tex`) were copied back into `LaTeX/` at the author's request, so the file count under `LaTeX/` is higher than in the table above; the two PowerPoint files went to the Drive `Yoga/Diagrams`. The unused images include the YCB1 exam screenshots, which ties in with the open question about the exam frames.

## Next after this repository
The Drive `ImpDocs/Yoga` folder is to be reorganised by theme and deduplicated, with an analysis report first. FreeFileSync copies the Drive `ImpDocs` (source) to the GitHub `ImpDocs` (destination). The plan is saved in the agent's memory (`impdocs-yoga-reorganisation-plan`).
