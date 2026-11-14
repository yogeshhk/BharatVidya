# TODO.md: Repo-Level Index

**Status as of 2026-11-14: maintained study archive.** It was closed in August 2026 and reopened for a
bounded upgrade (see `reports/STATUS.md` for progress and `reports/upgrade_nontech_14112026.md` for the
plan). There is no feature roadmap beyond that plan. The index below shows what exists and what state it
was left in.

Further Yoga Sutra study continues offline, from video playlists and books.

## Open, from the upgrade plan
- Release of the compiled PDFs (a GitHub Release is the author's step; compiled decks are git-ignored).
- Read the newly included Yoga Nidra instruction frames before a Release (the number suffixes on their titles are gone).
- Optional: record the source of `YogaSutra/Texts/Patanjali_YogaSutra_Vivekananda_Sanskrit_English.pdf` when remembered (the README already says it is unrecorded).
- Read the new folder READMEs (`Yoga/Sketchnotes`, `Yoga/GoodLife`) against the files; they were written from file names.

## Completed

| Area | State | Notes |
|---|---|---|
| Yoga Sutra (`YogaSutra/`, slides in `LaTeX/`) | **Complete.** Slide system final. | 1 Workshop + 6 Seminars (Intro, Samadhipad, Sadhanapad, Vibhutipad, Kaivalyapad, Overview), each with a matching cheat sheet. Built via `make_yogasutra.bat`; see [`LaTeX/README.md`](LaTeX/README.md). Folder guide and video list: [`YogaSutra/README.md`](YogaSutra/README.md). |
| Yoga Nidra (`YogaNidra/`, slides in `LaTeX/`) | **Complete.** | Beamer deck (Presentation + CheatSheet), detailed practice script, 8-stage practice notes, and a reading list of research papers. See [`YogaNidra/README.md`](YogaNidra/README.md). |

## Moved out

Everything else that used to be in this repository (Dasbodh, the Sanskrit courses, most of IKS and the other yoga
teachers' material, plus four unfinished decks) was moved out or deleted on 2026-11-14. See
[`MOVED_MATERIAL.md`](MOVED_MATERIAL.md). What is left is only what is original and complete enough to be useful.

## Build verification -- 2026-11-14

The YogaSutra documents were rebuilt on 2026-11-14 with XeTeX (`texify --engine=xetex -cp`): all exit 0, no
leftover build files. The page counts below are from that run (the August run had the Workshop at 492 and the Intro at 75;
the one-pager was not rebuilt, so its August count of 2 pages stands).

| Document | Pages |
|---|---|
| `Main_Workshop_YogaSutra_Presentation` | 504 |
| `Main_Seminar_YogaSutra_Vibhutipad_Presentation` | 129 |
| `Main_Seminar_YogaSutra_Sadhanapad_Presentation` | 128 |
| `Main_Seminar_YogaSutra_Samadhipad_Presentation` | 120 |
| `Main_Seminar_YogaSutra_Intro_Presentation` | 87 |
| `Main_Seminar_YogaSutra_Kaivalyapad_Presentation` | 80 |
| `Main_Seminar_YogaSutra_Overview_Presentation` | 50 |
| `Main_Workshop_YogaSutra_CheatSheet` | 46 |
| `Main_Seminar_YogaSutra_Vibhutipad_CheatSheet` | 13 |
| `Main_Seminar_YogaSutra_Samadhipad_CheatSheet` | 12 |
| `Main_Seminar_YogaSutra_Sadhanapad_CheatSheet` | 11 |
| `Main_Seminar_YogaSutra_Kaivalyapad_CheatSheet` | 7 |
| `Main_Seminar_YogaSutra_Overview_CheatSheet` | 7 |
| `Main_Seminar_YogaSutra_Intro_CheatSheet` | 7 |
| `Main_OnePager_YogaSutra_CheatSheet` | 2 |

### Fixed 2026-08-13: the headline overflow that made builds crawl

**Before.** `template_presentation.tex` used the `miniframes` outer theme, which lays out one
navigation marker per frame. Once a `.nav` file existed, the 492-frame Workshop deck produced a
navigation bar roughly 1000pt wider than the slide and reported the overflow on every page:

- Workshop deck: **510,355** `Overfull \hbox` warnings, a 37 MB log, and a ~420 second second pass.
  It did finish correctly, but it looked so much like a hang that one build was killed on the
  assumption that it was one.
- The three largest seminars hit the same thing at smaller scale: Vibhutipad 18,536 warnings,
  Sadhanapad 18,005, Samadhipad 14,009.

**Cause.** `\setbeamertemplate{mini frames}{}` was already blanking the markers *visually*, so
nothing looked wrong -- but the boxes were still being laid out, so they still overflowed.

**Fix.** The miniframes headline is replaced by a section-only bar built with
`\insertsectionnavigationhorizontal`. The section names were the only visible part of that headline,
so the slides look the same.

**After.** 64 overfull warnings across all 15 documents (from ~560,000), an 819 KB log (from 37 MB
for a single deck), and 279 seconds for the entire set (from 420 seconds for one pass of one deck).
Page counts are unchanged.

One deliberate, visible improvement: section names that the overflowing bar used to push off the
right-hand edge of the slide are now visible. On the Vibhutipad seminar, for example, the headline
previously showed `Intro | Vibhutipad` and now correctly shows `Intro | Vibhutipad | End`.

Worth knowing if this is ever revisited: `\insertsectionnavigation` (no suffix) lays sections out
*vertically* and is meant for sidebars. Using it here empties the bar -- that was tried first and
rejected on visual inspection. The horizontal variant is the correct one.

## Housekeeping done 2026-08-13

- `.gitignore` extended with LaTeX intermediates (`*.aux`, `*.nav`, `*.out`, `*.snm`, `*.toc`,
  `*.vrb`, `*.synctex.gz`, `*.bbl`, `*.blg`, `*.fls`, `*.fdb_latexmk`, `*.idx`, `*.ilg`, `*.ind`).
  `texify -c` cleans these on success, but a failed or interrupted build leaves them behind, and
  only `*.log` was previously covered.
- Repo swept for stray build artifacts: none tracked, none left behind.
- No open `TODO`/`FIXME`/`WIP` markers exist anywhere in the repository.
