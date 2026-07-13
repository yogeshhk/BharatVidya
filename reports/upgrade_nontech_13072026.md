# BharatVidya Non-Tech Repo Upgrade: 2026-07-13

## Done This Session

- [x] Removed two full third-party book PDFs from `YogaShastra/ArticlesPapers/`: `Book_When-breath-becomes-air.pdf` (Paul Kalanithi memoir, full text) and `Book_Zen Yoga A Creative Psychotherapy to Self-Integration - P.J Saher_text.pdf` (full book text).
- [x] Fixed two broken README.md links: Ayurveda now points to `./IKS/Ayurveda/`, Arthashastra now points to `./IKS/Arthashastra/Awesome_arthashastra.md` (previous links assumed root-level folders that don't exist; actual content lives nested under `IKS/`).
- [x] Removed the README.md line linking to `./Namami/Awesome_manuscriptology.md` — the `Namami/` folder was fully deleted in commit `3193cbd` ("Reorged files") with no replacement; the content no longer exists anywhere in the repo.
- [x] Removed the README.md line linking to `./Awesome-AI-By-Bharat.md` — this file never existed in repo history.
- [x] Cleaned em-dash characters from `README.md` (1 instance) and `LaTeX/README.md` (6 instances) per house style.
- [x] Created `CONTENTS.md` at repo root: a verified catalog of all top-level domains and their entry-point docs, linked from the root README's Introduction section.
- [x] Created `CONTRIBUTING.md` at repo root, consolidating the duplicated "how to contribute" sections that previously lived separately in `README.md` and `YogaShastra/README.md`. Both files now point to it instead.

## Sanskrit/Courses Cleanup (2026-07-13, follow-up session)

Analyzed `Samskrit/Courses/` (2.6GB) and split it into 6 risk tiers (institutional course packs, published books, instructor-taught class notes, government material, classical public-domain texts, and your own work). Moved the two highest-risk tiers out of the git working tree to `D:\Yogesh\BharatVidya_ThirdPartyArchive\` for you to keep on personal Google Drive:

- [x] **Tier 1 (Samskrit Bharati institutional course packs, ~2.3GB)** moved to `Tier1_SamskritBharati/` (uploaded to Drive and deleted locally before the folder-naming cleanup below, so it kept this name): `SamskritBharatiAll_Vanisri/` (549 files), `SamskritBharatiAll_NiveditaR/` (187 files), `SamskritBharatiAll_ExamPapers/` (68 files), `ParichayaVyoma/` (22 files), plus 6 loose institutional handout/textbook/exam-paper files.
- [x] **Tier 2 (published books/study guides, 46MB)** moved to `PublishedSanskritGrammarBooks/`: 6 "Enjoyable Sanskrit Grammar" volume/workbook/key files + 11 "Study Guide to Laghu Siddhanta Kaumudi" part files, all from `Samskrit/Courses/Arshaavanish/`.
- [x] Verified: `Samskrit/Courses/` dropped from 2.6GB to 245MB; no `.tex` or markdown file in the repo referenced any of the moved paths, so nothing broke.
- [x] You uploaded the archive to personal Google Drive and deleted the local `D:\Yogesh\BharatVidya_ThirdPartyArchive\` folder.

## Sanskrit/Courses Cleanup, Round 2 (2026-07-13, same day follow-up)

Recreated `D:\Yogesh\BharatVidya_ThirdPartyArchive\` (deleted after your Drive upload) and continued cleanup:

- [x] **Deduped `PraveshExamAug2024`:** moved the one extra file (`SB-MR-MH-N-29731-Pravesha.pdf`) from `Samskrit/Courses/YogeshPraveshExamAug2024/` into `Admin/PraveshExamAug2024/`, then deleted the now-redundant `Samskrit/Courses/YogeshPraveshExamAug2024/` folder (it exactly duplicated `Admin/PraveshExamAug2024/` otherwise).
- [x] **Deduped course zip:** deleted `Samskrit/Courses/Couse Sanskrit Bhasha Pravesh.zip` (31 files), a subset already fully contained in `Course_Samskrit_Book.zip` (34 files, which also has your own `subantaruupaNi.tex`/`.pdf` and was kept).
- [x] **Tier 3 (instructor-taught class notes) moved** to `SanskritInstructorClassNotes/`: `ChetanaMehta/`, `NeeleshBodas/`, `Neetichandrika/`, `Chinmay_EasySanskrit_Yogesh/` (~101MB total).
- [x] **`Sanskrit_Alphabet_VolI.pdf` and `VolII.pdf`** moved to `PublishedSanskritGrammarBooks/` (you chose to move both, since they're a matched pair from the same series). `Arshaavanish/` now holds only classical/derivative-analysis texts (`Astadhyayi.pdf`, `Dhatukosah.pdf`, `Grammatical Analysis of Bhagavad Gita.pdf`, `MundakaUpanisadGrammaticalAnalysis.pdf`, `Tattvbodha_Grammatical.pdf`, `VaakyaVrttihGrammatical.pdf`).
- [x] Verified: no repo file references any moved/deleted path. `Samskrit/Courses/` is now 133MB (down from the original 2.6GB across both rounds).
- [x] **Tier 4 (NIOS government material) moved** to `NIOS_GovtCourseMaterial/`: `NIOS_DigitizedSLM/`, `NIOS_Samskrit_246/`.
- [x] **`Course GrammarTutorial.zip`** (third-party "SAMSKRUTAM Studies" website PDFs) moved to `WebSanskritGrammarTutorials/`. `Samskrit/Courses/` is now 107MB, down from the original 2.6GB.
- [ ] `Course Sanskrit Bharati Correspondance.zip` looks like your own homework submissions (lower risk) and was left as-is; nothing else outstanding in `Samskrit/Courses/`.

## Admin Folder Cleanup (2026-07-13, same day follow-up)

- [x] Moved 22 third-party institutional course syllabi/brochure/lecture PDFs from `Admin/` to `InstitutionalCourseSyllabi/`: BA/MA Sanskrit syllabi, IK 501 and PGD/CDST programme syllabi, Easy Sanskrit / Vedanta / Postal Sanskrit / Bhagavad Gita / Upanishad course brochures, webinar and pre-course-test PDFs, and an IIT Mandi lecture PDF.
- [x] Kept in `Admin/`: your own certificates (digital Sanskrit, IKS intro, Easy Sanskrit Level 2, YCB Level 1), `MindMap_Sanskrit.pdf`, `Yogic Self-Awareness Assessment.pdf`, `Message_BeStrong_Vivekanand.jpg`, and the `PraveshExamAug2024/` subfolder (your own exam attempt).
- [x] Verified: no repo file links to any of the moved files (one coincidental text match in `Samskrit/Awesome_samskrit.md` is an unrelated external URL, not a broken local link).

## Archive Folder Renamed (2026-07-13)

Renamed the `Tier*` folders in `D:\Yogesh\BharatVidya_ThirdPartyArchive\` to descriptive names, since "Tier1/Tier2" reads as meaningless once copied onto Google Drive:

| Old | New |
|---|---|
| `Tier2_PublishedBooks` | `PublishedSanskritGrammarBooks` |
| `Tier3_InstructorNotes` | `SanskritInstructorClassNotes` |
| `Tier4_NIOS` | `NIOS_GovtCourseMaterial` |
| `Tier5_WebContent` | `WebSanskritGrammarTutorials` |
| `Tier6_AdminSyllabi` | `InstitutionalCourseSyllabi` |

(The first `Tier1_SamskritBharati` batch was already uploaded and deleted locally before this rename, so it's on Drive under its original name.)

**Reminder:** moved files are out of the working tree, not purged from git history. If they were previously committed, a history rewrite (`git filter-repo`/BFG) is a separate action you'd take yourself if you want them gone from old commits too. Remember to upload this new `D:\Yogesh\BharatVidya_ThirdPartyArchive\` batch to Drive too before deleting it locally.

## Final Cleanup Round (2026-07-13, same day follow-up)

- [x] Deleted the untracked third-party Medium article PDF: `YogaShastra/ArticlesPapers/Breath by Hiremath Raj _ Medium.pdf`.
- [x] Fixed `CLAUDE.md`'s "Domain Areas" table: removed the stale `Namami/` row (folder was deleted in commit `3193cbd`, same issue as the README link fixed earlier), corrected `Arthashastra/` and `Ayurveda/` to their actual nested paths under `IKS/`, and fixed the "Python / Notebook Code" section which referenced the now-nonexistent `Namami/src/opencv/` scripts (the only real Python content is two notebooks in `Samskrit/src/`). Also dropped "Manuscriptology" from the one-line repo description in `CLAUDE.md`, matching the README fix.
- [x] Added License and Last-Commit badges to the top of `README.md`.
- [x] Compiled `Main_Seminar_YogaSutra_Overview_Presentation.tex` with XeTeX, reviewed 4 candidate pages (title, principles, sutra 1.2, sutra 1.15-1.16), picked page 10 (sutra 1.2, shows Devanagari + transliteration + English commentary together) as it best demonstrates the content's format. Saved as `LaTeX/images/sample_yogasutra_slide.png` and embedded it in the README below the intro paragraph. Deleted the compiled PDF and other candidate screenshots (build artifacts, not part of repo convention).
- [x] **GitHub repo Description/Topics/social preview:** you completed all 4 manual steps from the guide below.

## Final Item Cleared (2026-07-13, same day follow-up)

- [x] `Course Sanskrit Bharati Correspondance.zip` moved to (recreated) `D:\Yogesh\BharatVidya_ThirdPartyArchive\SamskritBharatiCorrespondenceHomework\`, at your request, even though it looked like your own homework submissions. `Samskrit/Courses/` is now 104MB, down from the original 2.6GB. No repo file referenced it.

Nothing outstanding remains from the full review.

## Closing Housekeeping (2026-07-13, end of session)

- [x] Updated `CONTENTS.md`: the `Samskrit/Courses/` and `Admin/` descriptions, and the "A Note on Scale" caveat about bulk instructor material, were written before this session's cleanup rounds and were stale. Reworded to reflect the current, much smaller contents of both folders; removed the now-unnecessary caveat section.
- [x] Fixed one em-dash I introduced into `CLAUDE.md` earlier this session (line was mine to fix; the rest of `CLAUDE.md`'s pre-existing em-dashes elsewhere were not part of this review's scope and were left alone).
- [x] Re-verified every link and image path referenced in `README.md` and `CONTENTS.md` resolves on disk.

This closes the session. Nothing has been committed, per your standing instruction that git operations are yours to run.

## Manual Steps Guide (GitHub Settings — cannot be done by an agent)

If you want a repo Description, Topics, and a social preview image (all help discoverability and can't be set via files in the repo):

1. Go to `https://github.com/yogeshhk/BharatVidya`
2. Click the gear icon next to "About" on the right sidebar of the repo homepage.
3. Add a short Description (e.g. "A curated study archive on Indian Knowledge Systems: Sanskrit, Yoga, Arthashastra, and Manuscriptology under NEP 2020").
4. Add Topics (e.g. `sanskrit`, `yoga`, `indian-knowledge-systems`, `nep2020`, `latex`, `beamer`).
5. Optionally upload a social preview image under Settings > General > Social preview.

## Notes

- No git commands (status/diff/add/commit) were run as part of applying these changes, per your standing instruction that all git operations are yours to manage. You'll need to review and commit the changes above yourself.
- Two files were deleted from the working tree (the two full books). This does **not** remove them from git history if they were previously committed — a history purge (e.g. `git filter-repo` or BFG) is your call and your action if you want them gone from old commits too, not something done here.
