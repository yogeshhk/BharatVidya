# Yoga themes: analysis and movement plan (draft, 2026-11-14)

Status: access to the Drive `Yoga` folder, and only that folder, was granted by the author in the conversation on
2026-11-14. The survey is done and the full analysis is a private report on the author's Desktop (it names personal
items, so it is not stored here). Nothing has been moved or changed yet. Everything below is to be done one step at a
time, asking the author at each decision.

Result in short: the Drive folder is 2.17 GB; four of its folders are not yoga and make up 43 percent of it; 73 duplicate
sets waste about 362 MB; and only 19 of the 380 staged files are already in the Drive, so the staging must be moved in.

## Decided so far
- The Drive parent folder becomes `BharatVidya` (now `Yoga`), with themes inside: `YogaSutra`, `YogaNidra` (both stay as they are), `Yoga` (asana, practice and yoga philosophy), `Spirituality` (Dasbodh, Aurobindo, Sadhguru, the large e-books and the author's own diagrams), `Samskrit`, `Arthashastra`, and the master's course. The author renames the folder, because that happens above the allowed path, and then gives the new path. The FreeFileSync pair that points at `ImpDocs\Yoga` must be updated to match.

## Done in the Drive (2026-11-14, all logged and reversible)
- The author renamed the Drive folder to `BharatVidya`. Work stayed inside it.
- Themed folders created and filled: `Yoga` (practice, meditation, saved posts, articles), `YogaCertification` (certification material, the Yogalaya course, the NIOS and university curricula), `Spirituality` (Aurobindo, Sadhguru, Dasbodh, the author's own diagrams). `YogaSutra` and `YogaNidra` stayed as they were. Three yoga folders that had landed under `Samskrit` by a manual move were merged back into their themes and removed.
- Exact duplicates: 80 extra copies (362 MB) were moved, hash-checked, to a holding folder on the Desktop outside `ImpDocs`. Nothing was deleted. Keeper rule: the themed folder, then the topic folder, then the cleaner name.
- The staged files the Drive lacked (323 files, 350 MB) were copied in and hash-checked: Dasbodh into `Spirituality`, the master's course into `Bhishma_MCKS`, Indian Knowledge Systems documents into `IKS`, slide leftovers into `_SlidesArchive`, three near-duplicates into `_ToReview`. The Desktop staging copies are still there.
- The Drive folder is now 1,014 files and 2.15 GB (it was 771 files and 2.17 GB before the staged material arrived).
- Log of every action: `Desktop\BharatVidya_Drive_move_log.csv`.

## Later the same day: finished
- The Drive folders were merged into six themes (`IKS`, `Samskrit`, `Spirituality`, `Yoga`, `YogaNidra`, `YogaSutra`); every underscore folder, the Desktop staging and the duplicates holding folder were cleared after hash checks.
- The FreeFileSync Yoga pair now points at the new folder and the replica matches the Drive; the Z drive pair excludes `\ImpDocs\BharatVidya\` because Z is small.
- The author's own and public items were copied into this repository's `Yoga/`, `YogaSutra/`, `YogaNidra/` and `Samskrit/` folders, each after the author confirmed it. Third-party books, papers and recordings stay in the Drive.
- Nothing from this plan is open.

## What the author asked for
- Move what is staged on the Desktop (`BharatVidya_Moved`) into the right folders of the Drive `Yoga` folder first.
- Then analyse the Drive `Yoga` folder and report which parts could become themes in this repository.
- Fill the repository from the Drive by copying only what is generic and useful to others. Personal and copyrighted material stays in the Drive.
- Theme meanings in the repository: `YogaSutra/` is specific to the book, `YogaNidra/` is specific to the relaxation practice, `Yoga/` is the asana and philosophy side of yoga plus anything else yoga-related that is not specific, `Samskrit/` is separate. `LaTeX/` is the one mixed folder.
- Keep the Drive master small (the Z drive and the Zoho drive sync from it): deduplicate. FreeFileSync copies the Drive `ImpDocs` (source) to the GitHub `ImpDocs` (destination), so all organising happens in the Drive.

## How the Drive and this repository relate (author, 2026-11-14)
The Drive `Yoga` folder is the master: it holds everything, personal, non-personal and public. This repository holds a
subset of it, plus things the master does not have, mainly `LaTeX/` (the slides). So:
- The direction for the shared material is Drive to repository: the repository is a curated, public subset.
- Most of what is staged on the Desktop probably exists in the Drive already, because the repository was a subset of it. A blind move would create duplicates. Compare by hash first; move only what the Drive lacks, and only after that discard the Desktop copy.
- Work done only in the repository (the slides, edits to the notes, mind maps, the lists) has no master copy. Decide whether the master should receive it, or whether `LaTeX/` stays repository-only.
- Anything copied from the Drive into the repository must pass the public test; personal and copyrighted material stays in the master only.

## Steps, in order (each is a separate go-ahead)
- Grant access: add the Yoga folder's Drive path, and only that path, to the allowed list in `D:\Yogesh\GitHub\CLAUDE.md` and to the guard that enforces it. The author does this.
- Reconcile the staging with the Drive: follow `Desktop\BharatVidya_Moved\_MOVE_TO_DRIVE_MANIFEST.txt`. For every staged file, look for the same hash in the Drive `Yoga` folder. Files already there are duplicates: report them and let the author decide to drop the Desktop copy. Files the Drive lacks are copied to the right themed folder, hash-checked, and listed. Nothing is deleted until the author agrees.
- Survey the Drive `Yoga` folder: file counts and sizes per subfolder, duplicate sets by hash (inside Yoga, and against the staged material), what each folder holds, and a first sorting into own, generic public, and third-party.
- Write the analysis report from that survey and discuss it: is "Yoga" a good folder name and parent, what themes, what to merge.
- Reorganise the Drive `Yoga` folder by theme (Yoga Sutra and Yoga Nidra stay as they are), one theme at a time, with a dry run each time.
- Copy the generic material into `Yoga/` (and any other theme folder) of this repository, one theme at a time, then update its README and run the link check.
- Fix the FreeFileSync source folder if the Drive structure changed.

## First-pass analysis of what is already staged (no Drive access needed)
This sorts the 75 staged files of the old `YogaShastra` folder by what they appear to be, from names and what was seen in them.

| Group (staged folder) | What it appears to be | Proposed | Decision needed |
|---|---|---|---|
| Certification: official Yoga Certification Board documents (level syllabi, a chair-yoga syllabus, the Common Yoga Protocol, two protocol guideline versions) | public official documents of a government board | copy into `Yoga/Certification/` and link the official site | **Ask:** should certification material live in `Yoga/`? |
| Certification: a mind map of the protocol for instructors | unknown author | keep in the Drive until the author says it is theirs | **Ask:** whose is it? |
| Certification: three "Aurobindo practicals" pictures | third-party charts | stay in the Drive | none |
| Meditation: Isha Kriya instructions, a Soham mantra sheet, "Notes on Spirituality", a graphic | third-party | stay in the Drive; link in the Awesome Yoga list if public | none |
| Teacher course notes: Anahat Dhyan notes (English and Marathi) | either the author's own notes of a course or the teacher's | **Ask:** own or teacher's? If own, they could go in `Yoga/` | **Ask** |
| Articles and papers: "GoodLife" material (principles, eight limbs mind map and PDF, a picture), "The making of YogaNotes", a DIKW picture | several look like the author's own work | **Ask:** which are yours? Yours go into `Yoga/` | **Ask** |
| Articles and papers: web prints and third-party papers (Yoga Journal, a systems-engineering paper on yoga, others, one book not about yoga) | third-party | stay in the Drive; link only | none |
| Teacher folders for a Yoga Nidra course (notes, mind map, two articles) | a teacher's course material | stay in the Drive | none |
| Yoga Sutra extras: three IGNOU course blocks | an open university's course material, licence not yet checked | check the licence; copy into `YogaSutra/` if open, else link | **Ask** after the licence check |
| Yoga Sutra extras: two Wikipedia PDFs, an Integral Yoga Magazine overview, a teacher-training manual, a slide deck, a "sutras only in Sanskrit" PDF, a Samadhi sketchnote | third-party, except possibly the sketchnote | stay in the Drive; link where public | **Ask:** is the sketchnote yours? |
| Yoga Sutra extras: the YogaSutraTrees copy | Giacomo De Luca's project | link to upstream only (already done) | none |
| Yoga Sutra extras: working backups of the notes | the author's drafts | stay in the Drive | none |
| The root picture `Sadhana.png` (2 MB) | unknown | **Ask** | **Ask** |

## What may become repository content, by theme (to confirm after the survey)
- `Yoga/`: certification documents (public), the author's own articles and mind maps, the meditation note, more entries in the Awesome Yoga list.
- `YogaSutra/` and `YogaNidra/`: only if the survey finds more of the author's own material; the rest is linked.
- Other themes seen in the Drive may need their own folder: this is the point of the survey.

## Decisions I will ask for, one at a time
- Do you want certification material in `Yoga/`, as `Yoga/Certification/`?
- Which of the staged GoodLife, YogaNotes, sketchnote, mind-map and `Sadhana.png` files are yours?
- The Anahat Dhyan notes: yours or the teacher's?
- IGNOU course blocks: copy or link, after the licence check.
- Where do the non-yoga batches (Dasbodh, Sanskrit courses, IKS, Bhishma) live in the Drive? They do not belong in a Yoga folder; they need sibling folders outside it, which this task cannot reach.
- Whether the Drive folder should keep the name `Yoga`.
