@echo off
for /r %%i in (Main_Workshop_YogaShastra_*.tex) do texify  --engine=xetex -cp %%i
