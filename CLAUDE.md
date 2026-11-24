# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Status: maintained study archive (reopened November 2026)

The repo was closed in August 2026 and reopened in November 2026 for a bounded upgrade: Orientation
frames in the intro and glance decks, removal of third-party and personal material (moved out to the maintainer's
private Google Drive), a cut down to what is original and complete (see `NOTICE.md`), a landing-page
README and licence files. The plan and its progress are in
`reports/upgrade_nontech_14112026.md` and `reports/STATUS.md` (read STATUS first in a new session).

Outside that plan, keep changes to genuine defects (broken builds, broken links, wrong facts). Do not
add CI or workflows. Personal items are flag-only. See `TODO.md` for the state each area was left in.

## Repository Purpose

BharatVidya is a study archive on Indian Knowledge Systems (IKS) under NEP 2020, centred on Yoga (the Yoga Sutra seminar system and Yoga Nidra), with curated lists on Sanskrit and the Arthashastra. The primary outputs are compiled LaTeX/PDF documents, not software applications.

## Compiling LaTeX Documents

All LaTeX compilation uses **XeTeX** (required for Devanagari and Unicode support). The slides are grouped by topic under `LaTeX/` (`workshops/`, `onepagers/`, `_shared/`), and each family has its own batch script beside its drivers:

```bat
LaTeX\make_all.bat                              # every live family
LaTeX\workshops\YogaSutra\make_yogasutra.bat    # Yoga Sutra workshop and its seminars
LaTeX\workshops\YCB1\make_ycb1.bat              # YCB certification
LaTeX\workshops\YogaNidra\make_yoganidra.bat
LaTeX\workshops\Sharada\make_sharada.bat
LaTeX\workshops\YogaShastra\make_yogashastra.bat  # retired, switched off
LaTeX\onepagers\make_onepagers.bat
```

Scripts use `texify --engine=xetex -cp` and recursively find files matching their family's pattern, for example `Main_*_YogaSutra*.tex`, and compile each from its own folder because the sources use relative paths. To compile one driver manually, change into its folder first:

```bat
texify --engine=xetex -cp <filename>.tex
```

The decks share `LaTeX/_shared/template_presentation.tex` and `LaTeX/_shared/template_cheatsheet.tex`; shared images are in `LaTeX/_shared/images/`.

### The custom headline in `template_presentation.tex` -- do not revert it

`template_presentation.tex` overrides beamer's `headline` template with a section-only bar built
from `\insertsectionnavigationhorizontal`. This is deliberate and load-bearing for build
performance. **Do not "simplify" it back to the stock miniframes headline.**

Why it exists: `miniframes` lays out one navigation marker per frame. Once a `.nav` file exists,
the 492-frame Workshop deck produced a navigation bar ~1000pt wider than the slide and reported the
overflow on every page -- 510,355 `Overfull \hbox` warnings, a 37 MB log, and a ~420 second second
pass. The markers were already blanked by `\setbeamertemplate{mini frames}{}`, so nothing looked
wrong; the boxes were laid out regardless.

After the override: 64 overfull warnings across all 15 documents, an 819 KB log, 279 seconds for
the whole set. Page counts unchanged, slides look the same, and section names that used to be
pushed off the right edge are now visible.

Two traps if this is ever edited:

- `\insertsectionnavigation` (no suffix) lays sections out **vertically** and is for sidebars.
  Using it here silently empties the bar. The `...horizontal` variant is the correct one.
- A large deck's *first* pass is quiet and fast; problems only appear from the second pass onward,
  once `.nav` exists. Always judge a headline change on a full `texify` run, not a single pass.

## Third-party data and code

There is no code in this repository. The YogaSutraTrees knowledge graph by Giacomo De Luca (`graph.json`, with Devanagari, transliteration, word-by-word analysis, several translations and commentaries) used to be copied here; it was removed. Use the upstream project; the links are in `YogaSutra/SOURCES.md`.

## Domain Areas

