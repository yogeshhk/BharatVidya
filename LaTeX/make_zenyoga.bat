@echo off
for /r %%i in (Main_*ZenYoga*.tex) do texify  --engine=xetex -cp %%i
