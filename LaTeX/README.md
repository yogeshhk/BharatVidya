# LaTeX: Presentations and Documents

This folder holds the Beamer presentations, article-format cheat sheets and build scripts of the BharatVidya repository, grouped by topic.

## Folder map

| Folder | What it holds |
|---|---|
| `books/YCB1/workshop/` | The Yoga Certification Board Level 1 (Yoga Protocol Instructor) workshop: drivers, the `ycb1_*` topic files, its own `images/`, `make_ycb1.bat` |
| `workshops/YogaSutra/` | The Yoga Sutra workshop, with its seminars in `seminars/` (Intro, Samadhipad, Sadhanapad, Vibhutipad, Kaivalyapad, Overview) |
| `workshops/YogaNidra/` | The Yoga Nidra seminar (the guided practice: theory, instructions, teaching) |
| `workshops/Sharada/` | The Sharada script seminar |
| `workshops/YogaShastra/` | The retired omnibus deck, kept as a source of topic files; not built |
| `onepagers/` | The summary one-page cheat sheets |
| `_shared/` | The two templates, the Yoga Sutra topic files used by more than one deck family (`topics/`), and the images used by more than one family (`images/`) |
| `_leftovers/` | Files and images that no deck uses; kept, not deleted |
| `books/YCB1/` | The YCB Level 1 textbook (parked as a 2027 project): notes (the master), `book/` (LaTeX build), image register, the Board's syllabus copies, README, TODO and authoring rules |

Each family keeps its own images in its own `images/` folder. Images used by several families sit in `_shared/images/`.

## Build system

All compilation uses **XeTeX** (required for Devanagari and Unicode support). Run each driver from its own folder, because the sources use relative paths:

```bat
texify --engine=xetex -cp <filename>.tex
```

Each family has a batch script that finds and compiles its drivers, each from its own folder. `make_all.bat` in this folder runs every live family.

| Script | Pattern | Family |
|--------|---------|--------|
| `workshops/YogaSutra/make_yogasutra.bat` | `Main_*_YogaSutra*.tex` (including `seminars/`) | Yoga Sutra workshop and seminars |
| `books/YCB1/workshop/make_ycb1.bat` | `Main_*_YCB*.tex` | YCB certification |
| `workshops/YogaNidra/make_yoganidra.bat` | `Main_*_YogaNidra*.tex` | Yoga Nidra |
| `workshops/Sharada/make_sharada.bat` | `Main_*_Sharada*.tex` | Sharada script |
| `workshops/YogaShastra/make_yogashastra.bat` | `Main_*_YogaShastra*.tex` | Retired, switched off |
| `onepagers/make_onepagers.bat` | `Main_*_OnePager*.tex` | One-pagers |

The decks share `_shared/template_presentation.tex` and `_shared/template_cheatsheet.tex`. Drivers reach them with a relative path (`../../_shared/` from a workshop folder, `../../../_shared/` from a seminar folder, `../_shared/` from `onepagers/`). Compiled PDFs sit beside their drivers and are not stored in the repository; build them with the scripts above.

## The three workshops

| Workshop | Deck | What it is for |
|---|---|---|
| Yoga certification | `books/YCB1/workshop/Main_Workshop_YCB1_*` | The Yoga Certification Board Level 1 syllabus: theory units, asana demonstration, teaching skills |
| Yoga Sutra | `workshops/YogaSutra/Main_Workshop_YogaSutra_*` and its seminars | The text, pada by pada |
| Yoga Nidra | `workshops/YogaNidra/Main_Seminar_YogaNidra_*` | The guided practice: theory, instructions, teaching |

## Yoga Sutra workshop and seminars

The Yoga Sutra material is one workshop plus independent seminars, each with a corresponding cheat sheet. Page counts change as slides are added, so read them from the compiled PDFs.

### Presentations

