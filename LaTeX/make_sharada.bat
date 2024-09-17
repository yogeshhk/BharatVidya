@echo off
for /r %%i in (Main*Sharada*.tex) do texify  --engine=xetex -cp %%i
