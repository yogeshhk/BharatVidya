# BharatVidya Upgrade Report: 2026-11-14

Analysis only. No repository file was changed while preparing this report, apart from one change the
owner asked for during the review: the duplicate `YogaShastra/YogaSutra/Notes_YogaSutra.md` was
removed so that `Notes on Yogasutra.md` (the Google Docs name) is the only notes file. No git command
was run. Everything below waits for approval; execution is meant for Sonnet, one task at a time.

**What was checked, and how**

- Every file in the working tree was listed with its size (1,493 files, 2.12 GB). The `.git` folder
  was sized but not read (4.88 GB).
- Duplicates: every file that shares its byte size with another was hashed with SHA-256. Only
  byte-identical files are reported as duplicates (80 sets, 115.5 MB redundant). See Appendix A.
- LaTeX: the `\input` graph was walked from all 32 `Main_*` drivers, commented lines ignored; every
  `\includegraphics` target was resolved; build scripts were matched against drivers.
- Markdown: every relative link was resolved on disk; em dashes were counted in public files.
- Personal data: text files were scanned for phone numbers and email addresses; a handful of PDFs
  with personal-looking names were checked for markers (counts only, no content copied here).
- Facts: the README, CONTENTS, LaTeX README, CLAUDE.md, TODO.md and the Yoga Sūtra intro deck were
  read against what is on disk. Nothing was compiled; compiling needs your go-ahead.
- The July 2026 report (`reports/upgrade_nontech_13072026.md`) was read so that finished work is not
  proposed again.

---

### 📋 Repo Understanding

BharatVidya is a public study archive on Indian Knowledge Systems: Yoga philosophy, Sanskrit,
Arthashastra, Dasbodh and IKS coursework. Its genuinely original, high-value content is small and
strong:

- the **Yoga Sūtra slide system** (one workshop and six seminars, each with a cheat sheet, plus a
  one-pager), and the other Beamer decks (Yoga Shastra, Yoga Nidra, Zen Yoga, YCB Level 1, Sharada,
  Shrimath, Arthashastra, Bharat Vidya);
- the **Notes on Yogasutra** booklet and the other `Notes_*.md` files;
- the hand-drawn **Yoga Sūtra mind maps** (`YogaSutra/YogeshGDraws`);
- curated **Awesome lists** for Sanskrit, Arthashastra and Yoga.

Around that core sits a large mass of downloaded third-party material: books, course packs, audio
recordings, saved web pages and papers. It makes up most of the 2.12 GB working tree, and git history
adds 4.88 GB more, so a visitor who clones the repo downloads about 7 GB to read a few hundred
kilobytes of original work. The README still says the repo is a closed, finished archive.

For a stranger landing on the page today: the hook is generic, there is no way to see a finished deck
without installing XeTeX, and the size and the copyright exposure work against the goal of
popularity.

---

### 🚨 Critical Issues

**C1. Third-party copyrighted material redistributed publicly (largest issue).**
The July session cleaned `Samskrit/Courses` and `Admin`. The same kind of material remains elsewhere,
sometimes the very same books. Grouped by risk (sizes measured):

| Tier | What it is | Where (size) |
|---|---|---|
| A: full commercial books and recordings | Published books, scans of print editions, commercial audio | `YogaShastra/YogaNidra/Audio` (250.3 MB, 16 recordings) and `YogaNidra/TheYogaPodcastYogaNidra.mp3`; `YogaShastra/Meditation` recordings (about 44 MB); `YogaShastra/MHThaker` (95.7 MB, a teacher's course recordings and handouts); `YogaShastra/Iyengar` (40.6 MB); `YogaShastra/Aurobindo` (12.4 MB); `YogaShastra/Sadhguru` (3.1 MB); `Certification/Book_Hatha-Yoga-Pradipika-Muktibodhananda.pdf` (8.3 MB); `Certification/YCBOfficial/Book_YCB_Instructtor_Official.pdf` and `Yogalaya/yoga_certification_Book .pdf` (30.6 MB each); `YogaSutra/ArticlesPapers/Book_*` (Taimni, Pathway to God, Kolhatkar, a scan; about 37 MB); three copies of Satyananda's *Yoga Nidra*, two of them named after a pirate-library source (`zliborg`); `Samskrit/Grammar/Book_*` school and Samskrit Bharati textbooks (over 150 MB) and leftover *Enjoyable Sanskrit Grammar* volumes that the July session had already moved out of `Samskrit/Courses`; `Samskrit/Classics/Book_*`; `IKS/Arthashastra` translations and scans (181 MB); `Dasbodh/References` (81.6 MB) |
| B: institutional course material | Course packs and lecture PDFs from NIOS, Yogalaya, Bhishma MCKS, Dasbodh-by-email, YCB | `YogaShastra/NIOSYoga` (34.1 MB; the July session moved the NIOS Sanskrit material out, so this is inconsistent); `YogaShastra/Yogalaya` handouts (most of 97 MB); `IKS/Bhishma_MCKS` lecture PDFs (most of 78.6 MB; your own `Sem*_Notes` files are yours); `Dasbodh/Assignments` course PDFs; `YogaShastra/RamKishore` (4.5 MB); YCB syllabi and guidelines (public, low risk); `YogaSutra/IGNOU` (6.0 MB; IGNOU material is often openly licensed: check the licence before deciding) |
| C: saved web pages | Blog posts, website pages and forum threads printed to PDF | `YogaShastra/YogicJourney` (57.6 MB of Medium posts; the July session deleted one Medium PDF for this reason); `YogaSutra/SwamiJ` (21.9 MB); `YogaSutra/StudyGroup`, `Maayboli`, `AthaYoga` (about 6 MB); two Wikipedia PDFs |
| D: academic papers and journals | Papers, theses, journal issues | `Samskrit/Papers` (111.8 MB), `YogaNidra/Papers` (31.6 MB), `Samskrit/Magazines` (24.0 MB). Many are open access; lower risk, but links serve readers just as well |

Also third party, and easy to miss: `Samskrit/LaTeX/subantaruupaNi.tex` is another author's work (it
carries their own email in the source), and `YogaSutra/YogaSutraTrees` is Giacomo De Luca's project
(graph data, viewer page and a `CNAME` file belonging to their site). Neither has a licence or
attribution file in this repo; check the upstream licences before keeping them.

