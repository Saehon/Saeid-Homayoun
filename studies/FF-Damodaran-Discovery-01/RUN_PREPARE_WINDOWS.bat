@echo off
setlocal
cd /d %~dp0

echo ECONOVA-S FF-Damodaran preparation
echo Installing study dependencies for the current Python user...
python -m pip install --user -r requirements-study.txt
if errorlevel 1 goto :fail

echo Running authoritative-source preparation pipeline...
python run_prepare_local.py
if errorlevel 1 goto :fail

echo.
echo SUCCESS.
echo Review file: crosswalk\candidate_crosswalk.csv
echo Do not run the full baseline until the crosswalk is scientifically reviewed.
pause
exit /b 0

:fail
echo.
echo PREPARATION FAILED. Copy the error shown above into ChatGPT for diagnosis.
pause
exit /b 1
