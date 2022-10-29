@echo off
cd "C:\Task\SensorLook"
"C:\Task\SensorLook\T_H_test1.py"
timeout /t 1 >nul

@chcp 65001
IF EXIST "c:\task\SensorLook\info_1.txt" (
c:\Task\LineNotify\LineNotify_general.exe "0xQH1k7AuD1CERF9Hy12XNv8MnTOE8V6MwitbfdJHe9" "c:\task\SensorLook\info_1.txt"
) ELSE (
ECHO "沒執行linenotify"
)

IF EXIST "c:\task\SensorLook\down_temp.txt" (
c:\Task\SensorLook\restartSensorLook.bat
) ELSE (
ECHO "沒執行restart"
)

REM timeout /t 10 >nul
REM c:\LineNotify\LineNotify_general.exe "lj7BBFFqnWuoezANZEd5jD3NJu9dZkJFua3Cn4wIz2q" "c:\SensorLook V2.0\info.txt"