The repo's `LICENSE` is MIT. MIT is a software licence and cannot cover anyone else's books; it also
fits slide decks and notes poorly (see I3).

**C2. Clone size.** Working tree 2.12 GB plus git history 4.88 GB. Moving files out of the tree (C1)
fixes the browsing experience but not the clone size; files deleted in July are still in history.
Only a history rewrite fixes it, and that is your action (see Manual Steps).

**C3. Personal information in a public repo.** Listed separately below; flag only.

**C4. Wrong or stale facts.**

- `README.md` lists Philosophy, Science and Mathematics among the repo's areas; no such content
  exists. It also still declares the repo a finished archive with no roadmap.
- `TODO.md` and `CLAUDE.md` say the repo is closed and that no new content or restructuring should be
  proposed. Superseded by the owner on 2026-11-14.
- `LaTeX/README.md` says three reference PDFs live "in this folder"; they are in
  `YogaShastra/YogaSutra/ArticlesPapers`.
- `CLAUDE.md` and `LaTeX/README.md` say the decks' shared style files live in `Samskrit/LaTeX`. The
  drivers actually use `LaTeX/template_presentation.tex` and `LaTeX/template_cheatsheet.tex`;
  `preamble.tex` and `shloka.sty` serve only the standalone `subantaruupaNi.tex` document.
- `LaTeX/yogsutra_intro.tex`, the deck's own introduction:
  - It calls Patañjali "the father of Yoga". The deck's own notes, and the scholarly view, present
    him as the compiler who put existing teaching in order.
  - It dates him "between 200 and 500 B.C.". The usual scholarly dating puts the grammar in about the
    2nd century BC and the Yoga Sūtra in about the 2nd to 5th centuries AD, often given as about
    400 AD.
  - It has typos: "Patajali", "अनुशाशन" for अनुशासन, and "जगन" for जगत्.
  - It attributes the medical work as "चरकसंहिता (?)". This should be marked as the tradition's
    attribution, not a fact.
- Sutra count: `yogsutra_intro.tex` says "Total 195" while `yogsutra_brief_intro.tex` says "195/196".
  Use one wording, for example "195 or 196, depending on the recension".
- `Samskrit/Classics/NIOS_SanskritSahitya_Book-2.pdf` is byte-identical to `Book-1`: the real Book 2
  is missing.
- `YogaShastra/MHThaker`: "03_3 srb with 1-2-3-5-6 5 minutes with counting.mp3" and
  "07_3 srb with 1-2-3-5-6 5 minutes.mp3" are byte-identical, so one of them is mislabelled.
- `LaTeX/yogsutra_glance.tex` (the chapter-overview frames used at the end of the Intro seminar and the
  Workshop) uses headings that appear to follow Swami J's clustered outline, with no Ref line. Verify
  the source and add a reference.

**C5. House-style breaks.**

- **Em dashes.** They appear in `CLAUDE.md` (8), `YogaShastra/Meditation/Notes_Meditation.md` (2) and
  the July report (4). Five deck titles that print on title slides also contain them: the four pāda
  seminars and the Kaivalya seminar.
- **Hard-typed numbering.** It conflicts with the all-repos rule in `GitHub/CLAUDE.md`. Examples: the
  seminar titles "Seminar 1" to "Seminar 5", the glance frames "#3 of 8 Rungs", and the file name
  `IKS/2_Integral Yoga Vedanta Sutras.PDF`.

