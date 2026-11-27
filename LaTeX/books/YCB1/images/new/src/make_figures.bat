@echo off
REM Builds every YCB1 line diagram in this folder (XeTeX) and moves each PDF up into images/new/.
REM texify -c removes the auxiliary files. The preamble file is input by the others and is not built itself.
pushd "%~dp0"
for %%f in (*_new.tex) do (
  texify --engine=xetex -cp "%%f"
  if exist "%%~nf.pdf" move /y "%%~nf.pdf" .. >nul
)
popd
