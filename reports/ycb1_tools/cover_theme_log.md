## Quantum books: common front cover theme

Theme copied from the Game Theory Workbook covers file (Oswald bold, navy title, rule-dot-rule ornament, spaced caps lines). Accent for all five books: nyupurple RGB(90,35,140). Back covers keep text, lists and photo; headings now sans bold spaced caps, and the preamble matches the model (T1, lmodern, tikz, enumitem, oswald, microtype).

## Per book (front title lines)

- QCNP: old "Quantum Computing for Non-Physicists" with subtitle "From Classical Engineer to Quantum Practitioner". New: QUANTUM / COMPUTING, accent line FOR NON-PHYSICISTS, grey tagline FROM CLASSICAL ENGINEER TO QUANTUM PRACTITIONER, small accent line A BOOK FOR ENGINEERS AND PROGRAMMERS (taken from the back cover reader text).
- QT-01: old "Survey of Quantum Technologies and Applications", line "A Book for the AICTE QT-01 Course". New: SURVEY OF / QUANTUM / TECHNOLOGIES / AND APPLICATIONS, accent AICTE COURSE QT-01, grey MINOR DEGREE IN QUANTUM TECHNOLOGIES, small accent WORKED EXAMPLES. GRADED EXERCISES.
- QT-02: old "Foundations of Quantum Technologies". New: FOUNDATIONS OF / QUANTUM / TECHNOLOGIES, accent AICTE COURSE QT-02, same grey and small lines.
- QT-03: old "Basic Programming Lab". New: BASIC / PROGRAMMING / LAB, accent AICTE COURSE QT-03, same grey and small lines.
- QT-05: old "Introduction to Quantum Computation". New: INTRODUCTION / TO QUANTUM / COMPUTATION, accent AICTE COURSE QT-05, same grey and small lines.

## Notes and things that did not fit

- The grey tagline and small accent lines for the QT books come from existing back-cover wording (reader, exercises); the covers had no tagline before. Change them if you prefer other wording.
- Title sizes were reduced after the first build for TECHNOLOGIES (QT-01, QT-02) and PROGRAMMING (QT-03) to fit the 4.5 in text width.
- QT-02, QT-03 and QT-05 back covers spilled to a third page with the larger headings; fixed by using \small, smaller gaps (0.4em), heading gap 0.1em, top space 0 and the photo at 0.11 of the line width (was 0.15). Body text is unchanged.
- Remaining overfull boxes are 0.4pt or on the back cover only (QCNP footer links line about 8.7pt, QT-02 one bullet about 16pt); none on any front cover.
- No em or en dashes were added.
