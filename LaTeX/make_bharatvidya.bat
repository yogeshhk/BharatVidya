@echo off
for /r %%i in (Main_*_BharatVidya*.tex) do texify  --engine=xetex -cp %%i
