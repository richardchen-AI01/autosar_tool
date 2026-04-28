@echo off
REM tools\build_all.cmd - Windows build of bswgen.exe + bswval.exe
REM
REM Usage:
REM   cd D:\dev\autosar_tool
REM   tools\build_all.cmd
REM
REM Outputs land in build\dist\bswgen.exe and build\dist\bswval.exe.
SETLOCAL ENABLEEXTENSIONS

cd /d %~dp0..
if not exist build\dist mkdir build\dist
if not exist build\work mkdir build\work

set PYTHONPATH=core

echo === building bswgen.exe ===
python -m PyInstaller ^
    --workpath build\work\bswgen ^
    --distpath build\dist ^
    --noconfirm ^
    --clean ^
    generator\bswgen.spec
if errorlevel 1 goto fail

echo.
echo === building bswval.exe ===
python -m PyInstaller ^
    --workpath build\work\bswval ^
    --distpath build\dist ^
    --noconfirm ^
    --clean ^
    validator\bswval.spec
if errorlevel 1 goto fail

echo.
echo === artifacts ===
dir build\dist\

echo.
echo === smoke ===
build\dist\bswgen.exe --help

goto :eof

:fail
echo BUILD FAILED
exit /b 1
