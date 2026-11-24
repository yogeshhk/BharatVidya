@echo off
for /r %%i in (Main*OnePager*.tex) do (pushd "%%~dpi" & texify --engine=xetex -cp "%%~nxi" & popd)
