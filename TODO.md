# TODO.md: Repo-Level Index

**Maintained study archive.** It was closed in August 2026 and reopened for a bounded upgrade (see `reports/STATUS.md`
for progress and `reports/upgrade_nontech_14112026.md` for the plan). There is no feature roadmap beyond that plan.
The index below shows what exists and what state it was left in.

Further Yoga Sutra study continues offline, from video playlists and books.

## Open: 2027 Yoga Shastra pillar (workshops for academic, meetup and social settings; no consulting)
Order: read, then build the three workshops. Plan: `D:\Yogesh\GitHub\CAREER_PLAN_2027.md`. One workshop per distinct job, no overlap:
Yoga cert (the practice and teaching of yoga, per the Yoga Certification Board syllabus), Yoga Sutra (the text), Yoga Nidra (the guided practice).
- [ ] Read Vartak's "Yogasutra" first; study Sanskrit from the playlist talks and the story books (offline, author only).
- [ ] Yoga cert workshop = `Main_Workshop_YCB1_*` (the YPI Level 1 deck). Asana frames are wired in; the FAQ frames (`ycb1_theory_faqs`) stay out as a source for question practice. Still to do: re-check the deck against the current Yoga Certification Board syllabus (units, marks, memorised sutras and slokas), and fill the near-empty `ycb1_overview`, `ycb1_practical_application` and `ycb1_practical_fieldexperience` files from the syllabus. Compile once at the end and verify.
- [ ] Yoga Sutra workshop = `Main_Workshop_YogaSutra_*` plus the seminars (complete). After the Vartak reading, adjust only where it changes a point; pick the workshop length for each setting.
- [ ] Yoga Nidra workshop = `Main_Seminar_YogaNidra_*` as it stands (complete). A draft session plan is in `YogaNidra/Workshop_Session_Plan.md`; review and adjust the timings and the safety wording, then deliver once and revise. No new deck, no rename.
- [ ] `Main_Workshop_YogaShastra_*` is retired (not built any more; sources kept). Mine its topic files for the three workshops: the Ashtanga and intro files for Yoga cert, the other teachers' talks and Ayurveda and Sankhya as optional extras; the Yoga Sutra and Yoga Nidra copies already live in their own decks.
- [ ] `CONTENTS.md` still names the retired Yoga Shastra deck; fix when the topic files have been moved into the three workshops.

## Completed

| Area | State | Notes |
|---|---|---|
| Yoga Sutra (`YogaSutra/`, slides in `LaTeX/`) | **Complete.** Slide system final. | A workshop and independent seminars (Intro, Samadhipad, Sadhanapad, Vibhutipad, Kaivalyapad, Overview), each with a matching cheat sheet. Built via `make_yogasutra.bat`; see [`LaTeX/README.md`](LaTeX/README.md). Folder guide and video list: [`YogaSutra/README.md`](YogaSutra/README.md). |
| Yoga Nidra (`YogaNidra/`, slides in `LaTeX/`) | **Complete.** | Beamer deck (Presentation + CheatSheet), detailed practice script, practice notes, and a reading list of research papers. See [`YogaNidra/README.md`](YogaNidra/README.md). |

## Moved out

Everything else that used to be in this repository (Dasbodh, the Sanskrit courses, most of IKS and the other yoga
teachers' material, plus unfinished decks) was moved out or deleted. See [`MOVED_MATERIAL.md`](MOVED_MATERIAL.md).
What is left is only what is original and complete enough to be useful.
