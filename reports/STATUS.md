# Status log (resume point)

Updated 2026-11-14. Plan: `upgrade_nontech_14112026.md`. Read this first in a new session.

## Rules in force
No git commands. No CI or workflows. Personal items are flag-only. Nothing from `ImpDocs`. No copying to ToPrint. Compile once per batch with `texify --engine=xetex -cp`. No em dashes.

## Decisions made by the author
- Licence: CC BY-NC-SA 4.0 for content, MIT for code, third-party material excluded by a NOTICE (T7).

## Done
- T1: Orientation frames added to `LaTeX/yogsutra_intro.tex` (9 frames, after the Panini frame) and `LaTeX/yogsutra_glance.tex` (2 frames, at the start). Intro facts fixed (father of Yoga, dating, typos, Devanagari spellings, sutra count wording, en dashes). Intro presentation and cheat sheet compiled and checked. The workshop decks that input the intro are not yet recompiled (heavy build); do that in one batch at the end.

- T10: author chose "move to a private folder". 29 personal files (Yogalaya form, diary, assignments, notes, guidelines; Vagvipaka certificate and exam; Dasbodh assignments) moved to `C:\Users\yoges\Desktop\BharatVidya_Moved\Private` (author asked for the Desktop; hash-checked, 11.55 MB, list in `_moved_from_repo.txt`) and ignored in `.gitignore`. Not moved, still flagged: the WhatsApp image and `LaTeX/ycb1_exam*`. The deletions show in git as removed files for the author to commit; old history still holds them (the `.git` rewrite is the author's).
- Note: a `LICENSE` file already exists in the repo; check its content before T7.

- T2: author chose "move tiers A and B out, keep links". All moved material goes to `C:\Users\yoges\Desktop\BharatVidya_Moved\ThirdParty` (same folder layout as in the repo), not to D:. DONE for 417 files (1.40 GB, hash-checked, list in `Desktop\BharatVidya_Moved\ThirdParty\_moved_from_repo.txt`; the dry-run plan is `reports\t2_move_plan.txt`). Working tree is now about 0.75 GB. 20 files stayed because docs or decks link to them (Dasbodh .doc and .jpg, Enjoyable Sanskrit Grammar volumes, Laghu Siddhanta Kaumudi study guides, Deep Relaxation.mp3, Yogalaya FAQ.pdf): decide with the README work whether to keep or relink. Still to do: a links page for the moved material (tier-C and D untouched), and check the repo for links to moved files (a link-check pass in T5). Dasbodh/Assignments and the Bhishma exam and assignment PDFs were not moved (mixed with the author's own work); flagged. Own-authored files inside those folders (for example `Sem*_Notes`, `Main_Seminar_YogaNidra_*`, `Notes_YogaNidra.md`, Shrimath files) stay.

- T5, T6, T7 done: README landing page, CLAUDE.md status, TODO head, LaTeX/README (no page counts or numbering), CONTENTS pending a final link pass; new `LICENSE_CONTENT.md`, `NOTICE.md`, `CITATION.cff`, `CODE_OF_CONDUCT.md`. The existing `LICENSE` (MIT) stays for code.

- T4 done: moved to `Desktop\BharatVidya_Moved\Retired` (hash-checked, list in `_moved_from_repo.txt`): the three duplicate files `LaTeX/preamble.tex`, `shloka.sty`, `subantaruupaNi.tex` (identical copies remain in `Samskrit/LaTeX`) and 37 unused images (strict check against all .tex, .md, .sty, .bat; fewer than the 78 in the report). Orphans `ycb1_theory_faqs`, `yogashastra_sankhya` are deliberately commented out in their drivers and were kept; `yogashastra_meditation` is unreferenced and kept. Local markdown link check: 0 broken.
- Workshop builds done, exit 0, no leftovers: YogaSutra workshop 504 and 46 pages, YogaShastra workshop 870 and 87 pages. The YogaShastra build had been failing on an unescaped underscore in a URL in `LaTeX/yogashastra_refs.tex` (fixed). Other YogaSutra seminars were not touched by the edits.
- T3 done after the author said yes: 42 files (40.6 MB) moved to `Desktop\BharatVidya_Moved\Duplicates` (one copy per identical set kept, never a copy a doc links to; both pirate-library `zliborg` PDFs moved). List in `_moved_from_repo.txt` there. Link check: 0 broken.
- T9: the NIOS Book-2 copy and the MHThaker mp3 pair moved out with tier A and B, so no separate fix is needed.

## Left for the author
- T8: publish the compiled PDFs as a GitHub Release (outward-facing). PDFs are built in `LaTeX/`.
- Rewrite git history (the `.git` folder is about 4.9 GB); the repo working tree is now much smaller. Everything under `Desktop\BharatVidya_Moved` is outside the repo; review it, then delete or archive.
- Flagged, not moved: WhatsApp image `IKS/IndianKnowledgeSystems/IMG-20260226-WA0001.jpg`, `LaTeX/ycb1_exam.tex` and its images, `Dasbodh/Assignments` (mixed), Bhishma assignment and oral-exam PDFs, the contact email in every deck footer.
- T11: internal folders (`_backup`, `Code/claudecode`, `reports`, `.claude`): decide whether they stay public.
- 20 linked files kept in the repo (see T2 note).
- Commit all of this (git is yours).

## Pending (older list; T1, T2 tiers A and B, T5, T6, T7, T10 above are done)
- T9 small fixes, T4 tidy (dry-run list first, move not delete), T5 stale facts, T6 README landing page, T7 files (LICENSE, NOTICE, CITATION.cff, CODE_OF_CONDUCT).
- Recompile workshop decks once, after T4.
- Needs the author: T10 personal flags, T2 and T3 deletions and moves, T8 release, `.git` rewrite.
