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

- [x] **Tier 1 (Samskrit Bharati institutional course packs, ~2.3GB)** moved to `Tier1_SamskritBharati/`: `SamskritBharatiAll_Vanisri/` (549 files), `SamskritBharatiAll_NiveditaR/` (187 files), `SamskritBharatiAll_ExamPapers/` (68 files), `ParichayaVyoma/` (22 files), plus 6 loose institutional handout/textbook/exam-paper files.
- [x] **Tier 2 (published books/study guides, 46MB)** moved to `Tier2_PublishedBooks/`: 6 "Enjoyable Sanskrit Grammar" volume/workbook/key files + 11 "Study Guide to Laghu Siddhanta Kaumudi" part files, all from `Samskrit/Courses/Arshaavanish/`.
- [x] Verified: `Samskrit/Courses/` dropped from 2.6GB to 245MB; no `.tex` or markdown file in the repo referenced any of the moved paths, so nothing broke.
- [ ] **Not yet decided:** `Sanskrit_Alphabet_VolI.pdf` / `Sanskrit_Alphabet_VolII.pdf` in `Arshaavanish/` look like they may belong to the same published series as Tier 2, but weren't part of the originally-scoped move; left in place pending your call.
- [ ] **Tier 3 (instructor-taught class notes you attended)** left in place, your call: `ChetanaMehta/`, `NeeleshBodas/`, `Neetichandrika/`, `Chinmay_EasySanskrit_Yogesh/` (~102MB, ~175 files total).
- [ ] **Tier 4 (NIOS government material)** left in place: `NIOS_DigitizedSLM/`, `NIOS_Samskrit_246/` — plausibly already freely distributed by NIOS, but not verified.
- [ ] **Duplicates spotted, not yet cleaned up:** `Samskrit/Courses/YogeshPraveshExamAug2024/` exactly duplicates `Admin/PraveshExamAug2024/`; `Couse Sanskrit Bhasha Pravesh.zip` (31 files) is a subset already contained in `Course_Samskrit_Book.zip` (34 files, which also has your own `subantaruupaNi.tex`/`.pdf`).
- [ ] Two remaining loose zips not yet classified/actioned: `Course GrammarTutorial.zip` (third-party website PDFs) and `Course Sanskrit Bharati Correspondance.zip` (looks like your own homework submissions, lower risk).

**Reminder:** these files were moved out of the working tree, not purged from git history. If they were previously committed, a history rewrite (`git filter-repo`/BFG) is a separate action you'd take yourself if you want them gone from old commits too.

## Explicitly Out of Scope This Session (your calls)

- [ ] **`Admin/` folder** — mixes your own certificates/photos with third-party institutional syllabi PDFs and one scanned admission exam paper. Left as-is; lower stakes than the items above but still worth a look eventually.
- [ ] **Untracked file** `YogaShastra/ArticlesPapers/Breath by Hiremath Raj _ Medium.pdf` — a third-party Medium article, not yet committed. Left untracked; decide before it gets added.
- [ ] **`CLAUDE.md` domain table** documents `Arthashastra/` and `Ayurveda/` as top-level folders, but they actually live nested under `IKS/`. Not visitor-facing, but worth a fix for consistency next time `CLAUDE.md` is touched.
- [ ] **No GitHub repo Description/Topics confirmed** (requires GitHub web UI, can't be checked or set by an agent). See manual guide below if you want to set them.
- [ ] **No badges or sample screenshots** on the README — cosmetic polish, not urgent.

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