| Directory | Content |
|-----------|---------|
| `LaTeX/` | The slide system, grouped by topic: `workshops/` (YCB1, YogaSutra with its seminars, YogaNidra, Sharada, and the retired YogaShastra), `onepagers/`, `_shared/` (templates, shared topic files and images), `_leftovers/` (unused, kept), `books/` (planned) |
| `YogaSutra/` | Notes on the Yoga Sutra, the Devanagari text, hand-drawn mind maps (`mindmaps/`), `SOURCES.md` and a long video list (`README.md`) |
| `YogaNidra/` | Yoga Nidra overview (`README.md`), notes, a detailed practice script and a research reading list |
| `Spirituality/` | A curated list of Yoga resources (`README.md`), a meditation note, and the GoodLife and Sketchnotes folders (renamed from `Yoga/`) |
| `Samskrit/` | Curated lists on Sanskrit and the Arthashastra, and a reading list of papers on Sanskrit and computing |
| `reports/` | The upgrade plans and `STATUS.md` (read it first) |

Everything else that used to be here was moved out; see `NOTICE.md`.

## LaTeX Conventions

- Documents targeting Devanagari **must** use XeTeX, not pdflatex.
- Beamer presentation sources follow the pattern `Main_*_BharatVidya*.tex` for auto-discovery by build scripts.
- The `/upgrade-deck` slash command is available for structured review and improvement of Beamer presentations in this repo.

## YogaSutra Seminar System

The YogaSutra material in `LaTeX/workshops/YogaSutra/` (seminars in its `seminars/` folder) is structured as a workshop plus independent seminars, each with a matching cheat sheet.

**Presentations (built by `make_yogasutra.bat`, glob: `Main_*_YogaSutra*.tex`):**

| File | Title |
|------|-------|
| `Main_Workshop_YogaSutra_Presentation.tex` | Full workshop (all chapter seminars) |
| `Main_Seminar_YogaSutra_Intro_Presentation.tex` | Seminar: Introduction |
| `Main_Seminar_YogaSutra_Samadhipad_Presentation.tex` | Seminar: Samadhi Pada |
| `Main_Seminar_YogaSutra_Sadhanapad_Presentation.tex` | Seminar: Sadhana Pada |
| `Main_Seminar_YogaSutra_Vibhutipad_Presentation.tex` | Seminar: Vibhuti Pada |
| `Main_Seminar_YogaSutra_Kaivalyapad_Presentation.tex` | Seminar: Kaivalya Pada |
| `Main_Seminar_YogaSutra_Overview_Presentation.tex` | Overview (~45 slides, independent session) |

Each has a corresponding `*_CheatSheet.tex`.

**Content file architecture:**
- `workshop_yogasutra_content.tex`: inputs all chapter files for the full workshop
- `seminar_yogasutra_intro_content.tex`: intro + glance + refs
- `seminar_yogasutra_<chapter>_content.tex`: brief_intro + chapter + refs (one per chapter)
- `seminar_yogasutra_overview_content.tex`: standalone overview covering all chapters

**Shared source files, naming: `yogsutra_*` (no 'a'), except refs:**
- `yogsutra_intro.tex`, `yogsutra_samadhipad.tex`, `yogsutra_sadhanapad.tex`, `yogsutra_vibhutipad.tex`, `yogsutra_kaivalyapad.tex`, `yogsutra_glance.tex`
- `yogsutra_brief_intro.tex`: compact context-setter reused in each chapter seminar
- `yogasutra_refs.tex`: references (this file uses 'a': `yogasutra_refs`)

**Critical naming rule:** Source content files use `yogsutra_*` (no 'a'). Any `\input{yogasutra_*}` reference (with 'a') will break, so always use `\input{yogsutra_*}` except for refs.

## Workshops (2027 plan) and the retired YogaShastra deck

The three workshops are Yoga certification (`Main_Workshop_YCB1_*`), Yoga Sutra (`Main_Workshop_YogaSutra_*`) and Yoga Nidra (`Main_Seminar_YogaNidra_*`); open items are in `TODO.md`. The YogaShastra deck is retired: it is not built (`make_yogashastra.bat` is switched off) and its topic files are sources to reuse; do not extend it.

The retired deck is `LaTeX/workshops/YogaShastra/Main_Workshop_YogaShastra_Presentation.tex` (content via `workshop_yogashastra_content.tex` in the same folder). Do not convert new transcripts into it; its `yogashastra_*` topic files are to be mined for the three workshops (see `TODO.md`).
