@echo off
for /r %%i in (Main*OnePager*.tex) do texify  --engine=xetex -cp %%i
