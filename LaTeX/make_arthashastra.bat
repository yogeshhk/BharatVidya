@echo off
for /r %%i in (Main_*_ArthaShastra*.tex) do texify  --engine=xetex -cp %%i
