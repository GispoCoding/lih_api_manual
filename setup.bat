@echo off
echo 🚀 Location API Business Manual - Windows Setup
echo ==================================================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+ first.
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Run the Python setup script
python setup.py

echo.
echo 💡 Tip: You can also run this setup manually:
echo 1. python -m venv venv
echo 2. venv\Scripts\activate
echo 3. pip install -r requirements.txt
echo 4. mkdocs serve

pause