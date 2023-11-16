@echo off

echo installing requirements

timeout /t 1 >nul

:: Install requirements
pip install -r requirements.txt

echo Running Data
timeout /t 2 >nul
echo This may take a while...

timeout /t 5 >nul

:: Run Python Program
python Main.py

