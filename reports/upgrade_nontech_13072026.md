# BharatVidya Non-Tech Repo Upgrade: 2026-07-13

## Done This Session

- [x] Removed two full third-party book PDFs from `YogaShastra/ArticlesPapers/`: `Book_When-breath-becomes-air.pdf` (Paul Kalanithi memoir, full text) and `Book_Zen Yoga A Creative Psychotherapy to Self-Integration - P.J Saher_text.pdf` (full book text).
- [x] Fixed two broken README.md links: Ayurveda now points to `./IKS/Ayurveda/`, Arthashastra now points to `./IKS/Arthashastra/Awesome_arthashastra.md` (previous links assumed root-level folders that don't exist; actual content lives nested under `IKS/`).
- [x] Removed the README.md line linking to `./Namami/Awesome_manuscriptology.md` — the `Namami/` folder was fully deleted in commit `3193cbd` ("Reorged files") with no replacement; the content no longer exists anywhere in the repo.
- [x] Removed the README.md line linking to `./Awesome-AI-By-Bharat.md` — this file never existed in repo history.
- [x] Cleaned em-dash characters from `README.md` (1 instance) and `LaTeX/README.md` (6 instances) per house style.
- [x] Created `CONTENTS.md` at repo root: a verified catalog of all top-level domains and their entry-point docs, linked from the root README's Introduction section.
- [x] Created `CONTRIBUTING.md` at repo root, consolidating the duplicated "how to contribute" sections that previously lived separately in `README.md` and `YogaShastra/README.md`. Both files now point to it instead.

## Explicitly Out of Scope This Session (your calls)

- [ ] **`Samskrit/Courses/` (2.6GB)** — large volume of instructor course materials (question papers, answers, class notes, presentations) across multiple named instructors. Likely the single biggest attribution/redistribution risk and size driver in the repo. Needs its own dedicated conversation about what to keep, move, or remove.
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
