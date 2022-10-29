@echo off
cd "C:\Task\SensorLook"
"C:\Task\SensorLook\T_H_test.py"
timeout /t 1 >nul
c:\Task\LineNotify\LineNotify_general.exe "0xQH1k7AuD1CERF9Hy12XNv8MnTOE8V6MwitbfdJHe9" "c:\Task\SensorLook\info.txt"