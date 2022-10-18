@echo off

TASKKILL /F /IM "SensorLook V2.0.exe" /T  >nul
timeout /t 1 >nul
cd "C:\SensorLook V2.0\"
start "se" "C:\SensorLook V2.0\SensorLook V2.0.exe"
exit