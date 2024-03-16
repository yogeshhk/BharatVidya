@echo off
for /r %%i in (Main_*_YogShastra*.tex) do texify  --engine=xetex -cp %%i
