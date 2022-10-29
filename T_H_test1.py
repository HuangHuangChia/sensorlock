#有問題時寫入info_1  沒問題刪掉info_1
import pypyodbc
import pathlib
from datetime import datetime
import os

humidity_range = [30,65]
temperature_range=[18,22]
t=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
t1 = datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
currentpath=str(pathlib.Path().absolute())+"\\"
#path=currentpath+"alert_2022-09-07.rec"

#path=currentpath+"alert_"+t[0:10]+".rec"
#path=currentpath+"Sensor1\\"+t[0:7]+"\\Sensor1_"+t[0:10]+".rec"
#path=currentpath+"Sensor1\\"+t[0:7]+"\\Sensor1_"+t[0:10]+".rec"
path_status=currentpath+"info_1.txt"
path_down=currentpath+"down.txt"
path_down_temp=currentpath+"down_temp.txt"
#f= open(path, mode='r',encoding='UTF-8')
#content=f.readlines()
#f.close()

#db_file = currentpath+'DrData3C.accdb' ## Microsoft Access 檔案名稱
db_file = 'C:\SensorLook V2.0\DrData3C.accdb' ## Microsoft Access 檔案名稱
#db_file = 'C:\\temp1\\DrData3C.accdb' ## Microsoft Access 檔案名稱
user = 'Administrator'
password = 'jack'
connection_string = 'DRIVER={Microsoft Access Driver (*.accdb)};DBQ=%s;UID=%s;PWD=%s' % (db_file, user, password)
conn = pypyodbc.win_connect_mdb(connection_string)

#SQL = 'SELECT Top 1 * FROM [DB] ORDER BY [atime] DESC' 
SQL = 'SELECT Top 1 * FROM [DB] ORDER BY [aDate] Desc,[atime] DESC' 
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

if(os.path.isfile(path_status)): #刪除狀態檔及比較內容檔
    os.remove(path_status)

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
#    info+=str(atime)        
    with open(path_status, mode="w",encoding="utf-8") as f3:
        f3.write(info) 


interval=t1-atime  #if data not update over 900 sec,then make a tag file and restart sensorLock by batch file
if(os.path.isfile(path_down_temp)): #刪除狀態檔及比較內容檔
    os.remove(path_down_temp)
if interval.seconds>900:    
    with open(path_down, mode="a",encoding="utf-8") as f4:
        f4.write(info+"  "+str(atime)+"時間差 "+str(interval.seconds)+"sec\n") 
    with open(path_down_temp, mode="w",encoding="utf-8") as f5:
        f5.write(info+"  "+str(atime)+"時間差 "+str(interval.seconds)+"sec" )
print(info)
#f3 = open(path_status, mode="w",encoding="utf-8")             
#f3.write(info)
#f3.close()

#if humidity>=humidity_range[0] and humidity<=humidity_range[1]:


