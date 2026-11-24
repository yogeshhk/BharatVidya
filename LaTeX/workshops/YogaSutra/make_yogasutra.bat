@echo off
REM Builds the workshop and, recursively, the seminars folder; each driver is compiled from its own folder.
for /r %%i in (Main_*_YogaSutra*.tex) do (pushd "%%~dpi" & texify --engine=xetex -cp "%%~nxi" & popd)
