@echo off

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Run the script
python saimebot.py

REM Deactivate the virtual environment
deactivate