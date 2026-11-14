# Status log (resume point)

Updated 2026-11-14 (second pass: the tree was re-measured and the small fixes, deck titles, the compiled-PDF move and tier C were done). Plan: `upgrade_nontech_14112026.md`. Read this first in a new session.

## Rules in force
No git commands. No CI or workflows. Personal items are flag-only. Nothing from `ImpDocs`. No copying to ToPrint. Compile once per batch with `texify --engine=xetex -cp`. No em dashes.

## Decisions made by the author
- Licence: CC BY-NC-SA 4.0 for content, MIT for code, third-party material excluded by a NOTICE (T7).
- Personal files (T10): move to a private folder outside the repo. Third-party tiers A, B and C: move out, keep links. Duplicates (T3): yes, one copy per identical set. Old versions of third-party files: move, not delete.
- Seminar titles: no hard-typed number, a comma instead of the dash.
- Tier C (saved web pages): not to Publications (a public repo of the author's own work; that would only move the exposure). Moved out with a links README in each folder.
- Git history: not needed; a fresh start is the plan, to be done last (the author runs the git steps).

## State of the repo, measured 2026-11-14
- Working tree: 841 files outside hidden folders, 0.47 GB (the plan started from 1,493 files and 2.12 GB). The `.git` folder is 4.90 GB, because history still holds everything that was moved out.
- No build leftovers beside the sources. Local Markdown link check: 0 broken.
- Everything moved out of the repo now lives in the author's Google Drive folder `Yoga` (the author moved the whole `Desktop\BharatVidya_Moved` folder there; it sits inside `ImpDocs`, which the agent may not open, so its contents were not checked). The Desktop folder no longer exists. What was moved, with the counts at the time:

| Moved set | Files | Size | What |
|---|---|---|---|
| Tiers A and B | 417 | 1.37 GB | third-party books, recordings and course packs |
| Tier C | 70 | 80.4 MB | saved web pages: YogicJourney, SwamiJ, StudyGroup, Maayboli, AthaYoga |
| Tier D | 115 | 140.4 MB | papers, theses, spreadsheets of corpora and magazine volumes: `Samskrit/Papers`, `YogaNidra/Papers`, `Samskrit/Magazines` (staged on the Desktop, then no longer there when last looked at; presumably moved to Drive too, not verified) |
| Duplicates | 42 | 0.04 GB | one copy of each byte-identical set, including two pirate-library PDFs |
| Private | 29 | 0.01 GB | the author's forms, diary, assignments and certificates |
| Retired | 42 | 5.5 MB | three duplicate shared files, 37 unused images, the old `graphold.json` and `indexold.html` |
| Release staging | 5 | 40 MB | compiled PDFs that sat in content folders: YCB1 workshop and cheat sheet, YogaNidra seminar and cheat sheet, the YogaSutra one-pager (older build outputs, not rebuilt today) |

Sizes use 1 GB = 1024 MB. The Windows Recycle Bin still holds partial copies of the old Desktop folders (about 1.4 GB, with files missing that the author moved out of them); empty it after confirming the Drive copy.

## Done
- T1, deck content: Orientation frames added to `LaTeX/yogsutra_intro.tex` (after the Panini frame) and `LaTeX/yogsutra_glance.tex` (at the start), and the intro facts fixed (father of Yoga, dating, typos, Devanagari spellings, sutra count wording, en dashes).
- T2, third-party tiers A and B moved out, hash-checked; the dry-run list is `reports/t2_move_plan.txt`.
- Tier C moved out, hash-checked, the five folders each got a `README.md` with the original source links read from the PDFs themselves (Medium, swamij.com, yogasutrastudy.info, Maayboli, Sanskrit Documents). `StudyGroup/YogSutra_Devnagari.txt` stays in the repo: it is the only copy of the Devanagari sutra text.
- Tier D moved out (author's choice: move out, add a reading list), hash-checked. A scan of the first two pages of every PDF found no mention of the maintainer, so none of it is the author's own work. `Samskrit/Papers`, `YogaNidra/Papers` and `Samskrit/Magazines` each hold a `README.md` reading list: a DOI, arXiv id or intact web address where the PDF itself carried one (about a third of the Sanskrit papers, most of the Yoga Nidra ones), otherwise "search by title". Addresses that came out garbled or cut off were left out, not repaired by guessing.
- T3, duplicates: moved, link check 0 broken. The list of what remained is `reports/t3_duplicates_after_moves.txt`.
- T4, LaTeX tidy: three duplicate shared files and 37 unused images moved out (a strict check against every `.tex`, `.md`, `.sty` and `.bat`). The orphan topic files `ycb1_theory_faqs` and `yogashastra_sankhya` are commented out in their drivers on purpose and were kept; `yogashastra_meditation` is unreferenced and kept.
- T5, stale facts: `README.md`, `CLAUDE.md`, the head of `TODO.md` and `LaTeX/README.md`. `CLAUDE.md` and `LaTeX/README.md` no longer say the decks' shared style files live in `Samskrit/LaTeX`: the decks use `LaTeX/template_presentation.tex` and `LaTeX/template_cheatsheet.tex`, and `Samskrit/LaTeX` serves only `subantaruupaNi.tex`.
- T5, em dashes in text files: replaced in `CLAUDE.md`, `YogaShastra/Meditation/Notes_Meditation.md` and `reports/upgrade_nontech_13072026.md`. The only Markdown file still holding any is the author's own backup of the notes, `YogaShastra/YogaSutra/_backup/Notes on Yogasutra_ORIGINAL.md`.
- T5, deck titles: the five YogaSutra seminar decks and their five cheat sheets read "YogaSutra Seminar: Introduction", "YogaSutra Seminar: Samadhi Pada, Concentration" and so on. All ten rebuilt, exit 0, no leftovers. Pages: Intro 87 and its cheat sheet 7 (both grew with the Orientation frames), Samadhi 120 and 13, Sadhana 128 and 11, Vibhuti 129 and 13, Kaivalya 80 and 7. Titles checked on page 1 of each PDF. The seminar table in `CLAUDE.md` no longer carries numbers.
- T6 and T7: README landing page; `LICENSE_CONTENT.md`, `NOTICE.md`, `CITATION.cff`, `CODE_OF_CONDUCT.md`; the existing MIT `LICENSE` stays for code.
- T9: the duplicate Devanagari text was resolved in T3 (the `_clean` copy went out, same hash; do not delete the remaining one). `YogaSutraTrees/graphold.json` and `indexold.html` moved out, the YogaSutraTrees README has a credit section, `Dasbodh/README.md` and `Samskrit/LaTeX/README.md` were filled in, and `IKS/2_Integral Yoga Vedanta Sutras.PDF` became `IKS/Integral Yoga Vedanta Sutras.PDF`. The NIOS Book-2 copy and the MHThaker mp3 pair left with tiers A and B.
- T8 preparation: no compiled PDF is left in a content folder. The workshop and seminar PDFs are in `LaTeX/`.
- T10: 29 personal files moved out and ignored in `.gitignore`.
- Workshop builds (earlier today), exit 0: YogaSutra workshop 504 pages and cheat sheet 46, YogaShastra workshop 870 pages and cheat sheet 87. The YogaShastra build had been failing on an unescaped underscore in a URL in `LaTeX/yogashastra_refs.tex` (fixed). They were built before the title change and not rebuilt after it; their own titles were not part of it.

## Still open, and the agent can do these
- Em dashes in slide body text: about 90 across 20 source files (`yoganidra_shrimath` has the most, then the `yogsutra_sadhanapad`, `ycb1_*` and `yogashastra_meditation` files; `yogasutra_refs` has a few). Some are quotations. Decide whether the house rule covers body text before editing; every deck that inputs those files would need a recompile.
- `Samskrit/LaTeX/Notes.md` points at `images/sunsal.jpg`, which is not in the folder. Add the picture or remove the line.
- Links pages for the tier A and B folders: not checked in this pass (tier C has them).
- 20 files stayed because documents link to them (Dasbodh `.doc` and `.jpg`, Enjoyable Sanskrit Grammar volumes, Laghu Siddhanta Kaumudi study guides, `Deep Relaxation.mp3`, `Yogalaya FAQ.pdf`): keep or relink.
- Re-run the build of the workshop decks if their sources change, and refresh the page counts in `TODO.md` (they are from August).

## Left for the author
- T8: publish the compiled PDFs as a GitHub Release (outward-facing). Rebuild the five staged PDFs from `LaTeX/` first if their sources changed.
- Start the git history fresh, last, after everything above is settled (the author runs these; the agent never runs git). Back up the `.git` folder, delete it, `git init -b master`, `git add -A`, check `git status`, commit, add the remote `https://github.com/yogeshhk/BharatVidya.git` and `git push --force origin master`. GitHub keeps old commits reachable by their address until it garbage-collects, and existing forks and clones keep the old history, including the files moved out.
- Check the Drive `Yoga` folder holds everything listed above, then empty the Recycle Bin.
- Flagged, not moved: the WhatsApp image `IKS/IndianKnowledgeSystems/IMG-20260226-WA0001.jpg`, `LaTeX/ycb1_exam.tex` and its images, `Dasbodh/Assignments` (mixed), the Bhishma assignment and oral-exam PDFs, and the contact email in every deck footer.
- T11: whether the internal folders (`YogaShastra/YogaSutra/_backup`, `Code/claudecode`, `reports`, `.claude`) stay public. `.claude/settings.local.json` exists in the tree; run `git ls-files .claude reports Code` to see whether it is tracked.
- Commit all of this (git is the author's).

## Not rechecked in this pass
The Orientation frame work, the page counts of the two workshop builds and the first-pass moves are carried from the first pass. The Drive folder was not opened.
