cd "C:\SensorLook V2.0"
"C:\SensorLook V2.0\T_H_test1.py"
timeout /t 1 >nul

chcp 65001
IF EXIST "c:\SensorLook V2.0\info_1.txt" (
c:\LineNotify\LineNotify_general.exe "0xQH1k7AuD1CERF9Hy12XNv8MnTOE8V6MwitbfdJHe9" "c:\SensorLook V2.0\info_1.txt"
) ELSE (
ECHO "沒執行linenotify"
)



#c:\LineNotify\LineNotify_general.exe "lj7BBFFqnWuoezANZEd5jD3NJu9dZkJFua3Cn4wIz2q" "c:\SensorLook V2.0\info.txt"