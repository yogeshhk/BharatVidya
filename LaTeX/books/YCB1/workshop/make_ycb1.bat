@echo off
REM Each matching driver is compiled from its own folder (relative paths in the sources depend on it).
for /r %%i in (Main*YCB*.tex) do (pushd "%%~dpi" & texify --engine=xetex -cp "%%~nxi" & popd)
