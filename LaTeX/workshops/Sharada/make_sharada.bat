@echo off
for /r %%i in (Main*Sharada*.tex) do (pushd "%%~dpi" & texify --engine=xetex -cp "%%~nxi" & popd)