---

### 🔒 Personal & Sensitive Information Flags

Listed for your decision only. Nothing here is moved or deleted by any task below, even under a
"proceed with all" approval.

| File/Folder | What was found | Why it's flagged |
|---|---|---|
| `YogaShastra/Yogalaya/Yogalaya_Level1_course_form_YogeshKulkarni.pdf` | A filled course form; its text contains your name and two phone numbers | Personal contact details in a public repo |
| `YogaShastra/Yogalaya/DiaryYogeshK.xlsx` | A personal practice diary (not opened) | Personal record |
| `YogaShastra/Yogalaya/Assignment 1..6 YogeshK.docx`, `AssignmentsYogeshK.docx`, `NotesYogeshK.docx`, `Notes_Yogalaya_YogeshK.docx`, `Yogalaya_Level1_course_guidelines_YogeshKulkarni.pdf` | Your own course submissions and notes, named | Coursework record; your call whether it is public |
| `Samskrit/Courses/Vagvipaka/Vagvipaka Certificate  Yogesh Kulkarni .pdf`, `Vagvipaka_Exam.pdf` | A certificate (image) and an exam record | Certificates and exam records |
| `Dasbodh/Assignments/Prashna- manjusha yogesh kulkarni.(docx,pdf)`, `Dasbodh/Assignments/Pravesh/swadhya N samikshan kulkarni.pdf` (13 scanned files) | Your homework and its assessment, named | Coursework record |
| `IKS/IndianKnowledgeSystems/IMG-20260226-WA0001.jpg` | A WhatsApp image, content not checked | May show people or private chat content |
| `LaTeX/ycb1_exam.tex`, `LaTeX/images/ycb1_exam_i.jpg`, `_ii.png`, `_iii.png` | Exam-related deck source and screenshots (the images are unused) | Check whether they reproduce an exam paper |
| Every `Main_*` driver and `template_cheatsheet.tex` | Your contact email in the footer | Probably deliberate; confirm you want it published |
| `.claude/settings.local.json` | Local tool permissions, including file paths and the name of your off-repo archive folder | Machine-local file; check whether it is tracked (`git ls-files .claude`); if so, untrack it and ignore it |

---

### 🗂️ Proposed Structural Changes

**LaTeX folder: keep it flat; tidy it.** A sub-folder per domain was considered and is not
recommended. The build scripts, every `\input{...}` and the `images/` path assume a flat folder, and
your other repos (TeachingDataScience) use the same flat layout, so moving files would mean editing
more than a hundred paths for no reader-visible gain. The folder is already healthy: all 32 drivers
resolve, no image is missing, every Presentation has its CheatSheet, and there are no build leftovers.
What it needs is tidying:

| Action | File/Folder | Reason |
|---|---|---|
| Remove (duplicate, unused) | `LaTeX/preamble.tex`, `LaTeX/shloka.sty`, `LaTeX/subantaruupaNi.tex` | Byte-identical to the copies in `Samskrit/LaTeX`; no driver uses them |
| Decide: wire in or retire | `LaTeX/ycb1_theory_faqs.tex` (66 KB), `LaTeX/yogashastra_meditation.tex` (28 KB), `LaTeX/yogashastra_sankhya.tex` (96 KB; the deck uses `yogashastra_sankhya_short`) | Not reachable from any driver |
| Move to `LaTeX/_retired/images/` | 78 images in `LaTeX/images` that no reachable file uses (8.8 MB) | Clutter; kept, not deleted, in case a retired topic returns |
| Move out of content folders | `YogaShastra/Certification/Main_Workshop_YCB1_*.pdf` (34.3 MB), `YogaShastra/YogaNidra/Main_Seminar_YogaNidra_*.pdf` (6.5 MB), `YogaShastra/YogaSutra/Main_OnePager_YogaSutra_CheatSheet.pdf` | Build outputs of drivers in this repo; publish compiled PDFs as Release assets instead (see I2) |

Dry run for the image move: 78 files, 8.8 MB, from `LaTeX/images/` to `LaTeX/_retired/images/`.
The list is regenerated at execution time from the same reachability check, and a test compile of one
driver per domain runs before and after.

