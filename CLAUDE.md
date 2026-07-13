# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

BharatVidya is a curated study archive on Indian Knowledge Systems (IKS) under NEP 2020, covering Sanskrit, Yoga, Ayurveda, and Arthashastra. The primary outputs are compiled LaTeX/PDF documents and structured data files, not software applications.

## Compiling LaTeX Documents

All LaTeX compilation uses **XeTeX** (required for Devanagari and Unicode support). Each domain has a dedicated batch script in `LaTeX/`:

```bat
LaTeX\make_bharatvidya.bat       # BharatVidya overview documents
LaTeX\make_yogashastra.bat       # Yoga philosophy documents
LaTeX\make_yogasutra.bat         # Yoga Sutra compilations
LaTeX\make_arthashastra.bat      # Kautilya governance documents
LaTeX\make_onepagers.bat         # Summary one-pager sheets
LaTeX\make_sharada.bat           # Sharada script documents
LaTeX\make_shrimath.bat
LaTeX\make_ycb1.bat              # YCB certification materials
LaTeX\make_yoganidra.bat
LaTeX\make_zenyoga.bat
```

Scripts use `texify --engine=xetex -cp` and recursively find files matching `Main_*_BharatVidya*.tex`. To compile a specific `.tex` file manually:

```bat
texify --engine=xetex -cp <filename>.tex
```

Shared LaTeX style/preamble files live in `Samskrit/LaTeX/` (e.g., `preamble.tex`, `shloka.sty`).

## Key Data Structure: YogaSutra Knowledge Graph

`YogaShastra/YogaSutra/YogaSutraTrees/graph.json` is a machine-readable scholarly database of the Yoga Sutras. Each node contains:
- Devanagari text + IAST transliteration
- Word-by-word analysis (anvaya)
- Multiple English translations (Bryant, Leggett, Hariharananda, Vivekananda)
- Vyasa and Vacaspati commentaries in Sanskrit and English
- Cross-reference tags

`graphold.json` in the same directory is the prior version; `graph.json` is authoritative.

## Python / Notebook Code

Minimal code exists in one location:
- `Samskrit/src/` — two Jupyter notebooks (Sanskrit shlokas dataset, Sanskrit Wikipedia articles)

No `requirements.txt` or `environment.yml` exists; the Python work is exploratory/prototype-level.

## Domain Areas

| Directory | Content |
|-----------|---------|
| `Samskrit/` | Sanskrit grammar, learning resources, LaTeX utilities |
| `YogaShastra/` | Yoga philosophy, YogaSutra JSON graph, YogaNidra, Aurobindo |
| `LaTeX/` | Compiled Beamer/article documents and build scripts |
| `IKS/` | Master in Chanakya Kautilya Studies (Bhishma_MCKS) coursework, plus nested `Arthashastra/` and `Ayurveda/` subfolders |
| `IKS/Arthashastra/` | Kautilya's governance texts and academic analysis |
| `IKS/Ayurveda/` | Traditional medicine resources |
| `Dasbodh/` | Dasbodh-by-email learning materials |
| `Admin/` | Course certificates, mindmap, and personal exam records |

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
| `Main_Seminar_YogaSutra_Intro_Presentation.tex` | Seminar 1: Introduction |
| `Main_Seminar_YogaSutra_Samadhipad_Presentation.tex` | Seminar 2: Samadhi Pada |
| `Main_Seminar_YogaSutra_Sadhanapad_Presentation.tex` | Seminar 3: Sadhana Pada |
| `Main_Seminar_YogaSutra_Vibhutipad_Presentation.tex` | Seminar 4: Vibhuti Pada |
| `Main_Seminar_YogaSutra_Kaivalyapad_Presentation.tex` | Seminar 5: Kaivalya Pada |
| `Main_Seminar_YogaSutra_Overview_Presentation.tex` | Overview (~45 slides, independent session) |

Each has a corresponding `*_CheatSheet.tex`.

**Content file architecture:**
- `workshop_yogasutra_content.tex` — inputs all chapter files for the full workshop
- `seminar_yogasutra_intro_content.tex` — intro + glance + refs
- `seminar_yogasutra_<chapter>_content.tex` — brief_intro + chapter + refs (for each of 4 chapters)
- `seminar_yogasutra_overview_content.tex` — standalone 45-slide overview covering all chapters

**Shared source files — naming: `yogsutra_*` (no 'a'), except refs:**
- `yogsutra_intro.tex`, `yogsutra_samadhipad.tex`, `yogsutra_sadhanapad.tex`, `yogsutra_vibhutipad.tex`, `yogsutra_kaivalyapad.tex`, `yogsutra_glance.tex`
- `yogsutra_brief_intro.tex` — 4-slide compact context-setter reused in each chapter seminar
- `yogasutra_refs.tex` — references (this file uses 'a': `yogasutra_refs`)

**Critical naming rule:** Source content files use `yogsutra_*` (no 'a'). Any `\input{yogasutra_*}` reference (with 'a') will break — always use `\input{yogsutra_*}` except for refs.

## YogaShastra Beamer Presentation

The main workshop deck is `LaTeX/Main_Workshop_YogaShastra_Presentation.tex`. Its content is modularized via `LaTeX/workshop_yogashastra_content.tex`, which `\input`s individual topic files.

**Slide format conventions:**
- Section title frame: `{\Large Title}` centered with `{\tiny (Ref: ...)}` footer
- Content frames: `\begin{frame}[fragile]\frametitle{...}` with `\begin{itemize}\item...\end{itemize}`
- All Marathi content stays in Marathi (do not translate)
- Font: Nakula (Devanagari), loaded via `\devanagarifont`

**Current `\section[Teachings]{Other Teachings}` files** (in order): `yogashastra_yogoda`, `yogashastra_shrim`, `yogashastra_zenoga`, `yogashastra_vinod`, `yogashastra_desikachar`, `yogashastra_shrimath`, `yogashastra_osho`, `yogashastra_watwe`, `yogashastra_nirvana_shatakam`, `yogashastra_rakesh`, `yogashastra_sivasankaran`, `yogashastra_shivkrupanand`, `yogashastra_sadhana`.

**Transcript-to-slides workflow:** When a `.md` file containing a video transcript is placed in `LaTeX/`, convert it to a `yogashastra_<name>.tex` Beamer file (strip timestamps of format `H:MMM seconds` or `M:SS minute, N seconds`; summarize to bullet points in Marathi; keep essence without over-compression). Add `\input{yogashastra_<name>}` to `workshop_yogashastra_content.tex`. Delete the source `.md` file after the `.tex` is created. Recompile to verify.
