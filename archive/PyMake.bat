echo off
:start
set /p fn=Filename: 
echo %fn%
pyuic5 -x %cd%\%fn%.ui -o %cd%\%fn%.py

pause