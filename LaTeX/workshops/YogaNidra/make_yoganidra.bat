@echo off
for /r %%i in (Main*YogaNidra*.tex) do (pushd "%%~dpi" & texify --engine=xetex -cp "%%~nxi" & popd)