| File | Title |
|------|-------|
| `workshops/YogaSutra/Main_Workshop_YogaSutra_Presentation.tex` | Yoga Sutra Workshop (all the chapter seminars together) |
| `workshops/YogaSutra/seminars/Main_Seminar_YogaSutra_Intro_Presentation.tex` | Introduction, including the Orientation frames drawn from the lecture notes |
| `workshops/YogaSutra/seminars/Main_Seminar_YogaSutra_Samadhipad_Presentation.tex` | Samadhi Pada |
| `workshops/YogaSutra/seminars/Main_Seminar_YogaSutra_Sadhanapad_Presentation.tex` | Sadhana Pada |
| `workshops/YogaSutra/seminars/Main_Seminar_YogaSutra_Vibhutipad_Presentation.tex` | Vibhuti Pada |
| `workshops/YogaSutra/seminars/Main_Seminar_YogaSutra_Kaivalyapad_Presentation.tex` | Kaivalya Pada |
| `workshops/YogaSutra/seminars/Main_Seminar_YogaSutra_Overview_Presentation.tex` | Overview (independent short session) |

Each presentation has a matching `*_CheatSheet.tex` compiled as landscape A4, two-column article.

### Content file architecture

```
workshop_yogasutra_content.tex           (workshops/YogaSutra)  inputs all chapter files for the full workshop
seminar_yogasutra_intro_content.tex      (seminars/)  intro + glance + refs
seminar_yogasutra_samadhipad_content.tex (seminars/)  brief_intro + samadhipad + refs
seminar_yogasutra_sadhanapad_content.tex (seminars/)  brief_intro + sadhanapad + refs
seminar_yogasutra_vibhutipad_content.tex (seminars/)  brief_intro + vibhutipad + refs
seminar_yogasutra_kaivalyapad_content.tex (seminars/) brief_intro + kaivalyapad + refs
seminar_yogasutra_overview_content.tex   (seminars/)  standalone short overview with all chapters
```

### Shared source files

**Naming convention: `yogsutra_*` (no 'a' after yog)**

| File | Where | Content |
|------|-------|---------|
| `yogsutra_intro.tex` | `_shared/topics/` | Introduction: Patanjali, history, Ashtanga, key concepts, and the Orientation frames from the lecture notes |
| `yogsutra_samadhipad.tex` | `_shared/topics/` | Samadhi Pada sutras with Devanagari and multi-translator interpretations |
| `yogsutra_sadhanapad.tex` | `_shared/topics/` | Sadhana Pada: Kriya Yoga, Pancha Klesha, Ashtanga |
| `yogsutra_vibhutipad.tex` | `_shared/topics/` | Vibhuti Pada: Samyama, Siddhis |
| `yogsutra_kaivalyapad.tex` | `_shared/topics/` | Kaivalya Pada: Kaivalya, karma, liberation |
| `yogsutra_glance.tex` | `workshops/YogaSutra/` | Overview of the four pada grouped by topic, with Orientation frames |
| `yogsutra_brief_intro.tex` | `workshops/YogaSutra/` | Compact context-setter for the chapter seminars |
| `yogasutra_refs.tex` | `workshops/YogaSutra/` | References (note: this file uses 'a', i.e. `yogasutra_refs`) |

### References

The books and articles the slides draw on are listed in `yogasutra_refs.tex` and, with links, in
[`YogaSutra/SOURCES.md`](../YogaSutra/SOURCES.md). The PDFs themselves are not hosted here.

## Yoga Shastra deck (retired)

Retired as a fourth workshop: it overlapped the three above. It is no longer built (`make_yogashastra.bat` is switched off); the topic files stay in `workshops/YogaShastra/` as sources for the three workshops.

| File | Purpose |
|------|---------|
| `Main_Workshop_YogaShastra_Presentation.tex` | Main workshop deck |
| `Main_Workshop_YogaShastra_CheatSheet.tex` | Cheat sheet |
| `workshop_yogashastra_content.tex` | Inputs individual topic files |
| `yogashastra_<name>.tex` | Individual teacher or topic files |

The topic files and their order are listed in `workshop_yogashastra_content.tex`.

## File naming convention

```
Main_<Type>_<Domain>_<Subtype>_<Format>.tex

Type:     Workshop | Seminar | OnePager
Domain:   YogaSutra | YogaShastra | YogaNidra | YCB1 | Sharada | ...
Subtype:  Intro | Samadhipad | Overview | (blank for workshop)
Format:   Presentation | CheatSheet
```
