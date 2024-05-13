@echo off
for /r %%i in (Main_*_YogaSutra*.tex) do texify  --engine=xetex -cp %%i
