@echo off
:: Rebuild YCB1_Book_Proposal.pdf: proposal text plus sample pages from the book interior.
:: Compile the book interior first. The shared builder is Publications/Books/_scripts/build_proposal.py.
conda run -n genai python "%~dp0..\..\..\..\..\..\Publications\Books\_scripts\build_proposal.py" --md "%~dp0YCB1_Book_Proposal.md" --book "%~dp0..\..\book\Main_Book_YCB1_interior.pdf" --title "Yoga Certification Board Level 1 Exam Guide: book proposal and sample material" --start "Important Notice" --stop "Guiding Principles for Practitioners"
