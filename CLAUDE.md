# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Status: maintained study archive (reopened November 2026)

The repo was closed in August 2026 and reopened in November 2026 for a bounded upgrade: Orientation
frames in the intro and glance decks, removal of third-party and personal material (moved out to the maintainer's
private Google Drive), a cut down to what is original and complete (see `MOVED_MATERIAL.md`), a landing-page
README and licence files. The plan and its progress are in
`reports/upgrade_nontech_14112026.md` and `reports/STATUS.md` (read STATUS first in a new session).

Outside that plan, keep changes to genuine defects (broken builds, broken links, wrong facts). Do not
add CI or workflows. Personal items are flag-only. See `TODO.md` for the state each area was left in.

## Repository Purpose

BharatVidya is a study archive on Indian Knowledge Systems (IKS) under NEP 2020, centred on Yoga (the Yoga Sutra seminar system and Yoga Nidra), with curated lists on Sanskrit and the Arthashastra. The primary outputs are compiled LaTeX/PDF documents, not software applications.

## Compiling LaTeX Documents

All LaTeX compilation uses **XeTeX** (required for Devanagari and Unicode support). Each domain has a dedicated batch script in `LaTeX/`:

```bat
LaTeX\make_yogashastra.bat       # Yoga philosophy documents
LaTeX\make_yogasutra.bat         # Yoga Sutra compilations
LaTeX\make_onepagers.bat         # Summary one-pager sheets
LaTeX\make_sharada.bat           # Sharada script documents
LaTeX\make_ycb1.bat              # YCB certification materials
LaTeX\make_yoganidra.bat
```

Scripts use `texify --engine=xetex -cp` and recursively find files matching their domain's pattern, for example `Main_*_YogaSutra*.tex`. To compile a specific `.tex` file manually:

```bat
texify --engine=xetex -cp <filename>.tex
```

The decks share `LaTeX/template_presentation.tex` and `LaTeX/template_cheatsheet.tex`.

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
| `LaTeX/` | The slide system: Beamer decks, cheat sheets, topic files, images and build scripts |
| `YogaSutra/` | Notes on the Yoga Sutra, the Devanagari text, hand-drawn mind maps (`mindmaps/`), `SOURCES.md` and a long video list (`README.md`) |
| `YogaNidra/` | Yoga Nidra overview (`README.md`), notes, a detailed practice script and a research reading list |
| `Yoga/` | A curated list of Yoga resources (`README.md`) and a meditation note |
| `Samskrit/` | Curated lists on Sanskrit and the Arthashastra, and a reading list of papers on Sanskrit and computing |
| `reports/` | The upgrade plans and `STATUS.md` (read it first) |

Everything else that used to be here was moved out; see `MOVED_MATERIAL.md`.

## LaTeX Conventions

- Documents targeting Devanagari **must** use XeTeX, not pdflatex.
- Beamer presentation sources follow the pattern `Main_*_BharatVidya*.tex` for auto-discovery by build scripts.
- The `/upgrade-deck` slash command is available for structured review and improvement of Beamer presentations in this repo.

## YogaSutra Seminar System

The YogaSutra material in `LaTeX/` is structured as **1 workshop + 6 independent seminars**, each with a matching cheat sheet.

**Presentations (built by `make_yogasutra.bat`, glob: `Main_*_YogaSutra*.tex`):**

| File | Title |
|------|-------|
| `Main_Workshop_YogaSutra_Presentation.tex` | Full workshop (all 5 chapter seminars) |
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

## YogaShastra Beamer Presentation

The main workshop deck is `LaTeX/Main_Workshop_YogaShastra_Presentation.tex`. Its content is modularized via `LaTeX/workshop_yogashastra_content.tex`, which `\input`s individual topic files.

**Slide format conventions:**
- Section title frame: `{\Large Title}` centered with `{\tiny (Ref: ...)}` footer
- Content frames: `\begin{frame}[fragile]\frametitle{...}` with `\begin{itemize}\item...\end{itemize}`
- All Marathi content stays in Marathi (do not translate)
- Font: Nakula (Devanagari), loaded via `\devanagarifont`

**Current `\section[Teachings]{Other Teachings}` files** (in order): `yogashastra_yogoda`, `yogashastra_shrim`, `yogashastra_zenoga`, `yogashastra_vinod`, `yogashastra_desikachar`, `yogashastra_shrimath`, `yogashastra_osho`, `yogashastra_watwe`, `yogashastra_nirvana_shatakam`, `yogashastra_rakesh`, `yogashastra_sivasankaran`, `yogashastra_shivkrupanand`, `yogashastra_sadhana`.

**Transcript-to-slides workflow:** When a `.md` file containing a video transcript is placed in `LaTeX/`, convert it to a `yogashastra_<name>.tex` Beamer file (strip timestamps of format `H:MMM seconds` or `M:SS minute, N seconds`; summarize to bullet points in Marathi; keep essence without over-compression). Add `\input{yogashastra_<name>}` to `workshop_yogashastra_content.tex`. Delete the source `.md` file after the `.tex` is created. Recompile to verify.
