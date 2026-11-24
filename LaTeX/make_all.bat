@echo off
REM Builds every live deck family. The retired Yoga Shastra deck is not built.
call "%~dp0workshops\YCB1\make_ycb1.bat"
call "%~dp0workshops\YogaSutra\make_yogasutra.bat"
call "%~dp0workshops\YogaNidra\make_yoganidra.bat"
call "%~dp0workshops\Sharada\make_sharada.bat"
call "%~dp0onepagers\make_onepagers.bat"
