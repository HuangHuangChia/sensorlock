#一律寫入info
import pypyodbc
import pathlib
from datetime import datetime
import os

humidity_range = [30,65]
temperature_range=[18,22]
t=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

currentpath=str(pathlib.Path().absolute())+"\\"
#path=currentpath+"alert_2022-09-07.rec"

#path=currentpath+"alert_"+t[0:10]+".rec"
#path=currentpath+"Sensor1\\"+t[0:7]+"\\Sensor1_"+t[0:10]+".rec"
#path=currentpath+"Sensor1\\"+t[0:7]+"\\Sensor1_"+t[0:10]+".rec"
path_status=currentpath+"info.txt"

#f= open(path, mode='r',encoding='UTF-8')
#content=f.readlines()
#f.close()

db_file = currentpath+'DrData3C.accdb' ## Microsoft Access 檔案名稱

#db_file = 'C:\\temp1\\DrData3C.accdb' ## Microsoft Access 檔案名稱
user = 'Administrator'
password = 'jack'
connection_string = 'DRIVER={Microsoft Access Driver (*.accdb)};DBQ=%s;UID=%s;PWD=%s' % (db_file, user, password)
conn = pypyodbc.win_connect_mdb(connection_string)

SQL = 'SELECT Top 1 * FROM [DB] ORDER BY [atime] DESC'  ## 1010801-1080331為資料表名稱
cur = conn.cursor()
cur.execute(SQL)
list = cur.fetchall()
desc = cur.description
cur.close()
conn.close()
humidity    =float(list[0]['humi'])
temperature =float(list[0]['temp1'])

#humidity   =float(content[-1].split(',')[0])
#temperature=float(content[-1].split(',')[1])
atime=list[0]['atime']
#print(humidity,temperature)
info='機房溫度:%.1f 濕度:%.1f' %(temperature,humidity)

if humidity>=humidity_range[0] and humidity<=humidity_range[1]:
    info+=', 正常 '
else:
    if humidity<humidity_range[0]:
        info+=', 濕度太低 '
    elif humidity>humidity_range[1]:
        info+=', 濕度過高 '
    if temperature<temperature_range[0]:
        info+=', 溫度太低 '
    elif temperature>temperature_range[1]:
        info+=', 溫度過高 '

info+=str(atime)
print(info)

f3 = open(path_status, mode="w",encoding="utf-8")             
f3.write(info)
f3.close()

