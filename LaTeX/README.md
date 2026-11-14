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
| `make_onepagers.bat` | `Main_*_OnePager*.tex` | Summary one-pagers |
| `make_yoganidra.bat` | `Main_*_YogaNidra*.tex` | Yoga Nidra |
| `make_ycb1.bat` | `Main_*_YCB*.tex` | YCB certification |
| `make_sharada.bat` | `Main_*_Sharada*.tex` | Sharada script |

The decks share `template_presentation.tex` and `template_cheatsheet.tex` in this folder. Compiled PDFs are not stored in the repository; build them with the scripts above.

---

## YogaSutra Seminar System

The YogaSutra material is one workshop plus independent seminars, each with a corresponding cheat sheet. Page counts change as slides are added, so read them from the compiled PDFs.

### Presentations

| File | Title |
|------|-------|
| `Main_Workshop_YogaSutra_Presentation.tex` | YogaSutra Workshop (all the chapter seminars together) |
| `Main_Seminar_YogaSutra_Intro_Presentation.tex` | Introduction, including the Orientation frames drawn from the lecture notes |
| `Main_Seminar_YogaSutra_Samadhipad_Presentation.tex` | Samadhi Pada |
| `Main_Seminar_YogaSutra_Sadhanapad_Presentation.tex` | Sadhana Pada |
| `Main_Seminar_YogaSutra_Vibhutipad_Presentation.tex` | Vibhuti Pada |
| `Main_Seminar_YogaSutra_Kaivalyapad_Presentation.tex` | Kaivalya Pada |
| `Main_Seminar_YogaSutra_Overview_Presentation.tex` | Overview (independent short session) |

Each presentation has a matching `*_CheatSheet.tex` compiled as landscape A4, two-column article.

### Content File Architecture

```
workshop_yogasutra_content.tex          ← inputs all chapter files for full workshop
seminar_yogasutra_intro_content.tex     ← intro + glance + refs
seminar_yogasutra_samadhipad_content.tex ← brief_intro + samadhipad + refs
seminar_yogasutra_sadhanapad_content.tex ← brief_intro + sadhanapad + refs
seminar_yogasutra_vibhutipad_content.tex ← brief_intro + vibhutipad + refs
seminar_yogasutra_kaivalyapad_content.tex ← brief_intro + kaivalyapad + refs
seminar_yogasutra_overview_content.tex  ← standalone short overview with all chapters
```

### Shared Source Files

**Naming convention: `yogsutra_*` (no 'a' after yog)**

| File | Content |
|------|---------|
| `yogsutra_intro.tex` | Introduction: Patanjali, history, Ashtanga, key concepts, and the Orientation frames from the lecture notes |
| `yogsutra_samadhipad.tex` | Samadhi Pada sutras with Devanagari and multi-translator interpretations |
| `yogsutra_sadhanapad.tex` | Sadhana Pada: Kriya Yoga, Pancha Klesha, Ashtanga |
| `yogsutra_vibhutipad.tex` | Vibhuti Pada: Samyama, Siddhis |
| `yogsutra_kaivalyapad.tex` | Kaivalya Pada: Kaivalya, karma, liberation |
| `yogsutra_glance.tex` | Overview of the four pada grouped by topic, with Orientation frames |
| `yogsutra_brief_intro.tex` | Compact context-setter for the chapter seminars |
| `yogasutra_refs.tex` | References (note: this file uses 'a', i.e. `yogasutra_refs`) |

### References

The books and articles the slides draw on are listed in `yogasutra_refs.tex` and, with links, in
[`YogaSutra/SOURCES.md`](../YogaSutra/SOURCES.md). The PDFs themselves are not hosted here.

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
Domain:   YogaSutra | YogaShastra | YogaNidra | YCB1 | Sharada | ...
Subtype:  Intro | Samadhipad | Overview | (blank for workshop)
Format:   Presentation | CheatSheet
```
