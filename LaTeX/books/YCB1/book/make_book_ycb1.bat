@echo off
:: YCB1 book: YCB Level 1 exam guide. XeTeX is required (Devanagari, Unicode). Run from this folder.
pushd "%~dp0"
echo ===== Covers =====
texify -cp --pdf Main_Book_YCB1_covers.tex
echo ===== Interior =====
texify --engine=xetex -cp Main_Book_YCB1_interior.tex
popd
echo Done.
