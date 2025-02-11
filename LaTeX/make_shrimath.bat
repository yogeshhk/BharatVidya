@echo off
for /r %%i in (Main*Shrimath*.tex) do texify  --engine=xetex -cp %%i
