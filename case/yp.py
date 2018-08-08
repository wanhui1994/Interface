# from Interface.common import mysql_pub

import pymysql
import requests

db = pymysql.connect(host='150.138.148.222',port=63307,user='dev',password='dev123456',database='ucdb',charset="utf8")
cursor = db.cursor()
cursor.execute("SELECT USER_ACCOUNT,USER_PHONE,SYS_CODE,CREATE_TIME FROM `uc_user` WHERE  USER_ACCOUNT LIKE 'yp110000003%' OR USER_ACCOUNT LIKE 'yp110000004%' OR USER_ACCOUNT LIKE 'yp110000005%' OR USER_ACCOUNT LIKE 'yp110000006%';")
a = cursor.fetchall()
for i in range(0,len(a)):
    print(a[i][0])
    url="http://ucms.faxuan.net:82/ucds/ucenter/getUserDetail.do"
    parmas={'userAccount':a[i][0],
            'userPhone':a[i][1],
            'sysCode':a[i][2]}
    c=requests.get(url,parmas,timeout=10)
    print(c.url)
    if c.status_code==200:
        print('pass')

