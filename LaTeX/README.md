# LaTeX: Compiled Presentations and Documents

This folder contains all compiled Beamer presentations, article-format cheat sheets, and their build scripts for the BharatVidya repository.

## Build System

All compilation uses **XeTeX** (required for Devanagari/Unicode support):

```bat
texify --engine=xetex -cp <filename>.tex
```

Each domain has a dedicated batch script that recursively finds and compiles matching `.tex` files:

| Script | Glob pattern | Domain |
|--------|-------------|--------|
| `make_yogasutra.bat` | `Main_*_YogaSutra*.tex` | Yoga Sutra seminars and workshop |
| `make_yogashastra.bat` | `Main_*_YogaShastra*.tex` | Yoga philosophy workshop |
| `make_bharatvidya.bat` | `Main_*_BharatVidya*.tex` | BharatVidya overview |
| `make_arthashastra.bat` | `Main_*_Arthashastra*.tex` | Kautilya governance |
| `make_onepagers.bat` | `Main_*_OnePager*.tex` | Summary one-pagers |
| `make_yoganidra.bat` | `Main_*_YogaNidra*.tex` | Yoga Nidra |
| `make_ycb1.bat` | `Main_*_YCB*.tex` | YCB certification |
| `make_sharada.bat` | `Main_*_Sharada*.tex` | Sharada script |
| `make_shrimath.bat` | `Main_*_Shrimath*.tex` | Shrimath teachings |
| `make_zenyoga.bat` | `Main_*_ZenYoga*.tex` | Zen Yoga |

Shared LaTeX style/preamble files live in `Samskrit/LaTeX/` (e.g., `preamble.tex`, `shloka.sty`).

---

## YogaSutra Seminar System

The YogaSutra material is structured as **1 workshop + 6 seminars**, each with a corresponding cheat sheet.

### Presentations

| File | Title | Pages |
|------|-------|-------|
| `Main_Workshop_YogaSutra_Presentation.tex` | YogaSutra Workshop (all 5 seminars) | n/a |
| `Main_Seminar_YogaSutra_Intro_Presentation.tex` | Seminar 1: Introduction | ~75 |
| `Main_Seminar_YogaSutra_Samadhipad_Presentation.tex` | Seminar 2: Samadhi Pada | ~118 |
| `Main_Seminar_YogaSutra_Sadhanapad_Presentation.tex` | Seminar 3: Sadhana Pada | ~128 |
| `Main_Seminar_YogaSutra_Vibhutipad_Presentation.tex` | Seminar 4: Vibhuti Pada | ~129 |
| `Main_Seminar_YogaSutra_Kaivalyapad_Presentation.tex` | Seminar 5: Kaivalya Pada | ~80 |
| `Main_Seminar_YogaSutra_Overview_Presentation.tex` | Overview (independent ~45-slide session) | ~50 |

Each presentation has a matching `*_CheatSheet.tex` compiled as landscape A4, two-column article.

### Content File Architecture

```
workshop_yogasutra_content.tex          ← inputs all chapter files for full workshop
seminar_yogasutra_intro_content.tex     ← intro + glance + refs
seminar_yogasutra_samadhipad_content.tex ← brief_intro + samadhipad + refs
seminar_yogasutra_sadhanapad_content.tex ← brief_intro + sadhanapad + refs
seminar_yogasutra_vibhutipad_content.tex ← brief_intro + vibhutipad + refs
seminar_yogasutra_kaivalyapad_content.tex ← brief_intro + kaivalyapad + refs
seminar_yogasutra_overview_content.tex  ← standalone 45-slide overview with all chapters
```

### Shared Source Files

**Naming convention: `yogsutra_*` (no 'a' after yog)**

| File | Content |
|------|---------|
| `yogsutra_intro.tex` | Rich 444-line introduction: Patanjali, history, Ashtanga, key concepts |
| `yogsutra_samadhipad.tex` | Ch.1 sutras 1.1–1.51 with Devanagari + multi-translator interpretations |
| `yogsutra_sadhanapad.tex` | Ch.2: Kriya Yoga, Pancha Klesha, Ashtanga |
| `yogsutra_vibhutipad.tex` | Ch.3: Samyama, Siddhis |
| `yogsutra_kaivalyapad.tex` | Ch.4: Kaivalya, karma, liberation |
| `yogsutra_glance.tex` | Overview of all 4 chapters grouped by topic |
| `yogsutra_brief_intro.tex` | 4-slide compact context-setter for chapter seminars |
| `yogasutra_refs.tex` | References (note: this file uses 'a', i.e. `yogasutra_refs`) |

### Reference PDFs (in this folder)

- `Notes_Yoga Teacher Training yoga-sutras_Nancy.pdf`: Nancy Wile, Yoga Education Institute
- `An Overview of the Yoga Sutras - Integral Yoga Magazine.pdf`: Dr. Ananda Balayogi Bhavanani
- `Yoga Sutras of Patanjali - Wikipedia.pdf`: Wikipedia scholarly overview

---

## YogaShastra Workshop

| File | Purpose |
|------|---------|
| `Main_Workshop_YogaShastra_Presentation.tex` | Main workshop deck |
| `Main_Workshop_YogaShastra_CheatSheet.tex` | Cheat sheet |
| `workshop_yogashastra_content.tex` | Inputs individual topic files |
| `yogashastra_<name>.tex` | Individual teacher/topic files |

Current topic files (in order): `yogashastra_yogoda`, `yogashastra_shrim`, `yogashastra_zenoga`, `yogashastra_vinod`, `yogashastra_desikachar`, `yogashastra_shrimath`, `yogashastra_osho`, `yogashastra_watwe`, `yogashastra_nirvana_shatakam`, `yogashastra_rakesh`, `yogashastra_sivasankaran`, `yogashastra_shivkrupanand`, `yogashastra_sadhana`.

---

## File Naming Convention

```
Main_<Type>_<Domain>_<Subtype>_<Format>.tex

Type:     Workshop | Seminar | OnePager
Domain:   YogaSutra | YogaShastra | BharatVidya | Arthashastra | ...
Subtype:  Intro | Samadhipad | Overview | (blank for workshop)
Format:   Presentation | CheatSheet
```
