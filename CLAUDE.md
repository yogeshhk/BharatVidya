# CLAUDE.md

## Status: maintained study archive

Reopened in November 2026 for a bounded upgrade (plan: `reports/upgrade_nontech_14112026.md`; progress: `reports/STATUS.md`, read it first in a new session). Outside that plan, keep changes to genuine defects (broken builds, broken links, wrong facts). Do not add CI or workflows. Personal items are flag-only. Open actions are in `TODO.md`; what was moved out is in `NOTICE.md`.

## Purpose

A study archive on Indian Knowledge Systems under NEP 2020, centred on Yoga (the Yoga Sutra seminar system, Yoga Nidra, the YCB Level 1 workshop and textbook), with curated lists on Sanskrit. The outputs are compiled LaTeX/PDF documents. There is no code; the YogaSutraTrees knowledge graph (Giacomo De Luca) was removed, so use the upstream project (links in `YogaSutra/SOURCES.md`).

## Compiling

All LaTeX uses **XeTeX** (required for Devanagari), never pdflatex. Each family has a batch script beside its drivers; `texify --engine=xetex -cp` compiles each driver from its own folder (sources use relative paths):

```bat
LaTeX\make_all.bat                              # every live family
LaTeX\workshops\YogaSutra\make_yogasutra.bat    # Yoga Sutra workshop and seminars
LaTeX\books\YCB1\workshop\make_ycb1.bat         # YCB certification workshop
LaTeX\books\YCB1\book\make_book_ycb1.bat        # YCB1 textbook
LaTeX\workshops\YogaNidra\make_yoganidra.bat
LaTeX\workshops\Sharada\make_sharada.bat
LaTeX\workshops\YogaShastra\make_yogashastra.bat  # retired, switched off
LaTeX\onepagers\make_onepagers.bat
```

Single driver: change into its folder, then `texify --engine=xetex -cp <filename>.tex`. Decks share `LaTeX/_shared/template_presentation.tex` and `template_cheatsheet.tex`; shared images are in `LaTeX/_shared/images/`. Folder map and file patterns: `LaTeX/README.md`.

### The custom headline in `template_presentation.tex`: do not revert it

The template overrides beamer's `headline` with a section-only bar built from `\insertsectionnavigationhorizontal`. This is load-bearing for build performance. **Do not "simplify" it back to the stock miniframes headline.** Miniframes lays out one marker per frame; once a `.nav` file exists, the large workshop deck produced a navigation bar far wider than the slide and an overfull-box warning on every page (a huge log and a very slow second pass), even though the markers were blanked.

Two traps if it is ever edited:
- `\insertsectionnavigation` (no suffix) lays sections out vertically, is for sidebars, and silently empties the bar here. Use the `...horizontal` variant.
- A large deck's first pass is quiet and fast; problems appear only from the second pass, once `.nav` exists. Judge a headline change on a full `texify` run, not a single pass.

## Domain areas

| Directory | Content |
|-----------|---------|
| `LaTeX/` | The slide system: `workshops/` (YogaSutra with `seminars/`, YogaNidra, Sharada, retired YogaShastra), `onepagers/`, `_shared/` (templates, shared topics and images), `_leftovers/` (unused, kept), `books/YCB1/` (`docs/` notes, `workshop/` decks, `book/` textbook) |
| `YogaSutra/` | Notes, Devanagari text, mind maps, `SOURCES.md`, video list |
| `YogaNidra/` | Overview, notes, practice script, research reading list |
| `Spirituality/` | Curated Yoga resources, meditation note, GoodLife and Sketchnotes |
| `Samskrit/` | Curated Sanskrit lists and a papers reading list |
| `reports/` | Upgrade plans, `STATUS.md`, local YCB1 tools |

## Yoga Sutra seminar system

One workshop plus independent seminars (Intro, Samadhipad, Sadhanapad, Vibhutipad, Kaivalyapad, Overview) in `LaTeX/workshops/YogaSutra/` (seminars in `seminars/`). Drivers are `Main_Workshop_YogaSutra_*` and `Main_Seminar_YogaSutra_<name>_*`, each as `_Presentation` and `_CheatSheet`; the build glob is `Main_*_YogaSutra*.tex`.

Content files: `workshop_yogasutra_content.tex` inputs all chapter files; `seminar_yogasutra_intro_content.tex` is intro + glance + refs; `seminar_yogasutra_<chapter>_content.tex` is brief_intro + chapter + refs; `seminar_yogasutra_overview_content.tex` is the standalone overview.

**Critical naming rule:** shared source files are `yogsutra_*` (no 'a'): `yogsutra_intro`, `_samadhipad`, `_sadhanapad`, `_vibhutipad`, `_kaivalyapad`, `_glance`, `_brief_intro`. The one exception is `yogasutra_refs.tex` (with 'a'). A wrong spelling in `\input` breaks the build.

## Workshops (2027 plan) and the retired YogaShastra deck

The three workshops are Yoga certification (`Main_Workshop_YCB1_*`), Yoga Sutra and Yoga Nidra (`Main_Seminar_YogaNidra_*`). The YCB1 textbook follows its own rules in `LaTeX/books/YCB1/AUTHORING.md` (notes first, fact-check gate; all rights reserved; called a textbook; parked for 2027). The YogaShastra deck (`LaTeX/workshops/YogaShastra/`) is retired: not built, do not extend it or convert new transcripts into it; its `yogashastra_*` topic files are sources to mine for the three workshops.

The `/upgrade-deck` command is available for reviewing Beamer decks here.
