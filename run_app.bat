@echo off
echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing dependencies...
python -m pip install --upgrade -r requirements.txt

echo Starting AutoNB...
python app.py
pause
