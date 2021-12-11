@echo off
echo Installing Pylance Libraries...
timeout /t 1 /nobreak > nul
pip install praw
pip install discord
pip install discord-py-slash-commmand
pip install pickle
pip install requests
pip install nekos.py
pip install pynacl
cls
echo Library Installation Complete! Press any key to exit.
pause > nul
exit /b