**Third-party material (C1): move out of the repo, replace with links.** This follows the July pattern,
moving to `D:\Yogesh\BharatVidya_ThirdPartyArchive\` for you to keep on Google Drive. Each tier gets
its own decision. Dry run per tier: an exact file list and total size, a check that no `.md` or `.tex`
file links to a moved path, then a listing of the archive destination. Each moved folder is replaced by
a short `README.md` of links to the official sources (publisher pages, NIOS, IGNOU, Medium, swamij.com)
so readers still find the material.

| Tier | Approximate scope | Recommended default |
|---|---|---|
| A | about 1 GB across the folders listed in C1 | Move out |
| B | about 250 MB | Move out, except openly licensed items (check IGNOU) and your own notes |
| C | about 90 MB | Move out; links only |
| D | about 170 MB | Your choice: keep open-access papers, or replace all with a reading list |

**Internal working material in the public tree.**

| Action | File/Folder | Reason |
|---|---|---|
| Decide | `YogaShastra/YogaSutra/_backup/` (your original notes and the pre-final version) | Working backups, not reader content |
| Decide | `Code/claudecode/commands/` (your Claude Code commands) and `reports/` | Tooling and maintenance logs; fine to keep public, but they are not content. If kept, mention them in CONTENTS |

---

### ♻️ Clutter & Redundancy Findings

- **Duplicates.** There are 80 byte-identical sets, 115.5 MB redundant. They are mostly the Swami J
  site PDFs saved twice or three times, NIOS chapters copied into `Yogalaya`, "Article"-prefixed
  copies of papers, `_1` copies, and the same book under two names. Appendix A gives every set with a
  suggested copy to keep. Sets inside folders that a C1 decision moves out need no de-duplication.
- **Two copies of the same text.** `YogSutra_Devnagari_clean.txt` and
  `StudyGroup/YogSutra_Devnagari.txt` are byte-identical.
- **Old versions beside current ones.** `YogaSutraTrees/graphold.json` and `indexold.html` sit beside
  `graph.json` and `index.html`.
- **Oversized files.**
  - `YogaSutraTrees/bg8.jpg` is an 8.4 MB background image.
  - `YogaShastra/MHThaker/02_ attentive tension relaxation...rtf` is a 19.1 MB RTF.
- **Near-empty files.** `Dasbodh/README.md` is 16 bytes. `Samskrit/LaTeX/README.md` (36 bytes) and
  `Notes.md` (146 bytes) say almost nothing.
- **Build scripts.** `make_yogasutra.bat` also matches `Main_OnePager_YogaSutra_CheatSheet.tex`, so a
  full build compiles that one-pager twice (once more through `make_onepagers.bat`). This is harmless
  but wasteful.

---

### 💡 Improvement Suggestions (popularity)

- **I1. Rewrite the README as a landing page.** Open with one line on what this is and who it is for,
  then a short gallery of three sample slides: the sample slide already exists, and two more would be
  rendered and checked by eye before use. Then a "Start here" path for three readers: a student, a
  yoga teacher, a researcher. Link the Notes on Yogasutra booklet, the decks (as downloadable PDFs),
  the mind maps and the Awesome lists. Drop the "finished archive" banner and the areas that do not
  exist. Avoid hard-typed counts.
- **I2. Publish the compiled PDFs as GitHub Release assets.** This is the single biggest lever: today
  nobody can see a finished deck without installing XeTeX. Sonnet can build the PDFs locally (with
  your go-ahead, since the full YogaSutra set takes about 280 seconds); you upload them on GitHub as a
  release, a manual step. PDFs stay out of the tree.
- **I3. Licence your content properly.** Keep MIT for the few scripts if you like, but put the decks,
  notes and mind maps under a Creative Commons licence (CC BY-SA 4.0 is common for teaching
  material), say so in the README, and state plainly that third-party material is linked, not hosted.
  Your decision.
- **I4. Add trust signals.** Add `CITATION.cff` (so the decks and notes can be cited),
  `CODE_OF_CONDUCT.md`, and simple issue templates (a factual correction, a Sanskrit or
  transliteration fix, a new resource). No GitHub Actions or workflows.
- **I5. Make CONTENTS.md descriptive.** Once C1 is done it can describe each area by what a reader
  gets, not by folder name.
- **I6. GitHub Pages: not recommended for now.** The only interactive asset, YogaSutraTrees, is
  someone else's project and already hosted upstream; link to it instead. Revisit only if you want the
  booklet as a web page.

---

### 📚 Documentation Gaps

- No landing-page README (see I1). No `CODE_OF_CONDUCT.md`, issue templates or `CITATION.cff`.
- Subfolder READMEs are missing or near-empty for `Dasbodh`, `Samskrit/LaTeX`, `IKS/Bhishma_MCKS`,
  `YogaShastra/YogaSutra/YogeshGDraws` (the mind maps deserve a page of their own) and
  `YogaShastra/YogaSutra/YogaSutraTrees` (it needs an attribution line).
- `CLAUDE.md`, `TODO.md` and `LaTeX/README.md` need the corrections in C4.

---

### ✅ What's Already Good

- **The LaTeX system is in good health.** Every `\input` and image resolves from all 32 drivers,
  every presentation has its cheat sheet, and there are no build leftovers anywhere.
- **The headline fix from August is documented and should stay.** It is the custom section bar in
  `template_presentation.tex`.
- **The July session's work holds.** Links in README and CONTENTS resolve (re-verified today:
  zero broken relative links in any Markdown file), CONTRIBUTING has a clear third-party note, the
  badges and GitHub Description and Topics are in place, and `Admin/` is down to two harmless files.
- **Naming within the YogaSutra system is consistent** and documented.
- **The original content is distinctive.** A seven-part Yoga Sūtra seminar system with Devanāgarī,
  transliteration and multi-translator commentary is rare on GitHub, and the Notes on Yogasutra
  booklet is ready to sit beside it.

---

## Content task: put the Orientation material into the Yoga Sūtra deck

You asked for this earlier and it is **not done yet**. The transcript-based material is in
`YogaShastra/YogaSutra/Notes on Yogasutra.md` (the Orientation section). It belongs only in the
deck's general parts: the Introduction and the end. **The four pāda files (`yogsutra_samadhipad`,
`_sadhanapad`, `_vibhutipad`, `_kaivalyapad`) are not touched.**

Where it goes:

- **`LaTeX/yogsutra_intro.tex`.** Used by the Intro seminar and the Workshop. New frames go after the
  existing "Panini and Patanjali" frame:
  - "An Impossible Place to Start": the Newton analogy, 196 compressed lines, the three āsana lines,
    "someone else's notes from a lecture you never attended";
  - "How the Sūtra Reached Modern Yoga": the invocation, the long neglect and the 19th-century
    revival, the Aṣṭāṅga naming, "where the modern story of yoga decided to begin";
  - "Patañjali: A Point of View": three works centuries apart, the university analogy;
  - "The Birth of Patañjali": Ananta Śeṣa, Goṇikā, *pat* plus *añjali*;
  - "The Endless Remainder": Śeṣa as remainder and support, *ananta* in 2.47, the seer as the
    remainder, the añjali gesture;
  - "The River and the Whirlpool": *cit*, *citta*, *prakṛti*, *nirodha*, as an orientation frame,
    not a verse frame.
  The same edit fixes the C4 facts in this file.
- **`LaTeX/yogsutra_glance.tex`.** This is the "Towards End" section of the Intro seminar and the
  Workshop. New frames go after the Kaivalya overview frames, before the references:
  - "Two Ways of Reading: Sun and Moon": remove versus fill, *kaivalya*, the Nandi egg, Śiva's dance;
  - "Headset or Dream": with the two endings of 4.34;
  - "If You Are Not Planning to Become a Monk": the whirlpool in an argument, distance and choice,
    "you experience the world the way you breathe";
  - "An Acceptable Place to End": the closing frame.
- **Each new frame gets the deck's usual `\tiny{(Ref: ...)}` line,** naming the lecture ("I Was Told
  Patanjali Founded Yoga. Then I Read His Book.", Miska Käppi).
- **Claims that stay off the slides until checked:** the 700-year figure from David Gordon White,
  Vivekananda's view of postures, and the Northwestern breathing study. Alternatively they go on with
  "reported" wording.
- **Compile scope (after your go-ahead):**
  - `Main_Seminar_YogaSutra_Intro_Presentation` and its cheat sheet;
  - `Main_Workshop_YogaSutra_Presentation` and its cheat sheet.
  The chapter seminars use `yogsutra_brief_intro`, which is unchanged, so they need no rebuild.

---

## Task list (approve per item; execution by Sonnet, one at a time)

Decision items are asked one at a time, each with options and a recommendation.

- [ ] **T1. Deck content (owner's priority).** Add the Orientation frames to `yogsutra_intro.tex` and
  `yogsutra_glance.tex` and fix the C4 facts in `yogsutra_intro.tex`. Compile the four documents
  listed above, verify the pages, and copy the PDFs where you want them. Risk: low; it touches two
  files.
- [ ] **T2. Decision: third-party tiers (C1).** One question per tier. For each approved tier: dry
  run, move to the off-repo archive, add a links README in place, then verify no broken references.
- [ ] **T3. De-duplicate** the sets in Appendix A that remain after T2. Before each removal, grep for
  references; afterwards, list the folder.
- [ ] **T4. LaTeX tidy.** Remove the three duplicate shared files from `LaTeX/`. Decide on the three
  orphan topic files. Move the 78 unused images to `LaTeX/_retired/images/`. Run one test compile per
  domain.
- [ ] **T5. Fix stale facts and style** in `README.md`, `CONTENTS.md`, `TODO.md`, `CLAUDE.md` and
  `LaTeX/README.md`, including the em dashes and the "closed" status. Also fix the em dashes and
  numbering in the deck titles, which needs a compile of the affected drivers.
- [ ] **T6. README landing page (I1)**, with a checked screenshot gallery and verified links.
- [ ] **T7. Decision: licence (I3).** Then add `CITATION.cff`, `CODE_OF_CONDUCT.md` and issue
  templates (I4). No workflows.
- [ ] **T8. Release PDFs (I2).** Build all decks (with go-ahead) and hand you the set for a GitHub
  Release. Remove the five compiled PDFs from content folders.
- [ ] **T9. Small fixes.**
  - Delete the duplicate Devanāgarī text.
  - Decide `graphold.json` and `indexold.html`.
  - Add YogaSutraTrees attribution.
  - Fill the near-empty READMEs.
  - Fix the NIOS Book-2 copy and the MHThaker mislabel (your knowledge needed).
  - Rename `2_Integral Yoga Vedanta Sutras.PDF`.
- [ ] **T10. Decision: personal flags** (the table above). Owner only; nothing happens without an
  explicit instruction per file.
- [ ] **T11. Decision: internal folders** (`_backup`, `Code/claudecode`, `reports`, `.claude`).

Suggested order: T1 first (your priority, and independent of the rest), then T10 and T2 (they
decide what stays), then T3, T4, T5, T9, T6, T7, T8.

## Manual steps (you, not the agent)

1. **Clone size (C2).** After T2 and T10, rewrite history to drop the moved files, for example with
   `git filter-repo --invert-paths --paths-from-file <list>`. Alternatively, start a fresh history.
   This is destructive and needs a force-push. Make a full backup first. Sonnet can prepare the path
   list.
2. **GitHub Release (I2).** Create a release and upload the PDF set that T8 produces.
3. **Tracked-file check.** Run `git ls-files .claude reports Code` to see what is public today.

---

## Appendix A: byte-identical duplicates (SHA-256), with a suggested copy to keep

Rule of thumb used: keep the topical home and the clean name; drop "Article " prefixes, "_1" and
"(1)" copies, and pirate-site names; keep `LaTeX/images` copies because decks use them. "Leave" means
the duplication is between a deck image and its source and is harmless.

| Size | Keep | Remove |
|---|---|---|
| 11.39 MB | `YogaShastra/YogaNidra/Audio/TheYogaPodcastYogaNidra.mp3` | `YogaShastra/YogaNidra/TheYogaPodcastYogaNidra.mp3`, `YogaShastra/YogaNidra/Audio/yoga-nidra-yogapoint.mp3` |
| 18.04 MB | `Samskrit/Papers/Classifying Sanskrit Shlokas Using an LSTM-based Model.pdf` | `Samskrit/Papers/Article Classifying Sanskrit Shlokas Using an LSTM-based Model.pdf` |
| 10.56 MB | `YogaShastra/YogaSutra/ArticlesPapers/Book_Science_of_Yoga-Taimni.pdf` | `YogaShastra/YogaSutra/SwamiJ/Book_Science_of_Yoga-Taimni.pdf` |
| 8.65 MB | `IKS/Arthashastra/Kautilya Arthshashtra Vittal.pdf` | `IKS/Arthashastra/Timeless Grand Strategy.pdf` |
| 3.50 MB | `YogaShastra/YogaNidra/Book_YogaNidrabySwamiSatyananda.pdf` | `YogaShastra/YogaNidra/YogaNidrabySwamiSatyanandaSaraswatizliborg-200817-225446.pdf`, `YogaShastra/YogaNidra/Papers/YogaNidrabySwamiSatyanandaSaraswatizliborg-200817-225446.pdf` |
| 5.96 MB | `Samskrit/Classics/NIOS_SanskritSahitya_Book-1.pdf` | `Samskrit/Classics/NIOS_SanskritSahitya_Book-2.pdf` (it is a copy of Book-1) |
| 4.60 MB | `YogaShastra/MHThaker/03_3 srb with 1-2-3-5-6   5 minutes with counting.mp3` | `YogaShastra/MHThaker/07_3 srb with 1-2-3-5-6   5 minutes.mp3` (check which title is right) |
| 3.92 MB | `Samskrit/Grammar/Vyoma_2048907-Shabda_Rupa_Final_09062024.pdf` | `Samskrit/Courses/Shabda_Rupa_Final_09062024.pdf` |
| 2.92 MB | `Samskrit/Grammar/Enjoyable Sanskrit Grammar Volume 2.pdf` | `Samskrit/Grammar/Enjoyable Sanskrit Grammar Series 2.pdf` |
| 2.13 MB | `Samskrit/Papers/A Graph-Based Framework for Structured Prediction Tasks in Sanskrit.pdf` | `Samskrit/Papers/Article A Graph-Based Framework for Structured Prediction Tasks in Sanskrit.pdf` |
| 2.13 MB | `YogaShastra/YogaNidra/Yoga Nidra Steps.pdf` | `YogaShastra/YogaNidra/Papers/Yoga Nidra Steps.pdf` |
| 1.69 MB | `Samskrit/Papers/Thesis_NLP_Techniques_for_Sanskrit_MSR.pdf` | `Samskrit/Papers/NLP_Techniques_for_Sanskrit_MSR_Thesis.pdf` |
| 1.60 MB | `Samskrit/Grammar/Enjoyable Sanskrit Grammar Volume 1.pdf` | `Samskrit/Grammar/Enjoyable Sanskrit Grammar DEVA GOKULAMSanskritGrammar1BasicStructure.pdf` |
| 1.42 MB | `Samskrit/Grammar/Enjoyable Sanskrit Grammar Volume 3.pdf` | `Samskrit/Grammar/Enjoyable Sanskrit Grammar Series 3.pdf` |
| 1.23 MB | `Samskrit/Courses/Arshaavanish/Dhatukosah.pdf` | `Samskrit/Grammar/Enjoyable Sanskrit Grammar Dhatukosah.pdf` |
| 1.21 MB | `YogaShastra/Certification/YCBOfficial/YCB_Guideline_for_YP_-_Version_0.3.pdf` | `YogaShastra/Yogalaya/Guideline_for_YP_-_Version_0.3.pdf` |
| 1.13 MB | `YogaShastra/MHThaker/04 diettary guidance for aspiring yoga students.pdf` | `YogaShastra/MHThaker/04 diettary guidance for aspiring yoga students (1).pdf` |
| 1.05 MB | `Samskrit/Grammar/Book_Sanskrit for Beginners.pdf` | `Samskrit/Grammar/Book_Sanskrit For Begineers.pdf` |
| 0.97 MB | `YogaShastra/YogaSutra/SwamiJ/Swami J_Book_Summary of Practices.pdf` | `YogaShastra/YogaSutra/SwamiJ/Book_Summary of Practices Swami J.pdf` |
| 0.96 MB | `YogaShastra/YogaNidra/Papers/The Origin and Clinical Relevance of Yoga Nidra.pdf` | `YogaShastra/YogaNidra/The Origin and Clinical Relevance of Yoga Nidra.pdf` |
| 0.93 MB | `Samskrit/Grammar/Book_A-Practical_Sanskrit_wikner-rm.pdf` | `Samskrit/Classics/Book_A practicla Sanskrit Introdcutory wikner-rm.pdf` |
| 0.84 MB | `YogaShastra/Certification/YCBOfficial/Syllabus-for-level-3.pdf` | `YogaShastra/Certification/Syllabus-for-level-3.pdf` |
| 0.76 MB | `Samskrit/Grammar/ubcsanskrit_liṅ-optative tense - 2022.pdf` | `Samskrit/Grammar/ubcsanskrit_liṅ-optative tense - 2022_1.pdf` |
| 0.37 MB | `YogaShastra/YogaSutra/SwamiJ/Swami J_Yoga Sutras of Patanjali - Intepretive.pdf` | `.../SwamiJ/Interpretive Yog Sutra Swami J.pdf`, `.../SwamiJ/Yoga Sutras of Patanjali Intepretive Swami J.pdf` |
| 0.72 MB | `.../SwamiJ/Swami J_Yoga Sutras of Patanjali - Basics - Clustered.pdf` | `.../SwamiJ/ClusteredYoga Sutras Swami J.pdf` |
| 0.22 MB | `Samskrit/Papers/Framework for Question-Answering in Sanskrit through Automated Construction of Knowledge Graphs.pdf` | `Samskrit/Papers/Article Framework for Question-Answering ... Knowledge Graphs.pdf`, `Samskrit/Papers/Framework for Question-Answering in Sanskrit .pdf`, `Samskrit/Papers/Framework for Question-Answering in Sanskrit.pdf` |
| 0.59 MB | `IKS/Bhishma_MCKS/MK01 - Sanskrit/SK01 - Sanskrit Bhasha Parichay - Batch Oct 2023-25.pdf` | `IKS/Bhishma_MCKS/SK01 - Sanskrit Bhasha Parichay - Batch Oct 2023-25.pdf` |
| 0.54 MB | `YogaShastra/Certification/YCBOfficial/YCB_Guideline-for-YogaProtocol-Version-0.2.pdf` | `YogaShastra/Certification/Guideline-for-YogaProtocol-Version-0.2.pdf` |
| 0.25 MB | `.../SwamiJ/Swami J_Summary of Practices.pdf` | `.../SwamiJ/Summary of Practices Swami J.pdf`, `.../SwamiJ/Summary of Practices, Witnessing, and Internal Dialogue.pdf` |
| 0.44 MB | `Samskrit/Papers/Vaakkriti Sanskrit Tokenize.pdf` | `Samskrit/Papers/Sanskrit Tokenizer.pdf` |
| 0.42 MB | `.../SwamiJ/Swami J_Yoga Sutras of Patanjali - Rainbow.pdf` | `.../SwamiJ/Rainbow Patanjali Yoga Sutras.pdf` |
| 0.20 MB | `.../SwamiJ/Swami J_Real Yoga Will Not Wreck Your Body.pdf` | `.../SwamiJ/Real Yoga Will Not Wreck Your Body Swami J.pdf`, `.../SwamiJ/Real Yoga Will Not Wreck Your Body.pdf` |
| 0.40 MB | `YogaShastra/Certification/YCBOfficial/Syllabus-for-level-2.pdf` | `YogaShastra/Certification/Syllabus-for-level-2.pdf` |
| 0.39 MB | `Samskrit/LaTeX/subantaruupaNi.tex` | `LaTeX/subantaruupaNi.tex` |
| 0.37 MB | `Samskrit/Grammar/Exercises_Subhashita.pdf` | `Samskrit/Courses/Subhashita.pdf` |
| 0.37 MB | `YogaShastra/Certification/YCBOfficial/Syllabus-for-level-1.pdf` | `YogaShastra/Certification/Syllabus-for-level-1.pdf` |
| 0.35 MB | `Samskrit/Papers/Incorporating Domain Knowledge into Medical NLI using Knowledge Graphs.pdf` | `Samskrit/Papers/Article Incorporating Domain Knowledge into Medical NLI using Knowledge Graphs.pdf` |
| 0.26 MB | `YogaShastra/Shrimath/Shrimath_Yoganidra_Notes_Day1-5.pdf` | `YogaShastra/YogaNidra/Shrimath_Yoganidra_Notes_Day1-5.pdf` (check the YogaNidra README first) |
| 0.26 MB | `Samskrit/Grammar/ubcsanskrit_ṇijanta-causative-2022.pdf` | `Samskrit/Grammar/ubcsanskrit_ṇijanta-causative-2022_1.pdf` |
| 0.25 MB | `Samskrit/Grammar/ubcsanskrit_lṛṅ-conditional tense - 2022.pdf` | `Samskrit/Grammar/ubcsanskrit_lṛṅ-conditional tense - 2022_1.pdf` |
| 0.25 MB | `.../SwamiJ/Swami J_Understanding and Practicing.pdf` | `.../SwamiJ/Understanding and Practicing Swami J.pdf` |
| 0.11 MB | `Samskrit/Classics/Book_Yogasuutra.pdf` | `Samskrit/Classics/Book yogasuutra.pdf` |
| 0.09 MB | `Samskrit/Classics/VishnuSahasraNamStotraBold.pdf` | `Samskrit/vishnusahasranaamam.pdf` |
| 0.07 MB | `Samskrit/MindMap_Sanskrit.pdf` | `Admin/MindMap_Sanskrit.pdf` |
| 0.02 MB | `YogaShastra/YogaSutra/YogSutra_Devnagari_clean.txt` | `YogaShastra/YogaSutra/StudyGroup/YogSutra_Devnagari.txt` |
| 0.01 MB | `Samskrit/LaTeX/shloka.sty` | `LaTeX/shloka.sty` |
| 0.01 MB | `Samskrit/LaTeX/images/uchchar.jpg` | `LaTeX/images/uchchar.jpg` (unused by any deck) |
| 0.03 MB | `Samskrit/LaTeX/images/vedic-resesrve.gif` | `LaTeX/images/vedic-resesrve.gif` (unused by any deck) |
| 0.00 MB | `Samskrit/LaTeX/preamble.tex` | `LaTeX/preamble.tex` |

**NIOS Level-A chapters copied into Yogalaya (12 sets, about 2.6 MB).** Keep
`YogaShastra/NIOSYoga/NIOS_Yoga_(Level-A)_ch-N-final.pdf` and remove
`YogaShastra/Yogalaya/Yoga_(Level-A)_ch-N-final.pdf` for chapters 1 to 12. These go away entirely if
NIOS material is moved out under T2.

**Swami J site PDFs saved twice (16 more sets, about 2 MB).** Keep the `Swami J_`-prefixed copy of
each:

- Self-Awareness Assessment
- The Path
- Introduction
- Narrative Style of all Yoga Sutras
- Reminder Questions and Answers
- Self Study Outline
- Seven Keys to Practice
- Narrative Translation
- Biography Info of Patanjali
- Basics
- Vedic Psychology
- Questions
- Summary

These also go away if `SwamiJ/` is moved out under T2.

**Deck image beside its source (leave).**

- `LaTeX/images/Shrimath_Yoganidra_Mindmap.jpg` and `YogaShastra/Shrimath/...`
- `LaTeX/images/SwamiJ_YogasutraCard.png` and `.../SwamiJ/...`
- `LaTeX/images/SwamiJ_LearningPath.png` and `.../SwamiJ/...`
- `LaTeX/images/SanatanaDharma.jpg` and `IKS/...`
- `LaTeX/images/TheHinduPhilosophy.jpg` and `IKS/...`

Other papers saved twice: `Samskrit/Papers/Sanskrit Segmentation.pdf` (keep) and
`Article Sanskrit Segmentation.pdf` (remove).

Re-run the hash check at execution time. Files can change between this report and the work.
