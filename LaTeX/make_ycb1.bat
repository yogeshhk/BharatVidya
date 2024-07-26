@echo off
for /r %%i in (Main*YCB*.tex) do texify  --engine=xetex -cp %%i
