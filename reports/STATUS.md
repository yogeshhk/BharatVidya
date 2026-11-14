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

## Pending (older list; T1, T2 tiers A and B, T5, T6, T7, T10 above are done)
- T9 small fixes, T4 tidy (dry-run list first, move not delete), T5 stale facts, T6 README landing page, T7 files (LICENSE, NOTICE, CITATION.cff, CODE_OF_CONDUCT).
- Recompile workshop decks once, after T4.
- Needs the author: T10 personal flags, T2 and T3 deletions and moves, T8 release, `.git` rewrite.
