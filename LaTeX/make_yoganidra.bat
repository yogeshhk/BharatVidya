@echo off
for /r %%i in (Main*YogaNidra*.tex) do texify  --engine=xetex -cp %%i
